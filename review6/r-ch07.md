# Review 6: Chapter 7 (Chips, Data Centres, Energy and Open Models)

## Verdict
Ready to print after two small factual fixes. The chapter is dense but clear and carefully hedged. Its arithmetic is correct throughout, and the 2026 material holds up against primary and secondary sources: the BIS rule of 19 November 2026, the Affiliates-rule extension, China's suspension of the gallium/germanium ban to 27 January 2027, Nvidia's Q3 FY27 China shipments, the Anthropic Fable 5 / Mythos 5 episode, Huang's resignation, Muse Spark Open, Kimi K3 and ASML's 20-F. Tone towards named people and companies is fair. Anthropic's interest is disclosed where Amodei is quoted.

## MUST change before printing

### M1. Ironwood 16-bit peak is published
- Where: textbook/chapters/ch07.md:64 (Table 7.2)
- Text now: "| Peak dense 16-bit (TFLOPS) | ≈ 990 | ≈ 2,250 | not published |"
- Problem: VERIFIED WRONG. Google's own TPU7x (Ironwood) documentation lists a BF16 peak per chip alongside the FP8 peak that the table already uses.
- Evidence: https://docs.cloud.google.com/tpu/docs/tpu7x (accessed 27 Nov 2026). The per-chip specification table gives "Peak compute per chip (BF16) 2307 TFLOPs" and "(FP8) 4614 TFLOPs", with HBM "192 GiB" and bandwidth "7.37 TB/s".
- Change to: "| Peak dense 16-bit (TFLOPS) | ≈ 990 | ≈ 2,250 | 2,307 (peak) |". Add `@googlecloud2026tpu7x` to the table's source list, with this bib entry:
  ```
  @misc{googlecloud2026tpu7x,
    author       = {{Google Cloud}},
    title        = {{TPU7x} ({Ironwood})},
    year         = {2026},
    howpublished = {Cloud TPU documentation (company source)},
    url          = {https://docs.cloud.google.com/tpu/docs/tpu7x},
    urldate      = {2026-11-27}
  }
  ```
  The caption sentence "Google does not state whether Ironwood's peak is dense or sparse" can stay, changed to "peaks".

### M2. Gas-turbine orders: the 70% is for data-centre turbines only
- Where: textbook/chapters/ch07.md:104
- Text now: "orders for gas turbines rose 70% in 2025 [@iea2026key, Executive Summary]"
- Problem: MISQUOTED (scope). The IEA figure covers orders for gas turbines to power data centres, not all gas-turbine orders.
- Evidence: Eco-Business report on the IEA's *Key Questions on Energy and AI* (April 2026), https://www.eco-business.com/news/ais-energy-appetite-is-outpacing-deployment-of-ai-based-climate-solutions-iea/, which says "Orders for gas turbines to power data centres rose 70 per cent in 2025". I could not open the IEA page itself (it is behind a Cloudflare challenge), so the author should confirm the exact wording in the IEA Executive Summary.
- Change to: "orders for gas turbines to power data centres rose 70% in 2025 [@iea2026key, Executive Summary]"

## SHOULD change

### S1. The 15–27 GW of on-site gas is a global figure
- Where: ch07.md:191
- Text now: "In the United States some developers are building gas-fired generation on site; the IEA estimates that 15–27 GW of such capacity might power data centres by 2030"
- Problem: UNCLEAR. The IEA estimate is global, but the sentence order makes it read as a US figure.
- Evidence: Eco-Business on the IEA report (above): "between 15 and 27 gigawatts of onsite gas-fired power capacity could be supplying data centres globally by 2030".
- Change to: "In the United States some developers are building gas-fired generation on site; worldwide, the IEA estimates that 15–27 GW of such capacity might power data centres by 2030"

### S2. Anthropic export-control episode: wrong source for the "first known" phrase, and Mythos 5 timeline
- Where: ch07.md:135
- Text now: "Anthropic switched both off for all customers until Commerce lifted the control, with conditions, on 30 June, in what one law firm described as the first known US use of export controls to regulate a particular frontier AI model [@kahn2026anthropic; @eastland2026lutnick; @power2026us; @mayerbrown2026commerce]"
- Problem: UNSUPPORTED (attribution) and slightly simplified.
  - The "first known" wording comes from Greenberg Traurig, not from the Mayer Brown note that is cited. Mayer Brown says only that this "would be the first time Commerce has treated an AI model itself" as the controlled item, and frames that conditionally.
  - On 26 June Commerce had already allowed Mythos 5 access for certain trusted partners, so the models were not off for all customers right up to 30 June.
- Evidence:
  - Greenberg Traurig, June 2026, https://www.gtlaw.com/en/insights/2026/6/ai-company-anthropic-suspends-access-to-claude-fable-5-claude-mythos-5-following-us-export-control-directive: "This represents the first known U.S. use of export control authorities to regulate a particular AI frontier model on a national security basis."
  - Mayer Brown, 30 June 2026: the 26 June letter exempted "certain trusted partners" for Mythos 5.
  - Al Jazeera, 1 July 2026: Lutnick's letter said Anthropic no longer needs a licence, on conditions.
