# Review 9: Chapter 1 (textbook/chapters/ch01.md)

## Verdict
Ready to print after minor fixes. No statement was found to be wrong, misquoted or legally risky. Quotations checked against Mitchell (2021), Haigh (CACM Feb 2024), IBM, SEP, IEEE Spectrum, the Morris et al. AGI-levels paper and the late-2026 company posts all match. All arithmetic recomputes correctly. The Saniger passage is phrased as allegation, with the not-guilty plea stated, and no later development was found. The items below are SHOULD: one unsourced date, one quotation whose published wording could not be confirmed, and two balance points.

## MUST change before printing
None.

## SHOULD change

### S1. Gemini 4 Carbon general-availability date is not supported by the cited source
- Where: textbook/chapters/ch01.md:244
- Text now: "on 28 October Google announced Gemini 4 Carbon, again released first to a subset of cyber defenders; Carbon became generally available on 10 November."
- Problem: UNSUPPORTED — the cited post (kavukcuoglu2026gemini4carbon, 28 Oct 2026) gives no GA date. It says only that Google will widen access "as soon as possible". No other cited source covers 10 November.
- Evidence: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-carbon/ (28 Oct 2026): "Starting this week, we will make Carbon available to a subset of cyber defenders". https://blog.google/innovation-and-ai/technology/developers-tools/gemini-4-carbon-developers/ (10 Nov 2026), "Gemini 4 Carbon is now available for developers": "Starting today, developers can build with Gemini 4 Carbon".
- Change to: keep the text and add the citation `@google2026gemini4carbondevelopers` to the bracket. New bib entry:
  ```
  @misc{google2026gemini4carbondevelopers,
    author       = {{Google}},
    title        = {{Gemini} 4 {Carbon} Is Now Available for Developers},
    year         = {2026},
    howpublished = {Google blog, 10 November 2026 (company source)},
    url          = {https://blog.google/innovation-and-ai/technology/developers-tools/gemini-4-carbon-developers/},
    urldate      = {2026-11-27}
  }
  ```

### S2. Quotation from Bick, Blandin and Deming could not be matched
- Where: textbook/chapters/ch01.md:236
- Text now: "overall adoption, at home and at work, \"has outpaced both PCs and the internet\" [@bick2026rapid]"
- Problem: UNSUPPORTED (wording). The NBER version (w32966) says "adoption has been faster than either PCs or the internet". The Management Science version (DOI 10.1287/mnsc.2025.02523) returned 403, so the quoted wording could not be confirmed. The substance is correct.
- Evidence: NBER WP 32966 abstract: "adoption has been faster than either PCs or the internet."
- Change to: "overall adoption, at home and at work, has been faster than that of either PCs or the internet [@bick2026rapid]" (a paraphrase, with the quotation marks removed).

### S3. ClockBench passage is a near-duplicate of Chapter 4 and spotlights the authoring company's model
- Where: textbook/chapters/ch01.md:255
- Text now: "By late November 2026 Anthropic's Claude Fable 5.2 Max, released on 9 November, had reached 87.8%, ahead of Google's Gemini 4 Carbon at 85.0%; OpenAI's GPT-6.2 models, released on 17 November, had not yet been listed [@clockbench2026clockbench]."
- Problem: INCONSISTENT / balance. The figures are correct: clockbench.ai on 27 Nov 2026 shows Claude Fable 5.2 Max 87.8%, Gemini 4 Carbon High 85%, average human 90.7%, and no GPT-6.2 entry. But ch04.md:229 repeats the same data almost word for word. In a debate box about Sutton and Marcus, the point needs only the trend. Naming the Anthropic model as "ahead of" Google's, in a book written by Anthropic models, reads as gratuitous. Readers primed by the preface's disclosure may notice it.
- Evidence: https://clockbench.ai/ (accessed 27 Nov 2026): "Claude Fable 5.2 Max … 87.8%", "Gemini 4 Carbon High … 85%", average human "90.7%". There is no GPT-6.2 entry.
- Change to: "On 25 October 2026 the best model on ClockBench, a clock-reading leaderboard run by an independent developer, scored 83.3%, and by late November the best listed model had reached 87.8%, against 90.7% for the average human; the newest OpenAI models had not yet been listed (Section 4.7) [@clockbench2026clockbench]."

