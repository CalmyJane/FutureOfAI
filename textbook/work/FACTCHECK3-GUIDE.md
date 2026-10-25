# Fact-check 3 guide (web-search verification pass)

The book *Understanding AI* (current to October 2026; today is 24 October 2026) has been fact-checked twice, but **web search was unavailable** for most of that work. Verification relied on direct fetches, Crossref/arXiv metadata and text mirrors (r.jina.ai). WebSearch now works. The author's brief is "really make sure that everything is correct and according to sources … well researched". Your job is to use search to close the gaps and to catch anything the earlier passes missed.

You check TWO chapters (`chapters/chNN.md`, `bib/chNN.bib`, `work/evidence-chNN.md`).

## 1. Close the logged gaps (do all of these)
Read the evidence log in full. List every item marked uncertain, unverified, secondary-only, blocked, read via jina/mirror, "could not confirm", preprint whose published version was not checked, or similar. For each one:
- Search for the primary source (official page, paper, dataset, legal text, filing). Prefer `mode: "standard"`; use `"extended"` only for hard-to-find items.
- Fetch it (WebFetch; r.jina.ai only as a fallback) and compare the claim word by word: number, unit, year, sample, setting, attribution, quote.
- Outcomes: **confirmed** (note the URL), **corrected** (fix the text and bib), **published since** (a preprint now has a journal/conference version: update the bib entry and drop "preprint" labels where peer review is now done, if the numbers match), or **still unverifiable** (cut or soften the claim so it says only what can be supported).

## 2. Spot-check the load-bearing claims
Pick the ~25 most important factual claims per chapter: headline numbers, anything in a table or figure caption, every quotation, dates of laws and releases, anything about 2025–26 events (these date fastest and are the most error-prone). Check each against its primary source via search + fetch. Also search for **newer developments up to October 2026** that would make a sentence wrong or misleading (a law that took effect or was delayed, a study retracted or corrected, a figure revised, a case settled). Only add a new fact if it is needed to keep the text correct; verify it and cite it.

## 3. Figures and tables
For every figure spec (`figures/specs/fig-NN-*.md`) and table in your chapters whose data come from an external source, re-check the numbers against the source. Fix the spec/table if wrong and list every change in your report (do NOT edit `print/*.py`; I will redraw).

## Rules
- Facts stay correct, prose stays polished: change only what correction requires, in the chapter's existing style (British spelling, labels: "a preprint", "according to the company", etc.).
- Keep word count roughly stable (body ≤ 9,900 words).
- Bibliography: each cited key one entry. If you change an entry whose key also exists in another chapter's bib (`grep -l "{key," bib/*.bib`), do NOT edit the other file; report the key and the new entry text so I can unify it.
- Do not edit other chapters' files. Do not commit.
- Safety: no operational detail on weapons, pathogens, toxins, cyber-attack techniques or self-harm.
- Run `pandoc chapters/chNN.md --citeproc --bibliography bib/chNN.bib -t html -o /dev/null` (no warnings).
- Append `## Fact-check 3 (2026-10-24, with web search)` to the evidence log: one line per item checked (claim → outcome → URL).

## Report (keep it compact)
Per chapter: counts (gaps closed / confirmed / corrected / cut); every correction as "old → new (source)"; figure/table spec changes; shared bib keys changed; anything still unverifiable.
