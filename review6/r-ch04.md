# Review 6: Chapter 4, Scaling, Compute and the Limits of Progress

## Verdict

Ready to print after minor fixes. I recomputed every worked example and every 6ND figure, and all of them hold:
- AlexNet to Llama, the GPU-hours, and the GPT-4.5 hardware estimate;
- the Kaplan exponents, the Chinchilla losses (both the original and the corrected fit), and Table 4.2;
- the 77B/1.5T counterfactual and the Llama 3 case study;
- the exact-match powers, ARC's 175×, and the METR doubling times.

The 2026 figures match their primary sources: Epoch's trends dashboard of 5 Nov 2026, METR's TH1.1 data file, the Scale HLE leaderboard, ClockBench, GPT-6 Astra, and the Arena rename. Nothing is wrong, misquoted or legally sensitive. The SHOULD items are a misplaced citation, one claim that may be out of date, and repetition with Chapters 1 and 3.

## MUST change before printing

None.

## SHOULD change

### S1. An October 2026 ClockBench figure is cited to the April 2026 AI Index
- Where: textbook/chapters/ch04.md:229
- Text now: "On 25 October 2026 the best model, Google's Gemini 4 Argon, scored 83.3%, up from about half in March 2026 (Section 1.7) [@sajadieh2026ai]."
- Problem: UNSUPPORTED (citation mismatch). The AI Index was published on 13 April 2026, so it cannot support the 25 October score. That score comes from the ClockBench leaderboard (the bib note for clockbench2026clockbench records it), which is cited only in the next sentence.
- Evidence: https://clockbench.ai/ (accessed 27 Nov 2026): "Average human 90.7%", with Claude Fable 5.2 Max at 87.8% and Gemini 4 Carbon High at 85%. The HAI release date is 13 April 2026.
- Change to: "On 25 October 2026 the best model, Google's Gemini 4 Argon, scored 83.3% [@clockbench2026clockbench], up from about half in March 2026 (Section 1.7) [@sajadieh2026ai]."

### S2. "never published" for GSM1k may be out of date
- Where: textbook/chapters/ch04.md:225
- Text now: "...matched to the widely used GSM8K benchmark in difficulty, number of solution steps and answer size, and never published [@zhang2024careful]."
- Problem: OUTDATED (possible). The paper withheld the set but committed to releasing it by June 2025 at the latest. Since then Scale has published at least a 50-question sample, and a ScaleAI/gsm1k dataset repository exists on Hugging Face. I could not confirm whether the full set is now public, so "never published" is not safe.
- Evidence: https://arxiv.org/html/2405.00332: "we will not be releasing the dataset publicly at this time", with a commitment to release it by June 2025. https://labs.scale.com/leaderboard/math says Scale decided "to publicly release only 50 samples".
- Change to: "...and withheld from publication to avoid contamination [@zhang2024careful]."

### S3. Section 4.6 repeats Chapter 3 nearly word for word
- Where: textbook/chapters/ch04.md:181, 195, 199, 201
- Text now: several sentences repeat material from Section 3.7 and Section 3.8, with the same quotations:
  - Claude 3.7 Sonnet as "the first hybrid reasoning model on the market";
  - Qwen3's thinking budget;
  - the GPT-5 "real-time router";
  - Grok 4 "at pretraining scale";
  - DeepSeek-V3.2's ">10%" budget;
  - Grok 4 Heavy and Muse Spark's parallel modes.
- Problem: UNCLEAR (repetition). A reader who goes straight through meets the same quotations twice within about 30 pages. Section 3.8 already says "Section 4.6 describes these controls".
- Evidence: compare ch03.md:389 and 457–459 with ch04.md:181 and 195–201.
- Change to: keep the full treatment in Section 4.6. In Section 3.8, shorten "Reasoning, and control over it" to two sentences ending in the pointer to Section 4.6. At minimum, drop the repeated quotation marks in one of the two places.

### S4. ClockBench sentences duplicate Chapter 1
- Where: textbook/chapters/ch04.md:229
- Text now: "By late November 2026 the leader was Anthropic's Claude Fable 5.2 Max (its highest setting), released on 9 November, at 87.8%, ahead of Google's Gemini 4 Carbon at 85.0%"
- Problem: UNCLEAR (repetition). Chapter 1 (ch01.md:255) gives the same human score, the same three model scores and the same dates.
- Evidence: ch01.md:255.
- Change to: "By late November 2026 the leader had reached 87.8%, still below the human average (Section 1.7) [@clockbench2026clockbench]."

## Could not verify

