"""Build the textbook: merge bibliographies and glossaries, run pandoc citeproc (APA 7),
typeset with WeasyPrint to a print-ready A5 PDF (PDF/X-4, no bleed).

Run from anywhere:  python3 textbook/print/build.py
"""
import glob
import html
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
AUTHOR = "Jan Göbel"
YEAR = "2026"
# BoD assigns the ISBN when the book project is started in myBoD; rebuild with BOOK_ISBN=978-3-... set.
ISBN = os.environ.get("BOOK_ISBN", "978-3-0000-0000-0")

PARTS = {
    1: ("Part I", "How AI Works"),
    5: ("Part II", "The Frontier: Technology Trends"),
    8: ("Part III", "Society and Economy"),
    11: ("Part IV", "Risk, Safety and Governance"),
    14: ("Part V", "The Decade Ahead"),
}


def source_hash():
    """Hash of everything that goes into the PDF, so a stale delivery file can be detected."""
    import hashlib
    h = hashlib.sha256()
    files = sorted(glob.glob(os.path.join(CH, "*.md")) + glob.glob(os.path.join(TB, "bib", "*.bib"))
                   + glob.glob(os.path.join(TB, "work", "glossary-ch*.md")) + glob.glob(os.path.join(TB, "figures", "svg", "*.svg"))
                   + [os.path.join(PRINT, n) for n in ("build.py", "srcnotes.lua", "book.css", "pageline.css", "apa.csl")])
    for f in files:
        h.update(os.path.relpath(f, TB).encode())
        h.update(open(f, "rb").read())
    return h.hexdigest()


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
def assemble(only=None):
    parts = []
    pre = os.path.join(CH, "ch00-preface.md")
    if os.path.exists(pre) and only is None:
        parts.append(open(pre, encoding="utf-8").read())
    for n in (range(1, 15) if only is None else [only]):
        f = os.path.join(CH, f"ch{n:02d}.md")
        if not os.path.exists(f):
            print(f"warning: missing {f}", file=sys.stderr)
            continue
        if n in PARTS and only is None:
            p, t = PARTS[n]
            parts.append(f'```{{=html}}\n<section class="part"><p class="part-label">{p}</p><h1 class="part-title">{t}</h1></section>\n```')
        md = open(f, encoding="utf-8").read()
        md = re.sub(r"\]\(figures/", "](../figures/svg/", md)
        md = re.sub(r"[ \t]*\{#tbl:[\w-]+\}[ \t]*$", "", md, flags=re.M)
        parts.append(md)
    gloss, n_terms = merge_glossary()
    if only is None:
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
  <div class="t-rule"></div>
  <p class="t-author">{AUTHOR}</p>
</section>
<section class="copyright">
  <p>Evidence in this book is current to October 2026. Web sources were checked between 20 and 25 October 2026. References follow APA 7 and are numbered. Sources are not cited in the running text: the line at the foot of each page lists the numbers of the sources used on that page.</p>
  <p>Figures drawn for this edition. Set in EB Garamond, with Noto Serif Devanagari for Hindi (both SIL Open Font License).</p>
  <p>© {YEAR} {AUTHOR}. All rights reserved.</p>
  <p>Bibliographic information published by the Deutsche Nationalbibliothek: the Deutsche Nationalbibliothek lists this publication in the Deutsche Nationalbibliografie; detailed bibliographic data are available on the Internet at https://dnb.dnb.de.</p>
  <p>Publisher: BoD · Books on Demand, Überseering 33, 22297 Hamburg, bod@bod.de<br>Print: Libri Plureos GmbH, Friedensallee 273, 22763 Hamburg</p>
  <p>ISBN: {ISBN}</p>
