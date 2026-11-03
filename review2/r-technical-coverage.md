# Technical coverage review: does the book cover the path from "normal LLMs" to the frontier models of October 2026?

Reviewer scope: the author's question "Is it covering all the development from normal LLMs to our most top-tier models currently, from a technical point of view?" Method: (1) I built an independent map of how language models developed technically from GPT-2/GPT-3 to November 2026, using web research and my own background knowledge. (2) I read Chapters 2, 3, 4, 5 and 7 in full, skimmed Chapters 1, 6, 9 and 12 for technical content, and grepped the whole book for about 120 model names and technical terms. (3) I mapped each item on my list to where the book covers it. No book files were edited.

A caveat on the 2026 model lineage: for Nov 2025 to Oct 2026, the only web sources I could reach were mostly secondary release trackers (aggregators). They agree on the main releases but disagree on some dates. Where I name a 2026 release the book does not mention, I flag it **"verify"**.

---

## 1. Verdict

**Mechanisms of a 2022-era LLM: strong, accurate and unusually rigorous. The 2024–2026 path to today's frontier: only partly covered. Publish after a targeted addition (about 5,000–7,000 words across Ch. 3, 4 and 5, plus one table), not as is.**

The deciding reasons:

1. **The "classic" stack is explained excellently and correctly.** Tokenisation, attention, the transformer block, the KV cache, GQA, RoPE, MoE, decoding, pre-training data, SFT, RLHF, DPO, Constitutional AI, RLVR/GRPO, scaling laws, Chinchilla, over-training, test-time compute, benchmarks, FP8/BF16 and memory bandwidth are all there. Worked numbers are recomputed from real models. Every technical claim I spot-checked held (Section 6).
2. **The book never says, in one place, what a 2026 frontier model *is*.** No section or table contrasts GPT-3 (2020) or ChatGPT (2022) with GPT-6 Astra, Claude Mythos/Opus or Gemini 4 Argon. The relevant facts are scattered across Chapters 1, 3, 4, 5, 7 and 12, and the closed frontier models (OpenAI, Anthropic, Google, xAI) appear almost only as names attached to benchmark scores and safety incidents. A reader cannot get from the book a technical answer to "what changed between ChatGPT and today?"
3. **The defining technical shift of 2025–26 is missing: agentic, tool-integrated reinforcement learning.** This means training models with RL in environments where they call tools, write and run code, browse and operate computers over long horizons, with reasoning interleaved between the tool calls. Chapter 3 presents RLVR only on maths and code answers. Chapter 5 presents agents as prompted scaffolding (ReAct, 2022) plus a harness. The book therefore cannot explain why Claude Opus 4.6 reaches a 12-hour METR horizon or why OSWorld went from 12% to 90%, both of which it reports.
4. **Multimodality is the second large gap.** Native multimodal or "omni" models, real-time speech-to-speech, native image generation inside LLMs, video generation with sound, and world models get roughly one sentence in Chapter 3 (line 92), one paragraph in Chapter 9 and nothing more. For a book about AI "as it stands in October 2026", that badly under-represents what frontier models are.
5. **Several statements are now outdated in framing, though not false.** Examples: "essays and advice have no such checker" (rubric- and LLM-judge-based RL is the 2025–26 answer); the account of test-time compute (no thinking budgets, effort settings, hybrid or router models, parallel "deep think"); and the open-model story, which omits Meta's retreat from open Llama and the 2025–26 Chinese open-weight frontier (Kimi K2/K3, MiniMax, later Qwen and GLM).

---

## 2. My independent map, and the coverage matrix

Depth scale: **D3** = textbook-level, mechanism explained; **D2** = explained briefly; **D1** = named or mentioned; **—** = absent.

### A. Architecture

