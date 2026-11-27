# Review 8: Chapter 14 (Forecasting the Next Ten Years)

## Verdict

Ready to print. Chapter 14 reads well and is carefully hedged. I recomputed all the worked arithmetic and it is correct: the Brier example, Table 14.2, the 2.8-per-year efficiency factor, the 56-year framing gap and the ratio of the 80% to the 50% horizon. Every 2026 source I could reach supports the text, often word for word. These include METR, the AI Futures Project, FRI, ForecastBench, the 2024 ESPAI report, the BIS rule, the CAISI evaluation, the St. Louis Fed and Census.

I found nothing wrong, misquoted or legally sensitive. On balance between companies, the chapter treats the developers even-handedly, with one completeness gap (S1). The regulation passage and Table 14.4 credit company-imposed release limits to OpenAI only, although the book itself (Chapter 11) records an earlier one by Anthropic.

## MUST change before printing

None.

## SHOULD change

### S1. Company release restrictions are credited to OpenAI alone
- Where: textbook/chapters/ch14.md:167 and :178 (Table 14.4)
- Text now (line 167): "The first restrictions have come mostly from companies, with one government exception: the US export-control block on two Anthropic models in June 2026 (Chapters 7 and 13) [@kahn2026anthropic]."
  Text now (line 178): "release limits, a training pause and a held-back model by companies (OpenAI, Jun–Sep 2026)"
- Problem: INCONSISTENT / UNCLEAR. The sentence says the first restrictions came "mostly from companies", but the only company actions it then names are OpenAI's. Table 14.4 also attributes company release limits to OpenAI alone. Chapter 11 (line 137) records that in April 2026 Anthropic "chose not to release generally" Claude Mythos Preview. That predates OpenAI's limited release of GPT-5.6 Sol in June, and unlike OpenAI's it was not requested by the government. As written, a reader would infer that only one developer had held back a model. The fix is a matter of accuracy, not of favouring either company. It should be worded neutrally, and keep the OpenAI examples, which are well sourced.
- Evidence: textbook/chapters/ch11.md:137: "Anthropic's Claude Mythos Preview, which the company chose not to release generally" [@aisi2026our; @anthropic2026claude]. OpenAI's own announcement (26 June 2026) says its limited preview was made at the government's request.
- Change to (line 167): "The first restrictions have come mostly from companies: in April 2026 Anthropic chose not to release Claude Mythos Preview generally (Chapter 11) [@anthropic2026claude], and OpenAI's limited first release of GPT-5.6 Sol followed in June. There was one government exception: the US export-control block on two Anthropic models in June 2026 (Chapters 7 and 13) [@kahn2026anthropic]."
  (Then remove the clause "and OpenAI's government-requested limited first release of GPT-5.6 Sol" from the next sentence only if a repetition results; the FRI point can stay as it is.)
  Change to (line 178): "release limits, a training pause and a held-back model by companies (Anthropic, Apr 2026; OpenAI, Jun–Sep 2026)"
  If `anthropic2026claude` is not in ch14.bib, copy the entry from ch11.bib.

## Could not verify

- The IEA *Key Questions on Energy and AI* (April 2026) figures: 485 TWh in 2025; about 950 TWh (945) in 2030 and the 833–1,008 TWh range; capex of about $715 billion, "75% more than in 2025"; the memory shortage lasting "through at least the end of 2027"; and the "compute-constrained" quotation. iea.org returned 403. Secondary coverage confirms a 75% rise on more than $400 billion of 2025 capex for five large firms, which is consistent with the book but does not prove it.
- Epoch's November 2026 dashboard figure that AI-chip compute sold per quarter has grown about 2.5 times per year since 2024 (line 155).
- That the UK Government Office for Science consulted "more than 70 experts" (line 133).
- The Ecofys/Stuttgart worst case of "about 14 gigawatts" (line 203).

## Checked and confirmed

- XPT, Kučinskas et al.: 169 participants (June–Oct 2022); IMO gold at 2.3% (superforecasters) and 8.6% (experts); 38 resolved sub-questions.
- The Brier example: A = 0.5/4 = 0.125; B = 0.82/4 = 0.205; (0.977)² ≈ 0.955; (0.914)² ≈ 0.835.
- Table 14.2: 1,461/188 = 7.77 doublings, ×218, ≈2,600 h; /158 = 9.25, ×608, ≈7,300 h; /129 = 11.33, ×2,570, ≈31,000 h; /104 = 14.05, ×17,000, ≈203,000 h. At 2,000 h a year these are about 1.3 and 15.5 working years.
- METR Time Horizon 1.1 (Jan 2026): doubling every 196, 131 and 89 days. Frontier Risk Report: public frontier "~12h [5h-61h]"; "The TH 1.1 suite can't reliably measure time horizons above 16 hours." GPT-5.6 Sol at "around 11.3hrs" versus "beyond 270hrs", with "we do not consider any of these numbers to represent a robust measurement."
- FRI (Sept 2026): "forecasters dramatically underestimate AI progress on benchmarks"; $140 billion combined run rate; LEAP gives a 50% chance by 2030; "not yet seen evidence of improved accuracy on more recent questions"; 7.3% versus 2.5% for ride-hailing; Metaculus at 98%; Mythos Preview's 80% horizon of about 3.1 h; FrontierMath 40.7% versus medians of 30% and 31%; some models at superforecaster level on some question types; "does not appear to be the result of a binding directive".
- ForecastBench (ICLR 2025): superforecasters 0.096, public 0.121, Claude 3.5 Sonnet 0.122, on N = 200.
- ESPAI 2024 (AI Impacts, Sept 2026): 1,580 respondents, a 10% response rate; HLMI in 2042 and FAOL in 2098; "a gap of 56 years, the smallest to date"; median extinction or disempowerment of 10%. The figure spec already records the report's one-to-six-year recomputation of the earlier rounds.
- AI Futures Project: the automated-coder medians May 2028 → Nov 2027 (Kokotajlo) and Jul 2030 → Jan 2030 (Lifland); the definition is verbatim. Grading: "roughly 65%", then "more like 75%" in July 2026.
- Ho et al., NeurIPS 2024 version: an 8-month halving, 90% CI about 2–22 months. The arXiv preprint gives a 95% CI of 5–14, but the book cites the NeurIPS version, so the text is correct.
- BIS interim final rule, 91 FR 74970 (19 Nov 2026): remote-access data-centre licensing for D:5 and Macau headquarters, a new licence requirement for Indonesia, Malaysia, Singapore, Thailand and Brazil, and formal rescission of the AI Diffusion Rule.
- CAISI's DeepSeek V4 Pro evaluation (1 May 2026): "lag behind the frontier by about 8 months"; "the most capable PRC AI model evaluated by CAISI to date".
- St. Louis Fed (Sept 2026): 45% → 62% of adults aged 18–64. Census/NBER, Bonney et al.: 18% of firms, 32% weighted by employment (Nov 2025–Jan 2026).
- OpenAI's pause (18 Aug) and GPT-6.1 Astra (28 Sept) are consistent with Chapter 12 §12.7. The Anthropic export-control episode is consistent with Chapters 7 and 13.
- Cross-references to Sections 4.7, 5.3, 6.6 (the Navier–Stokes case), 8.7, 11.5, 13.2 and 13.7 point to matching content.

## Tally

Claims checked: 48 · confirmed: 44 · wrong: 0 · outdated: 0 · could not verify: 4
