# Review 4: Chapter 1, What We Mean by "AI": Definitions and a Short History

## Verdict

Ready to print. Only minor fixes are recommended. The chapter is accurate, carefully attributed and fair to the people and companies it names. I checked its quotations against the primary texts wherever those were available: Mitchell 2021, Haigh 2024, the Commission's 2025 guidelines, the IBM Deep Blue page, the FTC press release, the St. Louis Fed post and the ClockBench leaderboard. All matched word for word. All the 2026 material checks out against current sources as of 26 November 2026: the ChatGPT figure of 1.2 billion weekly users, GPT-6 Astra, Opus 5.5, both Gemini 4 models, Fable 5.2, ClockBench, OSWorld-Verified, the Bick et al. 62% figure and Microsoft's ranking of the US at 21st. I found no wrong facts and nothing legally sensitive. The AI-washing enforcement cases are stated as charges, settlements or allegations, as they should be.

## MUST change before printing

None.

## SHOULD change

### S1. Table 1.3, Go row: "no program had beaten a professional" needs "without handicap"
- Where: textbook/chapters/ch01.md:206
- Text now: "| 2016 | Go, games won against a professional (Fan Hui) on a full board | none (no program had beaten a professional) | 5–0 |"
- Problem: UNCLEAR / slightly overstated. Go programs had beaten professionals before 2016 in handicap games on the full 19 × 19 board. Silver et al. claim something narrower: the first win against a professional "without handicap, in the full game of Go". As written, the table cell is too broad.
- Evidence: Silver et al. (2016), *Nature* 529, abstract: "This is the first time that a computer program has defeated a human professional player in the full-sized game of Go" and main text: "…without handicap…".
- Change to: "| 2016 | Go, even games (no handicap) against a professional (Fan Hui) on a full board | none (no program had beaten a professional without handicap) | 5–0 |"

### S2. Cross-chapter: Chapter 4 sends readers to the wrong section for the clock-reading result
- Where: textbook/chapters/ch04.md:229 (the material it points to is at ch01.md:255, in the Debate box at the end of Section 1.7)
- Text now (ch04): "On 25 October 2026 the best model, Google's Gemini 4 Argon, scored 83.3%, up from about half in March 2026 (Section 1.8)."
- Problem: INCONSISTENT. The AI Index "about half the time" clock result and the ClockBench figures are in the Debate box "Is hand-built knowledge a dead end?", which comes before the heading "## 1.8" and so belongs to Section 1.7. Section 1.8 never mentions clocks.
- Change to (ch04.md:229): "…up from about half in March 2026 (Section 1.7)."

### S3. ClockBench box: say which entry was second
- Where: textbook/chapters/ch01.md:255
- Text now: "By late November 2026 Anthropic's Claude Fable 5.2 Max, released on 9 November, had reached 87.8%"
- Problem: UNCLEAR, but not wrong. The live leaderboard now places Google's Gemini 4 Carbon High (85.0%) between Fable 5.2 Max (87.8%) and Gemini 4 Argon High (83.3%). Without that, the box can read as a straight two-company race, and naming the author's own model as the leader with no context may look partial. Adding the second entry keeps the box even-handed. Make the same change at ch04.md:229.
- Evidence: https://clockbench.ai/ (accessed 26 Nov 2026): "1 Claude Fable 5.2 Max 87.8% … 2 Gemini 4 Carbon High 85% … 3 Gemini 4 Argon High 83.3%"; average human 90.7%.
- Change to: "By late November 2026 Anthropic's Claude Fable 5.2 Max, released on 9 November, had reached 87.8%, ahead of Google's Gemini 4 Carbon at 85.0%"

