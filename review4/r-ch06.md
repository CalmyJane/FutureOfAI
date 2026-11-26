# Chapter 6: AI for Science, Mathematics and Engineering (fourth review)

## Verdict

**Ready to print after small fixes.** This is an accurate, even-handed chapter. I checked the sensitive Navier–Stokes case box line by line against Buckmaster's statement, OpenAI's blog (including the 10 September update), *Scientific American*, *Quanta*, KCL, the Clay Institute, the EMS and the open letter. It quotes both sides accurately and does not go beyond what the sources say. I found no MUST-level error.

The main SHOULD item is currency. On 20 November 2026, the same day as the last event the chapter reports, Levent Alpöge announced a claimed Lean proof of the Riemann hypothesis found with Claude. In August 2026 Anthropic had also reported that Claude raised the proven share of zeta zeros on the critical line from 41.6% to 67.2%. Neither appears in a chapter that covers the comparable OpenAI and Google results in detail. The other three items are wording and attribution fixes.

## MUST change before printing

None.

## SHOULD change

### S1. Omission: the 20 November 2026 Riemann-hypothesis claim and the August 2026 zeta-zeros result
- Where: textbook/chapters/ch06.md:231 (end of the Navier–Stokes box) and §6.6 (around l.214)
- Text now (231, last sentences): "On 20 November 2026 Buckmaster and Alpöge posted an AI-assisted proof that the equations can blow up with no external force at all. … no independent expert had confirmed it [@hall2026ai; @thenextweb2026navierstokes]."
- Problem: OUTDATED / incomplete, with a balance issue. On the same day Alpöge claimed a proof of the Riemann hypothesis (and the Generalized RH) with Claude, released only as Lean code. That is the most prominent AI-mathematics claim of late November 2026, and the chapter, current to late November, does not mention it. Separately, Anthropic reported in August 2026 that Claude raised the lower bound on the proportion of zeta zeros satisfying RH from 41.6% to 67.2%. The chapter covers OpenAI's unit-distance and Navier–Stokes results and Google DeepMind's Erdős work in detail, but no Anthropic result, so readers get a lopsided picture.
- Evidence:
  - https://thenextweb.com/news/anthropic-alpoge-claude-riemann-hypothesis-proof-lean (21 Nov 2026): "Levent Alpöge, a mathematician at Anthropic, says he has proved the Riemann hypothesis with the company's AI model Claude… The proof itself is out only as code for Lean… One automated check, a comparator run, was still pending… Brian Conrad, a Stanford mathematician, criticised the release… 'frankly completely outrageous'".
  - https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/ (20 Nov 2026).
  - https://www.anthropic.com/research/riemann-zeta (Aug 2026): "An unreleased research version of Claude has improved on a longstanding lower bound for the fraction of zeros of the Riemann zeta function that satisfy the Riemann hypothesis… from 41.6% to 67.2%… Claude also produced a formally verifiable proof… We don't expect that the techniques Claude used will lead to proving the Riemann hypothesis."
- Change to: after "…no independent expert had confirmed it [@hall2026ai; @thenextweb2026navierstokes]." add: "The same day Alpöge announced that, working with Anthropic's Claude, he had found a proof of the Riemann hypothesis, released only as Lean code with no human-readable paper; early independent compilations of the code raised no problems, but a check that the formal statement matches the hypothesis was still pending, and some mathematicians criticised publishing a proof its author did not yet fully understand [@constantin2026riemann]." In §6.6, after the unit-distance paragraph (l.214), add: "In August 2026 Anthropic reported that an unreleased Claude model had raised the proven share of zeros of the Riemann zeta function that lie on the critical line from 41.6% to 67.2%, with a Lean proof; the company said it did not expect the method to lead to a proof of the Riemann hypothesis itself [@anthropic2026riemann]."
  New bib entries (ch06.bib):
  ```
  @misc{constantin2026riemann,
    author       = {Constantin, Ana Maria},
    title        = {{Anthropic} Mathematician Says He and {Claude} Proved the {Riemann} Hypothesis},
    year         = {2026},
    howpublished = {The Next Web, 21 November 2026},
    url          = {https://thenextweb.com/news/anthropic-alpoge-claude-riemann-hypothesis-proof-lean},
    urldate      = {2026-11-26}
  }
  @misc{anthropic2026riemann,
    author       = {{Anthropic}},
    title        = {Claude and the {Riemann} Zeta Function},
    year         = {2026},
    howpublished = {Company research post (company source), August 2026},
    url          = {https://www.anthropic.com/research/riemann-zeta},
    urldate      = {2026-11-26}
  }
  ```
  (Check the exact title of the Anthropic post before printing.)

