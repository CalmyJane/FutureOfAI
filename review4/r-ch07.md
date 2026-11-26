# Chapter 7 review: Chips, Data Centres, Energy and Open Models

## Verdict
Ready after the fixes. The chapter is careful, well sourced and the arithmetic holds throughout (FLOP count, roofline intensity, decode latency, FP format maxima, TPP, Elo-to-probability, GPU-hour and capex percentages all recomputed correctly). There are two small factual errors to fix: one misquotation of Google, and an overstatement about how Kimi K3 was trained. The SHOULD items are about precision and about agreeing with Chapters 13 and 14. One item depends on timing: the gallium/germanium suspension expires on 27 November 2026, the day after this review.

## MUST change before printing

### M1. Google Ironwood quotation is not word for word
- Where: textbook/chapters/ch07.md:43
- Text now: "Google described its 2025 Ironwood TPU pod as offering "over 24x the compute power" of El Capitan"
- Problem: MISQUOTED. Google's wording is "more than 24x the compute power", not "over 24x".
- Evidence: https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/ (9 April 2025): "Ironwood supports more than 24x the compute power of the world's largest supercomputer – El Capitan –"
- Change to: "Google described its 2025 Ironwood TPU pod as supporting "more than 24x the compute power" of El Capitan"

### M2. Kimi K3 was not "trained" in 4-bit; it was quantisation-aware post-trained
- Where: textbook/chapters/ch07.md:49
- Text now: "Kimi K3 was trained and published with 4-bit (MXFP4) weights"
- Problem: VERIFIED WRONG (overstated). According to the model card, quantisation-aware training applies only from the SFT stage onward. Nothing says pre-training used 4-bit weights.
- Evidence: https://huggingface.co/moonshotai/Kimi-K3 (model card, read 26 Nov 2026): "applies quantization-aware training from the SFT stage onward, using MXFP4 weights with MXFP8 activations"; quantisation field: "MXFP4 weights / MXFP8 activations (quantization-aware training)".
- Change to: "Kimi K3 was post-trained with 4-bit (MXFP4) weights, using quantisation-aware training from the fine-tuning stage onward, and published in that format"

## SHOULD change

### S1. Microsoft did not contract to restart Three Mile Island
- Where: textbook/chapters/ch07.md:3
- Text now: "the Three Mile Island nuclear unit that Microsoft has contracted to restart, about 835 megawatts"
- Problem: UNCLEAR/INCONSISTENT. Constellation is restarting the unit. Microsoft signed a 20-year agreement to buy its power. Line 193 of the same chapter has it right ("agreed to buy power from a restarted Three Mile Island unit").
- Change to: "the Three Mile Island nuclear unit that is being restarted to supply Microsoft, about 835 megawatts"

### S2. "First use of export controls to block access to an AI service" is stated as fact here but attributed elsewhere
- Where: textbook/chapters/ch07.md:135
- Text now: "in the first use of export controls to block access to an AI service"
- Problem: INCONSISTENT. Chapters 13 (line 144) and 14 (line 167) attribute this description to law firms ("first known use"). The facts in the sentence check out: a letter on 12 June 2026, the models switched off worldwide, and the control lifted with conditions on 30 June. Sources: Mayer Brown, 30 June 2026; Al Jazeera, 1 July 2026, "Anthropic said late on Tuesday that the Commerce Department had removed its export controls".
- Change to: "in what law firms described as the first known use of export controls to block access to an AI service" (add @mayerbrown2026commerce, already in the ch13 bib, to the ch07 bib)

### S3. Gallium/germanium suspension expires 27 November 2026: re-check before printing
- Where: textbook/chapters/ch07.md:138
- Text now: "until 27 November 2026; ... no extension had been announced by 22 November"
- Problem: OUTDATED soon. The statement is accurate as dated, and a search on 26 Nov 2026 found no extension announced. The suspension lapses the day after this review, so the sentence will be stale in print either way.
- Change to (if nothing is announced): "...it suspended that ban in November 2025, as part of the same truce, until 27 November 2026, and China's November 2026 extension of its other truce measures to 10 January 2027 did not cover it." If MOFCOM announces an extension, state it.

