# Third review: Chapter 4 — Scaling, Compute and the Limits of Progress

## Verdict
Ready after the MUST fixes below. The chapter is unusually well sourced: every number I recomputed (6ND, GPU-hours, the Chinchilla and Besiroglu loss values, the Table 4.2 and 4.3 values, the METR doubling times, the ARC-AGI cost ratio) is correct, and the Epoch, METR, Llama 3, Kaplan and Chinchilla figures match their sources to the digit. Four statements must change before print. Two are now out of date: Epoch replaced its trends dashboard on 5 November 2026 and dropped the "installed stock 3.4×/yr" figure, and ClockBench has a new leader since 9 November. One "best score" claim about Humanity's Last Exam (HLE) is contradicted by OpenAI's own published table. One sentence misstates Chinchilla's projection for a GPT-3-sized model. The SHOULD items are small precision and fairness fixes.

## MUST change before printing

### M1. Epoch dashboard date and the "installed stock 3.4×" figure are outdated
- Where: textbook/chapters/ch04.md:120 (also bib `epochai2026trends`)
- Text now: "Epoch's dashboard, last updated on 5 February 2026, puts the growth of training compute …" and "The installed stock of AI computing power is growing more slowly, at 3.4 times per year since 2022 by Epoch's estimate [@epochai2026trends]."
- Problem: OUTDATED. The dashboard now reads "Updated Nov. 5, 2026". Its training-compute (5×/yr, 90% CI 4–6×, 5.2 months, ~10,000× for the top-5 models), cost (3.5×/yr), chip price-performance (1.49×/yr), 30% inference share and ECI (14 vs 6 points/yr) figures are unchanged. The compute-stock tile (3.4×/yr since 2022) has been removed. In its place is "New compute growth 2.5×/year: The aggregate computing power of AI chips sold each quarter is growing at a rate of 2.5×/year … since 2024. That's down from roughly 6× in 2023." The book's citation therefore no longer supports 3.4×.
- Evidence: https://epoch.ai/trends (fetched 22 Nov 2026): "Updated Nov. 5, 2026 … New compute growth 2.5 ×/year 9 months … 90% CI 2.3× to 2.7×". Also Epoch data insight, 29 Oct 2026, https://epoch.ai/data-insights/ai-computing-capacity-additions-doubling: "The fitted trend is 2.5× per year (90% CI: 2.3× to 2.7×) … cumulative capacity grew 2.6× between Q2 2025 and Q2 2026."
- Change to: "Epoch's dashboard, last updated on 5 November 2026, puts the growth of training compute for frontier language models at 5 times per year since 2020 (90% CI 4 to 6 times), a doubling every 5.2 months." … "The supply of AI computing power is growing more slowly. By Epoch's estimate, the computing power of the AI chips sold each quarter has grown about 2.5 times per year since 2024, down from about 6 times in 2023 [@epochai2026trends]. The 2026 AI Index, drawing on Epoch's data, puts the growth of total capacity at 3.3 times per year since 2022 and global capacity at the equivalent of 17.1 million Nvidia H100 chips [@sajadieh2026ai]."
- Bib: `epochai2026trends` howpublished → `{Epoch AI website (dashboard dated 5 November 2026)}`, urldate → `2026-11-22`.

