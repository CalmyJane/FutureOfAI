# Review 6: Chapter 8 (Work, Productivity and the Economy)

## Verdict
Ready to print. One small data-range correction is advisable. The chapter is well organised around the exposure → adoption → experiments → jobs → macro chain. It is even-handed, and it labels preprints, company data and causal status consistently. Every 2026 figure I could reach in a primary source matches it exactly, including:
- BLS productivity for Q3 2026 and BLS exposure categories;
- the Census BTOS file;
- the Challenger October report and the Beige Book;
- the ADP "Canaries" paper (August 2026);
- the Humlum–Vestergaard revision (March 2026);
- the METR follow-up;
- the Vivalt et al. revision (August 2026);
- Fairlie & Wu, and the St. Louis Fed posts;
- the WGA 2026 MBA and the SAG-AFTRA vote;
- the "Super Intelligence" executive order.

All the worked arithmetic recomputes correctly. Amodei's Axios prediction is reported fairly, with his company's commercial interest noted.

## MUST change before printing
None.

## SHOULD change

### S1. BTOS range for the first half of 2026 is slightly high
- Where: textbook/chapters/ch08.md:65
- Text now: "Between about 18% and 22% of firms reported use in the first half of 2026, and 25.0% in the two weeks to 1 November 2026 [@census2026business]."
- Problem: INCONSISTENT with the cited data file. The 13 BTOS periods of January–June 2026 (202601–202613, question 7, "Yes") run from 17.5% to 20.6%. The first period above 21% is 202614, which starts in July. The 25.0% figure for 202623 is correct.
- Evidence: https://www.census.gov/hfp/btos/downloads/National.xlsx (published 19 Nov 2026, downloaded 27 Nov 2026). Question 7 "Yes", periods 202601–202613: 17.7, 18.2, 18.9, 17.5, 18.2, 18.9, 19.1, 19.8, 19.8, 19.5, 20.6, 20.6, 20.6%. Period 202623: 25.0%.
- Change to: "Between about 18% and 21% of firms reported use in the first half of 2026, and 25.0% in the two weeks to 1 November 2026 [@census2026business]."

## Could not verify
- Brynjolfsson, Li & Raymond (QJE): "lowest-skill fifth +36%" (ch08.md:96 and :119). The QJE abstract gives only the 15% average; the NBER version gave 34% for "novice and low-skilled workers". The QJE body is paywalled. Worth one check against the published table.
- Eloundou et al. task shares in Table 8.1 (15/31/47% for humans, 14/35/56% for GPT-4, with core tasks weighted double). I did not re-derive them from the preprint's tables.
- The Anthropic Economic Index figures: January 2026 (52/45, about three-quarters API automation, 1.8 pp and 1.0–1.2 pp) and June 2026 (9,700 users; 30% against 4%).
- Bonney et al. BTOS supplement, PwC 2026 Barometer ("seven times"), Fairwork 2023 ("four scored zero"), the SHOOT/SAG-AFTRA "significant additional value" quote, and Journal du Net on Cormann.
- The *Organization Science* (Dell'Acqua) and *Management Science* (Cui) publication details.

## Checked and confirmed
- Arithmetic:
  - 0.199 × 0.23 ≈ 4.6%
  - (40 + 14)/2 = 27%
  - 0.27 × 0.57 ≈ 15.4%
  - 0.046 × 0.154 ≈ 0.71%, about 0.07 pp a year
  - Aghion–Bunel 0.6 × 0.5 × 0.4 × 0.57 ≈ 6.8%, about 0.68 pp a year
  - 7% = half of 14%
  - Shen 67 − 50 = 17 points
  - Peng and METR ranges
- BLS release of 5 Nov 2026: 3.6% annualised in Q3, 2.1% over four quarters, 2.2% since 2019Q4, 1.5% for 2007–19, 2.2% since 1947.
- BLS AI exposure categories (27 Aug 2026):
  - 831 occupations;
  - three theoretical sources (AIOE, Eloundou, Eisfeldt) plus Anthropic and Microsoft usage;
  - "Exposure does not imply job loss…";
  - the categories do not distinguish automation from augmentation.
- Census BTOS: 25.0% for 19 Oct–1 Nov 2026. The question wording now reads "Super Intelligence or SI (formerly referred to as Artificial Intelligence or AI)", which confirms the book's remark. The EO "Inaugurating the Era of Super Intelligence" was signed on 29 Sep 2026.
- Challenger, October 2026: AI cited for 121,401 cuts YTD (about 20%), 1,265 in October; Market/Economic Conditions now leads; YTD cuts down 44%.
- Beige Book, October 2026: five Districts, "reduced staffing levels (through attrition), delayed hiring, or anticipated less job creation… after increasing productivity by investing in AI".
- Brynjolfsson, Chandar & Chen, August 2026:
  - data to June 2026;
  - −11% against +10%, and the 19% gap (15% at the July 2025 vintage);
  - 26 million workers, and a panel of 3.5–5 million;
  - "early, descriptive indicators".
- Humlum & Vestergaard, March 2026:
  - 25,000 workers and 7,000 workplaces;
  - 40%/7% against 93%/28%/19%, and 8%/17% new tasks;
  - effects above 2% ruled out;
  - switchers +12 pp.
- METR, 24 Feb 2026: 57 developers, 800+ tasks, August 2025 start; −18% (−38 to +9) and −4% (−15 to +9); 30–50% withheld tasks; "only very weak evidence".
- The original METR trial figures (16 developers, 246 issues, 24%, 38–39%, +19%, about 20%).
- Bick et al.: 62% in May 2026; the Q2 2026 tracker at 39.2%, 6.3% and 2.2%; "up to 1.3%"; the reweighting.
- Fairlie & Wu (NBER w35796) and Rodgers & Kassens (about a third; "not whether firms are using AI to automate jobs or to screen applicants").
- Vivalt et al. (NBER w32719, revised August 2026): "4.2 percentage point decrease", "1-2 hours/week".
- Otis et al. (*Management Science*, July 2026): over 0.20 SD, "nearly 10% worse", "over 15%".
- Hosseini & Lichtinger, May 2026 version: 65 million workers and more than 280,000 firms; senior employment largely unchanged; driven by hiring.
- PWBM: 40% of labour income, 1.5% by 2035, 3.7% by 2075, 0.2 pp peak in 2032.
- WGA 2026 MBA: term 2 May 2026–1 May 2030; "preserves all of the protections negotiated in 2023"; training-licence notice.
- SAG-AFTRA: four-year deal, over 90% approval (AP, 5 June 2026).
- ILO–NASK: one in four; 9.6% against 3.5%; "transformation, not replacement, is the most likely outcome" (ILO announcement).
- Consistency with ch13 on the Digital Omnibus dates (2 Dec 2027 for Annex III).

Tally: about 85 claims checked; about 75 confirmed; 0 wrong; 0 outdated; 1 imprecise (S1); the rest could not be verified.
