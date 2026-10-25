"""Build the print-ready A5 interior PDF (148 x 210 mm, no bleed) with WeasyPrint.

Run from the book folder:  python3 print/build_pdf.py
Output: delivery/when-everything-goes-right_A5_interior.pdf
"""
import glob
import html
import os
import re
import subprocess

BOOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRINT = os.path.join(BOOK, "print")
CHAPTERS = sorted(glob.glob(os.path.join(BOOK, "manuscript", "chapters", "chapter-*.md")))
OUT_HTML = os.path.join(PRINT, "book.html")
OUT_PDF = os.path.join(BOOK, "delivery", "when-everything-goes-right_A5_interior.pdf")

TITLE = "When Everything Goes Right"
SUBTITLE = "The Hidden Risks of Successful AI, and the Institutions We Must Invent Before 2036"
AUTHOR = "Jan Göbel"
YEAR = "2026"


def md_to_html(md):
    return subprocess.run(
        ["pandoc", "-f", "markdown-auto_identifiers", "-t", "html5", "--wrap=none"],
        input=md, capture_output=True, text=True, check=True,
    ).stdout


def split_heading(h1):
    """'Chapter 3: The M-1 Criterion' -> ('Chapter 3', 'The M-1 Criterion')."""
    m = re.match(r"(Prologue|Epilogue|Appendix|Chapter \d+):\s*(.+)", h1)
    return (m.group(1), m.group(2)) if m else ("", h1)


def chapter_html(path, idx):
    md = open(path, encoding="utf-8").read()
    part = None
    m = re.match(r"## (Part [^:]+):\s*([^\n]+)\n+", md)
    if m:
        part = (m.group(1), m.group(2))
        md = md[m.end():]
    m = re.match(r"# ([^\n]+)\n+", md)
    label, title = split_heading(m.group(1))
    body = md_to_html(md[m.end():])
    # dateline paragraphs of the 2036 scenes
    body = re.sub(r"<p><em>((?:20\d\d|1\d\d\d)[^<]*·[^<]*)</em></p>", r'<p class="dateline">\1</p>', body)
    # Notes section
    body = body.replace("<h2>Notes</h2>", '<section class="notes"><h2>Notes</h2>', 1)
    if '<section class="notes">' in body:
        body += "</section>"
    out = ""
    if part:
        out += (
            f'<section class="part"><p class="part-label">{part[0]}</p>'
            f'<h1 class="part-title">{html.escape(part[1])}</h1></section>'
        )
    cls = "chapter appendix" if label == "Appendix" else "chapter"
    out += (
        f'<section class="{cls}" id="ch{idx:02d}">'
        f'<img class="opener" src="illustrations/ill-{idx:02d}.svg" alt="">'
        f'<p class="ch-label">{label}</p>'
        f'<h1 class="ch-title">{html.escape(title)}</h1>'
        f"{body}</section>"
    )
    toc = (part, label, title, idx)
    return out, toc


def build():
    parts, tocs = [], []
    for i, p in enumerate(CHAPTERS):
        h, t = chapter_html(p, i)
        parts.append(h)
        tocs.append(t)

    toc_html = '<section class="toc"><h1 class="toc-title">Contents</h1><ol>'
    for part, label, title, idx in tocs:
        if part:
            toc_html += f'<li class="toc-part">{part[0]}: {html.escape(part[1])}</li>'
        name = f"{label}: {title}" if label.startswith("Chapter") else title
        if label in ("Prologue", "Epilogue", "Appendix"):
            name = f"{label}: {title}"
        toc_html += f'<li class="toc-entry"><a href="#ch{idx:02d}">{html.escape(name)}</a></li>'
    toc_html += "</ol></section>"

    front = f"""
<section class="halftitle"><p>{TITLE}</p></section>
<section class="titlepage">
  <p class="t-title">{TITLE}</p>
  <p class="t-sub">{SUBTITLE}</p>
  <div class="t-orn"></div>
  <p class="t-author">{AUTHOR}</p>
</section>
<section class="copyright">
  <p>© {YEAR} {AUTHOR}. All rights reserved.</p>
  <p>The scenes set in 2036, and the people in them, are invented. Any resemblance to real persons is coincidental. Statements about the present are sourced in the notes at the end of each chapter; web sources were checked in October 2026.</p>
  <p>Illustrations made for this edition.<br>Set in EB Garamond (SIL Open Font License).</p>
  <p>ISBN: [to be assigned]<br>Publisher and printer: [imprint details]</p>
</section>
{toc_html}
"""
    css = open(os.path.join(PRINT, "book.css"), encoding="utf-8").read()
    doc = f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<title>{TITLE}</title><meta name="author" content="{AUTHOR}">
<style>{css}</style></head><body>{front}{''.join(parts)}</body></html>"""
    open(OUT_HTML, "w", encoding="utf-8").write(doc)

    from weasyprint import HTML

    document = HTML(OUT_HTML, base_url=PRINT).render()
    n = len(document.pages)
    if n % 2:  # print-on-demand needs an even page count
        doc = doc.replace("</body>", '<div class="endblank"></div></body>')
        open(OUT_HTML, "w", encoding="utf-8").write(doc)
        document = HTML(OUT_HTML, base_url=PRINT).render()
    document.write_pdf(OUT_PDF, pdf_variant="pdf/x-4", output_intent="srgb")
    print(f"{OUT_PDF}: {len(document.pages)} pages")


if __name__ == "__main__":
    build()