</section>
{toc}
"""


def notes_to_footnotes(body):
    """Turn pandoc's end-of-document notes into inline spans that WeasyPrint floats to the page foot."""
    notes = {}
    m = re.search(r'<(aside|section) id="footnotes"[^>]*>.*?</\1>', body, re.S)
    if m:
        for n in re.finditer(r'<li id="(fn\d+)">(.*?)</li>', m.group(0), re.S):
            inner = re.sub(r'<a href="#fnref\d+"[^>]*>.*?</a>', "", n.group(2), flags=re.S)
            inner = re.sub(r"^\s*<p>|</p>\s*$", "", inner.strip())
            notes[n.group(1)] = inner.strip()
        body = body.replace(m.group(0), "")
    # keep the note call on the same line as the word it follows
    body = re.sub(r'([^\s<>]*)<a href="#(fn\d+)" class="footnote-ref"[^>]*><sup>\d+</sup></a>',
                  lambda x: f'<span class="nobr">{x.group(1)}<span class="fn">{notes.get(x.group(2), "")}</span></span>', body)
    # source notes: "(Smith, 2024; Jones, 2025)" -> "Smith, 2024; Jones, 2025."
    body = re.sub(r'(<span class="srcnote"[^>]*><span class="citation"[^>]*>)\((.*?)\)(</span></span>)',
                  r"\1\2.\3", body, flags=re.S)
    return body


def notes_to_pageline(body):
    """Number the reference list; replace each paragraph note with the numbers of its sources,
    collected by WeasyPrint into one line at the foot of each page; drop years from narrative citations."""
    keys = re.findall(r'<div id="ref-([^"]+)" class="csl-entry"', body)
    num = {k: i + 1 for i, k in enumerate(keys)}
    body = re.sub(r'<div id="ref-([^"]+)" class="csl-entry"([^>]*)>',
                  lambda m: f'<div id="ref-{m.group(1)}" class="csl-entry"{m.group(2)}><span class="refnum">{num[m.group(1)]}</span>', body)
    def nums(m):
        locs = {}
        lm = re.search(r'data-locs="([^"]*)"', m.group(0))
        if lm:
            for part in html.unescape(lm.group(1)).split("|"):
                k, _, loc = part.partition("=")
                if loc:
                    locs.setdefault(k, []).append(loc)
        ks = []
        for k in re.findall(r'data-cites="([^"]+)"', m.group(0)):
            for kk in k.split():
                if kk in num and num[kk] not in [x[0] for x in ks]:
                    ks.append((num[kk], "; ".join(dict.fromkeys(locs.get(kk, [])))))
        return html.escape("|".join(f"{n}~{l}" if l else str(n) for n, l in ks))
    counter = iter(range(1, 10**6))
    body = re.sub(r'<span class="fn"><span class="srcnote"[^>]*>.*?</span></span></span>',
                  lambda m: f'<span class="srcm" id="srcm{next(counter)}" data-nums="{nums(m)}">\u2060</span>',
                  body, flags=re.S)
    # every other citation (narrative mentions, table cells, captions) also joins its page's line
    def mark(m):
        mark.i += 1
        ks = [str(num[k]) for k in m.group(1).split() if k in num]
        return m.group(0) + f'<span class="srcm" id="srcx{mark.i}" data-nums="{"|".join(ks)}">\u2060</span>'
    mark.i = 0
    body = re.sub(r'<span class="citation" data-cites="([^"]+)">.*?</span>', mark, body, flags=re.S)
    # captions name their sources by reference number ("Source: 412, 418."), never by author and year
    def caption_numbers(m):
        found = []
        def to_token(c):
            found.append([num[k] for k in c.group(1).split() if k in num])
            return "\x00"
        cap = re.sub(r'<span class="citation" data-cites="([^"]+)">.*?</span>(?=<span class="srcm")', to_token, m.group(0), flags=re.S)
        # a run of citations ("A; B and C") becomes one sorted list of numbers
        def collapse(r):
            n = r.group(0).count("\x00")
            ks = [k for grp in found[:n] for k in grp]
            del found[:n]
            return f'<span class="refnums">{", ".join(map(str, sorted(set(ks))))}</span>'
        return re.sub(r'\x00(?:(?:<span class="srcm"[^>]*>\u2060</span>)*(?:\s*[;,]\s*|\s+and\s+)\x00)*', collapse, cap)
    body = re.sub(r'<(figcaption|caption)\b.*?</\1>', caption_numbers, body, flags=re.S)
    # in table cells the citation text is dropped (with the space before it): the page's source line carries it
    def table_cells(m):
        return re.sub(r'\s*<span class="citation" data-cites="[^"]+">.*?</span>(?=<span class="srcm")', "", m.group(0), flags=re.S)
    body = re.sub(r'<tbody>.*?</tbody>', table_cells, body, flags=re.S)
    # "Kestin et al. (2025)" -> "Kestin et al."
    def strip_year(m):
        return re.sub(r'\s*\((?:<a [^>]*>)?\d{4}[a-z]?(?:</a>)?(?:,[^()]*)?\)', "", m.group(0))
    body = re.sub(r'<span class="narr"><span class="citation"[^>]*>.*?</span>', strip_year, body, flags=re.S)
    return body


