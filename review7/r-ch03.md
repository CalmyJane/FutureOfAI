# Review 7: Chapter 3, How Large Language Models Work

## Verdict
Ready to print. Nothing in the chapter is wrong, misquoted or legally risky enough to block printing. The worked examples all recompute exactly: the BPE merges, the attention table, the GPT-2 parameter count, the KV-cache table, the temperature ratios, the losses and the GRPO example. Every quotation I checked against its source matches. The 2025–26 material I spot-checked is accurate: Sora's discontinuation dates, Kimi K3, Muse Spark Open, DeepSeek-V4, the 1.2 billion ChatGPT users, the SpaceXSI renaming, Grok 4.7, GPT-6.2, Qwen4-Max and the OpenAI–Hugging Face incident. The remaining items are about structure and wording.

## MUST change before printing
None.

## SHOULD change

### S1. Multimodality sits under "Generating text"
- Where: textbook/chapters/ch03.md:257 (### Beyond text: images, sound and video, inside ## 3.4 Generating text)
- Text now: "### Beyond text: images, sound and video"
- Problem: UNCLEAR. Section 3.4 already covers decoding, the KV cache, context windows and four kinds of cheaper attention. It then switches to how images and audio get into a model, which is mostly about input and has nothing to do with generating text. Other passages send readers to "Section 3.4" for multimodality (lines 92 and 455), and readers will look for it under a heading about generation.
- Evidence: internal structure. The cross-references at lines 92 and 455 both point to Section 3.4.
- Change to: either rename Section 3.4 "Generating text, long contexts and other modalities", or move the "Beyond text" subsection to the end of Section 3.2 (Embeddings), where image patches and CLIP are already introduced, and update the two cross-references.

### S2. Corporate-renaming aside interrupts a technical paragraph
- Where: textbook/chapters/ch03.md:389
- Text now: "(On 4 October 2026 Elon Musk said SpaceXAI would be renamed SpaceXSI [@frank2026why].)"
- Problem: UNCLEAR. The fact is correct (Musk said it in an X reply on 4 October 2026; Jalopnik, Fox Business and Not a Tesla App all reported it). It has nothing to do with reinforcement-learning compute, though, and it breaks up the paragraph's argument. Chapter 9 (line 246) already records the renaming.
- Evidence: https://www.notateslaapp.com/news/4770/musk-spacexai-will-be-renamed-spacexsi-dropping-ai ("SpaceXAI will be renamed SpaceXSI", October 2026)
- Change to: delete the parenthetical sentence, or move it to a footnote.

### S3. "Table 3.9" milestone for DeepSeek-V4 could note it was a preview
- Where: textbook/chapters/ch03.md:439
- Text now: "| DeepSeek-V4 | DeepSeek | Apr 2026 | 1.6-trillion-parameter MoE; compressed sparse attention; 1-million-token context, open weights |"
- Problem: OUTDATED (minor). The April 2026 release was DeepSeek-V4 *Preview*, and the 1.6T/49B figures are correct for it. SemiAnalysis's InferenceX lists a later general-availability checkpoint, V4-Pro-0813, with 1.7T parameters. I could not confirm that on DeepSeek's own page.
- Evidence: https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro (1.6T total, 49B activated); https://inferencex.semianalysis.com/model/deepseek-v4 ("1.7T params for DeepSeek-V4-Pro-0813")
- Change to: "1.6-trillion-parameter MoE (April preview); ..." Optionally, verify the August checkpoint first.

## Could not verify
- The tiktoken token IDs in Tables 3.1 and 3.4 and line 84 (" cat" = 9059), and the "strawberry" and number-chunking examples. I could not install tiktoken in this environment, so they rest on the author's stated runs. The vocabulary sizes in Table 3.3 match my independent knowledge (50,257; 100,277; 128,256; 151,665; 200,019).
- The GPT-2 and Qwen2.5 next-token probabilities in Table 3.7 and the nucleus sizes in the box. Reproducing them needs the models.
- Muse Spark Open "routes each token to 8 of 256 experts" (line 451) and the "1.8-billion-parameter perception encoder" (line 261). The 816B/42B figures and the perception encoder itself are confirmed by Meta's release coverage (Unite.AI, The New Stack, 15 Oct 2026).
- Gemini 4 Argon's thinking levels and output-only-text API (lines 259, 269, 457). Claude anti-distillation safeguard details (line 461).
- Michael et al. 2023: the 327 analysed respondents (line 400). The 51/49 split is consistent with the paper as I remember it.

## Checked and confirmed
- Table 3.2: I reran Sennrich et al.'s Algorithm 1 and got exactly the ten merges and counts shown.
- Table 3.5: the scores 2.83/0.71/2.12, sum 27.29, weights 0.620/0.074/0.306 and output (0.773, 0.227) are exact.
- Table 3.6: every row and the total of 124,439,808. Kaplan's 12·L·d² = 84,934,656 is within 0.14% of the blocks' total. The embedding share is 31.6% and the FFN share 66.6%.
- Table 3.8: 74 KB / 75 MB; 819,200 B / 1.6 GB; 0.52 MB / 66 GB; 8.3 MB / 1.06 TB; 70 KB / 9.0 GB. The "less than a seventh" comparison and the "16 times" factor hold.
- e^0.43 ≈ 1.54 and e^0.86 ≈ 2.36, consistent with 7.5/4.9 and 51.7/21.9. −ln 0.273 = 1.30, −ln 0.032 = 3.44, σ(1) = 0.73. GRPO sd 0.5/0.58. t/(1−t) = 3. 128,000² ≈ 1.6 × 10^10. 147k/2.79M ≈ 5%.
- Quotations: Brown ("without any gradient updates or fine-tuning"), Vaswani (four quotes plus the Figure 4 caption), GPT-2 "any Unicode string", the tiktoken README, Mixtral "47B…13B", Elhage residual stream, Olsson "preliminary and indirect evidence", Jain & Wallace, Holtzman, Ouyang "100x fewer parameters", Rafailov, LIMA, Lambert RLVR, the o1 system card, the R1-Zero "aha moment", Yue "rarely elicit[s]" (arXiv HTML abstract: "current training *rarely* elicit fundamentally new reasoning patterns"), Bender & Koller, the GPT-4 report non-disclosure, and Mata v. Avianca ("submitted non-existent judicial opinions…", $5,000).
- Sora: app and web discontinued 26 April 2026, API 24 September 2026 (help.openai.com/en/articles/20001152).
- ChatGPT had 1.2 billion weekly users at DevDay on 29 Sep 2026 (openai.com/index/devday-2026-recap).
- Kimi K3: 2.8T total, 104B active, KDA plus MLA layers, July 2026 (github.com/MoonshotAI/Kimi-K3).
- DeepSeek-V4-Pro: 1.6T/49B. At 1M tokens it needs "27% of single-token inference FLOPs and 10% of KV cache" compared with V3.2 (Hugging Face model card).
- Grok 4.7: released 21 Sep 2026 with a longer RL run on multi-hour tasks (SiliconANGLE, 21 Sep 2026).
- GPT-6.2 Astra and Sol on 17 Nov 2026; Qwen4-Max, closed weights, 16 Nov 2026 (TechNode, 16 Nov 2026).
- OpenAI–Hugging Face incident: training had rewarded cheating, per the 26 Aug 2026 technical report as described by MIT Technology Review.
- Architecture figures: Llama 3 405B (126 layers, 128 heads, 8 KV heads, 16,384/53,248, RoPE 500,000); DeepSeek-V3 (8 of 256 experts plus 1 shared, 37B/671B, MTP 85–90%, 1.8×); DeepSeek-V2 (93.3%, 5.76×); Qwen3.5-397B (15 of 60 full-attention layers); gpt-oss (MXFP4 4.25 bits, window 128).
- Other results: Kwon (20.4–38.2%, 2–4×), Karpukhin (78.4/59.1), Magesh (17–33%), Chen et al. (25%/39%), Lightman (800k steps, 78%), Gunjal ("up to 31% on HealthBench", arXiv:2507.17746).
- Cross-references: Sections 2.1, 2.3, 2.5, 3.2–3.7, 5.3, 7.1, 9.1, 12.2, 12.4 and 12.5, and Chapters 11 and 12. All targets exist and cover the topic named.

## Tally
Claims checked: about 120. Confirmed: about 112. Wrong: 0. Outdated: 1 (minor, S3). Could not verify: about 8.