### M2. ClockBench "best model" superseded by the 9 November releases
- Where: textbook/chapters/ch04.md:229 (the same claim appears at ch01.md:253 and should be changed with it)
- Text now: "On ClockBench, which asks models to read analogue clocks, the average human scores 90.7%; the best model in October 2026, Google's Gemini 4 Argon, scored 83.3%, up from about half in March 2026 (Section 1.8)"
- Problem: OUTDATED. The leaderboard is now topped by Claude Fable 5.2 Max at 87.8%, followed by Gemini 4 Carbon High at 85%. Gemini 4 Argon High is third at 83.3%. Gemini 4 Carbon was announced on about 28 October with restricted access and became generally available on 10 November, so even the "October" wording is uncertain.
- Evidence: https://clockbench.ai/ (fetched 22 Nov 2026): "Average Human Performance 90.7% · 1 Claude Fable 5.2 Max 87.8% Anthropic · 2 Gemini 4 Carbon High 85% Google · 3 Gemini 4 Argon High 83.3% Google". The March 2026 figure (GPT-5.4 High, 50.6%) is confirmed in AI Index 2026.
- Change to: "On ClockBench, which asks models to read analogue clocks, the average human scores 90.7%; in November 2026 the best model, Anthropic's Claude Fable 5.2 at its highest setting, scored 87.8%, up from about half in March 2026 (Section 1.8) [@clockbench2026clockbench; @sajadieh2026ai]." Bib `clockbench2026clockbench`: accessed/urldate → 22 November 2026. Align ch01.md:253 ("By November 2026 the leading model scored 87.8% …").

### M3. "Best reported scores on HLE … 54.8%" is contradicted by vendor-reported scores
- Where: textbook/chapters/ch04.md:258
- Text now: "The best reported scores on HLE rose from 13.4% to 54.8% in under two years, although the two figures come from different evaluation set-ups"
- Problem: VERIFIED WRONG. 54.8% is the top score on Scale AI's leaderboard, which tests without tools, and it is still the top entry there on 22 Nov. But OpenAI's own GPT-6 Astra page reports higher HLE scores with tools: Claude Fable 5.1 65.0%, Claude Fable 5 63.8%, Claude Opus 5 63.6% and GPT-6 Astra 57.2%. So 54.8% is not the best reported score. The main text at line 231 is correct, because it speaks of the leaderboard.
- Evidence: https://openai.com/index/gpt-6-astra/ (table "HLE (w/ tools)": GPT-6 Astra 57.2%, Claude Fable 5.1 65.0%, Claude Fable 5 63.8%, Claude Opus 5 63.6%); https://scale.com/leaderboard/humanitys_last_exam (fetched 22 Nov: "GPT 6 Astra … rank 1 … 54.80 ±1.94").
- Change to: "On HLE, the top score on Scale AI's independent leaderboard reached 54.8% within two years of the benchmark's release, against 13.4% for the best model in the original paper, although the two figures come from different evaluation set-ups, and developers report higher scores when models may use tools [@centerforaisafety2026benchmark; @scale2026humanity; @openai2026gpt6]."

### M4. Chinchilla's token projection for a GPT-3-sized model is misstated
- Where: textbook/chapters/ch04.md:82
- Text now: "A compute-optimal model of GPT-3's size, by the paper's estimates, would have needed roughly 4 trillion tokens, 3.7 trillion to 4.2 trillion depending on the method."
- Problem: VERIFIED WRONG. For 175B parameters the paper's three methods give 3.7T (Approach 1, Table 3), 4.3T (Approach 2) and 12.0T (Approach 3, Table A3). The "4.2 trillion" is the separate main-text statement "on over 4.2 trillion tokens" with 4.41 × 10^24 FLOP. It is not the upper end of a range across methods.
- Evidence: arXiv 2203.15556, Sec. 3.4: "a 175 billion parameter model should be trained with a compute budget of 4.41 × 10^24 FLOPs and on over 4.2 trillion tokens"; Table 3 (Approach 1): 175 Billion → 3.7 Trillion; Table A3: Approach 2 → 4.3 Trillion, Approach 3 → 12.0 Trillion.
- Change to: "A compute-optimal model of GPT-3's size, the paper estimated, should have been trained on over 4.2 trillion tokens, fourteen times what GPT-3 saw."

## SHOULD change (real but not blocking)