## Could not verify
- Buchanan & Shortliffe (1984) page-level citations (pp. 71, 81, 211, 215–216, 255–256, 260, 672–673, 698–702): I could not open the book. The MYCIN rule, the certainty-factor arithmetic and the "laid to rest in 1978" account all agree with standard secondary accounts, and the arithmetic is right (see below).
- Yu et al. (1979) JAMA figures (65%; 42.5–62.5%; eight outside raters): these agree with standard summaries, but I could not open the paywalled article.
- The Stanford Encyclopedia of Philosophy's count of "ten attendees" at Dartmouth (line 21).
- Brown et al. (1990): "48% of 73 new French sentences … 5% exactly". I did not open the paper.
- OECD explanatory memorandum page numbers (pp. 4, 6, 7, 9). The wording of the definition is correct.

## Checked and confirmed
- Dartmouth proposal (31 Aug 1955): "$13,500"; "a 2 month, 10 man study"; the "every aspect of learning…" quotation; the seven listed aspects; "The major obstacle is not lack of machine capacity…"; workshop dates 18 June–17 August 1956 (Solomonoff).
- Turing 1950: storage of about 10^9, "not more than 70 per cent chance … after five minutes".
- Michael et al. survey: split about 51/49 (consistent with ch03.md:400).
- Legg & Hutter "70-odd" definitions; OpenAI charter wording; Morris et al.: "Competent" means at least the 50th percentile of skilled adults, and the paper itself says "as of this writing in September 2023" (arXiv 2311.02462v4).
- EU AI Act art. 3(1), 3(63)–(65), 51 (10^25), art. 113 (application from 2 Feb 2025), recital 12 wording.
- Commission guidelines: published 6 Feb 2025 (C(2025) 924) and formally adopted 29 July 2025 (C(2025) 5053). Para 7 "not binding"/CJEU; para 9 seven elements; para 39 "early generation expert systems intended for medical diagnosis" and "search and optimisation methods"; para 41 "may"; para 42 regression and "used in consolidated manner for many years"; para 48 minimax chess program "without requiring prior learning from data"; paras 46, 49–50; para 62 "No automatic determination or exhaustive lists"; para 63 "The vast majority". All checked against the Commission PDF (ai-act-service-desk.ec.europa.eu, 2025-08).
- US NAIIA 2020 definition and enactment on 1 January 2021.
- Shannon 1950: 30 moves, 10^3, 10^120, "over 10^90 years".
- Mitchell 2021, checked word for word against arXiv 2104.12871: Simon 1960 quotation; Minsky "Within a generation...the problems of creating 'artificial intelligence' will be substantially solved"; "led to sharp funding decreases and a downturn in enthusiasm for AI in both countries"; "meteoric rise of machine learning"; "inspired by statistics rather than by neuroscience or psychology"; "then-discredited"; "often unable to generalize or adapt when faced with new situations"; spring/winter wording; fallacy "Easy things are easy and hard things are hard".
- Haigh 2024 (CACM 67(2)), checked word for word against a full-text copy: "first AI winter … never happened"; 480 rules; "more than $40 million a year"; 59 technical staff by 1989; Cyc "Starting in 1983", "approximately 2,000 years of person-effort", 30 million rules; "proved unsustainable"; "a less controversial alternative to artificial intelligence"; DARPA land vehicle abandoned end of 1987; "flipped to refer primarily to deep learning and generative systems"; US/UK focus of English-language histories.
- Lighthill quotations; McDermott 1985 panel quotations.
- MYCIN certainty-factor arithmetic: 0.3 + 0.2 × 0.7 = 0.44; 0.44 − 0.10 = 0.34; 0.34/0.9 ≈ 0.38; 0.999 − 0.8 = 0.199 < 0.2.
- Jelinek 1976; Bahl, Jelinek & Mercer 1983; Brown 1990 "hear"/"bravo".
- Banko & Brill 2001 quotation; Halevy, Norvig & Pereira 2009 quotation and "a million times" the Brown Corpus.
- Deep Blue: 1996 result 4–2 (3W 2D 1L), 1997 result 3.5–2.5; IBM page: "brute force computing power", "32 processors", "200 million chess positions per second", "first computer system to defeat a reigning world champion in a match under standard tournament controls", "supercomputers and artificial intelligence could simulate human thinking".
- ImageNet: 2010 winner 28.2%, 2011 25.8%, 2012 15.3%/16.4%, 2013 11.7%, 2014 6.7%, ResNet 3.57%, 152 layers; human annotator 5.1% on 1,500 images, second annotator 258 images; He et al. 4.94% quotation. Figure 1.2 values agree.
- Seide et al. 2011: 309 h, 27.4% → 18.5%, "33% relative improvement".
- AlexNet: 60M parameters, two GTX 580s, 5–6 days.
- AlphaGo: Fan Hui 5–0, "at least a decade away", Lee Sedol 4–1.
- Transformer: 28.4 BLEU, more than 2 points better, quotation correct.
- Table 1.4: GPT-1 117M, BooksCorpus, 9 of 12 tasks; GLUE 80.5 vs 72.8; BERT corpora 800M + 2,500M words; GPT-2 1.5B, 8M documents, 40 GB, 7 of 8; GPT-3 175B, 300B tokens, 3.14 × 10^23. 175B/117M ≈ 1,496, so "about 1,500" is right.
- InstructGPT 1.3B preferred to 175B; Chatterji et al.: 700 million weekly users in July 2025, about 10% of the world's adults.
- GPT-4 bar exam; Martínez re-analysis (62nd and 48th percentiles); LLaMA-13B outperforms GPT-3; DeepSeek-V3 in December 2024.
- AlphaFold quotation; 2018 Turing Award quotation; 2024 Nobel prizes (Hassabis and Jumper shared half of the chemistry prize).
- Bick et al., *Management Science* (doi 10.1287/mnsc.2025.02523): "has outpaced both PCs and the internet". St. Louis Fed, 1 Sep 2026: "Between August 2024 and May 2026, the share of adults using AI rose from 45% to 62%" (ages 18–64).
- Microsoft, 7 May 2026: the US "only from 24th to 21st".
- o1 quotation; DeepSeek-R1 *Nature* quotation and cold-start data; MCP quotation (Nov 2024).
- METR "doubling approximately every seven months since 2019"; OSWorld 72.36% human vs 12.24% model; OSWorld-Verified about 86% in Aug 2026 (consistent with Table 5.1, ch05.md:150).
- 2026 models: GPT-6 Astra system card (3 Sep 2026); Claude Opus 5.5 (22 Sep 2026); Gemini 4 Argon (Google blog, 30 Sep 2026); Gemini 4 Carbon to cyber defenders on 28 Oct and generally available 10 Nov 2026; Claude Fable 5.2 (9 Nov 2026).
- OpenAI DevDay 2026 recap (29 Sep 2026): 1.2 billion weekly users. This is consistent with ch03.md:411.
- ClockBench: average human 90.7%; Fable 5.2 Max 87.8% (live page, 26 Nov 2026); AI Index 2026 "gold medal … cannot reliably tell time" (about 50%).
- Sutton 2019 and Marcus 2018 quotations; GPT-3 "competitive with" fine-tuned systems.
- Tesler page wording ("Intelligence is whatever machines haven't done yet"); AI100 2016 "AI effect"/"odd paradox" quotations.
- SEC, March 2024: Delphia and Global Predictions, $400,000 in total, "AI washing". FTC, Sep 2024: five actions, "seized on the hype surrounding AI", "the world's first robot lawyer", "there is no AI exemption from the laws on the books" (ftc.gov press release). SEC v. Presto (Jan 2025); SDNY charges against the founder of Nate (Apr 2025), stated as allegations.
- All 101 citation keys used in ch01.md exist in bib/ch01.bib.
- Internal cross-references: Section 1.3/1.4/1.5/1.7 pointers; Section 2.6 (CNNs, GPUs); Section 3.5; Section 3.7 (the understanding debate is in ch03 §3.7); Section 3.8 (lineage). All correct.

## Tally
Claims checked: 132 · confirmed: 122 · wrong: 0 · outdated: 0 · imprecise: 2 (S1, S3) · could not verify: 5 groups (about 8 claims) · cross-chapter inconsistency: 1 (S2, in ch04)
