# Review 8: Chapter 6 (AI for Science, Mathematics and Engineering)

## Verdict
Ready to print after one small factual fix (M1) and the SHOULD items. The older material is accurate: AlphaFold, GraphCast/GenCast, GNoME/A-Lab, AlphaGeometry/AlphaProof, FunSearch/AlphaEvolve, the AI Scientist, Kosmos and Hao et al. The fast-moving 2026 mathematics material is remarkably current and checks out against primary sources: the Navier–Stokes dispute, the Lean FRO certification of the Riemann hypothesis proof, the Anthropic IPO timing, MathArena and AFP.

On balance between companies, the chapter treats OpenAI's Navier–Stokes claim with heavy and well-sourced scepticism. It treats the Anthropic-linked claims (the zeta bound, and Alpöge's Riemann hypothesis and unforced blow-up) more lightly, though it does include Conrad's criticism, Tao's ranking and the IPO timing. It discloses that Alpöge is an Anthropic researcher. Two small adjustments would even the treatment (S2, S3).

## MUST change before printing

### M1. Lamzouri did not prove a "slightly stronger bound"
- Where: textbook/chapters/ch06.md:214
- Text now: "although in September the number theorist Youness Lamzouri published a new and, in his words, conceptually simpler proof of a slightly stronger bound"
- Problem: VERIFIED WRONG. Lamzouri gives a new proof of the same result as Claude, "more than 67.25%" simple zeros on the critical line. The book's own rounded figure for Anthropic's result (67.2%) makes 67.25% look larger, but the bounds are identical. His new results are different estimates (88.76% and 83.62%). His abstract says the new estimates "are neither stated nor proved in the Claude paper".
- Evidence: https://arxiv.org/abs/2609.02882 (2 September 2026): "a new, conceptually simpler, unconditional proof" that more than 67.25% of the nontrivial zeros are simple and on the critical line, plus "two new unconditional estimates" (88.76%, 83.62%). The Anthropic post (anthropic.com/research/riemann-zeta, 10/13 August 2026) gives 41.6% → 67.2%, and the Lean-checked value is 67.25007%.
- Change to: "although in September the number theorist Youness Lamzouri published a new and, in his words, conceptually simpler proof of the same bound, together with two new estimates that the Claude paper does not contain"

## SHOULD change

### S1. "closes the gap on which the objections to OpenAI's result turn" is unclear
- Where: textbook/chapters/ch06.md:231
- Text now: "If it holds, it closes the gap on which the objections to OpenAI's result turn."
- Problem: UNCLEAR. An unforced blow-up proof by different authors does not repair OpenAI's result. It would settle the Millennium problem independently, under an alternative that needs no external force. The sentence also implies that the forcing is the only objection, but the text has just described the Lean-versus-prose objection as well.
- Evidence: Tao, 20 November 2026 (terrytao.wordpress.com/2026/11/20/…): the paper is "technically human-readable", and more work is needed before it is a professionally written proof. TNW, 21 November 2026: the certificate of numerical data is not yet released, and the Lean package was not rebuilt after the 20 November patch.
- Change to: "If it holds, it would settle the problem without the external force on which much of the objection to OpenAI's result turns."

### S2. The "obvious cynical view" is left unstated
- Where: textbook/chapters/ch06.md:231
- Text now: "The release came one day after Anthropic's stock-market debut; Alpöge rejected what he called the \"obvious cynical view\" of the timing [@constantin2026riemann]."
- Problem: UNCLEAR / balance. The reader is not told what the cynical view is. Nature reported a named critic, Andrew Granville, linking the timing to the share price, which fell after the debut. Granville also called the release "garbled". Stating the view keeps the treatment of the Anthropic-linked claim as candid as the treatment of OpenAI's. The dates are confirmed: the Anthropic IPO was on 19 November 2026 (Fortune, BNN Bloomberg) and the release on 20 November.
- Evidence: TNW, 21 November 2026: "The claim came one day after Anthropic's record stock market debut, and Anthropic's shares later fell." Alpöge: "There is an obvious cynical view, to do with the timing, but it is false." Nature news d41586-026-03812-7 (paywalled; seen in search summary): Granville, "What he released is garbled", and his view that the timing was tied to the fall in the company's stock.
- Change to: "The release came one day after Anthropic's stock-market debut, and as its shares were falling; some mathematicians suggested a link, which Alpöge rejected as the \"obvious cynical view\" [@constantin2026riemann]."