### S1. Villalobos et al. capped the repetition multiplier at 5×
- Where: ch04.md:153. Text: "Villalobos and colleagues used this result to assume that repetition can multiply the effective size of a dataset by between 3 and 15 times".
- Problem: the paper cites Muennighoff's 3×–15× but writes that "the upper extreme of 15x would require a very inefficient training procedure … For this reason we reduce it to 5x" (PMLR/arXiv 2211.04325, Sec. 2.3.2). Its 320T figure (100T × ~3.2) reflects that cap.
- Change to: "Villalobos and colleagues took from this result that repetition can multiply the effective size of a dataset by 3 to 15 times, and capped the multiplier at 5 because more epochs would make training very inefficient [@villalobos2024position]."

### S2. Reasoning-effort controls predate 2025
- Where: ch04.md:193. Text: "Three kinds of control appeared in 2025: explicit budgets, automatic routing and parallel reasoning".
- Problem: OpenAI's o1 API (17 Dec 2024) already had "A new reasoning_effort API parameter allows you to control how long the model thinks before answering" (https://openai.com/index/o1-and-new-tools-for-developers/).
- Change to: "Three kinds of control spread in 2025: …"

### S3. Llama 3 case study: Meta's 402B/16.55T pair does not equal 3.8 × 10^25 under the 6ND rule
- Where: ch04.md:111. A reader who has just learned C ≈ 6ND (Section 4.1) gets 6 × 402e9 × 16.55e12 = 4.0 × 10^25. The pair is quoted correctly from the Llama 3 report, but the mismatch will puzzle careful readers.
- Change: after "about 41 tokens per parameter" add "(figures as Meta reports them; by the 6*ND* rule the pair corresponds to about 4.0 × 10^25^ FLOP)".

### S4. Chatbot Arena: give the platform's response (fairness)
- Where: ch04.md:227. The text reports Singh et al.'s findings with no reply from the platform. LMArena published a rebuttal disputing several figures and said it helped Meta and other providers with pre-release testing under a public policy (https://news.lmarena.ai/our-response).
- Change: add "LMArena, which runs the platform, disputed several of the paper's figures and said its pre-release testing was open to all providers."

### S5. o3-mini score needs its setting
- Where: ch04.md:249. "It still trailed the reasoning model o3-mini, which scored 87.3%". OpenAI's table gives 87.3% for "OpenAI o3-mini (high)". Given the chapter's own point that a score means something only together with its setting (line 199), write "o3-mini at its high reasoning setting, which scored 87.3%".

### S6. ARC Prize bib entry omits the cost revisions the text relies on
- Where: bib `arcprize2024openai` howpublished "ARC Prize blog, 20 December 2024 (updated 16 April 2025)". The text (line 187) uses the 10 December 2025 repricing. Change to "ARC Prize blog, 20 December 2024 (updated 16 April 2025; costs repriced 24 March and 10 December 2025)", urldate 2026-11-22.

### S7. Bib `yue2025does` drops an author
- arXiv 2504.13837 lists eight authors: Yue, Yang; Chen, Zhiqi; Lu, Rui; Zhao, Andrew; Wang, Zhaokai; Yue, Yang; Song, Shiji; Huang, Gao. The bib omits the second "Yue, Yang" (sixth author). Insert it after Wang, Zhaokai.

## Could not verify
- ch04.md:163, bib `gerstgrasser2024model`, venue "Conference on Language Modeling 2024". OpenReview (5B2K4LRgmz) returned a bot challenge, the COLM accepted-papers page is rendered in JavaScript, and searches turned up only the arXiv version and an ICML 2024 workshop poster. Low importance; a human could open the OpenReview link in a browser.
- ch04.md:229, Truong et al., "between 2 (on part of MMLU) and 42 (on GSM8K) proved flawed". The per-benchmark counts appear only as bar labels in Fig. 1 (graphic). The text confirms that "2% corresponds to one question" and "up to 84%" precision, i.e. at most 42 of 50 questions, which is consistent with "42". The AI Index 2026 summarises the same result as "2% … to 42%", which would mean 1 and 21 questions. The book's reading fits the paper better, but a human should check the bar labels (arXiv 2511.16842, Fig. 1 right) before print.
- ch04.md:229: whether Gemini 4 Carbon had a ClockBench score before 31 October. This is irrelevant if M2 is applied.
- `singh2025leaderboard` venue (NeurIPS 2025): searches found no proceedings listing. Not checked further.

