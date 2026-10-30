# Understanding AI: Technology, Trends and the Decade Ahead

Author: Jan Göbel · Evidence current to October 2026 (web sources checked 20–25 October 2026, the last passes with web search)

## Files
- `understanding-ai_A5_interior.pdf`: the print-ready interior (Buchblock) for BoD. A5 (148 × 210 mm, BoD format 14,8 × 21 cm), no bleed (nothing runs to the page edge), PDF/X-4 (PDF 1.6) with sRGB output intent, 590 pages, all fonts embedded, no transparency, greyscale throughout (upload as a black-and-white interior). The imprint on page 4 follows BoD's template and leaves its upper part free for the FSC mark that BoD prints. The ISBN there is a placeholder until BoD assigns one.
- `understanding-ai_cover_A5_PB.pdf`: the paperback cover (back, spine, front) to upload to BoD. 342.0 × 220.0 mm including 5 mm bleed on all sides; trim 332.0 × 210.0 mm; spine 36.0 mm (BoD cover calculator: 590 pages, white 90 g paper, adhesive binding). TrimBox and BleedBox are set; no transparency; fonts embedded.
- `understanding-ai_cover_A5_PB_guides.pdf`: the same cover with trim lines, spine folds and safe zones drawn in. For checking only; do not upload.
- `understanding-ai.md`: the full manuscript in Markdown, for editing or conversion.

## Before uploading to BoD
1. Start the book project in myBoD: paperback, 14,8 × 21 cm, **white 90 g** paper (*weiß 90 g*), black-and-white interior, 590 pages. BoD then assigns the ISBN and shows the final cover size.
2. Rebuild the interior with the ISBN: `BOOK_ISBN=978-3-... python3 textbook/print/build.py`.
3. Rebuild the cover with the ISBN and BoD's spine width, if it differs: `python3 textbook/print/cover.py --isbn 978-3-... --spine-mm 36.0`. The script draws an EAN-13 barcode; using BoD's own barcode file in its place is the safer choice. For cream paper use `--paper chamois` (spine 40.4 mm).
4. Check that the cover size myBoD asks for matches the size the script prints. If you change the paper or the page count, the spine changes.

## Contents
- A preface on how the book is organised and how evidence is labelled.
- 14 chapters in five parts: How AI Works; The Frontier; Society and Economy; Risk, Safety and Governance; The Decade Ahead.
- About 197,000 words including references, 46 figures and 60 tables.
- A glossary of 409 terms.
- A numbered APA 7 reference list of 1,160 cited sources. The running text carries no citations: a line at the foot of each page lists the numbers of the sources used on that page, with pinpoints (pages, paragraphs, articles) in brackets; figure and table captions give their sources by number.

This edition is written as nonfiction, not as a course text: there are no learning objectives, summaries, key terms or discussion questions. Each chapter opens with a documented case and goes into the mechanisms, numbers and evidence in depth. It uses Concept, Case study, Debate and Going deeper boxes, ends with a synthesis paragraph and closes with annotated further reading.

## How the text was checked
1. **Deepening:** each chapter was rewritten to about 7,500–9,900 words from verified sources. Every new claim is logged with its URL and evidence type in `work/evidence-chNN.md`.
2. **Two independent fact-checks per chapter:** numbers, dates, quotations, attributions and bibliographic details were re-checked against primary sources. Corrections and remaining uncertainties are in each evidence log.
3. **Figure and table audit:** every figure was checked against its source data and its spec file (`figures/specs/`), then redrawn where labels, values, scales or captions were wrong.
4. **Specialist reader panel:** a general reader, a policy analyst and a machine-learning expert reviewed the chapters (`work/panel2/`). A whole-book consistency audit removed contradictions, duplicate explanations and broken cross-references.
5. **Third fact-check with web search:** after the polish, every chapter was checked again using web search to close the gaps logged in the earlier passes: claims that had been uncertain, blocked or confirmed only by secondary sources, preprints that have since been published, and developments up to October 2026. About 25 corrections followed, and seven newer developments were added.
6. **News sweep (25 October 2026):** every chapter was checked against news from July to late October 2026 (model releases, leaderboards, studies, court rulings, laws, export controls, incidents, official statistics). Outdated statements were corrected and major developments added, each verified and cited; every chapter was also re-read for errors and its worked arithmetic recomputed.
7. **Prose polish:** every chapter got a final pass for clarity, sentence length and number density, and to remove filler.
8. **Build checks:** no missing citations, consistent bibliography entries across chapters, and every section, table and figure cross-reference resolves.
9. **External review and revision (25 October 2026):** an independent full read with reference checks (reports in `review/` at the repository root) found errors, selective reporting, unlabelled company claims and preprints, outdated 2026 material and coverage gaps. Every chapter was revised against its report; each change and its source is logged under "Revision after external review" in `work/evidence-chNN.md`.
10. **Sourcing audit (30 October 2026):** every paragraph, list item, box and caption that states anything about the world now carries a citation to a source that supports it; standard concepts cite the original paper or a standard textbook; the author's own examples, calculations and opinions are marked as such. Claims that rested on secondary reports, search snippets or blocked pages were re-checked against primary sources where these could be reached; claims that could not be confirmed were removed or narrowed. `review/uncited.py` lists any paragraph without a citation. Outcomes are logged under "Sourcing audit" in each evidence log.

## Limitations
- **Blocked sites:** some publishers and companies (iso.org, parts of openai.com) refuse automated access. Those claims rest on official copies or reputable reports and are labelled.
- **IEA reports:** the IEA website blocks automated access, so these figures rest on an earlier reading of the full report PDF.
- **Paywalled papers:** some were checked against accepted manuscripts or preprints.
- **Company sources:** these are labelled as company claims in the text. Some OpenAI pages were read through a text mirror.
- **Fast-moving material:** model names, benchmark scores, export controls and which laws are in force will date quickly. A human expert review of this 2026 material before publication is still recommended.

Remaining uncertainties are listed for each chapter in the evidence logs.

## Rebuilding
Run `python3 textbook/print/figures.py` to build the figures, then `python3 textbook/print/build.py` to build the PDF. Requires pandoc ≥ 3.1, WeasyPrint, pypdf, reportlab and matplotlib. `python3 textbook/print/check_build.py` fails if the delivered PDF was built from different sources than those in the repository (the build records a hash in `BUILD-INFO.txt`).

Run `python3 textbook/print/cover.py` to build the cover. The cover uses Inter and JetBrains Mono (SIL OFL) alongside EB Garamond.

The files `sample-ch10-*.pdf` are earlier samples of alternative citation layouts and are not current.
