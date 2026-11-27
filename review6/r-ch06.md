# Review 6: Chapter 6, AI for Science, Mathematics and Engineering

## Verdict
Ready to print after three small SHOULD fixes. Nothing is wrong, misquoted or legally risky enough to block printing. The most sensitive material is the Navier–Stokes credit dispute and the Riemann-hypothesis claims of 20–21 November 2026. I checked those against the primary documents: Buckmaster's statement PDF, OpenAI's page and manuscript, the Lean FRO certification, the Fields Medallists' letter on Tao's blog, and the Clay, EMS and KCL statements. The book's wording matches them.

**Balance between companies.** The chapter states its Google DeepMind concentration openly. The two companies at the centre of the 2026 mathematics claims, OpenAI and Anthropic, get the same treatment:
- OpenAI's results (unit-distance disproof, quasi-RH, Navier–Stokes) are credited, with the strongest expert praise quoted (Litt, Gowers; "Experts … largely agreed that the shorter proof is correct").
- The Anthropic-linked Riemann-hypothesis claim gets the harshest criticism in the chapter (Conrad's "frankly completely outrageous"; "machine certification, not mathematical acceptance").
- In the credit dispute, the book gives OpenAI's denials and its later investigation in full. It quotes Buckmaster's "not accusing anyone of anything". It does not repeat the sharper allegations in Buckmaster's statement, for example that OpenAI wanted Alpöge, an Anthropic employee, removed from authorship. That restraint is appropriate for legal reasons and does not tilt toward Anthropic.
- I found one small under-statement of Anthropic (S2) and one of OpenAI (S3). Neither is a pattern.

## MUST change before printing
None.

## SHOULD change

### S1. A "late November" status claim cited to an October article
- Where: textbook/chapters/ch06.md:231
- Text now: "As of late November 2026, research groups were still examining the paper and the Lean code [@howlett2026openais]."
- Problem: UNSUPPORTED (as dated) — the cited *Scientific American* article is dated 13 October 2026. It supports "in mid-October", not "late November".
- Evidence: https://www.scientificamerican.com/article/openais-blockbuster-navier-stokes-proof-isnt-what-we-thought-it-was/ (13 Oct 2026: "more than a month later, no one fully does"; several research groups are using the paper and the Lean code to obtain overviews).
- Change to: "In mid-October 2026, research groups were still examining the paper and the Lean code [@howlett2026openais], and no peer-reviewed assessment had appeared by late November."

### S2. Anthropic's zeta-zeros result: outside reviewers left out
- Where: textbook/chapters/ch06.md:214
- Text now: "two of its mathematicians, Levent Alpöge and Ralph Furman, examined the work. That is a company claim, although …"
- Problem: UNCLEAR (incomplete; this is over-correction, not favouring) — Anthropic's post says two outside specialists, Brian Conrey and Dan Goldston, also examined the paper. A chapter that values independent checks should say so, and should keep the "company claim" caveat because neither review was formal peer review.
- Evidence: https://www.anthropic.com/research/riemann-zeta (10 Aug 2026; updated 13 Aug): Alpöge and Furman examined the work; "Brian Conrey and Dan Goldston, outside experts in this area, also examined the paper on short notice".
- Change to: "two of its mathematicians, Levent Alpöge and Ralph Furman, examined the work, and two outside specialists, Brian Conrey and Dan Goldston, read it on short notice. It has not been peer-reviewed, although …"

### S3. "It gave no reason" for not claiming the Millennium Prize
- Where: textbook/chapters/ch06.md:223
- Text now: "OpenAI said: \"We do not intend to claim the Millennium Prize for this result.\" It gave no reason;"
- Problem: UNCLEAR — the sentence just before it on OpenAI's page gives the release's purpose: "Our goal in releasing this result is to report on the substantial progress of our AI models." This is not a reason about the forcing question, but "no reason" is slightly unfair to OpenAI.
- Evidence: https://openai.com/index/navier-stokes-solution/ ("Progress and responsibility" section).
- Change to: "OpenAI said that its goal was \"to report on the substantial progress of our AI models\" and that \"We do not intend to claim the Millennium Prize for this result.\" It did not say why;"

## Could not verify
- Tao's Mastodon phrases "long tail", "many of which actually have straightforward solutions", "unlikely to be reported on any public site" and the 1–2% estimate. They are not in the cited 7 Jan 2026 thread (I read the full thread through the API), so they may come from another post. The bib entry covers several posts, so I am not flagging them as wrong.
- Mathlib's "more than 290,000 theorems" in November 2026 (the statistics page renders by script). The 28-signatory count at mathandai.org. GraphCast's 96.9%/88.0% sub-figures (not re-checked this round).
- The Bubeck quote "We did not use their prompt or proofs to prompt our models" is confirmed in *Scientific American*, but not on OpenAI's own page. The citation set covers it.

## Checked and confirmed
- Navier–Stokes manuscript: 166 pages; starts from rest; compactly supported smooth force; states alternatives (C) and (D) per Fefferman. Quanta: about 10,000 agents, 88 h, Lean in 17 h (8 Sept 2026).
- OpenAI page: the "do not intend to claim" quote; effort began on 1 September "after hearing a rumor"; "the priority of their work on forced Euler"; "did not see any of their work through any means…"; "could not have influenced the system in any way, including through training". Officechai: "cannot rule out" in the first statement.
- Buckmaster statement: personal collaboration; Claude and Codex/GPT-5.6 Sol/Astra; 15 August; Córdoba and Martínez-Zoroa credited; "after information about our work had reached OpenAI"; "I do not know whether our data was used. I am not accusing anyone of anything."
- EMS (10 Sept): "milestone", authorship and credit, "internal to OpenAI and not generally accessible". Clay (11 Sept): "apparently been settled", deliberately slow review. KCL (27 Oct): Bastounis/Circelli/Hansen; "have not shown that OpenAI's original proof is wrong".
- Fields letter (Tao blog, 11 Sept 2026): 25 initial signatories including Tao, Scholze and Viazovska. All three quoted phrases are verbatim.
- 20–21 Nov 2026: Buckmaster–Alpöge unforced Navier–Stokes ("unpolished and heavily LLM-assisted"; numerical certificate not yet released). Alpöge's RH/GRH claim (17M-line Lean library, four-page note). Lean FRO/Mathlib joint certification of RH against Mathlib's statement with independent checkers, silent on GRH; GRH covers Dirichlet L-functions per TNW. Tao lists the results "in decreasing order of how 'digested'", GRH last. Conrad quote.
- Anthropic zeta 41.6% → 67.2% with Lean, method not expected to prove RH. Lamzouri (arXiv 2609.02882): "conceptually simpler", over 67.25% simple and on the line.
- Quasi-RH: 1/8–7/8 Lean-verified, 1/12–11/12 human-edited; experts largely agree; Sarnak "a Theorem".
- Unit distance: Litt and Gowers quotes; Sawin about 1.014 (arXiv 2605.20579); 10^2,000,000; *The Conversation* via ScienceAlert. Tsoukalas et al. 9 of 353 (21 May 2026).
- Erdős #728: GPT-5.2 Pro + Aristotle, Lean; Tao on exposition; Pomerance 2014 note. Bloom 2025 quotes.
- IMO 2026 (AFP, 23 July 2026): Shanghai; Celia and dots-note-3.0 at 42/42; "strictly prohibited"; submitted to organisers; Deedy Das informal tests. MathArena USAMO 2026: 95.2/74.4/44.6, three-model jury with manual review, self-overrating, Google grant.
- Weather: NOAA (17 Dec 2025): GraphCast base, 99.7% less computing, 9% of GEFS, 18–24 h, "comparable", "a degradation in tropical cyclone intensity forecasts", hybrid best. AIFS v2 live 12 May 2026 with wave and snow cover. NHC 2025: GDMI slightly better than official Atlantic track at 12–72 h, comparable on intensity. WeatherNext Cyclones (*Nature*, 6 Aug 2026): 1 day or more of lead time, 2023–2025.
- Materials: A-Lab correction (19 Jan 2026): "not necessarily new to science", 36 of 40 confirmed, 4 inconclusive. Juelsholt in *Materials Horizons* 2026.
- Hao et al. (*Nature*, Jan 2026): 41.3M papers, F1 0.875, 3.02×, 4.84×, 1.37 years, 4.63%, 22.00%, "toward areas richest in data". Lu et al. (*Nature*, 25 Mar 2026). Co-Scientist (*Nature*, 19 May 2026).
- Older results (AlphaFold CASP14 figures, AF3 caveats, GNoME counts, Cheetham–Seshadri, MatterGen, FunSearch, AlphaEvolve, AlphaGeometry 1/2, IMO 2024/2025, USAMO 2025, Sakana/Beel, Si et al., Kosmos, Kapoor–Narayanan) agree with the primary sources as I know them.
- Arithmetic: Kosmos sub-rates are consistent. A-Lab 41 → 40 (one removed) → 36. Table 6.2 entries match the text.
- Consistency: AlphaFold is described compatibly in ch01. No conflicting accounts of the 2026 mathematics claims elsewhere in the book.

## Tally
Claims checked: 112 / confirmed: 109 / wrong: 0 / outdated or imprecise: 3
