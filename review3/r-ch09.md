# Third review: Chapter 9 — Information, Media and Democracy

STATUS: WORK IN PROGRESS (first version saved after the full read-through; web verification is being appended section by section).

## Verdict
(pending — to be filled in when the fact-check is complete)

## MUST change before printing

### M1. US midterms described as still to come
- Where: textbook/chapters/ch09.md:128
- Text now: "In the campaign for the US midterm elections, due on 3 November 2026, Reuters reported in March that deepfakes had become an open campaign tool."
- Problem: OUTDATED. The election was held on 3 November 2026; "due on" is future tense in a book printed after the vote. The paragraph opener at line 126 ("The elections of 2026, up to the end of October, showed more AI use but no clearer evidence of effects") also leaves the midterms hanging. (Outcome and any documented AI incidents: being checked, see below.)
- Evidence: date only (pending web check of post-election reporting).
- Change to: (wording to be finalised after the post-election search) "In the campaign for the US midterm elections of 3 November 2026, Reuters reported in March that deepfakes had become an open campaign tool."

## SHOULD change (real but not blocking)
(pending)

## Could not verify
(pending)

## Reader notes (from the first read, before fact-checking)
1. Line 63: "Fluent paraphrasing is a stronger attack, as the next paragraph shows. The authors' own follow-up found, however, that watermarks often survive paraphrasing..." — the "next paragraph" is the figure caption and then Zhang/Jovanović, and the sentence that follows immediately says the opposite (watermarks survive paraphrasing). A reader gets "stronger attack" and "often survive" back to back with a "however" that points the wrong way.
2. Line 128: "The United States and Brazil showed the regulatory gap and one attempt to close it." Brazil "held its presidential run-off on 25 October 2026" but the chapter says nothing about whether the rules worked or what happened; the US sentence is in the future tense ("due on"). The paragraph reads as written before both votes.
3. Line 126 vs line 128: "The elections of 2026, up to the end of October" — then the text discusses the midterm campaign (November). Scope statement and content do not match.
4. Line 150: "nothing significant (Lin's Polish experiment)" — the reader has not been told that Lin et al. tested personalisation at all; the Polish personalisation arm appears only here, in a parenthesis.
5. Line 144: the Costello paragraph gives "about 20%" twice and the correction history in one long sentence; the phrase "an expression of concern, since rescinded, and then a correction" is hard to parse on first reading (was the correction also rescinded?).
6. Line 179: "missed the human results by 12.4 percentage points on average" — no sense of what a good or bad miss is (e.g. the typical sampling error of the human panel), so the number floats.
7. Line 199: "Publishers expect a further fall of 43% over three years." — unclear who "publishers" are (a survey of executives?) and from which base.
8. Line 246: "the company that Reuters, reporting Ofcom's October update, called 'SpaceXAI, formerly xAI'" — the name appears from nowhere; a reader who does not know of a merger will stumble.
9. Table 9.2: Costello row gives N = 2,044 "(corrected analysis)" while the running text never gives the originally published N (2,190), so "corrected" has no visible antecedent.
10. Line 23 is a very long paragraph (Meta 2024, Meta 2026, OpenAI 2026, Safety Report) ending in a summary sentence that restates the paragraph's opening claim.

## Checked and confirmed
(working list, being extended)

Opening
- Calls on 21 Jan 2024, two days before the primary; "thousands"; 9,581 calls — FCC forfeiture order FCC 24-104 (docs.fcc.gov), paras 6, 12.
- AG estimate 5,000–25,000 — NBC News 6 Feb 2024 ("From 5,000 to 25,000 people received the calls ... Formella said").
- "save your vote for the November election" — AP 13 Jun 2025 (ksat.com copy).
- NAL $6m 23 May 2024; forfeiture order adopted 26 Sep 2024 (released 30 Sep), for caller-ID spoofing — FCC 24-104.
- Acquitted June 2025 on all 22 counts (11 voter suppression, 11 candidate impersonation) — AP.
- ElevenLabs, "instant voice cloning for as little as $5 a month"; 220 speakers; 604 listeners; "approximately 80%"; "only about 60%" — Barrington, Cooper, Farid (arXiv 2410.03791 text; Crossref for Sci. Rep. 15, 31 Mar 2025).
- FCC declaratory ruling FCC 24-17 adopted 2 Feb 2024, released 8 Feb 2024; AI voices "artificial" under TCPA; cites NH call (fn 22) — FCC PDF.

