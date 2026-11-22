# Third review: Chapter 8 — Work, Productivity and the Economy

## Verdict
**Ready after the MUST fixes below.** The chapter is accurate to a high standard: every study's sample size, effect size, population and publication status that I checked (Noy & Zhang, Peng et al., Brynjolfsson/Li/Raymond, Dell'Acqua et al., Cui et al., METR 2025 and its 2026 follow-up, Otis et al., Humlum & Vestergaard March 2026, Canaries August 2026, Acemoglu, Aghion & Bunel, Penn Wharton, the Census, BLS, Bick et al., Anthropic Economic Index and Yale/EIG material) matches the source, and all of the arithmetic is correct. The two blocking items are the two proof-day checks the author flagged. The BLS released Q3 2026 productivity on 5 November 2026, and Challenger's October 2026 report (5 November) shows that "market/economic conditions" has overtaken AI as the leading reason for 2026 job cuts. Left as it stands, the Challenger sentence would mislead readers. The SHOULD items are small attribution and precision fixes. None of them carries legal risk. The data-labelling paragraph (Sama/OpenAI) follows the TIME report closely, including Sama's rebuttals.

## MUST change before printing

### M1. US productivity figures: Q3 2026 release now available (author's proof-day check)
- Where: textbook/chapters/ch08.md:221
- Text now: "On the latest figures available at the end of October 2026, nonfarm business labour productivity grew 2.2% in the year to the second quarter of 2026. Since the end of 2019 it has grown at an annual rate of 2.1%, faster than the 1.5% of the 2007–2019 business cycle but equal to the average since 1947 [@bls2026productivity]."
- Problem: OUTDATED. These figures were correct for the 3 September release (I checked: 2.2% y/y to Q2; 2.1% since 2019Q4; 1.5% for 2007–19; 2.1% since 1947). The BLS published the Q3 2026 preliminary release on 5 November 2026, incorporating BEA's 2026 annual NIPA update, and every figure changed. Q3 2026 was +3.6% at an annual rate (output +3.7%, hours +0.1%). The four-quarter change was +2.1%. The current cycle since 2019Q4 now shows 2.2% a year, against 1.5% for 2007–2019 and a long-term rate of 2.2% since 1947Q1. Q2 2026 was revised to 2.3% y/y. The sentence's conclusion ("no break in trend"; the current cycle equals the long-run average) still holds.
- Evidence: BLS release 5 Nov 2026, https://www.bls.gov/news.release/archives/prod2_11052026.htm: "Nonfarm business sector labor productivity increased 3.6 percent in the third quarter of 2026 … From the same quarter a year ago … increased 2.1 percent"; "labor productivity has grown at an annualized rate of 2.2 percent through the third quarter of 2026", "higher than the 1.5-percent rate of the previous business cycle", "the same as the long-term rate of 2.2 percent since the first quarter of 1947". BLS TED, 13 Nov 2026: "Nonfarm business productivity up 2.1 percent from third quarter 2025 to third quarter 2026". The revised Q3 estimate is scheduled for 8 December 2026.
- Change to: "On the figures available in November 2026, nonfarm business labour productivity grew at an annual rate of 3.6% in the third quarter of 2026 and by 2.1% over the year to that quarter. Since the end of 2019 it has grown at an annual rate of 2.2%, faster than the 1.5% of the 2007–2019 business cycle but equal to the average since 1947 [@bls2026productivity]."
- Bib change (bls2026productivity): title "Productivity and Costs, Third Quarter 2026, Preliminary"; howpublished "News release, 5 November 2026"; url https://www.bls.gov/news.release/archives/prod2_11052026.htm; urldate 2026-11-22.

