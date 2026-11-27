# Review 5: Chapter 9, Information, Media and Democracy

## Verdict
Ready to print after three small SHOULD fixes. The chapter is carefully sourced and hedged. Every 2025–2026 claim I checked against a primary or near-primary source held up, including all the quotations from Meta, Pew, CETaS, the Colombia EU EOM, TheWrap/Penske, Conjur/TSE, the Commission's Code of Practice page and UK legislation. I found no MUST items. The SHOULD items are a rename that has not taken effect and is not supported by the cited sources, a loose paraphrase of the Hungary authors, and a state-law count that later reporting replaced.

## MUST change before printing
None.

## SHOULD change

### S1. "SpaceXSI" rename stated as done, and the cited sources do not support it
- Where: textbook/chapters/ch09.md:246
- Text now: "here Grok's developer, which was renamed from xAI to SpaceXAI in July 2026 after its merger with SpaceX and to SpaceXSI in October [@reuters2026concerns; @engadget2026xai]"
- Problem: UNSUPPORTED / OUTDATED-risk. On 4 October 2026 Musk said he *would* rename SpaceXAI to SpaceXSI and gave no date. Reuters reported no timeline, and the unit's X account had not changed. Neither cited source mentions SpaceXSI: Engadget covers the July rename, and the Reuters/BusinessDay piece of 14 October still says "Musk's SpaceXAI". Ch03 Table (ch03.md:443) uses "SpaceXAI", so stating the rename as done is also inconsistent within the book.
- Evidence: Jalopnik, 5 Oct 2026, https://www.jalopnik.com/2278279/why-spacex-rebranding-ai-artificial-intelligence-vs-super-intelligence/ : Musk: "Yes, we will make that change"; "Reuters reported that Musk did not say when the change would happen… SpaceXAI remains an official entity." BusinessDay/Reuters, 14 Oct 2026 (cited): "X and Musk's SpaceXAI".
- Change to: "here Grok's developer, which was renamed from xAI to SpaceXAI in July 2026 after its merger with SpaceX (in October Musk said it would become SpaceXSI) [@reuters2026concerns; @engadget2026xai]"

### S2. Hungary: the authors' reasons are paraphrased as reasons Fidesz lost
- Where: textbook/chapters/ch09.md:126
- Text now: "Fidesz lost, which the authors credit mainly to a credible challenger and voter fatigue with government messaging"
- Problem: UNCLEAR / slightly MISATTRIBUTED. The EDMO piece explains why the AI tactics had limited success, not why Fidesz lost. It gives six reasons, and the first is public rejection of AI-manipulated content (90% "entirely unacceptable"). It does not single out two of them as the main ones.
- Evidence: EDMO blog (Krekó et al., 2026), https://edmo.eu/blog/hungarys-2026-election-ai-driven-post-reality-campaigning-and-its-limits/ : the tactics were "only partially successful in swaying public opinion". Under the heading "Lack of success- possible reasons" the authors list public rejection, a challenger who could "fact-check" Orbán's narratives, Tisza's optimistic campaign, voter fatigue with disinformation, pre-emptive warnings, and a large independent media audience.
- Change to: "Fidesz lost. The authors attribute the limited success of its AI tactics to several factors, among them public rejection of AI-manipulated content, a credible challenger and voter fatigue with government disinformation"

### S3. "28 states" is a March figure. Later counts were higher.
- Where: textbook/chapters/ch09.md:128
- Text now: "No federal rule applied, and 28 states had laws on AI in political ads, mostly requiring disclosure [@ax2026ai]."
- Problem: OUTDATED (minor). The sentence is anchored to the March Reuters report, so it is not wrong. But readers will take it as the position for the campaign. NPR (16 Sept 2026, citing NCSL) and Al Jazeera (9 Oct 2026) give 31 states.
- Evidence: NPR, 16 Sept 2026, https://npr.org/2026/09/16/nx-s1-5953990/ai-political-ads-2026-midterms : "31 states have passed laws prohibiting deepfakes or requiring disclosures, according to the National Conference of State Legislatures" (as summarised in search results; not fetched in full).
- Change to: "No federal rule applied, and 28 states had laws on AI in political ads, mostly requiring disclosure [@ax2026ai]; by September the National Conference of State Legislatures counted 31." (plus a bib entry for the NPR article; alternatively just add "at the time").

