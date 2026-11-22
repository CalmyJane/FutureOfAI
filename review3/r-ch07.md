# Third review: Chapter 7 — Chips, Data Centres, Energy and Open Models

STATUS: FIRST VERSION (work in progress, 11 Nov 2026). Full read of chapter, bib, figure specs, plotting script and glossary done; all arithmetic recomputed; web verification is in progress and sections below will be filled in as it proceeds.

## Verdict
(pending completion of web checks)

## MUST change before printing

### M1. Affiliates-rule suspension was extended on 9 Nov 2026; the text and Figure 7.2 caption still say it was due to lapse (DRAFT - wording to be finalised)
- Where: textbook/chapters/ch07.md:133 and :116 (Figure 7.2 caption); also textbook/figures/specs/fig-07-02.md
- Text now (l.133): "As of late October 2026, however, BIS had not published a rule extending the suspension of the ownership rule, which was due to lapse on 9 November 2026, with the restrictions returning on 10 November [@bis2025one; @dechert2026bis]."
- Text now (l.116): "As of late October 2026 the one-year stay of the Affiliates rule was due to end on 9 November 2026."
- Problem: OUTDATED. BIS filed a final rule on 5 Nov 2026, published 9 Nov 2026 (91 FR 70789, FR Doc. 2026-22793), "Extension of the Suspension of Expansion of End-User Controls for Affiliates of Certain Listed Entities": "The suspension was set to end November 9, 2026. This final rule extends the suspension through January 10, 2027." China announced the matching two-month extension of its side of the truce on 9 Nov 2026 (to 10 Jan 2027).
- Evidence: https://www.federalregister.gov/api/v1/documents/2026-22793.json (title, citation 91 FR 70789, abstract as quoted); https://sanctionsnews.bakermckenzie.com/bis-extends-suspension-of-the-affiliates-rule-through-january-10-2027/ ; https://www.thenationalnews.com/news/us/2026/11/09/china-extends-pause-on-rare-earth-export-curbs-for-two-months/ ("The extension runs to January 10, according to the ministry").
- Change to: see final wording below (to be completed).

## SHOULD change (real but not blocking)
(to be filled)

## Could not verify
(to be filled)

## Reader notes
(to be filled)

## Checked and confirmed

### Arithmetic recomputed (all agree with the text)
- l.9: 6 x 37e9 x 14.8e12 = 3.29e24 FLOP ("about 3.3 x 10^24") OK.
- l.21: 990 TFLOPS / 3.35 TB/s = 296 ops/byte ("roughly 300") OK; 70e9 x 2 bytes = 140 GB OK; 140 GB / 3.35 TB/s = 41.8 ms ("about 42") OK; half = 20.9 ms ("about 21") OK.
- l.47: 70e9 x 0.5 byte = 35 GB OK.
- l.55: 900 / 128 = 7.03 ("seven times") OK.
- Table 7.1: FP32 max 3.40e38, FP16 65,504, BF16 3.39e38, E4M3 448 (with the all-ones mantissa at top exponent reserved for NaN, per the FP8 paper), E5M2 57,344: all OK.
- Table 7.2: 1,440 GB / 8 = 180 GB; 64 TB/s / 8 = 8 TB/s; 1,979 / 2 = 990 OK.
- l.74: 193.7 / 47.5 = 4.08 ("quadrupled", l.240) OK.
- l.122: TPP = 2 x 989.5 x 8 = 15,832 ("about 15,800") OK; 15,832 / 814 = 19.4 ("about 19") OK.
- l.161: 176 / 154 = 1.143 ("about 14% above") OK; 580 / 325 = 1.78 ("almost twice") OK.
- l.182: 2.9 / 0.047 = 61.7 ("more than 60 times") OK.
- l.184: 1 - 1.2/1.6 = 25% OK.
- l.217: 2.664M + 0.124M = 2.788M; x $2 = $5.576M OK.
- l.219: 2.664M h x 3600 = 9.59e9 GPU-s OK; 3.3e24 / 9.59e9 = 344e12/s ("about 340 trillion") OK; 344/990 = 0.35 ("about a third"), 344/1,980 = 0.17 ("a sixth") OK.
- Table 7.4: +59%, +80% (79.4), +74%, +87% OK.
- l.254: 147,000 x $2 = $294,000 OK.
- l.292: Elo, 49 points -> 1/(1+10^(-49/400)) = 57.0% OK.
- l.324: 3.3e24 / 1e25 = 0.33 ("a third") OK.
- Fig 7.4: 416-183-102-68 = 63; 945-426-277-114 = 128 OK (matches figs_ch07.py).
- Fig 7.3 values in figs_ch07.py (360, 416, 485, 833, 868, 945, 1,008) match the text at l.151-153.

## Tally
(pending)

## WORKING NOTES (to be merged into the sections above in the final version)

