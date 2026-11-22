# Third review: Chapter 3 — How Large Language Models Work

(First read and part of the checking by an earlier reviewer, first version saved 11 Nov 2026; continued and finished 22 Nov 2026. Every provisional item has now been checked against its source, and the working notes have been folded into the sections below.)

## Verdict
Ready after the MUST fixes below. The technical core holds up very well. Every worked number in the chapter was recomputed and matches: the attention example, the GPT-2 parameter count, the KV-cache table, the temperature, loss and GRPO arithmetic, and all of Table 3.7, the nucleus box and the Figure 3.2 bars, which I re-ran on GPT-2 small, GPT-2 XL and Qwen2.5-1.5B. The tokenisation tables were reproduced with tiktoken. Of about 170 claims checked against the web, only a handful fail. Two things must change before printing. The FlashAttention sentence contradicts the title and results of the paper it cites, and an ML reader will notice. The "largest open models of 2026" sentence leaves out the two largest open models, Kimi K3 at 2.8 trillion parameters and Qwen3.8 at 2.4 trillion. The rest are small fixes of dates, quotation wording and attribution. Section 3.8 is accurate to its stated cut-off of the end of October, but releases between 9 and 17 November (Claude Fable 5.2 and Mythos 5.2, GPT-6.2 Astra and Sol, Qwen4-Max) mean its "frontier of 2026" picture is already one generation old. A one-line note would cover this.

## MUST change before printing

