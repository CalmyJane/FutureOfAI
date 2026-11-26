# Review 4: Chapter 14 (Forecasting the Next Ten Years: Methods, Scenarios and Open Problems)

## Verdict
Ready to print. Nothing blocking. The arithmetic is exact (Brier example, Olympiad scores, Table 14.2, the efficiency factor, the horizon ratios). The figures from FRI, METR, AI Impacts, ForecastBench, Census, St. Louis Fed, AI Futures Project, NIST/CAISI and the AI Index match their sources. I checked the METR figures against the raw data file. The chapter is candid about its own uncertainty. The 14.7–14.8 proposals are clearly labelled as the author's own and untested, and their factual premises (SOGL reference incident, the 50.2 Hz retrofit, UK smart-charge delays, Knight & Leveson, Kim et al.) hold up.

There are three minor items. One (S1) repeats the Chapter 13 S1 issue, GPT-5.6 Sol called "unreleased". One sentence has an unsupported detail. A parenthetical mentions the June 2026 update of the UK scenarios but cites nothing for it.

## MUST change before printing
None.

## SHOULD change

### S1. GPT-5.6 Sol was not "unreleased"
- Where: textbook/chapters/ch14.md:167
- Text now: "Later in June OpenAI limited its unreleased GPT-5.6 Sol to a small group of partners approved by the US government, though FRI judged that this did not appear to result from a binding directive."
- Problem: INCONSISTENT / UNCLEAR. GPT-5.6 Sol was launched on 26 June 2026 as a limited preview for about 20 government-approved partners, then released generally in July. Chapter 12 (line 96) treats it as a released model. This is the same issue as Chapter 13 S1, and the two fixes should match.
- Evidence: TechCrunch, 26 Jun 2026, "OpenAI limits GPT-5.6 rollout after government request". TheNextWeb, 26 Jun 2026, released "to roughly 20 partners whose names the US government individually approved". Quartz (qz.com/openai-gpt-56-sol-us-government-approval-launch-070926), general rollout "after the Trump administration approved a broad release".
- Change to: "Later in June OpenAI, at the government's request, first released GPT-5.6 Sol only to a small group of partners approved by the US government, before a general release in July; FRI judged that this did not appear to result from a binding directive."

