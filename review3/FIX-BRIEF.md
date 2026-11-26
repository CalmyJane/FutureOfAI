# Third review: fix brief (26 November 2026)

You are applying the third review to the textbook *Understanding AI* (repository root: `/home/user/FutureOfAI`). The chapters are `textbook/chapters/chNN.md` (Pandoc Markdown, citations as `[@key]`). Bibliographies are `textbook/bib/chNN.bib`. Each chapter has an evidence log, `textbook/work/evidence-chNN.md`. Figure and table specs are in `textbook/figures/specs/`, and the figure scripts are `textbook/print/figs_chNN.py`.

Your reports are `review3/r-chNN.md`. The combined verdict is `review3/00-VERDICT.md`. Read the verdict sections A and B, then your chapter reports in full.

## Decisions already made by the author
- **The cut-off moves to late November 2026.** The book will say its evidence is current to late November 2026. Apply every currency update the reports give for November 2026, including the ones marked "optional, only if the author wants to go past October". Where the text says "as of October 2026" or "by October 2026" about something that is still true in late November (the reports checked on 22 November), change it to "as of November 2026". Where a statement was true only in October, date it precisely instead ("On 25 October 2026 …").
- The author name is now Calmy Jane. Chapter text does not mention the author by name, so this should not affect you.

## What to apply
1. **Every MUST item** in your reports, using the "Change to" wording unless it no longer fits the surrounding text. In that case, keep the meaning and the sources.
2. **Every SHOULD item.** The author wants them all done.
3. **"Could not verify" items:** narrow or attribute the claim as the report suggests.
4. **"Reader notes":** apply them when they point to a concrete unclear or wrong sentence.
5. **The cross-chapter items (verdict section B) that touch your chapters.** Use these canonical facts, so that chapters edited by different people agree:
   - **B1, US export control on Claude Fable 5 and Mythos 5:**
     - On 12 June 2026 the US Commerce Department required a licence for foreign nationals' access to the two models, including inside the US.
     - Anthropic switched both models off for all customers.
     - Commerce lifted the control, with conditions, on 30 June 2026.
     - It was the first use of export controls to block access to an AI service.
     - Take the exact wording and sources from r-ch14.md, and the coordinator's sources from the verdict (Mayer Brown, Greenberg Traurig, Bloomberg Law, Just Security). If a report has no bib entry, create one, checking the source URL by web search where you can.
     - Ch. 14 must correct its claim. Ch. 7 and Ch. 13 each add one sentence.
   - **Anthropic incidents:**
     - There were four incidents. The fourth was in January 2026 and involved an early Claude Opus 4.6.
     - An independent METR investigation was agreed in September 2026 and has published no findings yet.
     - On 9 September Anthropic withdrew its July "harness and operational failure" framing and called the incidents "serious".
     - Ch. 11 and Ch. 12 must agree.
   - **The US evaluator:** call it CAISSI throughout. At first mention in a chapter, add that it was formerly CAISI where the chapter already explains the name.
   - **ClockBench:**
     - On 25 October 2026 the leader was Gemini 4 Argon at 83.3%.
     - By late November it was Claude Fable 5.2 Max at 87.8% (released 9 November).
     - The average human scores 90.7%.
     - Ch. 1 and Ch. 4 must give the same figures.
   - **OpenAI's pauses:**
     - First, OpenAI paused certain frontier training for two weeks after the July 2026 OpenAI–Hugging Face incident, and announced the pause on 18 August.
     - Second, on 28 September it held back GPT-6.1 Astra for failing its alignment standards.
     - Say when each was announced; do not date the first pause to August.
   - **The 19 November 2026 BIS rule (91 FR 74970):** it rescinded the diffusion rule, including the model-weights control, and put remote access to large compute for China-headquartered firms, and five more countries, under licence.
   - **Kimi K3** (2.8 trillion parameters, July 2026) and **Qwen3.8** (2.4 trillion, August 2026).
   - **New frontier releases after October:**
     - Claude Fable 5.2 and Mythos 5.2 (9 November);
     - GPT-6.2 Astra and Sol (17 November);
     - Gemini 4 Carbon general availability (10 November).
     
     Mention them only where your report says to.

## Rules
- **Edit only the files of your assigned chapters:**
  - the chapter files;
  - their bib files;
  - their evidence logs;
  - their figure/table specs;
  - their `figs_chNN.py`.
  
  Do not edit `textbook/print/build.py`, `textbook/print/srcnotes.lua` or the CSS; the coordinator handles production. If a fix needs a production change, say so in your report-back.
- **Do not run the build. Do not commit, stash or run git commands that change state.** Other agents are editing other chapters at the same time.
- **Bib entries:**
  - Before adding a key, check it is not already used in any `textbook/bib/*.bib` file (grep).
  - If a work is already in another chapter's bib under a key, reuse that key and copy the entry into your chapter's bib.
  - Use the field style of the existing entries: `urldate`; and `howpublished` with "(company source)" for company posts.
  - Set urldate to the review's reading date (2026-11-22) unless you check it yourself.
- **Style:**
  - Keep the book's style: British spelling, plain sentences, one idea per sentence, numbers with their year.
  - No new filler, no rhetorical questions, no "it's not X, it's Y".
  - Company claims are labelled as such.
  - Allegations in lawsuits are labelled as allegations.
- **Cross-references:** keep cross-references (`@sec:`, `@fig:`, `@tbl:` or "Section 7.3") intact.
- **Web search:** you may use it to confirm a fact when a report is unclear or you suspect it is wrong. Do not add new material beyond the reports and this brief.
- **Evidence log:** in the chapter's evidence log, append a section `## Third review fixes (November 2026)`. List each item ID (M1, S3 …) with what changed, or why it was skipped.
- **Report back** in under 300 words:
  - items done;
  - items skipped, with the reason;
  - any production change needed;
  - any cross-chapter inconsistency you noticed.
