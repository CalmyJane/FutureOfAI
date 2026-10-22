# Understanding AI: Technology, Trends and the Decade Ahead — A Course Text

Author: Jan Göbel · Evidence current to 22 October 2026

## Files
- `understanding-ai_A5_interior.pdf` — print-ready interior: A5 (148 × 210 mm), no bleed, PDF/X-4 with sRGB output intent, 402 pages (even), fonts embedded (EB Garamond, SIL OFL). Cover and ISBN still to be added by the publisher/print-on-demand service.
- `understanding-ai.md` — the full assembled manuscript in Markdown (for editing or conversion).

## Contents
Preface with a 14-week course plan; 14 chapters in five parts (How AI Works; The Frontier; Society and Economy; Risk, Safety and Governance; The Decade Ahead); 41 figures and 10 tables drawn for this edition; glossary of 218 terms; APA 7 reference list of 583 sources.

Each chapter: learning objectives, an opening documented case, numbered sections, Key concept / Case study / Debate / Going deeper boxes, summary, key terms, discussion questions and annotated further reading.

## How the text was checked
1. Every chapter was written from verified sources (each claim logged in `work/evidence-chNN.md` with URL and evidence type).
2. An independent fact-check of every chapter re-checked numbers, dates, quotations, attributions and bibliographic details against primary sources; corrections and remaining uncertainties are listed in the "Fact-check" section of each evidence log.
3. A simulated reader panel (first-year social-science student, computer-science master's student, STS lecturer) reviewed sample chapters; all chapters were then revised (clarity, balance, evidence labelling, missing perspectives such as hidden data labour, unions, surveillance and privacy).
4. A whole-book consistency audit removed contradictions, duplicate tellings and broken cross-references; duplicate citation keys and glossary entries were merged.

Limitations: the session's web-search quota ran out during writing, so later verification used direct fetches of primary pages, DOI/Crossref/arXiv/PubMed metadata and archived or mirrored copies. A few sources (some company pages that block automated access) are cited via reputable secondary reports, which the text says. Remaining uncertainties are listed per chapter in the evidence logs. A human expert review before teaching use is still recommended, especially for the fast-moving 2026 material (models, benchmarks, laws in force).

## Rebuilding
`python3 textbook/print/figures.py` (figures) then `python3 textbook/print/build.py` (PDF). Requires pandoc ≥ 3.1, WeasyPrint, matplotlib.