### S2. "a successor due in October" is not supported by the cited source
- Where: textbook/chapters/ch14.md:167
- Text now: "On 28 September OpenAI announced that it would not release GPT-6.1 Astra, a successor due in October, because the model fell short of its internal standards for alignment [@aljazeera2026openai]."
- Problem: UNSUPPORTED. The Al Jazeera article confirms the 28 September announcement and the reason. Saachi Jain said it "failed to meet company standards for acting in accordance with human wishes during internal testing". It gives no planned October date, and I found no other source for one. Chapter 12 (line 277) says only "the planned successor".
- Evidence: Al Jazeera, 29 Sep 2026 (https://www.aljazeera.com/economy/2026/9/29/openai-scraps-release-of-latest-ai-model-over-safety-concerns): the decision was announced "on Monday ... on the eve of OpenAI's annual developer conference"; no release date given.
- Change to: "On 28 September OpenAI announced that it would not release GPT-6.1 Astra, the planned successor to GPT-6 Astra, because the model fell short of its internal standards for alignment [@aljazeera2026openai]."

### S3. The updated UK scenario set has no citation
- Where: textbook/chapters/ch14.md:133
- Text now: "…and gave each two extreme outcomes for 2030 [@goscience2024ai] (an updated set followed in June 2026)."
- Problem: UNSUPPORTED (no citation). The updated report exists. It is *AI Scenarios 2030: Helping policymakers plan for the future of AI*, GO-Science with AISI and DSIT, dated 15 June 2026, and it replaces the earlier set with the same methodology. Readers should get a source.
- Evidence: https://www.gov.uk/government/publications/ai-scenarios-2030-helping-policymakers-plan-for-the-future-of-ai (June 2026; toolkit page August 2026).
- Change to: "(an updated set, using the same method, followed in June 2026 [@goscience2026ai])". New bib entry:
  ```
  @techreport{goscience2026ai,
    author = {{Government Office for Science}},
    title = {{AI} Scenarios 2030: Helping Policymakers Plan for the Future of {AI}},
    institution = {UK Government},
    year = {2026},
    note = {Published 15 June 2026},
    url = {https://www.gov.uk/government/publications/ai-scenarios-2030-helping-policymakers-plan-for-the-future-of-ai},
    urldate = {2026-11-26}
  }
  ```

## Could not verify
- Table 14.1 rows 3–6 (MATH 71/80/≈88%, MMLU 77.8/84.8/88.7%, compute 100,000/420,680/578,704 petaFLOP/s-days) and "from 32 questions". FRI's summary confirms 38 of 172 resolved, the 2.3%/8.6% Olympiad figures, 9.7%/24.6%, the hydrogen figures, the 1-SD aggregation gain and the public at −1.82 SD, but not these figures. They are probably in the full paper.
- IEA: "about 945 TWh in its base case" and the 833–1,008 TWh range. The IEA site was blocked. The 2026 executive-summary snippet I found gives "485 TWh in 2025 to 950 TWh in 2030", and IEA coverage gives "more than USD 400 billion in 2025 … another 75% in 2026", which is consistent with about $715 billion. Please confirm 945 against the report body (the 945 figure is in the 2025 *Energy and AI* report).
- Grace et al. framing gap of 17 vs 34 years; Pedersen 2026 (13 endoscopists); Buser 2025 (1,199,838 TIP events, 728 screeners); titotal's "roughly 40% weight" and "eleven data points"; AI Index "3.3× per year" computing capacity.

## Checked and confirmed
- XPT: 89 superforecasters and 80 experts, June–Oct 2022; Olympiad 2.3% / 8.6%; 9.7% vs 24.6%; hydrogen $3.50–4.50 vs about $7.50; the no-change and trend baselines; median aggregation about +1 SD; public −1.82 SD; no correlation between near-term accuracy and risk views; extinction medians 3% / 0.38% (88 / 29 answering, consistent with Ch. 11).
- Grace 2023: 2,778 respondents, 15% response rate; HLMI 2060→2047; FAOL 2116; 5% (mean 9%). The ESPAI 2024 report (Sept 2026): 1,580 respondents, 10% response rate, HLMI 2042, FAOL 2098, 56-year gap "the smallest to date", median extinction/disempowerment 10%. The 2022 value appears as "2059 (reported as 2060 in 2023)", so the book's 2060 is acceptable.
- FRI Sept 2026 review: 339 LEAP experts; "reasonably representative"; "dramatically underestimate"; FrontierMath 30/31/40.7%; work hours 3.6/4/5.7% with the outdated-baseline caveat; biorisk RCT 16.2/22.5/40/5.2%; ride-hailing 7.3% vs 2.5%; Navier–Stokes resolution unclear; Metaculus 98%; $140bn run rate vs medians $70bn/$90bn; 80% horizon 3.1 h (May 2026); 50% chance of a legal delay by 2030; "not yet seen evidence of improved accuracy"; models at superforecaster level on some question types; the bias toward underestimates.
- ForecastBench (ICLR 2025): superforecasters 0.096, public 0.121, Claude 3.5 Sonnet 0.122.
- METR: TH1.1 doubling times of 196.5 / 131 / 89 days. The data file (benchmark_results_1_1.yaml) gives 187.8 days and 128.7 days (104.4–158.0). Opus 4.6 p50 = 718.8 min (≈12.0 h, CI 5.3–60.6 h); Mythos Preview p50 ≈ 17.4 h and p80 ≈ 3.1 h. Frontier Risk Report: "~12h [5h-61h]" and the 16 h ceiling. GPT-5.6 Sol 11.3 h vs >270 h, "do not consider any of these numbers ... robust". Page "no longer actively updated" (8 Sep 2026).
- Arithmetic: Brier A = 0.125 and B = 0.205; (0.977)² ≈ 0.955 and (0.914)² ≈ 0.835. Table 14.2: 1,461/188 = 7.77 doublings → ×218 → ≈2,600 h; /158 → ×608 → ≈7,300 h; /129 → ×2,570 → ≈31,000 h; /104 → ×17,000 → ≈200,000 h; 2,600/2,000 ≈ 1.3 working years and 31,000/2,000 ≈ 15.5. 2^(12/8) ≈ 2.83. 3.1/17.4 < 1/5. MATH forecast 12.7/50.3 ≈ ¼.
- AI Futures Project: automated-coder medians May 2028 / Jul 2030 → Nov 2027 / Jan 2030; 65% → 75% of pace.
- Bick et al. (St. Louis Fed): 45% → 62% of adults aged 18–64. Census CES-WP-26-25: 18% of firms, 32% employment-weighted (Nov 2025–Jan 2026).
- NIST/CAISI: DeepSeek V4 Pro lags "by about 8 months", 1 May 2026. AI Index: gap "has effectively closed". BIS remote-access IFR of 19 Nov 2026 rescinds the diffusion rule and adds five countries.
- Commerce/Anthropic: the Fortune account of the "technique to bypass Fable 5's safeguards" matches the text. OpenAI pause announced 18 Aug 2026 (Fortune). GPT-6.1 Astra withheld on 28 Sep.
- AI Act Annex XIII (10,000 registered business users), Art. 14(4)(b) and Art. 26(2) quotations. Becker et al. 19% / 24% / 38%. Lighthill quotation. Cross-references to Sections 4.7, 5.3, 6.6, 8.7, 11.5, 13.2 and 13.7 point to the right sections.

Tally: claims checked 78 / confirmed 70 / wrong 0 / outdated 0 / imprecise or unsupported 3 (S1–S3) / unverifiable 5.
