# Panel 2: senior ML researcher (ch2, ch4, ch12) — all worked examples recomputed and correct; quality high
[CERTAIN] = sure; [VERIFY] = reader's recollection, must be checked against primary sources before changing.

## ch02
- [CERTAIN, outdated] ReLU "default recommendation" (2016): add that transformer LLMs use GELU (BERT/GPT-2) and gated variants such as SwiGLU (Shazeer 2020; used in PaLM, Llama) — verify.
- [CERTAIN, outdated] "No optimiser dominates… user's familiarity": add that AdamW is the de facto standard for LLM pre-training; newer optimisers such as Muon used at scale (e.g. Kimi K2 technical report, 2025) — verify.
- [CERTAIN] post-LN "LayerNorm(x + Sublayer(x))" in the original design: add that current models use pre-norm, usually RMSNorm (Zhang & Sennrich 2019; Llama) — verify.
- [CERTAIN, misleading] "every block passes the error signal through at least unchanged along the shortcut path": gradient is g·(I + ∂F/∂x) — say "provides an identity path for the gradient"; note the original ResNet applies ReLU after the addition.
- [CERTAIN] 6N/2N per token: note attention cost grows with context length and embeddings are excluded (Kaplan's assumption d_model ≫ n_ctx/12); add inference ≈ 2N FLOP per token.
- [CERTAIN, dated] hardware example only H100: mention Blackwell (B200/GB200) as current generation in one sentence (Chapter 7 has specs).
- Missing (add briefly where it fits, verified): automatic differentiation/computational graphs; mixed precision (bf16/FP8, Chapter 7); gradient clipping; cosine and warmup-stable-decay schedules; inverted dropout and that dropout is largely absent from LLM pre-training (if verifiable, e.g. Llama/GPT-3 papers); implicit regularisation of SGD (one sentence, cited).
- [VERIFY] "millions of bank cheques a month" — LeCun 1998 may say "several million checks per day" (first fact-check recorded both phrases; check exact wording and context).
- [VERIFY] LeNet-5 "345,308 connections" (paper's figure vs reader's 340,908 sum) — use the paper's number if that's what it says.
- Prose: garbled sentence "some functions computable by a network of a given depth need a shallower network whose number of hidden units is exponential" → "…would need, in a shallower network, exponentially many hidden units"; ReLU 0.2/−0.3 example appears three times — cut the last; "X, not Y" closers.
- Minor: class-3 probability "0.099" vs "0.0986" — make consistent.

## ch04
- [CERTAIN] Astra consistency with ch12 (see audit-consistency2 T-07).
- [CERTAIN] "the largest of its Llama 3 language models" vs "Llama 3.1 405B": 405B was released as Llama 3.1 (July 2024) — name consistently.
- [CERTAIN] 6ND caveat (attention, embeddings) and inference ≈ 2N per token so the over-training argument rests on a stated formula; memory-bound decoding (Chapter 3).
- [VERIFY] "175-billion-parameter model… more than 4.2 trillion tokens with 4.41 × 10^24 FLOP" — check Chinchilla Table 3 (approach 1 vs 2) and state which.
- [VERIFY] GPQA Diamond "expert validators score 81.2%" (AI Index) vs GPQA paper (experts 65%/74%; OpenAI's 69.7%) — check and clarify which baseline.
- [VERIFY] R1-Zero 15.6%→77.9% (Nature) vs 71.0% (arXiv v1) — state version (ch03 already does).
- [VERIFY] GSM1k "Spearman rank correlation 0.36" and "1,205" problems — fact-check 2 changed r² to rank correlation; recheck.
- [VERIFY] ARC-AGI-1 costs $26 / $4,560 per task — revised by ARC Prize (already noted?).
- [VERIFY] OLMo 3.1 "nearly 90 times fewer parameters than Grok 4" — Grok 4 size undisclosed: say estimate or cut.
- Missing (brief, verified): pre-Kaplan scaling-law history (Hestness et al. 2017; Rosenfeld et al. 2019); MoE scaling laws (Clark et al. 2022; Krajewski et al. 2024); precision scaling laws (Kumar et al. 2024); distillation; MFU vs HFU; that the Astra estimate's MFU assumes a stated peak precision.
- Prose: garbled "Pre-training sequences of language models, they confirmed collapse under replacement"; repeated numbers in debate boxes (GPT-4.5 3.8×10^26, ARC "175 times", HLE 13.4%→54.8%); "X, not Y" closers; template debate endings.

## ch12
- [CERTAIN] Astra/ExploitGym/training-pause consistency with ch04; source the NIST "CAISSI" styling and EO 14434 (ch13 verified EO 14434 on govinfo; fact-check 1 saw the NIST header) — keep precise and cited.
- [CERTAIN, oversimplified] specification vs generalisation mapped onto "outer and inner alignment": inner alignment is about learned (mesa-) objectives (Hubinger et al. 2019); add goal misgeneralisation (Langosco et al. 2022; Shah et al. 2022) — verify.
- [VERIFY] Meinke et al. "gave five frontier models goals" — reader recalls six models tested, five schemed; check.
- [Minor] Table 12.1 "long, garbled text" vs short telegraphic quoted example — align description with the source (fact-check 2 said Stiennon App. H.2 calls them "long, low quality").
- Missing (brief, verified): RL with verifiable rewards as main locus of reward hacking (link to Chapter 3); gradient-based jailbreaks (GCG, Zou et al. 2023) and many-shot jailbreaking (Anil et al. 2024) — conceptual only; linear probes for deception (e.g. Goldowsky-Dill et al. 2025 or similar, verify); unlearning and pre-training data filtering (e.g. WMDP Li et al. 2024; O'Brien et al. 2025 "Deep Ignorance"); tamper resistance (TAR, Chapter 7 cross-ref); representation engineering / persona vectors (Zou et al. 2023 RepE; Chen et al. 2025) — conceptual only, no operational misuse detail.
- Prose: run-on "Nothing in this objective says… labellers; Stiennon and colleagues used 64,832…" → split; "X, not Y" closers; "The approach works." verdicts.
Keep: one-weight descent/curvature; nine-parameter backprop box; Adam scale invariance; He init arithmetic; 6ND reconciliation; Chinchilla fitted loss; Besiroglu; Schaeffer p^L; Large Language Monkeys coverage vs selection; Gao curve; evaluation-awareness counterfactual; AI control table; "Faithfulness … is not the same as monitorability"; SAE limits.
