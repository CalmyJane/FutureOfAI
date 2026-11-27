# Review 9: Chapter 7 (Chips, Data Centres, Energy and Open Models)

## Verdict
Ready to print after one small currency fix. The chapter is accurate, carefully hedged and well sourced. Every worked calculation I recomputed is correct. The 2026 material I checked (the Huang resignation, the Fable 5/Mythos 5 episode, the 19 November remote-access rule, the Affiliates-rule extension, the Chinese minerals extension, Nvidia's Q3 FY2027 China figure, and the Kimi K3, Qwen3.8, Muse Spark Open, GLM-5 and DeepSeek-V4-Pro specifications and licences) matches primary or reputable secondary sources. I found nothing defamatory.

**Balance between companies.** This is handled well in both directions. Amodei's pro-control statements come with a note that Anthropic competes with Chinese developers and lobbies for controls (l.142, l.255). Huang's opposing view comes with a matching conflict note. The chapter treats Google's per-prompt measurement ("cannot be checked from outside"), Altman's 0.34 Wh ("without describing the method") and OpenAI's gpt-oss safety evaluation ("a developer's evaluation of its own product") with the same scepticism. The Anthropic export-control episode is reported neutrally. The prompt-caching sentence (l.51) gives only Anthropic's marketing figure, but it is clearly attributed ("Anthropic, for example, says") and names OpenAI and Google as offering the same feature. This is acceptable, and the report does not raise it as an item.

## MUST change before printing
None.

## SHOULD change

### S1. Nvidia has since stopped shipping licensed Hopper products to China
- Where: textbook/chapters/ch07.md:132
- Text now: "Its outlooks for the following quarters assumed no data-centre compute revenue from China, although in the quarter to October 2026 it shipped $2.4 billion of Hopper data-centre products there [@nvidia2026nvidia; @nvidia2026q3cfo]."
- Problem: OUTDATED (incomplete). On the Q3 FY2027 earnings call (17–18 November 2026), interim CEO Colette Kress said the company had already stopped shipping licensed Hopper products to China. Without that, a reader may infer that the $2.4 billion is a continuing flow.
- Evidence: Q3 FY2027 earnings call transcript, https://www.nasdaq.com/articles/nvidia-nvda-q3-2027-earnings-call-transcript, and coverage at https://fourweekmba.com/ai-nvidia-ends-licensed-china-hopper-sales-2-4b-last-quarter/ ("Nvidia Ends Licensed China Hopper Sales: $2.4B Last Quarter"), November 2026. The CFO commentary says that "Data Center Hopper shipments to China in the quarter were $2.4 billion".
- Change to: "Its outlooks for the following quarters assumed no data-centre compute revenue from China. In the quarter to October 2026 it shipped $2.4 billion of Hopper data-centre products there, but it said in November that it had stopped shipping licensed Hopper products to China [@nvidia2026nvidia; @nvidia2026q3cfo; @nasdaq2026nvidiaq3]."
  New bib entry (ch07.bib):
  ```
  @misc{nasdaq2026nvidiaq3,
    author       = {{Nasdaq}},
    title        = {{NVIDIA} ({NVDA}) {Q3} 2027 Earnings Call Transcript},
    year         = {2026},
    howpublished = {Earnings call transcript, 18 November 2026},
    url          = {https://www.nasdaq.com/articles/nvidia-nvda-q3-2027-earnings-call-transcript},
    urldate      = {2026-11-27}
  }
  ```

### S2. The NTIA quotation drops its second half
- Where: textbook/chapters/ch07.md:311
- Text now: "the US National Telecommunications and Information Administration concluded that "current evidence is not sufficient to definitively determine" that restrictions on open-weight models were warranted"
- Problem: UNCLEAR / slightly one-sided. The NTIA sentence is symmetrical: it says current evidence is not sufficient to determine "either that restrictions on such open-weight models are warranted, or that restrictions will never be appropriate in the future". The book quotes only the first half, inside the "for openness" case. The words quoted are accurate, but the cut makes NTIA sound more pro-openness than it was.
- Evidence: NTIA, *Dual-Use Foundation Models with Widely Available Model Weights*, July 2024, executive summary (the wording above).
- Change to: "the US National Telecommunications and Information Administration concluded that "current evidence is not sufficient to definitively determine either that restrictions on such open-weight models are warranted, or that restrictions will never be appropriate in the future", and recommended that government "actively monitor" risks instead [@ntia2024dual]."

## Could not verify
- Microsoft FY2026 cash capex of $115.9 bn (Table 7.4). The $329.1 bn of uncommenced leases is confirmed (BTW Media, citing the 10-K). I did not see the capex line itself. Reuters notes a lease-accounting change, so the author should check the figure against the 10-K cash-flow statement.
- The 2026 AI Index figures (17.1 million H100e, the Arena gaps of 174/7/49 points, $285.9 bn vs $12.4 bn, 91.2%, Grok 4 at 73,000 t). I did not open the report; ch04 gives the same figures.
- ASML's "327 lithography systems" and "29.1%". The press reports ~29% (€9.5 bn) and 48 EUV units; I did not see the exact decimals.
- The EU's November 2025 extension of Dutch DUV licence requirements to all member states (sourced to ASML's annual report only).
- The specific IEA *Key Questions* numbers (485 TWh, 45 GW of SMR agreements, $715 bn, $3.9 tn); I took these as cited.

