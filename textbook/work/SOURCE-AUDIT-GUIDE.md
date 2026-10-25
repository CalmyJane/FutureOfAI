# Source audit (25 October 2026)

The book is switching to a citation layout with no citations in the running text: each page gets one line listing the numbers of the sources cited on it, keyed to a numbered reference list at the end of the book. Readers will no longer see which sentence a source belongs to, so the underlying markdown must be right: every claim must carry the right source, and every source must actually support the paragraph it sits in.

You audit TWO chapters (`chapters/chNN.md`, `bib/chNN.bib`, `work/evidence-chNN.md`). Read the evidence log first: it records what each source was verified for.

## 1. Does every citation make sense?
For every citation in the chapter (paragraphs, boxes, tables, captions):
- Does the cited source actually support the claim it is attached to (right paper/report/law, right year, right edition)? Use the evidence log; re-check the source itself (WebFetch, Crossref/arXiv API, or WebSearch sparingly) when the log does not clearly cover it or something looks off.
- Is the bib entry correct and complete (authors, title, year, venue/publisher, DOI or URL; preprint vs published)? Is the entry type sensible for APA output?
- Is a company blog, news article or secondary source being used where a primary source exists and is readily available? Swap in the primary source if you can verify it (keep the claim's wording accurate to it).
- Fix wrong or weak citations.

## 2. Is anything missing a source?
Read every paragraph and list the factual claims (numbers, dates, named events, quotations, study results, legal provisions, attributions) that carry no citation in that paragraph. Common knowledge and the book's own reasoning or arithmetic need none; anything a careful reader might want to check does. For each uncited claim:
- If another citation in the same paragraph already covers it, fine.
- Otherwise find and verify a source (primary preferred), add the citation and a bib entry (`surname/org + year + firstword`; if the key exists in another chapter's bib, copy that entry byte-identical), and log it in the evidence log.
- If you cannot verify the claim, soften or cut it.
- Quotations must always have a citation in the same paragraph.

## Rules
- Do not change prose beyond what the citation fixes need. Keep each chapter body ≤ 9,900 words.
- Citations stay in pandoc form (`[@key]`, `@key`); do not change the citation style.
- Do not edit other chapters' files or `print/*`. Do not commit.
- Searches: you share a session-wide web-search budget with other checkers; use direct fetches of known URLs and APIs first, search only when needed (aim ≤ 40 searches).
- Safety: no operational detail on weapons, pathogens, toxins, cyber-attack techniques or self-harm.
- Run `pandoc chapters/chNN.md --citeproc --bibliography bib/chNN.bib -t html -o /dev/null` (no warnings).
- Append `## Source audit (2026-10-25)` to the evidence log: citations corrected (old → new key and why), sources added (claim → key → URL), claims softened/cut.

## Report (compact)
Per chapter: number of citations checked; wrong/weak citations fixed; uncited claims found and how each was resolved; bib entries corrected; shared bib keys changed (report, don't edit other bibs); anything unresolved.
