# Review 5: Chapter 1 (textbook/chapters/ch01.md)

## Verdict
A careful, well-sourced chapter. Every 2026 claim I checked matched its source, as did the historical quotations and all the arithmetic. Several claims were checked against primary texts (Haigh's CACM column, Morris et al., Lecun et al., Microsoft, the St. Louis Fed, ClockBench, DeepSeek and Google pages). The tone towards named companies and people (SEC, FTC, Presto, Nate) is fair: the Nate case is correctly framed as allegations. I found no MUST items. **Ready to print**, with three minor SHOULD items.

## MUST change before printing
None.

## SHOULD change

### S1. Microsoft adoption ranking: a newer report gives the same rank
- Where: textbook/chapters/ch01.md:236
- Text now: "Microsoft's own usage telemetry, which counts users of its tools rather than survey answers, ranked the United States only 21st by the share of its population using AI in early 2026 [@lavistaferres2026state]."
- Problem: OUTDATED (minor). The cited post (7 May 2026) covers Q1 2026. Microsoft's Q2 2026 update ("The continued state of global AI diffusion in 2026", 21 September 2026) keeps the US at 21st. The sentence is still true, but a reader looking for the latest figure will find the newer report.
- Evidence: https://blogs.microsoft.com/on-the-issues/2026/05/07/the-state-of-global-ai-diffusion-in-2026/ says the US moved "from 24th to 21st based on a 31.3% usage rate by the working age population" (Q1 2026). MediaPost's report on the Q2 release says the US "ranked No. 21 in first-quarter 2026 and remained the same in second-quarter 2026" (https://www.mediapost.com/publications/article/418164/microsoft-tracks-ai-adoption-rates-us-ranking-stalls.html). Blog post: https://blogs.microsoft.com/on-the-issues/2026/09/21/the-continued-state-of-global-ai-diffusion-in-2026/
- Change to: "...ranked the United States only 21st by the share of its working-age population using AI in the first half of 2026 [@lavistaferres2026state; @microsoft2026continued]." Add a bib entry:
  ```
  @misc{microsoft2026continued,
    author       = {{Microsoft}},
    title        = {The Continued State of Global {AI} Diffusion in 2026},
    year         = {2026},
    howpublished = {Microsoft On the Issues blog, 21 September 2026 (Microsoft telemetry, Q2 2026)},
    url          = {https://blogs.microsoft.com/on-the-issues/2026/09/21/the-continued-state-of-global-ai-diffusion-in-2026/},
    urldate      = {2026-11-27}
  }
  ```
  Before using the post, confirm its byline and confirm that it gives the US rank. Otherwise keep the text as it is.

### S2. OSWorld leaderboard URL now redirects; OSWorld 2.0 exists
- Where: textbook/chapters/ch01.md:242 and bib/ch01.bib `osworld2026verified`
- Text now: "By August 2026 the best general-purpose model reached about 86% on the official leaderboard for OSWorld-Verified..." (bib url `https://os-world.github.io/`)
- Problem: OUTDATED (minor). The bib URL now 301-redirects to `http://osworld-v1.xlang.ai/`, and that page says: "2026-06-26: OSWorld 2.0 is now available!" The 86% figure is consistent with third-party aggregators for models; agent frameworks score up to about 90%. The book's wording "best general-purpose model" handles that distinction. Readers following the link will land on a page marked as the old version.
- Evidence: http://osworld-v1.xlang.ai/ (accessed 27 November 2026), the notice quoted above. BenchLM lists a top model score of 86.1% (accessed 27 November 2026).
- Change to: keep the sentence, and update the bib url to `https://osworld-v1.xlang.ai/`. Optionally add: "(a successor benchmark, OSWorld 2.0, appeared in June 2026)".

### S3. Martínez bib entry: year/volume mismatch
- Where: bib/ch01.bib `martinez2024reevaluating`
- Text now: `year = {2024}, volume = {33}, number = {3}`
- Problem: INCONSISTENT (bibliographic). The article was published online in 2024. Volume 33, issue 3 is the 2025 print issue.
- Evidence: https://link.springer.com/content/pdf/10.1007/s10506-024-09396-9.pdf
- Change to: keep `year = {2024}` and add `note = {Published online 2024; print issue 2025}`. Or set `year = {2025}` and change the in-text key consistently.

## Could not verify
- Line 21: the workshop dates of 18 June to 17 August 1956 (Solomonoff, IEEE Spectrum). I did not re-open the article in this round. The dates are consistent with the standard accounts.
- Line 155: the outcome of the Nate/Saniger prosecution. I found no reported plea, trial or verdict up to November 2026; a July 2025 law-firm note said the SEC had not served him (he lives in Spain). The book's wording ("charged ... alleging") is safe as it stands.

## Checked and confirmed
- The Dartmouth proposal: "2 month, 10 man study", $13,500, and the "every aspect of learning..." quotation.
- Turing: storage of 10^9^, 70%, five minutes.
- Haigh, CACM 67(2), read in full text:
  - "the 'first AI winter' of the 1970s never happened";
  - XCON's 480 rules and "more than $40 million a year";
  - DEC's 59 technical staff in 1989;
  - Cyc's "approximately 2,000 years of person-effort", the 1983 start and 30 million rules;
  - "proved unsustainable" and "a less controversial alternative to artificial intelligence";
  - "flipped to refer primarily to deep learning and generative systems";
  - the autonomous land vehicle abandoned at the end of 1987;
  - McDermott's "deep unease", "will eventually result in disaster" and "Everybody hurriedly changes the names...". (Haigh himself miswrites AAAI's name; the book's version is correct.)
- Morris et al. (ICML 2024): "as of this writing in September 2023", Emerging AGI, and the 50th percentile for Competent AGI.
- Shannon's figures (30 moves, 10^120^, 10^90^ years).
- Table 1.2 arithmetic: 0.44, 0.34 and 0.34/0.9 = 0.378. The brittleness example (0.999 − 0.8 = 0.199).
- The ImageNet figures: 15.3/26.2/16.4%, 28.2→6.7%, 3.57%, 5.1% on 1,500 images, 258 images, and He's 4.94%.
- Seide et al.: 27.4→18.5% and 309 hours.
- Deep Blue: 4–2 in 1996, 3.5–2.5 in 1997, 32 processors and 200 million positions a second; Campbell et al.: 30 processors and 480 chips.
- The GPT-1 to GPT-3 table, and the growth factor 175 B / 117 M ≈ 1,496.
- Martínez: the 62nd percentile among first-time takers and the 48th among those who passed.
- OpenAI DevDay of 29 September 2026: 1.2 billion weekly users (OpenAI recap; Engadget; The Decoder).
- St. Louis Fed: "Between August 2024 and May 2026, the share of adults using AI rose from 45% to 62%", for ages 18–64.
- ClockBench, live page on 27 November 2026: Claude Fable 5.2 Max 87.8%, Gemini 4 Carbon High 85%, Gemini 4 Argon High 83.3%, human average 90.7%.
- The AI Index 2026 clock result (about 50%).
- Fable 5.2 released on 9 November 2026 (press reports).
- Gemini 4 Argon, 30 September: "rolling out to a set of trusted cyber defenders".
- Gemini 4 Carbon generally available on 10 November 2026.
- Sources for the SEC Delphia/Global Predictions $400k, FTC Operation AI Comply, Presto and Nate.
- All cited keys exist in bib/ch01.bib.
- Cross-references to Sections 2.6, 3.5, 3.7 and 3.8 point to the right sections.

## Tally
Claims checked: 62 · confirmed: 59 · wrong: 0 · outdated: 2 (minor, S1–S2) · bibliographic: 1 · could not verify: 2