def marker_pages(document):
    """Map each source marker id to the index of the page it was laid out on."""
    where = {}
    for i, page in enumerate(document.pages):
        stack = [page._page_box]
        while stack:
            box = stack.pop()
            el = getattr(box, "element", None)
            if el is not None and el.get("class") == "srcm":
                where.setdefault(el.get("id"), i)
            stack.extend(getattr(box, "children", []) or [])
    return where


def stamp_pagelines(document, doc, pdf_path):
    """Write each page's source numbers into the space between the text block and the page number,
    after layout, so the line can never shift the pagination."""
    from io import BytesIO
    from pypdf import PdfReader, PdfWriter
    from reportlab.lib.utils import simpleSplit
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.pdfgen import canvas

    mm = 72 / 25.4
    nums = dict(re.findall(r'<span class="srcm" id="(src[mx]\d+)" data-nums="([^"]*)">', doc))
    where = marker_pages(document)
    pages = {}
    for mid, pi in where.items():
        for item in html.unescape(nums[mid]).split("|"):
            if not item.strip():
                continue
            n, _, loc = item.partition("~")
            locs = pages.setdefault(pi, {}).setdefault(int(n), [])
            for one in filter(None, (x.strip() for x in loc.split("; "))):
                if one not in locs:
                    locs.append(one)
    pdfmetrics.registerFont(TTFont("EBG", os.path.join(PRINT, "fonts", "EBGaramond-Regular.ttf")))
    pdfmetrics.registerFont(TTFont("EBG-It", os.path.join(PRINT, "fonts", "EBGaramond-RegularItalic.ttf")))
    reader = PdfReader(pdf_path)
    writer = PdfWriter(clone_from=reader)
    W, H = 148 * mm, 210 * mm
    width = 113 * mm
    # one overlay document for all pages, so the font subset is embedded once
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=(W, H), initialFontName="EBG", initialFontSize=7.4)
    for pi in range(len(reader.pages)):
        ns = pages.get(pi)
        if ns:
            x0 = 20 * mm if pi % 2 == 0 else 15 * mm  # right-hand pages have the wider inner margin on the left
            text = " · ".join(f"{n} ({'; '.join(ns[n])})" if ns[n] else str(n) for n in sorted(ns))
            lines = simpleSplit(text, "EBG", 7.4, width - 12 * mm)
            c.setLineWidth(0.4)
            c.line(x0, 17.6 * mm, x0 + 22 * mm, 17.6 * mm)
            y = 15.0 * mm
            for k, ln in enumerate(lines):
                if k == 0:
                    c.setFont("EBG-It", 7.4)
                    c.drawString(x0, y, "Sources")
                    c.setFont("EBG", 7.4)
                c.drawString(x0 + 11 * mm, y, ln)
                y -= 2.9 * mm
        c.showPage()
    c.save()
    buf.seek(0)
    overlay = PdfReader(buf)
    for pi in pages:
        writer.pages[pi].merge_page(overlay.pages[pi])
        writer.pages[pi].compress_content_streams()  # merging leaves the page content uncompressed
    writer.compress_identical_objects(remove_identicals=True, remove_orphans=True)
    writer.pdf_header = b"%PDF-1.6"  # PDF/X-4 needs 1.6; pypdf would otherwise write 1.3
    with open(pdf_path, "wb") as f:
        writer.write(f)
    return len(pages)


