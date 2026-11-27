# Review 9 — Chapter 6: AI for Science, Mathematics and Engineering

## Verdict
Ready to print after one MUST fix. The cited USAMO 2025 preprint was revised on 25 November 2026, and its current version contradicts the book's "all others below 5%". The fix is one sentence plus a table cell, or simply pinning the citation to the earlier version. The sensitive 2026 material held up when checked against the primary sources: the Navier–Stokes credit dispute, the Fields Medallists' letter, the Lean FRO certification of the Riemann hypothesis, the IPO-timing remark, and Anthropic's and OpenAI's zeta-function results. Quotations in that material are verbatim, and the legally delicate passages are carefully hedged. Buckmaster's "not accusing anyone of anything" and OpenAI's denial are both given. The book rightly leaves out the most inflammatory parts of Buckmaster's statement.

**Balance between companies.** Even-handed, with no sign of over-correction. The chapter says at the outset that most showcase results come from Google DeepMind, and it then subjects DeepMind's work to independent tests: GNoME, AlphaChip and AlphaFold's limits. OpenAI's mathematics claims get heavy scrutiny (the Erdős "misrepresentation", the Navier–Stokes box), but each critical point is sourced and OpenAI's side is quoted. Anthropic's claims get matching caveats. The August zeta result is "not peer-reviewed". Alpöge's Riemann claim is labelled "machine certification, not mathematical acceptance", with Conrad's "frankly completely outrageous", the IPO-timing question, and the disclosure that Alpöge works at Anthropic both in the credit dispute and in the RH paragraph. The MathArena paragraph states plainly that Claude Opus 4.6 scored 47% against GPT-5.4's 95%, and that Claude was one of two judges that overrated their own answers. One small point: Alpöge's Lean-certified RH claim, arguably the month's biggest mathematical news, sits inside the OpenAI Navier–Stokes box rather than in the main text. That placement is a matter of structure, not bias, and I do not flag it.

## MUST change before printing

### M1. USAMO 2025 results: the cited preprint now reports four models above 5%, best 30%
- Where: textbook/chapters/ch06.md:182 and Table 6.2, line 176
- Text now: "In their preprint, only Gemini 2.5 Pro, released after the contest and added in a later version, reached a non-trivial score of 25%; all others scored below 5%." Table: "Best model 25%; all others below 5%"
- Problem: OUTDATED / now VERIFIED WRONG against the cited source — arXiv:2503.21934 was revised to v6 on 25 November 2026. The bib entry has no version, so the link now opens v6. Table 1 of v6 (average of four runs, out of 42) reads: DeepSeek-R1 (05/28) 12.6 (30.0%), Gemini 2.5 Pro 10.3 (24.5%), o3 9.1 (21.7%), o4-mini 8.0 (19.0%); all others ≤ 2.0 (< 5%). The text says "Only four models … scored above 5%". The book's sentence matches v4–v5 only. The underlying point, that public models lagged far behind in early 2025, still stands, because all four were released after the contest.
- Evidence: https://arxiv.org/abs/2503.21934v6 (25 Nov 2026), Table 1, and: "Only four models — Gemini-2.5-Pro, o3, o4-mini, and DeepSeek-R1 (05/28) — scored above 5%"; abstract: "none exceeding a score of 30%, and most achieving only trivial scores below 5%".
- Change to (text): "In the latest version of their preprint, only four models, all released after the contest (DeepSeek-R1 in its May 2025 version, Gemini 2.5 Pro, o3 and o4-mini), reached non-trivial scores, between 19% and 30%; all others scored below 5%."
  Table cell: "Best model 30% (three others 19–25%); all others below 5%"
- Alternative minimal fix: keep the text and pin the version in the bib entry: `howpublished = {arXiv preprint arXiv:2503.21934v5, 4 September 2025}`, `url = {https://arxiv.org/abs/2503.21934v5}`.

## SHOULD change

