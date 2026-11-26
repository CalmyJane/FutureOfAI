# Chapter 4: Scaling, Compute and the Limits of Progress (fourth review)

## Verdict

Ready to print after two small fixes. I recomputed every calculation in the chapter and checked every Epoch, METR, AI Index, ARC Prize, ClockBench and HLE figure against its source as of 26 November 2026. All the numbers and quotations I checked were correct. That includes Table 4.3, which matches Epoch's current CSV to rounding, and Figure 4.3, which matches METR's TH1.1 data file. One cross-reference is wrong, and one leaderboard statement should carry its date.

## MUST change before printing

None.

## SHOULD change

### S1. ClockBench cross-reference points to the wrong section
- Where: textbook/chapters/ch04.md:229
- Text now: "On 25 October 2026 the best model, Google's Gemini 4 Argon, scored 83.3%, up from about half in March 2026 (Section 1.8)."
- Problem: INCONSISTENT. The clock-reading passage in Chapter 1, with "in March 2026 the best model read analogue clocks correctly only about half the time", is at ch01.md:255. That is in Section 1.7 ("Deep learning, foundation models and assistants (2011–2026)"). Section 1.8 starts at line 260.
- Evidence: textbook/chapters/ch01.md:177 (heading 1.7), :255 (ClockBench passage), :260 (heading 1.8).
- Change to: "On 25 October 2026 the best model, Google's Gemini 4 Argon, scored 83.3%, up from about half in March 2026 (Section 1.7)."

### S2. HLE leaderboard: give the date of the leaderboard, not just "by November 2026"
- Where: textbook/chapters/ch04.md:231
- Text now: "By November 2026 the top entry on Scale AI's leaderboard, GPT-6 Astra, scored 54.8% on the full public set [@scale2026humanity]."
- Problem: UNCLEAR. The score and ranking are correct: GPT 6 Astra 54.80 ± 1.94, ahead of Fable 5.1 (xhigh) at 46.50. But the leaderboard was last updated on 17 September 2026, and it has not evaluated Fable 5.2 or GPT-6.2 Astra, both released in November. "By November 2026" invites the reading that it is the November state of the art.
- Evidence: https://labs.scale.com/leaderboard/humanitys_last_exam (accessed 26 Nov 2026): "GPT 6 Astra: 54.80 ± 1.94"; page last updated 17 September 2026.
- Change to: "On Scale AI's leaderboard, last updated in September 2026, the top entry, GPT-6 Astra, scored 54.8% on the full public set [@scale2026humanity]." (and at :258, "reached 54.8% within two years" stays correct).

## Could not verify

- Epoch's documentation saying that MFU of 30–50% is typical (:17), and the wording of Epoch's confidence-label definitions (factor 3/10/30, :24). Both are consistent with Epoch's database labels, but I did not open the documentation page.
- HLE paper's 13.4% for o3-mini (high) on text-only questions (:231). The January 2025 preprint gave a slightly different figure, and I did not check the *Nature* version's table.
- *The Decoder*'s report of METR's "at least 16 hours" for early Mythos Preview (:237). The METR data file confirms the underlying values (17.4 h, CI 8.5–55 h).

## Checked and confirmed (brief)

- **Arithmetic, all reproduced:**
  - 6ND for Llama 3.1 405B (3.79 × 10^25^) and DeepSeek-V3 (3.29 × 10^24^); AlexNet ratio about 80 million; 26.4 M GPU-hours / 67 days; gap of 4.45 M
  - Kaplan exponents (0.95; 0.89; 100^0.73^ = 29; 100^0.27^ = 3.5; 8^0.74^ = 4.7)
  - Chinchilla fit for Gopher/Chinchilla (1.99/1.94; data term 4.8× model term). Besiroglu refit 2.00/1.97, ratio 2.6.
  - Table 4.2 (all rows); 77 B / 1.5 T; 402 B × 16.55 T ≈ 4.0 × 10^25^; 563 B / 11.3 T
  - p^10^ series; ARC 4,560/26 ≈ 175; 2^365/129^ ≈ 7.1; 5×/yr ↔ 5.2 months; 320 T × 1/20 and 1/9; 2 × 10^29^ ≈ 526 × GPT-4.5; Astra/GPT-4.5 ≈ 2.5
  - GPT-4.5 hardware estimate (2.7–5.3 × 10^26^, geometric mean 3.8 × 10^26^)