### S4. 2030 Base Case given as "about 950" here and "945" in Chapter 14
- Where: textbook/chapters/ch07.md:152 (vs ch14.md:135)
- Problem: INCONSISTENT. The IEA's headline is 950 TWh, and its Annex Table A.4 gives 945, which ch07 line 158 itself uses. Readers will see both numbers.
- Change to: ch14.md:135 "projects about 950 TWh (945 TWh in its data tables) in its base case".

### S5. PJM monitor quotation is attached to the wrong subject
- Where: textbook/chapters/ch07.md:189
- Text now: "record capacity prices, which feed into consumers' bills, were "almost entirely the result of large load additions from data centers""
- Problem: MISQUOTED (minor). The monitor's subject was "the current conditions in the capacity market", not prices.
- Evidence: https://www.publicpower.org/periodical/article/pjm-market-monitor-highlights-key-role-data-centers-driving-capacity-market-conditions (6 June 2025): "The current conditions in the capacity market are almost entirely the result of large load additions from data centers"
- Change to: "the independent market monitor concluded in June 2025 that the conditions behind record capacity prices, which feed into consumers' bills, were "almost entirely the result of large load additions from data centers""

### S6. Qwen3.8 "second-largest open-weight model" is the author's inference
- Where: textbook/chapters/ch07.md:272
- Problem: UNSUPPORTED. The model card makes no such claim. It says the model "brings a Qwen-Max-class model to open release". The ranking is true only among the models in Table 7.5 (Kimi K3 2.8T > Qwen3.8 2.4T > DeepSeek-V4-Pro 1.6T).
- Change to: "is, after Kimi K3, the largest model in Table 7.5 and the first Qwen flagship..."

### S7. Repetitive Mistral sentence
- Where: textbook/chapters/ch07.md:205
- Text now: "Mistral AI's life-cycle assessment, made with the consultancy Carbone 4 and the French agency ADEME, gives 45 millilitres ... for a 400-token response from its Le Chat assistant, in a life-cycle assessment of its Mistral Large 2 model, including upstream impacts"
- Problem: UNCLEAR. It says "life-cycle assessment" twice.
- Change to: "Mistral AI's life-cycle assessment of its Mistral Large 2 model, made with the consultancy Carbone 4 and the French agency ADEME, gives 45 millilitres (and 1.14 grams of CO~2~-equivalent) for a 400-token response from its Le Chat assistant, including upstream impacts such as hardware manufacturing"

### S8. Nvidia China outlook: say "compute" and add the Q4 outlook
- Where: textbook/chapters/ch07.md:132
- Problem: UNCLEAR (minor). Nvidia's wording is "Data Center compute revenue from China". The Q3 CFO commentary (17 Nov 2026) repeats the assumption for Q4: "We are not assuming any Data Center compute revenue from China in our outlook." It also confirms "Shipments of Data Center Hopper products to China during the quarter were $2.4 billion."
- Change to: "Its outlooks for the following quarters assumed no data-centre compute revenue from China, although in the quarter to October 2026 it shipped $2.4 billion of Hopper data-centre products there"

## Could not verify
- The "4-bit version" of Muse Spark Open (line 49). Meta's blog does not mention precisions, and *The Batch* mentions only running it at 4-bit.
- Nvidia's China-headquartered revenue of $25.0bn (FY25) and $19.7bn (FY26). The parts of the 10-K I could read give only the non-US share (31%/41%).
- Microsoft FY2026 cash capex of $115.9bn. The $329.1bn in uncommenced leases is confirmed.
- 9-month 2026 capex for Amazon, Alphabet and Meta.
- IEA *Key Questions* quotations, word for word (iea.org returned 403). The headline figures (485 TWh, +17%, 950 TWh, ~3%, +50% for AI-focused, 1.5%) are confirmed through the IEA summary and press coverage.
- Google 2026 Environmental Report figures (37%, 2.8 Mt, 15.1 Mt, 41 bn litres).
- Rosa et al. 2026 (9,347 data centres); IEA *Powering AI* (34% / "nearly 40%").
- The AI Index 2026 figures: 17.1M H100e, 91.2%, $285.9bn vs $12.4bn, Grok 4 emissions. Chapter 4 uses the same figures.

