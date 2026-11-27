# Review 7: Chapter 7 (Chips, Data Centres, Energy and Open Models)

## Verdict

Ready to print, with one small wording fix suggested. I found no factual errors, misquotations or legally risky statements. The chapter is dense but carefully sourced. The 2026 material holds up against current sources: the Anthropic Fable 5/Mythos 5 export-control episode, the November 2026 remote-access rule, Jensen Huang's resignation, Nvidia's Q3 FY27 China shipments, the gallium/germanium extension and the Muse Spark Open, Kimi K3 and Qwen3.8 licences. I recomputed every worked example and arithmetic claim and all of them hold.

## MUST change before printing

None.

## SHOULD change

### S1. Date logic of the Affiliates-rule extension
- Where: textbook/chapters/ch07.md:133
- Text now: "On 9 November 2026, the day the suspension of the ownership rule had been due to lapse, BIS extended it through 10 January 2027 [@bis2026extension]."
- Problem: UNCLEAR. The one-year suspension took effect on 10 November 2025, and the rule was due to come back into force on 10 November 2026. Law-firm alerts give that date, and so does the Dechert entry already in ch07.bib: "November 10 Reimposition Remains Scheduled". 9 November is the Federal Register publication date. The rule itself was released earlier: Reed Smith's alert is dated 6 November, and others say the rule was published 5 November, which probably means public inspection. So "the day the suspension had been due to lapse" is off by a day, or more if the public-inspection date is used.
- Evidence: https://www.reedsmith.com/our-insights/blogs/trade-compliance-resource-hub/5272/bis-further-suspends-affiliates-rule-until-january-2027/ (6 Nov 2026): the suspension is extended "until January 10, 2027". The Lowenstein/Thompson Hine alerts: "In a final rule published on November 5, 2026 ... further stayed its 'Affiliates Rule,' which would otherwise have taken effect on November 10, 2026, until January 10, 2027." (Dechert, 28 Oct 2026, already in ch07.bib as dechert2026bis).
- Change to: "In a rule published on 9 November 2026, the day before the ownership rule was due to come back into force, BIS extended its suspension through 10 January 2027 [@bis2026extension]."

### S2. Huang's title in a 2025 quotation (optional clarity)
- Where: textbook/chapters/ch07.md:142
- Text now: "Jensen Huang, Nvidia's chief executive until his resignation in November 2026, whose company had lost much of its Chinese market, called the controls "a failure" in May 2025"
- Problem: UNCLEAR, not wrong. The resignation is confirmed: the Nvidia 8-K of 11 November 2026 says the board accepted his resignation, effective immediately, and named Colette Kress interim CEO. But the long apposition makes the sentence hard to parse. Section 7.5 already uses "its then chief executive". The fact is unsourced here, so cite the 8-K if it is kept.
- Evidence: https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvda-20261111.htm (Nvidia Form 8-K, 11 Nov 2026).
- Change to: "On the other side, Jensen Huang, then Nvidia's chief executive, whose company had lost much of its Chinese market, called the controls "a failure" in May 2025, according to Reuters, ..." This keeps the rest of the sentence and drops the resignation clause. Alternatively, keep the clause and add a bib entry: `@misc{nvidia2026ceo, author={{NVIDIA Corporation}}, title={{Form 8-K}: Current Report, {November} 11, 2026}, year={2026}, howpublished={Filed with the U.S. Securities and Exchange Commission}, url={https://www.sec.gov/Archives/edgar/data/1045810/000104581026000082/nvda-20261111.htm}, urldate={2026-11-27}}`.

## Could not verify

- l.124: Nvidia revenue from customers headquartered in China, "$25.0 billion in fiscal 2025 to $19.7 billion in fiscal 2026". The parts of the 10-K I could read give only the non-US share (31% / 41%). The figure is plausible but unconfirmed.
- l.102: "memory prices rose by an order of magnitude between late 2024 and early 2026" (IEA). The IEA site returned 403, so I could not check the wording.
- l.104, 189, 191, 193 and l.234: other IEA *Key Questions* section-level figures (helium, turbine lead times, the 20 blocked projects, 15–27 GW, 45 GW SMR, $715 bn). The headline figures (17%, 485 TWh, 50%, 950 TWh, ~3%) are confirmed by the IEA press release.
- l.57: "Nvidia said in August 2026 that the Vera Rubin platform was in full production". Nvidia already said this in January 2026, so the sentence is not wrong, only late.
- l.72: LBNL's "74% of rated power" for H100 training servers.

## Checked and confirmed

