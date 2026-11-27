# Review 6: Chapter 14, Forecasting the Next Ten Years: Methods, Scenarios and Open Problems

## Verdict

Ready to print. I found nothing that is wrong, misquoted or legally risky. The quantitative core holds up against the primary sources: the XPT scoring, the Grace survey series including the new 2024 round, ForecastBench, the FRI September 2026 review, the Epoch constraint table, the Ho et al. interval, the Humlum and Vestergaard bound, and the Census and St. Louis Fed adoption figures. Every worked example recomputes correctly. Sections 14.7–14.8 are clearly labelled as the author's untested proposals, and their premises are cited fairly. Two wording fixes would help.

## MUST change before printing

None.

## SHOULD change

### S1. Ambiguous "The same rule" in the BIS sentence
- Where: textbook/chapters/ch14.md:169
- Text now: "On 19 November 2026 it formally rescinded the never-enforced AI diffusion rule, including its control on model weights. The same rule required licences to supply advanced chips to data centres anywhere that provide large amounts of computing power to companies headquartered in China or other countries of concern, and added licence requirements for chip exports to five countries seen as diversion risks [@bis2026addressing]."
- Problem: UNCLEAR / potentially misleading. "The same rule" reads as the AI diffusion rule, but the remote-access data-centre control and the five-country licence requirement are new provisions of the 19 November interim final rule ("Addressing Remote Access to Advanced Semiconductors"), which also rescinded the diffusion rule.
- Evidence: Greenberg Traurig, "BIS Interim Final Rule Targets Remote Access to Advanced Semiconductors, Rescinds AI Diffusion Rule" (Nov 2026); Morgan Lewis (Nov 2026), which reports a new licence requirement for exports to Brazil, Indonesia, Malaysia, Singapore and Thailand, and an end-use control on data centres providing more than 12 million aggregate TPP to companies headquartered in China, Macau or other D:5 countries (https://www.morganlewis.com/pubs/2026/11/commerce-targets-remote-access-to-advanced-semiconductors-in-new-interim-final-rule).
- Change to: "On 19 November 2026 an interim final rule formally rescinded the never-enforced AI diffusion rule, including its control on model weights. In its place, the new rule requires licences to supply advanced chips to data centres anywhere that provide large amounts of computing power to companies headquartered in China or other countries of concern, and adds licence requirements for chip exports to five countries seen as diversion risks [@bis2026addressing]."

### S2. Name the CAISI-evaluated model as in the source
- Where: textbook/chapters/ch14.md:169
- Text now: "estimated that DeepSeek V4, the most capable Chinese model it had tested"
- Problem: UNCLEAR (minor). The cited evaluation is titled "CAISI Evaluation of DeepSeek V4 Pro" (bib nist2026caisideepseek). Naming the variant avoids confusion with other V4 releases.
- Change to: "estimated that DeepSeek V4 Pro, the most capable Chinese model it had tested"

## Could not verify
- IEA *Key Questions on Energy and AI* (2026). The figures in question are 485 TWh (2025), 945/950 TWh (2030), 833–1,008 TWh, "$715 billion ... 75% more than in 2025 and more than the entire US energy sector invested in 2024", and the quotes "through at least the end of 2027" and "compute-constrained". iea.org returned 403. An IEA slide deck (June 2026) and press coverage are consistent with growth of about 17% in 2025 (from 415 TWh, giving about 485) and with capex above $700bn. The deck's own comparison is with *global oil and gas production investment*, so the "US energy sector" comparison should be checked against the report.
- METR's January 2026 doubling times (196, 131 and 89 days) and the refit (188 and 129 days, range 104–158), and the GPT-5.6 Sol evaluation (11 h vs >270 h). I did confirm the METR page "is no longer actively updated" (last entry 8 Sept 2026) and the warning that "Measurements above 16 hrs are unreliable".
- *AI 2027* self-grading (65%, then about 75%).
- Buser et al. (2025) threat-image-projection figures. Not checked.

## Checked and confirmed
- XPT working paper: 38 of 172 sub-questions from 32 questions; Olympiad 2.3% (superforecasters) and 8.6% (experts); 9.7% vs 24.6% across four benchmarks; hydrogen forecasts of $4.50 and $3.50 against an actual $7.50; public −1.82 SD; MATH 71% vs 87.92% and MMLU 77.75% vs 88.7%; compute outcome 578,704.
- Grace et al. 2024 round (AI Impacts, Sept 2026): HLMI 2042, FAOL 2098 (gap 56 years); median extinction or disempowerment 10% (5% in 2023); about 10% response rate; 1,580 valid responses. Its footnote explains the 2022 figure (2059 vs the 2060 reported in 2023), which is consistent with the book.
- ForecastBench v5: superforecasters 0.096, public 0.121, Claude 3.5 Sonnet 0.122, p < 0.001.
- FRI review (22 Sept 2026): "dramatically underestimate"; FrontierMath 30/31% vs 40.7%; work hours 3.6/4/5.7%; biology tasks 16.2/22.5/40% vs 5.2%; ride-hailing 7.3% vs 2.5%; Metaculus 98%; $140bn run rate; LEAP 339 experts; 50% chance by 2030 of a binding restriction; the GPT-5.6 Sol "binding directive" quote; Mythos Preview 80% horizon about 3.1 h; ForecastBench superforecaster-level remark.
- Ho et al. (NeurIPS 2024): 8-month halving with an interval of about 2 to 22 months.
- Humlum & Vestergaard (NBER w33777): "ruling out effects larger than 2% two years after the launch of ChatGPT".
- Bick et al.: 62% of adults aged 18–64 in May 2026, up from 45% in Aug 2024.
- Census CES-WP-26-25: 18% of firms, 32% employment-weighted, Nov 2025–Jan 2026.
- Epoch "Can AI scaling continue": 2e29 FLOP; every value in Table 14.3; power binds first, then chips.
- OpenAI GPT-6.1 Astra withheld on 28 Sept 2026 (Al Jazeera). Training pause and first safety pause (Fortune, 18 Aug 2026).
- CAISSI renaming under EO 14434 (CSA research note, Oct 2026).
- Lifland and Kokotajlo medians: May 2028 to Nov 2027, and Jul 2030 to Jan 2030. Automated-coder definition quoted correctly.
- GO-Science: "over 70 experts"; "not predictions"; June 2026 update.
- Narayanan & Kapoor quote "Diffusion occurs over decades, not years". Verbatim.
- Arithmetic:
  - Table 14.2 (all four rows: 2,623 / 7,290 / 30,800 / 203,000 hours).
  - Brier examples (0.125, 0.205, 0.955, 0.835).
  - "about a quarter" (12.7/50.3).
  - 2.8×/yr for an 8-month halving.
  - 80% horizon under a fifth of 50% (3.1/17).
  - 0.5 m × 6 kW = 3 GW.
- Cross-references checked: 4.1, 4.7, 5.3, 6.6, 7.7, 8.7, 11.5, 13.2 and 13.7.

## Tally
Claims checked: 64 · Confirmed: 62 · Wrong: 0 · Outdated: 0 · Unclear: 2 (S1, S2) · Could not verify: 4 groups