Confirmed so far against opened sources (11 Nov 2026):
- IEA Key Questions (full PDF text read, mirror at regie-energie.qc.ca): Alberta 16 GW / 1.2 GW cap (sec. 3); TMI ~835 MW (sec. 5.1); +17% 2025, AI-focused +50%; 485 -> 950 TWh, ~3%; AI-focused tripling; 1.5% and 20-30% local (sec. 3); packaging 2025 / memory H2 2025; <150 GB 2023 -> >1,000 GB 2027; HBM 3x wafer capacity; memory prices up an order of magnitude late 2024-early 2026; "through at least the end of 2027"; helium Box 1.1 (Qatar ~one-third; no substitute); transformers 2-3 years, gas turbines ~5 years; turbine orders +70%; 20 projects / USD 98bn Q2 2025; 5-10 year grid waits; "not a reliable indicator..." (Box 1.2); ~40% of corporate renewable PPAs; 15-27 GW onsite gas; SMR 45 GW, "less formal off-take arrangements" (p. 64, which is sec. 7.3 not 5.1); ~350 Mt in 2035, ~2%; capex USD 715bn, +75%, > US energy sector 2024 (slightly < USD 600bn); "absorb almost all cash generation in 2026"; ~USD 200bn debt in 2025; USD 3.9tn 2026-2030; "too large to be funded solely from the balance sheets of AI companies"; "running ahead of AI monetisation"; threefold users / fivefold revenue; 30-40% perf/W; PUE 1.1-1.2 vs 1.5-1.7, 1.6->1.2 = one-quarter; Jevons; video "hundreds to thousands of times more energy"; "by at least an order of magnitude annually"; "compute-constrained..." and "overtook..." (Box 10.1); "slightly less than 10%" of demand growth; Table A.1 (360/416/485; 833/868/945/1,008) and Table A.4 (US 154/183/426; China 102/277; Europe 68/114; world 416/945).
- IEA Powering AI (PDF, created 14 Oct 2026): "around 34% of identified capacity ... September 2026" (p. 31), "nearly 40%" (p. 9), cooling-system caveat; G7 France.
- LBNL 2024 report (PDF): ~60 TWh 2014-16; 176 TWh, 4.4% in 2023; 325-580 TWh, 6.7-12.0% in 2028; "the lack of data availability significantly limits..."; 8 H100 GPU nodes averaged 74% of rated TDP; inference "nearly 60%" of AI server energy 2023; water 21.2bn L 2014, 66bn L 2023, hyperscale 60-124bn L 2028.
- LBNL 2025 Update (eta-publications.lbl.gov, June 2026): 649 TWh reference, 11.8%, bounds 521-843 TWh, 9.5-15.3%; author list matches bib.
- CSO Ireland (7 July 2026): 23% in 2025, 5% in 2015.
- AI Index 2026 (PDF): 17.1M H100e, 3.3x/yr since 2022; Nvidia >60%, Google and Amazon; "fabricates virtually every leading AI chip, including Nvidia's Blackwell GPUs and AMD's MI300X"; high barriers at every layer; ASE/Amkor; HBM makers SK Hynix, Samsung, Micron; 91.2% industry; OpenAI 20, Google 14, Alibaba 11; US 5,427 data centres, >10x; AlexNet 0.01 t; Grok 4 72,816 t (text "about 73,000"); DeepSeek-V3 597 t; GPT-4o 0.42 Wh short query; water 1.3-1.6 million kL, 1.2 million people; "has effectively closed"; Arena gap 174 (May 2023) -> 7 (Aug 2024) -> 49 (Mar 2026, Claude Opus 4.6 1,503 vs GLM-5 1,454); "AI sovereignty emerged as a central organizing principle"; $285.9bn vs $12.4bn.
- Google 2026 Environmental Report (PDF): electricity +37%; scope 2 market-based -3% to 2,815,000 t; location-based 15,148,700 t vs 5,173,000 t in 2019 (2.93x); water 10.9bn gal = 41bn L, +34%. Google 2025 report: Waltham Cross air cooling.
- ASML 2025 annual report (strategic + financial sections): 327 lithography systems, 48 EUV; China 29.1% of 2025 total net sales vs 36.1%; Zeiss sole supplier, exclusive arrangement, "limited by the production capacity"; NL controls 15 Jan 2025 metrology/inspection; EU Nov 2025 incl. DUV immersion.
- Nvidia FY2026 10-K (EDGAR): $215.9bn; H20 $4.5bn charge; ~$60m H20 revenue Aug 2025 licences; 15% expectation, no regulation; H20 quote; 22% and 14% direct customers; CoWoS; Chinese government discouraged customers; geographic basis = HQ of direct customers. Nvidia Q2 FY27 release (26 Aug 2026): "Vera Rubin, now in full production"; no China data-center compute revenue assumed.
- Time-sensitive: BIS 91 FR 70789 (9 Nov 2026) extends Affiliates-rule suspension through 10 Jan 2027; China extended its truce measures to 10 Jan 2027 on 9 Nov 2026; no MOFCOM notice found extending the gallium/germanium/antimony ban suspension beyond 27 Nov 2026 (as of 11 Nov).