## Checked and confirmed
- Arithmetic: DeepSeek-V3 compute 6×37e9×14.8e12 ≈ 3.29e24; ridge point 990/3.35 ≈ 295 ops/byte; 140 GB/3.35 TB/s ≈ 42 ms (21 ms split across two GPUs); the format maxima in Table 7.1 (FP32 3.40e38, BF16 3.39e38, FP16 65,504, E4M3 448, E5M2 57,344); NVLink 900/128 ≈ 7×; H100 TPP 1,979×8 ≈ 15,800, density ≈ 19.4/mm²; B200 derivations (36/2/8 = 2.25 PF, 1,440/8 = 180 GB, 64/8 = 8 TB/s); Ironwood 9,216×4,614 TF ≈ 42.5 EF ≈ 24× El Capitan's 1.742 EF; Arena 49 points → 57%; DeepSeek $5.576 m and R1 $294k; 340 TFLOPS ≈ ⅓ and ⅙ of peak; PUE 1.6→1.2 = −25%; capex percentages in Table 7.4; LBNL 176 vs IEA 154 = +14%; Luccioni image/text ≈ 62×; Nvidia data-centre revenue $47.5 bn → $193.7 bn ≈ 4×.
- Huang's resignation on 11–12 November 2026 (Nvidia 8-K) and his May 2025 "failure" remark.
- The Fable 5/Mythos 5 timeline: 12 June letter, 26 June partial relief for Mythos 5, 30 June lift with conditions (Mayer Brown, Axios, TechCrunch, Al Jazeera). The text matches ch13.
- The BIS remote-access IFR: published 19 November 2026; rescinds the diffusion rule and the model-weights control; D:5 and Macau HQ test; adds Indonesia, Malaysia, Singapore, Thailand and Brazil (BIS, WilmerHale, Wiley).
- The Affiliates-rule suspension extended to 10 January 2027 (FR doc 2026-22793, 9 November 2026).
- China's extension of the gallium/germanium/antimony ban suspension to 27 January 2027, with licensing remaining (VOA, 26 November 2026).
- The Nvidia FY2026 figures ($215.9 bn, $193.7 bn), the H20 $4.5 bn charge, ~$60 m licensed revenue and the 15% arrangement.
- Amodei's quotations, word for word (darioamodei.com).
- Kimi K3 (2.8T/104B, MXFP4 with QAT from SFT, Kimi K3 License with a $20 m threshold and display clause); Qwen3.8-Max licence ($50 m threshold); Muse Spark Open (15 October 2026, 816B/42B, $20 m, BF16 and NVFP4); GLM-5 and DeepSeek-V4-Pro specifications and MIT licences; gpt-oss specifications.
- Google's 2026 environmental report: +37% electricity, market-based 2.8 Mt vs location-based 15.1 Mt, water +34% (10.9 bn gal ≈ 41 bn L).
- Lermen ($200, one GPU), Qi (10 examples, < $0.20), Jouppi (15–30×; 1.2–1.7×), Gholami (3.0/1.6/1.4×), FP8 paper (175B), DeepSeek FP8 (14 bits, < 0.25%), the Nvidia–OpenAI LOI wording, the Nvidia share fall on 27 January 2025.
- Cross-references to Sections 2.6, 4.1 and 4.4, Table 4.3, Chapter 12 (12.3) and Chapter 13 resolve correctly. The ch03, ch04, ch13 and ch14 versions of the same facts agree with ch07.

## Tally
Claims checked: ~80 · confirmed: ~72 · wrong: 0 · outdated/incomplete: 1 · misleading by truncation: 1 · not verified: ~7