### M2. Challenger job-cut reasons: AI no longer the leading reason for 2026 (author's proof-day check)
- Where: textbook/chapters/ch08.md:156
- Text now: "Employers' own statements point the other way. In announcements tracked by the outplacement firm Challenger, Gray & Christmas, AI was the most-cited reason for planned US job cuts in the first nine months of 2026. It was named for about 120,000 cuts, some 21% of the total, while announced cuts overall were 39% lower than a year earlier, or 15% lower excluding government, whose cuts in 2025 had been exceptional [@challenger2026september]."
- Problem: OUTDATED. The nine-month figures match the September report (AI 120,136 cuts, about 21%, "the leading reason year-to-date"; total 573,195, down 39%; down 15% excluding government). The October 2026 report reverses the headline. Market/economic conditions (130,531 YTD) "has overtaken Artificial Intelligence (AI) as the leading reason for job cuts in 2026". AI was cited for only 1,265 cuts in October, "its lowest monthly total this year", and 121,401 YTD (about 20%). Total cuts through October were 617,189, down 44% on the first ten months of 2025. A reader in 2027 told only that AI was "the most-cited reason" would be misled.
- Evidence: Challenger Report, October 2026, released 5 Nov 2026, https://www.challengergray.com/wp-content/uploads/2026/11/Challenger-Report-October-2026.pdf: "With 130,531 cuts so far this year, Market/Economic Conditions has overtaken Artificial Intelligence (AI) as the leading reason for job cuts in 2026"; "AI was cited for 1,265 cuts in October, its lowest monthly total this year. AI has been cited in 121,401 job cut announcements so far in 2026, approximately 20% of all cuts"; "Through October, employers have announced 617,189 job cuts, down 44% from the 1,099,500 cuts announced in the first 10 months of 2025"; Government "down 93% to 23,049". The October report gives no ex-government percentage. Computed: (617,189 − 23,049)/(1,099,500 − 307,638) = −25%.
- Change to: "Employers' own statements have pointed the other way, though less so in recent months. In announcements tracked by the outplacement firm Challenger, Gray & Christmas, AI was the most-cited reason for planned US job cuts through the spring and summer of 2026, but by the end of October 'market and economic conditions' had overtaken it. Through October, AI had been named for about 121,000 cuts, some 20% of the total, and in October itself for only about 1,300. Announced cuts overall were 44% lower than a year earlier, when federal government cuts had been exceptional [@challenger2026october]."
- Bib change: replace challenger2026september with
  `@misc{challenger2026october, author = {{Challenger, Gray \& Christmas}}, title = {October Layoffs Lowest for the Month Since 2023; Seasonal Hiring Plans Jump 26\%, Led by Record {Amazon} Announcement, Concentrated to Fewer Companies}, howpublished = {Challenger Report, October 2026, released 5 November 2026}, year = {2026}, url = {https://www.challengergray.com/wp-content/uploads/2026/11/Challenger-Report-October-2026.pdf}, urldate = {2026-11-22}}`
  (The key challenger2026september is used only in ch08, so it can be removed.)

## SHOULD change (real but not blocking)

### S1. Customer-support tool described as "GPT-3": the paper does not say so
- Where: ch08.md:96 (Table 8.3, "GPT-3-based assistant, 2020–21") and ch08.md:119 ("The assistant, built on GPT-3 and fine-tuned by a third-party company")
- Problem: UNSUPPORTED BY CITED SOURCE. Both the 2023 and the published versions say only that the tool "is built on a recent version of the Generative Pre-trained Transformer (GPT) family of large language models developed by OpenAI" (arXiv 2304.11771v2, p. 2; v1 has the same wording). Given the 2020–21 roll-out, GPT-3 is likely, but the authors do not name it.
- Change to: Table: "OpenAI GPT-based assistant, 2020–21". Text: "The assistant, built on a version of OpenAI's GPT models and fine-tuned by a third-party company, …"

