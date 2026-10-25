# Deepening guide: turning the course text into a dense nonfiction book

The book *Understanding AI: Technology, Trends and the Decade Ahead* (author Jan Göbel, current to October 2026) is no longer a course text. The author's brief: **"very full of information, not much blabla, a lot of deep-dive into all the topics; everything correct and according to sources; well written, makes sense, well researched."** Readers are intelligent non-specialists and professionals who want the real substance: how things work, what the numbers are, what the evidence shows, where experts disagree and why.

You rewrite ONE chapter (`chapters/chNN.md`). Read first: this guide; `work/WRITER-GUIDE.md` sections 3 (evidence standard), 4 (figures), 5 (glossary) and 6 (safety), which still apply; your chapter's evidence log `work/evidence-chNN.md` (it records what has already been verified, including fact-check and revision sections: do not undo verified corrections); and the neighbouring chapters' headings (`grep -n "^## " chapters/ch*.md`) to avoid overlap.

## 1. Remove the teaching apparatus
- Delete the `::: {.objectives}` block, the `## Summary`, `## Key terms` and `## Discussion questions` sections.
- Keep `## Further reading` (annotated, 4–6 items, each one sentence on what the reader gains).
- Remove every reference to students, seminars, courses, lecturers, "this chapter will", "in this chapter we", "as we saw", learning goals, exercises.
- Keep the glossary file (`work/glossary-chNN.md`): one entry per technical term the chapter defines. Drop entries for terms the chapter no longer uses.

## 2. Make it dense and deep
- **Cut filler.** No signposting ("It is worth noting", "Two points matter", "This raises an important question"), no restating what was just said, no generic transitions, no closing morals, no reflexive "both sides have a point" sentences. Every paragraph must add information: a mechanism, a number, a date, a finding, a counter-finding, a concrete example.
- **Go deeper.** For each section ask: what would an expert reader find missing or superficial? Add the substance: how the mechanism actually works (with real parameters and worked numbers), the history that explains the current state, the specific results with sample sizes and effect sizes, the methodological caveats that matter, the strongest counter-evidence, the open technical problems and who is working on them. Prefer one well-explained, well-sourced example over three name-checks.
- **Technical depth is welcome.** Chapters 2–4 may now include the key equations in the main text when they explain the mechanism (written in pandoc markup: *italic* variables, `~sub~`, `^sup^`, Unicode symbols; never `$…$` TeX), each explained in words with a worked number.
- **Boxes:** keep the box types (`.concept`, `.case`, `.debate`, `.deeper`) only where they genuinely help; 2–5 per chapter. Rename the label "Key concept:" to "Concept:" (keep the rest). Debate boxes: the best evidence on each side and what evidence would decide it, written in fresh words each time.
- **Tables:** where a set of comparable numbers appears (benchmarks, studies, laws, costs), a compact pipe table is better than prose. Caption line directly below: `: Table N.M: caption. Source: [@key].` Number tables in order of appearance.
- **Length:** body (from the first line after the title to the end of the last numbered section) 7,500–9,500 words. Depth, not padding: if material is thin, research more rather than write more words.
- **Structure:** keep the chapter title and numbered sections (5–8), you may reorganise, merge, split or add sections where that serves the subject. Opening: 1–3 paragraphs with a real, documented case or fact.

## 3. Correctness is the priority
- Every factual sentence must be supported by a source you have checked (WebSearch is unavailable: use WebFetch on primary URLs and DOIs; Crossref `https://api.crossref.org/works/DOI`, arXiv `https://export.arxiv.org/api/query?id_list=ID`, OpenAlex, Europe PMC, PubMed; for sites that block fetches try `https://r.jina.ai/https://…`). Copy numbers exactly, with year, sample and setting. If you cannot verify a claim, do not write it.
- Re-check any existing claim you keep that the evidence log marks as uncertain, secondary-only or unverified; if it still cannot be verified from a primary or reputable source, cut it.
- Labels: preprints/working papers ("a preprint", "a working paper"), company claims ("according to the company"), bank/consultancy research, opinions attributed. Unlabelled = peer-reviewed or official.
- Bibliography `bib/chNN.bib`: one entry per cited key, every entry cited. If a key exists in another chapter's bib (`grep -h "^@" bib/*.bib`), reuse it and copy that entry byte-identical. New keys: surname+year+firstword.
- Evidence log: append `## Deepening (date)` with one line per new claim (claim, exact number/quote, URL, evidence type) and a list of cuts.

## 4. Figures
- Keep existing figures that still fit the text; update captions to match. You may propose up to two NEW figures per chapter where a chart or diagram carries real information (data charts with exact sourced numbers preferred). Write specs to `figures/specs/fig-NN-MM.md` (type, purpose, caption, exact content/data with source key for every number). Renumber figures in order of appearance and update `![…](figures/fig-NN-MM.svg){#fig:NN-MM}` lines, in-text references, and spec file names/headers accordingly. Do NOT edit `print/figs_*.py`; list every figure whose spec, numbering or caption changed in your report.
- If you notice an error in an existing figure spec (number, label, date that the source does not support), fix the spec and report it.

## 5. Voice
British spelling. Clear, precise, calm; no hype or doom words; no em-dash chains; vary sentence length (average 17–22 words); paragraphs of 3–7 sentences. Explain every technical term at first use in plain words. No invented people or scenes. Cross-references to other chapters only where they save real repetition ("Chapter 4 explains scaling laws").

## 6. Safety
No operational detail on weapons, pathogens, toxins, cyber-attack techniques or self-harm; such risks only at the level of published assessments and policy.

## 7. Deliver
Run `cd /home/user/FutureOfAI/textbook && pandoc chapters/chNN.md --citeproc --bibliography bib/chNN.bib -t html -o /dev/null` (no citation warnings), check `wc -w`. Do not commit. Report: body word count; what you deepened (by section); new sources (count, with types); claims cut as unverifiable; tables added; figure changes (new specs, renumbering, caption changes, spec corrections).