## Reader notes
1. Line 111: "The extrapolation suggested 402 billion parameters on 16.55 trillion tokens". With the 6ND rule just taught, this comes to 4.0 × 10^25, not 3.8 × 10^25 (see S3).
2. Line 187: "100-task semi-private evaluation set". "Semi-private" is not explained. Half a clause would help ("held back from the public but run on vendors' servers").
3. Line 227: "Chatbot Arena". The platform has been called LMArena since 2025. Readers looking it up will find it under that name.
4. Line 225: "Accuracy fell by up to 8%" (percentage points). This follows the source, but readers may read it as a relative drop.
5. Line 13: "stays small only while the width of the model's internal vectors exceeds about a twelfth of that length". This is correct (Kaplan: d_model > n_ctx/12) but dense for a non-specialist and inessential.
6. Line 237: the paragraph gives five numbers in its last three sentences (17 h, 16 h, 129 days, sevenfold, 188 days). Splitting the last sentence would help.
7. Line 258 (debate box) repeats the HLE figures from line 231. Once M3 is applied, the two passages should use the same framing (leaderboard vs. vendor-reported).

## Checked and confirmed
(W = web/primary source opened; C = computed)

**Opening and §4.1**
- AlexNet "five to six days", two GTX 580 (NeurIPS paper); Epoch 4.7e17 FLOP (Epoch CSV) W
- Llama 3.1 405B: 16,384 H100s, 3.8e25 FLOP, 15.6T tokens, July 2024 (arXiv 2407.21783; Epoch CSV) W
- 466 interruptions in 54 days; ~78% confirmed or suspected hardware; manual intervention "only three times"; ">90% effective training time" (Llama 3 §3.3.4) W
- Ratio 3.8e25/4.7e17 ≈ 8.1e7 ("80 million") C
- 6 × 405e9 × 15.6e12 = 3.79e25 C
- DeepSeek-V3 671B/37B active/14.8T (arXiv 2412.19437); 3.29e24 = Epoch 3.3e24 "Confident" (Epoch note gives the same calculation) W, C
- 671/405 = 1.66; 3.3e24/3.8e25 = 0.087 C
- Kaplan attention term small when d_model > n_ctx/12 (Kaplan §2.1) W
- PaLM MFU 46.2%, HFU 57.8% (arXiv 2204.02311) W
- Llama 3 Table 4: 430/400/380 TFLOPs, 43/41/38% BF16 MFU W
- H100 FP8 peak = 2 × BF16 peak (Nvidia spec; Epoch GPT-4.5 note "2000 teraflop/s" FP8) W
- Epoch documentation: "Typical utilization rates for large distributed training runs are around 30-50%"; architecture counting "preferred" (epoch.ai/data/ai-models-documentation/estimation) W
- 26.4M GPU-hours, 67.1 days on 16,384 GPUs, gap 4.45M vs 30.84M C
- Model card 30.84M GPU-hours for 405B; "total GPU time required for training" (GitHub MODEL_CARD.md) W
- GPT-4.5: 187M H100-hours, 20–40% of FP8 2,000 TFLOP/s, 2.7–5.4e26, geomean 3.8e26 (Epoch CSV note) W; recomputed 2.66–5.33e26, geomean 3.77e26 C
- Epoch confidence tiers ×3 / ×10 / ×30 (Epoch notable-models page; documentation "±31x") W
- GPT-4 2.1e25 "Likely" (Epoch CSV) W
- AI Index 2026: parameter counts, dataset sizes etc. "no longer disclosed" (AI Index 2026 PDF) W

