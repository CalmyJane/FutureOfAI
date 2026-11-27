# Review 7: Chapter 6 (AI for Science, Mathematics and Engineering)

## Verdict
Ready to print after two small balance fixes, neither of them blocking. The legally sensitive Navier–Stokes case study matches its primary sources closely. That covers Buckmaster's statement, OpenAI's statement and its 10 September update, Bubeck's quote in *Scientific American*, King's College London, the EMS, the Fields Medallists' letter and the Clay Institute. It wisely leaves out the most inflammatory details in Buckmaster's account and in *Scientific American*'s summary ("attempted to bribe and threaten"). The November 2026 Riemann-hypothesis material matches the Lean FRO/Mathlib statement, Tao's blog and The Next Web.

**Balance between companies.** The chapter is mostly even-handed. Google DeepMind dominates because it produced most of the showcase results, and the chapter says so. OpenAI's mathematics claims are reported with expert support (Litt, Gowers, Quanta's experts) as well as criticism (Bloom, Sarnak, the Navier–Stokes caveats).

Two places lean slightly towards Anthropic, which matters in a book written by Anthropic models:
- In the USAMO 2026 results, the chapter names GPT-5.4, Gemini 3.1 Pro and the best open model, but leaves out Claude Opus 4.6's weak score.
- In the Riemann-hypothesis claim by an Anthropic researcher using Claude, it leaves out a widely reported conflict-of-interest point: the claim came one day after Anthropic's stock-market debut.

Adding both would also be fairer to the critics' side of the record.

## MUST change before printing
None.

## SHOULD change

### S1. USAMO 2026: Anthropic's own model left out of the results
- Where: textbook/chapters/ch06.md:184
- Text now: "reported that GPT-5.4 "essentially saturates the benchmark with a top score of 95%", with Gemini 3.1 Pro at 74% and the strongest openly available model at 45%. … noting that two of the judging models overrated their own answers."
- Problem: UNCLEAR / balance. MathArena reports Claude Opus 4.6 at 47%, ranked third. It also names the two self-overrating judges: Gemini 3.1 Pro and Opus 4.6. The book names every other top model but not Anthropic's, so a reader cannot see that the Anthropic model did poorly.
- Evidence: https://matharena.ai/usamo/ (28 March 2026): "Gemini-3.1-Pro reaches only 75%, Opus-4.6 scores 47%, and the strongest open model, Step-3.5-Flash, reaches just 45%"; "Gemini-3.1-Pro and Opus-4.6 both substantially overestimate their own performance."
- Change to: "…with Gemini 3.1 Pro at 74%, Anthropic's Claude Opus 4.6 at 47% and the strongest openly available model at 45%. … noting that two of the judging models, Gemini 3.1 Pro and Claude Opus 4.6, overrated their own answers."

### S2. The Riemann-hypothesis claim: the Anthropic timing context is missing
- Where: textbook/chapters/ch06.md:231
- Text now: "The same day Alpöge released what he said was a proof, found with Anthropic's Claude, of the Riemann hypothesis … Brian Conrad of Stanford called releasing a proof its author did not fully understand "frankly completely outrageous" [@constantin2026riemann; @tao2026unforced]."
- Problem: UNCLEAR / balance. For OpenAI's Navier–Stokes claim, the chapter reports commentators' readings of the company's motives. For this claim by an Anthropic employee using Claude, it leaves out the point the cited source itself raises: the release came one day after Anthropic's stock-market debut. Alpöge denied that the timing was cynical. The same source also gives a positive expert view (Maynard), which the book omits while keeping the critic. Adding both keeps the account even and discloses the company interest.
- Evidence: https://thenextweb.com/news/anthropic-alpoge-claude-riemann-hypothesis-proof-lean (21 Nov 2026): "The claim came one day after Anthropic's record stock market debut… 'There is an obvious cynical view, to do with the timing, but it is false,' he wrote"; "James Maynard of the University of Oxford was '98 or 99 percent' certain, he told The New York Times."
- Change to: insert before "That is machine certification": "The release came one day after Anthropic's stock-market debut; Alpöge rejected what he called the "obvious cynical view" of the timing [@constantin2026riemann]." Then change the closing sentence to: "…and no mathematician had explained the argument. James Maynard told *The New York Times* he was "98 or 99 percent" certain it was right, while Brian Conrad of Stanford called releasing a proof its author did not fully understand "frankly completely outrageous"; Terence Tao ranked it the least digested of the month's results [@constantin2026riemann; @tao2026unforced]." (Same sources; no new bib entry.)

