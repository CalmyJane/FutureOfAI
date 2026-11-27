# Review 5: Chapter 14, Forecasting the Next Ten Years: Methods, Scenarios and Open Problems

## Verdict
Ready to print after one factual fix. The chapter is well sourced and its arithmetic is correct. I recomputed the Brier example, the Olympiad Brier scores, every row of Table 14.2, the ratio of the 80% to the 50% horizon, and the efficiency factor of 2.8 per year; all are right. The forecasting-record claims match FRI's own summaries: 38 resolved questions, 9.7% against 24.6%, 2.3% against 8.6%, hydrogen at $7.50, the public 1.82 standard deviations below, aggregation worth about 1 SD, and no correlation with long-run beliefs. The 2026 items I checked are also right: the 2024 AI Impacts round published in September 2026, the METR evaluation of GPT-5.6 Sol, the METR page frozen on 8 September 2026, the Bick et al. 62% figure, the CAISI estimate of DeepSeek V4 at 8 months, the IEA's 485 and 950 TWh, the GPT-6.1 Astra decision and Ho et al.'s 90% CI of 2–22 months. One sentence misdescribes the BIS remote-access rule of November 2026, and Chapter 7 states that rule correctly. The research proposals in Sections 14.7–14.8 are clearly labelled as the author's own and untested.

## MUST change before printing

### M1. BIS remote-access rule: "five more countries" misdescribed
- Where: textbook/chapters/ch14.md:169
- Text now: "On 19 November 2026 it formally rescinded the never-enforced AI diffusion rule, including its control on model weights, and required licences for remote access to large amounts of advanced computing by companies headquartered in China and in five more countries [@bis2026addressing]."
- Problem: VERIFIED WRONG / INCONSISTENT.
  - The remote-access licence requirement covers companies headquartered in China, Macau or other Country Group D:5 destinations. That is not "five more countries".
  - The five named countries (Indonesia, Malaysia, Singapore, Thailand, Brazil) received a separate destination-based licence requirement for exports of advanced chips, because of diversion risk.
  - Chapter 7 (ch07.md:144) describes this correctly, so the two chapters now disagree.
- Evidence: Pillsbury, "Commerce Restricts Remote Access to Advanced Chips" (Nov 2026). The rule covers data centres providing more than 12,000,000 TPP to "companies headquartered in, or whose ultimate parent is headquartered in, Macau or Country Group D:5". Separately it creates a "destination-based license requirement for advanced SI items to Indonesia, Malaysia, Singapore, Thailand and Brazil". Released 16 Nov 2026, Federal Register 19 Nov 2026. WilmerHale alert of 17 Nov 2026 (same rule).
- Change to: "On 19 November 2026 it formally rescinded the never-enforced AI diffusion rule, including its control on model weights. The same rule required licences to supply advanced chips to data centres anywhere that provide large amounts of computing power to companies headquartered in China or other countries of concern, and added licence requirements for chip exports to five countries seen as diversion risks [@bis2026addressing]."

## SHOULD change

### S1. Regulation paragraph repeats Chapter 13 almost word for word
- Where: textbook/chapters/ch14.md:167 (also 178, 190, 286)
- Text now: "On 12 June 2026 the US Commerce Department used export-control powers to require a licence for any foreign national's access to Anthropic's newly released Claude Fable 5 and Mythos 5, including inside the US, … Law-firm analyses described it as the first known use of export controls to block access to an AI service … Later in June OpenAI, at the government's request, first released GPT-5.6 Sol only to a small group of partners …"
- Problem: UNCLEAR (padding). This paragraph restates ch13.md:144 and ch13.md:306, and ch07.md:135, nearly sentence for sentence. The June 2026 export-control block then comes back a fourth and fifth time at lines 190 and 286. A reader who has just finished Chapter 13 meets the same paragraph again. The paragraph is also the longest in the chapter, at about 330 words.
- Evidence: Internal comparison with ch13.md:144, ch13.md:306 and ch07.md:135.
- Change to: shorten the middle of line 167 to: "The first restrictions have come mostly from companies, with one government exception: the US export-control block on two Anthropic models in June 2026 (Chapters 7 and 13) [@kahn2026anthropic]. FRI counted that episode, and OpenAI's government-requested limited first release of GPT-5.6 Sol, as signs that its question could resolve far sooner than forecasters expected [@rosenberg2026how]." Then keep the OpenAI pause and GPT-6.1 Astra sentences.

