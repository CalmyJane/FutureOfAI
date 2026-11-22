# Third review: Chapter 7 — Chips, Data Centres, Energy and Open Models

Final version, 22 November 2026. Two reviewers worked on this report: a first round on 11 November and a continuation on 22 November. Both read the full chapter, bib, figure specs, plotting script and glossary, and all arithmetic was recomputed. The time-sensitive items were re-checked against news and official sources up to 22 November 2026.

## Verdict
**Ready after the MUST fixes below.** The technical sections are accurate and well sourced, and every worked number checks out. These are 7.1 (accelerators, number formats, serving), 7.4 (electricity, water, emissions) and 7.5 (costs). The IEA, LBNL, AI Index, company-filing and model-card claims match their sources closely. The problems are currency and sourcing in the fast-moving parts:
- **Export controls (Section 7.3).** Three November 2026 events overtook the text: BIS extended the Affiliates-rule stay on 9 November; BIS formally rescinded the diffusion rule and brought remote access to chips under licence on 19 November; and Nvidia's chief executive Jensen Huang resigned on 11 November.
- **Muse Spark Open.** Its facts are cited to a Meta blog from April 2026 that predates the model.
- **EU gigafactories.** The "four gigafactories" sentence is contradicted by the July 2026 call that the sentence itself cites.

All of these fixes are short wording changes. None needs restructuring.

## MUST change before printing