**§4.2**
- Sutton "The Bitter Lesson", 13 March 2019 (incompleteideas.net) W
- Hestness 2017: four domains; architectures change intercept, not exponent (arXiv 1712.00409) W
- Kaplan: 768 to 1.5B non-embedding params; "more than seven orders of magnitude"; αN 0.076, Nc 8.8e13; αD 0.095, Dc 5.4e13; αC 0.050, Cc 3.1e8 PF-days; 2^−αN = 0.95; "do not have a fundamental meaning"; "increase the model size 8x … data by roughly 5x"; "significantly short of convergence" (arXiv 2001.08361) W
- 2^−0.076 = 0.949; 10^−0.05 = 0.891; 8^0.74 = 4.66; 100^0.73 = 28.8; 100^0.27 = 3.47 C
- GPT-4 report: L(C) = aC^b + c; "at most 10,000x less compute"; "with high accuracy"; HumanEval "at most 1,000× less compute"; "may occasionally worsen with scale" (arXiv 2303.08774) W
- Llama 3: ARC Challenge two-step forecast, "only slightly underestimates", four orders of magnitude W

**§4.3**
- Chinchilla: >400 models, 70M–16B, 5–500B tokens; four token counts per model; 1,500 FLOP values; Table 2 exponents and 10th–90th percentile ranges (all 12 values in Table 4.1); 67.5% MMLU, ">7% improvement over Gopher"; 1T model needs ~1e26 FLOP (arXiv 2203.15556) W
- Chinchilla fit E 1.69, A 406.4, B 410.7, α 0.34, β 0.28 (paper; Besiroglu Table 1) W
- Gopher 1.69 + 0.052 + 0.251 = 1.993; 70B/1.4T 1.937 C
- Besiroglu refit E 1.8172, A 482.01, B 2085.43, α 0.3478, β 0.3658 W; gives 2.00 and 1.97, data/model term ratio 2.6 C
- Besiroglu: "over 600,000 experiments … fewer than 500"; Borgeaud explanation of early-stopping optimiser (v2); "approximately 70 tokens per parameter" (v1); refit "around 20" (v2) W
- Epoch: Chinchilla 5.76e23, Gopher 6.31e23 (from Gopher Table A26) W
- Kaplan used small models, "many being less than 100M" (Chinchilla §2) W
- Pearce & Song: non-embedding counting at small scale (arXiv 2406.12907) W
- Porian: three factors, "excellent agreement" (arXiv 2406.19146) W
- Clark 2022: expert benefit diminishes with size (arXiv 2202.01169) W
- Ludziejewski: granularity; MoE beats dense, gap widens (arXiv 2402.07871) W
- Sardana: ~1B requests; up to 10,000 tokens/parameter (arXiv 2401.00448) W
- Table 4.2 6ND values 3.15e23, 5.04e23, 5.88e23, 3.79e25, 7.2e23; ratios 1.7, 1.1, 20, 38.5, 1,875 C
- GPT-3 3.14e23 reported (Epoch CSV / GPT-3 paper) W
- 8B budget → 77B/1.55T at 20 tokens/param; 8/77 ≈ 0.10 C
- Llama 3 "much longer than is compute-optimal … same inference budget" W
- Kumar: >465 runs, ≤1.7B params, 7–8 bits (arXiv 2411.04330) W
- Llama 3 case study: 6e18–1e22 FLOP, 40M–16B, (α, A) = (0.53, 0.29), 402B/16.55T, flatter IsoFLOPs W; 41 tokens/param, 563B/11.3T at 20 tokens/param C
- 100^0.5 = 10 C

