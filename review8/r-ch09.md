# Review 8: Chapter 9, Information, Media and Democracy

## Verdict
Ready to print. The chapter is careful, well sourced and fair in tone. Every 2025–2026 claim I checked held up, including the post-June 2026 items: Pew digital twins, SynthID Detector, Apple Reference Image and SynthID in iOS 27.2, the ChatGPT VLOSE designation, the Digital Omnibus, Code of Practice signatories, Penske, Talarico, Lula, the TSE 4–3 ruling, the xAI/SpaceXAI/SpaceXSI renaming, the TAKE IT DOWN conviction and the UK offences. I found no MUST items. One balance item is worth fixing. Section 9.1 cites Meta's and OpenAI's own misuse reports, but it leaves out Anthropic's reports on misuse of Claude for influence operations. In a book written by Anthropic models, that gap invites a charge of bias.

## MUST change before printing
None.

## SHOULD change

### S1. Company balance: Anthropic's own influence-operation reports are missing
- Where: textbook/chapters/ch09.md:23
- Text now: "OpenAI said in October 2026 that two operations it had banned, from Russia and Iran, had used its models to make routine work easier, and that planting stories in established media outlets appeared to reach more people than fake social media accounts [@openai2026disrupting; @huo2026openai]. These are accounts by the platforms of misuse of their own products."
- Problem: UNSUPPORTED (balance) — The paragraph uses Meta's and OpenAI's self-reports as evidence. Anthropic publishes comparable reports, and they are directly on point: Claude was used to run a commercial bot network. Leaving them out, in a book that says it was written by Anthropic models, makes the selection look one-sided, even though the reason is probably innocent.
- Evidence: https://www.anthropic.com/news/detecting-and-countering-malicious-uses-of-claude-march-2025 (published 23 April 2025): "This operation managed over 100 social media bot accounts across Twitter/X and Facebook." "The operation engaged with tens of thousands of authentic social media accounts." Anthropic's September 2026 threat intelligence report (https://www.anthropic.com/threat-intelligence-report-september-2026) describes a commercial "influence-as-a-service" operation that used Claude to produce content for about 70 fabricated news websites. Press summaries say it drew little authentic engagement. Check the exact wording against the primary page before citing.
- Change to: after the OpenAI sentence, insert: "Anthropic, whose models wrote much of this book, reported in April 2025 that a commercial 'influence-as-a-service' operation had used Claude to manage more than 100 bot accounts on X and Facebook, which engaged with tens of thousands of real accounts [@anthropic2025detecting]." Then keep "These are accounts by the platforms of misuse of their own products."
  New bib entry (ch09.bib):
  ```
  @misc{anthropic2025detecting,
    author = {{Anthropic}},
    title = {Detecting and Countering Malicious Uses of {Claude}: {March} 2025},
    year = {2025},
    howpublished = {Company threat report, 23 April 2025},
    url = {https://www.anthropic.com/news/detecting-and-countering-malicious-uses-of-claude-march-2025},
    urldate = {2026-11-27}
  }
  ```

### S2. Pew digital twins: say that other developers' models did worse
- Where: textbook/chapters/ch09.md:179
- Text now: "The best-performing model, Anthropic's Claude Opus 4.6, missed the human results by 12.4 percentage points on average across the three waves."
- Problem: UNCLEAR (balance, minor) — The sentence is accurate. However, the only model the chapter names is an Anthropic model, described as "best-performing", and readers cannot see what it was compared against. Pew also tested OpenAI's GPT-5.1, which had the larger error.
- Evidence: https://www.pewresearch.org/data-labs/2026/09/30/how-well-synthetic-samples-replicate-public-opinion/ (30 Sept 2026): "Across all three waves, the synthetic polling results differed by an average of 12 percentage points from the estimates produced by the human polls." The per-wave totals are 11.3, 14.7 and 11.2.
- Change to: "The best-performing of the models Pew tested, which included systems from OpenAI and Anthropic, was Anthropic's Claude Opus 4.6. It still missed the human results by 12.4 percentage points on average across the three waves."