def build(only=None, notes=False, out_pdf=OUT_PDF, mode="foot"):
    keys, problems = merge_bib()
    md, n_terms = assemble(only)
    used = {k for k in cited_keys(md) if k in keys}
    missing = sorted(k for k in cited_keys(md) if k not in keys and not k.startswith("fig:") and "." not in k)
    if only is None:
        open(OUT_MD, "w", encoding="utf-8").write(md)
    filters = ["--lua-filter", os.path.join(PRINT, "srcnotes.lua")] if notes else []
    env = dict(os.environ, SRCMODE=mode)
    html_body = subprocess.run(
        ["pandoc", "-f", "markdown-tex_math_dollars", "-t", "html5", *filters, "--citeproc", "--section-divs",
         "--bibliography", os.path.join(PRINT, "all.bib"), "--csl", os.path.join(PRINT, "apa.csl"),
         "--metadata", "link-citations=true", "--wrap=none"],
        input=md, capture_output=True, text=True, env=env,
    )
    if html_body.returncode:
        print(html_body.stderr)
        sys.exit(1)
    body = html_body.stdout
    if notes:
        body = notes_to_footnotes(body)
        if mode == "pageline":
            body = notes_to_pageline(body)
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

    # tables with five or more columns get a tighter setting on the A5 page
    body = re.sub(r"<table>(.*?)</table>",
                  lambda m: ('<table class="wide">' if len(re.findall(r"<th\b", m.group(1).split("</thead>")[0])) >= 5 else "<table>") + m.group(1) + "</table>",
                  body, flags=re.S)
    css = open(os.path.join(PRINT, "book.css"), encoding="utf-8").read()
    if notes:
        css += open(os.path.join(PRINT, "notes.css" if mode == "foot" else "pageline.css"), encoding="utf-8").read()
    doc = (f'<!doctype html><html lang="en-GB"><head><meta charset="utf-8"><title>{TITLE}</title>'
           f'<meta name="author" content="{AUTHOR}"><style>{css}</style></head><body>'
           f'{front_matter("".join(toc)) if only is None else ""}{body}</body></html>')
    open(OUT_HTML, "w", encoding="utf-8").write(doc)

    from weasyprint import HTML

    document = HTML(OUT_HTML, base_url=PRINT).render()
    if len(document.pages) % 2:
        doc = doc.replace("</body>", '<div class="endblank"></div></body>')
        open(OUT_HTML, "w", encoding="utf-8").write(doc)
        document = HTML(OUT_HTML, base_url=PRINT).render()
    document.write_pdf(out_pdf, pdf_variant="pdf/x-4", output_intent="srgb")
    if notes and mode == "pageline":
        n = stamp_pagelines(document, doc, out_pdf)
        print(f"source lines stamped on {n} pages")
    if out_pdf == OUT_PDF and only is None:
        with open(os.path.join(TB, "delivery", "BUILD-INFO.txt"), "w", encoding="utf-8") as f:
            f.write(f"sources_sha256: {source_hash()}\npages: {len(document.pages)}\n")
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    print(f"{out_pdf}: {len(document.pages)} pages; ~{words} words incl. references")
    print(f"bib entries: {len(keys)}; cited: {len(used)}; glossary terms: {n_terms}")
    for p in problems:
        print("BIB:", p)
    if missing:
        print("MISSING KEYS:", ", ".join(missing))
    for w in warn[:30]:
        print("PANDOC:", w)


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", type=int, help="build a single chapter (sample)")
    ap.add_argument("--notes", action="store_true", help="per-paragraph source notes at the page foot")
    ap.add_argument("--pageline", action="store_true", help="one line of source numbers at the page foot (default)")
    ap.add_argument("--inline", action="store_true", help="old style: APA author-date citations in the text")
    ap.add_argument("--out", default=OUT_PDF)
    a = ap.parse_args()
    if a.inline:
        build(a.only, False, a.out)
    elif a.notes:
        build(a.only, True, a.out, "foot")
    else:
        build(a.only, True, a.out, "pageline")