### S4. The late-2026 release paragraph lists only the three US closed-model developers
- Where: textbook/chapters/ch01.md:244
- Text now: "New model generations kept arriving. In September 2026 OpenAI published the system card for GPT-6 Astra, Anthropic introduced Claude Opus 5.5 and Google announced Gemini 4 Argon …"
- Problem: UNCLEAR / balance. The same period saw major non-US and open-weight releases that the book covers elsewhere: DeepSeek-V4-Pro GA on 13 August, Kimi K3 in July, Qwen3.8 in August and Qwen4-Max on 16 November (ch03.md:449–451, ch07.md:272). Listing only OpenAI, Anthropic and Google implies the frontier is just these three, which Chapter 7 itself contradicts.
- Evidence: internal (ch03.md:449 "Alibaba the closed-weight Qwen4-Max (16 November)"; ch07.md:272).
- Change to: add after the bracketed citations: "Chinese developers released large open-weight models in the same months, among them DeepSeek-V4-Pro and Kimi K3 (Section 7.6)."

## Could not verify
- The OSWorld-Verified best general-purpose model at "about 86%" in August 2026 (line 242). The leaderboard page would not load its data. The OSWorld 2.0 notice dated 26 June 2026 was confirmed. The figure is consistent with Table 5.1 (ch05: 86.0%).
- MYCIN page numbers in Buchanan and Shortliffe (1984), Yu et al. (1979) percentages, Brown et al. (1990) figures (48% of 73 sentences), and Commission guideline paragraph numbers. These are book or paywalled sources and were not opened. They are consistent with my own knowledge of the texts.
- Saniger (Nate): no plea deal, trial or verdict was found up to 27 Nov 2026. The "has pleaded not guilty" wording is still accurate as far as can be seen.

## Checked and confirmed
- Dartmouth proposal: date, authors, $13,500, the seven aspects and the quotations. Workshop dates 18 June – 17 August 1956 and "a few dozen" (IEEE Spectrum). SEP: "Ten thinkers attended" and Logic Theorist "a remarkable achievement".
- Mitchell (2021): the Simon 1960 and Minsky quotations (Mitchell prints "problems"), "sharp funding decreases…", "meteoric rise", "then-discredited", "unable to generalize or adapt", the spring/winter wording, and "easy things are easy and hard things are hard".
- Haigh (CACM 67(2), 2024): "first AI winter … never happened"; XCON 480 rules and more than $40 million a year; Alvey; Strategic Computing assumptions; ALV abandoned at the end of 1987; "proved unsustainable"; 59 DEC staff in 1989; Cyc from 1983, about 2,000 person-years, 30 million rules; "less controversial alternative"; "flipped"; English-language histories as Anglo-American.
- Morris et al.: "as of this writing in September 2023, frontier language models … Emerging AGI".
- IBM Deep Blue page: 32 processors, 200 million positions per second, "brute force computing power", "supercomputers and artificial intelligence could simulate human thinking", first defeat under standard tournament time controls.
- Late-2026 releases: OpenAI DevDay 29 Sep 2026 "1.2B weekly users"; Opus 5.5 on 22 Sep; Gemini 4 Argon on 30 Sep to cyber defenders (Fairwind); Gemini 4 Carbon on 28 Oct to a subset of cyber defenders, then developers on 10 Nov; Fable 5.2 on 9 Nov (SD Times); GPT-6.2 Astra/Sol on 17 Nov.
- St. Louis Fed: adult use rose from 45% to 62% between August 2024 and May 2026, ages 18–64. Microsoft: 31.3% of the working-age population (15–64), US moved up from 24th to 21st.
- AI Index 2026: IMO gold-level score, but clocks read correctly about half the time.
- Arithmetic: CF combination 0.44, 0.34 and 0.38; 0.999 − 0.8 = 0.199; GPT-1 to GPT-3 ≈ 1,496×; AlexNet, ResNet and ImageNet figures; Seide 27.4% → 18.5% (33% relative).
- Table 1.4 entries (GPT-1, BERT, GPT-2, GPT-3) and the GLUE 80.5 vs 72.8 comparison.
- Cross-references to Sections 1.2, 1.5, 2.6, 3.5, 3.7, 3.8 and 7.1 point to the right headings.

## Tally
Claims checked: 78 / confirmed: 73 / wrong: 0 / outdated: 0 (1 unsupported date, 1 unconfirmed quotation wording, 2 balance/duplication)