## Checked and confirmed
- Jensen Huang described as "then" CEO: he resigned in mid-November 2026, and Colette Kress is interim CEO (several reports; Nvidia Q3 CFO commentary refers to "our leadership transition"). Both uses (lines 142, 243) are correct.
- Anthropic Fable 5/Mythos 5: letter of 12 June, all customers switched off, partial exemption on 26 June, control removed on 30 June (Mayer Brown; Al Jazeera).
- BIS remote-access interim final rule of 19 Nov 2026: rescinds the diffusion rule, D:5-headquartered scope, and adds Indonesia, Malaysia, Singapore, Thailand and Brazil (law-firm alerts).
- Nvidia 10-K: $215.9bn revenue (+65%); DC +68% (≈$193.7bn); direct customers 22% and 14%; $4.5bn H20 charge; ~$60m H20 revenue; "15% or more". Q2 FY27 release: "Vera Rubin, now in full production"; no China DC compute revenue assumed.
- Hopper blog: tensor core quote, FP8 quote, 132 SMs and 528 TCs, 5 HBM3 stacks and 10×512-bit, 900 GB/s = 7× PCIe Gen 5, 700 W, 2× MMA per SM clock-for-clock.
- Ironwood: 4,614 TFLOPs, 192 GB, 7.37 TB/s, 1.2 TBps, 2× perf/W, 9,216 chips, FP8 footnote.
- Amodei quotations (all three) word for word; Rhodium "well over two trillion dollars in economic activity at risk"; Bank of England quote word for word.
- Kimi K3 2.8T/104B and licence ($20m MaaS, display rule); Qwen3.8 2.4T/95B and licence ($50m MaaS/AI Work Assistant, display rule); Muse Spark Open 816B/42B, 15 Oct 2026, Muse Model License, $20m; *The Batch* ranking; Muse Spark proprietary in spring 2026.
- Ireland CSO: 23% (2025), 5% (2015). LBNL 2025 Update: 649 TWh, 11.8%, 521–843 TWh, 9.5–15.3%, June 2026.
- ASML: 48 EUV and 327 systems in 2025 (consistent with ASML results).
- Arithmetic: 6×37e9×14.8e12 = 3.29e24; 990/3.35 ≈ 295 FLOP/byte; 140 GB / 3.35 TB/s = 42 ms; FP maxima (3.40e38, 65,504, 3.39e38, 448, 57,344); TPP 1,979×8 = 15,832, density 19.4/mm²; 2.664M+0.124M = 2.788M GPU-h × $2 = $5.576M; 3.3e24 / 9.59e9 s = 344 TFLOPS ≈ ⅓ of 990; Elo 49 → 57.0%; PUE 1.6→1.2 = −25%; capex changes +59/+79.4(≈80)/+74/+87%; LBNL 176/154 = +14%; B200 per-GPU figures from HGX/DGX ÷ 8.
- Cross-references: Section 4.1 (3.3e24), 4.4 / Table 4.3 (Grok 4 $388m), Chapter 4 quantisation note (Kumar et al.), Section 12.3, Chapter 13 thresholds. All bib keys resolve.

## Tally
Claims checked: 96 / confirmed: 78 / wrong: 2 (M1, M2) / outdated: 1 pending (S3) / imprecise or inconsistent: 7 (S1, S2, S4–S8); 8 could not be verified.
