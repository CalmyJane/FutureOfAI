# Chapter 4: Scaling, Compute and the Limits of Progress — ninth review

## Verdict
Ready to print as it stands. I recomputed every worked example and found it correct. The Epoch, METR, ClockBench, HLE and ARC figures match the live sources: I read Epoch's notable-models CSV directly (downloaded 27 Nov 2026), the METR Time Horizon 1.1 YAML, and the ClockBench and Scale leaderboards. Quotations I sampled are verbatim. Cross-references are correct: §1.7 (Sutton and ClockBench), §3.4, §3.5, §3.7, §5.4, §6.5, §7.1, §12.7 and Chapters 13 and 14.

**Balance between companies.** The chapter is even-handed. Record holders are reported as the data show them: GPT-6 Astra leads the HLE leaderboard and Epoch's compute list; Claude Opus 4.6 and Mythos Preview hold the METR records; Claude Fable 5.2 leads ClockBench, with the note that the GPT-6.2 models were not yet listed. Anthropic's "first hybrid reasoning model on the market" is attributed to Anthropic as its own claim. The Leaderboard Illusion figures about Meta, Google and OpenAI are marked as from the preprint, and LMArena's rebuttal is cited, so the passage is not legally exposed. Developer claims from OpenAI, xAI, Meta, DeepSeek and Google are consistently flagged as company statements without figures. I found no tilt towards Anthropic or against any other developer.

## MUST change before printing
None.

## SHOULD change
None that rise above taste.

## Could not verify
- l. 24: Epoch's exact definitions ("confident" within 3×, "likely" 10×, "speculative" 30×). They are consistent with Epoch's usage; I did not open the documentation page.
- l. 165: the AI Index 2026 phrase "still no definitive evidence". Secondary summaries of Chapter 1 of the AI Index match the substance; I did not see the exact wording.
- l. 229: ClockBench "up from about half in March 2026" (AI Index). Chapter 1 cites the same figure, so the two chapters agree.
- l. 201: Muse Spark's "Contemplating" mode quote, and GPT-6 Pro parallel agents (16 Oct 2026). Several outlets confirm the second; the source cited is a minor one (RuntimeWire).

## Checked and confirmed
- Arithmetic: 6ND for Llama 3.1 405B = 3.79×10²⁵. DeepSeek-V3 = 3.29×10²⁴, which is less than a tenth of Llama's, from 1.66× the parameters. 26.4 M GPU-hours ≈ 67 days on 16,384 GPUs. The GPT-4.5 geometric mean is 3.8×10²⁶.
- Exponent results: 2^−0.076 ≈ 0.95; 10^−0.05 ≈ 0.89; 100^0.73 ≈ 29; 100^0.27 ≈ 3.5; 8^0.74 ≈ 4.7.
- Chinchilla losses: 1.99 and 1.94, and with Besiroglu's refit 2.00 and 1.97 at a 2.6× ratio.
- Table 4.2: all ratios and 6ND values. Llama 3 8B → 77B on 1.5T. Meta's 402B/16.55T pair = 4.0×10²⁵ and 41 tokens per parameter; the 20:1 rule gives 563B on 11.3T.
- Other ratios: 4,560/26 ≈ 175; p^10 = 0.1/11/35/90%; 9.4/3.8 ≈ 2.5; 2^(365/129) ≈ 7.1; 15.6/320 ≈ 1/20; 36/320 ≈ 1/9; 20/0.07 ≈ 280; AlexNet → Llama ≈ 8×10⁷.
- Epoch CSV: AlexNet 4.7e17; GPT-3 3.14e23; Gopher 6.31e23 ($0.64 M); Chinchilla 5.76e23; GPT-4 2.1e25 Likely ($37 M); Llama 3.1-405B 3.8e25 Confident ($53 M); DeepSeek-V3 3.3e24; Grok 3 3.5e26 Likely ($218 M); GPT-4.5 3.8e26 Likely ($366 M; 187 M H100-hours at 20–40% FP8); Grok 4 5e26 Speculative ($388 M); GPT-6 Astra 9.4e26 Likely, the largest in the database (≥100,000 GB200s, 90 days, 25% FP8, CI ~5e26–2e27).
- Epoch trends page (updated 5 Nov 2026): 5×/yr (4–6), 5.2-month doubling, 10,000-fold for the top 5, chips 2.5×/yr vs 6× in 2023, cost 3.5×/yr, price-performance +49%/yr, ECI 14 vs 6 points/yr, 30% of compute on inference. AI Index 2026: 3.3×/yr and 17.1 M H100-equivalents.
- METR YAML: Opus 4.6 p50 718.8 min (CI 317–3,634 min = 5.3–60.6 h), p80 69.9 min; Mythos Preview early 1,044.8 min ≈ 17 h; doubling 128.7 days (since 2023) and 187.8 days; GPT-2 ≈ 3.2 s; Claude 3.7 Sonnet ≈ 60 min; page "no longer actively updated"; the March 2026 regularisation correction. The Decoder: "at least 16 hours … 8.5 to 55 hours".
- ClockBench (live): Fable 5.2 Max 87.8%, Argon High 83.3%, human 90.7%, no GPT-6.2 listed. Scale HLE: GPT-6 Astra 54.80%, updated 17 Sep 2026. Arena renamed 28 Jan 2026.
- Quotes: AlexNet "five to six days" (p. 7). GPT-4 report: "at most 10,000x less compute", "high accuracy", "may occasionally worsen with scale", "no further details…". Chinchilla: ">400 models", "70 million to over 16 billion", "5 to 500 billion tokens", "greater than a 7% improvement", "over 4.2 trillion tokens", the 10²⁶ remark, "for every doubling…". Ho et al. "halved approximately every 8 months" with the 90% CI of 2–22 months, as in the NeurIPS version (the arXiv preprint has a 95% CI of 5–14), 7.2× for the transformer. GSM1k 1,205 problems, "up to 8%", r² = 0.36. GPQA Diamond 198 questions, validators 81.2%, experts 65%. ARC Prize o3 75.7%/$26 and 87.5%/$4,560, 172×, repricings of 24 Mar 2025 and 10 Dec 2025, trained on 75% of the public training set. o1 12/74/93%. Sutskever "the data is very clearly finite".
- Sections 4.3–4.5: Sardana, Kumar (465 runs, 1.7B, 7–8 bits), Villalobos (130/510/3,100/100/320 T; 2028, range 2026–32), Muennighoff, Shumailov, Gerstgrasser, Sevilla (123 systems; 2×10²⁹ "likely feasible by the end of this decade"). All consistent with the sources.
- Consistency with Chapter 3: GPT-6 Astra date, Critical cyber rating and Epoch estimate; DeepSeek-V3 compute; R1 and o1 AIME figures; the V3.2 post-training share above 10%; the Grok 4 "at pretraining scale" claim. All the same in both chapters.

## Tally
Claims checked: ~130 / confirmed: ~126 / wrong: 0 / outdated: 0 / not verified: 4
