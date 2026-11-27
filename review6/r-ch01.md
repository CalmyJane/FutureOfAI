# Review 6: Chapter 1 (textbook/chapters/ch01.md)

## Verdict
Ready to print. The chapter is accurate and fair, and its quotations and numbers hold up against the sources I could open. I found no wrong facts or misquotations. There are two small points worth fixing: one gives context to a legally sensitive item, the other makes a statistic precise.

## MUST change before printing
None.

## SHOULD change

### S1. Nate founder: say he has pleaded not guilty
- Where: textbook/chapters/ch01.md:274
- Text now: "in April 2025 federal prosecutors in New York charged the founder of the shopping app Nate with securities and wire fraud, alleging that transactions presented as automated were largely processed by human workers"
- Problem: LEGALLY SENSITIVE (mild). The text is accurate and uses "charged" and "alleging", but it names a living person in a criminal case without saying he denies the charges. MLex (17 December 2025) reported a not-guilty plea, and I found no later plea deal or verdict up to November 2026. Saying he pleaded not guilty is fairer and reduces risk.
- Evidence: https://www.justice.gov/usao-sdny/pr/tech-ceo-charged-artificial-intelligence-investment-fraud-scheme (charges, April 2025). The plea comes from search results summarising an MLex report: "Albert Saniger, the former chief executive of e-commerce platform Nate, pleaded not guilty to fraud charges" (17 December 2025, https://www.mlex.com/mlex/articles/2423455). The MLex article is paywalled, so confirm before printing.
- Change to: "...alleging that transactions presented as automated were largely processed by human workers; he has pleaded not guilty [@usdoj2025techceo; @rollet2025fintech]." (Add the MLex report or another source for the plea if one is preferred.)

### S2. Microsoft ranking: give the population base and the share
- Where: textbook/chapters/ch01.md:236
- Text now: "Microsoft's own usage telemetry, which counts users of its tools rather than survey answers, ranked the United States only 21st by the share of its population using AI in early 2026"
- Problem: UNCLEAR. The measure is the share of the working-age population (the bib entry says ages 15–64), and the US figure was 31.3%. The sentence comes straight after the Bick et al. figure of 62% of adults aged 18–64. Without the Microsoft number, readers cannot see how far apart the two measures are. That gap is the point of the paragraph's "by measures that count different things".
- Evidence: https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/ (7 May 2026): "The United States finally started to move up the national rankings, albeit only from 24th to 21st". The US share is given as 31.3% of the working-age population for Q1 2026.
- Change to: "Microsoft's own usage telemetry, which counts users of its tools rather than survey answers, put the share of working-age Americans using AI at 31.3% in the first quarter of 2026, which ranked the United States only 21st [@lavistaferres2026state]."

## Could not verify
- Line 21: Grace Solomonoff's dates for the workshop (18 June–17 August 1956) and the SEP count of ten attendees. These are plausible; I did not open the sources.
- Lines 105–117 and the MYCIN page references to Buchanan & Shortliffe (pp. 71, 81, 211–216, 255–260, 672–702). I recomputed the arithmetic (below) but did not open the book.
- Line 135: the quotations from the McDermott 1985 "dark ages" panel.

## Checked and confirmed
- Line 5: 1.2 billion weekly ChatGPT users at DevDay, 29 September 2026. OpenAI's recap says "our collective 1.2B weekly users".
- Line 29: Morris et al. say "as of this writing in September 2023" frontier LLMs are "Emerging AGI" (arXiv 2311.02462).
- Line 49: the guidelines were published 6 February 2025 and formally adopted 29 July 2025 as C(2025) 5053 final.
- Line 92: the Simon 1960 and Minsky quotations match Mitchell (arXiv 2104.12871). Mitchell cites Simon 1960, *The New Science of Management Decision*, p. 38. The Lighthill and US funding-cut wording also matches Mitchell.
- Lines 96, 131, 141, 145, 272: all the Haigh material is in "How the AI Boom Went Bust" (CACM, February 2024): the "first AI winter" of the 1970s "never happened", 480 rules, more than $40 million a year, 59 staff in 1989, 2,000 person-years, 30 million rules, "proved unsustainable", "less controversial alternative", "flipped".
- Tables 1.2 and 1.3: 0.3 + 0.2 × 0.7 = 0.44; 0.44 − 0.10 = 0.34; 0.34/0.9 = 0.378; 0.999 − 0.8 = 0.199. ImageNet figures: 15.3/26.2/16.4%, 28.2%→6.7%, 3.57%, 5.1%, 4.94%. Seide: 27.4→18.5%, 33% relative.
- Table 1.4 figures (117 M, 340 M, 1.5 B, 175 B, 3.14 × 10^23, GLUE 80.5/72.8, 9 of 12, 7 of 8). The growth factor 175 B/117 M ≈ 1,496 matches "about 1,500".
- Line 228: 700 million weekly users and about 10% of adults (Chatterji et al.). Line 230: 62nd and 48th percentiles (Martínez).
- Line 236: Bick et al.'s published *Management Science* abstract says work adoption was "faster than" the PC (the 2025 working paper said "as fast as"), so the text follows the published version. The St. Louis Fed blog says "the share of adults using AI rose from 45% to 62%" by May 2026, for ages 18–64.
- Line 242: OSWorld 72.36% human and about 12% model. The OSWorld-Verified results file has the best general model, claude-fable-5, at 85.96% dated 1 August 2026 (the best agent framework is 90.19%). The OSWorld 2.0 banner is dated 26 June 2026.
- Line 244: GPT-6 Astra system card (September 2026), Gemini 4 Argon (30 September), Gemini 4 Carbon announced 28 October and generally available 10 November 2026.
- Line 255: the 2026 AI Index says the top ClockBench model scored 50.6% in March 2026, alongside a gold-medal IMO score. The ClockBench leaderboard now shows Fable 5.2 Max at 87.8%, Gemini 4 Carbon High at 85% and average humans at 90.7%. Fable 5.2 was released 9 November 2026. (The AI Index gives humans 90.1%; the text uses the leaderboard's 90.7% consistently, as ch04:229 does.)
- Line 264: Tesler's own page says "Intelligence is whatever machines haven't done yet", "ca. 1970".
- Line 274: SEC, 18 March 2024, $400,000 in total ($225k + $175k) and "AI washing".
- Cross-references: §2.6, §3.5, §3.7 (its Debate box treats the "understanding" survey), §3.8, Chapter 4 (METR), Chapter 5 and Chapter 7 all point to the right places. The ChatGPT 1.2 billion figure, the OSWorld 86% figure and the ClockBench figures match ch03, ch05 and ch04.

## Tally
Claims checked: 62 / confirmed: 59 / wrong: 0 / outdated: 0 (2 SHOULD items, both on fairness or precision; 3 groups could not be verified)