- **Epoch AI:**
  - Database export of 26 Nov 2026: AlexNet 4.7e17; DeepSeek-V3 3.3e24; Gopher 6.31e23; Chinchilla 5.76e23; GPT-4 (Mar 2023) 2.1e25 "Likely"; Grok 3 3.5e26; GPT-4.5 3.8e26 with note "187M H100-hours ... 20 to 40% ... geomean of 3.8e26"; Grok 4 5e26 "Speculative"; GPT-6 Astra 9.4e26 "Likely", "≥100,000 GB200s ... 90 days at 25% FP8 MFU", CI about 5e26–2e27; largest estimate in the database
  - Table 4.3 costs ($0.64 M, $37.3 M, $52.9 M, $217.8 M, $366.0 M, $387.8 M)
  - Figure 4.2: 13 points, and the open/filled markers match the confidence labels
- **Epoch trends dashboard (5 Nov 2026):** 5× per year (4–6), 5.2-month doubling, 10,000× top five; chips 2.5× per year since 2024 vs about 6× in 2023; cost 3.5× per year; price-performance 1.49×; 30% of compute on inference; ECI 14 points per year (12–17) vs 6.
- **Edelman et al.:** about 10× less pre-training compute with reasoning; "10× every 4 months"; "<3×" of GPT-4 for 2.5 years and Behemoth; GPT-5 below GPT-4.5; GPT-6 "probably more than GPT-4.5".
- **2026 AI Index:** non-disclosure sentence; GPQA validator baseline 81.2% and o3's 87.7% in late 2024; "saturated in months"; "still no definitive evidence" on synthetic data; 3.3× per year to 17.1 M H100e.
- **Chinchilla paper:** "over 4.2 trillion tokens" for 175 B; 10^26^ for 1 T; Table 4.1 values.
- **GPT-4 report:** "at most 10,000x less compute", "high accuracy", "may occasionally worsen with scale".
- **Ho et al.:** "90% confidence interval of around 2 to 22 months" is the published NeurIPS abstract (the arXiv preprint says 95% CI 5–14 months, so the book follows the published version); 7.2× transformer gain.
- **Villalobos et al.:** 130 T/510 T/3,100 T; 320 T (65–1,700 T); 2.4× per year; median 2028; 3–15× capped at 5×.
- **ARC Prize page:** 75.7% at $26/task, 87.5% at $4,560/task, about 172× compute, repriced with o1-pro (Mar 2025) and o3-pro (Dec 2025), trained on 75% of the public training set.
- **METR:**
  - TH1.1 data file: doubling of 128.7 days since 2023 and 187.8 days overall; Opus 4.6 50% = 718.8 min (CI 5.3–60.6 h), 80% = 69.9 min; Mythos Preview (early) 17.4 h (8.5–55 h); GPT-2 ≈ 3 s; Claude 3.7 Sonnet 60 min
  - TH1.1 blog: 170 → 228 tasks, 29 Jan 2026
  - Time-horizons page: "no longer actively updated" (8 Sep 2026); 3 Mar 2026 correction; 16 h limit
- **ClockBench:** Fable 5.2 Max 87.8% leads; human average 90.7%; Gemini 4 Argon High 83.3%.
- **GPT-6 Pro:** parallel agents in ChatGPT, 16 Oct 2026.
- **Truong et al.:** precision up to 84% (42 of 50 on GSM8K).
- **xAI naming:** all of Chapter 4's xAI references are to 2025 events, so the rename noted in r-ch03 S1 does not apply here.

## Tally

Claims checked: 142 · confirmed: 139 · wrong: 0 · outdated: 0 · inconsistent: 1 (S1) · unclear: 1 (S2)
