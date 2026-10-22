"""Build the textbook: merge bibliographies and glossaries, run pandoc citeproc (APA 7),
typeset with WeasyPrint to a print-ready A5 PDF (PDF/X-4, no bleed).

Run from anywhere:  python3 textbook/print/build.py
"""
import glob
import os
import re
import subprocess
import sys

TB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRINT = os.path.join(TB, "print")
CH = os.path.join(TB, "chapters")
OUT_PDF = os.path.join(TB, "delivery", "understanding-ai_A5_interior.pdf")
OUT_HTML = os.path.join(PRINT, "book.html")
OUT_MD = os.path.join(TB, "delivery", "understanding-ai.md")

TITLE = "Understanding AI"
SUBTITLE = "Technology, Trends and the Decade Ahead"
TAG = "A Course Text"
AUTHOR = "Jan Göbel"
YEAR = "2026"

PARTS = {
    1: ("Part I", "How AI Works"),
    5: ("Part II", "The Frontier: Technology Trends"),
    8: ("Part III", "Society and Economy"),
    11: ("Part IV", "Risk, Safety and Governance"),
    14: ("Part V", "The Decade Ahead"),
}


# ---------------------------------------------------------------- bibliography
def merge_bib():
    entries, order, problems = {}, [], []
    for f in sorted(glob.glob(os.path.join(TB, "bib", "*.bib"))):
        text = open(f, encoding="utf-8").read()
        for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", text, re.S):
            key = m.group(2)
            block = m.group(0)
            if key in entries:
                # The same source cited in several chapters: keep the most complete entry
                # (fact-checkers added DOIs, pages and published venues chapter by chapter).
                if len(re.sub(r"\s+", "", block)) > len(re.sub(r"\s+", "", entries[key])):
                    entries[key] = block
                continue
            entries[key] = block
            order.append(key)
    with open(os.path.join(PRINT, "all.bib"), "w", encoding="utf-8") as out:
        out.write("\n\n".join(entries[k] for k in order) + "\n")
    return set(entries), problems


# ---------------------------------------------------------------- glossary
def merge_glossary():
    terms = {}
    for f in sorted(glob.glob(os.path.join(TB, "work", "glossary-ch*.md"))):
        for line in open(f, encoding="utf-8"):
            m = re.match(r"\s*[-*]?\s*\*\*(.+?)\*\*\s*[:—-]\s*(.+)", line)
            if not m:
                continue
            term, definition = m.group(1).strip(), m.group(2).strip()
            k = term.lower()
            if k not in terms or len(definition) > len(terms[k][1]):
                terms[k] = (term, definition)
    lines = ["# Glossary {.unnumbered .glossary}", ""]
    for k in sorted(terms, key=lambda s: re.sub(r"[^a-z0-9 ]", "", s)):
        t, d = terms[k]
        lines.append(f"**{t}**: {d}\n")
    return "\n".join(lines), len(terms)


# ---------------------------------------------------------------- assemble
def assemble():
    parts = []
    pre = os.path.join(CH, "ch00-preface.md")
    if os.path.exists(pre):
        parts.append(open(pre, encoding="utf-8").read())
    for n in range(1, 15):
        f = os.path.join(CH, f"ch{n:02d}.md")
        if not os.path.exists(f):
            print(f"warning: missing {f}", file=sys.stderr)
            continue
        if n in PARTS:
            p, t = PARTS[n]
            parts.append(f'```{{=html}}\n<section class="part"><p class="part-label">{p}</p><h1 class="part-title">{t}</h1></section>\n```')
        md = open(f, encoding="utf-8").read()
        md = re.sub(r"\]\(figures/", "](../figures/svg/", md)
        md = re.sub(r"[ \t]*\{#tbl:[\w-]+\}[ \t]*$", "", md, flags=re.M)
        parts.append(md)
    gloss, n_terms = merge_glossary()
    parts.append(gloss)
    parts.append("# References {.unnumbered .references-chapter}\n\n::: {#refs}\n:::\n")
    return "\n\n".join(parts), n_terms


def cited_keys(md):
    return set(re.findall(r"@([A-Za-z0-9_:\-]+[A-Za-z0-9])", md))