**§4.4**
- Sevilla 2022: 123 systems; ~20 months pre-2010; ~6 months; late-2015 large-scale era, 10–100× (arXiv 2202.05924; Crossref IJCNN) W
- Epoch trends (5 Nov 2026 version): 5×/yr, CI 4–6×, 5.2 months; ~10,000× top-5; three sources of growth; cost 3.5×/yr; 1.49×/yr since 2023; 30% inference; ECI +14/yr (CI 12–17) vs 6 W
- AI Index 2026: 3.3×/yr since 2022, 17.1M H100e W
- 3.8e26/3.14e23 = 1,210 C
- GPT-6 Astra: 9.4e26 "Likely", 2026-09-03, ≥100,000 GB200, 90 days at 25% FP8 MFU, CI ~[5e26, 2e27] (Epoch CSV note); still the largest estimate in the CSV on 22 Nov 2026 (GPT-6.2 Astra, Fable 5.2 and Mythos 5.2 have no compute estimate) W
- GPT-6 Astra "meets the Critical threshold in cybersecurity under our Preparedness Framework"; no compute figure (openai.com/index/gpt-6-astra; Vellum) W
- Fig. 4.2: all 13 values, dates and confidence labels match the Epoch CSV; 5 of 13 "Likely" W
- Cottier: 2.4×/yr since 2016 (90% CI 2.0–2.9); cloud "about twice as large"; staff 29–49%, hardware 47–64%, energy 2–6%; four models named; GPT-4 ~$40M (arXiv 2405.21015) W
- Table 4.3: all six compute values, confidence labels and costs (0.64M, 37.3M, 52.9M, 217.8M, 366.0M, 387.8M) (Epoch CSV) W

**§4.5**
- Villalobos: CC 130T, indexed web 510T, whole web 3,100T, quality-adjusted 100T, repetition-adjusted 320T [65T, 1,700T], 0.38 OOM/yr (≈2.4×), median 2028, 2026–2032, earlier if over-trained (arXiv 2211.04325) W
- 15.6/320 ≈ 1/20; 36/320 ≈ 1/9 C
- Qwen3 36T tokens; "thinking budget mechanism" (arXiv 2505.09388) W
- Muennighoff: 400 runs, 9B params, 900B tokens, 4 epochs "negligible changes to loss", ~16 epochs "diminish extremely fast" (arXiv 2305.16264) W
- Sevilla 2024: 400T–20 quadrillion tokens; 2e29 "will likely be feasible by the end of this decade"; power and chips binding (epoch.ai report) W
- FineWeb-Edu 1.3T of 15T (consistent with ch03 and Crossref NeurIPS 2024) W
- Edelman et al.: ~10× pre-training saving; RL environments as a limit (Epoch Gradient Updates, 26 Sep 2025) W
- Sutskever: "The data is very clearly finite", 25 Nov 2025; "age of scaling" 2020–2025 / "age of research" (dwarkesh.com) W
- Sutskever CEO of SSI from July 2025 (TechCrunch 3 Jul 2025); no change found to Nov 2026 W
- DeepSeek-R1: 800K samples; distillation (Nature/arXiv 2501.12948; Crossref) W
- Shumailov Nature 2024 (Crossref) W
- Gerstgrasser: replace vs accumulate; linear-model bound; molecules and VAEs (arXiv 2404.01413) W
- AI Index 2026: "still no definitive evidence"; hybrid and purely synthetic training for smaller models and narrow tasks W

