# Review 7: Chapter 8 (Work, Productivity and the Economy)

## Verdict

Ready to print. I found no factual errors, misquotations or legally sensitive passages. The chapter is careful about evidence quality, and it is fair to the people and firms it names: Amodei, Anthropic, OpenAI/Sama and the withdrawn MIT preprint, whose author it does not name. The 2026 material all checks out against primary sources, including the "Super Intelligence" executive order, the BTOS wording and the 25.0% figure, the Challenger, Beige Book, BLS productivity, ADP "Canaries" (August 2026), METR follow-up, WGA/SAG-AFTRA, Digital Omnibus and Vivalt revision. So do the worked examples: Acemoglu's arithmetic, Table 8.1 and Table 8.4. One small attribution point is listed below as a SHOULD.

## MUST change before printing

None.

## SHOULD change

### S1. The 1.8-point Anthropic estimate predates the January 2026 report
- Where: textbook/chapters/ch08.md:217
- Text now: "Anthropic's January 2026 report, using the company's own usage data, estimated that AI could add about 1.8 percentage points to annual US labour-productivity growth over the next decade, or about 1.0 to 1.2 points once task success rates are allowed for [@anthropic2026economic]."
- Problem: UNSUPPORTED (minor attribution). The January 2026 report introduces 1.8 pp as an earlier estimate. It reproduces the figure on its own data and then lowers it to 1.2 pp (Claude.ai) and 1.0 pp (API) once task success is allowed for. The numbers are right, but the wording credits the 1.8 to this report.
- Evidence: https://www.anthropic.com/research/anthropic-economic-index-january-2026-report (15 Jan 2026): "In earlier work, we estimated that widespread adoption of AI could increase US labor productivity growth by 1.8 percentage points annually over the next decade". Also: "implied productivity growth falls from 1.8 to 1.2 percentage points per year for the next decade based on Claude.ai usage". For API traffic the adjusted figure is 1.0 pp.
- Change to: "Anthropic's January 2026 report, using the company's own usage data, reproduced its earlier estimate that AI could add about 1.8 percentage points to annual US labour-productivity growth over the next decade, and lowered it to about 1.0 to 1.2 points once task success rates are allowed for [@anthropic2026economic]."

## Could not verify

- l.101 and l.136 (Otis et al.): "more than 0.2 standard deviations lower", "more than 15%" and "nearly 10% worse". The versions differ. The HKS working-paper abstract gives 0.27 SD, "just over 15%" and "about 8% worse". Another version gives ">0.20 SD" and "nearly 10%". The published *Management Science* text was paywalled (403), so I could not tell which version the book follows. The mechanism wording ("does not stem from differences in the questions posed to or advice received") matches.
- l.61: the Humlum & Vestergaard figures by employer policy (40%/7%, 93%/28%/19%, 8%/17%) and l.152 "12 percentage points faster". The abstract confirms the "ruling out effects larger than 2%" null and the occupational switching, but not these numbers.
- l.67: Bonney et al.'s "57% in three or fewer functions" and "two-thirds only augment". The abstract confirms 18% / 32% and 2%.
- l.37: ILO average score 0.30 → 0.29 and the 0.9 clerical examples.
- l.243: SAG-AFTRA "strengthens consent and compensation rules" is confirmed via SHOOT. The ">90%" is confirmed via AP.

## Checked and confirmed