9.1
- Meta Dec 2024: "only incremental productivity and content-generation gains"; "less than 1%" — about.fb.com.
- Meta H2 2026 Adversarial Threat Report (August 2026): "from an occasional tactic ... to a near-standard component of influence operation tradecraft"; every CIB network used generative AI; "behavioral detection approaches remain effective" — PDF pp. 34–35 (third-party copy).
- OpenAI Oct 2026: Russia and Iran operations; AI as shortcut for routine work; placement in established media "appeared to have reached a wider audience" — NPR/OPB 9 Oct 2026 (openai.com page 403).
- International AI Safety Report 2026: "over 100 independent experts"; "often at least as effective as non-expert human participants"; "is documented but not yet widespread" (sec. 2.1.2); voice-clone scams (sec. 2.1.1) — arXiv 2602.21012.
- Kapoor & Narayanan: 78 cases, 39 non-deceptive, "no more than a few hundred dollars", "seven times more often" — knightcolumbia.org.

9.2
- Deepfake-Eval-2024: 88 websites, 52 languages; AUC down 50%/48%/45%; seven commercial vendors; none ≥90% accuracy; 90% as lower bound for analysts — arXiv 2503.02857v5 (but see S-item on the 0.58 figure).
- Base-rate example recomputed: 990 true alarms, 10,000 false alarms, 91% false.

9.3
- Kirchenbauer 2023: z = 4 at ~128.2 tokens, FPR 3×10^-5, mean 159.5 green tokens, 98.4% detected; T5 attack AUC 0.998/0.988/0.954/0.838/0.696, PPL 6.3/13.1/21.2/28.4/33.9; TPR@4 0.819 (ε=0.1), 0.353 (ε=0.3) — arXiv 2301.10226 Fig. 6, Table 8. Arithmetic (sd 7.07; threshold 128.3; p = 3.2e-5) recomputed.
- Kirchenbauer 2024: ~800 tokens after strong human paraphrasing — arXiv 2306.04634 abstract.
- Jovanović et al.: "under $50", "over 80%", "previously considered safe" — arXiv 2402.19361 abstract.
- SynthID Detector opened to everyone 7 Oct 2026; page updated 29 Oct; partners OpenAI, NVIDIA, Kakao, Apple; "over 180 billion images and videos" — blog.google.
- OpenAI SynthID + C2PA, public checker preview, 19 May 2026 — The Next Web; OpenAI announcement/help page ("ChatGPT, Codex, or the OpenAI API").
- C2PA founded 22 Feb 2021 by Adobe, Arm, BBC, Intel, Microsoft, Truepic — Microsoft press release.
- C2PA explainer 2.2: "cannot tell you whether the digital content is true, accurate or factual"; credentials optional, absence not a signal — spec.c2pa.org.
- Pixel 10: Content Credentials on "any JPEG photo capture"; Assurance Level 2 "highest security rating currently defined"; Titan M2; "the implied truth effect" — Google Security Blog 10 Sep 2025.
- iPhone 18 Pro (9 Sep 2026): opt-in reference image, signed sensor data, no C2PA mention, SynthID "in a software update later this year" — apple.com newsroom.
- Golaszewski et al. ePrint 2026/804: exclusion range, time-stamp disagreement, revocation — eprint.iacr.org abstract.

9.4
- Reuters 28 Mar 2026 (Ax, Coster): NRSC Talarico ad, "AI generated" in small font; Loudoun County GOP committee; Mike Collins Senate campaign (Georgia); 28 states; no federal regulation — Star-Advertiser copy.
- TSE rules of 2 Mar 2026: explicit, prominent label; no new synthetic content in 72 h before (and 24 h after) the vote; ban on AI recommending candidates — CNN Brasil.
- Romania: annulled 6 Dec 2024; run-off due 8 Dec; declassified files; Telegram-coordinated TikTok campaign; "coup"; interior-ministry inference from Ukraine/Moldova similarities — Solea (Univ. of Portsmouth). Dan won rerun 18 May 2025, "centrist mayor of Bucharest" — AFP.

9.5
- Costello correction: EoC 11 Jun 2026 (now "RESCINDED"), erratum 22 Oct 2026 (Crossref); "inconsistencies in the application of screening criteria"; "extraneous spliced rows" (EurekAlert 1131247); "primary analyses included 2044 conspiracy believers with complete pretreatment- and post-treatment-belief data" (Dryad/DataCite).
- Hackenburg et al. Science 390(6777), 4 Dec 2025: N = 76,977; 19 LLMs; 707 issues; 466,769 claims; +2.94 / +3.60 pp; 36–42% at one month; post-training up to 51%; personalisation +0.43 pp; maximal persuasion 15.9 pp; 29.7% inaccurate vs 16.0%; 9 minutes — arXiv 2507.13919 and LSE accepted manuscript (Table S1: 8.80 [8.03, 9.57], 6.05 [4.95, 7.15]).
- Lin et al. Nature 648, 394–401: 2,306 / 1,530 / 2,118 / 501; 2.88 (2.02, 3.74); 10.05 (7.52, 12.57); 9.94 (6.68, 13.20); 22.73 (17.00, 28.46), n = 193; "slightly more than a third"; "more than half"; right-leaning less accurate; no accuracy–persuasion association; debriefing; state and local — full-text PDF (MIT-hosted).


## Tally
(pending)