**§4.6**
- Ho et al.: >200 evaluations, 2012–2023; NeurIPS abstract "90% confidence interval of around 2 to 22 months" (arXiv v1 gives 95% CI 5–14; book follows the published version); transformer 7.2× (neurips.cc poster 96565; arXiv 2403.05812) W; 7.2× ≈ 22.8 months C
- AI Index 2025: MMLU 64.8, $20 → $0.07, Gemini-1.5-Flash-8B, >280-fold (HAI) W
- Epoch: 9× to 900× per year (data insight) W
- o1: "consistently improves with more reinforcement learning (train-time compute)"; GPT-4o 12%; o1 74%/83%/93% (OpenAI blog) W
- o3/o4-mini: "pushed an additional order of magnitude in both training compute and inference-time reasoning"; "more compute = better performance"; 16 Apr 2025 W
- Khatri: >400,000 GPU-hours; sigmoidal curves (arXiv 2510.13786) W
- Yue: pass@k at large k (arXiv 2504.13837) W
- DeepSeek-V3.2: post-training >10% of pre-training; "comparably to GPT-5" (arXiv 2512.02556) W
- xAI Grok 4, 9 Jul 2025: RL "at pretraining scale"; "over an order of magnitude more compute"; Heavy "parallel test-time compute … multiple hypotheses at once" W
- Brown et al.: coverage over four orders of magnitude; SWE-bench Lite 15.9% → 56% at 250 samples vs 43% SOTA; MATH coverage 82.9% → 98.44%, majority vote/RM 40.50% → 41.41% (arXiv 2407.21787) W
- Snell: >4× efficiency; 14× larger model; non-trivial success rate (arXiv 2408.03314) W
- ARC Prize: 75.7% at $26/task, 87.5% at $4,560/task, 172× compute, 100 semi-private tasks; repriced 3/24/2025 (o1-pro) and 12/10/2025 (o3-pro $80/M); trained on 75% of the public training set (arcprize.org) W; 4,560/26 = 175, 11.8 points C
- o3-mini "three reasoning effort options—low, medium, and high", 31 Jan 2025 W
- Claude 3.7 Sonnet "first hybrid reasoning model on the market"; budget up to 128K output limit; 24 Feb 2025 W
- s1: EMNLP 2025 (Crossref); budget forcing "Final Answer:", "Wait"; 1,000 examples; AIME24 50% → 57% (arXiv 2501.19393) W
- GPT-5 system card (13 Aug 2025): "unified system … real-time router … 'think hard about this'"; router trained on user switches, preference rates, correctness; "parallel test time compute" pro setting W
- Gemini Deep Think: "simultaneously explore and combine multiple possible solutions", 21 Jul 2025, 35/42 W
- GPT-6 Pro parallel agents in ChatGPT, 16 Oct 2026 (RuntimeWire; mixed-news) W

**§4.7**
- Wei: emergence definition; jump at 2e22 FLOP (arXiv 2206.07682) W
- Schaeffer: >92% of BIG-Bench emergent abilities under two metrics; token edit distance (arXiv 2304.15004) W
- p^10 = 0.1%, 10.7%, 34.9%, 90.4% C
- Du: loss threshold, near-chance performance above it (arXiv 2403.15796) W
- Ruan: ~100 public models (arXiv 2405.10938) W
- GPQA: 198 Diamond questions; expert validators 81.2% (Table 5, selection-skewed); full set 65% (arXiv 2311.12022) W
- AI Index 2026: o3 87.7% in late 2024; "saturated in months" W
- GSM1k: 1,205 problems; "up to 8%"; Spearman's r² = 0.36; frontier models "minimal signs of overfitting" (arXiv 2405.00332, final version) W
- Singh: 27 Meta variants; Google 19.2%, OpenAI 20.4%, 83 open-weight models 29.7% (arXiv 2504.20879) W
- Truong: nine benchmarks, 50 flagged, up to 84% precision (= 42 questions); NeurIPS 2025 D&B W
- Dell'Acqua et al., Organization Science 37(2), 2026 (Crossref) W
- HLE: 2,500 questions; o3-mini (high) 13.4% text-only (arXiv 2501.14249v12; Nature 2026, Crossref) W
- Scale leaderboard: GPT 6 Astra 54.80 ±1.94, still rank 1 on 22 Nov 2026 W
- HLE-Rolling, October 2025 (HF dataset card; IntuitionLabs) W
- METR (Kwa et al.): 170 tasks (HCAST 97 tasks of 1 min–30 h, RE-Bench 7 × 8 h, SWAA 66 tasks of 1–30 s); ~7-month doubling; Claude 3.7 Sonnet ~50 min (v1); NeurIPS 2025 W
- METR TH1.1 (29 Jan 2026): 170 → 228 tasks; Claude 3.7 Sonnet 60 min W
- METR YAML: all 18 Fig. 4.3 rows; Opus 4.6 718.8 min (CI 316.7–3,633.8), p80 69.9 min; Mythos 1,044.8 min; doubling 128.744 d (104.4–158.0) and 187.778 d; three rows labelled METR-Horizon-v1.0 W
- METR page: "LAST UPDATED September 8, 2026", "no longer actively updated"; 3 Mar 2026 regularisation correction; 8 May 2026 Mythos and 16-hour notice; no newer METR update found to 22 Nov W
- The Decoder, 10 May 2026: "at least 16 hours", 95% CI 8.5 to 55 hours W
- 2^(365/128.744) = 7.1; 718.8 min = 12.0 h; CI 5.3–60.6 h; 1,044.8 min = 17.4 h C

