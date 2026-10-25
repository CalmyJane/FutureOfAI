# Reader panel: Jonas (CS master's) on ch3–5 — claims below are a reader's recollection: VERIFY before changing

Likely errors:
- ch4: savings-account analogy ("fixed percentage of interest: every step brings a smaller absolute gain") is backwards: compound interest brings LARGER absolute gains. Replace analogy (e.g. each extra decimal place of accuracy costs as much as all previous ones).
- ch4: Llama 3 405B "about 38 tokens per parameter" presented as over-training, but Meta's own fit gave 402B on 16.55T (~41 tokens/param), so 405B was near Meta's own optimum; Llama 3 8B on ~15T tokens (~1,900/param) is the over-training example. Verify against Llama 3 report.
- ch3: position information: original transformer/GPT-2 add position embeddings; Llama-style models use rotary embeddings (RoPE) inside attention. Mention both.
- ch3: with the causal mask a token also attends to itself ("every earlier token j", "only at tokens before it" → "itself and earlier tokens").
- ch3: "far less data … changes behaviour more than knowledge": qualify for 2025–26 reasoning models whose RL post-training uses a large share of compute (verify a source, e.g. DeepSeek-R1, Epoch, OpenAI o3 statements).
- ch4: OLMo 3 "through … curation of its training data alone": check; RL post-training also matters.
- ch4: Humanity's Last Exam "about 2,700 questions" (final set ~2,500?) and top score 38.3% (possibly outdated) — verify as of Oct 2026 from the AI Index 2026 or the HLE site, state date.
- ch5: OSWorld "within about six percentage points of human baseline" — verify latest (OSWorld-Verified); tau-bench "no model above 71%" — specify version/domain (τ-bench vs τ²-bench).
- ch5 vs ch4 inconsistency on METR: ch5 says ~50 minutes, doubling ~7 months, error bars ~factor of two; ch4 uses TH 1.1 (~60 min for Claude 3.7 Sonnet, ~4 months since 2023, Opus 4.6 CI 5–61 h). Make ch5 consistent with ch4.
- ch5: CaMeL "published in 2026" (IEEE SaTML 2026 — fact-checker confirmed) — fine, but "provable security guarantees" apply only to specific attack classes; say so.
- ch5 deeper box: pass^k: attempts are independent given the task; heterogeneity across tasks makes real pass^k higher than p^k on average (Jensen). Fix wording.
- ch4: Ho et al. algorithmic progress CI: chapter says 90% CI 2–22 months; ch14 says 95% CI ~5–14 months. Verify against Ho et al. (NeurIPS 2024) and make ch4/ch14 consistent.
- Minor: "two decimal numbers" → floating-point numbers; "a model never meets a word it cannot represent" true for byte-level BPE only.
Keep: author-computed tables, "errors produced by the same mechanism", MoE active-parameter advice, "filled-in order form", lethal trifecta, Kalai singleton argument, Llama 3 case study, Epoch confidence bands, pass@k vs pass^k.
Slow: ch5 §5.4 payments and §5.7 economic agents (citation per sentence); ch4 §4.7 run of "The 2026 AI Index reports…".
Style: analogy-then-limit template; every debate box ends "What would settle it?" (fine as a feature, but vary phrasing); repeated hedges; same citation 3× in one paragraph ([@anthropic2025project], [@hadfield2025economy], [@tomasev2025virtual]) — cite once per paragraph where possible.