### S2. OECD: the "predates generative AI" point is the report's, not Cormann's
- Where: ch08.md:154
- Text now: "Presenting it, Secretary-General Mathias Cormann likewise said, according to the French business site Journal du Net, that there was no sign that firms' use of AI was causing a general fall in the demand for labour across member countries, and that young people's difficulty entering work predates generative AI [@barhiye2026ocde]."
- Problem: Partly misattributed. JDN quotes Cormann on the first point ("Jusqu'à présent, rien n'indique que l'utilisation accrue de l'intelligence artificielle par les entreprises entraîne une baisse généralisée de la demande de main-d'œuvre"). The point that young people's difficulty predates generative AI is attributed by JDN to the report/organisation ("l'organisation précise que cette tendance est antérieure à son essor"). Cormann's own words on youth were that AI "n'affaiblit pas les perspectives d'emploi pour les jeunes" (https://www.journaldunet.com/business/1552481-…, 8 July 2026).
- Change to: "Presenting it, Secretary-General Mathias Cormann likewise said, according to the French business site Journal du Net, that there was no sign that firms' use of AI was causing a general fall in the demand for labour across member countries; the report itself notes that young people's difficulty entering work predates generative AI [@barhiye2026ocde]."

### S3. Survey-versus-experiment gap: interpretation attached to a source that does not make it
- Where: ch08.md:221 (last two sentences)
- Text now: "Surveys find time savings of about 2% of all work hours, whereas experiments find gains of 15% or more within the tasks they study. The difference mostly reflects how few hours AI yet touches, since the survey figure averages over non-users and over tasks AI does not reach [@stlouisfed2026does]."
- Problem: UNSUPPORTED BY CITED SOURCE (for the second sentence). The FRED blog post (27 Aug 2026) gives the 2.2% and 6.3% figures but does not compare them with experiments or explain the gap. The reasoning is sound (6.3% of hours touched × a 25–40% in-task saving ≈ 2%), but it is the author's.
- Change to: "Surveys find time savings of about 2% of all work hours [@stlouisfed2026does], whereas experiments find gains of 15% or more within the tasks they study. In the author's reading, the difference mostly reflects how few hours AI yet touches: the survey figure averages over non-users and over tasks AI does not reach, and AI was used in only about 6% of work hours."

### S4. Cui et al. is now in print
- Where: textbook/bib/ch08.bib, cui2026effects
- Problem: The bib entry has only "Published online 27 February 2026". Crossref (10.1287/mnsc.2025.00535) now gives Management Science vol. 72, no. 11, pp. 9408–9420, November 2026.
- Change to: add `volume = {72}, number = {11}, pages = {9408--9420}` and delete the "Published online" note.

### S5. Goldman Sachs date and scope
- Where: ch08.md:217
- Text now: "In research published by the investment bank Goldman Sachs in April 2023, its economists estimated that generative AI could raise global GDP by 7% and lift productivity growth by 1.5 percentage points over a ten-year period"
- Problem: The underlying Briggs & Kodnani report ("The Potentially Large Effects of Artificial Intelligence on Economic Growth") is dated 26 March 2023 and was reported by Bloomberg and Reuters on 27 March. The GS Insights summary cited in the bib is dated 5 April. The 1.5 pp figure is for US labour-productivity growth. A minor point, but an expert would notice.
- Change to: "In research published by the investment bank Goldman Sachs in March 2023, its economists estimated that generative AI could eventually raise global GDP by 7% and lift US labour-productivity growth by about 1.5 percentage points a year over a ten-year period". Keep the bib entry, which is the April summary.

### S6. Hosseini & Lichtinger: numbers come from the May 2026 revision
- Where: ch08.md:166; bib hosseinimaasoum2025generative
- Problem: "65 million workers at more than 280,000 US firms" is correct for the 6 May 2026 version. The October 2025 SSRN version cited by the bib (year 2025) says "62 million workers across 285,000 firms".
- Change to: add `note = {First version 31 August 2025; revised 6 May 2026}` to the bib entry.

