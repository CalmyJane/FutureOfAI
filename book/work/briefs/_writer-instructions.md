# Writer instructions (all chapters)

You are drafting one chapter of the nonfiction book *When Everything Goes Right: The Hidden Risks of Successful AI, and the Institutions We Must Invent Before 2036*. Today's date is 2026-10-20. The book is written from 2026, looking forward to 2036.

## Read first (in this order)
1. `book/artifacts/05-voice.md`: voice, chapter form, the things the voice does not do, the rhythm contract.
2. `book/manuscript/chapters/chapter-00.md`: the prologue. It is the voice anchor; match its register.
3. `book/artifacts/02-story-engine.md`: thesis and rules of the argument.
4. `book/artifacts/07-outline.md`: your chapter's entry (and its neighbours, for the transitions in and out).
5. `book/artifacts/03-characters.md` and `book/artifacts/09-continuity-ledger.md`: recurring 2036 figures and canonical facts and definitions. Use the names, ages, dates and definitions exactly.
6. `book/evaluations/novelty-check.md`: prior work you must credit, by name, in one or two sentences, before extending past it.

## Research (before writing)
- Use WebSearch (load with ToolSearch "select:WebSearch,WebFetch" if needed) to verify every present-day fact, figure and citation you intend to use, especially those marked "verify" in the outline. Run 5–12 searches.
- Save `book/work/evidence-chapter-NN.md`: each claim, its source (author, title, year, URL) and a strength rating, plus anything you searched for and could not find.
- Never invent a statistic, quote, study or URL. If you cannot verify something, leave it out or say plainly in the text that no measurement exists, which is often a useful point for researchers. Paraphrase sources; quote at most a short phrase.
- 2036 vignettes are fiction and may contain invented numbers, but they must be consistent with the ledger and plausible given the 2026 evidence.

## Write
- Target the planned word count in the outline (±10%). Use `wc -w` to check.
- Format (Markdown):
  - `# Chapter N: Title`
  - the vignette, opening with an italic place/date line like `*2036 · Porto*`
  - `---` scene breaks between sections
  - body sections may carry a few `##` subheadings if useful
  - a blockquote box: `> **For researchers**` followed by 2–3 numbered open problems, each naming a measurable quantity
  - a final `## Notes` section listing sources as short entries (author, title, year, URL)
- Name the chapter's new concept clearly. Specify the proposal concretely: who does what, what is measured, what number triggers what.
- Give the strongest objection a real hearing and answer it, or concede part of it.
- End on a concrete image, a hard question, or a turn into the next chapter's subject (see the outline's "Ending turn"). Never end on a moral summary.
- Keep to the voice rules: few em dashes, at most one "not X but Y" construction, no habitual groups of three, no hype words, no straw men, short paragraphs, and concrete examples within two sentences of every abstraction.

## Save
- Write the chapter to `book/work/attempts/chapter-NN/attempt-1.md` (NN two digits). Do not touch any other chapter or the manuscript folder.
- In your final reply, report: the word count, the sources verified, any outline facts you changed or could not verify (and why), and any ledger additions you made up (new names or facts) so the orchestrator can record them.
