# Review 9: Chapter 8 (Work, Productivity and the Economy)

## Verdict
Ready to print. The chapter is balanced and careful about what each study can and cannot show, and its 2026 updates are current to November 2026: BLS productivity for Q3 2026, the Challenger October report, the ADP "Canaries" August 2026 revision and the BLS exposure categories. The worked arithmetic (Acemoglu, Aghion & Bunel, Table 8.4) recomputes exactly. I found nothing wrong, misquoted or legally risky. The two SHOULD items concern how Anthropic's own research is presented.

**Balance between companies.** The chapter mostly handles this well. Amodei's forecast of 10–20% unemployment is set out with the note that Anthropic "sells AI tools to businesses" and then tested against evidence that does not yet support it (l.148). Anthropic's productivity estimate is labelled company data and not peer-reviewed (l.217). The Anthropic Economic Index's automation/augmentation labels are explicitly described as model-assigned conversation-style labels (l.73), and the skew in Anthropic's June 2026 survey is pointed out. The TIME/Sama account of OpenAI's labelling contractor includes Sama's responses. Anthropic material is, however, cited more often than other companies' (Economic Index twice, Massenkoff, Shen & Tamkin, the productivity estimate), and in two places the wording favours it slightly; see S1 and S2. I found no unfairness towards OpenAI, Microsoft or Google.

## MUST change before printing
None.

## SHOULD change

### S1. An Anthropic preprint is called "the cleanest test so far"
- Where: textbook/chapters/ch08.md:253
- Text now: "For knowledge work, the cleanest test so far is a small randomised experiment reported in a preprint by Anthropic researchers [@shen2026how]."
- Problem: UNSUPPORTED / balance. The study is a single unreviewed company preprint with 52 participants in one session (Table 8.3's own caveat). Ranking it as "the cleanest test so far" is an editorial judgement that favours the author-model's own developer. The finding is unflattering to AI, so this is not self-serving, but the superlative is not needed and cannot be backed up.
- Evidence: Table 8.3, l.102 ("Shen & Tamkin (2026, preprint) | RCT | 52 Python programmers … | Crowd workers; one session").
- Change to: "For knowledge work, one direct test is a small randomised experiment reported in a preprint, not peer-reviewed, by Anthropic researchers [@shen2026how]."

### S2. "Privacy-preserving" is the company's own description
- Where: textbook/chapters/ch08.md:71
- Text now: "Anthropic, the developer of the Claude models, publishes an "Economic Index" based on privacy-preserving analysis of conversations."
- Problem: UNCLEAR / balance. The book states as fact a property that Anthropic claims for its own system (Clio). The same paragraph describes OpenAI's and Microsoft's datasets neutrally.
- Change to: "Anthropic, the developer of the Claude models, publishes an "Economic Index" based on what it describes as privacy-preserving analysis of conversations."

## Could not verify
- Census BTOS: "between about 18% and 21% … in the first half of 2026" and "25.0% in the two weeks to 1 November 2026", and the rise in "do not know" answers from ~10% to ~13%. The Census Bureau's own May 2026 story gives "between 17% and 20%" for 14 December 2025 to 3 May 2026. A rounding difference or a June value could explain the gap, but the author should check it against the BTOS data page. The "Super Intelligence" rewording from 19 October 2026 (EO 14434) is confirmed by Simon Willison's post of 2 November 2026, which quotes the Census instrument.
- Brynjolfsson, Li & Raymond, QJE version: "lowest-skill fifth +36%" (the working paper said 34% for novice/low-skilled workers). I could not reach the QJE full text.
- Humlum & Vestergaard, March 2026 revision: the "2%" bound and the "12 percentage points" for switchers.
- METR follow-up figures, Otis et al. (published version), Dell'Acqua et al. and Cui et al. as published in 2026, the OECD/Cormann remark via JDN, the October 2026 Beige Book count (five of twelve districts), Fairlie (2026), Rodgers (2026), the Fairwork 2023 scores, and the SAG-AFTRA ratification share (>90%).
- The WGA 2026 MBA dates (2 May 2026 – 1 May 2030) and the "preserves all of the protections" wording. A four-year deal reached on 4 April 2026 is confirmed (Hollywood Reporter, NPR); the exact phrasing is not.

## Checked and confirmed
- Arithmetic: 0.199×0.23 = 4.58%; 0.27×0.57 = 15.4%; 0.046×0.154 = 0.71%; Aghion & Bunel 0.60×0.50×0.40×0.57 = 6.84% → 0.68 pp/yr; the average of 55.8, 40 and 25 = 40.3%; the "tenfold" gap.
- Aghion & Bunel inputs (60% from Pizzinelli et al.; 50% from 22% annual compute-cost decline; customer support ~25%; labour share 0.57; range 0.07–1.24 pp; electricity 1.3 pp and digital 0.8 pp) all match the note.
- Eloundou et al. Table 3 task-level means (human α/β/ζ 0.15/0.31/0.47; GPT-4 0.14/0.35/0.56), 80%/19%, "only 3%" and "up to 49%".
- METR 2025 (16 developers, 246 issues, −24% expected, +19% actual, ~20% believed); Noy & Zhang (−40%, +18%); Peng (55.8%, 21–89%); Cui (26.08%, SE 10.3%); Dell'Acqua (12.2%, 25.1%, 19 pp).
- BLS exposure categories (27 August 2026; 831 occupations; three theoretical indices including Felten and Eloundou; usage data from Anthropic and Microsoft; quote "Exposure does not imply job loss…" verified; does not distinguish automation from augmentation).
- ILO–NASK: one in four exposed; 34% high-income; 9.6% vs 3.5%; quote "transformation, not replacement, is the most likely outcome" verified on ilo.org.
- Challenger October 2026: AI ~121,400 cuts YTD (~20%), 1,265 in October, market/economic conditions now top reason, total −44% y/y.
- ADP "Canaries" August 2026 revision: data to June 2026, 19% gap, works through hiring, concentrated where AI substitutes, weakens with education controls, "early, descriptive indicators".
- BLS productivity (5 November 2026): Q3 +3.6%, +2.1% y/y, 2.2% since Q4 2019, 1.5% for 2007–19, "the same as the long-term rate of 2.2 percent since the first quarter of 1947".
- Vivalt et al. NBER w32719 revised August 2026: −4.2 pp participation, 1–2 hours/week, leisure largest increase, no effect on job quality.
- Amodei/Axios May 2025 claim; Pew (52%/36%); TIME/Sama details ($1.32–$2, $12.50, February 2022, eight months early); MIT statement quote; WGA 148-day strike; Goldman Sachs (7%, 1.5 pp); Penn Wharton (1.5% by 2035, 3.7% by 2075, 0.2 pp in 2032); Altman's American Equity Fund (2.5%); Budzyń (28.4% → 22.4%, 1,443 procedures).
- Cross-references to Sections 13.2 and 14.4 and Chapters 3, 5 and 10 resolve correctly. The AI Act timetable (2 December 2027) matches ch13.

## Tally
Claims checked: ~70 · confirmed: ~58 · wrong: 0 · outdated: 0 · balance/wording: 2 · not verified: ~12