### S7. Eloundou "agreed about four times in five"
- Where: ch08.md:23
- Text now: "Human annotators and an early version of GPT-4 both applied the rubric, and their labels agreed about four times in five."
- Problem: Slight overstatement. Table 2 of the v5 preprint reports agreement of 80.8% (α) and 82.1% (ζ) but 65.6% for β, the measure the headline numbers use.
- Change to: "… and their labels agreed between about two-thirds and four-fifths of the time, depending on the measure."

### S8 (optional currency). BTOS: a newer reading exists
- Where: ch08.md:65 and Table 8.2
- Note: Not wrong, since the book is current to October. Census National.xlsx now has 25.0% for 19 Oct–1 Nov 2026 (published 19 Nov), and a new question on employees' use of generative "SI" (27.6%). No change is needed unless the author wants to update to November.

## Could not verify
- ch08.md:249, Budzyń et al. dates "between September 2021 and March 2022": confirmed by secondary summaries of the Lancet abstract (1,443 colonoscopies, 795/648, 28.4% → 22.4%, four centres, retrospective) but not opened at the Lancet (paywall). Low risk.
- ch08.md:241, SHOOT report of the SAG-AFTRA board release (11 May 2026): not opened. The "significant additional value" wording and the June 2026 ratification at 91.42% are confirmed by TheWrap, Variety and Fortune coverage (5 June 2026). Low risk.
- ch08.md:243, Microsoft/AFL-CIO "neutrality framework" (Dec 2023) and the TIME May 2023 Nairobi union piece: not re-fetched (settled 2023 facts consistent with my knowledge). Low risk.
- bib europeanparliament2026regulation "of 8 July 2026" (date of signature) and "91 FR 63129" (EO page number): not verified. Chapter 13's reviewer may have covered these. Low risk.

## Reader notes
1. ch08.md:65, "(Since a September 2026 executive order the survey's wording calls the technology "Super Intelligence", …)". A lay reader will stop here. One clause saying the order renamed "AI" as "Super Intelligence" in federal usage, without changing what is covered, would prevent a double take.
2. ch08.md:156, "Employers' own statements point the other way." After M2 this framing needs softening, as in the proposed text, or the paragraph contradicts its own data.
3. ch08.md:202, the Aghion & Bunel paragraph packs nine numbers into one paragraph. It is correct, but Table 8.4 already carries most of them, and the prose could drop the 25%/14%/15% customer-support aside.
4. ch08.md:221, the J-curve paragraph mixes three topics: official statistics, the J-curve and the survey/experiment gap. A paragraph break before "A different gap needs no J-curve" would help.
5. ch08.md:3 and 130, the METR trial is described twice (opening, then §8.3). This is intentional and works, but the second description repeats "16 developers".
6. ch08.md:37 vs 39, "one in four workers worldwide" (ILO) against "almost 40%" (IMF). The text explains the difference well. No change needed.
7. Table 8.3, "Time −18% (returning, n = 10)": the source says "speedup of −18%". The book's reading (18% faster) is consistent with METR's own framing ("Our raw results show some evidence for speedup"). Some secondary coverage misreads it as slower, so the table's explicit "Time" label is valuable. Keep it.

## Checked and confirmed

