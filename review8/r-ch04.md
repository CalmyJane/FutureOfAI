# Review 8: Chapter 4, Scaling, Compute and the Limits of Progress

## Verdict
Ready to print as it stands. I recomputed every worked example (C ≈ 6ND, MFU and GPU-hours, the Kaplan and Chinchilla formulas, the Besiroglu refit, Table 4.2, the Llama 3 sizing case, exact-match scores, the ARC-AGI-1 cost ratio and the METR doubling rates), and all of them are right. I checked the figures for named models against the primary sources: the Epoch model pages, the Epoch trends dashboard (5 Nov 2026), METR's Time Horizon 1.1 data file, the ARC Prize post, the Scale HLE leaderboard and the ClockBench leaderboard. Each matches what the book says, and none was out of date on 27 November 2026.

Balance between companies is good. Non-disclosure is attributed to "OpenAI, Anthropic and Google" alike. Anthropic's "first hybrid reasoning model on the market" is presented as Anthropic's own wording. The record results that favour Anthropic (the METR horizons for Opus 4.6 and Mythos Preview, the ClockBench lead of Fable 5.2) are reported with METR's own reliability caveats and alongside Google's scores. They are not given as rankings without that context.

## MUST change before printing
None.

## SHOULD change
None that rise above taste.

## Could not verify
- Line 165: the AI Index 2026 quotation "still no definitive evidence" (on synthetic data). The PDF of the official Chapter 1 would not extract to text. A secondary summary of the report uses the same words, and the report's own chapter highlights say that "synthetic data is still not replacing real data in pre-training". The substance is supported; I could not confirm that the quoted wording is verbatim.
- Line 24: Epoch's GPT-4.5 method (187 million H100-hours at 20–40% of the 8-bit peak). The resulting 3.8 × 10^26 FLOP is confirmed on Epoch's GPT-4.5 model page, and the arithmetic is right (2.7–5.4 × 10^26, geometric mean 3.8 × 10^26). I did not see the H100-hour input itself.
- Line 241: METR's March 2026 curve-fitting correction, and the statement that the 14.5-hour figure predates it. Plausible; not checked against METR's changelog.

## Checked and confirmed
- Arithmetic: AlexNet → Llama 3.1, ×8.1 × 10^7. 6ND = 3.79 × 10^25 (Llama) and 3.3 × 10^24 (DeepSeek-V3; 1.66× the parameters, 0.087× the compute). 26.4M GPU-hours, 67 days, gap ≈ 4.4M. 2^−0.076 = 0.95; 10^−0.05 = 0.89. 100^0.73 = 29, 100^0.27 = 3.5, 8^0.74 = 4.7. Chinchilla losses 1.99 and 1.94, and the Besiroglu refit 2.00 and 1.97 (ratio 2.6). Table 4.2 (3.15, 5.0, 5.9, 3.8 × 10^25, 7.2 × 10^23; 1,875 and 39 tokens per parameter). 77B / 1.5T; 402B × 16.55T = 4.0 × 10^25 at 41 tokens per parameter; 563B / 11.3T. p^10 = 0.1%, 11%, 35% and 90%. ARC-AGI-1: $4,560 / $26 = 175. METR: 2^(365/129) ≈ 7.1 per year. 5×/yr gives a 5.2-month doubling. 2 × 10^29 / GPT-4.5 = 526. Astra / GPT-4.5 = 2.47. 15.6T / 320T ≈ 1/20 and 36T / 320T ≈ 1/9.
- Kaplan constants, exponents and quotations ("more than seven orders of magnitude", "do not have a fundamental meaning", "every time we increase the model size 8x…", "significantly short of convergence"). GPT-4 report ("with high accuracy", "at most 10,000x less compute", HumanEval "may occasionally worsen with scale"). Chinchilla (>400 models; 70M to >16B; 5–500B tokens; E/A/B/α/β; all Table 4.1 values; 67.5% MMLU; "over 4.2 trillion tokens"; 1T unlikely below 10^26).
- Sevilla et al. (20 months, 6 months, late 2015, "10 to 100-fold"). Ho et al. (NeurIPS version: 90% CI 2–22 months; the arXiv version gives a 95% CI of 5–14; transformer 7.2×). Villalobos et al. (130T / 510T / 3,100T / 100T / 320T [95% CI 65T–1,700T]; 2.4×/yr; 2026–2032; repetition 3–15× capped at 5×).
- Epoch trends dashboard, 5 Nov 2026: 5×/yr (CI 4–6), 5.2 months, 10,000-fold, chips 2.5× (6× in 2023), costs 3.5×/yr, price-performance 1.49×, 30% inference share, ECI 14 vs 6 points per year.
- Epoch model pages: GPT-4.5 3.8e26, Grok 3 3.5e26, Grok 4 5.0e26, GPT-6 Astra 9.4e26 (GB200), Chinchilla 5.8e23. GPT-6 Astra released 3 Sep 2026 and rated Critical for cyber (OpenAI safety overview). Jensen Huang's statement of 100,000 GPUs.
- ARC Prize post: $26 (75.7%) and $4,560 (87.5%); 172× compute; repricing notes of 3/24/2025 and 12/10/2025; trained on 75% of the public training set.
- METR benchmark_results_1_1.yaml: doubling 187.8 days (all time) and 128.7 days (from 2023, CI 104–158). Opus 4.6 p50 718.8 min (≈12 h, CI 5.3–60.6 h) and p80 69.9 min. Mythos Preview (early) 1,044.8 min (≈17.4 h). Claude 3.7 Sonnet 60.4 min. GPT-2 0.054 min (≈3 s). The Decoder: "at least 16 hours" (8.5–55 h).
- Scale HLE leaderboard: GPT-6 Astra 54.80 ± 1.94 at the top; HLE-Rolling launched October 2025. ClockBench now: Fable 5.2 Max 87.8%, Gemini 4 Carbon 85%, Gemini 4 Argon 83.3%; human average 90.7%. The AI Index ClockBench figure of 50.6% matches "about half in March 2026". LMArena renamed Arena on 28 Jan 2026. The GPT-6 Pro parallel agents in ChatGPT (16 Oct 2026) and Muse Spark Contemplating mode are confirmed. Truong et al.: up to 84% precision, i.e. 42 of 50.
- AI Index quotation "Evaluations intended to be challenging for years are saturated in months" is verbatim; o3 87.7% on GPQA Diamond vs the 81.2% validator baseline; 17.1M H100-equivalents.
- Cross-references checked: Sections 1.7 (Sutton), 3.4, 3.5 (FineWeb), 3.7, 5.4, 6.5 (Deep Think IMO), 7.1 and 12.7, and Chapters 13 and 14. The METR figures agree with Chapters 5 and 14. The ClockBench figures agree with Chapter 1. Astra's compute agrees with Chapter 3.

## Tally
Claims checked: about 130. Confirmed: about 127. Wrong: 0. Outdated: 0. Not verified: 3 (listed above).