### S2. The Xiaohongshu quotation is attached to a different claim
- Where: textbook/chapters/ch06.md:184
- Text now: "Xiaohongshu said it had submitted its solutions to IMO organisers for grading, \"under the IMO's official judging process\";"
- Problem: MISQUOTED (context). In the AFP report, "under the IMO's official judging process" belongs to the claim that "no large language model had ever achieved a perfect score" under that process. It is not part of the statement that the solutions were submitted for grading. The facts are right, but the quotation is spliced.
- Evidence: AFP via The Standard, 23 Jul 2026 (https://www.thestandard.com.hk/world/article/338012/AI-catches-up-with-humans-to-score-100-at-top-maths-contest): "'Previously, no large language model had ever achieved a perfect score under the IMO's official judging process,' the firm added" and "'During testing, any form of human intervention was strictly prohibited,' and the AI solutions were submitted to IMO organisers for grading, Xiaohongshu said."
- Change to: "Xiaohongshu said that human intervention had been \"strictly prohibited\" and that it had submitted its solutions to IMO organisers for grading;"

### S3. ECMWF: "Version 2 of both" goes beyond the source
- Where: textbook/chapters/ch06.md:91
- Text now: "Version 2 of both, live since 12 May 2026, adds what ECMWF calls its first data-driven wave and snow-cover forecasts [@ecmwf2026significant]."
- Problem: UNCLEAR. The release announces "an update to the Artificial Intelligence Forecasting System (AIFS v2)" alongside IFS Cycle 50r1. It does not say that the ensemble and the single model are each at "version 2".
- Evidence: https://www.ecmwf.int/en/about/media-centre/news/2026/ifs-cycle-50r1-aifsv2-live (12 May 2026): "A significant upgrade to ECMWF's Integrated Forecasting System (IFS), Cycle 50r1, has gone live today (12 May 2026) alongside an update to the Artificial Intelligence Forecasting System (AIFS v2)… The update to the AIFS introduces, among other features, ECMWF's first data-driven wave and snow cover forecasts."
- Change to: "An update to the system, AIFS v2, live since 12 May 2026, adds what ECMWF calls its first data-driven wave and snow-cover forecasts [@ecmwf2026significant]."

### S4. The date of Buckmaster's statement
- Where: textbook/chapters/ch06.md:225 and bib/ch06.bib entry `buckmaster2026statement` (howpublished "8 September 2026")
- Text now: "Hours before OpenAI's announcement, Tristan Buckmaster of New York University released a statement…"
- Problem: INCONSISTENT (minor). *Scientific American* dates the statement to Monday 7 September, "the night before" OpenAI's announcement on Tuesday 8 September. The Next Web says the forced results were posted "one day before". The text is defensible, but the bib date is probably wrong.
- Evidence: https://www.scientificamerican.com/article/openai-claims-blockbuster-math-breakthrough-amid-swirl-of-controversy/ (8 Sep 2026): "The night before OpenAI announced the proof, Buckmaster posted… In a statement released on Monday, Buckmaster alleged…". https://thenextweb.com/news/navier-stokes-blow-up-without-force-buckmaster-alpoge (21 Nov 2026): "In September, Buckmaster and Alpöge posted their forced results one day before OpenAI announced its proof."
- Change to: "The evening before OpenAI's announcement, Tristan Buckmaster…". In the bib, set howpublished = {Personal statement (PDF), New York University, 7 September 2026}.

## Could not verify

- Juelsholt (2026): that TaCr₂O₆ is "identical to a disordered phase first reported in 1971". The Crossref title and abstract support the overall finding ("MatterGen predicts compounds from the training dataset"). The year 1971 was not checked.
- Openai2026finite: "stirred by a smooth external force confined to a bounded region" (l.221). I did not read the 166-page manuscript. OpenAI's blog says only "a smooth force applied to the fluid".
- Storm Ciarán "caused sixteen deaths"; Terwilliger "102 crystal structures … median 0.6 Å … about 10% >2 Å"; GraphCast "96.9%" and "88.0%". All are consistent with my recollection of the papers but were not re-fetched.
- Tao's "long tail" and "1–2%" posts: I confirmed the root post of 7 Jan 2026 only.

## Checked and confirmed

- Navier–Stokes box:
  - OpenAI blog (8 Sep, updated 10 Sep 2026): "effort began on September 1st after hearing a rumor"; "recognize the priority of their work on forced Euler"; "did not see any of their work through any means until they released it publicly"; "could not have influenced the system in any way, including through training"; "We do not intend to claim the Millennium Prize for this result"; ~10,000 agents, 88 h, Lean in 17 h with GPT-6 Astra; claims of (C) and (D).
  - Buckmaster statement: personal collaboration; Córdoba and Martínez-Zoroa programme; blow-up 15 August; OpenAI's attempt began "after information about our work had reached OpenAI"; "I do not know whether our data was used. I am not accusing anyone of anything."
  - SciAm 8 Sep: Bubeck "We did not use their prompt or proofs to prompt our models". OfficeChai: "cannot rule out".
  - SciAm 13 Oct: "no one fully does" understand the proof; "the company's proof does not follow the Spanish program".
  - KCL release: "have not shown that OpenAI's original proof is wrong"; authors Bastounis, Circelli and Hansen.
  - Clay Institute (11 Sep): "apparently been settled"; "deliberately unhurried".
  - EMS: "internal to OpenAI and not generally accessible".
  - Open letter (Zenodo, 11 Sep): both quotations; 28 signatories (all Fields medallists) including Tao, Scholze and Viazovska.
  - 20 Nov unforced proof: "unpolished and heavily LLM-assisted"; certificate not yet released.
- Unit-distance result (20 May 2026): Litt and Gowers quotations; Sawin n^1.014, submitted the same day; ~10^2,000,000 points; DeepMind 9 of 353 Erdős problems (Tsoukalas et al.).
- MathArena USAMO 2026: GPT-5.4 95.2%, Gemini 3.1 Pro 74.4%, best open model 44.6%; Google grant; self-bias of judges.
- AFP IMO 2026: Celia and dots-note-3.0 at 42/42; tested after the contest within a time limit; Deedy Das's informal tests with OpenAI, Anthropic, Axiom and Moonshot.
- A-Lab author correction (Nature, 19 Jan 2026): "not necessarily new to science"; 36 of 40 confirmed, 4 inconclusive; Zn₂Cr₃FeO₈ removed.
- Hao et al. (Nature, 14 Jan 2026): F1 0.875; 41.3M papers; 3.02×, 4.84×, 1.37 years; 4.63%; 22%; "areas richest in data".
- AI Scientist (Nature, 25 Mar 2026): passed first round; 70% acceptance rate. Co-Scientist in Nature, 19 May 2026. WeatherNext Cyclones in Nature, 6 Aug 2026 ("lead-time advantage of 1 day or more"). Georgiev et al. in PNAS, 30 Sep 2026 (67 problems). AlphaProof in Nature, 12 Nov 2025 (quotations match).
- Kosmos: 12 h; 42,000 lines; 79.4%; authors' estimate 4.1 months and collaborators' 6.14 months (so "four to six months" is fair).
- ECMWF: AIFS operational 25 Feb 2025, "up to 20%", ~1,000× less energy, same initial conditions as the IFS. AIFS ENS on 1 Jul 2025: 31 km against 9 km, "remains indispensable", "over 10 times faster".
- NOAA (17 Dec 2025): GraphCast as foundation; 99.7%/0.3%; 9% of GEFS computing; "Early results… additional 18 to 24 hours" and "comparable"; "degradation in tropical cyclone intensity forecasts"; HGEFS "most major verification metrics". NWS SCN 26-68 (27 Jul 2026): improves intensity and reduces blurring.
- NHC 2025 verification: GDMI slightly better than official Atlantic track forecasts at 12–72 h; best intensity model, comparable with the official forecasts.
- Mathlib: 296,731 theorems (">290,000").
- Older material, consistent with the primary papers as I know them: AlphaFold 2 and 3 figures and quotations; AFDB 214M; Nobel citations and the 2 million users; GNoME and Cheetham–Seshadri numbers; MatterGen 200/169 GPa; AlphaGeometry 1 and 2; IMO 2024 and 2025 table entries; FunSearch 512 points and 4 of 140 runs; AlphaEvolve 48 multiplications, 0.7%, 23%/1%; Si et al.; Beel et al.; Kapoor and Narayanan 17 fields and 294 papers; NeuralGCM quotation.
- Cross-references: Ch2, Ch3, Ch7 (TPU), Ch10 (health) and §6.5/§6.6/§6.9 references are correct. The AlphaFold quotation in Ch1 l.234 is consistent.

## Tally

Claims checked: 104 · confirmed: 96 · wrong: 0 · outdated/omitted: 1 (S1) · misquoted (context): 1 (S2) · unclear/inconsistent: 2 (S3, S4) · could not verify: 4 groups
