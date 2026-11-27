# Review: Chapter 7, Chips, Data Centres, Energy and Open Models

## Verdict
Ready after one fix. The chapter is accurate, carefully hedged and well sourced. Every worked example recomputes. The high-risk 2026 material I checked holds up against primary or law-firm sources: the Anthropic model-access control, the BIS rule of 19 November 2026, Jensen Huang's resignation (which "then chief executive" correctly reflects), Nvidia's FY2026 and Q3 FY2027 figures, and the Kimi K3, Qwen3.8 and Muse Spark Open specifications. One statement about China's gallium/germanium suspension was overtaken by events on 24 November 2026 and must be updated.

## MUST change before printing

### M1. China did extend the gallium/germanium suspension
- Where: textbook/chapters/ch07.md:138
- Text now: "China's November 2026 extension of its other truce measures to 10 January 2027 did not cover it, and the suspension was due to expire on 27 November 2026 with no extension announced by 26 November [@evertiq2025china; @thenational2026china]."
- Problem: OUTDATED / VERIFIED WRONG. On Tuesday 24 November 2026 China's Ministry of Commerce announced that it would keep suspending the ban on US-bound exports of gallium, germanium, antimony and superhard materials from 28 November 2026 to 27 January 2027. It also kept stricter graphite reviews on hold. The book's cut-off sentence says the opposite.
- Evidence: VOA, 26 Nov 2026, https://www.voanews.com/a/china-extends-suspension-period-for-its-ban-on-export-of-critical-minerals-to-us-20261126/8228334.html : China "will continue to suspend its ban on U.S.-bound exports" of the materials "from November 28 through January 27, 2027". Tech Times, 25 Nov 2026, https://www.techtimes.com/articles/331482/20261125/china-extends-gallium-germanium-antimony-export-ban-pause-january-27-licenses-still-required.htm (licences are still required).
- Change to: "it suspended that ban in November 2025, as part of the same truce, until 27 November 2026, and on 24 November 2026 extended the suspension to 27 January 2027, although the metals still need export licences [@evertiq2025china; @voa2026china]."
  New bib entry (ch07.bib):
  ```
  @misc{voa2026china,
    author = {{Voice of America}},
    title = {China Extends Suspension Period for Its Ban on Export of Critical Minerals to {US}},
    year = {2026},
    month = nov,
    howpublished = {VOA News, 26 November 2026},
    url = {https://www.voanews.com/a/china-extends-suspension-period-for-its-ban-on-export-of-critical-minerals-to-us-20261126/8228334.html},
    urldate = {2026-11-27}
  }
  ```
  Also update the Figure 7.2 source or caption if the figure shows the 27 November expiry.

## SHOULD change

### S1. Say on first mention that Huang has left Nvidia
- Where: textbook/chapters/ch07.md:142 (and 243)
- Text now: "Jensen Huang, then Nvidia's chief executive, whose company had lost much of its Chinese market"
- Problem: UNCLEAR. "Then" is correct, because Huang resigned on 12 November 2026 and Colette Kress is interim CEO. But the book never says so, and a reader in 2027 may think "then" is an error.
- Evidence: The Next Web, Nov 2026, https://thenextweb.com/news/jensen-huang-resigns-as-nvidia-ceo-after-33-years-effective-immediately : "Jensen Huang resigns as Nvidia CEO after 33 years, effective immediately". The filing gives 12 November 2026 as the effective date.
- Change to: "Jensen Huang, Nvidia's chief executive until his resignation in November 2026, whose company had lost much of its Chinese market". Keep "its then chief executive" at line 243 as it is.

