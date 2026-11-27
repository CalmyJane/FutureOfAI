# Review: Chapter 8, Work, Productivity and the Economy

## Verdict
Ready to print. The chapter is careful, balanced and correctly hedged. Every worked example recomputes, and the late-2026 updates I checked match their sources: BLS productivity for Q3 2026, the Challenger October 2026 report, the BLS AI-exposure categories, the "Super Intelligence" executive order, the WGA and SAG-AFTRA 2026 contracts, the Digital Omnibus dates and METR's 2026 update. I found nothing wrong that blocks printing. Three items should be clarified.

## MUST change before printing
None.

## SHOULD change

### S1. "17% lower" is 17 percentage points
- Where: textbook/chapters/ch08.md:253 (also Table 8.3, row Shen & Tamkin, "quiz score −17%")
- Text now: "on a quiz afterwards, taken without AI, it scored 17% lower, about two grade points"
- Problem: UNCLEAR. The AI group averaged 50% and the hand-coding group 67%. The gap is 17 percentage points, which is about 25% lower in relative terms. Anthropic calls it "nearly two letter grades", not "grade points".
- Evidence: Anthropic, 29 Jan 2026, https://www.anthropic.com/research/AI-assistance-coding-skills : "the AI group averaged 50% on the quiz, compared to 67% in the hand-coding group—or the equivalent of nearly two letter grades". arXiv:2601.20245 reports "a reduction in the evaluation score by 17% or two grade levels".
- Change to: "on a quiz afterwards, taken without AI, it scored 17 percentage points lower (50% against 67%), nearly two letter grades". In Table 8.3, change "quiz score −17%" to "quiz score −17 points".

### S2. Challenger: say which period the 44% fall covers
- Where: textbook/chapters/ch08.md:156
- Text now: "Announced cuts overall were 44% lower than a year earlier, when federal government cuts had been exceptional"
- Problem: UNCLEAR. The 44% is the year-to-date figure: 617,189 cuts through October against the same period of 2025. October alone was 71% lower (43,994 against 153,074). The sentence follows "in October itself", so readers will apply 44% to October.
- Evidence: HCAMag on the Challenger report, Nov 2026, https://www.hcamag.com/us/specialization/transformation/ai-blamed-for-121401-job-cuts-but-the-labor-data-isnt-buying-it/594129 : total cuts are "down 44 percent from the same period in 2025". CPA Practice Advisor: "Companies last month announced 43,994 job cuts", down 71%.
- Change to: "Announced cuts in the first ten months were 44% lower than in the same period a year earlier, when federal government cuts had been exceptional"

### S3. Check the guaranteed-income figures against the QJE text
- Where: textbook/chapters/ch08.md:277
- Text now: "The larger payments reduced labour-market participation by 4.2 percentage points and working hours by one to two hours a week."
- Problem: UNSUPPORTED (could not confirm). The latest NBER revision (w32719, January 2026) gives "a 3.9 percentage point decrease in labor market participation". Earlier versions gave 2.0. The cited QJE article (141(4), doi 10.1093/qje/qjag042) exists but was paywalled to me. Use the QJE figure if it really is 4.2; otherwise change to 3.9.
- Evidence: https://www.nber.org/papers/w32719 (abstract, rev. Jan 2026): "a 3.9 percentage point decrease in labor market participation … 1-2 hours/week".
- Change to (if the QJE matches the NBER revision): "reduced labour-market participation by 3.9 percentage points and working hours by one to two hours a week."

## Could not verify
- Brynjolfsson, Li & Raymond: "lowest-skill fifth +36%" (line 96 and case box). The QJE abstract gives no quintile figure, and the 2023 working paper says 34% for novice and low-skilled workers. Check against the QJE text.
- Humlum & Vestergaard (March 2026 revision): "rule out effects … larger than 2%". I could not reach the revised PDF. The earlier version was worded more tightly.
- Census BTOS 25.0% (19 Oct–1 Nov 2026); Fed Beige Book (5 of 12 districts); the ADP "canaries" August 2026 version (−19%); PwC 2026 Barometer; Fairlie et al. 2026; journal status of Dell'Acqua (*Organization Science* 2026), Cui (*Management Science* 2026) and Otis (*Management Science* 2026).
- Eloundou Table 8.1 shares (15/14, 31/35, 47/56).

## Checked and confirmed
- Arithmetic:
  - Acemoglu: 0.199 × 0.23 ≈ 4.6%; (40 + 14)/2 = 27%; 0.27 × 0.57 ≈ 15.4%; 0.046 × 0.154 ≈ 0.71%; working-paper figures 0.71%/0.55%, published 0.66%/0.53%
  - Aghion–Bunel: 0.6 × 0.5 × 0.4 × 0.57 ≈ 6.8% → 0.68 pp a year
  - Elo, Domar and other side calculations consistent
- METR: original study (16 developers, 246 issues, +19%, CI +2 to +39%, forecasts 24% / 38–39%, felt ~20% faster); 2026 update (57 developers, 800+ tasks; −18% with CI −38 to +9; −4% with CI −15 to +9; 30–50% withheld tasks; "only very weak evidence"; started August 2025).
- Other experiments: Noy & Zhang (40%/18%); Peng (95 programmers, 55.8%, CI 21–89%); Shen & Tamkin (52 participants, six patterns, three engaged).
- Macro figures:
  - Penn Wharton: 1.5% by 2035, 3.7% by 2075, 0.2 pp in 2032
  - Goldman Sachs: 7% of GDP, 1.5 pp a year
  - BLS Q3 2026: productivity 3.6% annual rate; 2.1% over the year
- Labour-market figures:
  - EIG: 0.30 vs 0.94 pp
  - Challenger: 121,401 AI cuts year to date; 1,265 in October; "market/economic conditions" now the leading reason
  - BLS exposure categories: 831 occupations; three theoretical plus Anthropic and Microsoft usage data; quotes on "Exposure does not imply job loss" and automation vs augmentation verbatim
- Executive Order "Inaugurating the Era of Super Intelligence" (29 Sep 2026).
- Contracts and law:
  - WGA 2026 MBA: 2 May 2026–1 May 2030; "preserves all of the protections negotiated in 2023"; training-licence notice
  - SAG-AFTRA: four-year deal ratified June 2026 with 91.4%; "significant additional value"
  - Digital Omnibus: Annex III deferred to 2 Dec 2027, in force 27 Jul 2026 (consistent with Ch. 13)
- Statements and reports: Amodei to Axios (half of entry-level jobs, 10–20%); TIME/Sama ($1.32–2, $12.50, ended Feb 2022); WGA strike of 148 days; ILO–NASK and IMF exposure shares; Altman's American Equity Fund (2.5%).
- Cross-references to Ch. 3, 5, 10, 12, 13 and 14.4 point to the right chapters.

## Tally
Claims checked: 58 · confirmed: 51 · wrong: 0 · outdated: 0 · unclear: 2 (S1, S2) · unsupported/unconfirmed: 1 (S3) · could not verify: 4 groups
