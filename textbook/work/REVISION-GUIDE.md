# Revision guide (after reader panel)

You revise one or two chapters of the course text *Understanding AI* (current to 22 Oct 2026). Read first: `work/WRITER-GUIDE.md` (voice, template, evidence standard), the reader-panel notes in `work/panel/*.md` (apply every point that concerns your chapters; also apply the global points below to your chapters even if no reader read them), and your chapters' evidence logs (`work/evidence-chNN.md`, including the Fact-check section, which records verified facts: do not undo fact-check corrections).

## Global fixes (every chapter)
1. **Templated prose.** At most ONE explicit "the analogy breaks down / is imperfect / has a limit" sentence per chapter; for other analogies, fold the limit into the sentence naturally or drop it if obvious. Remove signpost filler ("X is worth noticing", "Two features deserve emphasis", "Three lessons stand out", "The lesson is general:", "Each element … does work", "Two cautions apply"). Remove reflexive both-sides closers ("these positions are not exclusive; what divides them is weight"). Keep at most one paragraph-final "Chapter X covers…" cross-reference per section. Vary the phrasing of "What would settle it?" lines (keep the content).
2. **Citations.** Cite the same source once per paragraph unless different claims need page locators. No "(abstract)" or "Computed by the author on 22 October 2026" in running text (keep such provenance in captions/notes only, once).
3. **Evidence labels.** At first mention in each chapter: preprints and working papers labelled as such (e.g. "a working paper", "a preprint"), investment-bank/consultancy research labelled, company claims "according to the company". Peer-reviewed work stays unlabelled. Numbers carry their year.
4. **Balance.** Where the chapter leans on one company's own documents (often Anthropic or OpenAI), pair claims with an independent or rival source where one exists, or state the limitation once. Tell each case once.
5. **Discussion questions.** No question that hands students the answer, rests on no evidence, is generic ("evaluate the arguments on each side"), or misstates the chapter. At least one evaluates evidence and one applies a concept to a new case.
6. **Readability.** Break up sentences over ~35 words and paragraphs that pile up more than ~4 percentages; define any technical term at first use.

## Evidence standard for any NEW claim
WebSearch is unavailable (budget exhausted). Verify with WebFetch of primary URLs/DOIs, Crossref/OpenAlex/arXiv/Europe PMC APIs, or r.jina.ai/https://… for pages that block direct fetches. Add bib entries (keys: surname+year+word; check `grep -h "^@" bib/*.bib` to reuse an existing key for the same work, copying its entry exactly) and evidence-log lines. If you cannot verify, do not add the claim.

## Constraints
- Keep structure, headings, figure/table numbering and box types. Body length (objectives to end of last numbered section) must stay 5,500–6,900 words (`wc -w`).
- Edit only your chapters' files (chapters/chNN.md, bib/chNN.bib, work/evidence-chNN.md, work/glossary-chNN.md, figures/specs). If a figure's data or labels must change, edit the spec and say so in your report (do not edit print/figs_*.py).
- Safety: no operational detail on weapons, pathogens, cyber-attack techniques or self-harm.
- Finish with `pandoc chapters/chNN.md --citeproc --bibliography bib/chNN.bib -t html -o /dev/null` (no citation warnings) and append a "## Revision (date)" section to the evidence log listing changes.
- Report briefly: changes made per panel point, new sources added, figure-spec changes, word counts. Do not commit.