### S3. Optional: state Scientific American's finding on the plagiarism question plainly
- Where: textbook/chapters/ch06.md:223
- Text now: "experts judged that in its details it took a different approach from the human research programme it had first been compared with [@howlett2026openais]"
- Problem: UNCLEAR (minor, fairness to OpenAI). The cited article's own summary is that the rumours OpenAI had taken the two mathematicians' work "may have been overblown". The book's wording implies this, but a reader of the credit section that follows may miss it.
- Evidence: https://www.scientificamerican.com/article/openais-blockbuster-navier-stokes-proof-isnt-what-we-thought-it-was/ (13 Oct 2026), standfirst: "Rumors that OpenAI's "Navier-Stokes" solution stole the work of two mathematicians may have been overblown"; "All said that it's increasingly clear that the company's proof does *not* follow the Spanish program."
- Change to: "…and experts judged that in its details it took a different approach from the human research programme it had first been compared with, suggesting that claims it had drawn on that work "may have been overblown" [@howlett2026openais]."

## Could not verify
- The exact wording of the A-Lab author correction ("not necessarily new to science"; 36 confirmed and 4 inconclusive). The Nature page is paywalled. A secondary summary confirms 36 of 40, with 4 inconclusive and one compound removed.
- The NHC 2025 verification report wording on the Google DeepMind ensemble (PDF not fetched).
- Cheetham and Seshadri's sample sizes (250 of 2,047 entries; 384,870); Terwilliger et al.'s 102 maps and the 0.6 Å and 10% figures. These are older material and plausible from memory.

## Checked and confirmed
- Buckmaster's statement (7 Sept 2026), all paraphrased claims: personal collaboration using models from several companies; the Córdoba/Martínez-Zoroa programme; 15 August for forced Boussinesq and Euler; OpenAI's first prompt sent "after information about our work had reached OpenAI"; "I am not accusing anyone of anything".
- OpenAI's statement (8 Sept, updated 10 Sept): "to report on the substantial progress…", "We do not intend to claim the Millennium Prize…", began 1 September "after hearing a rumor" later linked to Alpöge, "recognize the priority of their work on forced Euler", "did not see any of their work through any means…", "could not have influenced the system in any way, including through training", about 10,000 agents, about 88 hours, and 17 hours of Lean formalisation.
- The first OpenAI statement's "cannot rule out" (via OfficeChai); Bubeck's "We did not use their prompt or proofs to prompt our models" (*Scientific American*, 8 Sept).
- KCL release (27 Oct 2026): "The researchers have not shown that OpenAI's original proof is wrong"; KCL and Cambridge authors.
- EMS: "milestone"; "internal to OpenAI and not generally accessible". Clay: "apparently been settled".
- Open letter at mathandai.org: title, date 11 Sept 2026, quoted phrases verbatim, Tao, Scholze and Viazovska among the Fields Medallist signatories.
- *Scientific American* (13 Oct): "more than a month later, no one fully does [understand it]"; a different approach in the details.
- 20 November: Buckmaster's "unpolished and heavily LLM-assisted"; the numerical-data certificate not yet released (TNW, *Scientific American*); Tao's post ranking by how "digested" the results are.
- Lean FRO/Mathlib joint statement (21 Nov 2026): 17 million lines; two independent comparison tools; several independent checkers; RH only, with no mention of the generalisation.
- Anthropic zeta post: 41.6% to 67.2%, an unreleased model, Alpöge and Furman, Conrey and Goldston "on short notice", a Lean proof, and "We don't expect … will lead to proving the Riemann hypothesis". Lamzouri (arXiv 2609.02882): "conceptually simpler", more than 67.25%.
- Quanta on the quasi-RH claim: 1/8–7/8 Lean-verified (199 pp.); 1/12–11/12 not verified (49 pp., the only human-edited paper); experts "largely agree that the result is correct"; Sarnak won't call it "a Theorem" until humans check.
- Unit-distance result: OpenAI, 20 May 2026; Sawin's arXiv 2605.20579 (20 May), n^1.014; Litt and Gowers quotes verbatim (ScienceAlert/The Conversation); about 10^2,000,000 points. DeepMind's 9 of 353 (arXiv 2605.22763).
- AFP on IMO 2026: Celia and dots-note-3.0 at 42/42; "strictly prohibited"; submitted to IMO organisers; Deedy Das's informal tests of OpenAI, Anthropic, Axiom Math and Kimi K3.
- MathArena USAMO 2026: 95.2% and 74.4%; best open model at 45%; Google grant; a three-model jury with human review of every solution.
- Crossref check of all 2026 journal entries (A-Lab correction, Juelsholt in *Materials Horizons*, Hao et al. in *Nature*, Co-Scientist in *Nature*, WeatherNext Cyclones in *Nature*, Georgiev et al. in *PNAS*, Lu et al. in *Nature*): titles, journals, volumes and pages all match the bib entries.
- Mathlib holds 296,856 theorems (more than 290,000 confirmed).
- Internal consistency: ch14 refers to "Section 6.6" for Navier–Stokes, which is correct; internal forward and back references (§6.5 to §6.6, §6.9, Figure 6.1) are correct.

## Tally
Claims checked: 58 / confirmed: 55 / wrong: 0 / outdated: 0 / balance or clarity issues: 3 (S1–S3) / not verified: 3 groups
