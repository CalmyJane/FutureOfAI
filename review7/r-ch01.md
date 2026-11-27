# Review 7: Chapter 1 (textbook/chapters/ch01.md)

## Verdict
Ready to print. I checked the quotations, numbers and 2026 claims and found none that are wrong. The prose is clear and fair to the people and companies it names, and the chapter separates company claims from independent measurements consistently. The Saniger/Nate passage is handled correctly: it says the charges are allegations and that he has pleaded not guilty. Two minor SHOULD items are listed below.

## MUST change before printing
None.

## SHOULD change

### S1. The list of "new model generations" stops before the November flagships named later in the same chapter
- Where: textbook/chapters/ch01.md:244
- Text now: "New model generations kept arriving. In September 2026 OpenAI published the system card for GPT-6 Astra, Anthropic introduced Claude Opus 5.5 and Google announced Gemini 4 Argon, first to a restricted group of cyber-defence users; on 28 October Google announced Gemini 4 Carbon, again released first to a subset of cyber defenders; Carbon became generally available on 10 November"
- Problem: INCONSISTENT / UNCLEAR. The sentence brings the story up to 10 November but leaves out Anthropic's Claude Fable 5.2 (9 November). The debate box ten lines later names Fable 5.2 as the ClockBench leader, so a reader meets a model the history never introduced. The sentence also leaves out OpenAI's GPT-6.2 (17 November). Section 3.8 (ch03.md:449) lists both. A reader could take Opus 5.5 to be Anthropic's flagship, when the press describes Fable as the top tier available to the public.
- Evidence: 9to5Mac, 9 November 2026, https://9to5mac.com/2026/11/09/anthropic-upgrades-claude-with-new-fable-5-2-model-details-here/ ; SD Times, "Anthropic introduces Claude Fable 5.2, Mythos 5.2" https://sdtimes.com/ai/anthropic-introduces-claude-fable-5-2-mythos-5-2/ ; ch03.md:449 "In November 2026 Anthropic released Claude Fable 5.2 and Mythos 5.2 (9 November) ... and OpenAI GPT-6.2 Astra and Sol (17 November)".
- Change to: "... Carbon became generally available on 10 November. In November Anthropic also released Claude Fable 5.2 (9 November) and OpenAI GPT-6.2 (17 November) [@openai2026gpt6system; @anthropic2026opus55; @kavukcuoglu2026gemini4argon; @kavukcuoglu2026gemini4carbon; @sdtimes2026fable52; @openai2026gpt62]." Copy the bib entries sdtimes2026fable52 and openai2026gpt62 from ch03.bib into ch01.bib.

### S2. Microsoft's "working-age" figure uses a different age band from the survey figure next to it
- Where: textbook/chapters/ch01.md:236
- Text now: "Microsoft's own usage telemetry, which counts users of its tools rather than survey answers, put the share of working-age Americans using AI at 31.3% in the first quarter of 2026"
- Problem: UNCLEAR. Microsoft defines working age as 15–64, and the survey figure just before it covers ages 18–64. Microsoft also measures the share of people "who have used a generative AI product". The text already says the two figures count different things. Giving the age band shows the reader one of the reasons.
- Evidence: Microsoft On the Issues, 7 May 2026, https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/ — "the share of people worldwide between ages 15 and 64 who have used a generative AI product"; "based on a 31.3% usage rate by the working age population"; the US moved "only from 24th to 21st".
- Change to: "... put the share of Americans aged 15 to 64 using AI at 31.3% in the first quarter of 2026, which ranked the United States only 21st ..."