- Change to: "Anthropic switched both off for all customers; Commerce allowed some trusted partners back onto Mythos 5 on 26 June and lifted the control, with conditions, on 30 June. One law firm described it as the first known US use of export controls to regulate a particular frontier AI model [@kahn2026anthropic; @eastland2026lutnick; @power2026us; @gt2026anthropic]". Add this bib entry:
  ```
  @misc{gt2026anthropic,
    author       = {{Greenberg Traurig}},
    title        = {{AI} Company {Anthropic} Suspends Access to {Claude Fable 5}, {Claude Mythos 5} Following {U.S.} Export Control Directive},
    year         = {2026},
    howpublished = {Greenberg Traurig client alert, June 2026 (law-firm summary)},
    url          = {https://www.gtlaw.com/en/insights/2026/6/ai-company-anthropic-suspends-access-to-claude-fable-5-claude-mythos-5-following-us-export-control-directive},
    urldate      = {2026-11-27}
  }
  ```

### S3. Microsoft capex rounding
- Where: ch07.md:228 (Table 7.4)
- Text now: "| 64.6 | 115.9 | +80% |"
- Problem: Arithmetic. 115.9 / 64.6 = 1.794, which is +79%. The other three rows round correctly.
- Change to: "+79%"

## Could not verify
- The IEA *Key Questions* report: iea.org blocks automated access. The headline figures were confirmed through press coverage: 485 TWh, +17%, about 950 TWh in 2030, about 3% of demand, memory shortage "through at least the end of 2027", about 350 Mt in 2035 at about 2%. Not confirmed: the 40% share of corporate PPAs, 833–1,008 TWh, the threefold users and fivefold revenue, the $715 bn and the $3.9 trillion, and the section and page pinpoints.
- Microsoft FY2026 cash capex of $115.9 bn (the $329.1 bn of leases is confirmed). Also unconfirmed: the 9-month 2026 capex for Amazon, Alphabet and Meta, Nvidia's 22%/14% customer concentration, and TSMC's customer concentration.
- AI Index 2026 figures: 91.2% from industry, $285.9 bn against $12.4 bn, Arena gaps of 174, 7 and 49 points, and the Grok 4 emissions.
- LBNL *2025 Update* (649 TWh), Rosa et al. 2026, the CSO's 23% for Ireland in 2025, and the EuroHPC tender of July 2026.
- Qwen3.8 and Kimi K3 licence revenue thresholds. The model cards name the licences but do not show the terms.

## Checked and confirmed
- Arithmetic:
  - DeepSeek-V3 FLOP: 6 × 37e9 × 14.8e12 ≈ 3.3e24.
  - About 300 ops/byte (990 / 3.35).
  - 42 ms and 21 ms per token.
  - TPP about 15,800 and density about 19.4/mm².
  - $5.576 M and about 340 TFLOPS achieved.
  - 49 Elo points gives about 57%.
  - The FP max values in Table 7.1.
  - PUE 1.6 → 1.2 is about −25%.
  - 176/154 is +14%.
  - Image/text energy above 60×.
  - B200 per-GPU figures from HGX/DGX B200.
- BIS rule of 19 Nov 2026. Law-firm summaries (Morgan Lewis and others) confirm:
  - it rescinds the diffusion rule, including the 4E091 weights control;
  - it licenses exports to data centres serving entities headquartered in D:5/Macau;
  - it adds Indonesia, Malaysia, Singapore, Thailand and Brazil.
- BIS extension of the Affiliates rule to 10 Jan 2027. Bessent and the AP on the truce extension to 10 Jan.
- China: VOA confirms the gallium/germanium suspension extended to 27 Jan 2027, with licences still required.
- Nvidia:
  - Q3 FY27 CFO commentary: "Shipments of Data Center Hopper products to China during the quarter were $2.4 billion"; no China DC compute revenue assumed in the outlook.
  - Q2 FY27 release: Vera Rubin "now in full production".
  - China revenue on the headquarters basis: $25.0 bn → $19.7 bn.
  - Huang resigned on 12 Nov 2026 (8-K).
  - Huang's March 2026 "probably not in the cards"; the $30 bn into the $110 bn round.
- ASML 20-F:
  - "currently the world's only manufacturer of EUV lithography systems";
  - 327 systems, 48 EUV;
  - China 29.1% of 2025 net sales against 36.1% in 2024;
  - Zeiss "production capacity" wording;
  - EU extension of Dutch controls in Nov 2025.
- Muse Spark Open (The Batch, 23 Oct 2026): 816B/42B, Muse licence with a $20 M threshold and attribution, a 4-bit version, "top open weights model outside China", and the spring-2026 proprietary Muse Spark.
- Kimi K3: 2.8T/104B, MXFP4 with QAT from SFT.
- Amodei quotes word for word. Lermen et al. quote and "about 1%" (arXiv abstract). TAR "hundreds of steps of fine-tuning". Qi et al. "$0.20". 

Tally: about 95 claims checked; about 80 confirmed; 2 wrong (M1, M2); 0 outdated; 3 imprecise (S1–S3); the rest could not be verified.
