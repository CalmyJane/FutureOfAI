# Fix brief: second review

Repo /home/user/FutureOfAI, branch claude/epic-brown-l6rmum, book in textbook/. Read review2/00-VERDICT.md, then the report(s) for your chapters in review2/ (r-chNN-NN.md), plus review2/r-technical-coverage.md and review2/r-publication.md for items touching your chapters.

## Edit ONLY your files
textbook/chapters/chNN.md, textbook/bib/chNN.bib, textbook/work/evidence-chNN.md, textbook/work/glossary-chNN.md, textbook/figures/specs/*-NN-*.md, textbook/print/figs_chNN.py for your chapters. Others work in parallel. No git commits, no PDF build. The central editor handles the preface, build, CSS, index and the reference-list capitalisation.

## Do
1. Fix every blocking, major and minor item in your reports (C-items in the verdict are blocking). Verify before changing; if a reviewer is wrong, don't change it and log why.
2. Sourcing rule stays absolute: every statement about the world carries a citation to a source that supports it (verify with WebFetch/WebSearch, load via ToolSearch "select:WebFetch,WebSearch"; Crossref, arXiv). New releases and events must be checked on the vendor's/official page where reachable; if only press coverage exists, attribute it ("according to Reuters"). Never invent; remove what can't be sourced.
3. Currency: the book is current to the end of October 2026. Statements about deadlines in November 2026 or later must be dated ("as of late October 2026"). Past dates must be in past tense.
4. Writing (book-wide decision): the preface will say once that worked examples, calculations and tables without a source are the author's. So REMOVE inline tags like "worked example by the author", "calculation by the author", "by the author's arithmetic" from running text (keep "computed by the author" only in table/figure captions where settings are given). Keep "in the author's view" only for genuine opinions, at most about three per chapter, and vary the wording. Debate boxes must not all end with the same template sentence ("In the author's view, settling the question needs…"): end each with the specific evidence that would settle it, in natural prose.
5. Balance: where your chapter reports 2026 incidents or company claims, keep the reporting even-handed; don't overstate.
6. Keep length disciplined: pay for additions by cutting repetition and number dumps.
7. Keep en-GB, "%", "$", "Nvidia". Keep pandoc citation syntax. Token strings with a leading space: write them as inline code with straight quotes, e.g. `" mat"` (backticks), never as typographic quotes.
8. Log every change under `## Second review fixes (Nov 2026)` in your evidence log(s), with URLs.
9. Before finishing: `python3 review/uncited.py textbook/chapters/chNN.md` (only marked opinions/examples may remain), `pandoc --citeproc` with your bib (no missing keys), no uncited bib entries, `python3 -m py_compile` on changed figure scripts.

## Final message (≤20 lines)
What you fixed, what you rejected (why), new references, word-count change, anything the central editor must handle.