## Could not verify
- OSWorld-Verified "about 86%" for the best general-purpose model by August 2026 (line 242). The official leaderboard page would not load its data (https://osworld-v1.xlang.ai/ showed "Loading verified benchmark data..."). Third-party trackers show Claude Fable 5 at 86.0% and an agent framework at about 90.2%, which matches Table 5.1. The page does announce OSWorld 2.0 on 26 June 2026: confirmed.
- The AI Index 2026 clock-reading result is dated "March 2026" in the text (line 255). Secondary coverage confirms "about half" (50.1%) and the IMO gold result, but I could not confirm the month of measurement.
- MYCIN page references to Buchanan & Shortliffe 1984 (pp. 71, 81, 211–216, 255–260, 672–702). I did not open the book. The arithmetic on those pages was recomputed (see below).
- Saniger docket after October 2026: CourtListener returned 403. Secondary sources (Quinn Emanuel, June 2026; a litigation tracker checked on 7 October 2026) say the case is pre-trial and that he pleaded not guilty, so the text is correct as of those dates.

## Checked and confirmed
- The Dartmouth proposal's quotations, its seven topics in the order given, and the workshop dates 18 June to 17 August 1956 with "a few dozen" thinkers (IEEE Spectrum, Solomonoff 2023). Newell and Simon spoke "early in the summer".
- The SEP's "Ten thinkers attended"; Logic Theorist was "agreed by the attendees ... to be a remarkable achievement" (SEP).
- Turing 1950: the opening sentence, 10^9 storage, 70% after five minutes.
- Mitchell 2021: "In 1960 Herbert Simon declared ...", the Minsky "Within a generation" quotation, "sharp funding decreases and a downturn in enthusiasm for AI in both countries", "meteoric rise", "then-discredited", the springs and winters quotation, "Easy things are easy and hard things are hard", and the brittleness quotation (arXiv 2104.12871).
- Haigh, CACM Feb 2024: the "first AI winter" of the 1970s "never happened", XCON's 480 rules, "more than $40 million a year", the Strategic Computing assumption, speech recognition progressing, the autonomous land vehicle abandoned at the end of 1987, "proved unsustainable", DEC's 59 technical staff in 1989, Cyc starting in 1983 with an estimate of "approximately 2,000 years of person-effort" and 30 million rules, "less controversial alternative", "flipped to refer primarily to deep learning and generative systems", and histories in English as Anglo-American.
- EU Commission guidelines C(2025) 5053 final, dated 29 July 2025: paras 7 (not binding, CJEU), 9 (seven elements), 39 ("early generation expert systems intended for medical diagnosis", "search and optimisation methods"), 41, 42 (linear or logistic regression; "transcend 'basic data processing'"; "consolidated manner for many years"), 48 (minimax chess "without requiring prior learning from data"), 62 and 63 ("vast majority").
- The OECD 2019 and 2023 definitions, the US NAIIA 2020 definition and its enactment date (1 January 2021), and every cell of Table 1.1.
- Table 1.2 arithmetic: 0.3 + 0.2×0.7 = 0.44; 0.44 − 0.10 = 0.34; the revised rule gives 0.34/0.9 = 0.378 ≈ 0.38. Brittleness: 0.999 − 0.8 = 0.199 < 0.2.
- Shannon 1950: 30 moves, 10^3 per move pair, 10^120, 10^90 years.
- Deep Blue on the IBM history page: "brute force computing power", 32 processors, 200 million positions per second, first defeat "under standard tournament time controls", 4–2 in 1996, 3.5–2.5 in New York in 1997, and the quotation "supercomputers and artificial intelligence could simulate human thinking" (verbatim).
- The ImageNet figures (28.2%, 15.3%/16.4%, 26.2%, 6.7%, 3.57%, 5.1% on 1,500 images, 258 images, 4.94%); Seide 2011 (309 h, 27.4% to 18.5%, 33%); AlexNet's 60M parameters on two GTX 580 cards.
- Table 1.4 values (117M, 340M, 800M and 2,500M words, 1.5B, 40 GB, 175B, 300B tokens, 3.14×10^23); 175B/117M ≈ 1,496, so "about 1,500" holds; BERT 80.5 against GPT-1 72.8 on GLUE (the BERT abstract's 7.7-point improvement).
- ChatGPT's 1.2 billion weekly users at DevDay on 29 September 2026 (OpenAI recap: "our collective 1.2B weekly users"); 700 million in July 2025 (Chatterji et al.).
- St. Louis Fed blog, 1 September 2026: "Between August 2024 and May 2026, the share of adults using AI rose from 45% to 62%", ages 18–64. Bick et al. in Management Science (DOI 10.1287/mnsc.2025.02523) exists.
- Gemini 4 Argon on 30 September 2026, first to cyber defenders (Fairwind); Gemini 4 Carbon announced on 28 October and generally available on 10 November (Google blog); Fable 5.2 on 9 November.
- The ClockBench leaderboard: Fable 5.2 Max 87.8%, Gemini 4 Carbon High 85%, Argon High 83.3%, average human 90.7%, top human 95%. This is consistent with Section 4.7.
- SEC fines of $400,000 on Delphia and Global Predictions (March 2024); the FTC's Operation AI Comply quotations; Presto (January 2025); the Saniger charges (April 2025) and his not-guilty plea.
- The Tesler quotation from his website.
- Cross-references to Sections 1.5, 2.6, 3.5, 3.7 (the NLP understanding survey is discussed at ch03.md:400) and 3.8 all point to the right sections.

## Tally
Claims checked: 95 / confirmed: 91 / wrong: 0 / outdated: 0 (2 SHOULD wording items; 4 could not be verified)