- **Epoch's amortised costs in Table 4.3** ($0.6M, $37M, $53M, $218M, $366M, $388M) and the confidence labels. The database page did not render. They are consistent with Cottier et al.'s ~$40M for GPT-4.
- **The basis of Epoch's GPT-6 Astra estimate** (at least 100,000 GB200 chips, 90 days at 25% of the 8-bit peak). Only secondary summaries were reachable (FutureSearch, Digg), and they agree on 9.4×10^26 and those assumptions. My own estimate comes out at about 9.7×10^26, assuming about 5 PFLOP/s dense FP8 per chip.
- **The Gemini 4 Argon and Carbon ClockBench scores on 25 October.** These rest on the bib note. The current page agrees for Carbon and for Fable 5.2 Max.
- **GPT-6 Pro parallel agents (16 Oct 2026).** Several secondary outlets confirm it. The RuntimeWire URL cited now serves an API page.

## Checked and confirmed (brief)

- **Arithmetic.**
  - 4.7e17 → 3.8e25 is about 81 million times.
  - 6·405e9·15.6e12 = 3.79e25, and 6·37e9·14.8e12 = 3.29e24, which is less than a tenth of Llama's.
  - 26.4M GPU-hours, 67 days and a 4.4M gap.
  - GPT-4.5: 187M H100-hours at 20–40% of 1,979 TFLOP/s gives 2.7–5.3e26, with a geometric mean of 3.8e26.
  - 2^−0.076 = 0.95, 10^−0.05 = 0.89, 100^0.73 = 29, 100^0.27 = 3.5, 8^0.74 = 4.7.
  - Chinchilla losses 1.99 and 1.94, a data/model ratio of 4.8, and the Besiroglu refit giving 2.00/1.97 with a ratio of 2.6.
  - Table 4.2 (all rows), 77B/1.55T, 402B×16.55T → 4.0e25, and 563B/11.3T.
  - 0.5^10 … 0.99^10, 175× for ARC, 129/188 days giving about 7× a year, 2e29/3.8e26 ≈ 500, and Astra/GPT-4.5 ≈ 2.5.
- **Kaplan and Chinchilla.**
  - Chinchilla: "4.2 trillion tokens", "unless one has a compute budget of 10^26 FLOPs … 1 trillion parameter model", "67.5% … greater than a 7% improvement", and the values in Table 4.1.
- **Ho et al.** The 8-month halving with a 90% CI of 2–22 months matches the NeurIPS 2024 version (the preprint says 95% CI 5–14). The transformer gain of 7.2× is "nearly two years".
- **Villalobos et al. (ICML).**
  - Stock: Common Crawl 130T, indexed web 510T, whole web 3,100T, an effective stock of 320T [65T, 1,700T], a median exhaustion year of 2028, and a projection of 2026–2032.
  - Data trends: datasets grew 2.4× a year, and the repetition multiplier of 3–15× was reduced to 5×.
- **GSM1k and GPQA.** GSM1k: 1,205 problems, up to an 8% drop, r² = 0.36, and frontier models showing "minimal signs of overfitting". GPQA Diamond: 198 questions, experts at 81.2% (Table 5) with selection-effect caveats, 65% across the full pool.
- **ARC Prize.** 75.7% at $26 per task and 87.5% at $4,560 per task, 172× the compute, repricings on 3/24/2025 and 12/10/2025, and 75% of the public training set seen in training.
- **METR TH1.1 data file.**
  - Doubling times: 128.7 days since 2023 and 187.8 days overall.
  - Claude models: Opus 4.6 at 719 minutes (12.0 h), CI 5.3–60.6 h, with an 80% horizon of 70 minutes. Mythos Preview (early) at 17.4 h, CI 8.5–55 h. Claude 3.7 Sonnet at 60 minutes.
  - GPT-2 at about 3 seconds.
  - The page notes the regularisation correction of 3 March 2026, that it has not been actively updated since 8 September 2026, and that results above 16 h are unreliable.
- **Epoch trends (5 Nov 2026).** 5×/year with a 4–6× CI, ~10,000× growth for the top 5 models, chip compute up 2.5×/year (6× in 2023), costs up 3.5×/year, price-performance up 49%/year, ECI rising 14 versus 6 points a year, and 30% of compute spent on inference.
- **AI Index 2026.** "saturated in months", 3.3×/year growth and 17.1M H100-equivalents.
- **Benchmarks and leaderboards.** Scale HLE: GPT-6 Astra at 54.80 (2,500 questions, updated September 2026). Astra's own HLE score with tools is 57.2%, which supports "higher scores when models may use tools". LMArena became Arena on 28 Jan 2026. Truong et al.: nine benchmarks, up to 84% precision, consistent with 42 of 50.
- **Quotations checked word for word.** Grok 4: "at pretraining scale", "over an order of magnitude more compute", "parallel test-time compute…". DeepSeek-V3.2 ">10%" (post-training). Edelman et al., cited for GPT-5 versus GPT-4.5.
- **Cross-references.** All exist with matching content: 1.7, 3.4, 3.5, 3.7, 5.4, 6.5, 7.1, 7.5, 12.7, and Chapter 13 on legal definitions of frontier models.

## Tally

Claims checked: about 110. Confirmed: about 106. Wrong: 0. Outdated: 1 (possible; S2). Citation mismatch: 1 (S1). Repetition: 2 (S3, S4).