**§4.8**
- 2e29/3.8e26 = 526 C
- Edelman et al.: GPT-5 likely less compute than GPT-4.5 ("Unlike all previous versions of GPT"); <3× GPT-4 compute; Llama 4 Behemoth; 100× pre/post; 10× every 4 months; GPT-6 "probably more than GPT-4.5" W
- GPT-4.5 blog: AIME '24 GPT-4o 9.3%, GPT-4.5 36.7%, o3-mini (high) 87.3%; 27 Feb 2025 W
- 9.4e26/3.8e26 = 2.47 C

**Bib entries checked (exist; authors, title, year and venue match)**
krizhevsky2012imagenet, epochai2026data, grattafiori2024llama, kaplan2020scaling, sutton2019bitter, openai2023gpt4, hoffmann2022empirical (NeurIPS title confirmed as "An empirical analysis of compute-optimal large language model training"), sevilla2022compute, epochai2026trends (date problem, M1), sajadieh2026ai, cottier2024rising, villalobos2024position, patel2025ilya, shumailov2024ai, sevilla2024can, ho2024algorithmic, maslej2025ai, openai2024learning, snell2025scaling, wei2022emergent, schaeffer2023emergent, du2024understanding, zhang2024careful, kwa2025measuring, metr2026task, centerforaisafety2026benchmark, scale2026humanity, dellacqua2026navigating, meta2024llama, pearce2024reconciling, porian2024resolving, besiroglu2024chinchilla, sardana2024beyond, muennighoff2023scaling, brown2024large, arcprize2024openai (note problem, S6), openai2025introducinga, openai2025introducingb, edelman2025why, singh2025leaderboard (venue not checked), guo2025deepseek, deepseekai2024deepseekv3, metr2026time, hestness2017deep, clark2022unified, ludziejewski2024scaling, kumar2025scaling, chowdhery2023palm, rein2023gpqa, openai2026gpt6, clockbench2026clockbench, cottier2025llm, truong2025fantastic, cais2025hle, yang2025qwen3, khatri2025art, yue2025does (missing author, S7), ruan2024observational, penedo2024fineweb, zeff2025ilya, bastian2026metr, deepseekai2025deepseekv32, xai2025grok4, openai2025o3mini, anthropic2025claude37, muennighoff2025s1, openai2025gpt5systemcard, google2025advanced, merket2026openai.

## Tally
Claims checked against a web source: 168. Confirmed: 161. Wrong: 2 (M3, M4). Outdated: 2 (M1, M2). Unsupported by cited source: 1 (S1; M1's 3.4× is also no longer on the cited page). Could not verify: 4. Arithmetic items recomputed: 38 (errors: 0; one source-internal inconsistency noted in S3). Bib entries checked: 68 (problems: 3 — epochai2026trends date, arcprize2024openai note, yue2025does author list).
