# Third review: Chapter 3 — How Large Language Models Work

STATUS: WORK IN PROGRESS (first version saved 11 Nov 2026 after the first full read; web verification and recomputation still running. Items below marked PROVISIONAL are from the first read and my own knowledge and have not yet been opened against a source.)

## Verdict
(pending)

## MUST change before printing
(in progress)

### M1. "The largest open models of 2026" omits the two largest (Kimi K3, 2.8 trillion; Qwen3.8, 2.4 trillion)
- Where: textbook/chapters/ch03.md:448 (and Table 3.9, lines 431-444, which has no row for either)
- Text now: "The largest open models of 2026 are mixtures of experts with around a trillion parameters or more, of which a few per cent are used for each token. DeepSeek-V4-Pro has 1.6 trillion parameters, 49 billion of them active, and was pre-trained on more than 32 trillion tokens [@deepseekai2026deepseekv4]; Kimi K2 has 1.04 trillion with 32 billion active [@kimiteam2025kimi]; Muse Spark Open has 816 billion and routes each token to 8 of 256 experts [@meta2026musesparkopen]."
- Problem: OUTDATED / misleading "largest" claim. Moonshot's Kimi K3 (weights on Hugging Face, July 2026) has 2.8 trillion parameters and Alibaba's Qwen3.8-2.4T-A95B (weights 12 August 2026) has 2.4 trillion; both are larger than every model the sentence names, and Kimi K2 is a 2025 model. An informed reader will take the sentence to say DeepSeek-V4-Pro is the largest open model.
- Evidence: https://huggingface.co/moonshotai/Kimi-K3 (model card: "2.8T-parameter model", activated "104B", "activates 16 out of 896 experts", 93 layers, "69 KDA + 24 Gated MLA", context 1048576); https://thenextweb.com/news/moonshot-kimi-k3-largest-open-model (17 July 2026: "a 2.8-trillion-parameter system", "DeepSeek's V4-Pro tops out at 1.6 trillion"); https://letsdatascience.com/news/alibaba-releases-qwen38-max-open-model-weights-b63514d0 (Qwen3.8-2.4T-A95B, 2.4 trillion total, 95 billion active, weights 12 Aug 2026; secondary source, Qwen card not opened).
- Change to: "The largest open models of 2025-26 are mixtures of experts with around a trillion parameters or more, of which a few per cent are used for each token. Moonshot's Kimi K3, released in July 2026, is the largest, with 2.8 trillion parameters according to its model card, about 104 billion of them active; DeepSeek-V4-Pro has 1.6 trillion parameters, 49 billion of them active, and was pre-trained on more than 32 trillion tokens [@deepseekai2026deepseekv4]; Kimi K2 (2025) has 1.04 trillion with 32 billion active [@kimiteam2025kimi]; Muse Spark Open has 816 billion and routes each token to 8 of 256 experts [@meta2026musesparkopen]." Add a bib entry for the Kimi K3 model card (Moonshot AI, 2026, https://huggingface.co/moonshotai/Kimi-K3). Optionally add a Table 3.9 row: "Kimi K3 | Moonshot AI | Jul 2026 | 2.8-trillion-parameter open MoE; linear-attention (KDA) and latent-attention layers; 1-million-token context".


## SHOULD change (real but not blocking)

### S-prov-1. FlashAttention "saves time but not memory" (PROVISIONAL, to be checked against the paper)
- Where: textbook/chapters/ch03.md:243
- Text now: "That saves time but not memory; the next subsection describes four further remedies used by models of 2024–26."
- Problem: FlashAttention's own headline claim is that it is memory-efficient: it never materialises the n-by-n attention matrix, so working memory is linear rather than quadratic in sequence length. What it does not shrink is the KV cache or the quadratic amount of arithmetic. An ML reader will read the sentence as wrong.

### S-prov-2. "Llama 3 ... Jul 2024" in Table 3.9 (PROVISIONAL)
- Where: textbook/chapters/ch03.md:420
- Problem: the caption says dates are "first release or announcement". Llama 3 was first released in April 2024 (8B, 70B); the 405B model and the cited paper are from July 2024 (released as Llama 3.1).

### S-prov-3. Doubled connective
- Where: textbook/chapters/ch03.md:90
- Text now: "So "bank" in "the river bank" and "bank" in "the bank raised rates" can therefore end up represented quite differently."
- Change to: "So "bank" in "the river bank" and "bank" in "the bank raised rates" can end up represented quite differently."

## Could not verify
(pending)

## Reader notes
(pending)

## Checked and confirmed
(in progress; web-verified so far)
- 3.1 Table 3.1 token IDs, Table 3.3 n_vocab (50,257 / 100,277 / 200,019), Table 3.4 counts (7/7, 9/15, 12/62, 13/20), strawberry, 12345678, parrot emoji (4 bytes, 3 tokens in both), " cat"=9059, model-to-encoding mapping for gpt-4o/o3/gpt-4.1/gpt-5: all reproduced with tiktoken 0.14.0 (pip).
- 3.1 Table 3.2 BPE merges: reproduced by running Sennrich et al.'s Algorithm 1.
- 3.8 DeepSeek-V4 (arXiv page: title, 1.6T/49B, 284B/13B, 1M context, >32T tokens, 27% FLOPs and 10% KV cache vs V3.2).
- 3.8 Fable 5 / Mythos 5 (anthropic.com, 9 June 2026: "can work autonomously for longer than any previous Claude models"; same underlying model; Mythos tier above Opus; distillation fallback to Opus 4.8).
- 3.8 Opus 5.5 (anthropic.com, 22 Sept 2026: effort low/medium/high/xhigh/max; "no longer available with "thinking" mode switched off"; "anti-distillation safeguard").
- 3.8 GPT-6 Astra system card (deploymentsafety.openai.com: "first model to reach the Critical level of cybersecurity capability"); GPT-6 Sol and Luna launched 22 Sept 2026 (TechCrunch, MacRumors headlines); MRCR 512K-1M 96.3% (InfoQ).
- 3.8 Grok 4.7 (x.ai, 21 Sept 2026: "a new, larger base model", "a longer reinforcement learning run on a harder mix of tasks", "weighted toward problems that take many hours to complete").
- 3.4/3.8 Gemini 4 Argon docs (1,048,576 unified limit; Text, Image, Video, Audio, PDF in; Text out; thinking low/medium/high); Argon blog 30 Sept 2026 and Carbon blog 28 Oct 2026 (cyber defenders first; "run for days").
- 3.4/3.8 Muse Spark Open card (816B/42B, 8 of 256 experts, 1.8B perception encoder, text+image+video+audio in, text out, 15 Oct 2026).
- 3.4/3.7 Qwen3.5-397B-A17B card (60 layers = 15 x (3 Gated DeltaNet + 1 Gated Attention); early fusion; "scaled across million-agent environments").
- 3.7/3.8 Muse Spark blog 8 April 2026 ("leverages compute to scalably amplify model capabilities"; Contemplating mode; meta.ai + private API preview).
- 3.8 ChatGPT 1.2 billion weekly users (Engadget live blog 29 Sept 2026).
Arithmetic recomputed by hand on first read, all consistent (to be re-run in Python): softmax worked example (Table 3.5), GPT-2 parameter table (3.6), KV-cache table (3.8), temperature ratios, cross-entropy values, sigma(1), t/(1-t), GRPO example, 147,000/2.79M, 128,000 squared, 9.4e26/3.14e23.

## Tally
(pending)
