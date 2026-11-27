# Chapter 3: How Large Language Models Work — ninth review

## Verdict
Ready to print after one small fix. This is a careful chapter. Every worked example and computed table I could re-run came out exactly as printed: Tables 3.1–3.8, the attention example, the parameter count, the KV-cache sizes, the temperature ratios and the GRPO arithmetic. I re-ran the tokeniser outputs with tiktoken 0.14.0, the BPE merges with Sennrich's Algorithm 1, and the next-token probabilities for GPT-2 small and Qwen2.5-1.5B with transformers 5.24.1. Quotations I sampled are verbatim. The 2026 material checks out against the primary pages: Gemini 4 Argon and Carbon, GPT-6 Astra, Sol and Luna, GPT-6.2, Claude Fable 5, Mythos 5 and Opus 5.5, Muse Spark Open, Kimi K3, Qwen3.8, DeepSeek-V4, Grok 4.7, the Sora shutdown, the OpenAI–Hugging Face incident report and DevDay 2026.

**Balance between companies.** The chapter is even-handed in both directions. Anthropic's interpretability work is labelled "a company's studies of its own system" (l. 404). The faithfulness result that shows Claude 3.7 Sonnet doing worse than DeepSeek-R1 is reported plainly (l. 391). Anthropic's reward-hacking study sits next to OpenAI's Hugging Face incident (l. 387), and both are described neutrally and accurately. OpenAI, Google, Meta, DeepSeek, Alibaba, Moonshot and xAI/SpaceXAI all receive comparable, sourced treatment in Table 3.9 and §3.8. Mata v. Avianca is a matter of public record and is quoted accurately. I found no tone problem.

## MUST change before printing
None.

## SHOULD change

### S1. The xAI successor is now SpaceXSI
- Where: textbook/chapters/ch03.md:389 and :459
- Text now: "the same developer, renamed SpaceXAI in July 2026 after its merger with SpaceX, said of Grok 4.7" … "SpaceXAI said that Grok 4.7's training emphasised tasks that take many hours"
- Problem: OUTDATED / INCONSISTENT. On 4 October 2026 Musk said SpaceXAI would become SpaceXSI ("super intelligence"). By mid-October the X handle had changed, and x.ai/news/grok-4-7 now carries the footer "© 2026 SpaceX Super Intelligence LLC". Chapter 9 (ch09.md:246) already records the second rename, so Chapter 3 is behind Chapter 9. "SpaceXAI" is correct for the September 2026 release in Table 3.9, so the table can stay as it is.
- Evidence: Khaleej Times / Cybernews, early October 2026, "Musk renames SpaceXAI to SpaceXSI" (https://www.khaleejtimes.com/world/americas/musk-renames-spacexai-to-spacexsi-trumps-super-intelligence); x.ai/news/grok-4-7 footer, read 27 Nov 2026.
- Change to (l. 389): "the same developer, renamed SpaceXAI in July 2026 after its merger with SpaceX (and SpaceXSI from October), said of Grok 4.7"; l. 459 can stay as it is.

## Could not verify
- l. 389 Meta's Muse Spark quote "leverages compute to scalably amplify model capabilities" (I did not fetch the page).
- l. 400 Michael et al. survey: "327 active researchers", "51% agreed". The arXiv abstract only says the community is "split almost exactly in half".
- l. 440 the Claude Opus 5 date (July 2026). Not fetched; the Opus 5.5 date (22 Sep 2026) is confirmed.
- l. 321 Epoch's "about a hundredth" post-training share. The Epoch article supports the general point; I did not find the exact wording.

## Checked and confirmed
- Table 3.1: token IDs and splits; o200k_base is assigned to gpt-4o, o3, gpt-4.1 and gpt-5 in tiktoken 0.14.0.
- Table 3.2: all ten BPE merges and their counts.
- Table 3.3: tiktoken values 50,257 / 100,277 / 200,019.
- Table 3.4: all eight counts. Also confirmed: the parrot emoji (4 bytes, 3 tokens in both tokenisers), " strawberry", the " 12345678" split, and " cat" = 9059.
- Table 3.5: weights 0.620/0.074/0.306, output (0.773, 0.227), sum 27.29.
- Table 3.6: total 124,439,808, matching the library count. The 12·L·d² estimate is within 0.14%.
- Table 3.7: GPT-2 small and Qwen2.5-1.5B columns, re-run exactly. I did not re-run XL.
- Table 3.8: 74 KB / 75 MB, 0.52 MB / 66 GB, 1.06 TB, 70 KB / 9.0 GB, and "less than a seventh" (0.136).
- Arithmetic: e^0.43 ≈ 1.54, e^0.86 ≈ 2.36, −ln 0.273 = 1.30, −ln 0.032 = 3.44, t/(1−t) = 3, GRPO std 0.5/0.58, 147k/2.79M ≈ 5%, 128,000² ≈ 1.6×10¹⁰, GPT-6 Astra ≈ 3,000 × GPT-3.
- Quotations (Vaswani ×5, GPT-2, tiktoken README, Elhage, Olsson, Jain & Wallace, Mixtral, Holtzman, Rafailov, Ouyang "100x", LIMA, Tülu 3 RLVR, Bender & Koller, o1 system card, R1 "aha moment"): all verbatim. The Yue et al. "rarely elicit[s]" wording matches arXiv v5 (v1 has "does not … elicit").
- Llama 3 figures: 126 layers, 16,384 width, 53,248 FFN, 128 heads with 8 KV heads, RoPE base 500,000, 15.6T tokens, 50/25/17/8 data mix, compression 3.17 → 3.94.
- DeepSeek-V2/V3/R1/V3.2/V4 figures (93.3%, 5.76×, 37B/671B, 8 of 256 experts + 1 shared, 85–90% MTP acceptance, 1.8×, 77.9%/71.0%/79.8%, >10%, top-2048 indexer, 1.6T/49B, >32T tokens, 27% and 10%).
- Kwon et al. (20.4–38.2%, 2–4×), Gemma 3 (60% → <15%), gpt-oss (128-token window, 4.25 bits), Qwen3-Next (3:1, >10×), Qwen3.5 (15 of 60 layers), RaR "up to 31%" on HealthBench.
- 2026 items: Gemini 4 Argon API (1,048,576 tokens shared, text-only output, low/medium/high thinking, PDF input); Carbon of 28 Oct "run for days", cyber defenders first; Muse Spark Open (816B/42B, 8 of 256 experts, 1.8B encoder, text output, 15 Oct); Kimi K3 2.8T/104B; Qwen3.8 2.4T/95B; Grok 4.7 quote (21 Sep); Fable 5/Mythos 5 (9 Jun; "work autonomously for longer…"; distillation fallback); Opus 5.5 (no thinking-off mode; anti-distillation safeguard, accounts from 31 Aug 2026); Sora app closed 26 Apr and API 24 Sep 2026; OpenAI HF report ("copied the reference answer … positive RL reward"); DevDay "1.2B weekly users"; GPT-6 Astra "Critical" cyber; Fable 5.2 9 Nov, Qwen4-Max 16 Nov, GPT-6.2 17 Nov; Epoch 9.4×10²⁶ for Astra.
- Cross-references checked: §2.1, 2.3, 2.5, 3.x, 4.6, 5.3, 7.1, 9.1, 11, 12.2/12.4/12.5 all exist and match.

## Tally
Claims checked: ~140 / confirmed: ~135 / wrong: 0 / outdated: 1 (S1) / not verified: 4
