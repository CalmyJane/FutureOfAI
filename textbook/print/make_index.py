"""Build the back-of-book index from the laid-out PDF.

Entries are the glossary terms plus the people, organisations, models and laws the book names
most often (index_entities.txt, one entry per line, optional "Heading | pattern | pattern").
Each entry lists the printed pages of the main text (preface to the end of Chapter 14) on which
it occurs; the page where the glossary defines it is not counted.

Run after a full build, then build again: the index is appended after the references, so the
pages it points to do not move.   python3 textbook/print/make_index.py
"""
import glob
import os
import re
import subprocess

PRINT = os.path.dirname(os.path.abspath(__file__))
TB = os.path.dirname(PRINT)
PDF = os.path.join(TB, "delivery", "understanding-ai_A5_interior.pdf")
OUT = os.path.join(PRINT, "index.md")
MAX_PAGES = 8
# glossary terms whose word also has everyday or unrelated senses: count them only in the chapters
# where the technical sense is used; None drops the entry
CHAPTERS_ONLY = {
    "bias (in a neuron)": {2},
    "adam": {2},
    "epoch": {2},
    "momentum": {2},
    "circuit": {3, 12},
    "feature": {2, 3, 12},
    "environment (reinforcement learning)": {3, 4, 5},
    "resolution": None,
}
# duplicate entries become cross-references
SEE = {"auc": "area under the curve (AUC)", "time horizon (50%)": "50% time horizon", "time horizon": "50% time horizon"}
NOTE = ("For names and terms that occur very often, the index lists the first page and the pages with the "
        "most mentions.")  # more than this and an entry stops helping; keep the earliest, densest pages


def page_texts():
    raw = subprocess.run(["pdftotext", "-layout", PDF, "-"], capture_output=True, text=True).stdout
    pages = {}
    for i, txt in enumerate(raw.split("\f")):
        lines = [l for l in txt.splitlines() if l.strip()]
        if not lines:
            continue
        m = re.fullmatch(r"\s*(\d+)\s*", lines[-1])
        num = int(m.group(1)) if m else i + 1
        body = "\n".join(l for l in lines[:-1] if not l.lstrip().startswith("Sources "))
        # undo end-of-line hyphenation so split words are found
        body = re.sub(r"(\w)‐\n\s*(\w)", r"\1\2", body)   # break hyphen (U+2010): join
        body = re.sub(r"(\w)-\n\s*(\w)", r"\1-\2", body)   # real hyphen at a line end: keep it
        pages[num] = re.sub(r"\s+", " ", body)
    return pages


def main_range(pages):
    """Pages of the preface and the chapters: from the preface heading to the glossary heading."""
    # the first page that begins with "Preface" (the Contents page mentions it too, but begins with "Contents")
    start = min(n for n, t in pages.items() if t.strip().startswith("Preface"))
    end = min(n for n, t in pages.items() if n > start + 50 and t.strip().startswith("Glossary"))
    return range(start, end)


def chapter_of(pages, rng):
    """Map each main-text page to its chapter number (0 for the preface), from the 'Chapter N' opening pages."""
    out, cur = {}, 0
    for n in rng:
        m = re.match(r"\s*Chapter (\d+)\b", pages.get(n, ""))
        if m:
            cur = int(m.group(1))
        out[n] = cur
    return out


def entries():
    out = {}
    for f in sorted(glob.glob(os.path.join(TB, "work", "glossary-ch*.md"))):
        for line in open(f, encoding="utf-8"):
            m = re.match(r"\s*[-*]?\s*\*\*(.+?)\*\*\s*[:—-]", line)
            if not m:
                continue
            term = m.group(1).strip()
            head = re.sub(r"\s*\(.*?\)\s*$", "", term)  # "byte-pair encoding (BPE)" -> heading keeps the full term
            pats = [head]
            abbr = re.search(r"\(([A-Z][A-Za-z0-9\-]+)\)", term)
            if abbr:
                pats.append(abbr.group(1))
            out.setdefault(term.lower(), (term, pats))
    ent = os.path.join(PRINT, "index_entities.txt")
    if os.path.exists(ent):
        for line in open(ent, encoding="utf-8"):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split("|")]
            out.setdefault(parts[0].lower(), (parts[0], parts[1:] or [parts[0]]))
    return out.values()


def pattern(p):
    case = p[0].isupper() or any(c.isupper() for c in p[1:])
    words = [re.escape(w) for w in p.split()]
    body = r"[\s‐-]+".join(words)
    plural = "" if case else r"(?:s|es)?"
    return re.compile(r"(?<![\w-])" + body + plural + r"(?![\w-])", 0 if case else re.I)


def build():
    pages = page_texts()
    rng = main_range(pages)
    chap = chapter_of(pages, rng)
    lines = ["# Index {.unnumbered .index}", "", f"*{NOTE}*", ""]
    rows = []
    see_rows = []
    for term, pats in entries():
        key = term.lower()
        if key in SEE:
            see_rows.append((term, SEE[key]))
            continue
        if key in CHAPTERS_ONLY and CHAPTERS_ONLY[key] is None:
            continue
        regs = [pattern(p) for p in pats]
        hits = []
        for n in rng:
            if key in CHAPTERS_ONLY and chap.get(n) not in CHAPTERS_ONLY[key]:
                continue
            t = pages.get(n, "")
            c = sum(len(r.findall(t)) for r in regs)
            if c:
                hits.append((n, c))
        if not hits:
            continue
        if len(hits) > MAX_PAGES:
            first = hits[0]
            dense = sorted(hits[1:], key=lambda h: -h[1])[: MAX_PAGES - 1]
            hits = sorted([first] + dense)
        rows.append((term, [n for n, _ in hits]))
    rows += [(t, "see " + target) for t, target in see_rows]
    def sortkey(t):
        return re.sub(r"[^a-z0-9 ]", "", t.lower().replace("τ", "tau"))
    rows.sort(key=lambda r: sortkey(r[0]))
    letter = None
    for term, ns in rows:
        L = sortkey(term).replace(" ", "")[:1].upper()
        L = "0–9" if L.isdigit() else L
        if L != letter:
            lines.append(f"\n## {L} {{.unnumbered}}\n")
            letter = L
        if isinstance(ns, str):
            lines.append(f"{term}, *{ns}*\n")
        else:
            lines.append(f"{term}, {', '.join(map(str, ns))}\n")
    open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"index: {len(rows)} entries -> {OUT}")


if __name__ == "__main__":
    build()
