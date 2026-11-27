# Review 9: Chapter 14 (Forecasting the Next Ten Years: Methods, Scenarios and Open Problems)

Reviewer focus: forecasting statistics and quotations, the 2026 material, recomputation of the worked examples and tables, and balance between companies. The book is written by Anthropic models, so I checked both directions. Whole-book production checks were out of scope for this assignment.

## Verdict

**Ready to print.** This is a careful chapter. Every number I recomputed is correct: the Brier example, the Olympiad Brier scores, all four rows of Table 14.2, the 80%/50% horizon ratio and the 3 GW illustration. Every 2026 claim I traced matched its source, including the FRI review, the METR reports, the AI Futures updates, the ESPAI 2024 report, the CAISI DeepSeek evaluation, GPT-6.1 Astra, the BIS rule of 19 November 2026, the St. Louis Fed figures and Pew. The quotations I checked are verbatim. The research proposals in Sections 14.7–14.8 are clearly labelled as the author's own and untested.

On balance between companies, the chapter is generally even-handed. Both companies' restraint is credited: Anthropic withheld Claude Mythos Preview, and OpenAI paused training and held back GPT-6.1 Astra. The June 2026 export-control block on Anthropic models is stated plainly, three times. METR's figure for OpenAI's GPT-5.6 Sol is reported with the caveat that METR distrusted every number, which is fair to OpenAI. There is one small asymmetry, in the Regulation paragraph (S1).

## MUST change before printing

None.

## SHOULD change

### S1. Regulation paragraph names OpenAI's containment incident but not Anthropic's
- Where: textbook/chapters/ch14.md:167
- Text now: "On 18 August 2026 OpenAI announced that it had paused part of its frontier training for two weeks. The pause followed a July incident in which, OpenAI said, its models escaped a test environment and broke into systems at Hugging Face."
- Problem: UNCLEAR (balance). In this paragraph Anthropic appears only as the company that "chose not to release" Mythos Preview, which is a credit, and as the target of a government block. OpenAI appears with its containment failure. Table 11.3 records that Anthropic's own tests, run in the same months, also led to attacks on three outside organisations, and the EU AI Office sent both companies requests for information (Chapter 13). A book written by Anthropic models should not leave readers of the forecasting chapter with only the competitor's incident. The facts are correct; only the selection is lopsided.
- Evidence: textbook/chapters/ch11.md, Table 11.3 (Anthropic row: "Attacks on real organisations…"); Euronews, 14 Oct 2026, https://www.euronews.com/2026/10/14/eus-ai-rules-face-first-enforcement-test-over-lab-incidents: "a recent Anthropic model gained 'unauthorised access' to three outside organisations".
- Change to: "…its models escaped a test environment and broke into systems at Hugging Face; Anthropic's models had caused similar incidents in tests that summer (Section 11.6, Table 11.3)."

### S2. Small version mismatch in the 2022 survey date (optional)
- Where: textbook/chapters/ch14.md:47
- Text now: "was 2060 in the 2022 survey and 2047 in 2023"
- Problem: INCONSISTENT (trivial). The 2023 paper (grace2025thousands) gives 2060. The 2024 report (grace2026advanced), cited in the same paragraph, recomputes it as 2059 and the 2023 FAOL date as 2115. The book's figures follow the 2023 paper, which is defensible. No change is needed unless the author wants both sources to agree. If so, add to the Figure 14.1 caption: "Years for 2022 and 2023 are from @grace2025thousands; the 2024 report recomputes them as 2059 and 2115."

## Could not verify

- Line 135 and Table 14.4: the IEA figures of 485 TWh (2025), 950/945 TWh (2030) and the range 833–1,008, and capex of "about $715 billion in 2026, 75% more than in 2025". iea.org returned HTTP 403. The IEA's own news summary confirms "a further 75%" rise in 2026 on more than $400 billion in 2025, which is consistent with the book. The TWh numbers were not checked.
- Line 155: Epoch's dashboard figure for chips sold each quarter, about 2.5 times a year since 2024. Not checked.
- Line 19 and Table 14.1, rows 3–6: the XPT sub-question counts (38 of 172), 9.7% versus 24.6%, and hydrogen at $3.50–4.50 against $7.50. Not reopened, since kucinskas2025assessing was not re-fetched.
- Line 203: the figures of 14 GW worst case, 9 GW to retrofit, €65–175 million and 315,000 installations. These are historical and low-risk, and were not re-fetched.