- METR 2025 (16 developers, 246 issues, +19% [+2, +39], 24% expected / 20% believed, experts 38–39%). METR 2026 (57 developers, 800+ tasks, −18% [−38, +9] and −4% [−15, +9], 30–50% withholding, "only very weak evidence").
- Noy & Zhang 40% / 18%. Peng 55.8% (21–89%). Brynjolfsson et al. QJE: 5,172 agents, +15%, lowest skill quintile +36% (arXiv v2: "36% increase in resolutions per hour"). Cui et al. 26.08% (SE 10.3%). Dell'Acqua 12.2% / 25.1% / 19 pp.
- Eloundou et al.: 80% / 19%, 3% and 49% for human labels, and every task-level share in Table 8.1 (0.15/0.31/0.47 human; 0.14/0.35/0.56 GPT-4) against the paper's Table 3.
- ILO–NASK: one in four, 3.3% in Gradient 4, 34% vs 11%, 9.6% vs 3.5% (high-income), "transformation, not replacement, is the most likely outcome". IMF 40/60/40/26%.
- BLS AI exposure categories (27 Aug 2026): 831 occupations, three theoretical and two observed sources (Anthropic, Microsoft), "Exposure does not imply job loss", "do not distinguish ... automation versus augmentation".
- Bick et al.: 62% (May 2026), 39.2% / 6.3% / 2.2% (Q2 2026), "may have increased labor productivity by up to 1.3%", reweighting after the question-order test.
- BTOS (National.xlsx): 25.0% for the reference period 19 Oct–1 Nov 2026 (released 19 Nov). H1 2026 values 17.7–20.6%. Question wording now reads "Super Intelligence or SI (formerly referred to as Artificial Intelligence or AI)". EO 14434 (29 Sep 2026) relabels the term with the same statutory scope.
- Anthropic Jan 2026: 1M + 1M samples from November 2025, 52% / 45%, three-quarters API automation. June 2026 report: ~9,700 respondents, 30% computer/math vs 4% of employment.
- Challenger Oct 2026: 121,401 AI-cited cuts (~20%), 1,265 in October, Market/Economic Conditions overtook AI, YTD −44%. October 2026 Beige Book: five Districts, attrition and delayed hiring after "investing in AI".
- ADP "Canaries" August 2026: >26 M workers, 3.5–5 M panel, −11% / +10%, 19% gap (15% at July 2025 vintage), "early, descriptive indicators".
- Hosseini & Lichtinger (May 2026 version): 65 M workers, >280,000 firms. PwC 2026: >1 bn ads, entry-level roles "seven times more likely".
- EIG 0.30 vs 0.94 pp. Fairlie & Wu NBER w35796 (summer 2026 CPS, no significant rise). St. Louis Fed (Rodgers & Kassens): one-third, April 2023–Dec 2025, and the quotation verbatim.
- Acemoglu April 2024 working paper: 19.9%, 23%, 27%, 0.57, 0.154, 0.71%, 7% for hard tasks, <0.55%, GDP 0.9–1.1% and 1.6–1.8%. Published version 0.66% / 0.53%. All arithmetic recomputed (0.199×0.23 = 0.046; 0.27×0.57 = 0.154; 0.046×0.154 = 0.71%).
- Aghion & Bunel: 60% (Pizzinelli et al.), 50%, 22% compute-cost decline, 40%, 0.68 pp, 0.07–1.24, 0.8–1.3, the ideas caveat. Table 8.4 product 0.6×0.5×0.4×0.57 = 6.84%, with (55.8+40+25)/3 ≈ 40%.
- Penn Wharton: 1.5% by 2035, 3.7% by 2075, 0.2 pp peak in 2032, 40% exposure. BLS Productivity Q3 2026: 3.6%, 2.1% y/y, 2.2% since 2019, 1.5% for 2007–19, 2.2% since 1947.
- Vivalt et al. NBER w32719 (rev. August 2026): −4.2 pp participation, 1–2 h/week.
- WGA 2026 MBA: "preserves all of the protections negotiated in 2023", training-licence notice, term 2 May 2026–1 May 2030. SAG-AFTRA: four-year deal, "significant additional value".
- Digital Omnibus (Reg. 2026/1744): OJ 24 Jul 2026, in force 27 Jul, Annex III deferred to 2 Dec 2027. Consistent with Ch. 13 §13.2 and Table 13.1.
- Fairwork 2023: 15 platforms, top score 5, four zeros, microwork "among the lowest scores". Amodei / Axios quotation and dates. Pew 52% / 36%.
- Cross-references (§8.1, §13.2, §14.4, Ch. 3, Ch. 5, Ch. 10 "When help harms learning") all resolve.

## Tally

Claims checked: ~115 · Confirmed: ~105 · Wrong: 0 · Imprecise attribution: 1 (S1) · Outdated: 0 · Could not verify: ~9