## Could not verify
- Lin et al. (2025, *Nature*) effect sizes (2.88 [2.02–3.74], 10.05, 9.94, 22.73, n = 193, sample sizes, "slightly more than a third" persistence, and no accuracy–persuasion association). The article is paywalled. The abstract confirms the three elections, the ballot measure on psychedelics, effects larger than for video ads, persuasion by facts and evidence, and more inaccurate claims for right-leaning candidates in all three countries.
- The corrected wording "primary analyses included 2044 conspiracy believers…" in the Science erratum. Crossref confirms that the erratum (10.1126/science.aem1178, 22 Oct 2026) and the expression of concern, now titled "RESCINDED: Editorial Expression of Concern" (11 Jun 2026), both exist. I could not read the erratum text.
- Golaszewski et al. 2026 C2PA "exclusion range" findings (ePrint 2026/804), not opened.
- Kirchenbauer et al. "159.5 green tokens" average (Table values), not re-opened. The threshold arithmetic is correct: z = 4 needs more than 128.3 green tokens, so "about 128" is acceptable.

## Checked and confirmed
- NH robocall: 5,000–25,000 recipients; FCC $6m forfeiture order of 26 Sept 2024; Kramer acquitted June 2025.
- Barrington et al. (Sci. Rep. 2025): 604 participants; "for as little as $5 a month"; about 80% identity match and about 60% detection; ElevenLabs Instant Voice Cloning. The book's "more than 200 speakers" is correct (the paper has 220).
- Meta H2 2026 Adversarial Threat Report (August 2026), p. 34: "from an occasional tactic employed by the most resourced actors to a near-standard component of influence operation tradecraft"; every network used generative AI; "behavioral detection approaches remain effective".
- OpenAI "false front" report, 8 Oct 2026: Russia and Iran; operations that land stories in real media outlets have the highest potential reach.
- International AI Safety Report 2026: "documented but not yet widespread".
- Google SynthID Detector post (7 Oct 2026, updated 29 Oct): partners OpenAI, NVIDIA, Kakao, Apple; "over 180 billion images and videos"; images, video and audio.
- Apple iPhone 18 Pro (9 Sept 2026): opt-in Reference Image, signed sensor data, no mention of C2PA, SynthID support in a later update.
- Pew (30 Sept 2026): Claude Opus 4.6 best model; 12.4-point average error across three waves (Waves 185, 190 and 192); "far less politically diverse"; 86% vs 45% on billionaires; 46% vs 34% Trump approval; "no current or future plans".
- CETaS 16/11 viral cases; Kapoor & Narayanan 78/39; Goldstein 2024 figures; Costello 2024 figures; Salvi 64.4%/81.2%; Hackenburg 76,977/19 models/707 issues.
- Colombia EU EOM final report: "frequent disinformation and an unprecedented use of AI and deepfakes"; "its most notable use was as a campaign tool".
- Talarico deepfake of 20 Oct 2026, the former student's denial, the Graphika/Clemson attribution to Storm-1516, and PolitiFact's coverage. TIME (Chow & Booth, 4 Nov 2026): deepfakes "do not appear to have had an outsize impact in many races"; Talarico beat Paxton.
- TSE ruling by 4 to 3 on 1 Sept 2026 (Conjur, 2 Sept); Lula won the 25 Oct 2026 run-off (51.78%).
- DNR 2026: 7%→10%; no growth in the US, UK, France or Germany; trust 20% vs 37% (UK 6%); click-through 42% vs 44%; Chartbeat −33% globally and −38% in the US; −43% expected; 48 markets.
- CMA conduct requirement of 3 June 2026 (opt-out and clear links); Penske suit dismissed 30 Sept 2026 by Judge Mehta, "an expectation is not an agreement", without prejudice.
- EBU/BBC 45%/31%/20%, 2,709 core responses; NewsGuard Pravda 33%.
- ChatGPT designated a VLOSE on 31 Aug 2026; Code of Practice of 10 June 2026; 103 provider and 219 deployer signatories (page updated 18 Nov 2026), all five named firms in Section 1; Digital Omnibus (EU) 2026/1744 in force 27 July 2026, with nudification/CSAM ban and Art. 50(2) grace period for existing systems to 2 Dec 2026.
- DUAA 2025 s.138 in force 6 Feb 2026, summary-only offence; Crime and Policing Act 2026 s.99 in force 29 June 2026 (S.I. 2026/689), 3 years on indictment, reasonable-steps defence.
- TAKE IT DOWN Act: first conviction (Strahler, Ohio, plea of 7 April 2026); Senate Commerce release of 19 May 2026.
- Ofcom investigation of 12 Jan 2026 and the October "new phase"; the Grok image block for UK users.
- Base-rate arithmetic: 990 true and 10,000 false alarms gives 91% false alarms. The watermark σ = √50 ≈ 7.07 and the false-positive rate of 3×10⁻⁵ are correct.
- Internal cross-references: Section 2.8 defines the AUC; Section 7.6 (open-weight); Section 11.4 (fraud); Section 13.6 (copyright); Ch10 covers detector bias against non-native writers.

## Tally
Claims checked: 78 · confirmed: 74 · wrong: 0 · outdated or unsupported: 3 (S1–S3) · could not verify: 4 (listed above; a few related figures, such as all of Lin et al.'s effect sizes, are grouped into one entry)
