# Export: When Everything Goes Right
Author: Jan Göbel. Language: en-GB. Source: manuscript/chapters/chapter-00.md to chapter-19.md (20 files).

## Status
- **delivery/when-everything-goes-right_A5_interior.pdf**: print-ready **book interior** for print-on-demand. 256 pages (an even count), A5 trim 148 × 210 mm, no bleed (no element reaches the page edge), PDF/X-4 with an sRGB output intent, all fonts embedded (EB Garamond, SIL OFL), 20 vector line illustrations in black and grey (suits a black-and-white interior). Chapters open on right-hand pages; running heads; page numbers.
- delivery/when-everything-goes-right.md: the proofread manuscript (Markdown).
- Cover: **not included**. A POD cover is a separate file whose spine width depends on page count and paper (256 pages → roughly 15–18 mm, depending on paper). Get it from the printer's cover calculator.

## Rebuild (from the book folder)
    pip install weasyprint           # tested with WeasyPrint 70.0
    python3 print/make_illustrations.py   # regenerates print/illustrations/*.svg
    python3 print/build_pdf.py            # writes the interior PDF
Layout lives in print/book.css (page size, margins: inner 20 mm, outer 15 mm, top 18 mm, bottom 20 mm; type 10.5 pt EB Garamond).

## Before you upload
- Replace the placeholders on the copyright page (ISBN, imprint/publisher; BoD and similar services often assign the ISBN and supply their imprint line).
- Check your platform's specs: BoD, KDP and others accept A5 interiors without bleed; some require PDF/X-3 or X-4 (this file is X-4).
- Many platforms ask you to disclose AI-assisted content when you upload.
- Order a proof copy before release.
