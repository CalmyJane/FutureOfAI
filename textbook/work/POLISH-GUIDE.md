# Polishing guide (final prose pass)

You polish ONE or TWO chapters of the nonfiction book *Understanding AI* (current to October 2026; author's brief: "very full of information, not much blabla, a lot of deep-dive; everything correct and according to sources; well written, makes sense"). The chapters have been rewritten for depth and fact-checked twice; **facts, numbers, quotations, citations, tables and figure captions are verified — do not change them** except where a point below requires it, and never introduce a new factual claim without verifying it (WebFetch/Crossref/arXiv; WebSearch is unavailable) and adding it to bib and evidence log.

Read first: `work/panel2/*.md` (reader reports; apply every point about your chapters), `work/panel2/audit-consistency2.md` if present (cross-chapter fixes assigned to your chapters), and your chapter.

## Prose: what to fix everywhere
1. **Count-announcing openers** ("Two further ideas…", "Three results matter", "Four causes are documented", "Two caveats apply"): rewrite so the content leads. At most one such sentence per chapter.
2. **"Not X but Y" / "X rather than Y" reflexes** and "That argument is not academic"-style lines: keep only where the contrast is the point; rewrite the rest as direct statements.
3. **Punchline paragraph endings** (one-line morals: "The question is open.", "The selection problem is itself a finding."): keep a few where they earn their place; cut or merge most.
4. **Verdict tics** ("The pattern … is consistent.", "Each fit is honest, but…"), **identical sentence shapes** ("The first concerns… The second concerns…"), **doubled attribution** ("Meta reported … according to the company" → one attribution).
5. **Debate-box closers**: each box ends with what evidence would decide the question, but phrase it differently each time and fold it into the prose; no fixed italic label repeated across chapters.
6. **Prose that restates a table row by row**: replace with the takeaway and refer to the table.
7. **Number pile-ups**: no sentence with more than ~4 numbers; no paragraph with more than ~8. Move detail to a table or cut the least important.
8. **Version histories** of papers (revisions, data vintages): latest figure in the text; history in a short parenthesis or the caption.
9. **Undefined symbols or jargon** in equations or text: define in place or cut.
10. **Chapter endings**: end the last numbered section with a short synthesis paragraph (3–5 sentences) that draws the chapter's threads together with substance (no moralising, no "this chapter has shown"). Avoid abrupt endings.
11. **Sentence length**: average 17–22 words; split anything over ~40 words; untangle nested clauses.
12. Keep British spelling, the box types, headings, numbering, figure/table references, citations. Remove any leftover teaching language or signposting.

## Length
Polishing should usually shorten. Final body 7,000–9,500 words.

## Deliver
Pandoc check (`pandoc chapters/chNN.md --citeproc --bibliography bib/chNN.bib -t html -o /dev/null`, no citation warnings). Append `## Polish (date)` to the evidence log listing structural changes (not every wording change) and any facts added/removed. Report: what you changed per reader point; word count before/after; any figure-caption or table changes; anything you were unsure about. Do not commit. Do not edit other chapters' files or print/*.py.
