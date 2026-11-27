# Review 7: Chapter 4, Scaling, Compute and the Limits of Progress

## Verdict
Ready to print. I recomputed every worked number and found no error. That covers 6ND for each model, the GPU-hour conversion, the Kaplan and Chinchilla exponents and loss terms (original and Besiroglu fits), the Llama 3 sizing, the 77B alternative, the exact-match powers, the ARC-AGI ratio, the doubling conversions and the Epoch ratios. Quotations and the 2025–26 facts I checked against sources are correct. One figure looked wrong at first: Ho et al.'s "90% CI 2 to 22 months". It is right for the NeurIPS version the book cites; the arXiv preprint gives 95% CI 5–14 months. The SHOULD items below concern one source figure I could not match, a time-horizon value that differs from widely reported numbers, and wording.

## MUST change before printing
None.

## SHOULD change

### S1. The data-stock figures do not match the authors' own summary
- Where: textbook/chapters/ch04.md:149
- Text now: "Filtering for quality reduces the usable stock to about 100 trillion tokens. Allowing for each token to be used several times in training raises the effective stock to about 320 trillion, with a 95% confidence interval of 65 to 1,700 trillion."
- Problem: UNSUPPORTED (as far as I can check). Epoch's summary of the paper gives "on the order of 300 trillion tokens", with a 90% confidence interval of 100T to 1000T. The arXiv HTML text contains neither "320", "65T" nor "1700"; it gives the quality-usable share as a fraction ("between 10% and 40%"), not as 100T. The arithmetic also does not follow: 100T times the 5× repetition cap the paragraph itself mentions (line 153) would be about 500T, not 320T. The figures may come from a chart in the ICML PDF, but they need checking.
- Evidence: https://epoch.ai/blog/will-we-run-out-of-data-limits-of-llm-scaling-based-on-human-generated-data ("on the order of 300 trillion tokens", 90% CI 100T–1000T); https://arxiv.org/html/2211.04325 ("between 10% and 40% of deduplicated web data can be used for training"; "For this reason we reduce it to 5x").
- Change to (if the ICML PDF does not show 320/65–1,700): "Only part of this, between 10 and 40% of de-duplicated web text by the authors' estimate, is good enough to train on. Allowing for each token to be used several times in training, they put the effective stock at about 300 trillion tokens (90% confidence interval 100 to 1,000 trillion)." Then also change "central estimate" at line 151: 15.6T ≈ one-twentieth and 36T ≈ one-eighth of 300T, so "about a ninth" becomes "about an eighth".

### S2. Claude Opus 4.6 time horizon differs from the widely reported METR figure
- Where: textbook/chapters/ch04.md:237 and 241
- Text now: "from about 3 seconds for GPT-2 (2019) to 12 hours for Claude Opus 4.6 (February 2026)" … "Claude Opus 4.6's 50% interval runs from about 5 to 61 hours"
- Problem: UNCLEAR. When METR added Opus 4.6 in February 2026, the figure reported was about 14.5 hours (CI about 6 to 98 hours), with an 80% horizon of about 1 hour 3 minutes. METR corrected "a regularization mistake that affected our measurements" on 3 March 2026, which probably explains the book's lower post-correction values. I could not open the data file to confirm the 12 h, 5–61 h and 70 min figures. Readers who have seen "14.5 hours" will think the book is wrong unless it says why the numbers differ.
- Evidence: https://officechai.com/ai/exponential-progress-claude-opus-4-6-has-50-time-horizon-of-14-5-hours-on-metr-time-horizons-benchmark (Feb 2026: "50% Time Horizon Of 14.5 Hours"); https://metr.org/time-horizons/ changelog, 3 March 2026: "Corrected a regularization mistake that affected our measurements."
- Change to: after confirming against the data file, add at line 241 after "METR corrected an error in its curve-fitting in March 2026": "(which lowered Claude Opus 4.6's estimate from the 14.5 hours first reported)".

### S3. Sutskever's role at SSI
- Where: textbook/chapters/ch04.md:155
- Text now: "Ilya Sutskever, a co-founder of OpenAI who has led the start-up Safe Superintelligence since 2025"
- Problem: UNCLEAR. Sutskever co-founded SSI in June 2024 and became its chief executive in July 2025, after Daniel Gross left. "Led … since 2025" is defensible only as CEO, and readers may infer that he joined in 2025.
- Evidence: the bib entry zeff2025ilya (TechCrunch, July 2025: Sutskever becomes SSI CEO).
- Change to: "Ilya Sutskever, a co-founder of OpenAI who co-founded the start-up Safe Superintelligence in 2024 and has been its chief executive since 2025".

### S4. Duplicate cross-reference
- Where: textbook/chapters/ch04.md:229
- Text now: "up from about half in March 2026 (Section 1.7) [@sajadieh2026ai]. By late November 2026 the leader had reached 87.8%, still below the human average (Section 1.7)"
- Problem: UNCLEAR (editing). The same cross-reference appears twice in consecutive sentences. Also, Section 1.7 names the November leader (Claude Fable 5.2 Max) but this passage does not.
- Change to: "…up from about half in March 2026 [@sajadieh2026ai]. By late November 2026 the leader, Anthropic's Claude Fable 5.2 Max, had reached 87.8%, still below the human average (Section 1.7) [@clockbench2026clockbench]."

