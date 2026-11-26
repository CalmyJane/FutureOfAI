# Fourth review: fix brief

Apply the fourth-review reports, `review4/r-chNN.md`, to the book *Understanding AI* (repository `/home/user/FutureOfAI`).

**Scope**
- Apply every **MUST** and every **SHOULD** item, using the "Change to" wording unless it no longer fits the surrounding text. In that case keep the meaning and the sources.
- "Could not verify" items: narrow or attribute the claim if the report suggests it. Otherwise leave it.

**The book's settings**
- The cut-off is late November 2026.
- The style is British spelling, plain sentences and numbers with their year.
- Company claims are labelled as company claims, and lawsuits as allegations.

**Files**
- Edit only your assigned chapters' files:
  - `textbook/chapters/chNN.md`
  - `textbook/bib/chNN.bib`
  - `textbook/work/evidence-chNN.md`
  - `textbook/figures/specs/*-NN-*.md`
  - `textbook/print/figs_chNN.py`
- If a report item asks for a change in another chapter's file (a consistency fix), make that one change. Name it in your report-back.
- Do not run the build, and do not run git commands that change state.

**Bibliography**
- Before adding a key, grep all `textbook/bib/*.bib` files for it.
- If the key already exists, copy the identical entry into your chapter's bib.
- New entries use the style of the existing ones (`urldate`, `howpublished`, and "(company source)" for company sources).

**Evidence log**
Append `## Fourth review fixes (November 2026)` to each evidence log, listing each item ID and what changed, or why it was skipped.

**Report back** in under 150 words:
- items done;
- items skipped, with the reason;
- any change made outside your chapters.
