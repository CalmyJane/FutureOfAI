# Review 4: Chapter 10 (Education, Health and Everyday Life)

## Verdict
Ready to print after one small wording fix. The chapter is balanced. It states the evidence's limits clearly (working papers, vendor funding, attrition, intention-to-treat estimates), and it is fair to the named companies. All the 2026 facts I checked are correct: MASAI's final results, AMIE in *The Lancet*, the Penda Health trial, the Maryland tutoring paper, the NYC moratorium, California's SB 1119 and SB 867, New York's October 2026 law, the Garante's fine on Character.AI, the Oregon suit, Turkle's book, HEPI 2026 and Pew's teen survey. All the arithmetic checks out. I found no MUST items.

## MUST change before printing
None.

## SHOULD change

### S1. "Eleven had sued OpenAI … most recently Oregon" ignores California's 16 November suit, which Chapter 11 reports
- Where: textbook/chapters/ch10.md:163
- Text now: "By mid-November 2026 eleven had sued OpenAI, most recently Oregon on 17 November, alleging that ChatGPT harmed children and that the company misled the public about its safety"
- Problem: INCONSISTENT / UNCLEAR. Eleven states have sued over harms to children: Florida in June, eight states on 14 Oct, Texas on 23 Oct and Oregon on 17 Nov. But California also sued OpenAI on 16 Nov 2026, over agent-security failures, and ch11.md:227 reports that suit. Read literally, "eleven had sued OpenAI" undercounts (twelve states have sued). The sentence becomes accurate once it is limited to child-safety suits.
- Evidence: OPB, 17 Nov 2026, https://www.opb.org/article/2026/11/17/oregon-ag-sues-openai-claims-company-knowingly-endangers-teens/: "Eight U.S. states sued OpenAI in October, each claiming the technology is dangerously influential on teens." California DOJ, 16 Nov 2026, https://oag.ca.gov/node/632941 ("Attorney General Bonta Sues OpenAI Over Cybersecurity Incidents"). Florida's suit (June 2026) and Texas's (23 Oct 2026) are already cited in the chapter.
- Change to: "By mid-November 2026 eleven states had sued OpenAI over harms to children, most recently Oregon on 17 November, alleging that ChatGPT harmed children and that the company misled the public about its safety (California's separate suit of 16 November concerns AI agents; see Section 11.6)"

## Could not verify
- ch10.md:36. The Kestin et al. effect of 0.63 SD and the 142/174 counts. I did not reopen the paper; the design details match published descriptions.
- ch10.md:23. The De Simone et al. cost figures ($48 per pupil, $9 at the margin) and the implied gain of 0.16 SD a year. I did not reopen the working paper. 0.31/0.16 ≈ 1.9 years, which is consistent with "1.5 to 2 years".
- ch10.md:170, Table 10.3. SB 1119's civil penalty of "up to $15,000 per child" is taken from the law-firm summaries the chapter cites. The signature date (10 Sept 2026) and the July 2027 start are confirmed.

## Checked and confirmed
- MASAI final results (Gommers et al., *Lancet* 2026;407:505–514): 105,934 randomised; 1.55 vs 1.76 per 1,000; ratio 0.88 (0.65–1.18); sensitivity 80.5% vs 73.8%; specificity 98.5% in both arms; fewer invasive interval cancers (75 vs 89).
- AMIE feasibility study (Brodeur et al., *Lancet*, 8 Oct 2026): 98 patients completed both the AMIE chat and the visit; no safety stops; one hallucination; supervisors added information in five interactions; funded by Alphabet. The preprint's "100" counts AMIE chats only, so the chapter's 98 is the correct figure for the published paper.
- Penda Health trial (*Nature Medicine* 2026): 16 clinics; 103 clinical officers; 9,691 patients; 2.2% vs 2.0%; adjusted OR 0.77 (0.55–1.08).
- Liu et al. (EdWorkingPaper ai26-1598): University of Maryland, Fall 2025; 2,379 students; 30 instructors; −0.37 SD; larger losses for first-generation students; about 15% take-up. 0.37/0.15 ≈ 2.5 SD.
- NYC moratorium (2 Sept 2026): one year, student-facing generative AI through grade 8, supervised high-school pilots, companion chatbots banned in all grades.
- California SB 1119 and SB 867 signed 10 Sept 2026; SB 867 runs to 1 Jan 2031 and covers toys for children under 16.
- New York's law on "unsafe AI companion features" signed 28 Oct 2026, in force 1 Jan 2027, with penalties up to $25,000.
- Garante: €158,000 fine on Character Technologies (decision of 3 July 2026, announced 9 July); orders on age checks and private profiles for minors.
- Oregon suit, 17 Nov 2026; eight-state suits, 14 Oct 2026; Florida's suit, June 2026.
- Character.AI and Google settlements, Jan 2026, undisclosed terms.
- Turkle, *Artificial Intimacy: Who We Become When We Talk to Machines* (Little, Brown, 29 Sept 2026).
- HEPI 2026: 1,054 students; December 2025; 94%; 3% → 12% including AI-generated text.
- Pew teens (24 Feb 2026): 1,458 teens; "just over half" for schoolwork; 12% for emotional support.
- FDA list: most recent final decision 29 June 2026, consistent with "the most recent decided in June 2026"; FDA "will explore methods to identify and tag medical devices that incorporate foundation models". Table 10.2 sums to 1,614, and the shares are correct (96.2/2.5/1.3%). Radiology is 1,230/1,614 = 76%. 6 → 335 is more than fiftyfold.
- Arithmetic: 0.3 SD ≈ 62nd percentile and 0.63 SD ≈ 74th; 150 false alarms at 98.5% specificity; attrition of 334/671 ≈ 50% and 235/657 ≈ 36%; 0.15% × 800m ≈ 1.2m.
- Cross-references: Chapter 8 (Budzyń endoscopist study, ch08.md:251); Section 13.6 (EDPB opinion; Garante fine annulled by the Tribunal of Rome, consistent with ch13.md:274); Table 13.1 dates (2 Dec 2027 Annex III; 2 Aug 2028 Annex I); Chapter 11 (automation bias); Section 2.8 (AUC).

## Tally
Claims checked: 52 · confirmed: 51 · wrong: 0 · outdated: 0 · inconsistent: 1
