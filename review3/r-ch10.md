# Third review: Chapter 10 — Education, Health and Everyday Life

## Verdict
Ready after the MUST fix below. The chapter is unusually careful. I re-derived the contested numbers from the primary sources: the Rori sample (477 analysed of 637 at baseline), Nigerian attrition, Bastani's effects, Kestin's sample sizes, the MASAI detection and workload figures, the FDA device counts, Epic, AMIE, Penda and the scribe trial. Every one matches. One statement was already wrong at the book's own cutoff: New York's stricter companion-chatbot bill is described as unsigned "by late October", but the Governor signed it on 28 October 2026. That sentence and Table 10.3 must change. The other items below are for currency and precision: a new state lawsuit (Oregon, 17 November), an unsupported "first", a quotation that has disappeared from the FDA's live page, and some small overstatements.

## MUST change before printing

### M1. New York's AI-companion bill for minors was signed on 28 October 2026
- Where: textbook/chapters/ch10.md:165, and Table 10.3 (lines 167–178)
- Text now: "A stricter New York bill barring AI companions from features deemed unsafe for minors passed both houses in June 2026 but had not been signed by late October [@nyassembly2026a10379]."
- Problem: VERIFIED WRONG (already at the book's stated cutoff of end October 2026) and OUTDATED. Governor Hochul signed S9051-B/A10379-C on 28 October 2026 as Chapter 368 of the Laws of 2026. It adds a new Article 48 to the General Business Law, in force from 1 January 2027. The cited bill page itself now records the signature.
- Evidence:
  - NY Assembly bill record (the URL in the bib entry), action history: "10/28/2026 DELIVERED TO GOVERNOR 10/28/2026 SIGNED CHAP.368 10/28/2026 APPROVAL MEMO.6" (https://nyassembly.gov/leg/?default_fld=&leg_video=&bn=A10379&term=2025&Summary=Y&Actions=Y).
  - Holland & Knight, "New York Enacts AI Chatbot Safeguards for Minors" (November 2026), https://www.hklaw.com/en/insights/publications/2026/11/new-york-enacts-ai-chatbot-safeguards-for-minors. It says: signed 28 October 2026; effective 1 January 2027; new Article 48 GBL. Operators "may not provide 'unsafe AI companion features' to minors", including claiming to be human, encouraging secrecy or isolation, and sexually explicit content. Age assurance is required. The Attorney General enforces it, with civil penalties of up to $25,000 per violation and no private right of action.
- Change to: "A stricter New York law, signed on 28 October 2026 and in force from 1 January 2027, bars operators from offering minors 'unsafe AI companion features', such as claiming to be human or encouraging secrecy or isolation, and requires them to check users' ages [@nyassembly2026a10379; @hklaw2026new]."
- Add a Table 10.3 row after the existing New York row: "| New York | General Business Law Art. 48 (S9051-B, Chapter 368 of 2026), in force January 2027 | Bars 'unsafe AI companion features' for minors (e.g. claiming to be human, encouraging secrecy or isolation, sexual content); age assurance; Attorney General enforcement, civil penalties up to $25,000 per violation |". Add both keys to the table's source list.
- Bib:
  - Change the note on `nyassembly2026a10379` to "Signed 28 October 2026 as Chapter 368 of the Laws of 2026; in force 1 January 2027".
  - Add `@misc{hklaw2026new, author={{Holland \& Knight}}, title={New York Enacts {AI} Chatbot Safeguards for Minors}, year={2026}, howpublished={Law-firm alert, November 2026}, url={https://www.hklaw.com/en/insights/publications/2026/11/new-york-enacts-ai-chatbot-safeguards-for-minors}}`.

## SHOULD change (real but not blocking)

### S1. State lawsuits against OpenAI: Oregon sued on 17 November 2026
- Where: ch10.md:163
- Text now: "By late October 2026 ten had sued OpenAI, alleging that ChatGPT harmed children and that the company misled the public about its safety"
- Problem: OUTDATED (correct as dated). Ten is right for late October: eight states on 14 October (Arizona, Arkansas, Idaho, Iowa, Kansas, Montana, Nebraska, West Virginia), Florida (June) and Texas (23 October). Oregon's Attorney General then sued on 17 November 2026 in Multnomah County Circuit Court under the Unlawful Trade Practices Act, seeking at least $2 billion.
- Evidence: Oregon Capital Chronicle, 17 Nov 2026 (https://oregoncapitalchronicle.com/2026/11/17/oregon-sues-open-ai-for-more-than-2b-for-child-endangerment-misleading-the-public/); Engadget, 17 Nov 2026; Troutman, "Eight State AGs Sue OpenAI" (16 Oct 2026).
- Change to: "By mid-November 2026 eleven had sued OpenAI, most recently Oregon on 17 November, alleging that ChatGPT harmed children and that the company misled the public about its safety [...; add an Oregon source]."

### S2. "First detailed rules" for California SB 243 conflicts with New York's earlier law
- Where: ch10.md:165
- Text now: "California's SB 243, in force since January 2026, set the first detailed rules."
- Problem: UNSUPPORTED "first" / INTERNAL TENSION. New York's Article 47 took effect on 5 November 2025, two months before SB 243, and the same paragraph says so. Law-firm sources call New York the first state whose companion-chatbot law entered into force (Hochul letter of 5/10 November 2025; Manatt and Fenwick alerts).
- Change to: "California's SB 243, in force since January 2026, set more detailed rules."

### S3. Opening overstates who got GPT-4 in the Turkish trial
- Where: ch10.md:5
- Text now: "a field experiment in a large high school in Turkey gave nearly 1,000 mathematics students access to GPT-4 during practice sessions."
- Problem: OVERSTATEMENT. Nearly 1,000 students took part, but the control arm, about a third of classes, had textbooks and notes only (PNAS, PMC12232635).
- Change to: "a field experiment with nearly 1,000 mathematics students in a large high school in Turkey gave some of them access to GPT-4 during practice sessions."

### S4. FDA 510(k) quotation no longer on the cited page
- Where: ch10.md:78
- Text now: "in which a manufacturer shows that its device is \"as safe and effective, that is, substantially equivalent\" to a legally marketed device"
- Problem: The FDA page was revised (now "Content current as of: 11/19/2026"). It now reads: "A 510(k) is a premarket submission made to FDA to demonstrate that the device to be marketed is substantially equivalent to a legally marketed device (section 513(i)(1)(A) FD&C Act)". The quoted phrase no longer appears. The bib cites the August 2024 version, which I could not retrieve (Wayback blocked). The second quote, "can include clinical data", is still on the page.
- Change to: "in which a manufacturer shows that its device is \"substantially equivalent to a legally marketed device\", known as the predicate" and update the bib note on `fda2024premarket` to "content current as of 19 November 2026" with urldate 2026-11-22.

### S5. Vaccaro meta-analysis: the loss is relative to the better performer, not always the AI
- Where: ch10.md:131
- Text now: "The loss is relative to the AI working alone, not to the human [@vaccaro2024combinations]."
- Problem: IMPRECISE. The −0.23 is measured against "the best of humans or AI alone". The same paragraph says combinations gained when the human was the stronger partner, which contradicts "relative to the AI". Source: Nature Human Behaviour abstract; the full text (PMC11659167) gives g = 0.64 against humans alone.
- Change to: "The loss is relative to whichever partner performed better alone, usually the AI, not to the human [@vaccaro2024combinations]."

### S6. Rori paper has a published (conference) version
- Where: ch10.md:29 (Table 10.1 "Henkel et al. (preprint)"), ch10.md:38 ("The current version of the preprint"), bib `henkel2024effective`
- Problem: arXiv v2, the version the chapter uses, appeared as a short paper in *Artificial Intelligence in Education: Posters and Late Breaking Results…*, Communications in Computer and Information Science, Springer 2024, pp. 373–381. The DOI is 10.1007/978-3-031-64315-6_34 (Crossref verified). Its title is "Effective and Scalable Math Support: Experimental Evidence on the Impact of an AI-Math Tutor in Ghana". Calling it only a "preprint" is slightly inaccurate. The numbers in the chapter are right.
- Change to: Table: "Henkel et al. (short conference paper)". Text: "The published version of the study (an AIED 2024 short paper, identical to the preprint's second version) reports…". Add the DOI to the bib, or cite both versions.

### S7. HEPI: the report hedges the "move back" to exams
- Where: ch10.md:68
- Text now: "The report's authors describe a move back towards traditional exam-style assessment, alongside assessments designed to exclude AI and others that include its use by design"
- Problem: SLIGHTLY STRONGER THAN SOURCE. HEPI Report 199, p. 29, says concerns "may have pushed more institutions – at least initially – back to traditional exam-style assessments. However, we are now also seeing institutions embrace AI in assessments…"
- Change to: "The report's authors suggest that integrity concerns may have pushed some institutions, at least initially, back towards traditional exam-style assessment, and that others now combine assessments designed to exclude AI with ones that include its use by design"

### S8. Covington alert used where the FDA primary source exists
- Where: ch10.md:89
- Problem: The FDA has its own page, "Considerations for the Regulation of Generative AI-Enabled Medical Devices: Discussion Paper and Request for Feedback" (docket FDA-2026-N-7874, comments due 19 October 2026). It states that the paper does not propose or implement policy. The content is right; citing the primary source would be stronger than "According to a client alert from the law firm Covington".
- Change to (optional): "In August 2026 the agency published a discussion paper, explicitly not guidance, on how generative-AI devices might be assessed by risk, tested before marketing and monitored afterwards [@fda2026considerations]."

## Could not verify
- ch10.md:78, the August 2024 wording of the FDA 510(k) page ("as safe and effective, that is, substantially equivalent"). The live page was revised on 19 Nov 2026 and the Wayback Machine is blocked from this environment. This is low risk; S4 removes the dependency.
- ch10.md:129, "GPT-4 working alone scored a median of 92%". The abstract gives only "+16 percentage points" over the conventional-resources group (median 74%), which is consistent. The 92% is in the paper body, which I did not re-read. Low risk.
- ch10.md:66, the conclusion of Jiang et al. 2024 (ETS) that carefully developed detectors are "not necessarily biased". The title is verified on Crossref but the abstract is not available there; I checked the claim against the title and my knowledge only. Low risk.
- ch10.md:3, "The students then questioned the chatbot freely". The working paper describes teacher-guided, curriculum-aligned activities with students working in pairs. "Freely" is the author's gloss and not wrong as such. Low risk.
- None of these needs a human check before printing, apart from optionally re-reading Jiang et al. 2024.

## Reader notes
1. ch10.md:5: "gave nearly 1,000 mathematics students access to GPT-4". A reader assumes everyone had it; see S3.
2. ch10.md:23: the Nigeria paragraph is a dense run of numbers (attrition, bounds, 0.16 SD, $48/$9). It is accurate, but a lay reader may lose the thread. Splitting it after "…rest on assumptions about who stayed away." would help.
3. ch10.md:36: "194 eligible students … counts 142 results in the AI arm and 174 in class". The reader is left to work out why these do not sum to 194 or 388. One clause would help: "because not every student completed every test".
4. ch10.md:135: "After adjustment … the odds ratio was 0.77 …, pointing the other way". The raw rates favour control and the adjusted estimate favours the assistant, and "the other way" is ambiguous. Suggest: "pointing towards a benefit".
5. ch10.md:188: the Oxford study (Bean et al.) on whether chatbot health advice helps sits inside Section 10.7 on privacy, between ChatGPT Health and developers' retention defaults. It reads as a detour. It would fit better at the end of Section 10.5.
6. ch10.md:165: "California's SB 243 … set the first detailed rules" appears three sentences before "New York's law, in effect since November 2025". An attentive reader notices the order; see S2.
7. ch10.md:131: "The loss is relative to the AI working alone" sits awkwardly with the preceding sentence about gains when the human is stronger; see S5.
8. ch10.md:38: "The preprint's arXiv abstract still gives the first version's 'approximately 1,000 students' and 0.37". This is accurate and useful, but inside-baseball for a general reader. It could go to a note.
9. The chapter names no individual lawsuit (it does not mention Raine v. OpenAI or Garcia v. Character Technologies) and does not mention Khanmigo. Given the legal sensitivity this is a defensible choice, and nothing in the text needs those names.

## Checked and confirmed

**Opening and 10.1 (tutoring)**
- Nigeria (World Bank WPS 11125 PDF, openknowledge bitstream): June–July 2024; nine public schools in Benin City; first-year senior secondary; Copilot/GPT-4; pairs; twelve 90-min sessions, at most two a week; lottery among volunteers; 657 T / 671 C, of whom 422 / 337 sat the endline (so 235 and 334 missing, 35.8% and 49.8%); ITT 0.31 SD total and 0.238 SD English; attendance 72%; larger effects for girls (girls-only school caveat) and for higher prior attainment; $48 per pupil, $9 marginal; 0.238 SD = 1.5 years and 0.31 SD = 2 years (implied ≈0.16 SD a year, recomputed); retrieval practice and Bjork desirable difficulties in prompts; working paper.
- Bastani et al. PNAS 2025 (PMC12232635): nearly 1,000 students; about fifty grade 9–11 classes; four 90-min sessions; about 15% of the curriculum; class assignment by integer program matching observables, with random allocation of students to classes; +48% / +127% practice; −17% exam for GPT Base (0.321 → 0.267, recomputed); GPT Tutor −0.004, n.s.; "crutch"; "What is the answer?" ×10 on 57 problems gives 51% correct, 42% logical and 8% arithmetic errors; two part-time teachers; closed-book, closed-laptop exam; misperception of learning; limited heterogeneity on preregistered variables; autumn 2023.
- Kestin et al., Sci Rep 2025 (nature.com): Fall 2023, PS2 for life sciences; 233 enrolled and 194 eligible; N = 142 AI vs 174 in class; d = 0.63 by regression, called an underestimate because of the ceiling (0.73–1.3 by quantile regression); median 49 min vs 60 min; higher engagement and motivation; AI lesson at home; step-by-step solutions in prompts; tests built by a separate team member and not counted for grades; overlap between authors and the active-learning literature.
- Rori (arXiv 2402.09809 v2 PDF §3.1–4.3, plus v1): 11 schools, 6 control and 5 treatment, randomised; grades 3–8; two 30-min sessions a week; baseline February and endline August 2023. **Analysed sample: 477 of 637** (241 C + 236 T in §3.2; Table 1 says 237 T, an inconsistency in the source). Baseline 336 T / 301 C, so attrition 100/336 vs 60/301 (25% overall); drop-outs scored lower at baseline (18.53 vs 22.26); d = 0.36. The arXiv listing abstract still shows "approximately 1,000 students in grades 3-9" and 0.37; v1 counted 850 at baseline including 213 ninth-graders. The chapter's figures are right.
- Tutor CoPilot (arXiv 2410.03017 abstract, v of 10 Oct 2026, still a preprint): 900 tutors and 1,800 students; +4 pp and +9 pp; $20 per tutor per year; more guiding questions, fewer answers given away.
- Liu et al., Maryland (EdWorkingPaper 26-1598 PDF, 30 Sep 2026; version of Oct 2026): 2,379 students and 30 instructors; Fall 2025; GPT-4o; −0.37 SD in the exact-match sample; not significant in the full sample; first-generation losses; 14.63% ever used it; 0.37/0.15 = 2.5 SD (recomputed).
- Nickow et al. AERJ (Crossref abstract): pooled 0.288 SD; moderators exactly as stated.
- Kulik & Fletcher 2016 (Crossref abstract): 50 evaluations; median 0.66; local vs standardised tests.
- Cheung & Slavin 2016 (Crossref abstract): 645 studies from 12 reviews; twice as large for published, small and experimenter-made; quasi-experiments larger.
- VanLehn 2011 (0.79 / 0.76), Bloom 1984, Kraft 2020 (747 RCTs, median 0.10, benchmarks), Cohen conventions: from knowledge, all correct.
- Pew 2026 (pewresearch.org): 1,458 teens, 25 Sep–9 Oct 2025; 54% schoolwork; 10% all or most; 12% emotional support; 16% casual conversation.
- Pew 2025 short read: 26% (vs 13% in 2023); 1,391 teens, Sep–Oct 2024; 54% research acceptable; 18% essays acceptable.
- Chatterji et al. NBER w34255 (OpenAI PDF via search): about 10% tutoring or teaching; 1.9% relationships and personal reflection; 0.4% games and role play.
- EEF/NFER Teacher Choices trial (EEF PDF): 68 schools (34 + 34); Year 7/8 science; 56.2 vs 81.5 min a week (31%); blind expert panel found no quality difference; teacher diaries.

**10.2**
- Fan et al. BJET (Crossref abstract): 117 students; four conditions; ChatGPT best essay improvement, no difference in knowledge gain or transfer.
- Stadler et al. 2024 (search plus repository): 91 students; ChatGPT vs Google; lower cognitive load, lower-quality reasoning.
- Kosmyna et al. (arXiv abstract v2): 54 participants, 18 in session 4; weakest connectivity; lowest ownership; difficulty quoting.
- OpenAI study mode (TechCrunch, 29 Jul 2025): asks questions and can withhold answers; students can leave it.
- NYC moratorium (nyc.gov via search): 2 Sep 2026; one year; 2-K to grade 8; companion chatbots banned in all grades; five supervised high-school pilots.
- Risko & Gilbert definition (verbatim) and Bjork 1994: knowledge.

**10.3**
- HEPI Report 199 PDF: 1,054 students; Savanta, December 2025; 94% for assessed work; text included directly 3% → 8% → 12%; 65% say assessment changed significantly.
- Liang et al. Patterns 2023 (arXiv PDF): seven detectors; 91 TOEFL essays; mean FPR 61.22%; near-perfect on US 8th-grade essays; 11.77% after enhancement.
- Al Ali et al. 2026 (arXiv abstract): no systematic bias against non-native Czech writers across three detector families.
- Hao 2026 (arXiv): ETS book chapter on GRE essays.
- OpenAI classifier withdrawn July 2023 for "low rate of accuracy": knowledge, matches the bib.
- EU AI Act Art. 5(1)(f) emotion recognition in education, from 2 Feb 2025; Annex III(3)(a)–(d): knowledge.
- Digital Omnibus Reg. (EU) 2026/1744 (signed 8 Jul 2026; Annex III to 2 Dec 2027, Annex I to 2 Aug 2028): White & Case / EUR-Lex listing via search.

**10.4**
- FDA AI-enabled device list, live page (content current 09/04/2026, still the latest on 22 Nov 2026), recounted by script: 1,614 entries; K 1,553 / DEN 40 / P 21 (96.2 / 2.5 / 1.3%); radiology 1,230 (76.2%), cardiovascular 154, neurology 73; earliest 1995; latest 29 Jun 2026; 2015–2025 yearly counts 6, 18, 27, 65, 80, 114, 129, 162, 226, 235, 335, exactly as in Figure 10.2 and figs_ch10.py; 181 in 2026; "not a comprehensive resource"; plan to tag foundation-model/LLM devices; no ambient-scribe products found by name search.
- FDA 510(k) page: "can include clinical data … software validation" (wording of the main quote changed; see S4).
- FDA generative-AI discussion paper, August 2026, not guidance (FDA page and law-firm alerts via search).
- Liu et al. 2019 Lancet Digital Health (82 studies, 25 externally validated; 87.0/86.4 and 92.5/90.5): knowledge.
- Takita et al. 2025 (PubMed): 83 studies; 52.1%; no difference vs physicians or non-experts; worse than experts.
- Plana et al. 2022 (PubMed): 41 RCTs; median 294; 21 (51%) single-site; none fully CONSORT-AI adherent.
- Han et al. 2024 (PubMed and PMC full text): 86 RCTs; 70 (81%) positive; 37 (43%) gastroenterology; publication-bias warning.
- CONSORT-AI 14 new items (Crossref record; knowledge).
- Specificity example: 1.5% of 10,000 = 150 (recomputed).

**10.5**
- MASAI, Lång et al. 2023 (PubMed): 80,033 women; 6.1 vs 5.1 per 1,000; p = 0.052; FPR 1.5% in both arms; workload −44.3%; in situ 60 vs 38; score 10 → double reading; CAD marks for 8–10; radiologists not masked.
- MASAI, Gommers et al. Lancet 2026 (PubMed): 105,934 women; interval cancers 1.55 vs 1.76 per 1,000; ratio 0.88 (0.65–1.18); fewer invasive (75 vs 89); sensitivity 80.5 vs 73.8%; specificity 98.5% in both.
- Eisemann et al. 2025 (PubMed): 463,094 women; July 2021–Feb 2023; radiologists chose whether to use AI; funded by Vara; detection up, recall not up.
- Epic, Wong et al. 2021 (PubMed): 38,455 hospitalisations; 2,552 sepsis; AUC 0.63; 15-minute scoring.
- Epic, Wong et al. 2026 (PubMed): four health systems; 227,091 encounters, Aug 2023–Mar 2025; AUROC 0.82–0.92; PPV 0.13–0.26.
- Goh et al. 2024 (PubMed): 50 physicians; Nov–Dec 2023; 76% vs 74%; LLM alone +16 pp.
- Goh et al. 2025 (PubMed): 92 physicians; +6.5 pp; +119 s; no difference from GPT-4 alone.
- Vaccaro et al. 2024 (Crossref abstract and PMC11659167): 106 studies; g = −0.23; g = 0.64 vs humans alone; decision vs creation tasks.
- AMIE, Tu et al. 2025 (PubMed): 159 scenarios; 20 PCPs; 30/32 and 25/26 axes; text-chat caveat.
- AMIE, McDuff et al. 2025 (PubMed): 20 clinicians; 302 cases; 59.1 vs 33.6%; 51.7 vs 44.4%.
- Brodeur et al. Lancet 2026 (PubMed; Lancet 24 Oct 2026, epub 8 Oct): single-centre, single-arm; 98 completed; zero safety stops; one hallucination; five interventions adding information; funded by Alphabet.
- Penda, Agweyu et al. Nature Medicine 2026 (PubMed; NPR for GPT-4o): 16 facilities; 103 clinical officers; 9,691 patients, Apr–Jul 2025; 2.2 vs 2.0%; aOR 0.77 (0.55–1.08); no safety signal; "probably modest".
- Lukac et al. NEJM AI (UCLA release, PubMed abstract via search): 238 physicians; 14 specialties; about 72,000 encounters; Nov 2024–Jan 2025; Nabla 4:30 → 3:49, 9.5% larger reduction than control; DAX n.s.; usage 33.5% / 29.5%; occasional clinically significant inaccuracies; one mild adverse event.

**10.6**
- Common Sense / NORC report PDF: 1,060 teens; 30 Apr–14 May 2025; 72% ever; 52% regular; 33% of users chose AI over a person; 67% found it less satisfying; nonprobability component; definition includes ChatGPT/Claude.
- Fang et al. (arXiv abstract): n = 981; four weeks; modality × conversation type; no condition effects; heavier voluntary use linked to worse outcomes.
- Phang et al. (arXiv abstract): more than 3 million conversations; more than 4,000 surveyed; a small number of users accounts for a disproportionate share of affective cues.
- Zhang et al. Nature Human Behaviour 2026 (PubMed): 1,131 users; 4,664 sessions from 237 participants; findings as stated.
- De Freitas et al. JCR 2025 (arXiv abstract, HBS): on par with talking to a person; more than YouTube; week-long reductions; feeling heard.
- Turkle, *Artificial Intimacy: Who We Become When We Talk to Machines* (Little, Brown, 29 Sep 2026; Hachette, Kirkus).
- Folk & Dunn, Psychological Science 2026 (Crossref abstract): 12 months; more than 2,000 adults; four Western countries; single-item and broader measures exactly as stated; analyses exploratory.
- Therabot, Heinz et al. NEJM AI 2025 (PubMed): N = 210; MDD/GAD/CHR-FED; 4-week intervention; waitlist until 8 weeks; more than 6 hours of use; therapeutic alliance comparable to human therapists.
- Dartmouth release: "first-ever clinical trial…"; Heinz: "no generative AI agent is ready to operate fully autonomously in mental health"; team ready to intervene.
- OpenAI suicide figures (TechCrunch, 27 Oct 2025): 0.15%; "explicit indicators of potential suicidal planning or intent"; "more than 800 million weekly active users"; 91% vs 77%.
- Character.AI and Google settlements (CNN via KVIA, 7 Jan 2026): five suits (Garcia plus four in NY, CO and TX); terms not disclosed.
- Florida suit (June 2026; Claims Journal and Bloomberg Law via search).
- Eight-state suits of 14 Oct 2026 (Troutman, Haynes Boone, KUTV via search).
- Texas suit, 23 Oct 2026, Collin County, OpenAI and Altman (Texas Tribune and Courthouse News via search).
- FTC 6(b) orders (FTC release, 11 Sep 2025): seven companies, list confirmed.
- Character.AI under-18 announcement (blog, 29 Oct 2025; effective by 25 Nov).
- SB 243: disclosure standard, crisis protocol, three-hour break reminders for known minors, at least $1,000 per violation (FPF); in force 1 Jan 2026 and reporting from 1 Jul 2027 (Skadden and Sidley via search).
- SB 1119, signed 10 Sep 2026 as Ch. 190: age determination or treat all users as minors; ban on simulated romance and on encouraging reliance; default time limits and parental controls; most duties from 1 Jul 2027; up to $15,000 per child for intentional violations (ZwillGen, Fenwick, Common Sense). Annual risk assessment confirmed by Common Sense.
- SB 867: toys for children under 16; moratorium through 1 Jan 2031 (Fenwick).
- New York Art. 47: in force 5 Nov 2025; disclosure at the start and every three hours; self-harm protocol (FPF, Manatt/Fenwick via search).
- Illinois WOPR Act, signed 1 Aug 2025; Nevada AB 406, signed 5 Jun 2025; Utah HB 452, signed 25 Mar 2025, disclosure and data rules (search).
- Garante / Replika (EDPB news item and Reuters via search): €5 million; decision 10 Apr 2025, announced 19 May; no legal basis; privacy notice; no age verification; separate training proceeding.
- Garante / Character Technologies (Il Post, Reuters via The Star): €158,000; decision 3 Jul 2026, announced 9 Jul; privacy notice and age verification; orders on age checks and private-by-default profiles for minors.

**10.7**
- King et al. AIES 2025 (arXiv abstract, Crossref): six developers; training on chats by default; some retain chats indefinitely; four include children's data; policies lack information.
- Anthropic consumer terms (anthropic.com, 28 Aug 2025): user choice; 5-year vs 30-day retention.
- SDNY stipulation (ECF 992 PDF, 9 Oct 2025): obligation terminated as of 26 Sep 2025; already-preserved data kept except EEA, Switzerland and UK; Appendix A domains still preserved. May 2025 order (Judge Wang): knowledge.
- ChatGPT Health (TechCrunch, 7 Jan 2026): more than 230 million weekly users; connects wellness apps; no training on Health conversations.
- Bean et al. Nature Medicine 2026 (PubMed): 1,298 participants; three LLMs; 94.9% alone; under 34.5% with participants; no better than control.
- Mireshghallah et al. (arXiv abstract): 39% and 57%.
- Carlini 2021; ChatGPT memory Feb 2024 and Apr 2025; BetterHelp $7.8 million (2023); GDPR Art. 9; HIPAA covered entities; EDPB Opinion 28/2024: knowledge.
- Garante €15 million fine (provv. 755 of 2 Nov 2024, announced 20 Dec 2024) annulled by Tribunale di Roma judgment 4153/2026 of 18 Mar 2026 on one-stop-shop competence, without ruling on substance (diritto.it, dirittodiinternet.it, ANSA via search). No Cassazione appeal reported as of November 2026.

**10.8**
- Speech Accessibility Project (live site): about 2,000 participants by end of September 2025; Microsoft gains of 18–60%; five company supporters; conditions listed.
- Gonzalez Penuela et al. 2026 (arXiv abstract): 20 participants; 3.76 and 4.13 out of 5; 22.2% incorrect; 10.8% abstained.
- Garg et al. 2026 (arXiv abstract): 1,859 images; 98% vs 75%.
- Crossref records confirmed for NLLB (Nature 2024), Seamless (Nature 2025), Willett 2023, Card 2024, Gonzalez Penuela 2024 (CHI). Their figures (44% BLEU; 62 wpm at about 24% WER; 97.5% and 248 hours; 2.76/5), WHO's 1.3 billion / 16%, and Be My Eyes' 14 Mar 2023 announcement: knowledge, correct.

**Cross-references.** Chapter 8 (endoscopy deskilling and the later trial), Chapter 9 (text-detector discussion), Section 2.8 (AUC), Section 11.5 (automation bias), Table 13.1 and Section 13.6 (Garante): all present and consistent.

**Figures, glossary and bib keys.** Figures 10.1–10.3 match the spec, figs_ch10.py and the sources. Glossary entries are consistent with the text. All 130 bib keys are cited and every citation resolves.

## Tally
Claims checked against a web source: 112. Confirmed: 103. Wrong: 1 (M1). Outdated: 2 (S1; S4 source page changed). Unsupported by cited source or overstated: 4 (S2, S3, S5, S7). Could not verify: 4. Arithmetic items recomputed: 22 (errors: 0). Bib entries checked: 52 (problems: 3; nyassembly2026a10379 note outdated, fda2024premarket page revised, henkel2024effective has a published version).