**Opening and §8.1 Tasks and exposure**
- l.3: METR 16 developers, 246 issues, Feb–June 2025, forecast −24%, experts 39%/38%, +19%, post-hoc 20%: arXiv 2507.09089 abstract
- l.15: Autor et al. QJE 2024, eight decades, majority of employment in specialties since 1940, automation vs augmentation since 1980: Crossref abstract (QJE 139(3))
- l.15: Acemoglu & Restrepo 2022, 50–70%, 1980–2016: Crossref abstract (Econometrica 90(5))
- l.21: Felten et al. 2023 LM-AIOE, correlation 0.979, telemarketers; English, foreign-language and history post-secondary teachers: arXiv 2303.01157 abstract and p. 5 table
- l.23: Eloundou rubric, "third party … would not notice or care" quote, α/β/ζ definitions: arXiv 2303.10130v5
- l.25: 80% / 19% (β); wages and science/critical-thinking finding: v5 p. 1 and §4
- Table 8.1: task-level 15/14, 31/35, 47/56; 3% (human α), 19% (β), up to 49% (ζ); core tasks weighted double: v5 Table 3 and p. 3
- l.25: Science 2024 version: Crossref (Science 384:1306)
- l.37: ILO 20 May 2025, "transformation, not replacement, is the most likely outcome"; 25%; 34% in HICs: ILO news release
- l.37: Gradient 4 3.3%; 11% in low-income countries: ILO WP140/research brief (via search)
- l.39: IMF almost 40% / 60% / 40% / 26%, AIOE-based, median thresholds: IMF SDN 2024/001 (via search)
- l.49: BLS exposure categories, 831 occupations, Felten / Eloundou / Eisfeldt plus Anthropic and Microsoft usage, "Exposure does not imply job loss …", no automation/augmentation distinction, 27 Aug 2026: bls.gov page

**§8.2 Adoption**
- l.57: Bick et al. faster than the PC: Mgmt Sci 72(10) abstract (Crossref)
- l.57: 62% by May 2026, four authors, 1 Sep 2026: St. Louis Fed blog
- Table 8.2: 39.2%, 6.3%, 2.2% for Q2 2026: FRED blog 27 Aug 2026
- l.59: reweighting after the question-order test; "may have increased labor productivity by up to 1.3%"; caveat: St. Louis Fed 13 Nov 2025
- l.61: Humlum & Vestergaard revised March 2026; 11 occupations; 25,000/7,000; 40%/7%; 93%/28%/19%; 8%/17% new tasks: NBER w33777 page and PDF
- Table 8.2: about 3% of work hours: NBER w33777 PDF p. 40
- l.65: BTOS ~10% in late 2025, double mid-2024; question change Nov 2025; information/professional services nearly 4 in 10; agriculture/transport/construction <10%: Minneapolis Fed 29 May 2026
- l.65: 24.6% for 21 Sep–4 Oct 2026 (published 22 Oct); cycle from 17 Nov 2025; H1 2026 range 17.5–21.7%; "Super Intelligence" wording: Census National.xlsx
- l.65: EO 14434 signed 29 Sep 2026, published 2 Oct 2026, renames AI as SI: Federal Register/White House (via search)
- l.67: Bonney et al. CES-WP-26-25: 18%/32%; 50–60% in large Info/Prof/Finance firms; 57% use ≤3 functions; Sales & Marketing 52%; 66% augment only; 2.0% of AI-using firms report decreases: Census PDF
- l.71: Handa et al. >4 million conversations; software and writing nearly half; 57/43: arXiv 2503.04761
- l.71: Anthropic Jan 2026: 1M + 1M, 13–20 Nov 2025; 52%/45%; API about three-quarters automation: anthropic.com, 15 Jan 2026
- l.73: Massenkoff et al. 26 June 2026, ~9,700 respondents, ~30% computer/math vs 4%: anthropic.com

