# Recent-developments pass (news sweep, 25 October 2026)

The book *Understanding AI* claims to be current "as of October 2026". Today is 25 October 2026. The author wants it to reflect the latest developments and to contain no errors. Three fact-checks have been done (see the evidence logs); this pass looks **outward at the news** and **inward for remaining errors**.

You cover TWO chapters (`chapters/chNN.md`, `bib/chNN.bib`, `work/evidence-chNN.md`). Load WebSearch/WebFetch via ToolSearch (`select:WebSearch,WebFetch`). Budget your searches (~150): you have a hard per-agent limit.

## 1. News sweep (most important)
Search news from roughly **July–25 October 2026** on every topic your chapters cover: model releases and benchmark records, company announcements, studies and preprints that made news, court rulings and settlements, laws/regulations/executive orders taking effect or delayed, export controls, energy and data-centre deals, incidents, surveys and official statistics with new releases. Use several queries per topic (e.g. "<topic> October 2026", "<topic> September 2026", named entities in the chapter + "2026"). For each hit, ask: **does any sentence, table cell, figure caption or "latest" claim in my chapters become wrong, outdated or misleading?**
- If a statement is now wrong or outdated: fix it, verifying the new fact in a primary or reputable source (official page, filing, paper, Reuters/AP/FT-level reporting), cite it and add a bib entry.
- If a major development is missing and the chapter's argument would look out of date without it (e.g. a new frontier model that now holds the record a sentence names; a law that now applies; a big new study on exactly the chapter's question): add it concisely (1–3 sentences), verified and cited. Do not add minor news.
- Superlatives and "latest/largest/first/most recent/as of" claims are the most fragile: check every one.

## 2. Error sweep
Re-read your chapters in full, critically, as a careful expert reader. Look for: internal contradictions; arithmetic errors in worked examples; numbers that disagree between text, tables and captions; wrong dates or names; claims stated more strongly than their source; cross-references to sections/tables/figures that don't match; anything that no longer makes sense. Check anything suspicious against the source.

## Rules
- Keep the chapter's style (British spelling; evidence labels: "a preprint", "according to the company"; no hype). Keep each chapter body ≤ 9,900 words: if you add, trim lower-value detail elsewhere.
- Safety: no operational detail on weapons, pathogens, toxins, cyber-attack techniques or self-harm.
- Bibliography: one entry per cited key; new key surname/org+year+firstword. If you must change an entry whose key also appears in another chapter's bib (`grep -l "{key," bib/*.bib`), don't edit the other file; report it.
- Figures: do NOT edit `print/*.py`. If a figure's data or caption must change, update `figures/specs/fig-NN-MM.md` and the caption in the chapter, and report exactly what must be redrawn.
- Don't edit other chapters. If you find something wrong in another chapter, report it. Do not commit.
- Pandoc check: `pandoc chapters/chNN.md --citeproc --bibliography bib/chNN.bib -t html -o /dev/null` (no warnings).
- Append `## News sweep (2026-10-25)` to each evidence log: developments checked (with URLs), changes made, errors fixed.

## Report (compact)
Per chapter: developments found that required changes ("old → new (source)"), developments added, errors fixed, figure redraws needed, items for other chapters, anything uncertain.
