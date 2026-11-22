# Third review: Chapter 4 — Scaling, Compute and the Limits of Progress

(Interim save; being completed.)

## Working notes (to be folded)
- Epoch trends dashboard now "Updated Nov. 5, 2026"; 5x, 5.2 mo, 10,000x, 3.5x cost, 1.49x, 30% inference, ECI 14 vs 6 unchanged; "installed stock 3.4x/yr since 2022" no longer on dashboard (replaced by "New compute growth 2.5x/yr" since 2024). -> MUST (line 120, bib).
- ClockBench now led by Claude Fable 5.2 Max 87.8%; Gemini 4 Carbon High 85%; Argon 83.3% -> MUST (line 229).
- HLE: Scale leaderboard still GPT 6 Astra 54.8 (+-1.94) top on 22 Nov. Vendor with-tools scores higher (Fable 5.1 65.0%), so "best reported scores ... 54.8%" (line 258) is wrong.
- ARC o3 table: $26 / $4,560 per task, notes 3/24/2025 (o1-pro) and 12/10/2025 (o3-pro $80/M) confirmed; bib howpublished lacks Dec 2025 revision.
- METR YAML and page confirmed (all values; 8 Sep 2026; 16 h notice May 8 2026; regularisation fix 3 Mar 2026).
- Epoch CSV confirmed: Table 4.3, Fig 4.2 values, GPT-4.5 note, Astra note, DeepSeek-V3, Gopher A26.
- Chinchilla Table 3/A3: 175B -> 3.7T (approach 1), 4.3T (approach 2), 12.0T (approach 3); main text "over 4.2 trillion tokens" with 4.41e24 FLOP. Book line 82 "3.7 trillion to 4.2 trillion depending on the method" wrong.
- Villalobos: cites Muennighoff 3x-15x but "we reduce it to 5x" (upper extreme). Book line 153 says assume 3-15x.
- Confirmed (papers): Ho NeurIPS 90% CI 2-22 mo (neurips.cc), 7.2x; GSM1k 1205, up to 8%, r2=0.36; Besiroglu 600,000/500, Borgeaud, fit values, ~20 tokens/param; Kaplan all; Cottier all; GPQA 81.2 / 65; Brown all; Muennighoff all; Kwa v1 50 min; Kumar, Sardana, Khatri, s1, Qwen3, DSV3.2, Singh, Snell, Ruan, Du, Sevilla 2022, Porian, Pearce, Ludziejewski, Clark; Llama 3 all; GPT-4 quotes; PaLM; DSV3; R1 800k; Wei; Schaeffer; Gerstgrasser; AI Index 2026 (3.3x,17.1M, disclosure, synthetic, GPQA, saturated, ClockBench Mar 50.6%).
- Truong: "up to 84%" of 50 = 42 questions; consistent with book's 42; min not verifiable from text.
- RuntimeWire GPT-6 Pro parallel agents 16 Oct 2026 confirmed (+ mixed-news).