### S1. Riemann hypothesis: independent checks after 21 November also cover the generalisation
- Where: textbook/chapters/ch06.md:231
- Text now: "Their statement did not address the generalisation" … "By late November no complete human-readable proof or peer review existed, and no mathematician had explained the argument."
- Problem: OUTDATED (changed just after the book's cut-off) — the Lean FRO/Mathlib statement indeed covers only RH. However, Michael Rubinstein (Waterloo) and Andrew Sutherland (MIT) have since reported that independent kernel checks passed for all five theorems, including GRH for Dirichlet L-functions. On 25 November Luke Sernau and colleagues posted a compact rewrite of about 76,000 lines, which also passed Comparator (26 Nov). A partial explanatory paper on the zeta case appeared as a working draft on 22 November; it reduces the main inequality to 13 hypotheses and does not prove them, so "no complete human-readable proof" remains true.
- Evidence: https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/ (21–26 Nov 2026): the checks cover "RH and GRH for Dirichlet L-functions"; "Comparator reported 'Your solution is okay!'"; https://leanprover-community.github.io/blog/posts/riemann-hypothesis/ (21 Nov 2026).
- Change to: after "Their statement did not address the generalisation", add: "; independent checks reported over the following days, by Michael Rubinstein at Waterloo and Andrew Sutherland at MIT, found that the Lean proofs of both parts compile and are accepted by several independent checkers, and a compact 76,000-line rewrite appeared on 25 November [@rubinstein2026alpoge]". New bib entry:
  ```
  @misc{rubinstein2026alpoge,
    author       = {Rubinstein, Michael},
    title        = {{Alpöge}/{Claude} Proof of the Generalized {Riemann} Hypothesis: Verification Notes},
    year         = {2026},
    howpublished = {University of Waterloo web page, updated 26 November 2026},
    url          = {https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/},
    urldate      = {2026-11-27}
  }
  ```
  (Optional. If the author prefers to keep the stated cut-off, leave as is.)

### S2. Tao's ranking: "of the month's results" overstates what he ranked
- Where: textbook/chapters/ch06.md:231
- Text now: "Terence Tao ranked it the least digested of the month's results"
- Problem: UNCLEAR — Tao's 20 November post ranks three specific results (unforced Euler, unforced Navier–Stokes, GRH) "in decreasing order of how 'digested' the results currently are". It does not rank all of the month's results.
- Evidence: https://terrytao.wordpress.com/2026/11/20/unforced-euler-singularity-unforced-navier-stokes-singularity-and-the-generalized-riemann-hypothesis/ — "in decreasing order of how 'digested' the results currently are … I imagine the digestion process will take some time."
- Change to: "Terence Tao placed it last of the three results announced that day in order of how far they had been 'digested'"

## Could not verify
- One secondary report says the DeepMind Erdős paper (Tsoukalas et al.) appeared in *Science* on 8 October 2026. I could not confirm this. If it is true, the citation at line 214 could be updated from the arXiv preprint.
- I could not fetch the A-Lab author correction (*Nature*, paywalled redirect); its figures (36 confirmed, 4 inconclusive, 1 removed) were not re-checked this round.
- GraphCast "96.9% excluding 50 hPa" was not re-checked against the paper this round.

## Checked and confirmed
- Buckmaster statement (NYU PDF, 7 Sept 2026): 15 August Euler/Boussinesq results with smooth forcing; building on Córdoba and Martínez-Zoroa; personal capacity; several companies' LLMs; "after information about our work had reached OpenAI"; "I am not accusing anyone of anything".
- OpenAI Navier–Stokes post: "substantial progress of our AI models", "We do not intend to claim the Millennium Prize", "after hearing a rumor", "priority of their work on forced Euler", "did not see any of their work through any means", 10 Sept update "could not have influenced the system in any way, including through training". About 10,000 agents, 88 h, 17 h Lean (multiple sources).
- KCL release: "have not shown that OpenAI's original proof is wrong"; KCL and Cambridge authors.
- Fields letter (mathandai.org): "the push by AI companies to solve mathematical problems as a benchmark is detrimental to the science of mathematics", "announced in a rush", "severe attribution and plagiarism questions" — verbatim. Tao, Scholze and Viazovska are signatories.
- Lean FRO/Mathlib (21 Nov 2026): certifies RH statement and proof; statement is "exactly Mathlib's statement"; several checkers; GRH not addressed.
- TNW (21 Nov): "one day after Anthropic's record stock market debut"; shares fell on Friday 20 Nov; "obvious cynical view"; Maynard "98 or 99 percent"; Conrad "frankly completely outrageous"; four-page note. The IPO debut was 19 Nov 2026 (Nasdaq, record size).
- Tao 20 Nov post: the three results and the digestion ranking (see S2).
- Anthropic zeta post (10 Aug, updated 13 Aug): 41.6% → 67.2%; unreleased model; Lean; Alpöge, Furman; Conrey and Goldston "on short notice"; no expectation of an RH proof.
- Quanta on quasi-RH: 1/8–7/8 Lean-verified (199 pp.); 1/12–11/12 human-edited and not verified (49 pp.); experts largely agree; Sarnak will not call it "a Theorem" until humans check.
- MathArena USAMO 2026 (28 Mar 2026): GPT-5.4 95.2%, Gemini 3.1 Pro 74.4%, Opus 4.6 47.0%, best open model (Step-3.5-Flash) 44.6%; three-model jury; every solution checked by hand; Gemini and Opus overrated themselves; Google grant disclosed.
- AFP (23 July 2026, Shanghai): Huawei Celia and Xiaohongshu dots-note-3.0 at 42/42; "strictly prohibited"; submitted to organisers; Deedy Das's informal tests (OpenAI, Anthropic, Axiom, Moonshot).
- Unit-distance (ScienceAlert/Conversation): Litt and Gowers quotes; 10^2,000,000.
- DeepMind AlphaProof Nexus: 9 of 353 open Erdős problems (arXiv 2605.22763, May 2026).
- ECMWF AIFS v2: 12 May 2026; "first data-driven wave and snow cover forecasts".
- mathlib: 296,856 theorems (above 290,000).
- Earlier-era figures consistent with sources: CASP14 0.96/2.8/1.5/3.5 Å; GenCast 97.2% of 1,320; AIFS 25 Feb 2025; AIFS ENS 1 Jul 2025; Si et al. 5.64 vs 4.84, 79 reviewers, 43 executors; Hao et al. 41.3M papers, 3.02×/4.84×/1.37 y/4.63%/22%.
- Cross-references: Section 6.6 cited from Ch. 14 is correct; Chapter 7 (TPU) and Chapter 10 (health) are correct.

## Tally
Claims checked: 64 / confirmed: 60 / wrong (now, against the cited source): 1 (M1) / outdated by post-cut-off developments: 1 (S1) / imprecise: 1 (S2) / not verified: 3