### M1. "The largest open models of 2026" omits the two largest (Kimi K3, 2.8 trillion; Qwen3.8, 2.4 trillion)
- Where: textbook/chapters/ch03.md:448. Table 3.9 (lines 415–446) also has no row for either model.
- Text now: "The largest open models of 2026 are mixtures of experts with around a trillion parameters or more, of which a few per cent are used for each token. DeepSeek-V4-Pro has 1.6 trillion parameters, 49 billion of them active, and was pre-trained on more than 32 trillion tokens [@deepseekai2026deepseekv4]; Kimi K2 has 1.04 trillion with 32 billion active [@kimiteam2025kimi]; Muse Spark Open has 816 billion and routes each token to 8 of 256 experts [@meta2026musesparkopen]."
- Problem: OUTDATED and misleading. Both models below were released before the book's cut-off at the end of October, and both have more parameters than any model the sentence names. Moonshot's Kimi K3 was launched on 16 July 2026, with weights released on 27 July. Alibaba's Qwen3.8-2.4T-A95B followed in August 2026. Kimi K2 is a 2025 model. A reader will take the sentence to mean that DeepSeek-V4-Pro is the largest open model of 2026. Qwen4-Max (16 November 2026, also 2.4 trillion parameters) has no open weights, so it does not change the fix.
- Evidence:
  - https://huggingface.co/moonshotai/Kimi-K3 (model card): "a 2.8T-parameter model"; Total Parameters "2.8T"; Activated Parameters "104B"; "activates 16 out of 896 experts"; Context Length "1048576"; "69 KDA + 24 Gated MLA".
  - https://thenextweb.com/news/moonshot-kimi-k3-largest-open-model: "a 2.8-trillion-parameter system"; "DeepSeek's V4-Pro tops out at 1.6 trillion".
  - Epoch AI Notable Models data (https://epoch.ai/data/notable_ai_models.csv): Kimi K3, 2026-07-16, 2.8e12 parameters.
  - https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B (model card): "Number of Parameters: 2.4T in total and 95B activated"; "Number of Experts: 512"; "10 Routed + 1 Shared"; "Context Length: 262,144 natively and extensible up to 1,010,000 tokens". The Hugging Face repository was created on 8 August 2026, and the Epoch AI data gives 2026-08-08.
- Change to: "The largest open models of 2025–26 are mixtures of experts with around a trillion parameters or more, of which a few per cent are used for each token. The largest, Moonshot's Kimi K3 (July 2026), has 2.8 trillion parameters, 104 billion of them active, and Alibaba's Qwen3.8-2.4T-A95B (August 2026) has 2.4 trillion with 95 billion active [@moonshot2026kimik3; @qwen2026qwen38]. DeepSeek-V4-Pro has 1.6 trillion parameters, 49 billion of them active, and was pre-trained on more than 32 trillion tokens [@deepseekai2026deepseekv4]; Kimi K2 (2025) has 1.04 trillion with 32 billion active [@kimiteam2025kimi]; Muse Spark Open has 816 billion and routes each token to 8 of 256 experts [@meta2026musesparkopen]."
  - Add bib entry `moonshot2026kimik3`: {Moonshot AI}, "Kimi K3 Model Card", Hugging Face model repository, July 2026 (company source), https://huggingface.co/moonshotai/Kimi-K3.
  - Add bib entry `qwen2026qwen38`: {Qwen Team}, "Qwen3.8-2.4T-A95B Model Card", Hugging Face model repository, August 2026 (company source), https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B.
  - Recommended Table 3.9 row, after "Grok 4.7" or in date order after the "Claude Fable 5 ..." row: "Kimi K3 | Moonshot AI | Jul 2026 | 2.8-trillion-parameter open MoE (104 billion active); linear-attention (KDA) and latent-attention layers; 1-million-token context | [@moonshot2026kimik3]".

### M2. FlashAttention "saves time but not memory" contradicts the cited paper
- Where: textbook/chapters/ch03.md:243
- Text now: "FlashAttention computes exact attention in tiles that fit in a processor's fast on-chip memory, avoiding repeated trips to slower main memory [@dao2022flashattention]. That saves time but not memory; the next subsection describes four further remedies used by models of 2024–26."
- Problem: VERIFIED WRONG / UNSUPPORTED BY CITED SOURCE. The cited paper is titled "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness". FlashAttention never stores the n-by-n score matrix, so the extra memory it needs grows linearly, not quadratically, with sequence length. What it does not reduce is the KV cache and the quadratic amount of arithmetic, which is what the following subsection addresses. As written, the sentence would embarrass the author in front of any ML reader.
- Evidence: Dao et al. 2022, arXiv:2205.14135, Sec. 4.3: "FlashAttention and block-sparse FlashAttention have the same memory footprint, which grows linearly with sequence length. FlashAttention is up to 20× more memory efficient than exact attention baselines". Sec. 3.2: "This leads to both faster execution and lower memory footprint". Appendix B: "requiring extra memory linear instead of quadratic in the sequence length".
- Change to: "FlashAttention computes exact attention in tiles that fit in a processor's fast on-chip memory, avoiding repeated trips to slower main memory and never storing the full table of scores, so it saves both time and working memory [@dao2022flashattention]. It does not, however, reduce the quadratic amount of arithmetic or the size of the KV cache; the next subsection describes four further remedies used by models of 2024–26."

## SHOULD change (real but not blocking)

### S1. Llama 3 dated "Jul 2024" in Table 3.9, but the caption says "first release"
- Where: textbook/chapters/ch03.md:420 (row "LLaMA; Llama 3"), with the caption at line 446: "Dates are first release or announcement."
- Problem: INTERNAL CONTRADICTION. Llama 3 was first released on 18 April 2024 (8B and 70B). The 405-billion-parameter model with a 128,000-token context described in the row was released on 23 July 2024 as Llama 3.1. Evidence: Epoch AI Notable Models data gives "Llama 3-70B | 2024-04-18" and "Llama 3.1-405B | 2024-07-23".
- Change to: date cell "Feb 2023; Apr 2024 (405B: Jul 2024)". Alternatively, rename the model cell "LLaMA; Llama 3 (3.1)" and keep "Feb 2023; Jul 2024".

### S2. "More than 1.2 billion weekly users": neither OpenAI nor the cited report says "more than"
- Where: textbook/chapters/ch03.md:411
- Text now: "By late September 2026, according to a slide shown at OpenAI's developer conference, it had more than 1.2 billion weekly users [@bonifacic2026openai]."
- Problem: UNSUPPORTED overstatement. The Engadget live blog (29 Sept 2026) reports: "A graphic behind Altman indicates ChatGPT now has 1.2 billion weekly users" and "Altman is reiterating the stat that 1.2 billion people now use ChatGPT every week." OpenAI's own DevDay 2026 recap, also dated 29 September 2026 (https://openai.com/index/devday-2026-recap/), says "our collective 1.2B weekly users". Both say 1.2 billion; neither says "more than". I found no newer official figure up to 22 November 2026.
- Change to: "By late September 2026, OpenAI said at its developer conference, it had 1.2 billion weekly users [@openai2026devday]." Add bib entry `openai2026devday`: {OpenAI}, "DevDay 2026 Recap", company blog, 29 September 2026, https://openai.com/index/devday-2026-recap/. Alternatively, keep @bonifacic2026openai and delete "more than".

### S3. Mythos Preview "New tier above Opus" is not in the cited source
- Where: textbook/chapters/ch03.md:437 (Table 3.9 row "Claude Mythos Preview | ... | New tier above Opus; withheld from general release over its cyber capabilities | [@anthropic2026claude]")
- Problem: UNSUPPORTED BY CITED SOURCE, though true elsewhere. The cited post of 7 April 2026 (https://www.anthropic.com/research/mythos-preview) calls Mythos Preview "a new general-purpose language model", compares it with Opus 4.6, and says "we do not plan to make Mythos Preview generally available" because it "is strikingly capable at computer security tasks". It never describes a tier above Opus. The tier structure is stated in the Fable 5 / Mythos 5 announcement, which the chapter already cites at line 458.
- Change to: source cell "[@anthropic2026claude; @anthropic2026fable]".

### S4. The Yue et al. quotation changes a word
- Where: textbook/chapters/ch03.md:363
- Text now: "current training of this kind "rarely elicits fundamentally new reasoning patterns""
- Problem: the quotation is not exact. In the arXiv v5 (NeurIPS 2025) version the source reads "current training rarely elicit fundamentally new reasoning patterns" (sic). Versions 1 and 2 read "does not elicit".
- Change to: "current training of this kind "rarely elicit[s] fundamentally new reasoning patterns"". Alternatively, drop the quotation marks: "current training of this kind rarely elicits fundamentally new reasoning patterns".

### S5. Epoch AI's "hundredfold" is about compute, not data
- Where: textbook/chapters/ch03.md:321
- Text now: "Post-training of this kind has traditionally used far less data and computation than pre-training, by about a hundredfold according to an analysis by Epoch AI researchers [@edelman2025why]."
- Problem: the source supports the hundredfold figure for compute only. Its words are: "Until recently, most LLMs were trained with 100× more pre-training than post-training compute" (Edelman, Denain, Sevilla and Ho, 26 Sept 2025).
- Change to: "Post-training of this kind has traditionally used far less data than pre-training, and about a hundredth of the computation, according to an analysis by Epoch AI researchers [@edelman2025why]."

### S6. Doubled connective
- Where: textbook/chapters/ch03.md:90
- Text now: "So "bank" in "the river bank" and "bank" in "the bank raised rates" can therefore end up represented quite differently."
- Change to: "So "bank" in "the river bank" and "bank" in "the bank raised rates" can end up represented quite differently."

### S7. Section 3.8 is one release behind at printing
- Where: textbook/chapters/ch03.md:446 (Table 3.9 caption), and the "frontier of 2026" paragraphs at lines 448–464.
- Problem: OUTDATED in part, though not wrong as of the stated cut-off. After 25 October 2026:
  - Anthropic released Claude Fable 5.2 and Mythos 5.2 on 9 November. Anthropic's page: "Claude Mythos 5.2 is our most capable model for cybersecurity and life sciences research".
  - OpenAI released GPT-6.2 Astra and Sol on 17 November (openai.com/index/gpt-6-astra/, update of 17 November). Its page says that, like GPT-6 Astra, they meet the Critical cybersecurity threshold.
  - Alibaba released Qwen4-Max (closed weights; 2.4 trillion parameters in total, 71 billion active) on 16 November.
  - Moonshot released Kimi K3.1 Pro weights on 5 November (TechNode).
  - Aggregator sites report Gemini 4 Hydrogen (12–13 November), but I could not confirm this from Google.

  No sentence in the chapter is falsified by these releases. The models the text names as the frontier (GPT-6 Astra, Claude Opus 5.5, Fable 5 / Mythos 5) are, however, no longer the newest.
- Change to: caption "Table 3.9: Selected milestones from GPT-3 to the end of October 2026. ..." Optionally add after the table: "Releases continued after this book's cut-off; in November 2026 alone Anthropic, OpenAI and Alibaba each released new flagship versions."

## Could not verify
- textbook/bib/ch03.bib `lambert2024tulu`, venue "Second Conference on Language Modeling (COLM 2025)". arXiv:2411.15124 confirms the authors, the title and the RLVR quotation. The OpenReview page (id i1uGbfHHpH) blocked automated access, and a web search did not show a COLM listing. Low importance, but a human should confirm the venue or cite it as arXiv 2024.
- textbook/chapters/ch03.md:441, the GPT-6 tier description "A tiered family" (Table 3.9). The GPT-6 Astra page says only "expanding our GPT‑6 family with GPT‑6 Sol and GPT‑6 Luna" and does not describe tiers. This is the author's reasonable reading, not a quotation. No action needed.
- Gemini 4 Hydrogen and Neon (November 2026) could not be confirmed from Google sources. These models are not mentioned in the chapter and are listed only for S7.

## Reader notes
1. Line 243: the FlashAttention sentence (M2) will stop an informed reader.
2. Line 90: "So ... can therefore" (S6).
3. Lines 308–312 (DPO box): `[@rafailov2023direct]` appears three times in a two-sentence box, once in mid-formula ("DPO minimises [@rafailov2023direct]" and again after the formula). One citation is enough.
4. Line 305: "The openly documented Tülu 3 recipe, for example, runs supervised fine-tuning, then DPO, then a reinforcement-learning stage". The sentence follows the finding that tuned PPO beats DPO, so it is unclear what "for example" illustrates. Suggest: "In practice the two are combined: the openly documented Tülu 3 recipe runs ...".
5. Line 212 (box): "After "The capital of France is", where one answer dominates, ...". Table 3.7 has just said that even for Qwen "most of the probability goes to other continuations" (Paris at 27.3%), so "dominates" jars. Suggest "where one answer stands out".
6. Figure 3.2 marks a leading space with "␣" ("␣edge", "␣cat"), while the text and tables use quoted inline code (`" edge"`). The convention is never explained for the figure. A caption note would help: "␣ marks a leading space."
7. Line 456: "Developers now describe their models chiefly by how long and how reliably they work". This is a generalisation from three company quotations; "increasingly" would be safer than "chiefly".
8. Line 243: "four further remedies used by models of 2024–26". The first example under "Looking only nearby" is Mistral 7B (2023), and Mamba is also 2023. This is harmless, but "of 2023–26" would be exact.
9. Line 448 (after M1): the paragraph moves from parameter counts straight to "Training compute rose too: Epoch AI estimates GPT-6 Astra's at about 9.4 × 10^26 FLOP". The figure is right, but the reader is not told that it is an outside estimate for a closed model. "an outside estimate" would make that clear.

## Checked and confirmed
Each line is a claim (or group of claims) verified correct, with the source. Items marked [R1] were confirmed in the first round; the rest were confirmed in this round.

**Opening and 3.1 Tokens**
- [R1] Table 3.1 token IDs; Table 3.3 n_vocab 50,257 / 100,277 / 200,019; Table 3.4 counts 7/7, 9/15, 12/62, 13/20; strawberry split; " 12345678" → space, 123, 456, 78; parrot emoji 4 bytes and 3 tokens in both tokenisers; " cat" = 9059; encoding for gpt-4o, o3, gpt-4.1 and gpt-5. All reproduced with tiktoken 0.14.0.
- [R1] Table 3.2 BPE merges reproduced by running Sennrich et al.'s Algorithm 1.
- Sennrich et al.: "BPE with 59 500 merge operations, and joint BPE with 89 500" (arXiv:1508.07909).
- tiktoken README: "It works on arbitrary text, even text that is not in the tokeniser's training data" (github.com/openai/tiktoken).
- Leading-space token strings in inline code are used consistently across lines 11–22, 63, 84, 187–195, 203–215 and 279 (grep of all `"…"` code spans).

**3.2 Embeddings and attention / 3.3 Transformer block**
- Vaswani et al.: sqrt(d_k) rationale ("extremely small gradients"); 8 heads × 64; Fig. 4 shows layer 5 of 6, encoder self-attention, "apparently involved in anaphora resolution". From knowledge of the paper; quotations match.
- Elhage et al.: "a communication channel, since it doesn't do any processing itself and all layers communicate through it" (transformer-circuits.pub/2021/framework).
- Olsson et al.: "preliminary and indirect evidence" that induction heads may be the mechanism for the majority of in-context learning (arXiv:2209.11895).
- Table 3.5 recomputed with NumPy: dot products 4, 1, 3; scaled 2.83, 0.71, 2.12; sum 27.29; weights 0.620, 0.074, 0.306; output (0.773, 0.227); rows 1 and 2 also match.
- Table 3.6 recomputed: each row; block 7,087,872; total 124,439,808 (matches the HF model: 124,439,808 parameters); 12·L·d² is within 0.14% of the block total; feed-forward 66.6% of a block; embeddings 31.6% of the model; 2N ≈ 170 million operations per token.

**3.4 Generating text**
- Table 3.7 re-run (transformers 5.24, torch 2.15 CPU, fp32, no BOS):
  - GPT-2 small: the 8.46, now 4.79, a 4.62, France 3.24, Paris 3.22.
  - GPT-2 XL: the 10.12, a 9.90, Paris 8.63, in 2.49, one 2.35.
  - Qwen2.5-1.5B: Paris 27.34, located 6.35, a 4.53, " __" 4.43, " ______" 4.15.
  - All match the table.
- Temperature box re-run: GPT-2 XL logits 8.78 / 8.35; 7.54% / 4.90%; nucleus 3,068; at T = 0.5, 51.67% / 21.86% and nucleus 10; "The cat sat on the" nucleus 951 → 14; Qwen France nucleus 103 → 4; " mat" rank 50. e^0.43 = 1.54 and e^0.86 = 2.36 recomputed.
- Figure 3.2 bars (edge 7.32, floor 5.24, table 4.93, bed 4.38) re-run and matching.
- LLaDA "performs comparably to our self-constructed ARM baselines" (arXiv:2502.09992).
- Mercury Coder "1109 tokens/sec and 737 tokens/sec ... on NVIDIA H100 GPUs", from Artificial Analysis (arXiv:2506.17298).
- Table 3.8 recomputed: GPT-2 73,728 B and 75.5 MB; OPT 819,200 B and 1.68e9 B; Llama 3 0.516 MB and 66.06 GB; all-heads 8.26 MB and 1.057 TB; DeepSeek-V3 70.3 KB and 8.99 GB; 7.3 times smaller than Llama (so "less than a seventh"); GQA factor 16.
- Kimi K2 Thinking card: "interleave chain-of-thought reasoning with function calls"; "lossless 2x speed-up in low-latency mode" with INT4 QAT; "200–300 consecutive tool invocations" (huggingface.co/moonshotai/Kimi-K2-Thinking).
- FlashAttention paper read; see M2.
- Gemma 3: 5 local per global, window 1,024, KV overhead "60%" → "less than 15%" at a 32k context (arXiv:2503.19786).
- DeepSeek-V3.2: lightning indexer; "select 2048 key-value tokens for each query token" (arXiv:2512.02556).
- [R1] DeepSeek-V4 arXiv: 1.6T/49B, 284B/13B, 1M context, >32T tokens, 27% FLOPs and 10% KV vs V3.2.
- This round, the same arXiv page: submitted 26 Apr 2026; "Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA)".
- Kimi K2: 64 heads "as opposed to 128 in DeepSeek-V3" to cut long-context inference overhead; QK-Clip "rescaling the query and key projection weights" (arXiv:2507.20534).
- Qwen3-Next card: 3 Gated DeltaNet per Gated Attention; "10 times inference throughput for context over 32K tokens" vs Qwen3-32B.
- [R1] Qwen3.5-397B-A17B card: 15 × (3 Gated DeltaNet + 1 Gated Attention) = 60 layers; early fusion.
- [R1] Gemini 4 Argon docs: 1,048,576 limit; text, image, video, audio and PDF in; text out; thinking low, medium and high.
- [R1] Muse Spark Open card: 816B/42B; 8 of 256 experts; 1.8B perception encoder; modalities; 15 Oct 2026.
- Llama 4 blog (5 Apr 2025): "early fusion to seamlessly integrate text and vision tokens into a unified model backbone"; "our first models that use a mixture of experts"; "codistilled ... Maverick ... from Llama 4 Behemoth"; "interleaved attention layers without positional embeddings".
- Veo 3 blog (20 May 2025): "generate videos with audio"; "dialogue between characters".
- Sora 2 page: "better about obeying the laws of physics compared to prior systems"; speech and sound effects; "As of April 26, 2026, the Sora product is no longer available."
- Genie 3 (5 Aug 2025): "to simulate aspects of it"; 24 fps; 720p; consistent for "a few minutes".
- GPT-6 Astra page: reports OSWorld 2.0 and ScreenSpot-Pro without describing how images enter the model; MRCR v2 8-needle 512K–1M 96.3%.

**3.5 Pre-training and post-training**
- Cross-entropy values: −ln 0.273 = 1.30 and −ln 0.032 = 3.44; σ(1) = 0.731. Recomputed.
- Edelman et al. (Epoch, 26 Sept 2025): 100× compute figure (see S5); RL environments named as a possible limit on scaling; authors and date match the bib entry.

**3.6 Hallucination**
- Mata v. Avianca opinion (ECF 54):
  - p. 1: "submitted non-existent judicial opinions with fake quotes and citations created by the artificial intelligence tool ChatGPT".
  - p. 15: "I falsely assumed was like a super search engine called ChatGPT".
  - p. 19: ChatGPT said it had supplied "real" authorities.
  - pp. 33–34: "$5,000 is jointly and severally imposed".
- Kalai et al.: t/(1−t) at t = 0.75 gives 3, recomputed. The rest was checked against the paper from knowledge (singleton rate, Is-It-Valid).

**3.7 Reasoning models**
- GRPO example: mean 0.5; standard deviation 0.5 (population) or 0.577 (sample); advantages ±1 or ±0.87, so "roughly" holds. 147,000 / 2.79M = 5.3%.
- Epoch, You (9 May 2025): "about 20% of the cost of pre-training ... DeepSeek-V3"; "o3 is a 10× scale-up in training compute from o1".
- Tülu 3: RLVR "only gets a reward if the model's completions are verified to be correct" (arXiv:2411.15124).
- Yue et al.: base models win at large k; quotation wording (S4) (arXiv:2504.13837 v1, v2, v5).
- Gunjal et al.: "relative improvements of up to 31% on HealthBench" over Likert-based judge baselines (arXiv:2507.17746 v2).
- DeepSeek-V3.2:
  - "a generative reward model where each prompt has its own rubrics";
  - "over 1,800 distinct environments and 85,000 complex prompts";
  - "1,827 task-oriented environments";
  - real search and coding environments;
  - reasoning "discarded only when a new user message is introduced";
  - RL budget "exceeds 10% of the pre-training cost".
- Kimi K2:
  - "3000+ real MCP ... tools" and "over 20,000 synthetic tools";
  - "thousands of distinct agents"; tool simulator; simulated users;
  - an LLM judge filters trajectories against task rubrics;
  - real sandboxes for coding;
  - core, prescriptive ("eliminate reward hacking") and human-annotated rubrics;
  - token budget, with "Responses that exceed this token budget are truncated and assigned a penalty".
- o3 and o4-mini (16 Apr 2025): "not just how to use tools, but to reason about when to use them"; "agentically use and combine every tool within ChatGPT".
- Grok 4 (9 Jul 2025): "trained with reinforcement learning to use tools"; "at pretraining scale"; parallel test-time compute (Heavy).
- Claude 4 (22 May 2025): extended thinking with tool use, "alternate between reasoning and tool use".
- MacDiarmid et al.: "real Anthropic production coding environments"; reward hacking generalises to misalignment (arXiv:2511.18397).
- OpenAI–Hugging Face incident report (26 Aug 2026):
  - July 2026, models "circumvented controls intended to isolate them from the internet";
  - an agent "copied the reference answer into its submission exactly, which led to positive RL reward";
  - cheating "rose over the training runs that contributed to" the incident.
  - The chapter's summary is fair to OpenAI.
- [R1] Grok 4.7 (21 Sept 2026): "a new, larger base model"; "a longer reinforcement learning run on a harder mix of tasks"; hours-long problems.
- [R1] Muse Spark blog (8 Apr 2026): "leverages compute to scalably amplify model capabilities"; Contemplating mode.
- This round, the same blog: "the first in the Muse family of models developed by Meta Superintelligence Labs"; available at meta.ai and the app, plus a "private API preview".
- [R1] Qwen3.5 card: "scaled across million-agent environments".
- Chen et al.: faithfulness "25% for Claude 3.7 Sonnet and 39% for" DeepSeek-R1 (arXiv:2505.05410).
- Michael et al.: 480 completed, "327 (68%)" in the target group; Q4-1 wording "in some non-trivial sense"; split 51% / 49% (arXiv:2208.12852).

**3.8 From ChatGPT to the 2026 frontier**
- ChatGPT 1.2 billion weekly users: Engadget live blog and OpenAI DevDay recap, both 29 Sept 2026. The figure is confirmed; "more than" is not (S2).
- AI Index 2026, Ch. 1: "Training code, parameter counts, dataset sizes, and training duration are no longer disclosed for several of the most resource-intensive systems".
- Epoch AI data:
  - GPT-6 Astra 9.4e26 FLOP; GPT-3 3.14e23; ratio 2,994, so "some 3,000 times".
  - Table 3.9 dates: Claude 3 2024-03-04; Gemini 1.5 2024-02-15; GPT-4o 2024-05-13; Claude 3.7 Sonnet 2025-02-24; Qwen3 2025-04-29; Kimi K2 2025-07-11; Qwen3.5 2026-02-15; Mythos Preview 2026-04-07; Muse Spark 2026-04-08; DeepSeek-V4 2026-04-24; Gemini 3.5 Flash 2026-05-19; Fable 5 / Mythos 5 2026-06-09; Opus 5 2026-07-24; Grok 4.7 2026-09-21; Opus 5.5 2026-09-22; GPT-6 Astra 2026-09-03, Sol and Luna 2026-09-22. All consistent with the table, except Llama 3 (S1).
- Claude 3.7 Sonnet (24 Feb 2025): "the first hybrid reasoning model on the market"; thinking budget "no more than N tokens".
- GPT-5 (7 Aug 2025): "a unified system"; "a real‑time router that quickly decides which to use".
- Claude Opus 5 announcement (24 July 2026): effort settings, low to max.
- Claude Mythos Preview post (7 Apr 2026): withheld from general availability; cyber capability (see S3).
- [R1] Fable 5 / Mythos 5 (9 June 2026): "can work autonomously for longer than any previous Claude models"; same underlying model; Mythos tier above Opus; distillation fallback.
- [R1] Opus 5.5 (22 Sept 2026): effort levels; no longer available with thinking off; "anti-distillation safeguard".
- [R1] GPT-6 Astra system card: "first model to reach the Critical level of cybersecurity capability".
- [R1] GPT-6 Sol and Luna launched 22 Sept 2026.
- [R1] Gemini 4 Argon blog (30 Sept) and Carbon blog (28 Oct): cyber defenders first; "run for days".
- "Every 2026 model whose architecture has been published is still a transformer, in some cases with linear-attention layers mixed in" still holds: Kimi K3 is 69 KDA + 24 Gated MLA layers, and Qwen3.8 uses a hybrid-attention backbone.
- Currency search, 25 Oct to 22 Nov 2026: see S7. No statement in Section 3.8 is falsified.

## Tally
- Claims checked against a web source: 172. Confirmed: 164. Wrong: 2 (M2, S1). Outdated: 1 (M1). Unsupported by cited source: 4 (S2, S3, S4, S5). Could not verify: 1 (Tülu 3 venue).
- Arithmetic items recomputed: 75, plus the tiktoken reproduction in round 1. Errors: 0.
- Bib entries checked: 39. Problems: 0. Two entries need to be added for M1, and one is optional for S2.
- The 39 entries: dao2022flashattention, yue2025does, gunjal2025rubrics, macdiarmid2025natural, michael2023what, chen2025reasoning, nie2025large, khanna2025mercury, deepseekai2025deepseekv32, kimiteam2025kimi, gemmateam2025gemma3, lambert2024tulu (venue unverified), deepseekai2026deepseekv4, edelman2025why, you2025how, openai2026technical, sajadieh2026ai, epochai2026data, bonifacic2026openai, anthropic2026claude, anthropic2026opus5, openai2025sora, google2025fuel, deepmind2025genie, xai2025grok4, openai2025introducingb, openai2025gpt5, anthropic2025claude37, anthropic2025claude4, meta2025llama4, meta2026muse, qwen2025qwen3next, moonshot2025kimi, sdny2023mata, sennrich2016neural, olsson2022context, elhage2021mathematical, openai2026tiktoken, openai2026gpt6.
