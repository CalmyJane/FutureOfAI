# Review 5: Chapter 4, Scaling, Compute and the Limits of Progress

## Verdict

**Ready to print after one fix.** I recomputed every piece of arithmetic in the chapter, and all of it holds:

- 6ND for Llama 3.1 and DeepSeek-V3.
- The GPU-hours and the 67 days.
- The GPT-4.5 geometric mean.
- The Kaplan exponents (0.95, 0.89, 29×, 3.5×, 8^0.74^≈5).
- Both Chinchilla loss evaluations, with the original and with the Besiroglu refit (1.99/1.94 and 2.00/1.97; ratio 2.6).
- Table 4.2.
- The 77B/1.5T and 402B/16.55T (4.0×10^25^) figures, and the 560B/11T alternative.
- The exact-match powers.
- ARC's 175×.
- 129-day doubling ≈ 7× a year.

I checked the Epoch figures (compute, confidence labels, costs, the GPT-4.5 and GPT-6 Astra estimation notes) against Epoch's live CSV. The METR figures match the live Time Horizon 1.1 data file: Opus 4.6 at 718.8 min, CI 5.3–60.6 h, p80 69.9 min; Mythos early at 17.4 h; GPT-2 at 3.2 s; doublings of 128.7 and 187.8 days. The Epoch trends dashboard, the ClockBench and HLE leaderboards, and the ARC Prize repricing also match.

There is one MUST item: a cross-reference that points to text that does not exist, together with an unsourced figure. There is one SHOULD item, an outdated company name.

## MUST change before printing

### M1. ClockBench "about half in March 2026 (Section 1.7)": no such text in Chapter 1, and the figure has no source
- Where: textbook/chapters/ch04.md:229
- Text now: "On 25 October 2026 the best model, Google's Gemini 4 Argon, scored 83.3%, up from about half in March 2026 (Section 1.7)."
- Problem: INCONSISTENT / UNSUPPORTED.
  - Chapter 1 never mentions ClockBench, clocks or a March 2026 score. `grep -i clock ch01.md` returns nothing, and Section 1.7 (lines 177–259) has no such passage. The cross-reference sends the reader to nothing.
  - The bib entry @clockbench2026clockbench records only the 25 October and 22 November readings, so "about half in March 2026" has no source in the book.
- Evidence: textbook/chapters/ch01.md (whole file searched); textbook/bib/ch04.bib, clockbench2026clockbench howpublished field: "leader Gemini 4 Argon High 83.3% when accessed 25 October 2026; leader Claude Fable 5.2 Max 87.8% when accessed 22 November 2026". The live leaderboard at https://clockbench.ai/ (accessed 27 Nov 2026) shows: Claude Fable 5.2 Max 87.8%, Gemini 4 Carbon High 85%, Gemini 4 Argon High 83.3%; average human 90.7%.
- Change to: "On 25 October 2026 the best model, Google's Gemini 4 Argon, scored 83.3%." Delete "up from about half in March 2026 (Section 1.7)". If the author wants to keep the trend, they need a dated source (for example an archived leaderboard snapshot from March 2026) added to the bib.

## SHOULD change

### S1. LMArena has been called "Arena" since January 2026
- Where: textbook/chapters/ch04.md:227
- Text now: "Chatbot Arena (renamed LMArena in 2025) shows users the answers of two anonymous models and asks which is better. … LMArena, which runs the platform, disputed several of the paper's figures"
- Problem: OUTDATED. The platform rebranded from LMArena to Arena (arena.ai) on 28 January 2026, which is before the book's currency date. The LMArena response (April 2025) can still be cited under its old name.
- Evidence: https://arena.ai/blog/lmarena-is-now-arena/ ("LMArena is now Arena"); secondary summaries give the date as 28 January 2026, with lmarena.ai redirecting to arena.ai.
- Change to: "Chatbot Arena (renamed LMArena in 2025 and Arena in January 2026) shows users the answers of two anonymous models and asks which is better. … LMArena, as the operator was then called, disputed several of the paper's figures". Cross-chapter: ch07.md:294 says "On the LMArena leaderboard"; it should become "On the Arena (formerly LMArena) leaderboard".

## Could not verify

- The 2026 AI Index figures: total capacity growth of 3.3× a year since 2022, 17.1 million H100-equivalents, the "saturated in months" quote, and "still no definitive evidence" on synthetic data. I did not fetch the report text.
- "METR corrected an error in its curve-fitting in March 2026." This is not stated on the current time-horizons page.
- HLE's original-paper best score (o3-mini high, 13.4%) as given in the *Nature* version. It matches the arXiv version; I did not re-check the Nature tables.
- The Snell "4×" and "14×" figures and the Brown et al. MATH figures (82.9→98.44%, 40.50→41.41%). These are consistent with my memory of the papers but were not re-fetched.

## Checked and confirmed (brief)

- **Epoch CSV:**
  - AlexNet 4.7×10^17^ (ratio 8.1×10^7^ ≈ 80 million).
  - GPT-3 3.14×10^23^, Gopher 6.31×10^23^, Chinchilla 5.76×10^23^, Llama 3.1-405B 3.8×10^25^, DeepSeek-V3 3.3×10^24^.
  - Grok 3 3.5×10^26^ (Likely, $218M); GPT-4.5 3.8×10^26^ (Likely, $366M; 187M H100-h at 20–40% FP8 gives 2.7–5.4×10^26^); Grok 4 5×10^26^ (Speculative, $388M).
  - GPT-6 Astra 9.4×10^26^, Likely, CI ~5×10^26^ to 2×10^27^, ≥100k GB200 for 90 days at 25% FP8. Published 3 Sep 2026.
- **Epoch trends dashboard (5 Nov 2026):** 5×/yr (4–6), 5.2 months, ~10,000-fold for the top 5, chips 2.5×/yr since 2024 versus ~6× in 2023, cost 3.5×/yr, price-performance 1.49×/yr, inference 30% of OpenAI's 2024 compute spending, ECI 14 versus 6 points a year.
- **Papers:**
  - AlexNet "five to six days".
  - Chinchilla: 67.5% MMLU "greater than a 7% improvement"; 175B on "over 4.2 trillion tokens"; 1T unlikely optimal below 10^26^.
  - The GPT-4 report's "at most 10,000x less compute", "high accuracy" and "may occasionally worsen with scale".
  - GPQA Diamond: 198 questions, 81.2%/65%.
  - GSM1k: 1,205 problems, up to 8%, r² = 0.36.
  - Villalobos: 320T [65T, 1700T], 2.4×/yr, 2026–2032.
  - Ho et al.: NeurIPS abstract gives 90% CI 2–22 months; transformer 7.2×.
- **Leaderboards and announcements:**
  - ARC Prize: 75.7% at $26, 87.5% at $4,560, 172×, repriced 24 Mar and 10 Dec 2025, 75% of public training set.
  - ClockBench values and the human average.
  - HLE Scale leaderboard: GPT-6 Astra 54.80, updated 17 Sep 2026.
  - GPT-6 Pro parallel agents in ChatGPT (16 Oct 2026; widely reported).
- **Cross-references:** Sections 1.7 (Sutton), 3.4, 3.5, 3.7, 5.4, 6.5, 7.1 and 12.7 and Chapters 13 and 14 resolve correctly, except the ClockBench reference in M1. Figures are consistent with Chapter 3 (o3 at 10× o1, RL share, GPT-6 Astra date and compute).

## Tally

Claims checked: 104. Confirmed: 102. Wrong or unsupported: 1 (M1). Outdated: 1 (S1).