### S3. Unit-distance result: Gowers's caveat from the same source is omitted
- Where: textbook/chapters/ch06.md:214
- Text now: "and Timothy Gowers wrote that he would have recommended it to the *Annals of Mathematics* \"without any hesitation\" had a human submitted it [@lee2026stunning]."
- Problem: UNCLEAR / balance. The cited article also quotes Gowers saying "Many of the ideas needed for the proof were present in the literature already." Leaving this out makes the OpenAI result look more original than its strongest endorser said. This is in OpenAI's favour, so it is included here for symmetry.
- Evidence: https://www.sciencealert.com/stunning-ai-solution-for-80-year-old-problem-shocks-mathematicians (28 May 2026, from The Conversation): "Many of the ideas needed for the proof were present in the literature already."
- Change to: "…\"without any hesitation\" had a human submitted it, while noting that \"many of the ideas needed for the proof were present in the literature already\" [@lee2026stunning]."

## Could not verify
- Nature news d41586-026-03812-7 (Granville quotations) was paywalled. I saw the wording only in a search summary, so check it before using the S2 wording beyond what TNW supports.
- Cheetham and Seshadri's "first 250 of 2,047 entries" and the random sample of ten from 384,870 (paywalled *Chem. Mater.*).
- NHC 2025 verification details for the Google DeepMind ensemble (a large PDF that I did not open), and Juelsholt's identification of the 1971 phase.
- The Erdős #728 preprint quotation and Tao's "1–2%" estimate on Mathstodon (consistent with my recollection, but not re-fetched).

## Checked and confirmed
- Nobel citations and dates; AlphaFold DB "over 214 million"; 2 million users in 190 countries; CASP14 0.96/2.8 Å and 1.5/3.5 Å, 87 domains; AF3 chirality 4.4%; ProteinMPNN 52.4% vs 32.9%; Boltz-1.
- GraphCast: 227 variables (5+6×37), 36.7M parameters, 90% of 1,380 targets, 96.9% of 1,280 without 50 hPa, 88.0% after blurring, 40 six-hour steps; GenCast 97.2% of 1,320 targets, 8 min on TPU v5; AIFS dates.
- GNoME 2.2M/381,000/421,000/736; A-Lab 41/58 over 17 days; Author correction (online 19 January 2026): "not necessarily new to science", 36 of 40 confirmed, 4 inconclusive; MatterGen TaCr₂O₆, 169 GPa.
- AlphaGeometry 25/30; AG2 54%→84%; IMO 2024 28/42; IMO 2025 claims and dates; Seed-Prover; USAMO 2025 25%.
- MathArena USAMO 2026: GPT-5.4 95.2%, Gemini 3.1 Pro 74.4%, Opus 4.6 47.0%, open model 44.6%, self-overrating, Google grant. AFP IMO 2026: Celia, dots-note-3.0, "strictly prohibited", informal 42/42 tests.
- FunSearch 512 points, 4 of 140 runs; AlphaEvolve figures; DeepMind 9 of 353 Erdős problems; Litt and Gowers quotations.
- Anthropic zeta bound (Alpöge, Furman, Conrey, Goldston; Lean).
- Navier–Stokes: Quanta (10,000 agents, 88 h, 17 h Lean); OpenAI blog quotations ("report on the substantial progress", "do not intend to claim the Millennium Prize", "after hearing a rumor", "priority … forced Euler", "did not see any of their work…", 10 September update "could not have influenced…"); OfficeChai "cannot rule out"; SciAm Bubeck quotation and "may have been overblown"; Buckmaster statement (personal collaboration, 15 August, Córdoba/Martínez-Zoroa, "I am not accusing anyone of anything", the timing as OpenAI conceded it to him); EMS and Clay quotations; Fields Medal letter (11 September, 25 medallists).
- Riemann hypothesis: release 20 November; Lean FRO/Mathlib joint statement 21 November (statement matches Mathlib's RiemannHypothesis; several independent checkers; GRH not addressed); 17M lines and four-page note; Maynard "98 or 99 percent" (per NYT via TNW); Conrad "frankly completely outrageous"; Tao ranks GRH "least digested"; Anthropic IPO 19 November 2026.
- Hao et al. (41.3M papers, 3.02×, 4.84×, 1.37 y, 4.63%, 22%); Kosmos percentages; Si et al.; Beel et al.; Kapoor & Narayanan (17 fields, 294 papers).
- Internal consistency: Ch14 refers to "Section 6.6" for Navier–Stokes, which is correct.

## Tally
Claims checked: ~85 · confirmed: ~80 · wrong: 1 (M1) · unclear or balance: 3 · outdated: 0 · unverified: 4
