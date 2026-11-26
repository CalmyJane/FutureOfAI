# Chapter 8 review: Work, Productivity and the Economy

## Verdict
Ready after two small fixes. This is a balanced and carefully hedged chapter. I checked most of the study figures against the papers, including the latest revisions (Vivalt Aug 2026, Humlum Mar 2026, ADP Aug 2026, Brynjolfsson v2, Aghion & Bunel, Shen & Tamkin, Eloundou), and they are right. The Acemoglu and Aghion–Bunel arithmetic recomputes exactly. Two items are wrong. One is a percent/percentage-point error for Dell'Acqua et al., which appears twice. The other is a figure caption that says METR gave no confidence level when it did. Tone towards named people and firms (Amodei, Altman, Sama/OpenAI, MIT) is fair and attributed.

## MUST change before printing

### M1. Dell'Acqua et al.: 19 percentage points, not 19%
- Where: textbook/chapters/ch08.md:110 and ch08.md:97 (Table 8.3)
- Text now (110): "consultants using AI were 19% less likely than the control group to reach the correct answer"
- Text now (97): "outside: 19% less likely to be correct"
- Problem: VERIFIED WRONG. The paper reports a drop of 19 *percentage points* (control 84.5% correct against about 60–70% with AI). In relative terms that is a fall of roughly 23%, not 19%.
- Evidence: Dell'Acqua et al., working paper (MIT Sloan copy of SSRN 4573321, Sept 2023): "consultants using AI were 19 percentage points less likely to produce correct solutions compared to those without AI"; and "the AI conditions scored at 60% and 70% (for an average decrease of 19 percentage points)".
- Change to (110): "consultants using AI were 19 percentage points less likely than the control group to reach the correct answer"; (97): "outside: 19 percentage points less likely to be correct"

### M2. Figure 8.2 caption: METR follow-up intervals are 95%
- Where: textbook/chapters/ch08.md:144
- Text now: "Bars show intervals where the source reports them: 95% for Peng et al. and the first METR trial, level not stated for the METR follow-up."
- Problem: VERIFIED WRONG. METR states 95% confidence intervals for both follow-up estimates.
- Evidence: https://metr.org/blog/2026-02-24-uplift-update/ (24 Feb 2026): returning developers −18%, "95% CI −38% to +9%"; new developers −4%, CI −15% to +9%.
- Change to: "Bars show 95% intervals where the source reports them (Peng et al. and both METR studies)." Check that the bars drawn in fig-08-02 match −38% to +9% and −15% to +9%.

## SHOULD change

### S1. Table 8.3: add the follow-up's intervals
- Where: textbook/chapters/ch08.md:100
- Text now: "Time −18% (returning, n = 10); −4% (new, n = 47); neither significant"
- Problem: UNCLEAR. The other rows give CIs where they exist. Adding these makes "neither significant" checkable.
- Change to: "Time −18% (returning, n = 10; 95% CI −38% to +9%); −4% (new, n = 47; −15% to +9%); neither significant"

### S2. Eloundou headline: "at least half", not "more than half"
- Where: textbook/chapters/ch08.md:25
- Text now: "about 19% in occupations where more than half are exposed"
- Problem: MISQUOTED (minor). The paper says "at least 50%".
- Evidence: arXiv 2303.10130 abstract: "approximately 19% of workers may see at least 50% of their tasks impacted".
- Change to: "about 19% in occupations where at least half are exposed"

## Could not verify
- Yale Budget Lab quotations ("no sign of being related to changes in employment or unemployment"; "better data is needed"). The page did not render.
- Bick et al. 62% of adults (May 2026); Census BTOS 25.0% and the 18–22% range; Bonney et al. supplement figures; Anthropic Economic Index Jan/Jun 2026 shares and the 1.8 / 1.0–1.2 pp estimates.
- Fairwork 2023 (15 platforms; none above 5; four at zero); Hosseini Maasoum & Lichtinger; PwC Barometer "seven times"; Fairlie NBER w35796; OECD/JDN Cormann statement; Beige Book "five of twelve districts"; WGA 2026 MBA term and SAG-AFTRA >90% ratification.

## Checked and confirmed
- Becker et al.: 16 developers, 246 issues, +19% (CI +2% to +39%), 24% / 38–39% expected, ~20% believed. METR follow-up: 57 developers, 800+ tasks, started Aug 2025, 30–50% withheld tasks, "only very weak evidence".
- Vivalt et al. (NBER w32719, revised Aug 2026): "a 4.2 percentage point decrease in labor market participation"; 1–2 hours a week; 1,000 × $1,000 and 2,000 × $50.
- Humlum & Vestergaard (rev. Mar 2026): "ruling out effects larger than 2% two years after the launch of ChatGPT".
- Brynjolfsson, Li & Raymond (v2): 5,172 agents, +15%, lowest-skill quintile +36%. The 14% figure comes from the 2023 version (Aghion & Bunel cite it as 14% rising to ~25%).
- Aghion & Bunel: 60% exposed (Pizzinelli et al.), 50% profitable (22% annual cost decline), 40% saving, 0.57 labour share, 0.68 pp, range 0.07–1.24 pp.
- Shen & Tamkin: 52 participants, quiz −17% "or 2 grade points", six patterns of which three preserve learning.
- Eloundou et al.: α/β/ζ task shares 0.15/0.31/0.47 (human) and 0.14/0.35/0.56 (GPT-4); 80% / 19% / 3% / 49%.
- Canaries (Aug 2026): 19% gap, −11% vs +10%, "over 26 million" workers, 3.5–5 million panel, "early, descriptive indicators".
- FRED blog Q2 2026: 39.2%, 6.3%, 2.2%. BLS Q3 2026: 3.6% annual rate, 2.1% y/y, 2.2% since Q4 2019, 1.5% for 2007–19, 2.2% since 1947.
- Challenger Oct 2026: AI 121,401 YTD (~20%), 1,265 in October; Market/Economic Conditions now lead; cuts −44%.
- EO 14434 (29 Sept 2026) "Super Intelligence" terminology, which is consistent with ch12/ch13.
- Arithmetic: 0.199×0.23 = 4.58%; (40+14)/2 = 27%; 0.27×0.57 = 15.4%; 0.046×0.154 = 0.71%; Aghion 0.6×0.5×0.4×0.57 = 6.84% (10 yrs); (55.8+40+25)/3 = 40.3%.
- Cross-references: Section 13.2 (Digital Omnibus, 2 Dec 2027), Section 14.4 (Scenarios), Chapter 10 (learning), Chapter 5 agents; dates match ch13. All bib keys resolve.

## Tally
Claims checked: 74 / confirmed: 56 / wrong: 2 (M1, M2) / outdated: 0 / imprecise: 2 (S1, S2); 14 could not be verified.
