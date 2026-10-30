# Sourcing audit brief: every statement linked to a source

Repo: /home/user/FutureOfAI (branch claude/epic-brown-l6rmum). Book source: textbook/.
Goal set by the author: NOTHING in the book may lack a source. Every statement must be properly linked to a source, or removed.

## Your files (edit ONLY these)
textbook/chapters/chNN.md, textbook/bib/chNN.bib, textbook/work/evidence-chNN.md, textbook/figures/specs/*-NN-*.md and textbook/print/figs_chNN.py for your chapters. Other editors work on other chapters at the same time. Do NOT git commit, push or run the PDF build.

## Rules
1. **Every paragraph, list item, box paragraph, table caption and figure caption that states anything about the world must carry a citation** `[@key]` whose source actually supports it. This includes: numbers, dates, events, quotes, attributions, descriptions of what a paper/model/law/company did, historical claims, "first/largest" claims, and standard technical facts (formulas, definitions of established methods).
2. **Standard concepts and definitions** (e.g. what a neuron, softmax, gradient descent, effect size, sensitivity, Brier score, hard law is): cite an authoritative reference — the original paper or a standard textbook (e.g. Goodfellow, Bengio & Courville 2016 `goodfellow2016deep`; Jurafsky & Martin; Russell & Norvig; Cohen 1988; the law's own text). Reuse keys that already exist in any `textbook/bib/*.bib` (copy the entry byte-identical into your bib if it isn't there). Verify any new entry (Crossref/arXiv/publisher page).
3. **The author's own reasoning, worked examples and calculations** may stay without an external source only if the text marks them as such ("a worked example", "the author's calculation", "in the author's view", "Table X.Y: … computed by the author"). If an example uses real figures, cite where those figures come from.
4. **Quotes** must cite the exact source they come from; blockquoted legal definitions cite the law (with article).
5. **If you cannot find a source that supports a statement, remove or rewrite the statement** so that what remains is sourced. Never invent a source, never cite a source for something it does not say.
6. **Weak sourcing must be fixed.** Search your evidence logs for anything marked secondary, "via", "search snippet", "not accessed", "not re-opened", "could not verify", "unverified", "relied on log", "from knowledge", "blocked", "403", "paywalled". For each: fetch the primary source (try official site, archive.org `https://web.archive.org/web/2026/<url>`, PMC/Europe PMC, arXiv, publisher abstract, court/government copies, Google cache-like mirrors) and confirm the claim; if confirmed, cite the primary (or keep the secondary but say "as reported by X" if the primary truly cannot be reached and the secondary is reputable); if it cannot be confirmed from any accessible source, remove the claim or soften it to what an accessible source supports. Record the outcome in the log.
7. **Sentence-level check:** in every cited paragraph, every sentence containing a number, date, name of a study/law/company event, or quotation must be supported by one of that paragraph's citations. Use the evidence log to map claims to keys; where a sentence's claim is not covered, add the right citation or remove it.
8. Figure captions: data figures name their source keys; schematic diagrams say "Schematic by the author" AND cite the source of the concept depicted. Replace vague captions like "as cited in Sections 1.1–1.7" with explicit keys.
9. Keep the prose quality: don't bloat; prefer adding a citation to rewriting. Keep en-GB, "%", "$", "Nvidia".
10. Log every change under `## Sourcing audit (Oct 2026)` at the end of each evidence log: one line each (location, what was added/removed/verified, URL).

## Helper
A scanner listing uncited paragraphs: `python3 /home/user/FutureOfAI/review/uncited.py textbook/chapters/chNN.md` (run from repo root). Your chapters must end with zero factual paragraphs flagged, except those explicitly marked as the author's own example/argument. Also check boxes (`:::` blocks), list items and captions by eye — the scanner skips short items.

Before finishing, run `pandoc --citeproc` on your chapter with your bib to confirm no missing keys, and check every key in your bib is cited (delete uncited entries).

## Final message (≤20 lines)
Counts: paragraphs given citations, statements removed (list each briefly), weak sources upgraded to primary, weak sources that remain "as reported by" (list), anything you could not resolve.
