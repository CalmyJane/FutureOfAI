# Review 8: Chapter 3, How Large Language Models Work

## Verdict
Ready to print. Every worked example I recomputed is correct. I checked the quotations I could reach, and they are word for word. The 2025–26 claims I checked against company pages and press coverage all hold. I found no MUST items. One SHOULD item makes the corporate description of SpaceXAI accurate and consistent with Chapter 9.

Balance between companies is good. OpenAI, Google, Meta, DeepSeek, Alibaba, Moonshot and SpaceXAI/xAI are all described in the developers' own words and labelled as company claims where they are. The chapter does not favour Anthropic. Its unreviewed interpretability studies are flagged as "a company's studies of its own system". The faithfulness result that puts Claude 3.7 Sonnet below DeepSeek-R1 (25% vs 39%) is reported plainly. The Anthropic rows in Table 3.9 are no more numerous than OpenAI's. The OpenAI July 2026 incident is described neutrally and in line with OpenAI's own technical report.

## MUST change before printing
None.

## SHOULD change

### S1. SpaceXAI described as a "SpaceX subsidiary"
- Where: textbook/chapters/ch03.md:389
- Text now: "and the same developer, by then the SpaceX subsidiary SpaceXAI, said of Grok 4.7"
- Problem: INCONSISTENT / UNCLEAR. SpaceX acquired xAI in February 2026, and in July 2026 xAI was renamed SpaceXAI. Musk said xAI "will be dissolved as a separate company, so it will just be SpaceXAI, the AI products from SpaceX". So "subsidiary" is at best imprecise. Chapter 9 (line 246) describes the same thing differently: "renamed from xAI to SpaceXAI in July 2026 after its merger with SpaceX".
- Evidence: Engadget, "xAI is now officially known as SpaceXAI" (https://www.engadget.com/2209300/xai-now-officially-spacexai/), July 2026; Dataconomy, 7 July 2026, "Elon Musk rebrands merged xAI and SpaceX as SpaceXAI" (https://dataconomy.com/2026/07/07/elon-musk-rebrands-merged-xai-and-spacex-as-spacexai/).
- Change to: "and the same developer, renamed SpaceXAI in July 2026 after its merger with SpaceX, said of Grok 4.7"

## Could not verify
- Table 3.7, Section 3.4 and the "Going deeper" box give GPT-2 / GPT-2 XL / Qwen2.5-1.5B next-token probabilities, logits and nucleus sizes. I did not re-run these: it needs model downloads of several GB. They are internally consistent. 7.5%/4.9% gives a ratio of 1.53 ≈ e^0.43. At T = 0.5, 51.7%/21.9% = 2.36 ≈ e^0.86. −ln 0.273 = 1.30 and −ln 0.032 = 3.44.
- Kimi K3's "104 billion active" parameters (line 451, Table 3.9) matches the model card as summarised by NYU Shanghai RITS. TheNextWeb and DeepLearning.AI instead report about 50 billion active. The book follows the primary source, which is acceptable.
- DeepSeek-V4's "27% of the per-token computation and 10% of the KV cache of DeepSeek-V3.2" (line 253) is consistent with press summaries of the release. I did not reach the preprint itself.
- Gemini 4 Carbon "has run for days on internal multi-step engineering tasks" (line 459): not checked.

## Checked and confirmed
- Table 3.1 (all 8 IDs), Table 3.3 (`gpt2` 50,257, `cl100k_base` 100,277, `o200k_base` 200,019), Table 3.4 (7/7, 9/15, 12/62, 13/20), strawberry, the 12345678 digit split, " cat" = 9059, and the parrot emoji (4 bytes → 3 tokens in both tokenisers). All re-run with tiktoken 0.14.0. tiktoken maps gpt-4o, o3, gpt-4.1 and gpt-5 to `o200k_base`.
- Table 3.2: I re-ran Sennrich's Algorithm 1 and got the same 10 merges with the same counts.
- Table 3.5: weights 0.620/0.074/0.306, sum 27.29, output (0.773, 0.227). Correct.
- Table 3.6: 7,087,872 per block, 85,054,464 for the blocks, 124,439,808 in total. Kaplan's 12·L·d² is within 0.14%. 2N ≈ 170M.
- Table 3.8: 74 KB / 75 MB; 819,200 B; 0.52 MB / 66 GB; 8.3 MB / 1.06 TB; 70 KB / 9.0 GB; ratio 7.3 ("less than a seventh"). 128,000² = 1.6 × 10^10.
- σ(1) ≈ 73%; the Kalai threshold 0.75/0.25 = 3; the GRPO example (σ = 0.5 or 0.58); 147,000 / 2.79M ≈ 5%; GPT-6 Astra about 3,000× GPT-3.
- Quotations checked: Vaswani ("dispensing with recurrence and convolutions entirely", "extremely small gradients", "more parallelizable", "apparently involved in anaphora resolution", multi-head quote); GPT-3 "without any gradient updates or fine-tuning"; tiktoken README; Jain & Wallace; Elhage residual stream; Olsson "preliminary and indirect evidence"; RoFormer; Mixtral 47B/13B; Holtzman; Ainslie "a severe bottleneck"; Llama 3 GQA rationale; Kimi K2 Thinking "lossless 2x speed-up"; OpenAI image addendum; Sora 2 physics; o1 system card; Tülu 3 RLVR; R1-Zero "aha moment"; Yue et al. "rarely elicit[s]" (wording of the current arXiv HTML version; the abstract says "does not elicit"); Gunjal "up to 31%"; Mata v. Avianca quotations and the $5,000 sanction.
- Sennrich 59,500/89,500 merges; Llama 3 tokenizer (100K + 28K; 3.17 → 3.94); Petrov "up to 15 times"; word2vec 1.6B words; Llama 3 405B architecture (126 layers, 128/8 heads, 16,384 width, FFN 53,248, RoPE base 500,000, 15.6T tokens, data mix 50/25/17/8); DeepSeek-V2 93.3% / 5.76×; DeepSeek-V3 MTP 85–90% / 1.8×; Gemma 3 5:1 and 60% → <15%; gpt-oss MXFP4 4.25 bits and 128-token window; vLLM 20.4–38.2%, 2–4×, 1.6 GB; Mercury 737–1,109 tok/s; Gemini 1.5 >99% at 10M; Qwen3-Next 10×; Qwen3.5 15 of 60 attention layers; GPT-4o 320 ms; DPR 78.4% vs 59.1%; Magesh 17–33%; Chen et al. 25%/39%; Michael et al. 327 respondents, 51/49; InstructGPT ~40 labellers and ~33k prompts; Epoch "100×" pre- vs post-training and "about 20%" for R1 RL, o3 = 10× o1.
- 2026 items: DeepSeek-V4 (24 April 2026, preview, 1.6T/49B, >32T tokens, 1M context, MIT); Kimi K3 (July 2026, 2.8T); Qwen3.8-2.4T-A95B (August 2026); GPT-6 Astra (3 Sep 2026, Critical cyber); GPT-6 Sol/Luna (22 Sep); Gemini 4 Argon (30 Sep, 1M shared input/output limit, output up from 64K, low/medium/high thinking levels, cyber defenders first); Grok 4.7 (21 Sep, "longer reinforcement learning run", hours-long tasks); Muse Spark Open (15 Oct, 816B/42B); ChatGPT 1.2B weekly users (DevDay 2026); Sora app closed 26 April 2026 and API 24 Sep 2026 (OpenAI help centre); OpenAI–Hugging Face incident report (reward hacking among root causes); Claude Fable 5 / Mythos 5 (9 June 2026: "same underlying model … safeguards lifted"; Mythos tier "above our Opus class"; "work autonomously for longer than any previous Claude models"; distillation-flagged requests "fall back to Opus 4.8"); Opus 5.5 (22 Sep; no longer available with thinking off; preserved thinking from Fable 5.1; accounts created on or after 31 Aug 2026); Fable 5.2 / Mythos 5.2 (9 Nov), Qwen4-Max closed (16 Nov), GPT-6.2 Astra/Sol (17 Nov).
- Cross-references checked: Sections 2.1, 2.3, 2.5, 3.2, 3.4–3.7, 4.6, 5.3, 7.1, 9.1, 12.2, 12.4 and 12.5 all exist and contain the material referred to.

## Tally
Claims checked: about 140. Confirmed: about 135. Wrong: 0. Outdated: 0. Imprecise or inconsistent: 1 (S1). Not verified: 4 (listed above).
