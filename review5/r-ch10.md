# Review 5: Chapter 10, Education, Health and Everyday Life

## Verdict
Ready to print. I found no MUST items. The chapter is careful about study design, its caveats are accurate, and the 2026 material I checked is correct: the FDA list counts reproduce exactly from the live list, HEPI 2026, Pew, NYC's moratorium, the OpenAI suits by state, the NY and California chatbot laws, the Garante's Character.AI fine, the Tribunal of Rome ruling, MASAI, Penda, AMIE and the updated Epic sepsis model. Two small SHOULD items improve precision.

## MUST change before printing
None.

## SHOULD change

### S1. AMIE feasibility study: 100 patients talked with AMIE, and 98 attended
- Where: textbook/chapters/ch10.md:135
- Text now: "There, 98 patients talked with AMIE before an urgent primary-care appointment while physicians supervised every conversation"
- Problem: UNCLEAR (minor). Google's account says 100 patients completed the pre-visit AI interaction and 98 attended the appointment. "Urgent" is used loosely: the visits were for "new, non-emergency, episodic complaints".
- Evidence: Google Research blog, "Exploring the feasibility of conversational diagnostic AI in a real-world clinical study" (2026), https://research.google/blog/exploring-the-feasibility-of-conversational-diagnostic-ai-in-a-real-world-clinical-study/ : "100 patients completed a pre-visit interaction with AMIE, and 98 attended their scheduled primary care appointment"; patients booked for "new, non-emergency, episodic complaints". (If the Lancet text analyses 98 throughout, keep 98 but say "98 patients who went on to attend".)
- Change to: "There, 100 patients talked with AMIE before a primary-care appointment for a new, non-emergency complaint (98 then attended), while physicians supervised every conversation"

### S2. Maryland tutor trial: the authors' main interpretation and engagement result are omitted
- Where: textbook/chapters/ch10.md:54
- Text now: "the authors suggest it may reflect how instructors' promotion of it changed students' other AI use."
- Problem: UNCLEAR / incomplete. That suggestion is in the paper (p. 3). But the abstract's headline finding is that participation in the learning-management system fell by 0.90 SD, and its headline interpretation is that the tutor "may displace engagement with existing learning activities". Readers get only the secondary explanation.
- Evidence: Liu et al., EdWorkingPaper ai26-1598 (2026), https://edworkingpapers.com/ai26-1598 : "These findings suggest that introducing an AI tutor may displace engagement with existing learning activities without improving academic performance". Body text: "it is possible that instructors introducing and encouraging use of the course-specific tutor may have changed GenAI use beyond the VSA itself."
- Change to: "Participation in the course's online learning system also fell, by 0.90 SD. The authors suggest that offering the tutor may have displaced engagement with existing course activities, or that instructors' promotion of it changed students' use of other AI tools."

## Could not verify
- De Simone et al. (World Bank working paper): 1,328 volunteers, attrition 334/671 and 235/657, $48/$9 per pupil, 72% attendance. I did not re-open the paper; the internal arithmetic is consistent (49.8% and 35.8%).
- CNN's "five such suits" (Character.AI and Google, January 2026). eWeek also says five, across Florida, Colorado, New York and Texas; Bloomberg Law gives no total.
- Penda Health trial details (103 clinical officers, 9,691 patients, 2.2% vs 2.0%, OR 0.77 [0.55–1.08]). The paper exists (Nature Medicine, 26 June 2026, "pragmatic, cluster-randomized trial"), and NPR's "23% decrease, not significant" matches the OR. I did not read the full text.
- Brodeur et al. (Lancet, Oct 2026): one hallucination and five supervisor additions are not in Google's blog; the paper itself was not read.
- Speech Accessibility Project counts (about 2,000 participants; 18–60% gains).