- Alberta: >16 GW of requests and a 1.2 GW interim cap (AESO, June 2025). TMI/Crane unit is ~835 MW.
- H100 specs: 80 bn transistors, 814 mm², 4N, 132 SMs / 528 tensor cores, the MMA quotation, 5 HBM3 stacks / 5,120-bit interface, 3.35 TB/s, 700 W vs 400 W. NVLink 900 GB/s = 7× PCIe Gen5. FP8 quotation ("halves data storage requirements and doubles throughput...").
- TPU 15–30×, the "triple" memory estimate, TPU v4 1.2–1.7× vs A100. Gholami's 3.0×/1.6×/1.4× per two years.
- Table 7.1: all largest normal values recomputed (3.40e38, 65,504, 3.39e38, 448, 57,344).
- Arithmetic: 6×37e9×14.8e12 ≈ 3.3e24. 990/3.35 ≈ 300 FLOP/byte. 140 GB / 3.35 TB/s ≈ 42 ms (21 ms split). 70B at 4 bits = 35 GB. TPP 1,979×8 ≈ 15,800 and ~19/mm². 2.788 M × $2 = $5.576 M. 3.3e24 / 9.59e9 s ≈ 344 TFLOPS. 49 Elo points → 57%. PUE 1.6→1.2 = −25%. 176/154 = +14%. Table 7.4 growth rates (+59%, +79%, +74%, +87%). Nvidia data-centre revenue 47.5 → 193.7 ("quadrupled").
- Table 7.2 B200 per-GPU figures (HGX/DGX ÷ 8, sparse ÷ 2). Ironwood 2,307/4,614 TFLOPS, 192 GB, 7.37 TB/s, 9,216 chips. Ironwood's 24× El Capitan claim against El Capitan's 1.742 EF HPL figure.
- DeepSeek-V3: FP8 "extremely large-scale" claim, ~14-bit accumulation, <0.25% relative error, 2,048 H800s. R1 Nature SI: 147k GPU-hours / $294k, A100 use.
- GPTQ and AWQ quotations. gpt-oss: 117 B / 5.1 B active, 80 GB / 16 GB, and the abstract's "trained using large-scale distillation and reinforcement learning". Gemma 3 distillation. Speculative decoding 2–3×. Prompt caching 90% / 85%.
- ASML: "only manufacturer of EUV", 327 units in 2025, China 29.1% of 2025 net sales (36.1% in 2024), from the 20-F text.
- Nvidia 10-K: $215.9 bn revenue. H20 licences in August 2025, ~$60 M of revenue, $4.5 bn charge, the 15% expectation "but no regulation codifying this", direct customers at 22% / 14%, CoWoS.
- Nvidia Q3 FY27: $2.4 bn of Hopper products shipped to China, and an outlook assuming no China data-centre compute revenue.
- Anthropic Fable 5 / Mythos 5: 12 June licence requirement, worldwide shutdown, partial Mythos release on 26 June, lifted with conditions on 30 June (Mayer Brown, GT, Axios, Al Jazeera).
- BIS "Addressing Remote Access to Advanced Semiconductors" IFR: formal rescission of the diffusion rule and its weight controls, the remote-access licence requirement, and the five countries Indonesia, Malaysia, Singapore, Thailand and Brazil (WilmerHale, GT).
- China's mineral-ban suspension extended on 24 Nov 2026 to 27 Jan 2027, with licences still required (VOA).
- Nvidia–OpenAI LOI. $30 bn of a $110 bn round. Huang's "probably not in the cards" (4 March 2026).
- Ireland 23% of metered electricity in 2025 (CSO). LBNL 2025 Update: 649 TWh, 11.8%, 521–843 TWh.
- Google 2026 report: electricity +37%, water +34% (10.9 bn gal ≈ 41 bn L). Rosa et al. ES&T, 9,347 sites. IEA *Powering AI*: ~34% of capacity, "nearly 40%" in the summary.
- AI Index 2026: $285.9 bn US vs $12.4 bn China.
- Table 7.5 licences checked against the licence texts: Qwen3.8-Max ($50 M per 12 months MaaS/assistant threshold, display rule), Kimi K3 ($20 M MaaS threshold, "Kimi K3" display), Muse Spark Open (816 B / 42 B, $20 M, attribution, "top open weights model outside China"). Kimi K3 2.8 T / 104 B with MXFP4 QAT from SFT. Qwen3.8 2.4 T / 95 B.
- TAR "hundreds of steps of fine-tuning". Lermen's "$200 / one GPU". Qi's 10 examples / $0.20. Kapoor (25 authors). Sastry (19 authors) and its quotations.
- Cross-references: §4.1 compute rule and the 3.3e24 figure, Table 4.3 ($388 M for Grok 4), Chapter 4 on quantisation and data (Kumar et al.) all match ch04.

## Tally

Claims checked: ~120 · Confirmed: ~112 · Wrong: 0 · Imprecise: 1 (S1) · Outdated: 0 · Could not verify: ~7