**§8.3 Experiments (Table 8.3, Figure 8.2)**
- Noy & Zhang: 453, preregistered, −40%/+18%, inequality narrowed, twice as likely to use ChatGPT two weeks later: Science 381:187 abstract
- Peng et al.: 95 recruited via Upwork, 45 treated, HTTP server in JavaScript, May–June 2022, 55.8% (95% CI 21–89%), still a preprint: arXiv 2302.06590 and search
- Brynjolfsson et al.: 5,172 agents; +15%; lowest-skill quintile +36%; top-skill small speed gains and small quality decline; two-month vs six-month tenure; moderately rare problems; English fluency; politeness and manager requests; facilitates learning: QJE 140(2) abstract and arXiv v2
- Brynjolfsson et al.: 89% outside US, mainly Philippines; Fortune 500 business-process software firm serving SMBs; roll-out Fall 2020–Winter 2021: arXiv v2
- Dell'Acqua et al.: 758, three arms, 18 tasks, 12.2%/25.1%/19%: Org Sci 37(2):403–423 abstract
- Cui et al.: Microsoft, Accenture and a Fortune 100 firm; 4,867; 26.08% (SE 10.3%); less experienced gain more: Mgmt Sci abstract
- Cui et al.: electronics manufacturer; 4–8 months; Microsoft take-up 42.5% after two reminders; IV; recent hires and junior staff gain: MIT draft PDF
- METR: >decade of experience, 5 years on repo, ~1.1M LOC, five likely factors, <44% acceptance, 9% reviewing: arXiv 2507.09089 Table 1 and §2.1
- METR 95% CI +2% to +39%: METR blog 24 Feb 2026
- METR follow-up: Aug 2025 start; 57 developers (10/47); 800+ tasks; −18% (−38 to +9); −4% (−15 to +9); 30–50% withheld tasks; developers declined to participate; "only very weak evidence"; likely more sped up in early 2026: METR blog 24 Feb 2026
- No later METR results or journal publication of Becker et al. as of 22 Nov 2026: search
- Otis et al.: no significant average effect; >0.20 SD gap; ~10% worse / >15% better; difference lies in advice implemented; Mgmt Sci online 10 Jul 2026: Crossref abstract
- Shen & Tamkin: no significant speed gain; −17% / two grade points; six patterns, three preserving learning; Trio library: arXiv 2601.20245 v2
- l.142: MIT statement 16 May 2025, quote exact, arXiv withdrawal request: economics.mit.edu
- Fig 8.2 Cui interval 5.9–46.3 (recomputed); METR follow-up CI "level not stated" accurate: figs_ch08.py vs sources

**§8.4 Jobs and wages**
- l.148: Amodei to Axios, May 2025: half of entry-level white-collar jobs, 10–20% unemployment in one to five years: quoted identically in Humlum & Vestergaard fn. 1; Axios URL dated 28 May 2025
- l.152: H&V null effects, ruling out >2% at two years; no occupation significant; occupational switching into IT-support and clerical roles; +12 pp; records to Dec 2024: NBER w33777 abstract and introduction
- l.154: Yale 1 Oct 2025: 33 months; "no sign of being related to changes in employment or unemployment"; "Better data is needed": budgetlab.yale.edu
- l.154: tracker updated 14 Oct 2026 (still the latest on 22 Nov), "does not yet clearly indicate an AI-related labor market footprint": budgetlab.yale.edu
- l.154: Yale May 2026 piece finds no clear effects comparing exposed and unexposed occupations: budgetlab page (via search)
- l.154: EIG 10 Aug 2025: +0.30 vs +0.94 pp; five measures; young workers and graduates in both groups: eig.org
- l.154: OECD Employment Outlook 2026 on geographic disparities, published 7 July (a Tuesday); Cormann quotation: JDN 8 Jul 2026; see S2
- l.156: September Challenger figures as stated (correct at the time): Challenger Sept 2026 PDF; see M2
- l.156: Beige Book Oct 2026: five districts; attrition, delayed hiring, less job creation after productivity gains from AI: federalreserve.gov
- l.160: Hui et al.: employment and earnings fall; past performance gives no protection; top freelancers suggestively hit harder: Org Sci 35(6) abstract
- l.160: Demirci et al.: 21%, eight months, 17% for image creation: Mgmt Sci 71(10) abstract
- l.164: Canaries Aug 2026: ADP >26M workers; 3.5–5M balanced panel; data to June 2026; −11% vs +10%; 19% gap widening since Aug 2025; hiring not separations; employment not base pay; substitutive vs complementary: Canaries_August2026.pdf abstract and pp. 3–8
- l.171, 173: robustness (excl. tech/computer occupations, interest rates, remote work); attenuates with education; pre-trends; larger than national surveys; "early, descriptive indicators": same PDF
- No version newer than Aug 2026: search
- l.166: Hosseini & Lichtinger, 65M workers, >280,000 firms, junior decline at adopters through hiring: May 2026 version PDF; see S6
- l.166: PwC 15 June 2026: >1 billion ads; US entry-level exposed roles seven times more likely to require senior "human-intensive" skills (leadership, face-to-face): PR Newswire release
- l.173: H&V replicate the early-career decline but find it not driven by adopters; no differential changes in hires/separations: NBER w33777 introduction
- l.173: Fairlie & Wu NBER w35796 (Sept 2026): CPS summer 2026; no significant rise relative to older graduates or non-graduates: NBER abstract
- l.173: Rodgers & Kassens 30 Jun 2026: about a third, Apr 2023–Dec 2025, "not whether firms are using AI to automate jobs or to screen applicants": St. Louis Fed