## Could not verify
- The date of OpenAI's announcement withholding GPT-6.1 Astra, given as "On 28 September" (line 167). Al Jazeera reported it on 29 September 2026. A US-time announcement on the 28th is plausible, but I did not see the primary post.
- The figure of "about $715 billion" in 2026 capital spending and the comparison with the US energy sector (line 155). The IEA says spending exceeded $400 bn in 2025 and is expected to rise 75% in 2026, which gives about $700 bn and is consistent with the book.
- The AI Index estimate of capacity growing 3.3× per year, the Census figures of 18% and 32% of firms, FRI's revenue run rate of $140 bn, the LEAP 50% question, and the Pew figure of 52% for June 2026.
- The AI 2027 authors' revised medians for April and August 2026, and their grading at 65% and then 75% (line 141).
- The framing split of 17 against 34 years in the 2023 Grace survey (line 47).
- METR's doubling-time figures of 196/131/89 and 188/129 days, and the 12-hour frontier for Claude Opus 4.6 (line 94). The page confirms only that measurements above 16 hours are unreliable; the numbers themselves are in the data file.

## Checked and confirmed
- XPT participants: 89 superforecasters and 80 experts, June–Oct 2022. FRI's own summary confirms 38 resolved questions, 9.7% against 24.6% on four AI benchmarks, 2.3% against 8.6% for an IMO gold, renewable hydrogen at $7.50/kg against forecasts of $4.50 and $3.50, the public 1.82 SD below, median aggregation worth about 1 SD, and no correlation with long-run risk beliefs.
- IMO gold-medal-level results by Google DeepMind and OpenAI in July 2025.
- Grace et al. 2023 survey: 2,778 respondents (15%), HLMI 2047, FAOL 2116, 38–51% giving at least a 10% chance of extinction-level outcomes.
- 2024 round: 1,580 respondents (10%), human-level AI about 16 years and 72 years out (about 2042 and 2098, a gap of 56 years), more than half giving at least 10%. Posted September 2026.
- Steinhardt contest: MATH forecast 12.7% against 50.3% (about a quarter); MMLU forecast 57.1% against 67.5%.
- Brier example: A = 0.125, B = 0.205. (0.977)² ≈ 0.955 and (0.914)² ≈ 0.835.
- Table 14.2: 1,461 days divided by 188, 158, 129 and 104 days gives 7.8, 9.2, 11.3 and 14.0 doublings, factors of about 220, 610, 2,600 and 17,000, and horizons of about 2,600, 7,300, 31,000 and 200,000 hours. At 2,000 hours a year that is 1.3 and 15.5 working years.
- 80% horizon of 3.1 h against a 50% horizon of about 17 h for Mythos Preview, a ratio of about 0.18, consistent with "under a fifth" and "factor of about five". An eight-month halving gives 2^1.5 ≈ 2.8 per year.
- Ho et al., NeurIPS 2024 version: "90% confidence interval of around 2 to 22 months" (the arXiv version gives 95% CI 5–14). This is consistent with ch04.
- METR on GPT-5.6 Sol: about 11.3 h with cheating counted as failure, more than 270 h with cheating counted as success, not a robust measurement. METR's time-horizon page is no longer updated (8 Sep 2026) and says measurements above 16 h are unreliable.
- METR developer RCT: 16 developers, 19% slower, forecast of 24%, ML experts 38%.
- ForecastBench: superforecasters 0.096 against 0.122 for the best model. Berg et al.: 964 polls, 74%.
- Lighthill quotation and the Wolfers–Zitzewitz finding.
- Narayanan & Kapoor quotation "Diffusion occurs over decades, not years" (Knight First Amendment Institute text).
- Epoch scaling analysis: 2 × 10^29 by 2030, about 10,000 × GPT-4. Villalobos et al.: 2026–2032, median 2028.
- IEA: 485 TWh in 2025, 950 (945) TWh in 2030, Headwinds case 833 and Lift-Off case 1,008.
- Bick et al. (St. Louis Fed, 1 Sep 2026): 62% in May 2026 against 45% in Aug 2024. CAISI: DeepSeek V4 "lag behind the frontier by about 8 months", "most capable PRC AI model evaluated by CAISI to date", 1 May 2026.
- OpenAI cancelled the release of GPT-6.1 Astra over alignment concerns (Al Jazeera, 29 Sep 2026).
- Humlum & Vestergaard: effects of more than 2% ruled out, consistent with ch08.
- Acemoglu: 0.66% over ten years. Aghion & Bunel: 0.68 pp a year.
- AI Act Annex XIII threshold of 10,000 registered business users. UK smart-charge random delay of 600 s default and up to 1,800 s. Knight & Leveson: 27 versions, one million tests.
- Cross-references to Section 4.7, Section 5.3, Section 6.6 (Navier–Stokes), Section 8.7, Section 11.5 and Sections 13.2 and 13.7 point to matching content.

## Tally
Claims checked: 82 / confirmed: 73 / wrong: 1 / outdated: 0 / unclear: 1 / could not verify: 7
