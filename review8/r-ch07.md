# Review 8: Chapter 7 (Chips, Data Centres, Energy and Open Models)

## Verdict
Ready to print after small fixes. I found no factual error, misquotation or legally risky statement. The 2025–2026 material holds up against primary sources: Nvidia's FY2026 10-K and its Q3 FY2027 CFO commentary, the Bank of England FPC record, the DOJ "Operation Gatekeeper" case, the Anthropic Fable 5 / Mythos 5 export-control episode, the BIS remote-access rule of 19 November 2026, China's mineral-ban extension of 24 November 2026, CSO Ireland, the Kimi K3, Qwen3.8 and Muse Spark Open releases, and the Nvidia–OpenAI $100 billion story. All the arithmetic is correct. Coverage of the companies is mostly balanced. Amodei's views are flagged twice as those of an interested party, and Huang's views are given as the opposing side. The items below are clarity and balance fixes.

## MUST change before printing
None.

## SHOULD change

### S1. "then Nvidia's chief executive" is never explained
- Where: textbook/chapters/ch07.md:142 (also :243)
- Text now: "Jensen Huang, then Nvidia's chief executive, whose company had lost much of its Chinese market"
- Problem: UNCLEAR. The wording is correct, because Huang resigned on 12 November 2026 and Colette Kress became interim CEO. But the chapter never says so, so readers will be puzzled by "then". Give the fact only, not the reasons: the press reports about why he left are unconfirmed and sensitive.
- Evidence: TheNextWeb / Digital Trends / American Bazaar, 12–13 Nov 2026: "Jensen Huang resigns as Nvidia CEO after 33 years, effective immediately"; "Nvidia names Kress interim CEO after Jensen Huang resigns".
- Change to: "On the other side, Jensen Huang, Nvidia's chief executive until his resignation in November 2026, whose company had lost much of its Chinese market, …" (no new bib entry needed if a neutral source is added, e.g. Nvidia's 8-K of 12 November 2026).

### S2. Prompt caching cites only Anthropic (company balance)
- Where: textbook/chapters/ch07.md:51
- Text now: "Anthropic, for example, says that caching cuts costs by up to 90% and latency by up to 85% for long prompts [@anthropic2024prompt]."
- Problem: UNCLEAR / balance. OpenAI and Google also offer prompt caching (Google calls it context caching). In a book written by Anthropic models, naming only Anthropic's product as the example looks like promotion.
- Evidence: OpenAI API docs, "Prompt caching" (platform.openai.com/docs/guides/prompt-caching); Google Gemini API docs, "Context caching".
- Change to: "Major providers including OpenAI, Google and Anthropic offer it; Anthropic, for example, says that caching cuts costs by up to 90% and latency by up to 85% for long prompts [@anthropic2024prompt]."

### S3. Scope of the November 2026 remote-access rule
- Where: textbook/chapters/ch07.md:144
- Text now: "requiring a licence to supply advanced chips to data centres anywhere that provide large amounts of computing power to companies headquartered in China"
- Problem: UNCLEAR (incomplete). According to law-firm summaries, the end-use control covers companies headquartered in China, Macau or other Country Group D:5 countries, above an aggregate threshold of 12 million TPP.
- Evidence: K&L Gates / Morgan Lewis / Greenberg Traurig alerts, 17–19 Nov 2026: a licence is needed "to export advanced chips to data centers anywhere in the world that provide more than 12 million aggregate TPP of compute to companies headquartered in China, Macau or other Country Group D:5 countries".
- Change to: "… to companies headquartered in China, Macau or other countries under US arms embargo (Country Group D:5) …"

### S4. "headlines usually quote the lower one" is unsupported
- Where: textbook/chapters/ch07.md:195
- Text now: "Both follow recognised rules; they answer different questions, and headlines usually quote the lower one."
- Problem: UNSUPPORTED. No source is given. Coverage of Google's 2026 report actually led with rising emissions (Axios, 30 June 2026: "Google's AI boom sends emissions, power use soaring", total emissions up 18%).
- Change to: "Both follow recognised rules; they answer different questions, so readers should check which one a figure uses."

## Could not verify
- TSMC: "ten largest customers provided 78% of its 2025 revenue". I could not open the risk section of the annual report. HPC at 58% is confirmed.
- ASML: China at 29.1% of 2025 net sales (36.1% in 2024). Press reports give 33% of *system* sales, so 29.1% of *total* net sales is plausible but unconfirmed. 48 EUV systems and 327 lithography systems (300 new plus 27 used) are confirmed.
- AI Index 2026 figures: 17.1 million H100-equivalents, the Arena gaps (174, 7 and 49 points, Claude Opus 4.6 against GLM-5), Grok 4 emissions, 91.2% industry share.
- Microsoft leases of $329.1 billion; capital spending for the first nine months of 2026; Alberta's figure of more than 16 GW of connection requests.

## Checked and confirmed
- Arithmetic. DeepSeek-V3 compute: 6 × 37e9 × 14.8e12 ≈ 3.3e24. H100 ridge point: 990/3.35 ≈ 296 FLOP per byte. Reading 140 GB takes 41.8 ms, or 21 ms when split across two GPUs. 4-bit storage gives 35 GB. TPP: 1,979 × 8 ≈ 15,832, and density 15,832/814 ≈ 19.4. Elo: a 49-point gap gives 57.0%. DeepSeek cost: 2.788M × $2 = $5.576M, and 147k × $2 = $294k. 3.3e24/9.59e9 s ≈ 344 TFLOPS. The Table 7.1 maxima are correct. The Table 7.4 percentages (+59/+79/+74/+87%) are correct. PUE 1.6 → 1.2 is a 25% saving. LBNL/IEA 176/154 = +14%. NVLink is 7× PCIe 5.
- Nvidia FY2026 10-K: revenue $215,938m; data centre $193,737m (against $47,525m in FY2024); China $19,677m against $25,048m; H20 licence revenue "approximately $60 million"; "15% or more … did not publish a regulation"; customers at 22% and 14%; CoWoS; the list of chips needing licences.
- Nvidia Q3 FY2027 CFO commentary: "Shipments of Data Center Hopper products to China during the quarter were $2.4 billion"; "We are not assuming any Data Center compute revenue from China in our outlook."
- Bank of England FPC record, December 2025: "many risky asset valuations remain materially stretched, particularly for technology companies focused on Artificial Intelligence (AI)"; "role of debt financing … increasing quickly".
- Huang, 4 March 2026: "probably not in the cards". The $30 billion investment in OpenAI is confirmed. The September 2025 letter of intent is confirmed.
- DOJ, December 2025: Hao Global and its owner pleaded guilty; "at least $160 million" of H100/H200 chips.
- Anthropic Fable 5 / Mythos 5: letter of 12 June; Anthropic disabled both models worldwide; Mythos 5 relief for trusted partners on 26 June; restrictions lifted on 30 June/1 July with conditions (Mayer Brown; Al Jazeera). Greenberg Traurig: "first known U.S. use of export control authorities to regulate a particular AI frontier model".
- BIS rule of 19 November 2026: rescinds the diffusion rule; new licence requirements for Brazil, Indonesia, Malaysia, Singapore and Thailand.
- China, 24 November 2026: suspension of the gallium/germanium/antimony ban extended to 27 January 2027 (VOA).
- CSO Ireland: data centres used 23% of electricity in 2025, against 5% in 2015.
- Google 2026 environmental report: electricity demand up 37%; water about 10.9 billion gallons (≈41 billion litres), up 34%.
- Kimi K3: 2.8T parameters (104B active); MXFP4 with QAT "from the SFT stage onward". Qwen3.8-2.4T-A95B: licence with a $50M threshold for 12 months. Muse Spark Open: 15 October 2026, 816B parameters (42B active), Muse Model License with a $20M threshold, BF16 and NVFP4 versions; The Batch ranks it top open model outside China.
- Earlier, well-established facts: H100 specifications; TPU studies; Gholami (3.0×/1.6×/1.4×); FP8 paper; the DeepSeek-V3/R1 facts; Nvidia's −17% / ~$600B fall on 27 January 2025; Amodei's quotations; Huang's "failure"; Llama 2 licence; gpt-oss sizes; Lermen and Qi quotations; NTIA; Seger; EU AI Act Art. 51(2); OSAID 1.0.
- Cross-references to Sections 4.1 and 4.4, Table 4.3 (Grok 4 at $388M), Sections 13.2 and 14.4: all correct.

## Tally
Claims checked: 62 · confirmed: 56 · wrong: 0 · outdated: 0 · unclear/unsupported: 4 (S1–S4) · could not verify: 6 groups