**§8.5 Macroeconomics (box and Table 8.4)**
- Acemoglu Economic Policy: ≤0.66%, <0.53%: Crossref abstract (40(121):13–58)
- Acemoglu WP: 19.9%; 23%; 4.6%; 27% (Noy & Zhang + BLR, Peng excluded); 0.57; 15.4%; 0.71%; ~0.07; hard tasks 7%; <0.55%; GDP 1.1% / 0.92%; 1.6–1.8%; 7% GDP / 1.5 pp for GS: MIT WP PDF
- Aghion & Bunel June 2024: 60% (Pizzinelli et al.); 22% annual compute-cost decline → ~50%; BLR ~25%; average 40%; 0.68 pp; 0.07–1.24; 0.8–1.3 by second method; ideas production omitted: FRBSF PDF
- Penn Wharton 8 Sep 2025: 40% of labour income; 23%; 25→40%; 1.5% by 2035; 3.7% by 2075; peak 0.2 pp in 2032: PWBM page
- l.217: Anthropic 1.8 pp; 1.2 (Claude.ai) / 1.0 (API) with task success: anthropic.com Jan 2026
- l.221: J-curve 15.9% higher TFP by end-2017: AEJ:Macro 13(1) abstract
- l.221: H&V J-curve reading (cites Brynjolfsson, Rock and Syverson; "productivity J-curves"): NBER w33777 PDF
- l.221: Q2 2026 BLS figures as stated (correct at the time); Q3 release: see M1

**§8.6 Hidden labour and bargaining**
- l.229: TIME 18 Jan 2023: about three dozen workers; $1.32–$2; $12.50; Sama "covers all costs"; all four mentally scarred; counselling rare and unhelpful, which Sama disputed; ended Feb 2022, eight months early; detector built into ChatGPT: time.com
- l.231: Fairwork 2023: 15 platforms; three scored 5; none of the rest >3; four zero; "Microwork platforms were among the lowest scores" (PDF p. 2); Global North/South: Fairwork PDF
- l.239–241: WGA 2026 MBA: "preserves all of the protections negotiated in 2023"; written notice of licensing for GAI training; discussion including payment; 2 May 2026–1 May 2030: wga.org summary
- l.241: SAG-AFTRA ratified June 2026, 91.42%, four-year deal; "significant additional value": TheWrap/Variety/Fortune (via search)

**§8.7 Deskilling**
- l.249: Budzyń et al. 1,443; 28.4% → 22.4%; four Polish centres; retrospective observational; "might": search summaries of the Lancet paper
- l.249: Pedersen et al. 13 endoscopists, PDR-5, no deskilling or upskilling after CADe: Endoscopy 58(9) abstract
- l.251: Shen & Tamkin details: see §8.3