### S2. The law firm's "first known use" wording is narrower than the book's
- Where: textbook/chapters/ch07.md:135
- Text now: "in what law firms described as the first known use of export controls to block access to an AI service"
- Problem: UNSUPPORTED (wording). Greenberg Traurig says "the first known U.S. use of export control authorities to regulate a particular AI frontier model". It does not say "to block access to an AI service". The other dates in the sentence check out: the letter of 12 June, Anthropic disabling both models for all users, and the requirement withdrawn for both models on 30 June. Mythos 5 had been partly eased for trusted partners on 26 June and remains limited.
- Evidence: https://www.gtlaw.com/it/insights/2026/6/ai-company-anthropic-suspends-access-to-claude-fable-5-claude-mythos-5-following-us-export-control-directive ; Axios, 30 Jun 2026, https://www.axios.com/2026/06/30/trump-anthropic-ai-model-fable-restrictions
- Change to: "in what one law firm described as the first known US use of export controls to regulate a particular frontier AI model"

## Could not verify
- The Kimi K3 licence terms ($20 million revenue threshold and the display requirement). The parameters (2.8T total, 104B active) and the MXFP4 quantisation-aware training are confirmed by the official README.
- ASML: 327 total lithography systems, and China at 29.1% / 36.1% of *total* net sales. Secondary sources give China as 33% / 41% of *system* sales, which is consistent with the book's figures if those are total net sales. 48 EUV systems is confirmed.
- First-nine-months 2026 capex for Amazon, Alphabet and Meta. LBNL 2025 Update figures (649 TWh). IEA October 2026 water-stress percentages.

## Checked and confirmed
- Arithmetic:
  - 6 × 37e9 × 14.8e12 ≈ 3.3e24
  - 132 × 4 = 528 tensor cores
  - 990/3.35 ≈ 300 FLOP/byte
  - 140 GB / 3.35 TB/s ≈ 42 ms (21 ms split over two GPUs)
  - 35 GB at 4 bits
  - FP-format maxima (3.40e38, 65,504, 3.39e38, 448, 57,344)
  - TPP 1,979 × 8 ≈ 15,800; density ≈ 19/mm²
  - B200 per-GPU figures from HGX/DGX
  - $5.576M; ≈340 TFLOP/s average; ⅓ and ⅙ of peaks
  - Table 7.4 percentage changes (Microsoft 115.95/64.55 = +80%)
  - 49 Elo points ≈ 57%
  - PUE 1.6 → 1.2 = −25%
  - 176/154 = +14%
  - 485/416 = +17%
- Microsoft FY2026 PP&E additions $115.9bn.
- Nvidia: FY26 revenue and data-centre revenue; China $25.0bn → $19.7bn (headquarters basis); $4.5bn H20 charge; ~$60M of licensed H20 revenue; $2.4bn of Hopper shipments to China in Q3 FY27; no China data-centre revenue in the outlook.
- Nvidia–OpenAI: $30bn into the $110bn round; Huang's "probably not in the cards" (March 2026).
- Huang resigned 12 Nov 2026 ("then" is correct).
- Anthropic Fable 5 / Mythos 5 control of 12 June and lifting on 30 June 2026.
- BIS interim final rule (issued 16 Nov, effective and published 19 Nov 2026): rescinds the diffusion rule, controls remote access, adds the five named countries.
- China's suspension of the gallium/germanium ban to 27 Nov 2026 (original), and the December 2024 ban.
- ASML: 48 EUV systems in 2025.
- Open-weight models: Qwen3.8-2.4T-A95B with its $50M licence threshold; Muse Spark Open (15 Oct 2026, 816B/42B, $20M cap, BF16 + 4-bit); Kimi K3 2.8T/104B with MXFP4 QAT.
- Amodei quotations ("serve a vital purpose", "only thing that can prevent…", "expected point on an ongoing cost reduction curve"); Huang's "a failure" (Reuters, May 2025).
- Nvidia's fall of 17% and nearly $600bn on 27 Jan 2025.
- Cross-references: Section 4.1 (compute rule, 3.3e24), Section 4.4 / Table 4.3 (Grok 4 $388M), Chapter 4 on quantisation (Kumar et al.), Chapter 13 Article 51(2) threshold. All consistent.

## Tally
Claims checked: 72 · confirmed: 66 · wrong: 0 · outdated: 1 (M1) · imprecise wording: 2 (S1, S2) · could not verify: 3 groups
