# Understanding AI: Technology, Trends and the Decade Ahead

Author: Jan Göbel · Evidence current to October 2026 (web sources checked 20–25 October 2026, the last passes with web search)

## Files
- `understanding-ai_A5_interior.pdf`: the print-ready interior. A5 (148 × 210 mm), no bleed, written as PDF/X-4 (PDF 1.6, sRGB output intent) but not yet validated by a preflight tool: run the printer's preflight before submission. 626 pages (an even number), all fonts embedded (EB Garamond; Noto Serif Devanagari, Noto Serif KR, Noto Sans Math and Noto Sans Mono for Hindi, Korean, symbols and code; all SIL OFL). The publisher or print-on-demand service still needs to add the cover and ISBN.
- `understanding-ai.md`: the full manuscript in Markdown, for editing or conversion.

## Contents
- A preface on how the book is organised and how evidence is labelled.
- 14 chapters in five parts: How AI Works; The Frontier; Society and Economy; Risk, Safety and Governance; The Decade Ahead.
- About 213,000 words including references and index; 46 figures and about 65 tables.
- A glossary of 431 terms and an index of 462 entries (generated from the laid-out pages by `print/make_index.py`).
- A numbered APA 7 reference list of 1,244 cited sources, with full author lists where available. The running text carries no citations: a line at the foot of each page lists the numbers of the sources used on that page, with pinpoints (pages, paragraphs, articles) in brackets; figure and table captions give their sources by number.

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

The files `sample-ch10-*.pdf` are earlier samples of alternative citation layouts and are not current.

11. **Second independent review and fixes (3 November 2026):** nine fresh reviewers (reports in `review2/`) re-checked about 530 claims, audited technical coverage and publication readiness. All chapters were revised: about 25 factual corrections, a new Section 3.8 on the path from ChatGPT to the 2026 frontier, agentic reinforcement learning, rewards without automatic checkers, efficient long-context attention, multimodality, controllable reasoning (Section 4.6), serving and quantisation (Section 7.1), the 2025–26 open-weight models (Section 7.6), and a closing synthesis in Chapter 14. Build: bracketed reference numbers in captions and table cells, code set in a bundled monospace font, a layout pass that moves figures to fill page gaps, and an index.

## To do before publication
- **Author decisions:** AI-assistance disclosure and copyright line, about-the-author, acknowledgements, ISBN and imprint, title.
- **Human expert read** (technical and legal/policy) of the whole text.
- **Printer preflight** of the PDF (PDF/X-4 conformance, colour, fonts).
- **Proof-day checks of time-sensitive facts:** US ownership-rule suspension and US–China truce (9–10 Nov 2026), China's gallium/germanium suspension (27 Nov 2026), BLS Q3 2026 productivity (5 Nov), Challenger October 2026 job cuts, any new frontier model releases after October 2026.
- **Pages blocked from the review environment** (openai.com, oecd.org, sagaftra.org, CETaS, Metaculus): a person with normal web access should confirm the claims logged as "as reported by" in `work/evidence-chNN.md`.