**§8.8 Inequality and policy**
- l.259: Acemoglu inequality findings (more evenly spread, no reduction in labour-income inequality, capital–labour gap): Economic Policy abstract
- l.259, 261: IMF higher returns to capital and wealth inequality; women and college-educated more exposed but better placed; older workers: SDN abstract
- l.261: ILO–NASK 9.6% vs 3.5% (HICs): ILO release
- l.263: Pew Oct 2024, 52% worried / 36% hopeful, 5,273 workers: pewresearch.org
- l.267: Digital Omnibus 2026/1744, OJ 24 Jul 2026, in force 27 Jul; Annex III high-risk moved from 2 Aug 2026 to 2 Dec 2027: law-firm alerts (White & Case, Lewis Silkin) via search
- l.267: Annex III point 4 and Art. 26(7): consistent with the AI Act text
- l.271: AI Action Plan: "Remove Red Tape and Onerous Regulation"; "worker-first AI agenda"; AI Workforce Research Hub under DOL: whitehouse.gov PDF
- l.275: Altman 2021: American Equity Fund; 2.5% of market value of large companies and of privately held land; citizens over 18: moores.samaltman.com
- l.275: Vivalt et al. QJE 2026: 1,000 × $1,000/month for three years vs 2,000 × $50; −4.2 pp participation; 1–2 h/week; leisure; no quality-of-employment gain: QJE 141(4) abstract

**Arithmetic recomputed (all correct):** 0.199×0.23 = 0.046; 0.27×0.57 = 0.154; 0.046×0.154 = 0.71%; Aghion & Bunel 0.6×0.5×0.4×0.57 = 6.84% (≈0.68 pp/yr); ratio of inputs ≈ 9.7 ("tenfold"); Cui CI 26.08 ± 1.96×10.3 = 5.9–46.3; Peng/Noy average (40+14)/2 = 27; A&B three-study average (40+55.8+25)/3 ≈ 40; Challenger ex-government change through October −25%; AI share of October YTD cuts 19.7% ("about 20%"); weekday checks (7 Jul 2026 Tuesday; 29 Sep 2026 signing).

**Bib entries checked (31):** acemoglu2019automation, autor2024new, felten2021occupational, felten2023language, eloundou2023gpts, eloundou2024gpts, cazzaniga2024genai, gmyrek2025generative, noy2023experimental, brynjolfsson2025generative, dellacqua2026navigating, peng2023impact, cui2026effects (S4), becker2025measuring, otis2026uneven, humlum2025still, bonney2026microstructure, handa2025which, brynjolfsson2026canaries, hosseinimaasoum2025generative (S6), acemoglu2025simple, brynjolfsson2021productivity, budzyn2025endoscopist, vivalt2026employment, pedersen2026learning, acemoglu2022tasks, hulten1978growth, demirci2025who, hui2024short, bick2026rapid, fairlie2026early, plus URL-dated items opened above (anthropic2026economic, massenkoff2026anthropic, stlouisfed2026does, bick2026what, bick2025state, census2026business, challenger2026september (M2), bls2026productivity (M1), bls2026artificial, garcialuna2026ai, rodgers2026how, federalreserve2026beige, gimbel2025evaluating, budgetlab2026tracking, eckhardt2025ai, barhiye2026ocde, perrigo2023exclusive, fairwork2023work, wga2026summary, mit2025assuring, whitehouse2025winning, altman2021moores, arnon2025projected, aghion2024ai, acemoglu2024simple, svanberg2024beyond, korinek2019artificial, autor2024applying, lin2025us, ilo2025one, trump2026inaugurating). Problems: bls2026productivity and challenger2026september superseded (M1, M2); cui2026effects missing volume/pages (S4); hosseinimaasoum2025generative version note (S6).

## Tally
Claims checked against a web source: 196. Confirmed: 186. Wrong: 0. Outdated: 2 (M1, M2). Unsupported by cited source: 3 (S1 "GPT-3"; S2 Cormann attribution; S3 survey/experiment gap). Minor imprecision: 3 (S5 Goldman date/scope; S6 version; S7 agreement rate). Could not verify (fully): 4 (all low risk). Arithmetic items recomputed: 11 (errors: 0). Bib entries checked: 31 against Crossref/arXiv/publisher, plus 31 URL entries opened (problems: 4: two superseded by M1/M2, S4, S6).