### M1. Affiliates-rule suspension was extended on 9 November 2026
- Where: textbook/chapters/ch07.md:133; ch07.md:116 (Figure 7.2 caption); textbook/figures/specs/fig-07-02.md (caption; event 6a "stayed until 9 Nov 2026")
- Text now (l.133): "As of late October 2026, however, BIS had not published a rule extending the suspension of the ownership rule, which was due to lapse on 9 November 2026, with the restrictions returning on 10 November [@bis2025one; @dechert2026bis]."
- Text now (l.116): "As of late October 2026 the one-year stay of the Affiliates rule was due to end on 9 November 2026."
- Problem: OUTDATED. BIS published a final rule on 9 November 2026 extending the suspension through 10 January 2027. China extended its matching suspension of rare-earth and related controls on the same day, also to 10 January 2027.
- Evidence: Federal Register 91 FR 70789, FR Doc. 2026-22793 (https://www.federalregister.gov/api/v1/documents/2026-22793.json): "The suspension was set to end November 9, 2026. This final rule extends the suspension through January 10, 2027." The National, 9 November 2026 (https://www.thenationalnews.com/news/us/2026/11/09/china-extends-pause-on-rare-earth-export-curbs-for-two-months/): "The extension runs to January 10." MOFCOM's 28 September 2026 readout of the eighth round of talks says the two sides agreed to extend the Kuala Lumpur joint arrangement to 10 January 2027 (http://www.mofcom.gov.cn/zcjd/dwmy/art/2026/art_c68e66e26aae44278b2a7f1845857270.html).
- Change to (l.133, replace the last sentence): "BIS duly extended the suspension of the ownership rule, which had been due to lapse on 9 November 2026, through 10 January 2027, and China extended its suspension of the rare-earth controls to the same date [@bis2026extension; @thenational2026china]."
- l.116 and the fig-07-02.md caption: see M2 for the combined new caption. In the fig-07-02.md event 6a note, replace "stayed until 9 Nov 2026" with "stay extended on 9 Nov 2026 to 10 Jan 2027 (91 FR 70789)".
- Bib: add
  - `@misc{bis2026extension, author={{Bureau of Industry and Security}}, title={Extension of the Suspension of Expansion of End-User Controls for Affiliates of Certain Listed Entities}, year={2026}, howpublished={Final rule, 91 FR 70789, 9 November 2026}, url={https://www.federalregister.gov/documents/2026/11/09/2026-22793/extension-of-the-suspension-of-expansion-of-end-user-controls-for-affiliates-of-certain-listed}}`
  - `@misc{thenational2026china, author={Fitzgerald, Kyle}, title={China extends pause on rare earth export curbs for two months}, year={2026}, howpublished={The National, 9 November 2026}, url={https://www.thenationalnews.com/news/us/2026/11/09/china-extends-pause-on-rare-earth-export-curbs-for-two-months/}}`
  - `dechert2026bis` can then be dropped from l.133. Keep it if wanted for the history.

### M2. The diffusion rule was formally rescinded, and remote access brought under licence, on 19 November 2026
- Where: textbook/chapters/ch07.md:128, :143, :116 (Figure 7.2 caption), :316; textbook/figures/specs/fig-07-02.md (caption; the fact-check note under event 6)
- Text now (l.128): "In July 2026 the worldwide licence requirement still appeared in the regulations, but BIS stated that it was enforcing it only for certain destinations, mainly countries of concern such as China [@bis2026enhanced]."
- Text now (l.143): "Renting chips in data centres abroad was not itself covered; a bill to bring such remote access under export controls passed the House of Representatives in January 2026 but had not become law [@congress2026remote]."
- Text now (l.116): "...the promised replacement had not been issued by October 2026, and access was handled through country-specific measures such as the July 2026 UAE rule."
- Text now (l.316): "The January 2025 diffusion rule controlled the weights of certain advanced closed-weight models but left the weights of open-weight models outside its scope, on the ground that the most advanced of them were less powerful than the leading closed models [@bis2025framework]."
- Problem: OUTDATED. BIS published the interim final rule "Addressing Remote Access to Advanced Semiconductors" (91 FR 74970) on 19 November 2026, effective the same day. It does four things relevant to the chapter:
  - It requires licences for advanced chips going to data centres anywhere that remotely supply significant compute to companies headquartered in Country Group D:5 (which includes China) or Macau. The threshold is more than 12,000,000 aggregate TPP.
  - It adds a licence requirement for Indonesia, Malaysia, Singapore, Thailand and Brazil as diversion risks.
  - It "formally rescinds the regulations implementing the Biden-era AI Diffusion Rule", including the worldwide licence requirement.
  - It "revokes the controls on model weights" by removing ECCN 4E091.
  The House bill is unchanged: it passed the House and was referred to the Senate Banking Committee, and no Senate action was found.
- Evidence: https://www.federalregister.gov/api/v1/documents/2026-23529.json (abstract: "...establishes new restrictions which will apply for exports... to overseas data centers that remotely supply significant volumes of compute to companies headquartered in Country Group D:5 or Macau... a license will be required to export... advanced semiconductors to Indonesia, Malaysia, Singapore, Thailand, or Brazil... Finally, the IFR formally rescinds the regulations implementing the Biden-era AI Diffusion Rule"; dates: "This rule is effective November 19, 2026"). The full text was read at https://www.govinfo.gov/content/pkg/FR-2026-11-19/html/2026-23529.htm: "This IFR revokes the controls on model weights published in the AI Diffusion Rule... ECCN 4E091 is removed from the CCL"; "this IFR... removes the worldwide license requirement from former Sec. 742.6(a)(6)(iii)(A)"; "...will provide access to more than 12,000,000 'aggregate TPP'...".
- Change to:
  - l.128, add after the sentence ending "[@bis2026guidance].": "On 19 November 2026 an interim final rule formally rescinded the diffusion rule, including its worldwide licence requirement and its control on model weights [@bis2026addressing]."
  - l.143, replace the sentence with: "Until November 2026 renting chips in data centres abroad was not itself covered. A bill to bring such remote access under export controls passed the House of Representatives in January 2026 [@congress2026remote]; BIS then acted itself, with a rule of 19 November 2026 requiring a licence to supply advanced chips to data centres anywhere that provide large amounts of computing power to companies headquartered in China, and adding licence requirements for Indonesia, Malaysia, Singapore, Thailand and Brazil as diversion risks [@bis2026addressing]."
  - l.316, append to the sentence: "...than the leading closed models [@bis2025framework]; BIS revoked that control on model weights in November 2026 [@bis2026addressing]."
  - Figure 7.2 caption (l.116 and fig-07-02.md), replace the whole caption with: "Figure 7.2: Main US export-control measures on advanced AI chips and related items, October 2022 to July 2026. The direction of policy changed in 2025. Rules continued to restrict China, while the global licensing framework of January 2025 was abandoned before it took full effect, and access was handled through country-specific measures such as the July 2026 UAE rule. In November 2026, after the period shown, BIS extended the stay of the Affiliates rule to 10 January 2027 and formally rescinded the diffusion rule in a rule that also brought remote access to chips in data centres abroad under licence (Section 7.3). Source: @bis2022implementation; @bis2023implementation; @bis2024foreignproduced; @bis2025framework; @bis2025department; @nvidia2025form; @bis2025expansion; @bis2025one; @bis2026revision; @bis2026enhanced; @bis2026extension; @bis2026addressing."
  - In fig-07-02.md, replace the fact-check note under event 6 ("...do not label this a completed rescission") with: "Rescission formalised by 91 FR 74970 on 19 Nov 2026, after the period shown." The timeline itself can stay at July 2026 (see S8 for an optional extension).
- Bib: add `@misc{bis2026addressing, author={{Bureau of Industry and Security}}, title={Addressing Remote Access to Advanced Semiconductors}, year={2026}, howpublished={Interim final rule, 91 FR 74970, 19 November 2026}, url={https://www.federalregister.gov/documents/2026/11/19/2026-23529/addressing-remote-access-to-advanced-semiconductors}}`

### M3. Jensen Huang is no longer Nvidia's chief executive
- Where: textbook/chapters/ch07.md:141 and :242
- Text now (l.141): "On the other side, Nvidia's chief executive Jensen Huang, whose company had lost much of its Chinese market, called the controls "a failure" in May 2025..."
- Text now (l.242): "...and in March its chief executive said that a $100 billion investment was "probably not in the cards" [@reuters2026openai; @king2026nvidia]."
- Problem: OUTDATED. Nvidia's board accepted Huang's resignation as President, CEO and director on 11 November 2026, and Colette Kress is interim CEO. A reader after November 2026 will read "Nvidia's chief executive Jensen Huang" as present tense. This is the only chapter that names him.
- Evidence: Nvidia Form 8-K filed 12 Nov 2026, Item 5.02 (https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000082/nvda-20261111.htm): "On November 11, 2026, the Board of Directors... accepted the resignation of Jen-Hsun Huang, as NVIDIA's President, Chief Executive Officer and member of the Board, effective immediately... appointed... Colette M. Kress... to serve as interim Chief Executive Officer". The 17 Nov 2026 Q3 FY2027 release quotes Kress as "interim CEO".
- Change to:
  - l.141: "On the other side, Jensen Huang, then Nvidia's chief executive, whose company had lost much of its Chinese market, called the controls "a failure" in May 2025..."
  - l.242: "...and in March its then chief executive, Jensen Huang, said that a $100 billion investment was "probably not in the cards" [@reuters2026openai; @king2026nvidia]."
  - The quotes themselves are verified (see Checked and confirmed).

### M4. The Muse Spark Open facts are cited to a Meta post that predates the model
- Where: textbook/chapters/ch07.md:49 and :271
- Text now (l.49): "Kimi K3 and Meta's Muse Spark Open (Section 7.6) were also published with 4-bit weights [@moonshot2026kimik3; @meta2026muse]."
- Text now (l.271): "...before publishing on 15 October 2026 the weights of Muse Spark Open, with 816 billion parameters, 42 billion active [@deeplearningai2026meta; @meta2026muse]."
- Problem: UNSUPPORTED BY CITED SOURCE.
  - `meta2026muse` is "Introducing Muse Spark", dated 8 April 2026. It covers the proprietary Muse Spark and does not mention Muse Spark Open, open weights, 816B/42B, 4-bit weights or October 2026.
  - The Batch (23 Oct 2026) gives 816B/42B but not the 15 October date or the precision of the released weights. It mentions 4 bits only in a memory estimate.
  - Meta's own release post of 15 October 2026 supports the date and the parameter counts. Meta's official Hugging Face organisation (meta-models, verified "Meta Inc.") publishes the base weights in BF16 (`meta-models/Muse-Spark-Open-816B-A42B`, safetensors BF16) plus a separate NVFP4 version. So "published with 4-bit weights" is only half true for Muse Spark Open.
  - Kimi K3's model card does state "MXFP4 weights / MXFP8 activations" with quantisation-aware training.
- Evidence: https://ai.meta.com/blog/introducing-muse-spark-msl/ (dated 8 April 2026; "Muse Spark is available today at meta.ai"). https://research.meta.ai/blog/muse-spark-open ("October 15, 2026"; "Today, we're releasing the weights for Muse Spark Open... 816B total parameters (42B active) and a 1M-token context window"; "Muse Model License with limited commercial terms"). Hugging Face API for meta-models/Muse-Spark-Open-816B-A42B (BF16 parameters) and meta-models/Muse-Spark-Open-816B-A42B-NVFP4. https://huggingface.co/moonshotai/Kimi-K3.
- Change to:
  - l.49: "Kimi K3 was trained and published with 4-bit (MXFP4) weights, and Meta released Muse Spark Open (Section 7.6) in a 4-bit version as well as at 16 bits [@moonshot2026kimik3; @meta2026museopen]."
  - l.271: "...before publishing on 15 October 2026 the weights of Muse Spark Open, with 816 billion parameters, 42 billion active [@meta2026museopen; @deeplearningai2026meta]." Keep `@meta2026muse` only for "released its new Muse Spark models in spring 2026 as proprietary services".
- Bib: add `@misc{meta2026museopen, author={{Meta}}, title={Introducing Muse Spark Open, the Most Capable {US} Open-Weight Model to Date}, year={2026}, howpublished={Meta AI research blog, 15 October 2026 (company source)}, url={https://research.meta.ai/blog/muse-spark-open}}`

### M5. EU AI gigafactories: the cited July 2026 call provides for up to seven, not four
- Where: textbook/chapters/ch07.md:326
- Text now: "The European Commission's InvestAI initiative of February 2025 aims to mobilise €200 billion, including a €20 billion fund for four "AI gigafactories" of around 100,000 of the latest chips each, whose consortia are to be selected in early 2027 [@ec2025eu; @eurohpc2026eurohpc]."
- Problem: OUTDATED and contradicted by the cited source. The February 2025 Commission release says the fund "will finance four future AI gigafactories" with "around 100 000 latest-generation AI chips". The EuroHPC call of 30 July 2026, which the sentence cites for the 2027 selection, says: "This procurement will support the establishment of up to seven AI Gigafactories... expected to be located in at least seven Member States", with selection "in early 2027".
- Evidence: EC IP/25/467 (via presscorner API); https://eurohpc-ju.europa.eu/eurohpc-joint-undertaking-launches-ai-gigafactories-call-2026-07-30_en
- Change to: "The European Commission's InvestAI initiative of February 2025 aims to mobilise €200 billion, including a €20 billion fund for "AI gigafactories" of around 100,000 of the latest chips each; the call for tenders launched in July 2026 provides for up to seven, to be selected in early 2027 [@ec2025eu; @eurohpc2026eurohpc]."

## SHOULD change (real but not blocking)

### S1. Gallium/germanium/antimony suspension: its 27 November end date was not covered by the November extension
- Where: ch07.md:137: "...with the suspension due, as of late October 2026, to end on 27 November 2026 [@evertiq2025china]."
- Problem: still correct on 22 November, but incomplete. China's 9 November extension to 10 January 2027 covered the measures due to end on 10 November. It did not cover MOFCOM Announcement 2025 No. 72, which suspends the US-specific ban until 27 November. No extension had been announced by 22 November: MOFCOM's 2026 announcements list shows nothing newer than 10 November, and trade press of 31 October and 17 November reports none. The book will appear after 27 November, so the author should check MOFCOM just before printing.
- Change to: "...it suspended that ban in November 2025, as part of the same truce, until 27 November 2026; China's November 2026 extension of its other truce measures to 10 January 2027 did not cover it, and no extension had been announced by 22 November [@evertiq2025china; @thenational2026china]." If an extension is announced before printing, replace this with the new date.

### S2. Nvidia did ship to China in the quarter its outlook excluded
- Where: ch07.md:132: "Its outlook for the following quarter assumed no data-centre revenue from China [@nvidia2026nvidia]."
- Problem: true, but a reader will infer that no sales followed. Nvidia's Q3 FY2027 CFO commentary (17 Nov 2026) says: "Shipments of Data Center Hopper products to China during the quarter were $2.4 billion." The Q4 outlook again assumes no China data-centre compute revenue.
- Change to: "Its outlook for the following quarter assumed no data-centre revenue from China, although in the quarter to October 2026 it shipped $2.4 billion of Hopper data-centre products there [@nvidia2026nvidia; @nvidia2026q3cfo]."
- Bib: add `@misc{nvidia2026q3cfo, author={{NVIDIA Corporation}}, title={{CFO} Commentary on Third Quarter Fiscal 2027 Results}, year={2026}, howpublished={Exhibit to Form 8-K, 17 November 2026}, url={https://www.sec.gov/Archives/edgar/data/1045810/000104581026000088/q3fy27cfocommentary.htm}}`

### S3. Qwen3.8 is missing from the list of the largest open models
- Where: ch07.md:271 and Table 7.5 (l.273–286)
- Problem: Alibaba published Qwen3.8-2.4T-A95B on 8 August 2026: 2.4 trillion parameters, 95 billion active. It is the second-largest open-weight model after Kimi K3 and much larger than the Qwen3.5 the text names. It also moved Qwen from Apache 2.0 to a custom licence with revenue thresholds, which is exactly the trend the paragraph describes: "Qwen3.8-Max License", separate licence for Model-as-a-Service or AI-work-assistant businesses with more than US$50 million revenue in 12 months, and model-name display for products with more than 100 million MAU or US$20 million monthly revenue. Kimi K3 is still the largest. The other models named are correct.
- Evidence: https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B (README: "Number of Parameters: 2.4T in total and 95B activated"; license_name qwen3.8-max). https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B/raw/main/LICENSE.
- Change to (l.271, after the Qwen3.5 sentence): "Its Qwen3.8 (August 2026), with 2.4 trillion parameters, 95 billion active, is the second-largest open-weight model and the first Qwen flagship released under a licence with a revenue threshold [@qwen2026qwen38]." Add a Table 7.5 row: "| Qwen3.8-2.4T-A95B (Aug 2026) | Qwen3.8-Max License | Model-as-a-service or AI-assistant businesses with over $50 million revenue in 12 months need a separate licence; very large products must display the model name |"
- Bib: add `@misc{qwen2026qwen38, author={{Qwen Team}}, title={{Qwen3.8-2.4T-A95B} Model Card and License}, year={2026}, url={https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B}}`

### S4. IEA pinpoint for the nuclear sentences is wrong
- Where: ch07.md:192: "...not expected before about 2030 [@iea2026key, sec. 5.1, p. 64]."
- Problem: in the IEA PDF (Régie de l'énergie mirror), the TMI, Susquehanna, 45 GW and "around 2030" facts are in sec. 5.1, pp. 47–48. The quotation "less formal off-take arrangements" is in sec. 7.3, p. 65. Page 64 is sec. 7.3 and does not contain the quote.
- Change to: "[@iea2026key, sec. 5.1, pp. 47–48; sec. 7.3, p. 65]".

### S5. The Mistral per-response figure is for Le Chat
- Where: ch07.md:204: "...gives 45 millilitres (and 1.14 grams of emissions) for a 400-token response from Mistral Large 2..."
- Problem: Mistral's post gives the figure for "the use of our AI assistant Le Chat for a 400-token response - excluding users' terminals: 1.14 gCO₂e, 45 mL of water". The life-cycle study itself is of Mistral Large 2.
- Change to: "...gives 45 millilitres (and 1.14 grams of CO~2~-equivalent) for a 400-token response from its Le Chat assistant, in a life-cycle assessment of its Mistral Large 2 model, including upstream impacts such as hardware manufacturing [@mistral2025our]."

### S6. Optional: 2026 capital spending is now visible in quarterly filings
- Where: ch07.md:222–233 (Table 7.4 and the IEA $715 billion sentence)
- Problem: the table is correct (see confirmed). Nine-month 2026 cash capex is already: Amazon $175.7bn, Alphabet $132.0bn, Meta $83.1bn. Microsoft's July–September 2026 quarter was $39.4bn. Each of the three calendar-year companies has already passed its full-year 2025 figure. One sentence would make the point the IEA projection makes, with audited numbers.
- Suggested addition after l.233: "Quarterly filings show the pace: in the first nine months of 2026 Amazon spent $175.7 billion, Alphabet $132.0 billion and Meta $83.1 billion on property and equipment, each more than in the whole of 2025 [10-Q filings]." The source is SEC XBRL companyconcept data (PaymentsToAcquireProductiveAssets for Amazon; PaymentsToAcquirePropertyPlantAndEquipment for the others).

### S7. AESO: "more than" 16 GW
- Where: ch07.md:3: "Requests to connect new data centres to its grid soon reached 16 gigawatts (GW)"
- Problem: AESO (4 June 2025) says "more than 16 gigawatts (GW) of total demand" from 29 projects.
- Change to: "...soon exceeded 16 gigawatts (GW)...".

### S8. Optional: extend the Figure 7.2 timeline to November 2026
- Where: textbook/print/figs_ch07.py (t1 = 2026.72; event list at l.95–100) and fig-07-02.md
- Suggestion: add "19 Nov 2026 — Remote-access rule — diffusion rule formally rescinded; data-centre licences — tightening (91 FR 74970)" and an open circle "9 Nov 2026 — stay extended to 10 Jan 2027". Then set t1 to about 2026.95 and drop "(after the period shown)" from the M2 caption. Not needed if the M2 caption is used.

## Could not verify
- ch07.md:100, TSMC quotation "to enhance HPC products with superior compute power and memory bandwidth" [@tsmc2026annualreport]. The TSMC investor PDF is behind a Cloudflare challenge, and the phrase is not in TSMC's 20-F. TSMC's 3DFabric page says CoWoS "empowers products with high-performance compute and memory bandwidth". Low priority: a human should open the annual report PDF (ch. 5) and confirm the exact wording, or else paraphrase without quotation marks.
- ch07.md:252, the Guardian figures (17% fall, "nearly $600 billion"). The Guardian blocks automated access. Several outlets confirm the 17% fall and a $589–593 billion loss, and a search excerpt of the Guardian piece gives "fell 17%, wiping nearly $600bn". Treated as confirmed via secondary sources; no action needed.
- ch07.md:122, the October 2023 TPP thresholds (4,800; 1,600 with density 5.92; the second tier) and the "dense, not sparse" counting. Checked against knowledge and the Nvidia 8-K, not re-read in the Federal Register text. Settled pre-2025 material; low priority.

## Reader notes
1. ch07.md:109: "In AI hardware the clearest examples are the four described above". The reader has to count back to work out which four. Name them: "design software, EUV lithography, leading-edge fabrication, and memory and packaging".
2. ch07.md:133: the "Ownership rules and the trade truce" bullet is now a chain of five dated events in one bullet. After M1, consider splitting it into two sentences, one about the US rule and one about China's side.
3. ch07.md:116: Figure 7.2 stops in July 2026 while the text runs to November. The M2 caption bridges the gap, but the figure would be clearer extended (S8).
4. ch07.md:41: one paragraph covers the FP8 paper, H100 FP8 support, DeepSeek's block scaling, Hopper's 14-bit accumulation, the H800's export history and Blackwell's FP4. The H800 history sentence would read better in 7.3.
5. ch07.md:161: the LBNL paragraph stacks nine numbers in a row, from 60 to 649 TWh. It is accurate but heavy, and a small table or a sentence break would help.
6. ch07.md:271: "Z.ai's GLM-5 and DeepSeek-V4 complete the group (Table 7.5)" sends the reader to a licence table for parameter counts. That works, but it is the only place where sizes appear only in a table.
7. ch07.md:292: two different measures of the open–closed gap sit side by side: Epoch's "about four months" on its capability index and the Arena's 49 points "widened again". A short clause saying they measure different things would prevent confusion.
8. ch07.md:3: the opening sets 1 GW beside an 835 MW unit and calls 1 GW "a little more than" it, which is 20% more. "Somewhat more than" is closer.

## Checked and confirmed
All entries below were checked against the named source. Entries marked (R1) were confirmed in the first round on 11 Nov 2026; the rest were checked on 22 Nov 2026.

### Arithmetic recomputed (all agree with the text) (R1)
- l.9: 6 × 37e9 × 14.8e12 = 3.29e24 FLOP ("about 3.3 × 10^24").
- l.21: 990 TFLOPS / 3.35 TB/s = 296 ops/byte ("roughly 300"); 70e9 × 2 bytes = 140 GB; 140 GB / 3.35 TB/s = 41.8 ms ("about 42"); half = 20.9 ms ("about 21").
- l.47: 70e9 × 0.5 byte = 35 GB.
- l.55: 900 / 128 = 7.03 ("seven times").
- Table 7.1: FP32 max 3.40e38; FP16 65,504; BF16 3.39e38; E4M3 448; E5M2 57,344.
- Table 7.2: 1,440 GB / 8 = 180 GB; 64 TB/s / 8 = 8 TB/s; 1,979 / 2 = 990; HGX B200 36 and 72 PFLOPS sparse / 8 / 2 = 2,250 and 4,500.
- l.74: 193.7 / 47.5 = 4.08 ("quadrupled", l.240).
- l.122: TPP = 2 × 989.5 × 8 = 15,832 ("about 15,800"); 15,832 / 814 = 19.4 ("about 19").
- l.161: 176 / 154 = 1.143 ("about 14% above"); 580 / 325 = 1.78 ("almost twice").
- l.182: 2.9 / 0.047 = 61.7 ("more than 60 times").
- l.184: 1 − 1.2/1.6 = 25%.
- l.217: 2.664M + 0.124M = 2.788M; × $2 = $5.576M.
- l.219: 2.664M h × 3600 = 9.59e9 GPU-s; 3.3e24 / 9.59e9 = 344e12/s ("about 340 trillion"); 344/990 = 0.35 ("about a third"); 344/1,980 = 0.17 ("a sixth").
- Table 7.4: +59%, +80% (79.4), +74%, +87%.
- l.254: 147,000 × $2 = $294,000.
- l.292: 49 Elo points → 1/(1+10^(−49/400)) = 57.0%.
- l.324: 3.3e24 / 1e25 = 0.33 ("a third").
- Fig 7.4: 416−183−102−68 = 63; 945−426−277−114 = 128 (matches figs_ch07.py).
- Fig 7.3 values in figs_ch07.py (360, 416, 485, 833, 868, 945, 1,008) match l.151–153.

### Opening and 7.1 How AI accelerators work
- AESO 4 Jun 2025: interim limit 1,200 MW; "more than 16 gigawatts" (see S7). (aeso.ca)
- TMI ~835 MW (IEA sec. 5.1, p. 47). (R1 and this round)
- DeepSeek-V3 report (arXiv 2412.19437 PDF):
  - 37B active, 14.8T tokens, 671B total.
  - FP8 "for the first time, validate... on an extremely large-scale model".
  - Hopper tensor cores keep "around 14 bits"; the limitation is called "the Hopper architecture's hardware deficiency".
  - FP8 test models trained on ~1T tokens, relative loss error "below 0.25%".
  - 2,048 H800s in nodes of 8 with NVLink/NVSwitch and InfiniBand.
  - 2,664K + 119K + 5K = 2,788K GPU-hours, $5.576M; "excluding the costs associated with prior research and ablation experiments".
  - "performance comparable to leading closed-source models".
- Nvidia Hopper in-depth blog: 80bn transistors, 814 mm², TSMC 4N; 132 SMs, 528 tensor cores; MMA quote; 2× MMA per SM vs A100; 5 HBM3 stacks, 10 × 512-bit controllers, 5,120-bit; FP8 "halves data storage requirements and doubles throughput"; 18 NVLink links, 900 GB/s; PCIe Gen 5 128 GB/s, 7×; TDP 700 W vs A100 400 W.
- Nvidia H100 product page: 80 GB; 3.35 TB/s; FP16/BF16 1,979 and FP8 3,958 TFLOPS "With sparsity".
- HGX page: FP16 36 PF and FP8 72 PF for 8× B200; "Dense is ½ sparse spec shown"; NVLink 1.8 TB/s per GPU.
- DGX B200 page: 1,440 GB total; 64 TB/s HBM3e.
- GB200 NVL72 page: NVFP4 1,440 | 720 PFLOPS (sparse | dense).
- Blackwell release (18 Mar 2024): 208bn transistors; "two-reticle limit GPU dies"; 10 TB/s chip-to-chip link; GB200 NVL72 "1.4 exaflops of AI performance", "30TB of fast memory"; FP4 with micro-tensor scaling.
- Rubin blog (Aubrey, 5 Jan 2026): up to 288 GB HBM4; up to 22 TB/s; "nearly triples memory bandwidth compared to Blackwell".
- Nvidia Q2 FY27 release: Vera Rubin "in full production" (R1). Q3 FY27 release (17 Nov 2026) says Vera Rubin NVL72 "has shipped", so the August statement in the text is not contradicted.
- Ironwood blog (9 Apr 2025): 4,614 TFLOPs per chip (FP8 in figure notes); 192 GB; 7.37 TB/s; ICI 1.2 TBps bidirectional; 9,216 chips; "over 24x the compute power of the world's largest supercomputer"; El Capitan 1.7 EF; perf/W 2× Trillium.
- TOP500 June 2025: El Capitan No. 1, Rmax 1.742 EF.
- Jouppi 2017 abstract: deployed since 2015; 65,536 8-bit MACs; "15X - 30X faster"; K80; GDDR5 "would triple achieved TOPS".
- Jouppi 2023 abstract: 4,096 chips; OCS; "1.2x-1.7x faster... than the Nvidia A100".
- Gholami IEEE Micro abstract: 3.0×, 1.6×, 1.4× per 2 years; memory the bottleneck for decoder models, "particularly in serving".
- GPTQ (ICLR 2023): 175B in about four GPU-hours, 3 or 4 bits, "negligible accuracy degradation", single GPU.
- AWQ (MLSys 2024 Best Paper): "Protecting only 1% salient weights can greatly reduce quantization error"; TinyChat on desktop and mobile GPUs.
- gpt-oss-120b model card: 117B/5.1B; MXFP4 MoE weights; single 80 GB GPU; 20b "within 16GB of memory"; Apache 2.0.
- gpt-oss arXiv model card: "large-scale distillation and reinforcement learning".
- Gemma 3 report: 1–27B; "trained with distillation".
- Leviathan et al. (ICML 2023): 2×–3× speed-up, "identical outputs".
- Anthropic prompt caching: "reducing costs by up to 90% and latency by up to 85% for long prompts".
- Kimi K3 card: 2.8T / 104B; MXFP4 weights.
- AI Index 2026 PDF: 17.1M H100e; 3.3×/yr; Nvidia >60%; Google and Amazon (R1).
- Nvidia FY2026 10-K: $215.9bn revenue; data centre $193.7bn vs $47.5bn (R1).

### 7.2 Supply chain
- AI Index (R1): barriers at every layer; TSMC "fabricates virtually every leading AI chip"; ASE/Amkor; HBM makers SK Hynix, Samsung, Micron.
- TrendForce (2 Jun 2025): Synopsys 31%, Cadence 30%, Siemens 13% in 2024 = 74%.
- BIS Aug 2022 rule (87 FR, govinfo): ECCN 3D006 ECAD for GAAFET "effective October 14, 2022".
- Cadence 8-K: BIS letter of 23 May 2025; rescinded 2 July 2025.
- ASML 20-F: "currently the world's only manufacturer of EUV lithography systems". R1 also confirmed: 327 systems, 48 EUV; China 29.1% vs 36.1%; Zeiss sole supplier and capacity quote; NL Jan 2025 metrology/inspection; EU Nov 2025 incl. DUV immersion.
- TSMC 20-F (FY2025): HPC 58% of 2025 revenue, 43% in 2023; ten largest customers 78%, largest 19%; capacity in Arizona, Kumamoto, Dresden.
- Rhodium (14 Dec 2022): "well over two trillion dollars in economic activity at risk", blockade, before sanctions or military escalation.
- Nvidia 10-K: CoWoS (R1).
- IEA Key Questions (R1): packaging 2025 / memory H2 2025; <150 GB → >1,000 GB; HBM 3× wafer capacity; prices up an order of magnitude; "through at least the end of 2027"; helium Box 1.1; transformers 2–3 years, turbines ~5 years; turbine orders +70%.

### 7.3 Export controls
- BIS 2022/2023 rules: Nvidia 8-K 17 Oct 2023, A100–RTX 4090 list quoted exactly. BIS 2024 rule abstract: "adding new controls for certain high bandwidth memory".
- Nvidia FY2026 10-K: H20 licence wording "memory bandwidth, interconnect bandwidth, or combination thereof"; China incl. HK $19,677m (FY26) vs $25,048m (FY25); HQ basis. R1 also: $4.5bn charge; ~$60m H20 revenue; 15% expectation; Chinese government discouraged purchases; 22% and 14% customers.
- BIS diffusion rule abstract (90 FR 4544): "adds a new control on artificial intelligence (AI) model weights for certain advanced closed-weight dual-use AI models".
- BIS 13 May 2025 release: "would have stifled American innovation"; non-enforcement; replacement promised; compliance date 15 May.
- BIS 31 May 2026 guidance (PDF): licence required for D:5/Macau-headquartered entities wherever located.
- BIS H200 rule (91 FR 1684, 15 Jan 2026): presumption of denial → case-by-case; independent third-party testing in the US.
- BIS UAE rule (91 FR 43034, effective 10 Jul 2026): "license-free access to advanced computing items".
- BIS Affiliates rule (90 FR 47201): 50% ownership. Suspension (90 FR 50857, effective 10 Nov 2025): "set to end November 9, 2026". Extension (91 FR 70789, 9 Nov 2026): see M1.
- BIS remote-access IFR (91 FR 74970, 19 Nov 2026): see M2.
- White House fact sheet (1 Nov 2025): China suspends Oct 2025 rare-earth controls; US suspends the Affiliates rule from 10 Nov 2025 for one year.
- AP via WXYZ: Bessent on Fox, truce extended "to Jan. 10" (Sep 2026). MOFCOM readout of 28 Sep 2026 confirms the extension of the KL arrangement to 10 Jan 2027.
- CSET translation of MOFCOM Notice 46 (3 Dec 2024): gallium, germanium, antimony, superhard materials "In principle... not permitted".
- Evertiq (10 Nov 2025): suspension "until November 27, 2026". MOFCOM 2026 announcement list and trade press of 31 Oct and 17 Nov 2026: no extension found (S1).
- Amodei essay (Jan 2025): "serve a vital purpose"; "are the only thing that can prevent China from getting millions of chips"; "an expected point on an ongoing cost reduction curve".
- Anthropic (30 Apr 2025): argued for strengthening the rule (lower Tier 2 thresholds, more BIS enforcement funding).
- Reuters (21 May 2025, via AOL/Fortune/The Standard): Huang "the export control was a failure"; buyers pushed to Huawei.
- DOJ (8 Dec 2025): Houston company Hao Global LLC and its owner pleaded guilty; "at least $160 million" of H100 and H200.
- House roll call 13 (12 Jan 2026): H.R. 2683 passed 369–22. Trackers show it referred to Senate Banking, with no later action found.
- Bloomberg via Bloomberg Tax: Kessler testimony, "just 200,000" Ascend chips in 2025. Bloomberg via Gulf News: "as many as 1.6 million dies" in 2026, "people familiar with the matter".
- AI Index: "has effectively closed" (R1). IEA Box 10.1 "compute-constrained" (R1).

### 7.4 Data centres, electricity and water
- R1 confirmed:
  - IEA Key Questions: +17% to 485 TWh, ~1.5%, AI-focused +50%, ~950 TWh / ~3% in 2030, AI-focused tripling; scenarios; 20–30% local; Table A.1 and A.4 values; "slightly less than 10%"; 5–10 year grid waits and the "not a reliable indicator..." quote; 20 projects / $98bn; ~40% of PPAs; 15–27 GW onsite gas; ~350 Mt / ~2%; 30–40% perf/W; PUE 1.1–1.2 vs 1.5–1.7; Jevons; video "hundreds to thousands of times more energy"; "by at least an order of magnitude annually".
  - IEA Powering AI: ~34% of identified capacity (p. 31), "nearly 40%" (p. 9), cooling caveat, G7 France, 14 Oct 2026.
  - LBNL 2024 report: 60 TWh 2014–16; 176 TWh, 4.4%; 325–580 TWh, 6.7–12%; data-limitation quote; 74% of rated TDP; inference ~60%; water 21.2bn L, 66bn L, 60–124bn L.
  - LBNL 2025 Update: 649 TWh, 11.8%, 521–843 TWh, 9.5–15.3%.
  - CSO Ireland: 23% in 2025, 5% in 2015.
  - Google 2026 Environmental Report: +37% electricity; market-based −3% to ~2.8 Mt; location-based 15.15 Mt, 2.93× 2019; 41bn L, +34%. Google 2025 report: Waltham Cross air cooling.
  - AI Index: AlexNet 0.01 t; Grok 4 72,816 t; DeepSeek-V3 597 t; GPT-4o 0.42 Wh; water 1.3–1.6 million kL, 1.2 million people.
- IEA Key Questions PDF (Régie mirror), this round:
  - Microsoft/Constellation TMI ~835 MW PPA (2024).
  - AWS–Talen Susquehanna PPA (2025).
  - SMR pipeline 45 GW (20 GW announced Jan 2026); first SMRs "around 2030" (sec. 5.1, pp. 47–48).
  - "less formal off-take arrangements... not yet backed by firm financing" (sec. 7.3, p. 65; see S4 on the pinpoint).
- Elsworth et al. (arXiv 2508.15734): median Gemini Apps text prompt 0.24 Wh, May 2025; narrow boundary 0.10 Wh; 33× energy and 44× carbon reduction over a year; 0.26 mL.
- Altman, "The Gentle Singularity": "the average query uses about 0.34 watt-hours".
- Epoch (You, 7 Feb 2025):
  - ~0.3 Wh; 500 output tokens; H100; ~10% utilisation.
  - Range "as low as about 0.1" to 4 Wh; 10k-token input ≈ 2.4–2.5 Wh.
  - 3 Wh traced to de Vries 2023, based on 2,000 output tokens, A100 and peak power.
- de Vries, Joule 7(10):2191–2194 (Crossref).
- Luccioni, Jernite, Strubell, FAccT 2024 (Crossref; arXiv); "over 60 times" (R1).
- Li et al., CACM 68(7) 2025 (Crossref): GPT-3 training "700,000 liters"; 4.2–6.6 billion m³ withdrawal in 2027.
- Rosa et al., ES&T 60(39):27780–27791 (Crossref abstract): 9,347 data centres; 25% under 2001–2010 conditions; 33% future.
- Mistral (22 Jul 2025): 1.14 gCO₂e, 45 mL, 400-token response, Carbone 4 and ADEME, upstream manufacturing included (see S5 on Le Chat).
- PJM market monitor via APPA (6 Jun 2025): "almost entirely the result of large load additions from data centers".
- SELC (8 May 2026): 35 turbines in 9 Apr 2025 photos; permit application for 15; approval 2 Jul 2025; appeal 16 Jul 2025.

### 7.5 Costs and concentration
- Table 7.4, from SEC XBRL (10-K values):
  - Amazon $83.0bn (2024) → $131.82bn (2025).
  - Microsoft $64.55bn (FY25) → $115.95bn (FY26).
  - Alphabet $52.53bn → $91.45bn.
  - Meta $37.26bn → $69.69bn.
- Microsoft FY2026 10-K: "additional leases, primarily for datacenters, that had not yet commenced of $329.1 billion... subject to certain contractual conditions... commence between fiscal year 2027 and fiscal year 2033".
- IEA (R1): $715bn, +75%, > US energy sector 2024; absorbs almost all cash generation; ~$200bn debt; $3.9tn; "too large to be funded solely..."; "running ahead of AI monetisation"; threefold users / fivefold revenue.
- Cottier et al. 2024 (arXiv 2405.21015): amortised-cost method; >$1bn by 2027 trend.
- Epoch Grok 4 ~$388m is consistent with ch04 Table 4.3.
- International AI Safety Report 2026 (arXiv 2602.21012 PDF): "leading models cost hundreds of millions of dollars to develop".
- Nvidia–OpenAI release (22 Sep 2025): "letter of intent"; "up to $100 billion"; "progressively as each gigawatt is deployed".
- Reuters via RTÉ (27 Feb 2026): $110bn round; "$30 billion from chip giant Nvidia".
- Bloomberg via Bloomberg Law (4 Mar 2026): Huang, "probably not in the cards".
- BoE FPC record (2 Dec 2025): "materially stretched, particularly for technology companies focused on Artificial Intelligence"; debt "increasing quickly".
- Epoch (12 Mar 2025): 9× to 900× per year.
- AI Index (R1): 91.2%; OpenAI 20 / Google 14 / Alibaba 11; >10× data centres. Nvidia 10-K (R1): 22% and 14% direct customers.
- AI Index PDF: transparency "declined in 2025"; FMTI average 58 → 40 ("AI companies grew less transparent").
- DeepSeek-R1 model card: MIT; distilled Qwen and Llama versions; "distillation for training other LLMs" permitted.
- Nature (Crossref): Guo et al., Nature 645:633–638, 17 Sep 2025.
- The Register (19 Sep 2025), reading the R1 SI: 101k + 41k + 5k ≈ 147k H800 GPU-hours, ~$294k; A100s for preparatory experiments (Reuters via CTV/BNN).
- Nvidia 27 Jan 2025: −17%, ~$589–593bn (Bloomberg, NBC, ThePrint; Guardian excerpt "nearly $600bn").

### 7.6 Open-weight models
- IASR 2026: GPT-NeoX "Fully open... no use restrictions", BLOOM "with use restrictions" (Table 3.9); closed lead "less than one year"; weights "cannot be recalled"; hosting platforms can remove copies; adaptation for "underresourced minority languages"; data filtering "10 times more effectively than defences added after training".
- OSI OSAID 1.0: four freedoms; data information so "a skilled person can build a substantially equivalent system"; complete training code; parameters.
- Meta Llama 2 post (18 Jul 2023): "free of charge for research and commercial use". Llama 2 licence: 700 million MAU clause.
- Mistral 7B (27 Sep 2023): Apache 2.0.
- IEA Box 10.1 downloads quote (R1). gpt-oss "first open-weight models since GPT-2" (IASR).
- Kimi K2 (arXiv 2507.20534): 1T total / 32B active; MuonClip. Kimi K3: 2.8T / 104B; launched 16 Jul 2026 at WAIC, weights 27 Jul 2026 (Beijing government news; trade press).
- MiniMax-M2 card: 230B / 10B (Oct 2025).
- Qwen3.5-397B-A17B card: 397B / 17B; Apache 2.0; layout 15 × (3 × Gated DeltaNet + 1 × Gated Attention), i.e. three in four layers linear; Feb 2026.
- GLM-5 card: 744B / 40B; MIT; Feb 2026.
- DeepSeek-V4-Pro card: 1.6T / 49B; MIT; 1M context; repo April 2026; arXiv 2606.19348.
- The Batch (23 Oct 2026): Muse Spark proprietary in spring 2026; 816B / 42B; Muse Model License up to $20m revenue; "Built with Muse Spark Open" attribution; "the top open weights model outside China", still behind MiMo-V2.6-Pro and GLM-5.3.
- Meta (15 Oct 2026): release date and licence (see M4).
- Table 7.5 licences:
  - Llama 4 licence and AUP: 700M MAU; "Built with Llama"; EU clause for multimodal models, with the end-user exception.
  - Gemma Terms (modified 1 Apr 2026): restrictions to be passed on (3.1); Google may restrict use (3.2).
  - Mistral Large 2411: "mrl" licence (HF), MRL research licence text.
  - DeepSeek-V3 original DeepSeek License v1.0 (use-based restrictions); V3-0324 MIT.
  - Qwen3-235B-A22B: Apache 2.0.
  - Kimi K3 License: $20m MaaS revenue over 12 months; display "Kimi K3" above 100M MAU or $20m monthly revenue.
- Epoch (4 Nov 2024): 5 to 22 months (90% CI), "around one year". Epoch (29 May 2026): four-month average lag since January 2026. AI Index (R1): Arena gap 174 → 7 → 49 (Claude Opus 4.6 vs GLM-5).
- Kapoor et al.: 25 authors; five properties; benefits (abstract); cyber marginal risk "low"; NCII "pose considerable marginal risk at present"; Thiel et al.: "most of CG-CSAM is based on the Stable Diffusion series".
- Action Plan (Jul 2025): open models "have geostrategic value"; "full AI technology stack".
- Lermen et al.: "a budget of less than $200 and using only one GPU"; ~1% refusals on two benchmarks.
- Qi et al.: GPT-3.5 Turbo, 10 examples, "< $0.20".
- Tamirisa et al.: TAR; "hundreds of steps of fine-tuning".
- NTIA (30 Jul 2024): "current evidence is not sufficient to definitively determine"; "actively monitor".
- Wallace et al.: MFT gpt-oss below o3, which is "below Preparedness High"; ICLR 2026 (iclr.cc poster page).
- Seger et al.: "should not be open-sourced, at least not initially"; open-sourcing has historically brought substantial net benefits.

### 7.7 Compute governance and sovereign AI
- Sastry et al. (arXiv 2402.08797): 19 authors incl. Bengio; "detectable, excludable, and quantifiable"; "an extremely concentrated supply chain".
- Heim et al.: compute providers can use "information that is already available" for workload classification and compute accounting.
- Shavit: on-chip firmware "occasionally save snapshots of the... weights"; supply-chain monitoring.
- EU AI Act Art. 51(2) presumption at 10^25 FLOP (consistent with ch13).
- EC IP/25/467 (Feb 2025): €200bn; €20bn fund; "four future AI gigafactories"; "around 100 000 latest-generation AI chips" (see M5).
- EuroHPC (30 Jul 2026): up to seven; selection early 2027 (see M5).
- PIB India (Feb 2026): "more than 38,000 high-end GPUs have been onboarded".
- AI Index (R1): "AI sovereignty emerged as a central organizing principle"; $285.9bn vs $12.4bn.
- BIS UAE rule (above).

## Tally
- Claims checked against a web source: 236. Round 1: about 108 (IEA, LBNL, AI Index, Google, ASML, Nvidia, CSO, BIS). This round: 128.
- Confirmed: 222.
- Wrong: 0 outright factual errors in the text as written for its date.
- Outdated: 5: Affiliates-rule extension; diffusion-rule rescission and remote-access rule (several sentences); Huang's resignation; EU "four gigafactories"; Nvidia China shipments (SHOULD).
- Unsupported by cited source: 3: Muse Spark Open citation (l.49, l.271); IEA nuclear pinpoint (S4); Mistral "Mistral Large 2" vs Le Chat (S5, minor).
- Minor imprecision: 1 (AESO "more than 16 GW").
- Could not verify: 3 (one matters slightly: the TSMC CoWoS quotation).
- Arithmetic items recomputed: 27 (errors: 0).
- Bib entries checked: 72 (problems: 2). `meta2026muse` does not support the claims it is attached to (M4). `google2026gemma` URL now redirects to https://gemma.ai/resources/terms/; update the url.
- New bib entries required: bis2026extension, bis2026addressing, thenational2026china, meta2026museopen. Optional: nvidia2026q3cfo, qwen2026qwen38.
