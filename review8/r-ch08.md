# Review 8: Chapter 8 (Work, Productivity and the Economy)

## Verdict
Ready to print after small fixes. Every 2026 figure I checked matches its primary source: BLS productivity for Q3 2026, the Challenger report for October 2026, the BLS AI exposure categories, the Census BTOS file, the METR follow-up, the January 2026 Anthropic Economic Index, the WGA 2026 MBA, SAG-AFTRA ratification, the Vivalt et al. revision and its QJE publication, the August 2026 "Canaries" revision, Fairlie & Wu, and Executive Order 14434. Acemoglu's arithmetic is reproduced exactly from the April 2024 working paper. The chapter weighs evidence fairly and labels interested parties (Amodei, the Anthropic estimates, the Anthropic-authored skills study).

The main weakness is balance between companies. The subsection "Usage data from AI companies" describes only Anthropic's data. Microsoft's Copilot study, which BLS itself uses, and OpenAI's NBER study of ChatGPT use are both left out. Every number in the chapter is right, so I list this as SHOULD rather than MUST, but it is the first item to fix in a book written by Anthropic models.

## MUST change before printing
None.

## SHOULD change

### S1. "Usage data from AI companies" covers only Anthropic (company balance)
- Where: textbook/chapters/ch08.md:69–73 (and Table 8.2, line 84)
- Text now: "AI providers can observe use directly. Anthropic, the developer of the Claude models, publishes an "Economic Index" …"
- Problem: UNCLEAR / balance. The subsection heading is plural, but only Anthropic's data are described. Two comparable studies are missing. Microsoft researchers analysed 200,000 Copilot conversations (Tomlinson et al.), and line 49 already says BLS combines that study with Anthropic's data. OpenAI economists and academic co-authors published an NBER study of ChatGPT use. Their finding that most consumer messages are not work-related is also directly relevant to adoption.
- Evidence: NBER w34255 (Chatterji, Cunningham, Deming, Hitzig, Ong, Shan, Wadman, Sept 2025): non-work messages "now represent more than 70% of all consumer ChatGPT messages" (53% in June 2024, 73% in June 2025). arXiv 2507.07935 (Tomlinson, Jaffe, Wang, Counts, Suri, Microsoft, July 2025): 200,000 anonymised Bing Copilot conversations from 2024, mapped to O*NET work activities. BLS page: "Massenkoff and McCrory (Anthropic) … Tomlinson, Jaffe, Wang, Counts, and Suri (Microsoft)".
- Change to: insert after the first sentence: "OpenAI economists and academic co-authors, classifying a sample of consumer ChatGPT messages, found that the share not related to work rose from 53% in June 2024 to 73% in June 2025 [@chatterji2025how]. Microsoft researchers mapped 200,000 Copilot conversations from 2024 to O\*NET work activities and found information gathering and writing the most common goals [@tomlinson2025working]. Anthropic, the developer of the Claude models, publishes an "Economic Index" …". Then change "for one company's products and customers only" to "each for one company's products and customers only".
  New bib entries:
  ```
  @techreport{chatterji2025how,
    author = {Chatterji, Aaron and Cunningham, Thomas and Deming, David J. and Hitzig, Zoe and Ong, Christopher and Shan, Carl Yan and Wadman, Kevin},
    title = {How People Use {ChatGPT}},
    institution = {National Bureau of Economic Research},
    type = {NBER Working Paper}, number = {34255}, year = {2025},
    url = {https://www.nber.org/papers/w34255}, doi = {10.3386/w34255}
  }
  @misc{tomlinson2025working,
    author = {Tomlinson, Kiran and Jaffe, Sonia and Wang, Will and Counts, Scott and Suri, Siddharth},
    title = {Working with {AI}: Measuring the Applicability of Generative {AI} to Occupations},
    year = {2025}, howpublished = {arXiv preprint 2507.07935 (Microsoft Research)},
    url = {https://arxiv.org/abs/2507.07935}
  }
  ```

### S2. Say that the latest BTOS reading uses the "Super Intelligence" wording
- Where: textbook/chapters/ch08.md:65 and Table 8.2 line 81
- Text now: "and 25.0% in the two weeks to 1 November 2026 [@census2026business]." / table row "Use AI in any business function | 25.0%"
- Problem: UNCLEAR. The Census file now asks whether the business used "Super Intelligence or SI (formerly referred to as Artificial Intelligence or AI)". In the last two periods the "Do not know" share rose from about 9.6% to 13.9% and then 13.3%, which suggests the new wording did change answers. The 25.0% figure itself is correct, and the rise in "Yes" (24.2% to 25.0%) is smooth.
- Evidence: Census BTOS National.xlsx (published 19 Nov 2026), question 7: Yes 25.0%, 24.2%, 24.6% …; Do not know 13.3%, 13.9%, 9.6%, 9.8% …
- Change to: in the table, "Use AI ("Super Intelligence") in any business function | 25.0%"; in the text, after the parenthesis, add: "In the first periods with the new wording, the share answering "do not know" rose from about 10% to about 13%."