## Checked and confirmed
- Arithmetic: 0.3 SD gives the 62nd percentile and 0.63 SD the 74th; 98.5% specificity on 10,000 people gives 150; 0.37/0.15 ≈ 2.5 SD; Henkel 160/637 = 25%, 100/336 and 60/301; FDA table 1,553 + 40 + 21 = 1,614 (96.2/2.5/1.3%); radiology 1,230 (76%); 0.15% × 800m ≈ 1.2m; Bastani 32% × 0.83 ≈ 27%; Nigeria 0.31/0.16 ≈ 1.9 years.
- FDA AI-enabled device list (content current as of 4 Sept 2026; still the live version on 27 Nov 2026). I parsed it directly: 1,614 devices (K 1,553, DEN 40, P 21), radiology 1,230, 6 in 2015 and 335 in 2025, earliest 1995, latest 29 June 2026, "not a comprehensive resource", plan to tag foundation-model devices.
- Kestin et al. (Sci. Rep. 2025): 194 eligible students, 142/174 post-tests, regression 0.63 SD with ceiling (quantile 0.73–1.3), 49 vs 60 minutes, author overlap with the active-learning literature, tests by an uninvolved team member, autumn 2023.
- Liu et al. (EdWorkingPaper): University of Maryland, Fall 2025, 2,379 students and 30 instructors, −0.37 SD, about 15% take-up, larger losses for first-generation students.
- HEPI 2026: 1,054 students polled December 2025; 94%; 12% (3% in 2024); 65% assessment changed.
- NYC moratorium announced 2 Sept 2026 (2-K to grade 8, one year, companion chatbots banned in all grades, supervised high-school pilots).
- Eleven state suits against OpenAI: Florida (June) + eight in October (AR, AZ, ID, MT filed; IA, KS, NE, WV announced) + Texas (23 Oct) + Oregon (17 Nov, Multnomah County, UTPA). California's suit of 16 Nov concerns cybersecurity and agents, consistent with Section 11.6.
- NY Art. 48 signed 28 Oct 2026, effective 1 Jan 2027, $25,000 per violation, bars claiming to be human; California SB 1119/SB 867 chaptered 10 Sept 2026.
- Garante: Character Technologies fined €158,000 (decision 3 July, announced 9 July 2026), age checks, minors' profiles private by default. Tribunal of Rome judgment n. 4785 of 18 March 2026 annulled the €15m OpenAI fine on competence (one-stop shop) without ruling on the merits; consistent with ch13.md:274.
- MASAI final (Gommers et al., Lancet, Jan 2026) and interim figures; Epic sepsis 2021 figures and Wong et al. 2026 (JAMA Netw Open: 227,091 encounters, 4 systems, AUROC 0.82–0.92, PPV 0.13–0.26).
- Folk & Dunn (Psychol. Sci., 2026), Zhang et al. (Nat. Hum. Behav., Aug 2026), González Peñuela et al. (CHI 2026) and Bean et al. (Nat. Med.) DOIs resolve. Turkle, *Artificial Intimacy* (Little, Brown, 29 Sept 2026) exists.
- Older figures consistent with the literature: VanLehn 0.79/0.76; Kulik & Fletcher 0.66; Kraft 747/0.10; Cheung & Slavin 645/12; Liu 2019 (Lancet Digit Health); Plana 41/294; Han 86/81%/43%; Goh 2024 and 2025; Vaccaro −0.23/0.64; AMIE 159/30 of 32/25 of 26; McDuff 59.1/33.6/51.7/44.4; Liang 61% and 12%; Therabot 210; OpenAI 0.15% and 91% vs 77%; Carlini 2021; Willett 62 wpm; Card 97.5%/248 h.
- Cross-references: Section 2.8 (AUC), Chapter 8 endoscopy (ch08.md:251, consistent), Section 11.5 automation bias, Section 11.6 California suit, Section 13.6, and Table 13.1 (2 Dec 2027 for Annex III and 2 Aug 2028 for Annex I, consistent with ch13).

## Tally
Claims checked: 86 · confirmed: 84 · wrong: 0 · outdated: 0 · imprecise or incomplete: 2 (S1, S2) · could not verify: 5 (some grouped)