def front_matter(toc):
    return f"""
<section class="halftitle"><p>{TITLE}</p></section>
<section class="titlepage">
  <p class="t-title">{TITLE}</p>
  <p class="t-sub">{SUBTITLE}</p>
  <p class="t-tag">{TAG}</p>
  <div class="t-rule"></div>
  <p class="t-author">{AUTHOR}</p>
</section>
<section class="copyright">
  <p>© {YEAR} {AUTHOR}. All rights reserved.</p>
  <p>Evidence in this book is current to October 2026. Web sources were checked between October 20 and 22, 2026. Citations follow APA 7; full references are at the end of the book.</p>
  <p>Figures drawn for this edition. Set in EB Garamond (SIL Open Font License).</p>
  <p>ISBN: [to be assigned]<br>Publisher and printer: [imprint details]</p>
</section>
{toc}
"""


def build():
    keys, problems = merge_bib()
    md, n_terms = assemble()
    used = {k for k in cited_keys(md) if k in keys}
    missing = sorted(k for k in cited_keys(md) if k not in keys and not k.startswith("fig:") and "." not in k)
    open(OUT_MD, "w", encoding="utf-8").write(md)
    html_body = subprocess.run(
        ["pandoc", "-f", "markdown-tex_math_dollars", "-t", "html5", "--citeproc", "--section-divs",
         "--bibliography", os.path.join(PRINT, "all.bib"), "--csl", os.path.join(PRINT, "apa.csl"),
         "--metadata", "link-citations=true", "--wrap=none"],
        input=md, capture_output=True, text=True,
    )
    if html_body.returncode:
        print(html_body.stderr)
        sys.exit(1)
    body = html_body.stdout
    warn = [l for l in html_body.stderr.splitlines() if l.strip()]

    # table of contents from h1s
    toc = ['<section class="toc"><h1 class="toc-title">Contents</h1><ol>']
    for m in re.finditer(r'<section id="([^"]+)" class="(level1[^"]*)">\s*<h1[^>]*>(.*?)</h1>|<section class="part"><p class="part-label">(.*?)</p><h1 class="part-title">(.*?)</h1>', body):
        if m.group(4):
            toc.append(f'<li class="toc-part">{m.group(4)}: {m.group(5)}</li>')
        else:
            title = re.sub(r"<[^>]+>", "", m.group(3))
            toc.append(f'<li class="toc-entry"><a href="#{m.group(1)}">{title}</a></li>')
    toc.append("</ol></section>")

    # chapter labels: "Chapter 3: Title" -> label + title
    def chap(m):
        attrs, label, title = m.group(1), m.group(2), m.group(3)
        if label == "Preface":
            return f'<h1{attrs}><span class="ch-title">Preface</span></h1>'
        return f'<h1{attrs}><span class="ch-label">{label}</span><span class="ch-title">{title}</span></h1>'
    body = re.sub(r"<h1([^>]*)>(Chapter \d+|Preface)\s*:?\s*(.*?)</h1>", chap, body)

    css = open(os.path.join(PRINT, "book.css"), encoding="utf-8").read()
    doc = (f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>{TITLE}</title>'
           f'<meta name="author" content="{AUTHOR}"><style>{css}</style></head><body>'
           f'{front_matter("".join(toc))}{body}</body></html>')
    open(OUT_HTML, "w", encoding="utf-8").write(doc)

    from weasyprint import HTML

    document = HTML(OUT_HTML, base_url=PRINT).render()
    if len(document.pages) % 2:
        doc = doc.replace("</body>", '<div class="endblank"></div></body>')
        open(OUT_HTML, "w", encoding="utf-8").write(doc)
        document = HTML(OUT_HTML, base_url=PRINT).render()
    document.write_pdf(OUT_PDF, pdf_variant="pdf/x-4", output_intent="srgb")
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    print(f"{OUT_PDF}: {len(document.pages)} pages; ~{words} words incl. references")
    print(f"bib entries: {len(keys)}; cited: {len(used)}; glossary terms: {n_terms}")
    for p in problems:
        print("BIB:", p)
    if missing:
        print("MISSING KEYS:", ", ".join(missing))
    for w in warn[:30]:
        print("PANDOC:", w)


if __name__ == "__main__":
    build()
