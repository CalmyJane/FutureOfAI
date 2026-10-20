# Export: When Everything Goes Right
Author: **not yet supplied** (required before export). Language: en-GB. Source: manuscript/chapters/chapter-00.md to chapter-19.md (20 files); export copies with separate Part title pages in work/export/chapters/.

## Status
- pandoc: 3.1.3 (found)
- PDF engine: none working (checked: xelatex, lualatex, tectonic, typst, weasyprint, pdflatex)
- delivery/when-everything-goes-right.md: the proofread manuscript (created)
- delivery/when-everything-goes-right.epub: not created, because the author name is missing (Book Genesis never invents one)
- delivery/when-everything-goes-right.pdf: not created, because no PDF engine is installed
- delivery/when-everything-goes-right.docx: not created yet (available on request once the author name is set)

## Commands (run from the book folder, after putting the author's name into work/export/metadata.yaml)
EPUB:
pandoc --metadata-file=work/export/metadata.yaml --css=work/export/ebook.css --toc -o delivery/when-everything-goes-right.epub work/export/chapters/chapter-00.md work/export/chapters/chapter-01-part.md work/export/chapters/chapter-01.md work/export/chapters/chapter-02.md work/export/chapters/chapter-03.md work/export/chapters/chapter-04.md work/export/chapters/chapter-05-part.md work/export/chapters/chapter-05.md work/export/chapters/chapter-06.md work/export/chapters/chapter-07.md work/export/chapters/chapter-08-part.md work/export/chapters/chapter-08.md work/export/chapters/chapter-09.md work/export/chapters/chapter-10.md work/export/chapters/chapter-11.md work/export/chapters/chapter-12-part.md work/export/chapters/chapter-12.md work/export/chapters/chapter-13.md work/export/chapters/chapter-14.md work/export/chapters/chapter-15-part.md work/export/chapters/chapter-15.md work/export/chapters/chapter-16.md work/export/chapters/chapter-17.md work/export/chapters/chapter-18.md work/export/chapters/chapter-19.md 

DOCX:
pandoc --metadata-file=work/export/metadata.yaml --toc -o delivery/when-everything-goes-right.docx work/export/chapters/chapter-00.md work/export/chapters/chapter-01-part.md work/export/chapters/chapter-01.md work/export/chapters/chapter-02.md work/export/chapters/chapter-03.md work/export/chapters/chapter-04.md work/export/chapters/chapter-05-part.md work/export/chapters/chapter-05.md work/export/chapters/chapter-06.md work/export/chapters/chapter-07.md work/export/chapters/chapter-08-part.md work/export/chapters/chapter-08.md work/export/chapters/chapter-09.md work/export/chapters/chapter-10.md work/export/chapters/chapter-11.md work/export/chapters/chapter-12-part.md work/export/chapters/chapter-12.md work/export/chapters/chapter-13.md work/export/chapters/chapter-14.md work/export/chapters/chapter-15-part.md work/export/chapters/chapter-15.md work/export/chapters/chapter-16.md work/export/chapters/chapter-17.md work/export/chapters/chapter-18.md work/export/chapters/chapter-19.md 

PDF (after installing a PDF engine, e.g. xelatex):
pandoc --metadata-file=work/export/metadata.yaml --toc --pdf-engine=xelatex -V documentclass=book -V "geometry:paperwidth=6in,paperheight=9in,inner=1in,outer=0.75in,top=0.75in,bottom=0.875in" -o delivery/when-everything-goes-right.pdf work/export/chapters/chapter-00.md work/export/chapters/chapter-01-part.md work/export/chapters/chapter-01.md work/export/chapters/chapter-02.md work/export/chapters/chapter-03.md work/export/chapters/chapter-04.md work/export/chapters/chapter-05-part.md work/export/chapters/chapter-05.md work/export/chapters/chapter-06.md work/export/chapters/chapter-07.md work/export/chapters/chapter-08-part.md work/export/chapters/chapter-08.md work/export/chapters/chapter-09.md work/export/chapters/chapter-10.md work/export/chapters/chapter-11.md work/export/chapters/chapter-12-part.md work/export/chapters/chapter-12.md work/export/chapters/chapter-13.md work/export/chapters/chapter-14.md work/export/chapters/chapter-15-part.md work/export/chapters/chapter-15.md work/export/chapters/chapter-16.md work/export/chapters/chapter-17.md work/export/chapters/chapter-18.md work/export/chapters/chapter-19.md 

## If you choose to install what is missing
- pandoc: https://pandoc.org/installing.html
- a PDF engine: a TeX distribution (TeX Live, MiKTeX or MacTeX) provides xelatex and lualatex

## Before you publish
- Author name, bio and copyright line.
- Decide the title (the hook test recommends "Two Hundred Million Acts of Loyalty").
- Verify the comps and every Notes URL (most were checked on 2026-10-20; some rest on secondary sources, flagged in work/evidence-chapter-NN.md).
- A human editor's read; a permissions check for quoted phrases.
- Check the appendix table on small screens.