## Could not verify
- The *Science* erratum of 22 October 2026 for Costello et al., and the rescinding of the June 2026 expression of concern (line 144). I confirmed the expression of concern of 11 June 2026 through Retraction Watch and EurekAlert. Searches found nothing on what happened later, but the bib notes give specific dates and DOIs.
- The quoted figures from OpenAI's October 2026 "false front" report. Anadolu Agency coverage confirms the Russia and Iran operations and the placement of stories in media outlets. The bib notes that the primary page returns HTTP 403.
- Colombia EU EOM wording; the Clemson and Graphika attribution of the Talarico deepfakes to Storm-1516; the NCSL count of 31 states.
- Barrington et al.'s 604 listeners and the "approximately 80%" and "about 60%" figures.

## Checked and confirmed
- Kramer: FCC $6m forfeiture order of 26 Sept 2024; acquittal in June 2025.
- Kirchenbauer arithmetic: SD √(200·0.25)=7.07; z=4 at about 128 green tokens; one-sided p≈3.2×10⁻⁵. Base-rate example: 990 true positives against 10,000 false alarms, so 91% of alarms are false.
- Meta's H2 2026 report, quoted word for word: "from an occasional tactic employed by the most resourced actors to a near-standard component of influence operation tradecraft"; "behavioral detection approaches remain effective"; every disrupted CIB network used generative AI.
- International AI Safety Report 2026: "documented but not yet widespread".
- Pew (30 Sept 2026): 12.4 pp average error, three waves, 86% vs 45% on billionaires, "far less politically diverse", no plans to use AI to generate survey results, 46% vs 34% on Trump approval.
- SynthID Detector opened 7 Oct 2026 with OpenAI, Nvidia and Kakao, with Apple "soon". Apple added SynthID in iOS 27.2 (about 26 Oct 2026). Apple Reference Image announced 9 Sept 2026.
- ChatGPT designated a VLOSE on 31 Aug 2026, with compliance due by Jan 2027.
- Regulation (EU) 2026/1744 in force 27 July 2026; nudification and CSAM bans from 2 Dec 2026.
- Code of Practice published 10 June 2026; 103 provider and 219 deployer signatories, including Anthropic, Google, Meta, Microsoft and OpenAI (EC list updated 18 Nov 2026).
- Penske suit dismissed 30 Sept 2026: "is not an agreement".
- Talarico won Texas (3 Nov 2026). Lula won the 25 Oct 2026 run-off. TSE declined 4–3 (1 Sept 2026) to fine Flávio Bolsonaro.
- Hungary: Political Capital survey, 52% of those who had seen deepfakes were unsure; Fidesz lost.
- TAKE IT DOWN Act: first conviction (Strahler, Ohio, plea of 7 April 2026).
- UK DUAA s.138 in force 6 Feb 2026. Crime and Policing Act 2026 s.99 in force 29 June 2026, maximum 3 years (Home Office circular).
- xAI renamed SpaceXAI (July 2026), and Musk's announcement of SpaceXSI.
- X fined €120m on 5 Dec 2025. DSA: 45m users, 6% cap, in full since 17 Feb 2024. AI Act Art. 99(4): €15m or 3%.
- Romania: annulment on 6 Dec 2024, TikTok proceedings opened 17 Dec 2024, Dan won in May 2025.
- CETaS: 16 and 11 cases. Kapoor and Narayanan: 78 cases, 39 deceptive. Meta: "less than 1%".
- Persuasion studies (Goldstein, Hackenburg, Costello, Salvi): figures as given.
- Cross-references: Section 2.8 defines the AUC; Chapter 10 covers detector bias (Section 10.3); Section 11.4 covers fraud; Section 13.6 covers copyright.

Tally: claims checked 62 / confirmed 58 / wrong 0 / outdated 0 (4 could not be verified).