### S3. "Nearly four years" against a one-to-five-year forecast
- Where: textbook/chapters/ch08.md:148
- Text now: "…and it does not yet show change on that scale."
- Problem: UNCLEAR (fairness to a named person). Amodei made the forecast in May 2025 for "one to five years", so about 18 months of it had passed by November 2026. As written, the sentence can read as if the forecast had already failed.
- Change to: "…and it does not yet show change on that scale, though the period Amodei named runs to 2030."

## Could not verify
- Bick et al. tracker values (39.2%, 6.3%, 2.2%) and the 62% figure on the St. Louis Fed blog for May 2026.
- Humlum & Vestergaard March 2026 revision: 93%, 28%, 19%, 8% and 17%.
- PwC 2026 Barometer: entry-level roles "seven times more likely".
- OECD Employment Outlook 2026, and Cormann's remark as reported by Journal du Net; Beige Book for October 2026 ("five of the twelve districts").
- Penn Wharton figures (1.5% by 2035, 3.7% by 2075).

## Checked and confirmed
- BLS Productivity, Q3 2026 (5 Nov 2026): 3.6% annual rate; 2.1% over four quarters; 2.2% since Q4 2019; 1.5% for 2007–19; 2.2% since 1947.
- Challenger, October 2026: AI named for 121,401 cuts so far in 2026 (about 20%); 1,265 in October; "Market/Economic Conditions has overtaken Artificial Intelligence"; announced cuts down 44% year on year.
- BLS AI Exposure Categories (27 Aug 2026): 831 occupations; Felten, Eloundou and Eisfeldt indices plus Anthropic and Microsoft usage data; "Exposure does not imply job loss"; no split between automation and augmentation.
- EO 14434 "Inaugurating the Era of Super Intelligence" (signed 29 Sep 2026): requires "Super Intelligence" in place of "AI" in federal usage, with the same statutory meaning. The Census question wording has changed accordingly.
- METR, 24 Feb 2026: 57 developers, 800+ tasks; −18% (−38% to +9%) and −4% (−15% to +9%); 30–50% withheld tasks; "only very weak evidence"; began August 2025.
- Anthropic Economic Index, Jan 2026: 52% augmentation / 45% automation; three-quarters of API traffic automation; 1.8 percentage points falling to 1.0–1.2; 1M + 1M samples from November 2025.
- WGA 2026 MBA: "preserves all of the protections negotiated in 2023"; written-notice duty for training licences; term 2 May 2026 to 1 May 2030. SAG-AFTRA: four-year deal ratified with more than 90% of votes (AP, 5 June 2026).
- Vivalt et al.: NBER w32719 revised August 2026, with "a 4.2 percentage point decrease in labor market participation" and "1–2 hours/week"; QJE 141(4) 2675–2734 exists (Crossref).
- Canaries, August 2026: 19% gap; −11% and +10%; data to June 2026; "early, descriptive indicators".
- Fairlie & Wu, NBER w35796: no significant rise for recent graduates in summer 2026.
- Acemoglu April 2024 working paper: 19.9%, 23%, 27%, 0.57, 0.154, 0.71%, about 0.07 points a year, 7% for hard tasks ("half of the cost savings of their study"), 0.55%, GDP about 1.1% and 1.6–1.8%. The published version gives 0.66% and 0.53% (NBER abstract). Aghion & Bunel: 0.6 × 0.5 × 0.4 × 0.57 = 6.8%.
- Dell'Acqua et al., *Organization Science* 37(2) 2026; Cui et al., *Management Science* 72 (Nov 2026); Otis et al., *Management Science* 2026 (all confirmed via Crossref).
- Established findings: Noy & Zhang; Peng et al.; Brynjolfsson, Li & Raymond; METR 2025; ILO–NASK; IMF; Eloundou; Felten; Autor et al.; Acemoglu & Restrepo; Goldman Sachs; TIME/Sama; Fairwork; Bainbridge; Budzyń; Pew; Altman's American Equity Fund; MIT statement on the withdrawn preprint; Amodei's Axios forecast (paraphrased accurately).
- Cross-references to Section 14.4, Section 13.2, Chapter 3 and Chapter 5 are correct.

## Tally
Claims checked: 58 · confirmed: 55 · wrong: 0 · outdated: 0 · unclear/balance: 3 (S1–S3) · could not verify: 5 groups