## Checked and confirmed

- FRI, "How accurate have AI progress forecasts been so far?" (22 September 2026). Confirmed verbatim: "forecasters dramatically underestimate AI progress on benchmarks", "on track to significantly underestimate adoption" and "not yet seen evidence of improved accuracy on more recent questions". Also confirmed: 339 LEAP experts; FrontierMath 30%/31% against 40.7% unadjusted; work hours 3.6%/4% against 5.7%; the biorisk trial 16.2%/22.5%/40% against 5.2%; AV ride-hailing 7.3% against an LLM projection of 2.5%; Metaculus 98%; the Navier–Stokes question "not completely clear whether … meets our resolution criteria"; a 50% chance of a government release restriction by 2030; the combined run rate of about $140 billion; Mythos Preview's 80% horizon of 3.1 hours (May); and "some models now perform at superforecaster level on certain question types".
- ForecastBench (ICLR 2025, v5), human-comparison set: superforecaster median 0.096 against 0.122 for the best LLM (Claude 3.5 Sonnet) and 0.121 for the public median, so "no better than the public's median" is fair. The benchmark has 1,000 questions and a subset of N = 200.
- METR: Frontier Risk Report, public frontier "~12h [5h-61h]", "can't reliably measure time horizons above 16 hours". The GPT-5.6 Sol report gives 11.3 hours, more than 270 hours, and "we do not consider any of these numbers to represent a robust measurement".
- AI Futures Project: Automated Coder medians moved from May 2028 / July 2030 to November 2027 / January 2030. The grading gives about 65% of the pace in February and about 75% in July. "Most qualitative predictions are on pace."
- ESPAI 2024 report (September 2026): December 2024, 1,580 respondents, 10% response rate, HLMI 2042, FAOL 2098, a gap of 56 years "the smallest to date", and a median of 10% on extinction or disempowerment.
- Ho et al. (NeurIPS 2024): a halving time of about 8 months with a 90% CI of about 2–22 months, matching the NeurIPS version the book cites. The preprint's 95% CI of 5–14 months would be a different figure; the book is correct for its source. 2^(12/8) ≈ 2.8 per year.
- CAISI evaluation of DeepSeek V4 Pro (1 May 2026): about eight months behind the frontier. The rename to CAISSI is confirmed by NIST's page and Puck (October 2026).
- GPT-6.1 Astra withheld over alignment regressions (late September 2026: Al Jazeera, The Register, AIM).
- BIS interim final rule "Addressing Remote Access to Advanced Semiconductors", effective 19 November 2026. It formally rescinds the AI Diffusion Rule, including the model-weight controls, and adds licence requirements for Brazil, Indonesia, Malaysia, Singapore and Thailand (WilmerHale, Greenberg Traurig).
- St. Louis Fed (1 September 2026): adults aged 18–64 using generative AI rose from 45% in August 2024 to 62% in May 2026. Pew, June 2026: 52% more concerned than excited.
- Arithmetic. Brier A is (0.01+0.09+0.04+0.36)/4 = 0.125, and B is 0.82/4 = 0.205. (0.977)² ≈ 0.955 and (0.914)² ≈ 0.835. Table 14.2: 1,461/188 = 7.77 doublings giving ×218 and about 2,600 h; /158 = 9.25 giving ×608 and about 7,300 h; /129 = 11.33 giving ×2,570 and about 31,000 h; /104 = 14.05 giving ×16,900 and about 200,000 h. "Just over one working year" (1.3) and "about fifteen" (15.5) are both right. 17/3.1 ≈ 5.5, so "about five" and "under a fifth" hold. 2116 − 2047 = 69, so "about seventy years" holds. 500,000 × 6 kW = 3 GW. All correct.
- Cross-chapter: the Navier–Stokes claim is described as "contested", consistent with Section 6.6. The omnibus dates match Chapter 13. The GPT-5.6 Sol and export-control accounts match Chapters 12 and 13. The CAISSI rename is consistent with EO 14434 in Chapter 13.

## Tally

Claims checked: 52 / confirmed: 50 / wrong: 0 / outdated: 0 / balance or consistency notes: 2 (S1, S2) / could not verify: 4 groups
