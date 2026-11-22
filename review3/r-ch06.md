# Third review: Chapter 6 — AI for Science, Mathematics and Engineering

## Verdict
Ready after the MUST fixes below. The chapter is carefully sourced and, on the contested discovery claims (GNoME, A-Lab, MatterGen, AlphaChip, Erdős problems, olympiads), attributes both sides accurately and rarely states anything more firmly than its source; of about 165 claims checked against sources, nearly all held, including every figure in Tables 6.1–6.3 and Fig. 6.3. The problems cluster in the Navier–Stokes case study, which was written before two developments a reader at publication will know: OpenAI's 10 September investigation update (the book prints only its earlier "cannot rule out" concession, which is unfair to OpenAI), and the 20 November 2026 claim by Buckmaster and Alpöge of blow-up without any external force. Outside that box, one quotation from Beel et al. is a paraphrase in quotation marks, and the AI co-scientist is still called a company preprint although it appeared in *Nature* in May 2026. All four fixes are one- or two-sentence edits with replacement text given.

## MUST change before printing

### M1. Navier–Stokes credit dispute: OpenAI's position is reported in its superseded 8 September form, and "OpenAI denied it" misstates what OpenAI denied
- Where: textbook/chapters/ch06.md:223
- Text now: "he alleged that word of their progress had reached OpenAI before its own attempt [@buckmaster2026statement; @howlett2026openaiclaims]. OpenAI denied it. Its statement said that its researchers and agents "did not see any of their work through any means until they released it publicly", while conceding that it "cannot rule out" that de-identified data from the pair's use of its products had improved its models generally, and Sébastien Bubeck of OpenAI said: "We did not use their prompt or proofs to prompt our models""
- Problem: OUTDATED and one-sided against a named company. (a) The "cannot rule out" concession comes from OpenAI's statement of 8 September as quoted by OfficeChai. On 10 September OpenAI updated its announcement ("Update — September 10, 2026: We have updated "Concurrent work" with findings from our investigation") and the page now says that "Buckmaster's Codex prompts over the two months preceding this announcement and paper on September 8, 2026, could not have influenced the system in any way, including through training." The phrase "cannot rule out" no longer appears there. Printing only the concession, without the later finding, makes OpenAI's position look weaker than OpenAI itself now states it. (b) "OpenAI denied it" is not accurate as attached to "word of their progress had reached OpenAI": OpenAI's own page says "Our effort began on September 1st after hearing a rumor" that "we later realized was related to Levent Alpöge, an Anthropic employee", and "We recognize the priority of their work on forced Euler". What OpenAI denied was seeing or using their work. (Scientific American, 8 Sep, does write "OpenAI denies these allegations", so the gap is one of precision, but with a named living person and a company on each side the precise version is needed.)
- Evidence: https://openai.com/index/navier-stokes-solution/ (editor's footnote "Update — September 10, 2026"; "Concurrent work" section, quotes above); Buckmaster statement PDF https://cims.nyu.edu/~tristanb/statement.pdf p. 3: "Eventually it was agreed that it had been sent in the past few days, after information about our work had reached OpenAI" and p. 4: "I do not know whether our data was used. I am not accusing anyone of anything."
- Change to: "...he said that, by OpenAI's own account to him, its attempt had begun after word of their progress reached the company [@buckmaster2026statement; @howlett2026openaiclaims]. OpenAI said its effort began on 1 September "after hearing a rumor" later linked to Alpöge, recognised "the priority of their work on forced Euler", and denied using their work: its researchers and agents "did not see any of their work through any means until they released it publicly", and Sébastien Bubeck of OpenAI said: "We did not use their prompt or proofs to prompt our models". Its first statement conceded that it "cannot rule out" that de-identified data from the pair's use of its products had improved its models generally; after an internal investigation, it said on 10 September that Buckmaster's Codex prompts "could not have influenced the system in any way, including through training" [@officechai2026openai; @openai2026navierstokes]. Buckmaster, for his part, wrote that he did not know whether their data had been used and was "not accusing anyone of anything" [@buckmaster2026statement]."
- Bib: add
  @misc{openai2026navierstokes, author = {{OpenAI}}, title = {On the {Navier--Stokes} Millennium Prize Problem}, year = {2026}, howpublished = {Company blog, 8 September 2026, updated 10 September 2026}, url = {https://openai.com/index/navier-stokes-solution/}, urldate = {2026-11-22}}

### M2. Navier–Stokes case study is overtaken by events of 20 November 2026
- Where: textbook/chapters/ch06.md:227 (and the box as a whole; Fig. 6.3 caption line 204 calls the entry "a contested claim")
- Text now: "As of October 2026, research groups were still examining the paper and the Lean code [@howlett2026openais]."
- Problem: OUTDATED. On 20 November 2026 Tristan Buckmaster and Levent Alpöge posted an AI-assisted proof that the Navier–Stokes equations can blow up in finite time with no external force, i.e. without the smooth force on which OpenAI's result and its "What is contested" paragraph turn; with Matei Coiculescu they released a companion paper on unforced blow-up for the Euler equations. The claim is unverified: the write-up is, in Buckmaster's words, "unpolished and heavily LLM-assisted", the numerical certificate had not been released, and no expert had confirmed it. A reader of a book printed in late November 2026 who knows of this will find a case study that stops at "forcing" without it. (Also new since the text was written: Zhen Lei and Xiao Ren posted a two-part exposition of OpenAI's proof, arXiv:2611.06869, 4 Nov 2026, that "claim[s] no original mathematical contribution"; optional.)
- Evidence: Scientific American, 20 Nov 2026, "AI just solved the 'real' Navier-Stokes problem" (https://www.scientificamerican.com/article/ai-just-solved-the-real-navier-stokes-problem/): researchers "claimed to have solved the 'real' version", "closing the loophole OpenAI left open", "a dense, artificial-intelligence-aided proof"; The Next Web, 21 Nov 2026 (https://thenextweb.com/news/navier-stokes-blow-up-without-force-buckmaster-alpoge): "The Navier-Stokes equations can blow up in finite time with no outside force acting on the fluid"; Buckmaster: "After last time, we couldn't risk waiting, so the Navier-Stokes write-up is unpolished and heavily LLM-assisted"; certificate "not yet posted"; Claude and Codex used; Tao: strategy clear, a properly written proof still needs more work.
- Change to (replace the last sentence of the box): "As of October 2026, research groups were still examining the paper and the Lean code [@howlett2026openais]. On 20 November 2026, as this book went to press, Buckmaster and Alpöge posted an AI-assisted proof that the equations can blow up with no external force at all, which would close the gap on which the objections to OpenAI's result turn; Buckmaster called the write-up "unpolished and heavily LLM-assisted", part of its computer check had not yet been released, and no independent expert had confirmed it [@hall2026ai; @thenextweb2026navierstokes]."
- Bib: add @misc{hall2026ai, author = {Hall, Peter}, title = {{AI} just solved the `real' {Navier-Stokes} problem}, howpublished = {Scientific American, 20 November 2026}, year = {2026}, url = {https://www.scientificamerican.com/article/ai-just-solved-the-real-navier-stokes-problem/}} and @misc{thenextweb2026navierstokes, author = {Constantin, Ana Maria}, title = {{Navier-Stokes} can blow up with no outside force, {Buckmaster} and {Alp\"oge} say}, howpublished = {The Next Web, 21 November 2026}, year = {2026}, url = {https://thenextweb.com/news/navier-stokes-blow-up-without-force-buckmaster-alpoge}}. (SciAm byline as shown to me: Peter Hall, edited by Joseph Howlett; confirm on the page.) If the author prefers not to add new text this late, the minimum is to change "As of October 2026" to keep the dated statement and add a footnote that later developments are not covered.

### M3. Beel et al.: a paraphrase printed as a quotation
- Where: textbook/chapters/ch06.md:242
- Text now: "and some papers that "contained hallucinated numerical results". They likened the quality to "a rushed undergraduate paper", produced at very low cost"
- Problem: UNSUPPORTED BY CITED SOURCE (misquotation). Neither the SIGIR Forum version nor the arXiv version contains "a rushed undergraduate paper". The abstract says the quality "aligns with that of an unmotivated undergraduate student rushing to meet a deadline"; the body (p. 9) says "Four of seven manuscripts (57%) contained incorrect or hallucinated numerical results", so the second quotation also drops words without an ellipsis.
- Evidence: Crossref abstract of 10.1145/3769733.3769747 and arXiv:2502.14297 full text (searched for "rushed", "undergrad", "hallucinat").
- Change to: "and four of seven papers that "contained incorrect or hallucinated numerical results". They likened the quality to that of "an unmotivated undergraduate student rushing to meet a deadline", produced at very low cost"

### M4. AI co-scientist: described as a "company preprint", but it was published in *Nature* in May 2026
- Where: textbook/chapters/ch06.md:266 (and bib entry gottweis2025towards)
- Text now: "Google's "AI co-scientist", a set of Gemini-based agents that generate, critique and rank hypotheses, was described in a company preprint in February 2025. Its authors report that drug-repurposing candidates it proposed for acute myeloid leukaemia were confirmed in laboratory (in vitro) experiments [@gottweis2025towards]."
- Problem: OUTDATED. The work was published as Gottweis et al., "Accelerating scientific discovery with Co-Scientist", *Nature* 655, 487–496 (online 19 May 2026), DOI 10.1038/s41586-026-10644-y; the arXiv record (2502.18864) now carries that title and the comment "Nature (2026)". Throughout the chapter the author marks when company work later passed peer review (AlphaProof, The AI Scientist, the AlphaEvolve–Tao paper); leaving this one as "a company preprint" understates its evidential status, and the bib title no longer matches the arXiv record. The paper's abstract keeps the AML in-vitro claim, so the substance stands. Google's 19 May 2026 announcement reports case studies but no head-to-head comparison with human-generated hypotheses, so the last sentence of the paragraph can stay.
- Evidence: Crossref https://api.crossref.org/works/10.1038/s41586-026-10644-y (title, Nature, 2026-05-19, vol. 655, pp. 487–496; abstract: "drug-repurposing candidates and synergistic combination therapies for acute myeloid leukaemia that were validated through in vitro experiments"); https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/ (19 May 2026: published "in Nature").
- Change to: "Google's "AI co-scientist", a set of Gemini-based agents that generate, critique and rank hypotheses, was described in a company preprint in February 2025 and in *Nature* in May 2026. Its authors report that drug-repurposing candidates it proposed for acute myeloid leukaemia were confirmed in laboratory (in vitro) experiments [@gottweis2026accelerating]."
- Bib: replace gottweis2025towards with @article{gottweis2026accelerating, author = {Gottweis, Juraj and Weng, Wei-Hung and Daryin, Alexander and Tu, Tao and Sirkovic, Petar and others}, title = {Accelerating scientific discovery with {Co-Scientist}}, journal = {Nature}, volume = {655}, pages = {487--496}, year = {2026}, doi = {10.1038/s41586-026-10644-y}, note = {Preprint arXiv:2502.18864 (February 2025), first titled ``Towards an {AI} co-scientist''}}.

## SHOULD change (real but not blocking)

### S1. Open letter: signatory count has grown
- Where: ch06.md:223
- Text now: "signed by 25 leading mathematicians including Terence Tao, Peter Scholze and Maryna Viazovska"
- Problem: OUTDATED (minor). Zenodo v1 (11 Sep) lists 25 creators; the letter's site, mathandai.org, now lists 28 (Drinfeld, Margulis and Mumford added).
- Evidence: https://zenodo.org/records/22737750 ; https://mathandai.org (28 names).
- Change to: "signed initially by 25 leading mathematicians (28 by November), including Terence Tao, Peter Scholze and Maryna Viazovska"

### S2. "their university's announcement"
- Where: ch06.md:221
- Text now: "In a preprint, three mathematicians argue ...; their university's announcement stresses"
- Problem: Bastounis is at King's College London; Circelli and Hansen are at Cambridge. The announcement is KCL's.
- Evidence: https://www.kcl.ac.uk/news/openais-navier-stokes-proof-called-into-question (27 Oct 2026; affiliations listed).
- Change to: "three mathematicians at King's College London and the University of Cambridge argue ...; King's College London's announcement stresses"

### S3. Sawin's explicit exponent came the same day, not "within days"
- Where: ch06.md:212
- Text now: "Within days Will Sawin made the exponent explicit, about 1.014"
- Problem: Sawin's arXiv:2605.20579 was submitted 20 May 2026 (00:37 UTC), the date of OpenAI's announcement, which already cites "a forthcoming refinement by Will Sawin" giving δ = 0.014. "Within days" suggests a later, independent follow-up.
- Evidence: arXiv API record for 2605.20579 (published 2026-05-20T00:37:35Z); https://openai.com/index/model-disproves-discrete-geometry-conjecture/ (20 May 2026).
- Change to: "In a preprint released alongside it, Will Sawin made the exponent explicit, about 1.014"

### S4. Navier–Stokes: name Alpöge's employer
- Where: ch06.md:223
- Text now: "he and Levent Alpöge, working with AI models from several companies"
- Problem: Fairness and context. The dispute is in part between two AI companies: Alpöge is an Anthropic employee (OpenAI's account, Buckmaster's statement and the SciAm/TNW reports of 20–21 Nov all say so). A reader cannot weigh the dispute without this.
- Change to: "he and Levent Alpöge, an Anthropic researcher, working in a personal capacity with AI models from several companies"
- Evidence: Buckmaster statement p. 1 ("a purely personal collaboration, free of any institutional agreements"); OpenAI page ("Levent Alpöge, an Anthropic employee").

### S5. Erdős #728: Bloom's wording is more tentative
- Where: ch06.md:210
- Text now: "Bloom judged that the AI proof answered a tightened version, "the question in the spirit it was intended""
- Problem: The site says: "This appears to answer the question in the spirit it was intended."
- Evidence: https://www.erdosproblems.com/728 (page last edited 6 Jan 2026).
- Change to: "Bloom judged that the AI proof "appears to answer the question in the spirit it was intended", a tightened version"

### S6. EMS: "objected" is stronger than the statement
- Where: ch06.md:223
- Text now: "and objected that the model was not generally accessible"
- Problem: The EMS notes the model is "internal to OpenAI and not generally accessible" and calls this a concern for open science.
- Evidence: https://preview.euromathsoc.org/news/ems-statement-on-navier-stokes-announcement-225 (10 Sep 2026).
- Change to: "and called it a concern for open science that the model was "internal to OpenAI and not generally accessible""

### S7. mathlib statistics URL has moved
- Where: bib/ch06.bib, lean2026mathlib
- Problem: https://leanprover-community.github.io/mathlib_stats.html is now a redirect stub; the counts are at https://mathlib.org/mathlib_stats.html (296,355 theorems on 22 Nov 2026, consistent with the text).
- Change to: url = {https://mathlib.org/mathlib_stats.html}

### S8. Quanta: "copies" of a model
- Where: ch06.md:219
- Text now: "about 10,000 copies of an unreleased model worked for about 88 hours"
- Problem: Quanta says "10,000 or so" agents; OpenAI says "on the order of 10,000 concurrent agents". "Copies" is a gloss.
- Change to: "about 10,000 AI agents running on an unreleased model worked for about 88 hours"

## Could not verify
- ch06.md:208, Bloom's X post (bloom2025hi): x.com not readable; both quotations confirmed verbatim via TechCrunch, 19 Oct 2025. Low risk.
- ch06.md:165, Alexander Wei's X thread: not opened directly; content (35/42, three former IMO medallists, 19 Jul 2025) confirmed through several news reports. Low risk.
- ch06.md:3, 45 Nobel press release: nobelprize.org returned 403; wording confirmed through Utrecht University and EMBL-EBI reproductions of the press release. Low risk.
- ch06.md:266, "no independent comparison with human-generated hypotheses of the kind Si and colleagues ran has been published": I could not read the full *Nature* version of Co-Scientist (paywall); Google's announcement reports none. A human should glance at the Nature paper's evaluation section before printing, together with M4.
- M2 citation: the byline of the Scientific American article of 20 Nov 2026 was reported to me as "Peter Hall, edited by Joseph Howlett"; confirm on the page before adding the bib entry.
- ch06.md:53, AlphaFold 3 details (chirality violation 4.4%, "substantially de-emphasized", parameters under terms of use): checked from knowledge only; settled 2024 material, consistent with my knowledge.

## Reader notes
1. ch06.md:165 and Table 6.2 lines 172–173: Gemini is "within the 4.5-hour limit" / "within 4.5 h", OpenAI "two 4.5 h sessions". Same conditions, described differently; a reader will think they differ. Use "two 4.5-hour sessions" for both.
2. ch06.md:194: "the first improvement for complex-valued 4×4 matrices since Volker Strassen's algorithm of 1969" is a company claim experts qualified (it holds for non-commutative, recursively usable schemes; commutative tricks such as Winograd/Waksman's use fewer multiplications). It is attributed ("The company reports"), so not wrong, but a mathematically literate reader may stumble.
3. ch06.md:182: "within hours of the problems' release in March 2025 ... only Gemini 2.5 Pro reached ... 25%": Gemini 2.5 Pro was released after the contest and was added in a later version of the preprint (the abstract conflates the two). Fine as a summary of the abstract, slightly misleading on timing.
4. ch06.md:210: one paragraph carries #728, Bloom, Tao, Pomerance, the long tail, the 1–2% guess and a database. It is the densest paragraph in the chapter; splitting after "...solve the problem" would help.
5. ch06.md:223: the "Who gets the credit" paragraph is long and, after M1, longer; consider splitting at "OpenAI said ...".
6. ch06.md:184: the USAMO 2026 and IMO 2026 material in one paragraph is a number dump (95%, 74%, 45%, 42, 42, four companies). Table 6.2 already holds most of it.
7. ch06.md:219: the box opens with "alternatives (C) and (D)" before the reader is told what the four alternatives are; one clause ("the two alternatives that allow an external force") would help.
8. ch06.md:7: "Most of the showcase results ... come from a handful of companies, above all Google DeepMind" reads well; but after M2 the chapter's last word on Navier–Stokes would be an Anthropic-affiliated claim. Keep the caveat even-handed (as in S4).
9. ch06.md:131: "Starting from about 48,000 previously known stable crystals ... 381,000 lie on the final updated hull, for a total of 421,000": 48,000 + 381,000 = 429,000, so a reader will think the arithmetic is wrong. The source says exactly this (some earlier stable phases fall off the updated hull). Add "(some previously known crystals no longer lie on the updated hull)".

## Checked and confirmed
### Front matter, 6.1, 6.2 (AlphaFold, design)
- Nobel chemistry 2024 split and "more than two million people from 190 countries" (press-release text as reproduced by Utrecht University and EMBL-EBI; nobelprize.org 403).
- Van Noorden & Perkel 2023: "concerned, as well as excited", 1,600 researchers (Nature standfirst via search).
- CASP14 overview (Kryshtafovych 2021, PMC8726744): "Core components are rigorous blind testing..."; "competitive with experimental accuracy for at least 2/3 of the targets"; "a solution to the classical protein-folding problem, at least for single proteins"; objections to "solution" recorded in Discussion.
- Varadi 2024 (NAR): "over 214 million"; initial release "over 360 000 structures" (Data archiving section; the abstract says "initial 300k").
- Terwilliger 2024 (PMC10776388): 102 models and maps; median 0.6 Å for pLDDT>90; ~10% >2 Å; about twice the difference between high-resolution pairs; "remarkably closely", "exceptionally useful hypotheses", "particularly those that involve interactions not included in the prediction" (abstract).
### 6.3 Weather
- GraphCast arXiv:2212.12794: 36.7M parameters, "relatively small model by modern ML standards"; 96.9% of remaining 1,280 excluding 50 hPa; optimally blurred 88.0% of 1,380.
- WeatherBench 2 (arXiv:2308.15560): ACC 0.6 "ceases to have value for forecasting purposes"; "the mean of many states is not a realistic state itself".
- Pangu-Weather abstract: "in all tested variables"; published 5 July 2023.
- ECMWF 25 Feb 2025: AIFS operational; "many measures", tropical cyclone tracks, up to 20%; ~1,000 times less energy; same initial conditions as IFS.
- ECMWF 1 Jul 2025: AIFS ENS, 51 members, 31 km vs 9 km, "indispensable for high-resolution fields and coupled Earth-system processes", >10× faster, ~1,000× less energy.
- ECMWF 12 May 2026: AIFS v2 live; "first data-driven wave and snow cover forecasts".
- AIFS preprint arXiv:2406.01465: pre-training on ERA5 1979–2020; fine-tuning on operational IFS analyses; 10-day forecast ~2 min 30 s on one GPU; transformer processor with GNN encoder/decoder.
- NOAA 17 Dec 2025: AIGFS/AIGEFS/HGEFS; GraphCast as foundation; up to 99.7% less computing; ~9% of GEFS; "early results" 18–24 h; "comparable"; "degradation in tropical cyclone intensity forecasts"; hybrid outperforms both "across most major verification".
- NWS SCN 26-68 (27 Jul 2026): AIGFS v1.1 "improve tropical cyclone intensity forecasts ... reduce the so-called blurring issue".
- NHC 2025 verification report (Cangialosi et al., 30 Mar 2026): GDMI "slightly outperformed NHC at the shorter lead times from 12 to 72 h"; intensity "comparable skill with the best model, GDMI".
- Alet et al., Nature, online 6 Aug 2026 (Crossref): WeatherNext Cyclones; 2023–2025; "average lead-time advantage of 1 day or more" for track, intensity and wind radius.
- Ben Bouallègue et al. 2024 (BAMS): "operational-like context"; "Overly smooth forecasts, increasing bias with forecast lead time, and poor performance in predicting tropical cyclone intensity".
- Bonavita 2024: Pangu, FourCastNet, GraphCast; "fidelity and physical consistency".
- Charlton-Perez et al. 2024: Storm Ciarán "sixteen deaths"; four ML models; all underestimate peak winds.
- Selz & Craig 2023: "completely fails to reproduce the rapid initial growth rates"; agreement for realistic-size perturbations.
- Sun et al. 2025 (PNAS): FourCastNet 1979–2015; Cat 3–5 removed; 2018–2023 Cat 5; "cannot accurately forecast Category 5"; one-basin removal generalises.
- Allen et al. 2025 (Aardvark): "for several variables and lead times".
- Kochkov et al. 2024 (NeuralGCM): prescribed SST, multiple decades; "our model does not extrapolate to substantially different future climates".
### 6.4 Materials
- Merchant et al. 2023 abstract: 48,000; "2.2 million structures below the current convex hull"; "order-of-magnitude expansion in stable materials known to humanity"; 736 independently realised.
- Cheetham & Seshadri 2024 (PMC11044265): first 250 of 2,047; 10 of 384,870; "scant evidence ... trifecta of novelty, credibility, and utility"; "does not report any new materials but reports a list of proposed compounds"; call for domain expertise.
- Leeman et al. 2024 (PRX Energy, 7 Mar 2024): Rietveld analysis "not yet reliable"; disorder neglected; "two thirds ... likely to be known compositionally disordered versions of the predicted ordered compounds"; "no new materials".
- A-Lab author correction (Nature, 19 Jan 2026; PMC12872444): "new to the prediction platform, not necessarily new to science"; Zn2Cr3FeO8 removed (training data); 40 → 36 confirmed, 4 inconclusive.
- Juelsholt 2026 (Materials Horizons 13, 5672–5679; DOI 10.1039/D6MH00268D): TaCr2O6 identical to Ta1/2Cr1/2O2 first described 1971 and in MatterGen training data. No published reply from the MatterGen authors found.
### 6.5 Mathematics
- mathlib statistics (now at mathlib.org/mathlib_stats.html): 296,355 theorems (consistent with "more than 290,000").
- AlphaGeometry 2 (arXiv:2502.03544 v. Dec 2025): 54% → 84% on IMO 2000–2024 geometry.
- DeepMind IMO 2024 blog (25 Jul 2024): 28/42; gold from 29; Gowers and Myers; "within minutes ... up to three days"; manual translation.
- Hubert et al., Nature, online 12 Nov 2025 (Crossref abstract): AlphaZero-inspired; "millions of auto-formalized problems"; test-time RL with "millions of related problem variants".
- DeepMind IMO 2025 blog (21 Jul 2025): 35/42, five of six, natural language, 4.5-h limit, "officially graded and certified by IMO coordinators".
- Wei (OpenAI) 19 Jul 2025: 35/42; three former IMO medallists graded each proof (multiple reports).
- Aristotle (arXiv:2510.01346) p. 7: "the only human formalization step"; five of six.
- Seed-Prover (arXiv:2507.23726): statements formalised by human experts; "the proof for Problem 1 was finished after the deadline".
- Petrov et al. (arXiv:2503.21934): within hours; Gemini-2.5-Pro 25%; all others <5%.
- MathArena USAMO 2026 (28 Mar 2026): GPT-5.4 95.2%, "essentially saturates"; Gemini-3.1-Pro 74.4%; best open model Step-3.5-Flash 44.6%; three-model jury; every solution checked by hand; self-overrating; "partially supported by an evaluation grant from Google".
- AFP 23 Jul 2026 (The Standard HK): Huawei "Celia", Xiaohongshu "dots-note-3.0", 42/42; after the human contest, within a time limit; "under the IMO's official judging process"; Deedy Das (Menlo Ventures) informal test with OpenAI, Anthropic, Axiom Math, Moonshot Kimi K3 at 42.
### 6.6 Search, Erdős problems
- AlphaEvolve white paper arXiv:2506.13131 (48 scalar multiplications for complex 4×4).
- Georgiev et al., PNAS (Crossref: online 30 Sep 2026): abstract "rediscovered the best known solutions in most cases and improved on them in several" (verbatim); arXiv text: "smooth score function ... sometimes struggles otherwise"; "cheating phenomenon ... loopholes or exploit artifacts (leaky verifier ...)"; Kakeya pipeline AlphaEvolve → Deep Think → AlphaProof.
- TechCrunch 19 Oct 2025: Bloom "a dramatic misrepresentation"; "I personally am unaware of a paper which solves it"; The Decoder 18 Oct 2025: Weil, "10 (!)".
- Sothanaphan arXiv:2601.07421 abstract: "the first Erdős problem ... regarded as fully resolved autonomously by an AI system"; GPT-5.2 Pro + Aristotle, operated by Kevin Barreto; Lean.
- erdosproblems.com/728: "This problem is ambiguous, and there are a number of trivial solutions"; "This appears to answer the question in the spirit it was intended."
- Tao Mathstodon 7 Jan 2026 thread (API): exposition "more interesting than the solution itself"; 10 Jan addendum edited 5 Mar 2026: Pomerance 2014 methods, Pomerance note; 14 Jan thread: "long tail", "many of which actually have straightforward solutions", "unlikely to be reported on any public site", "on the order of 1-2%".
- The Decoder 18 Jan 2026: database by Paata Ivanisvili and Mehmet Mars Seven; "one to two percent"; "clustered around easier problems".
- OpenAI 20 May 2026: internal general-purpose reasoning model; n^(1+δ); Sawin arXiv:2605.20579 "more than n^1.014".
- ScienceAlert/The Conversation (Melissa Lee, 28 May 2026): Litt and Gowers quotes; ~10^2,000,000 points; 1946; problem 90.
- Tsoukalas et al. arXiv:2605.22763: 9 of 353 open Erdős problems.
### 6.7 Engineering
- Goldie, Mirhoseini, Dean arXiv:2411.10053: no pre-training, "20x fewer RL experience collectors and half as many GPUs"; Markov's "own unpublished paper"; "deployed in state-of-the-art chips across Alphabet".
- Markov arXiv:2306.09633 / CACM: lags humans, simulated annealing, commercial software.
- Cheng, Kahng et al. arXiv:2302.11014 (updated 10 Mar 2026; still lists "still-missing confirmations"): consistent with "the public record has not resolved the dispute".
### 6.8 Automated research
- Lu et al., Nature, online 25 Mar 2026: "passed the first round of peer review"; 70%; "taxing overwhelmed review systems and adding noise to the scientific literature" (PMC13017497).
- Sakana 12 Mar 2025: 3 papers, ICBINB workshop at ICLR 2025, scores 6/7/6, withdrawn, reviewers knew 3 of 43 might be AI; lower workshop bar.
- Sakana 26 Mar 2026: naive ideas, rigour, computational only; watermarking; norms.
- Beel et al. SIGIR Forum 2025: 42% (5 of 12) failed; median five citations; $6–15; 3.5 h human involvement.
- Si et al. 2024/2025 (arXiv): more novel, slightly weaker feasibility; 43 researchers, >100 h each; scores of LLM ideas fall more; ranking flips.
- Kosmos arXiv:2511.02824: up to 12 hours; 42,000 lines; 102 statements from 3 reports; 79.4/85.5/82.1/57.9%; authors 4.1 expert-months (n=6), collaborators 6.14 months (n=7).
### 6.9
- Hao et al., Nature, 14 Jan 2026 (Europe PMC abstract): F1 0.875; 41.3 million; 3.02×, 4.84×, 1.37 years; 4.63%; 22%; "towards areas richest in data".
- Osmani blog 14 Mar 2026, "Comprehension debt" definition.
### 6.6 Navier–Stokes case study
- OpenAI manuscript: 166 pages; "starts from rest"; force in C_c^infty (compact in space and time); "establishes alternative (C)" and (D) via Cor. 10.6 (PDF from cdn.openai.com, pdfinfo 166 pages, created 8 Sep 2026).
- Quanta (Kakaes, 8 Sep 2026): "10,000 or so" agents; "After 88 hours"; "after an additional 17 hours, another AI model had formalized the result".
- OpenAI page: "We do not intend to claim the Millennium Prize for this result." (openai.com/index/navier-stokes-solution, accessible 22 Nov).
- TNW (Constantin, 9 Sep 2026) quotes the same sentence; gives no OpenAI reason; "The crux is forcing" (book's "linked the decision" is a fair reading).
- SciAm 13 Oct 2026: "more than a month later, no one fully does"; Cao-Labora "it is a different approach"; "Several prominent research groups are now using both the Lean code and the paper".
- Bastounis, Circelli, Hansen arXiv:2610.08144 (6 Oct 2026) exists, authors/title match; KCL news 27 Oct 2026: "The researchers have not shown that OpenAI's original proof is wrong."
- Buckmaster statement PDF (created 8 Sep 2026 02:38 UTC): 15 August Boussinesq and Euler blow-up with smooth forcing; Lean 22 August; programme credited to Córdoba and Martínez-Zoroa; LLMs from Anthropic and OpenAI used; "information about our progress had been passed to OpenAI".
- OfficeChai 8 Sep 2026: OpenAI "did not see any of their work through any means until they released it publicly"; "cannot rule out" de-identified data.
- SciAm 8 Sep 2026: Bubeck "We did not use their prompt or proofs to prompt our models"; "OpenAI denies these allegations".
- EMS statement 10 Sep 2026: "a milestone"; "Questions of authorship and credit"; model "internal to OpenAI and not generally accessible".
- Open letter "A Severe Misalignment of AI in Mathematics", 11 Sep 2026, Zenodo v1 25 creators incl. Tao, Scholze, Viazovska; mathandai.org: all three quoted phrases present.
- Clay Mathematics Institute news, 11 Sep 2026: "has apparently been settled"; process "deliberately unhurried".

- Arithmetic recomputed: 5 + 6×37 = 227; 40 × 6 h = 10 days; 721 × 1,440 = 1,038,240; 41 − 1 = 40 = 36 + 4; (200 − 169)/200 = 15.5% (within 20%); 0.6/0.3 Å = about twice; 95.2/74.4/44.6% → 95/74/45%; 48,000 + 381,000 = 429,000 vs 421,000 (source-faithful, see Reader note 9); 9/353 = 2.5%; 1.014 exponent (Sawin abstract); AIGFS 99.7% (NOAA).
### Figures and tables
- Table 6.1 (all cells) matches lam2023learning, price2025probabilistic, ECMWF 25 Feb and 1 Jul 2025, NOAA 17 Dec 2025, NWS SCN 26-68; matches tbl-06-01 spec.
- Table 6.2 (all rows) matches the DeepMind 2024/2025 blogs, Wei, Aristotle, Seed-Prover, Petrov, MathArena, AFP.
- Table 6.3 (all rows) matches Beel, Sakana 2025, Lu 2026, Si 2024/2025, Kosmos.
- Fig. 6.3 entries (figs_ch06.py lines 154–165 and spec) match sources and running text; Fig. 6.2 (48 Evoformer blocks, recycling 4 passes) matches Jumper et al.
- Glossary-ch06 entries consistent with the chapter.

## Tally
Claims checked against a web source: 167. Confirmed: 152. Wrong or imprecise: 5 (Beel quotation; "OpenAI denied it"; Sawin "within days"; Bloom wording; "their university"). Outdated: 5 (OpenAI 10 Sep update; 20 Nov Buckmaster–Alpöge claim; Co-Scientist in Nature; letter now 28 signatories; mathlib URL). Unsupported by cited source: 1 (Beel "a rushed undergraduate paper"). Could not verify: 4 (none blocking; Co-Scientist evaluation section worth a glance). Arithmetic items recomputed: 12 (errors: 0). Bib entries checked: 72 (problems: 3 — gottweis2025towards superseded, lean2026mathlib URL moved, fields2026severe signatory count; plus 3 new entries proposed for M1/M2).
