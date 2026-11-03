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
MAX_PAGES = 8  # more than this and an entry stops helping; keep the earliest, densest pages


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
        body = re.sub(r"(\w)[‐-]\n\s*(\w)", r"\1\2", body)
        pages[num] = re.sub(r"\s+", " ", body)
    return pages


def main_range(pages):
    """Pages of the preface and the chapters: from the preface heading to the glossary heading."""
    start = min(n for n, t in pages.items() if t.strip().startswith("Preface") or " Preface " in t[:80])
    end = min(n for n, t in pages.items() if n > start + 50 and t.strip().startswith("Glossary"))
    return range(start, end)


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
    lines = ["# Index {.unnumbered .index}", ""]
    rows = []
    for term, pats in entries():
        regs = [pattern(p) for p in pats]
        hits = []
        for n in rng:
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
    rows.sort(key=lambda r: re.sub(r"[^a-z0-9 ]", "", r[0].lower()))
    letter = None
    for term, ns in rows:
        L = re.sub(r"[^a-z0-9]", "", term.lower())[:1].upper()
        L = "0–9" if L.isdigit() else L
        if L != letter:
            lines.append(f"\n## {L} {{.unnumbered}}\n")
            letter = L
        lines.append(f"{term}, {', '.join(map(str, ns))}\n")
    open(OUT, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"index: {len(rows)} entries -> {OUT}")


if __name__ == "__main__":
    build()