## Could not verify
- Epoch figures: the database values in Table 4.3 (costs and confidence labels), the GPT-6 Astra interval of 5 × 10^26 to 2 × 10^27, and the dashboard rates (5×/yr with 90% CI 4–6, 2.5×/yr, 3.5×/yr, 1.49×/yr, about 30% inference share, ECI 14 vs 6 points). The 9.4 × 10^26 estimate and its assumptions (≥100,000 GB200 chips, 90 days, 25% utilisation) are confirmed by a secondary page citing Epoch (futuresearch.ai). The Astra release date of 3 Sep 2026 is confirmed by Epoch's 12 Sep 2026 brief.
- Claude Mythos Preview's "at least 16 hours" (via The Decoder) and the 129- and 188-day doubling times from the METR data file.
- ClockBench human baseline of 90.7%. Launch coverage gave 89.1%, so it was probably updated later; Chapter 1 uses the same 90.7%, so the book is consistent with itself.
- Truong et al.: the per-benchmark counts (2 on part of MMLU, 42 on GSM8K). The paper reports precision@50 on nine benchmarks and a maximum of "up to 84%" (= 42/50), but the per-benchmark bars are only in a figure.
- The 1,205-problem size of GSM1k (the abstract gives no count). The "up to 8%" drop and Spearman r² = 0.36 are confirmed.

## Checked and confirmed
- Arithmetic:
  - AlexNet to Llama: 8.1 × 10^7.
  - 6ND: 3.79 × 10^25 for Llama; 3.29 × 10^24 for DeepSeek-V3; Table 4.2 (5.04, 5.88, 7.2 × 10^23; 3.15 × 10^23); tokens per parameter.
  - GPU-hours: 26.4M GPU-hours and 67 days, against 30.84M (the gap is ~4.4M).
  - GPT-4.5 compute: 187M H100-h at 20–40% of the 1,979 TFLOP/s FP8 peak gives 2.66–5.33 × 10^26, geometric mean 3.77 × 10^26.
  - Kaplan exponents: 2^−0.076 = 0.95, 10^−0.05 = 0.89, 8^0.74 ≈ 4.7, 100^0.73 = 29, 100^0.27 = 3.5.
  - Chinchilla loss terms: 1.99/1.94, and 2.00/1.97 with the Besiroglu fit; Gopher's data term is 4.8× its model term in the original fit and 2.6× in the refit.
  - Llama 3 sizing: 402B × 16.55T gives 4.0 × 10^25; at 20 tokens per parameter the budget gives 563B on 11.3T; the alternative is 77.5B on 1.55T.
  - Exact-match powers: 0.5^10, 0.8^10, 0.9^10, 0.99^10 = 0.1%, 11%, 35%, 90%.
  - ARC-AGI: 4,560/26 = 175; 87.5 − 75.7 ≈ 12 points.
  - Ratios: 5×/yr is a doubling every 5.2 months; a 129-day doubling is ≈ 7×/yr; 2 × 10^29/3.8 × 10^26 ≈ 500; 9.4/3.8 ≈ 2.5; Astra/GPT-3 ≈ 3,000.
- Ho et al. (NeurIPS 2024): "halved approximately every 8 months", 90% CI about 2–22 months, transformer 7.2× (https://proceedings.neurips.cc/paper_files/paper/2024/hash/6b066da6a23bc55f9b887e7298102884-Abstract.html).
- Chinchilla: "over 4.2 trillion tokens" for 175B; the 1T model and 10^26; E, A, B, α, β; the Table 4.1 exponents and ranges; 67.5% MMLU.
- ARC Prize o3: 75.7% at $26, 87.5% at $4,560, "roughly 172x", repricing notes dated 3/24/2025 and 12/10/2025, "trained … on 75% of the Public Training set" (arcprize.org/blog/oai-o3-pub-breakthrough).
- Yue et al. "rarely elicit[s]"; Zhang et al. GSM1k ("up to 8%", r² = 0.36).
- GPQA 65% experts across the full pool, 198 Diamond questions, o3 87.7%.
- Arena: LMArena renamed Arena on 28 January 2026 (arena.ai blog).
- Sutskever "The data is very clearly finite" and "age of scaling" → "age of research" (Dwarkesh Podcast, 25 Nov 2025).
- Other quotations and figures checked: Kaplan quotes, GPT-4 report ("at most 10,000x less compute", "may occasionally worsen with scale"), Meta's Llama 3 report (466 interruptions, 78%, MFU 38–43%, "higher than 90% effective training time"), PaLM MFU/HFU, o1/o3 statements, Brown et al. coverage figures, Snell (4×, 14×), s1 (50% → 57%), Claude 3.7 "first hybrid reasoning model on the market", Muennighoff (4 and 16 epochs), Shumailov, AI Index ($20 → $0.07, 280-fold), GPT-4.5 vs GPT-4o vs o3-mini AIME (36.7/9.3/87.3).
- Cross-references: Sections 1.7 (Sutton and ClockBench, consistent at 83.3%/87.8%), 3.4, 3.5, 3.7, 4.x, 5.4 (a setting-dependent score), 6.5 (IMO), 7.1, 12.7, Chapter 13 (frontier and compute thresholds) and Chapter 14. All exist and match.
- Consistency with Chapter 3: R1 RL ≈ 5% of V3, V3.2 above 10%, about 100:1 pre- to post-training, Astra 9.4 × 10^26 and "some 3,000 times GPT-3", the 2N and 6N rules. All consistent.

## Tally
Claims checked: about 130. Confirmed: about 118. Wrong: 0. Outdated: 0. Unsupported or unclear: 2 (S1, S2). Could not verify: about 10.
