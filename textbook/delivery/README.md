# Understanding AI: Technology, Trends and the Decade Ahead

Author: Jan Göbel · Evidence current to October 2026 (web sources checked 20–25 October 2026, the last passes with web search)

## Files
- `understanding-ai_A5_interior.pdf`: the print-ready interior. A5 (148 × 210 mm), no bleed, PDF/X-4 with sRGB output intent, 564 pages (an even number), all fonts embedded (EB Garamond, SIL OFL). The publisher or print-on-demand service still needs to add the cover and ISBN.
- `understanding-ai.md`: the full manuscript in Markdown, for editing or conversion.

## Contents
- A preface on how the book is organised and how evidence is labelled.
- 14 chapters in five parts: How AI Works; The Frontier; Society and Economy; Risk, Safety and Governance; The Decade Ahead.
- About 191,000 words including references, 46 figures and 61 tables.
- A glossary of 375 terms.
- An APA 7 reference list of 1,007 cited sources.

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

## Limitations
- **Blocked sites:** some publishers and companies (iso.org, parts of openai.com) refuse automated access. Those claims rest on official copies or reputable reports and are labelled.
- **IEA reports:** the IEA website blocks automated access, so these figures rest on an earlier reading of the full report PDF.
- **Paywalled papers:** some were checked against accepted manuscripts or preprints.
- **Company sources:** these are labelled as company claims in the text. Some OpenAI pages were read through a text mirror.
- **Fast-moving material:** model names, benchmark scores, export controls and which laws are in force will date quickly. A human expert review of this 2026 material before publication is still recommended.

Remaining uncertainties are listed for each chapter in the evidence logs.

## Rebuilding
Run `python3 textbook/print/figures.py` to build the figures, then `python3 textbook/print/build.py` to build the PDF. Requires pandoc ≥ 3.1, WeasyPrint and matplotlib.