| Topic | Covered? Where | Depth | Correct? | Gap |
|---|---|---|---|---|
| Tokenisation (BPE, byte-level, vocabulary growth, language inequity) | Ch3 §3.1 | D3 | Yes (tables recomputed with tiktoken) | None of note. Tokeniser-free and byte models (BLT) not needed |
| Embeddings, self-attention, multi-head, causal mask, encoder vs decoder | Ch3 §3.2 | D3 | Yes | — |
| Transformer block, residual stream, pre-norm, RMSNorm, SwiGLU | Ch2 §2.5, Ch3 §3.3 | D3 | Yes | QK-norm, logit soft-capping and attention sinks absent (fine for audience) |
| Positional encodings (sinusoidal, learned, RoPE, base frequency) | Ch3 §3.3 | D3 | Yes | Context extension (position interpolation/YaRN, progressive long-context training), NoPE/iRoPE (Llama 4) absent |
| Mixture of experts (Shazeer, Mixtral, DeepSeek-V3 routing, load balancing) | Ch3 §3.3; Ch4 §4.3 (MoE scaling laws) | D2–D3 | Yes | Fine-grained and shared experts; the fact that nearly every 2026 frontier model is believed to be MoE (1T+ total parameters is now normal: Kimi K2, DeepSeek-V4-Pro 1.6T, Qwen3.8 2.4T, Mistral Large 4 1T) — not drawn out |
| KV cache, GQA | Ch3 §3.4 (Table 3.8) | D3 | Yes (66 GB figure checks: 126×2×8×128×2 B × 128k) | **Multi-head latent attention (MLA, DeepSeek-V2/V3, Kimi K2)** absent, though it is the main KV-compression technique of 2024–26 open models and the book discusses DeepSeek extensively |
| FlashAttention | Ch3 §3.4 | D1–D2 | Yes | — |
| Sliding-window / local-global attention (Mistral, Gemma 2/3, gpt-oss) | — | — | — | Absent |
| Sparse attention (DeepSeek Sparse Attention in V3.2; V4's compressed sparse attention) | Ch3 §3.4, one sentence on V4 | D1 | Yes (27% FLOPs / 10% KV vs V3.2 matches model card) | Mechanism not explained |
| Linear attention / state-space / hybrids (Mamba, Jamba, Nemotron-H, Qwen3-Next/3.5 Gated DeltaNet, MiniMax lightning attention, Kimi Linear) | Ch3 §3.4, one sentence on Qwen3.5 | D1 | Yes (45 of 60 layers matches card) | "Mamba"/"state-space" never named; no explanation of why linear-cost layers matter (long agent trajectories) |
| Multi-token prediction (DeepSeek-V3, used also for speculative decoding) | — | — | — | Absent |
| Diffusion language models (Gemini Diffusion, Inception Mercury, LLaDA) | — | — | — | Absent. Only autoregression is described ("Each token, once emitted, stays", Ch3 l.183) |
| Residual-stream innovations (hyper-connections / DeepSeek mHC, 2026) | — | — | — | Absent (minor) |
| Vision encoders / how images become tokens | Ch3 l.92 (ViT patches, CLIP, Gemini 1.5) | D1 | Yes | No account of how a vision-language model is built (encoder + projector vs native early fusion) |

### B. Pre-training

| Topic | Where | Depth | Correct? | Gap |
|---|---|---|---|---|
| Objective, cross-entropy, self-supervision | Ch3 §3.5 | D3 | Yes | — |
| Data scale, filtering, FineWeb, Llama 3 mix | Ch3 §3.5; Ch4 §4.5 | D2–D3 | Yes | Mid-training/annealing on high-quality and reasoning data, and code/maths up-weighting as standard practice: not named |
| Scaling laws, Chinchilla, replication, over-training | Ch4 §4.2–4.3 | D3 (exemplary) | Yes | — |
| Data wall, repetition, synthetic data, model collapse | Ch4 §4.5 | D3 | Yes | Synthetic pre-training data in practice (rephrasing, textbook-style data, Phi; reasoning traces used as pre-training data) only gestured at via the AI Index |
| Distillation | Ch4 §4.5 (Hinton; R1 distillation); Ch7 | D2 | Yes | Distillation as the standard way small and flash tiers are made (Gemma, Gemini Flash, Llama 4 co-distillation), and contested distillation from competitors' APIs: absent |
| Optimisers: SGD, momentum, Adam, AdamW, schedules incl. WSD, Muon | Ch2 §2.5 + box | D3 | Yes | Good and current (Kimi K2 MuonClip, DeepSeek-V4 Muon) |
| Precision: mixed precision, BF16, FP8 (DeepSeek-V3), FP4 on Blackwell | Ch7 §7.1 | D2–D3 | Yes (the "14 bits" accumulation claim matches the V3 report) | FP4/MXFP4 training and serving (gpt-oss shipped in MXFP4; NVFP4 training) named only as a hardware feature |
| Training compute trends and costs | Ch4 §4.4 | D3 | Yes | — |
| Infrastructure: parallelism, failures, MFU | Ch4 §4.1; Ch7 | D2 | Yes | Data/tensor/pipeline/expert parallelism not explained (acceptable) |

### C. Post-training

| Topic | Where | Depth | Correct? | Gap |
|---|---|---|---|---|
| SFT / instruction tuning | Ch3 §3.5 | D2 | Yes | — |
| RLHF (reward model, PPO, KL penalty) | Ch3 §3.5; Ch12 §12.1 | D3 | Yes | — |
| DPO and the PPO-vs-DPO debate | Ch3 §3.5 | D3 | Yes | Variants (IPO, KTO, SimPO, online DPO) not needed |
| Constitutional AI / RLAIF | Ch3 §3.5; Ch12 | D2 | Yes | Anthropic's 2026 constitution, if discussed, is in Ch12/13 (not checked in depth) |
| RLVR, GRPO, R1-Zero | Ch3 §3.7 | D3 | Yes (GRPO worked example correct) | Successor algorithms (DAPO, GSPO, Dr GRPO) not needed for this audience |
| Reasoning models: o1, o3, R1; faithfulness; does RL add skills | Ch3 §3.7; Ch4 §4.6; Ch12 §12.5 | D3 | Yes | Stops at early 2025 |
| **Hybrid and controllable reasoning** (thinking on/off, effort levels, thinking budgets, GPT-5's router, adaptive thinking) | — | — | — | Absent. Every 2026 frontier model exposes this, and the book mentions GPT-6 Sol/Luna tiers without explaining them |
| **Parallel test-time compute** (Deep Think, best-of-n with verifiers, multi-agent "heavy" modes; the IMO 2025 gold systems) | Ch4 §4.6 (2024 research on sampling); Ch6 §6.5 (IMO results, not mechanism) | D1–D2 | Yes | How IMO-gold-level systems worked technically is not connected to Ch3/4 |
| Process vs outcome rewards (PRMs, "Let's verify step by step") | Ch4 l.171 mentions a "learned scoring function" re-ranking samples | D1 | — | Absent as a concept |
| **Rewards for non-verifiable tasks** (rubrics, generative reward models, LLM-as-judge) | Ch14 l.238 mentions "other models acting as judges" | D1 | **Framing outdated**: Ch3 l.330 says essays and advice "have no such checker, which … limits the method there" | Needs a paragraph on how labs extended RL beyond checkable answers in 2025–26 |
| **Agentic / tool-integrated RL** (RL in coding, browser, terminal and computer environments; interleaved thinking and tool calls; long-horizon credit assignment; environments as the new scarce input) | Ch4 l.149 one clause ("problems and environments with checkable answers"); Ch12 (reward hacking in "production coding environments") | D1 | — | **Biggest single gap** (see Section 3) |
| RL compute share growing toward pre-training scale | Ch3 l.326; Ch4 §4.8 | D2 | Yes, careful | Could add xAI's own July 2025 claim that Grok 4 used RL compute at pre-training scale (a company claim; the evidence log says no primary disclosure was found) |
| Self-play / self-improvement | Ch1 (AlphaGo only) | — | — | Absent for LLMs (e.g. self-generated tasks, Absolute Zero). Minor |
| Safety post-training (deliberative alignment, refusal training, unlearning) | Ch12 §12.1 | D2 | Not checked in depth | — |

### D. Multimodality

| Topic | Where | Depth | Correct? | Gap |
|---|---|---|---|---|
| Image input in LLMs (GPT-4, Gemini 1.5) | Ch1 l.226; Ch3 l.92 | D1 | Yes | No mechanism |
| Diffusion image generation, latent diffusion, rectified flow | Ch1; Ch9 §9.1 | D2–D3 | Yes | — |
| Native/autoregressive image generation inside LLMs (GPT-4o image, Gemini image models) | Ch9 l.15, one clause | D1 | Yes | No explanation that frontier chat models now generate and edit images themselves |
| Video generation (Sora 2, Veo 3 with synchronised audio), world models (Genie 3) | Ch7 (energy only), Ch9 (Sora once) | D1 | — | Absent technically |
| Speech: codec language models (VALL-E), voice cloning | Ch9 §9.1 | D2 | Yes | **Real-time speech-to-speech "omni" models** (GPT-4o voice, Gemini Live, 2026 realtime models) absent |
| Omni / any-to-any models, robotics VLAs | Ch1, Ch12 (VLA mentioned) | D1 | — | Absent as a technical development |

### E. Inference and serving

| Topic | Where | Depth | Correct? | Gap |
|---|---|---|---|---|
| Prefill/decode, KV cache, PagedAttention/vLLM, batching | Ch3 §3.4; Ch7 §7.1 | D3 | Yes (one op per byte, 42 ms/token checked) | — |
| Speculative decoding | Ch3 l.183 | D1–D2 | Yes (simplified) | Draft heads/MTP not covered |
| Quantisation for serving (INT8/INT4/FP4, GPTQ/AWQ) | Ch4 l.100 (Kumar et al. on quantisation damage) | D1 | Yes | Not explained as standard practice; how open models run on laptops is absent |
| Prompt caching, disaggregated serving, expert parallelism | — | — | — | Absent (minor) |
| Price per token and energy trends | Ch4 §4.6; Ch7 §7.4–7.5 | D3 | Yes | — |
| Hardware (GPUs, TPUs, HBM, interconnect, Blackwell, Rubin) | Ch7 §7.1 | D3 | Yes | — |

### F. Tools, agents, memory, retrieval

| Topic | Where | Depth | Correct? | Gap |
|---|---|---|---|---|
| RAG, dense retrieval | Ch3 §3.6 | D2–D3 | Yes | Agentic search / "deep research" products absent |
| Function calling, MCP, A2A | Ch5 §5.3 | D3 | Yes, current to July 2026 | — |
| ReAct, Reflexion, memory designs, context engineering, compaction, sub-agents | Ch5 §5.2 | D3 | Yes | Model-native long-term memory in products (ChatGPT/Claude memory) absent; continual learning as a research frontier absent |
| Computer use, coding agents, benchmarks | Ch5 §5.4 | D3 | Yes | How models are *trained* to do this (see C) absent; coding agents (Claude Code, Codex) named but not described as products that changed the field |
| Prompt injection and security | Ch5 §5.6 | D3 (excellent) | Yes | — |
| Multi-agent systems | Ch5 §5.8 | D2–D3 | Yes | — |

### G. Evaluation

| Topic | Where | Depth | Correct? | Gap |
|---|---|---|---|---|
| Emergence debate, saturation, contamination, validity, Arena gaming | Ch4 §4.7 | D3 | Yes | — |
| HLE, GPQA, ARC-AGI-1, SWE-bench family, OSWorld, τ-bench, METR horizons, ClockBench | Ch4, Ch5 | D3 | Yes | ARC-AGI-2/3, GDPval (economically valuable tasks), Terminal-Bench, FrontierMath (only in Ch14), LMArena as a 2026 ranking: thin |

### H. The actual model lineage (OpenAI, Anthropic, Google, Meta, xAI, DeepSeek, Qwen, Kimi, Mistral, others)

| Lineage item (my map) | In book? |
|---|---|
| GPT-3 → InstructGPT → ChatGPT → GPT-4 (multimodal input) | Yes (Ch1, Ch3) |
| GPT-4o (natively multimodal, voice) | Only as a tokeniser, energy and sycophancy reference; its omni design is not explained |
| o1 → o3 → GPT-5 (Aug 2025, unified router of fast and thinking models) → GPT-5.x → GPT-6 Astra/Sol/Luna (Sep 2026) | o1/o3 yes. GPT-5 only as a compute and benchmark data point; its router/unified design is absent. GPT-6 appears via Epoch's compute estimate, HLE, OSWorld 2.0 and safety; its tiers and computer-use focus are not explained |
| gpt-oss (Aug 2025, open MoE, MXFP4) | Licence and safety only |
| Claude 3 → 3.5/3.7 (first hybrid reasoning model) → 4 → 4.5/4.6/4.7 → Mythos Preview (Apr 2026) / Fable 5 → Opus 5 / Opus 5.5 / Sonnet 5.5 (Jul–Oct 2026, **verify**) | Up to Opus 4.7 and Mythos/Fable via evaluations. **No mention of Claude Opus 5 or 5.5 anywhere** (grep "Opus 5": 0 hits), although trackers list Opus 5.5 (22 Sep 2026) as Anthropic's current flagship — **verify** |
| Gemini 1.5 (long context) → 2.0/2.5 (thinking) → 3 (Nov 2025) → 3.1 Pro → 3.5/3.8 Flash → Gemini 4 Argon (Oct 2026); Gemma 3/4 | Gemini 1.5 long context yes; 2.5, 3, 3.1 and 4 Argon appear only as benchmark scores (Gemini 4 Argon once, for ClockBench). No technical description |
| Meta: Llama 3 → Llama 4 (MoE, Apr 2025; Behemoth not clearly ahead) → Meta Superintelligence Labs' closed Muse models (2026, **verify**) | Llama 3 deeply; Llama 4 licence and Arena gaming. Meta's move away from open weights is absent |
| xAI: Grok 3/4 (huge RL compute), 4.x | Compute and cost only |
| DeepSeek: V2 (MLA) → V3 (MoE, FP8, MTP) → R1 → V3.1/V3.2 (DSA) → V4 (Apr 2026, 1M context, mHC, Muon) | V3, R1 and V4 covered well on cost and compute; MLA, MTP, DSA and mHC unexplained |
| Qwen 2.5 → 3 (hybrid thinking) → 3.5/3.6 (Gated DeltaNet hybrid) → 3.8 (Aug 2026, **verify**) | 2.5 deeply, 3 for data size, 3.5 one sentence |
| Moonshot Kimi K2 (1T MoE, MuonClip) → K2 Thinking (Nov 2025, hundreds of interleaved tool calls) → K2.5 → K3 (Jul 2026, **verify**) | K2 in the Ch2 box only |
| Mistral (7B, Mixtral, Large 2/3/4), GLM-5, MiniMax, Nemotron hybrids | Mixtral and licences only; GLM-5 in Table 7.5 |

---

## 3. Missing or outdated topics, ranked by how much their absence hurts a book claiming to explain AI "as it stands in October 2026"

1. **No technical portrait of the 2026 frontier model, and no lineage.** A reader finishes Chapter 3 with a good model of InstructGPT plus R1. They never learn that today's flagship models are typically very large sparse MoE models trained on tens of trillions of tokens with heavy synthetic and reasoning data. Nor do they learn that these models are natively multimodal, have 1M-token contexts with compressed or hybrid attention, run controllable reasoning, and are post-trained with large-scale RL in tool-use environments. Finally, they never learn that they are served as tiered model families (Astra/Sol/Luna; Mythos/Opus/Sonnet/Haiku; Pro/Flash/Flash-Lite) distilled from the largest model. This is the direct answer to the author's question, and it is missing.
2. **Agentic RL and tool-integrated reasoning.** This is the main driver of the 2025–26 capability jumps the book itself reports (the METR horizon, OSWorld, SWE-bench). Its absence leaves Chapter 5 explaining agents as clever prompting, which was true in 2023, not in 2026.
3. **Rewards beyond verifiable answers** (rubrics, generative and LLM-judge reward models, process reward models). Without this, Ch3 l.330 implies RL cannot help writing or advice, which the 2025–26 literature and products contradict. The sentence is outdated, not false: the author marks it as his view.
4. **Multimodality and omni models**: native image generation and editing, real-time voice, video with audio, world models. It is the most visible change to users between 2023 and 2026, and it is reduced to a few lines.
5. **Reasoning-control and test-time-compute productisation**: hybrid thinking (Claude 3.7, Qwen3), routers (GPT-5), effort and budget settings, parallel "deep think" modes, and how IMO-2025-gold systems worked. Chapter 4's test-time section is solid but ends with o3 (April 2025).
6. **Efficient long-context architecture** (MLA, sliding-window, sparse attention, SSM/linear hybrids, MTP). It is touched in two sentences. This is important because it is *why* 1M-token contexts and long agent runs became affordable, and because it is the main way open Chinese labs differ technically from each other.
7. **Open-weight landscape of 2025–26**: Kimi K2/K3, MiniMax, later Qwen and GLM, Mistral Large 3/4, Gemma 4, Nemotron hybrids, Meta's pivot to closed models (**verify**), gpt-oss's design. Ch7 §7.6 is strong on governance and licences but thin on what these models are.
8. **Serving-side practice**: quantisation, distilled small tiers, on-device models, prompt caching. Moderate.
9. **Diffusion LMs and other non-autoregressive generation.** Minor, but one paragraph would stop "each token, once emitted, stays" from reading as universal.
10. **Memory and continual learning** (product memory; 2026 research such as DeepSeek's Engram and test-time-training approaches). Minor to moderate, and a natural bridge to Ch14's outlook.

---

## 4. Errors and imprecisions in technical explanations

I found **no verified-wrong technical statements** in Chapters 2, 3, 4, 5 and 7 within this scope. That is unusual and to the author's credit. Items to fix or tighten:

- **Ch3 l.330** — "essays and advice have no such checker, which in the author's view limits the method there." Outdated framing. Add that labs now use rubric-based and model-judged rewards, with their own reward-hacking risk (linking to Ch12).
- **Ch3 l.183** — "Each token, once emitted, stays. A standard autoregressive model cannot delete…". This is correct for autoregressive models, but the chapter never says that non-autoregressive (diffusion) text models exist. Add one clause.
- **Ch3 l.183** — speculative decoding "keeping those it would have produced itself". This is accurate only for greedy decoding. For sampling, the method accepts or rejects draft tokens so that the output *distribution* is unchanged (Leviathan et al.). Reword: "…and the output has exactly the same probabilities as the large model alone would give."
- **Ch2 box (DeepSeek-V3 line)** — "most of the heaviest arithmetic done in 8-bit numbers (Section 2.6)". FP8 is explained in Section 7.1, not 2.6. Fix the cross-reference.
- **Ch2 box (Kimi K2)** — "safeguard at scale against exploding attention scores (Chapter 3)". Chapter 3 never discusses exploding attention logits. Either add a sentence in Ch3 or drop the cross-reference.
- **Ch2 box (Llama line)** — "RMSNorm applied at the input of each sub-layer … an arrangement used earlier in OpenAI's GPT-2". GPT-2 used pre-*LayerNorm*, not RMSNorm. The sentence means the placement, but it reads as if GPT-2 used RMSNorm. Reword as "input-side normalisation, an arrangement…".
- **Ch3 l.238** — DeepSeek-V4 "compresses and sparsifies attention". This is correct, but the KV-cache story (Table 3.8) jumps from GQA to V4 without MLA, the DeepSeek-V2/V3 technique that V4 builds on. Readers who see "671B DeepSeek-V3" in four chapters never learn its key inference trick.
- **Ch4 l.149** — "Ilya Sutskever, formerly of Google and OpenAI". This is incomplete rather than wrong. He has co-founded and led Safe Superintelligence since 2024, which is relevant context for his "age of research" claim.
- **Ch3 Figure 3.3 caption / l.326** — RL at "about 5%" of pre-training compute is correctly attributed to DeepSeek-R1. But the caption reads as typical. Say explicitly that by 2025–26 several labs claimed far larger shares (xAI for Grok 4, a company claim), and that the share for closed 2026 models is undisclosed.

Spot-checked as correct: Llama 3 405B KV cache (0.52 MB/token, 66 GB at 128k); GPT-2 parameter table; GRPO normalisation example; Kaplan's d_model > n_ctx/12 condition; C ≈ 6ND for Llama 3.1 and DeepSeek-V3; H100 ridge point of about 300 FLOP/byte and 42 ms per weight read; FP8 E4M3/E5M2 maxima; Qwen3.5 layer layout (model card "15 × (3 × Gated DeltaNet + 1 × Gated Attention)"); DeepSeek-V4 27% FLOPs and 10% KV vs V3.2 and 1.6T/49B (model card, via secondary sources); GPT-6 Astra on 3 Sep 2026 (trackers agree); Hopper FP8 accumulation at about 14 bits (V3 report); Gemini 1.5's 99% recall at 10M tokens.

---

## 5. Would a reader understand what distinguishes a 2026 frontier model from GPT-3 or ChatGPT (2022)?

**Partly.** A careful reader could assemble five differences from the book:

- post-training (RLHF, then RL with verifiable rewards and reasoning chains): Ch3;
- much more data and compute, smaller over-trained models, and MoE: Ch3–4;
- longer context: Ch3 §3.4;
- tool use and agent loops: Ch5;
- far higher benchmark scores and time horizons: Ch4–5.

They would **not** learn:

- that frontier models are now trained *as agents* (RL in tool, code and computer environments), not merely wrapped in agent loops;
- that they see, hear, speak and generate images, audio and video natively;
- how reasoning is controlled and paid for (effort levels, routers, parallel thinking);
- what architectural changes made 1M-token contexts affordable (MLA, sparse and hybrid attention);
- how model families and tiers are produced (distillation from a top model);
- anything technical about GPT-5/6, Claude 4.x/5.x/Mythos or Gemini 3/4 beyond their scores.

The contrast is never stated explicitly; the reader has to infer it.

---

## 6. Concrete proposals

| # | What to add | Where | Words | Key sources |
|---|---|---|---|---|
| P1 | **"From ChatGPT to the 2026 frontier" synthesis**, with a table of about 12 rows (GPT-3, ChatGPT/InstructGPT, GPT-4, GPT-4o, o1, DeepSeek-V3/R1, Claude 3.7, GPT-5, Gemini 3, Kimi K2 Thinking, DeepSeek-V4, GPT-6 Astra / Claude Opus 5.5 / Gemini 4 Argon). Columns: architecture (dense/MoE, total/active parameters where public), context, modalities in/out, reasoning mode, post-training, open/closed. Mark undisclosed cells "not disclosed". | New §3.8 closing Ch3 (or end of §1.7 with a pointer) | 1,200–1,500 + table | Company system cards and model cards; DeepSeek-V3/V4 reports; Kimi K2 report (arXiv 2507.20534); GPT-5 system card (Aug 2025, router design); Epoch AI model database; AI Index 2026 |
| P2 | **Agentic RL**: environments, tool-integrated reasoning, interleaved thinking, long-horizon credit, reward hacking in environments (link to Ch12), environment scarcity as the new data constraint | Ch3 §3.7 new subsection, and a 300-word bridge at the start of Ch5 §5.4 ("why agents got better") | 900–1,200 | Kimi K2 / K2 Thinking reports (Moonshot 2025); DeepSeek-V3.2 report (agentic task synthesis); OpenAI Codex/o3 system cards; Anthropic Claude 4.x system cards; MacDiarmid et al. 2025 (already cited); Epoch "RL environments" pieces |
| P3 | **RL beyond verifiable answers**: rubrics, generative reward models, process vs outcome rewards | Ch3 §3.7, replacing the l.330 sentence | 400–500 | Lightman et al. 2023 "Let's Verify Step by Step"; Gunjal et al. 2025 "Rubrics as Rewards"; DeepSeek-GRM (Liu et al. 2025); Kimi K2 self-critique rubric reward |
| P4 | **Controllable reasoning and parallel test-time compute**: hybrid models, thinking budgets, routers, "deep think"/heavy modes; the IMO 2025 gold systems as the worked case | Ch4 §4.6, new subsection after "Scaling at test time" | 600–800 | Anthropic Claude 3.7 announcement (extended thinking); Qwen3 report (thinking budget); GPT-5 system card; Google Gemini Deep Think IMO blog (Jul 2025); OpenAI IMO statement |
| P5 | **Efficient attention and long context**: MLA (with one KV-size row added to Table 3.8), sliding-window, sparse attention (DSA), linear and SSM hybrids (Mamba → Gated DeltaNet), MTP; why this matters for agents | Ch3 §3.4, expand "Context windows" | 700–900 | DeepSeek-V2 (arXiv 2405.04434, MLA); DeepSeek-V3 (MTP); DeepSeek-V3.2 (DSA); Gu & Dao 2023 (Mamba); Yang et al. 2024 (Gated DeltaNet); Qwen3-Next/3.5 card; Gemma 3 report (local-global) |
| P6 | **Multimodal and omni models**: how images enter an LLM (encoder + projector vs early fusion); native image generation; speech-to-speech; video with audio; world models | New §3.x or a Ch9 §9.1 expansion with a pointer from Ch3 | 1,000–1,300 | GPT-4o system card; Gemini 1.5/2.5/3 reports; Chameleon (Meta 2024); Veo 3 / Sora 2 system cards; Genie 3 blog; Qwen2.5-Omni report |
| P7 | **Diffusion LMs** paragraph | Ch3 §3.4 after "autoregressive" | 150–200 | LLaDA (Nie et al. 2025); Inception Mercury (2025); Google Gemini Diffusion (May 2025) |
| P8 | **Serving practice**: quantisation (INT4/FP4, gpt-oss MXFP4), distilled tiers, prompt caching, on-device | Ch7 §7.1 after "Number formats", or Ch3 §3.4 | 400–500 | gpt-oss model card; Frantar et al. GPTQ; Lin et al. AWQ; Gemma/Gemini Flash reports |
| P9 | **Open-weight frontier 2025–26** paragraph plus extended Table 7.5 (Kimi K2/K3, MiniMax, Qwen3.5+, Mistral Large 3, Gemma 4, Nemotron), and Meta's shift (**verify**) | Ch7 §7.6 | 400–600 | Model cards; Epoch "open vs closed" (already cited); AI Index 2026 |
| P10 | **Currency check of the closed lineage**: the book has no Claude Opus 5/5.5, Sonnet 5.5, Gemini 3.5/3.8, Grok 4.x or Mistral Large 4. Verify against vendor pages and either mention them in P1 or state the cut-off explicitly | P1 table; Ch1 §1.7 timeline | 100–200 | Vendor announcement pages (trackers below are leads only) |
| P11 | Fix the cross-references and wording in Section 4 above | Ch2, Ch3, Ch4 | ~100 net | — |

**Total**: about 5,500–7,500 words. That fits by trimming: Chapter 5's payments section (§5.7) and parts of Chapter 7's sovereign-AI section are lower-value for the technical question and could give up about 1,500 words.

---

## 7. What works (technical)

- Chapter 3 is among the best general-reader explanations of transformers I have seen. Every number is recomputed from real models (tiktoken, GPT-2, Qwen2.5), with settings stated.
- Chapter 4's scaling-law treatment is exemplary: Kaplan vs Chinchilla, the Besiroglu replication, over-training, MoE scaling laws, the RL-scaling evidence, and a balanced "is scaling slowing" debate.
- The Chapter 2 optimiser box is current to 2026 (WSD, Muon, DeepSeek-V4).
- Chapter 5 on tool protocols, prompt-injection security, reliability maths (pass@k vs pass^k) and benchmark decay is rigorous and current to mid-2026.
- Chapter 7 §7.1 explains memory-bandwidth-bound decoding and number formats correctly.
- Epistemic labelling throughout (company claim vs preprint vs peer-reviewed) is consistent.

## 8. Spot-check tally (technical claims, this scope)

- About 25 technical and quantitative claims were checked by recomputation or against sources.
- **Confirmed**: 23.
- **Wrong**: 0 substantive. There are 3 wording or cross-reference slips (Section 4).
- **Unverifiable from primary sources**: 2 2026 items, where I could reach only secondary confirmation (the DeepSeek-V4 card figures and the GPT-6 Astra date). Both are consistent with the book.
- **Outdated framing**: 1 (Ch3 l.330).
- **Coverage gaps** (Section 3): 10, of which 3 are major for the book's stated scope (P1, P2, P6).

### Web sources consulted (leads; 2026 dates mostly from secondary trackers)

- https://jobsecuritymeter.com/guides/frontier-ai-models-2026
- https://www.swfte.com/blog/april-2026-ai-model-releases-roundup
- https://datalakehousehub.com/blog/ai-model-families-2026/
- https://slash-digital.io/en/insights/ai-models-2026/
- https://lilting.ch/en/articles/deepseek-v4-preview-1m-context-csa-hca-moe
- https://www.bestblogs.dev/explore/topics/deepseek-v4-preview-release
- https://openrouter.ai/qwen/qwen3.6-plus
- https://medium.com/@mlabonne/qwen3-5-nobody-agrees-on-attention-anymore-4709e1bd014b (title and snippet only; the page was blocked)
- Book evidence log: /home/user/FutureOfAI/textbook/work/evidence-ch03.md, lines 239–249
