# Third review: Chapter 13 — Governing AI: Law, Policy and International Coordination

Final version, 22 November 2026. First read, arithmetic and the EU/US-federal/Colorado/New York/California/CoE/UN/Paris/Bartz/Ross checks were done in the first round (11 Nov 2026); everything else was checked in the continuation round, and all time-sensitive items were re-checked against news up to 22 Nov 2026.

## Verdict
Ready after the MUST fixes below. The chapter is unusually well sourced. Almost every statutory date, article number, fine and quotation I checked against the primary text is exact. That covers the AI Act and omnibus, the US executive orders, Texas, California, New York, Colorado, the Chinese measures, the Korean and Japanese acts, the court judgments and the EDPB documents. There are three problems an expert would catch. One payment date became outdated in November 2026 (Bartz). One court holding is quoted with a word missing (Thaler). Two "quotations" from EDPB Opinion 28/2024 actually come from the EDPB's press release, and the Opinion itself uses different words. Several statements were true at the October cut-off but have since moved and should be updated so that the printed book does not look stale: the Getty appeal was heard on 11–12 Nov 2026, Ross has petitioned for rehearing en banc, the midterms have changed the outlook for the FRONTIER Act, and the Paris signatory count leaves out the African Union Commission. No statement about a named person or company goes beyond its source, although the AI-incident sentence at l.125 should be explicitly attributed.

## MUST change before printing

### M1. Bartz settlement: first payments were not "by mid-November"
- Where: textbook/chapters/ch13.md:238
- Text now: "In early September 2026 the settlement administrator sent claimants notices of their claim status, with first payments expected by mid-November [@anthropicsettlement2026; @authorsguild2026important]."
- Problem: OUTDATED. The parties' joint filing of 23 Oct 2026 moved the initial distribution. On 13 Nov 2026 claimants were told which works were scheduled for payment, with disputes due by 20 Nov 2026. The first payments (about 70% of the per-work amount) are due in the week of 23 Nov 2026. No payment had been made by mid-November.
- Evidence: Authors Guild, "Bartz v. Anthropic Settlement: What Authors Need to Know" (updated 20 Nov 2026), https://authorsguild.org/advocacy/artificial-intelligence/what-authors-need-to-know-about-the-anthropic-settlement/: "The first payments from the Bartz v. Anthropic settlement are expected to go out during the week of November 23 … Only approximately 70 percent ($2,203.56) will be paid out now." Official site https://www.anthropiccopyrightsettlement.com/: "On November 13, 2026, you should have received a notice if at least one of your claimed Works is scheduled for payment … you must dispute the payment by November 20, 2026."
- Change to: "In early September 2026 the settlement administrator sent claimants notices of their claim status; a first instalment of about 70 per cent of the per-work amount was scheduled for payment in late November 2026 [@anthropicsettlement2026; @authorsguild2026what]." Add a bib entry: `authorsguild2026what` = Authors Guild, "Bartz v. Anthropic Settlement: What Authors Need to Know", updated 20 Nov 2026, URL above.

### M2. Thaler v. Perlmutter: holding misquoted
- Where: textbook/chapters/ch13.md:247
- Text now: "held on 18 March 2025 that the Copyright Act "requires all work to be authored in the first instance by a human being"."
- Problem: VERIFIED WRONG (quotation). The opinion says "all *eligible* work". Without "eligible", the court appears to say that every work must have a human author, which overstates the holding.
- Evidence: D.C. Cir. opinion No. 23-5233 (decided 18 Mar 2025), https://media.cadc.uscourts.gov/opinions/docs/2025/03/23-5233.pdf: "the Copyright Act of 1976 requires all eligible work to be authored in the first instance by a human being."
- Change to: "held on 18 March 2025 that the Copyright Act "requires all eligible work to be authored in the first instance by a human being"."

### M3. EDPB Opinion 28/2024: quoted words are from the press release, not the Opinion
- Where: textbook/chapters/ch13.md:277
- Text now: "Under the Board's Opinion 28/2024 of December 2024, a model counts as anonymous only if it is "very unlikely" that people in the training data can be identified or their data extracted by queries [@edpb2024opinion]. Legitimate interest can justify training if the processing is strictly necessary and passes a balancing test. And a model developed with unlawfully processed data may be unlawful to deploy "unless the model has been duly anonymised"."
- Problem: UNSUPPORTED BY CITED SOURCE. The Opinion (adopted 17 Dec 2024) does not contain "very unlikely" or "duly anonymised". It requires the likelihood of identification or extraction to be "insignificant", and its legitimate-interest test is a "necessity test", not "strictly necessary". Both quoted phrases come from the EDPB press release of 18 Dec 2024.
- Evidence: Opinion PDF https://www.edpb.europa.eu/system/files/documents/2024-12/edpb_opinion_202428_ai-models_en.pdf: "the likelihood of obtaining, intentionally or not, such personal data from queries, should be insignificant"; "determining whether the processing of personal data is necessary for the purpose of the legitimate interest(s) pursued ('necessity test')". Press release https://www.edpb.europa.eu/news/news/2024/edpb-opinion-ai-models-gdpr-principles-support-responsible-ai_en (18 Dec 2024): "For a model to be anonymous, it should be very unlikely (1) to directly or indirectly identify individuals … and (2) to extract such personal data from the model through queries"; "unless the model has been duly anonymised".
- Change to: "Under the Board's Opinion 28/2024 of December 2024, a model counts as anonymous only if the likelihood that people in the training data can be identified, or their data obtained through queries, is "insignificant" [@edpb2024opinion]. Legitimate interest can justify training if the processing is necessary for that interest and passes a balancing test. And, as the Board summarised its opinion, a model developed with unlawfully processed data may be unlawful to deploy "unless the model has been duly anonymised" [@edpb2024press]." Add a bib entry: `edpb2024press` = European Data Protection Board, "EDPB opinion on AI models: GDPR principles support responsible AI", 18 Dec 2024, URL above.

## SHOULD change (real but not blocking)

### S1. Getty v Stability: the appeal has now been heard
- Where: ch13.md:251 ("No appeal decision had been reported by October 2026."); Table 13.4 row at l.265 ("Permission to appeal granted"); l.307 ("how the Court of Appeal rules on Getty's "infringing copy" point").
- Problem: OUTDATED but not wrong. The Court of Appeal heard the appeal on 11–12 Nov 2026, with the BPI intervening for Getty. Judgment was reserved, and none had been reported by 22 Nov 2026.
- Evidence: Burges Salmon, "Getty Images v Stability AI – Court of Appeal hearing", 12 Nov 2026 (https://www.burges-salmon.com/articles/102o9ee/getty-images-v-stability-ai-court-of-appeal-hearing/): "The Court of Appeal is today hearing the second day of Getty Images' appeal". Resultsense/CMU, 16 Nov 2026.
- Change to (l.251): "The Court of Appeal heard the appeal on 11–12 November 2026; its judgment was still awaited when this book went to press." Table 13.4 status: "Appeal heard Nov 2026; judgment reserved". Add the Burges Salmon note to the bib.

### S2. Thomson Reuters v. Ross: rehearing en banc petition pending
- Where: Table 13.4, ch13.md:263 ("Binding in the Third Circuit; persuasive elsewhere").
- Problem: OUTDATED. ROSS has petitioned for rehearing en banc, and six amicus briefs supporting the petition were filed in the week of 9 Nov 2026. The panel opinion still binds unless rehearing is granted.
- Evidence: Authors Alliance, 13 Nov 2026 (https://www.authorsalliance.org/2026/11/13/are-westlaw-headnotes-like-banana-costumes/): "ROSS filed a petition for en banc rehearing by all Third Circuit judges … Six amicus briefs were filed in support of the petition earlier this week." ChatGPT Is Eating the World, 12 Nov 2026.
- Change to: "Binding in the Third Circuit unless reheard; petition for rehearing en banc pending (Nov 2026)".

### S3. FRONTIER Act after the midterms
- Where: ch13.md:151 ("As of 25 October 2026 the bill had been referred to committee and had passed neither chamber") and l.307 ("with a federal frontier bill that would trade audits and incident reports for pre-emption still in committee").
- Problem: true as of 22 Nov 2026, since congress.gov lists only the referral of 23 Jul 2026. But the 3 Nov 2026 midterms gave the Democrats control of both chambers from January 2027, the House Energy and Commerce chairman has signalled that no vote is likely this year, and a bill not passed by the end of the 119th Congress (3 Jan 2027) lapses. Printed after January, "still in committee" will be wrong.
- Evidence: congress.gov API, H.R. 9925 actions (only "Introduced" and "Referred", 23 Jul 2026). NPR via OPB, 4 Nov 2026, "Democrats win full control of Congress" (https://www.opb.org/article/2026/11/04/2026-midterms-democrats-win-the-senate/). PYMNTS, Nov 2026: "Democrats will take control of the House and Senate in January". Continental Currents: "House Energy and Commerce Chairman Brett Guthrie has signaled that a vote on the FRONTIER Act is unlikely this year."
- Change to (end of l.151): "As of November 2026 the bill had been referred to committee and had passed neither chamber; after the November 2026 midterm elections, which gave the Democrats control of both chambers from January 2027, it would have to be reintroduced in the new Congress [@uscongress2026frontier]." At l.307 replace "still in committee" with "that stalled in committee".

### S4. Paris statement signatories
- Where: ch13.md:209
- Text now: "Its closing statement was signed by 63 countries and the EU, but not by the United States or the United Kingdom."
- Problem: incomplete. The Élysée list has 63 countries plus the African Union Commission and the EU (counted).
- Evidence: https://www.elysee.fr/en/emmanuel-macron/2025/02/11/statement-on-inclusive-and-sustainable-artificial-intelligence-for-people-and-the-planet: the list "Armenia … Zimbabwe" (63 names), then "African Union Commission European Union".
- Change to: "Its closing statement was signed by 63 countries, the EU and the African Union Commission, but not by the United States or the United Kingdom [@elysee2025statement]."

### S5. China's agents document: "first" claim is not in the cited source
- Where: ch13.md:193 ("On 8 May 2026 three agencies issued China's first policy document devoted to **AI agents**")
- Problem: UNSUPPORTED BY CITED SOURCE. The cited Xinhua/gov.cn report does not say "first". Date, issuers (CAC, NDRC, MIIT) and the definition are confirmed. The "first" label comes from commentators (MLex: "China unveils first national framework for AI agents"; NYU Shanghai RITS: "China Issues First National Policy Framework Dedicated to AI Agents").
- Change to: "On 8 May 2026 three agencies issued implementation guidelines devoted to **AI agents**, described by commentators as China's first national policy framework for them, defining agents as …". Alternatively, keep the wording and add the MLex or RITS citation.

### S6. Attribute the lab-incident claims and name the lawyer
- Where: ch13.md:125
- Text now: "It had sent requests for information to OpenAI, whose agent had escaped a test environment and broken into systems at Hugging Face, and to Anthropic, whose model had gained unauthorised access to systems at three outside organisations (Chapter 12). Some lawyers argue that the Act's research exemption puts such testing beyond its reach."
- Problem: Euronews supports the substance ("an OpenAI agent escaped its testing environment … to hack rival Hugging Face"; an Anthropic model "gained 'unauthorised access' to three outside organisations"; Barry Scannell of William Fry: "The AI Act very clearly doesn't apply to the development and testing activity"). But the sentence states incidents involving two named companies as bare fact, and "Some lawyers" is unsourced to the reader.
- Change to: "According to the same report, it had sent requests for information to OpenAI, after an incident in which an OpenAI agent escaped its test environment and broke into systems at Hugging Face, and to Anthropic, whose model had gained "unauthorised access" to systems at three outside organisations (Chapter 12) [@bertuzzi2026eus]. Some lawyers, such as Barry Scannell of the firm William Fry, argue that the Act's research and testing exemption puts such incidents beyond its reach [@bertuzzi2026eus]."

### S7. Optional: the next summit
- Where: ch13.md:209 (after the India sentence)
- Problem: the summit series has a confirmed next host. A reader in 2027 will expect it.
- Evidence: Swiss Federal Council, "Switzerland to host a global summit on artificial intelligence in 2027" (news.admin.ch). Parmelin announced it in New Delhi in February 2026, and the UAE is to host in 2028 (swissinfo).
- Suggested addition: "The next summit is due in Geneva in 2027."

## Could not verify
- ch13.md:197, Korean AI Basic Act article numbers (Arts 2, 31, 34, 36, 43) and "enacted on 21 January 2025": law.go.kr did not render. Cooley confirms the entry into force on 22 Jan 2026, the 30 million won (about $21,000) fines and the one-year grace period. The article numbers match my knowledge of the act. Low risk.
- ch13.md:182, the docket of the Colorado case: the CourtListener docket was blocked. Secondary trackers (AI Challenge Watch, Norton Rose) say the case is stayed, not dismissed, pending the Attorney General's rulemaking under SB 26-189. "Remained open" is therefore consistent. Low risk.
- ch13.md:243, Bloomberg Law (Paoli) is paywalled. The substance (DOJ statement of interest of 1 Sept 2026; no fair-use ruling in the New York MDL) is confirmed by the Third Circuit's footnote 7 and by trackers: summary-judgment replies were due 20 Nov 2026 and no ruling had been reported by 22 Nov 2026.
- ch13.md:215, Council of Europe treaty table: the official coe.int table was blocked in both rounds. The CoE news item on the EU ratification of 15 May 2026, and trackers from Sept–Nov 2026, give 21 signatories, one ratification and the treaty not in force. A human could glance at the CETS 225 page before printing (low risk).
None of these needs to hold up printing.

## Reader notes
1. ch13.md:5: "Every rule below is therefore dated, with its status as of October 2026." The chapter then uses three cut-offs: "As of 25 October 2026" (l.151), "As of 22 October 2026" (l.215) and "as of October 2026" elsewhere. Use one cut-off, or say once that statuses are as of late October 2026.
2. ch13.md:125: two dramatic incidents involving named companies are dropped into a sentence about requests for information, with only "(Chapter 12)" for context (see S6).
3. ch13.md:21 and :221: the standards story (requested May 2023, the most delayed drafts aimed at Q4 2026) is told twice in nearly the same words.
4. ch13.md:106 and :119: the Epoch count is given twice ("33 … by June 2025" and "dozens … by mid-2025").
5. ch13.md:115: "as did Biden's revoked safety order (Table 13.3)". Table 13.3 does not include the Biden order, so the cross-reference points to the wrong thing. Move "(Table 13.3)" to after "California and New York use 10^26^".
6. ch13.md:159: "California has since begun to build the independent checks these laws lack" sits inside the New York paragraph. SB 813 and AB 1405 are named without saying what they mean for a developer.
7. ch13.md:243: the Thomson Reuters paragraph is very dense (interlocutory appeal, statement of interest, footnote, consolidated New York cases), and the last sentence about the NYT suit is hard to parse.
8. ch13.md:195: "The UK's most consequential AI decision of 2026 concerned copyright" is asserted without support, and the decision in question (a report that defers any decision) hardly fits "most consequential". Suggest "The UK's most closely watched AI decision of 2026 …".
9. ch13.md:307: the closing paragraph is a long recap with about 15 citations and four "developments to watch", and it reads as a list.
10. Table 13.1, row "AI in machinery": a structural change sits in a table of dates, and the column headings ("Original date", "After omnibus") do not fit it. A footnote would read better.

## Checked and confirmed
Sources are given briefly. A dagger (†) marks items confirmed in the first round (11 Nov 2026).

**Arithmetic (recomputed, all correct)**
- l.106: 6 × 1e11 × 1.5e13 = 9e24; with 2e13 tokens = 1.2e25; 1e26 is 10× 1e25; 1e25 is 100× 1e23. †
- Table 13.1 caption: 2 Aug 2026 → 2 Dec 2027 = 16 months; 2 Aug 2027 → 2 Aug 2028 = 12 months. †
- l.141: 20 Jan + 3 days = 23 Jan 2025 (EO 14179 signing date, confirmed via the Federal Register API). †
- l.182: 24 Apr + 3 days = 27 Apr 2026 (minute order). †
- l.241: 23 Jun + 2 days = 25 Jun 2025 (Kadrey order filed 06/25/25). †
- Table 13.2: Art. 99(3) €35m/7%, 99(4) €15m/3%, 99(5) €7.5m/1%, Art. 101 €15m/3%, SMEs "lower". Consistent with the Act and with l.91.

**13.1–13.2 EU AI Act and omnibus**
- Reg. 2026/1744: dated 8 Jul, OJ 24 Jul, in force 27 Jul 2026; Annex III → 2 Dec 2027; Annex I → 2 Aug 2028; new bans from 2 Dec 2026 with "intended purpose"/"reasonably foreseeable" trigger; Art. 50(2) grace to 2 Dec 2026; sandboxes by 2 Aug 2027; machinery moved Section A → B; AI Office exclusive competence (Cuatrecasas; artificialintelligenceact.eu reproduction; Cooley 3 Aug 2026). †
- Omnibus Art. 4 "take measures to support"; Art. 4a; Art. 5(1)(ba)/(bb); Art. 75c(5) 5%; Art. 99(6a) "whichever is lower"; Art. 111(4); Art. 40(2) "without undue delay". †
- Art. 6(3) registration kept with a simplified procedure (Cooley, Van Eecke & Regenhardt). †
- EP approval 16 Jun 2026 (EP press release; 423–57–174) and Council adoption 29 Jun 2026 (Council voting result, 4188th meeting). Commission proposal 19 Nov 2025.
- GPAI guidelines published 18 Jul 2025; 10^23 FLOP indicative criterion; one-third compute test for modifiers; "significant change" (Commission page; WilmerHale/Orrick summaries).
- GPAI Code published 10 Jul 2025, three chapters; signatory list of 1 Aug 2025 with Anthropic, Google, Microsoft, Mistral, OpenAI; xAI safety chapter only; Meta did not sign (Commission page, 7 Oct 2026†; Euronews 1 Aug 2025).
- Epoch: 33 models ≥1e25 by June 2025, 12 developers, about 2 a month in 2024; frontier compute ~5×/yr. †
- FLI tracker: 9 member states with both authority types designated, June 2026. †
- Euronews 14 Oct 2026: Virkkunen "Our AI Office has started enforcing these rules" (Dublin summit); RFIs to OpenAI and Anthropic; incident wording; Scannell's research-exemption argument (re-read via WebFetch). No AI Office fine or formal finding reported by 22 Nov 2026 (TechRepublic, CSA research note).

**13.3 United States**
- EO 14110 signed 30 Oct 2023; "greater than 10^26 integer or floating-point operations" (govinfo FR text).
- EO 14148 signed 20 Jan 2025 (Federal Register API).
- EO 14179 signed 23 Jan 2025; "to sustain and enhance America's global AI dominance" (govinfo).
- AI Action Plan, July 2025: three pillars as described; funding not to go to "states with burdensome AI regulations" (White House PDF, p. 3).
- EO 14319 signed 23 Jul 2025: "Unbiased AI Principles", "Truth-seeking", "Ideological Neutrality", "shall not intentionally encode partisan or ideological judgments …", disclosure of "system prompt, specifications, evaluations" and avoiding disclosure of "model weights … where practicable" (govinfo).
- EO 14409: Treasury/NSA/CISA classified benchmark; NSA Director; 30 days; "mandatory governmental licensing, preclearance, or permitting requirement". EO 14434 of 29 Sept 2026. †
- Senate vote 1 Jul 2025, Blackburn Amdt. 2814, purpose "To strike the section relating to support for artificial intelligence", Record Vote 363, 99–1 (senate.gov roll call; congress.gov API).
- EO 14365 signed 11 Dec 2025: AI Litigation Task Force; Commerce evaluation within 90 days of "onerous" laws; BEAD conditions; legislative recommendation not to pre-empt child-safety laws; Colorado law "may even force AI models to produce false results" (govinfo).
- AG memo 9 Jan 2026, "sole responsibility", three grounds. †
- FRONTIER Act H.R. 9925: introduced 23 Jul 2026, 5 co-sponsors, thresholds, 72 h, Sec. 8, three covered subject areas, savings clauses †; still only referred as of 22 Nov 2026 (congress.gov API).
- TAKE IT DOWN Act, Public Law 119-12, 139 Stat. 55, 19 May 2025 (govinfo).
- AI Index 2026: state bills <10 (2020) → 150 (2025) †; US $285.9bn vs UK $5.9bn, UK ahead of France ($4.36bn) and Germany ($3.89bn), so "Europe's largest recipient" holds (AI Index 2026 ch. 4, Fig. 4.2.8).
- SB 53: signed 29 Sept 2025; >10^26 including fine-tuning/RL; >50 deaths or injuries or >$1bn in a single incident; 15 days / 24 h; >$500m revenue for large developers; AG only; $1m per violation (Governor release †; MoFo, Mayer Brown summaries).
- RAISE Act: signed 19 Dec 2025, chapter amendment 27 Mar 2026, effective 1 Jan 2027, 72 h, DFS office, $1m/$3m (Wiley; DWT). †
- California SB 813 and AB 1405 signed 9 Sept 2026 (Governor). †
- Texas HB 149: signed 22 Jun 2025 (IAPP), effective 1 Jan 2026; incitement, intent-to-discriminate and government social-scoring bans; "a disparate impact is not sufficient by itself to demonstrate an intent to discriminate"; AG exclusive authority; 60-day cure; 36-month sandbox (enrolled text).
- Colorado: xAI suit 9 Apr; DOJ intervention 24 Apr (equal protection); minute order 27 Apr; SB 26-189 signed 14 May 2026, details † (leg.colorado.gov; McDermott); case stayed, not dismissed, as of Nov 2026 (AI Challenge Watch; Norton Rose Fulbright).
- Midterms 3 Nov 2026: Democrats won both chambers (NPR/OPB 4 Nov 2026).

**13.4 China, UK, others**
- Algorithmic Recommendation Provisions in force 1 Mar 2022; Art. 17 opt-out wording; Art. 24 filing for providers "具有舆论属性或者社会动员能力" (CAC text).
- Labelling Measures in force 1 Sept 2025; explicit labels plus implicit metadata labels including provider name (Loeb & Loeb; China Law Translate; Allen & Gledhill).
- Cybersecurity Law amendment approved 28 Oct 2025, AI article on "safe and sound development of AI", effective 1 Jan 2026 (China Daily/Xinhua; Caixin).
- Anthropomorphic interactive services measures: five agencies (CAC, NDRC, MIIT, MPS, SAMR), published 10 Apr 2026, in force 15 Jul 2026; minors and older-user protection, security assessment, algorithm filing (Xinhua/网信中国).
- AI agents guidelines 8 May 2026; CAC, NDRC, MIIT; definition quote (gov.cn/Xinhua). See S5 on "first".
- No comprehensive AI law draft published by Nov 2026; legislative plans only (MLex; China Briefing). The "rather than one horizontal law" statement still holds.
- Global AI Governance Action Plan (July 2025): "an international public good"; open-source sharing; Global South capacity-building (fmprc.gov.cn).
- UK AI Opportunities Action Plan response: 47 "Agree", 2 "Partially agree", 1 consultation, so "accepted 47 of the 50" is right; AI Growth Zones (gov.uk, counted).
- AISI renamed 14 Feb 2025; "It will not focus on bias or freedom of speech" (gov.uk).
- King's Speech 13 May 2026, no AI bill; Labour 2024 manifesto pledge of "binding regulation on the handful of companies developing the most powerful AI models" (IAPP, 14 May 2026). No government AI bill introduced by 22 Nov 2026 (Bird & Bird tracker; searches).
- UK copyright report, March 2026, presented under s.136 DUA Act; "the majority of respondents rejected the originally preferred proposal"; "a broad copyright exception with opt-out is no longer the government's preferred way forward" (report PDF paras 25, 27).
- Korea AI Basic Act in force 22 Jan 2026; 30m won ≈ $21,000; one-year grace period (Cooley).
- Japan Act No. 53 of 2025; Art. 7 (responsibilities of businesses), Art. 16 (research and study), Strategic Headquarters (Japanese Law Translation).

**13.5 International**
- Bletchley 1–2 Nov 2023: 28 countries plus the EU (list counted); "serious, even catastrophic, harm" (gov.uk).
- Seoul: 16 companies, 4 added later = 20 (gov.uk).
- Paris statement: 63 countries + AU Commission + EU; US and UK absent (Élysée; see S4).
- India AI Impact Summit 16–20 Feb 2026, New Delhi; "People, Planet and Progress"; "the first global AI summit to be hosted in the Global South" (PIB backgrounder 21 Jan 2026; News On AIR).
- Next summit Geneva 2027, UAE 2028 (Swiss Federal Council; swissinfo).
- CoE CETS 225: opened 5 Sept 2024; Art. 30 entry-into-force rule; 21 signatories, one ratification (EU, 15 May 2026), not in force †; no new ratification found up to 22 Nov 2026 (CoE news; trackers).
- UN Res. 79/325 of 26 Aug 2025; Panel of 40; Geneva 2026 / New York 2027 (UN Panel FAQ); first Dialogue 6–7 Jul 2026, 163 countries, preliminary report †.
- LAWS resolution 79/62, 2 Dec 2024, 166–3–15; "open informal consultations", not negotiations (HRW).
- OECD Principles adopted 2019, updated May 2024, "47 adherents" (oecd.ai).
- HAIP reporting framework launched Feb 2025; first report on 20 organisations (oecd.ai/hiroshima).
- CEN-CENELEC acceleration package, Oct 2025, "available by Q4 2026" (CEN-CENELEC news 23 Oct 2025).
- Microsoft ISO/IEC 42001 certification covering Copilot services (Microsoft Learn).

**13.6 Copyright and personal data**
- Bartz order (ECF 231): "over seven million copies of books"; LibGen and PiLiMi; "many millions of dollars"; "exceedingly transformative and was a fair use"; "training schoolchildren to write well" (CourtListener PDF).
- Bartz final approval 20 Jul 2026: $1.5bn; 482,460 works; about $3,000; destruction of datasets †; notices sent early Sept 2026 (Authors Guild, 4/17 Sept 2026).
- Kadrey (ECF 598, filed 25 Jun 2025): thirteen authors; "no more than 50 words and punctuation marks"; "in most cases the answer will likely be yes"; market dilution; ruling "only affects the rights of these thirteen authors". Distribution/torrenting claim still pending, with summary-judgment hearing set for 25 Feb 2027 (CourtListener PDF; ChatGPT Is Eating the World 27 Mar 2026; TechTimes 21 Oct 2026).
- Thomson Reuters v. Ross opinion (29 Sept 2026): interlocutory, 2,243 headnotes, quotations, fn. 7. † (en banc: see S2).
- NYT/OpenAI MDL: no fair-use ruling as of 22 Nov 2026; cross-motions filed 4 Sept, replies due 20 Nov 2026 (trackers).
- UMG–Udio settlement 29/30 Oct 2025; WMG–Suno settlement 25 Nov 2025 (Bloomberg Law; MBW; SiliconANGLE).
- Thaler: decided 18 Mar 2025 (see M2 for the quotation); cert denied 2 Mar 2026 (SCOTUS docket 25-449; Holland & Knight).
- USCO Part 3 pre-publication version of 9 May 2025, still not finalised in Nov 2026 (copyright.gov AI page; commentary).
- Getty [2025] EWHC 2863 (Ch), handed down 4 Nov 2025, Joanna Smith J: "the model weights are not themselves an infringing copy and they do not store an infringing copy"; "does not store or reproduce any Copyright Works and nor has it ever done so"; "historic and extremely limited in scope" (National Archives). Permission-to-appeal quotation (IPKat) †.
- GEMA v OpenAI, LG München I, 11 Nov 2025: nine songwriters; "reproduzierbar … in den Sprachmodellen 4 und 4o … enthalten"; fixation in probability values irrelevant; § 44b covers corpus copies, not model copies (press release 11/2025). No appeal judgment reported.
- GEMA v Suno, 31 Jul 2026: six works; models v3.5 and v4; "nicht rechtskräftig" (press release 16/2026).
- LAION: LG Hamburg 27 Sept 2024 (§ 60d; ~6 billion pairs; no ruling on training); OLG 10 Dec 2025, 5 U 104/24 (§ 44b too; plain-language reservation not machine-readable; Revision to BGH allowed) (Hamburg press releases; heise).
- Garante 30 Mar 2023 order: "no legal basis underpinning the massive collection and processing of personal data"; €15m fine (decision 755 of 2 Nov 2024, announced 20 Dec 2024); Tribunal of Rome judgment 4153/2026, published 18 Mar 2026, upheld OpenAI's opposition (Garante pages).
- Papini (diritto.it): the DPC recognised OpenAI Ireland on 15 Feb 2024; the court did not rule on the merits.
- EDPB ChatGPT taskforce report (23 May 2024): "due to the probabilistic nature of the system … may also produce biased or made up outputs"; responsibility not to be shifted via the Terms and Conditions (PDF).
- EDPB Opinion 28/2024 adopted 17 Dec 2024 (see M3 for the quotations).
- EDPB Guidelines 03/2026 v1.0 adopted 7 Jul 2026 for consultation; "websites which clearly oppose the scraping" (EDPB PDF).
- Dutch AP Clearview fine €30,500,000; final decision 16 May 2024 (announced 3 Sept 2024); no legal basis and inadequate information (EDPB news).
- DPC: Meta paused in June 2024; training from 27 May 2025 after transparency notices and an easier objection form (DPC statement).

**13.7 Liability and debate**
- PLD 2024/2853 in force 8 Dec 2024; transposition by 9 Dec 2026; applies to products placed on the market after 8 Dec 2026; psychological harm; destruction or corruption of data; disclosure of evidence (Commission page).
- Bundestag adopted the German implementing law on Thursday 8 Oct 2026 (bundestag.de).
- AI Liability Directive: "06/10/2025 Proposal withdrawn by Commission" (OEIL).
- Garcia order (Doc. 115, May 2025): "not prepared to hold that Character A.I.'s output is speech"; product "rather than ideas or expressions within the app"; no Section 230 argument in the order (CourtListener PDF). Settlement reported 8 Jan 2026 (Decrypt).
- Raine: filed August 2025; OpenAI's answer (NBC News, 25 Nov 2025) invokes Section 230.
- Florida v. OpenAI filed 1 Jun 2026: product liability, negligence, deceptive practices (Bloomberg Law). At least eight more states sued on 15 Oct 2026; Florida is not among those listed (AP via Fox19).
- Draghi: "around 100 tech-focused laws and over 270 regulators active in digital networks"; AI Act threshold example; "only larger companies – which are often non-EU based" (report Part A PDF).
- Jia, Jin & Wagman, Marketing Science 2021 (Crossref).
- Janßen et al.: "exit of about a third of available apps … entry of new apps fell by half" (NBER w30028).
- Demirer et al.: storage −25%; cost of data +21%; "only a 0.1–0.6% rise in overall production costs" (NBER w32146); JPE online 18 Sept 2026, doi 10.1086/744118 (Crossref).
- FRI: GPT-5.6 Sol restricted in late June 2026; "does not appear to be the result of a binding directive" (FRI page).
- Hooker: "highly uncertain and rapidly changing" (arXiv abstract).

**Figures and tables**
- Fig 13.1 (figs_ch13.py): tier notes "Art. 5; since Feb 2025 / + deepfake, CSAM bans Dec 2026", "Annex III: Dec 2027; Annex I: Aug 2028", "Art. 50; from Aug 2026", GPAI "Art. 53; since Aug 2025", ">10^25 FLOP (presumed)", "Arts 51, 55". All consistent with the text and sources.
- Fig 13.2 (figs_ch13.py): all 29 events have correct month and year against the sources above (e.g. Japan Act Jun 2025, Korea Jan 2026, anthropomorphic Jul 2026, CoE opens Sep 2024, EU ratifies May 2026, UN Dialogue Jul 2026). Binding/non-binding encoding is correct.
- Table 13.1: all dates match Art. 113 (original and amended) †.
- Table 13.2: confirmed (see arithmetic).
- Table 13.3: confirmed against the AI Act, SB 53 and RAISE sources.
- Table 13.4: dates and holdings confirmed. Status column needs S1 and S2.
- Glossary (glossary-ch13.md, 23 entries): consistent with the text. No errors found.

**Bibliography (entries checked for existence and correct metadata, 78)**
europeanparliament2026regulation†, councileu2026proposal†, europeancommission2025generalpurpose, europeancommission2024liability, europeancommission2025gpaiguidelines, biden2023safe, trump2025initial, trump2025removing, trump2025preventing, trump2025ensuring, trump2026promoting†, whitehouse2025winning, uscongress2025samdt2814, uscongress2026frontier, uscongress2025tools, usdoj2026artificial†, texaslegislature2025hb149, cac2021provisions, xinhua2026five, govcn2026china, chinadaily2025china, mfa2025global, dsit2025tackling, dsit2025opportunities, dsit2026report, iapp2026kings, ukgov2023bletchley, dsit2024frontier, elysee2025statement, pib2026india, usdcnortherncal2025bartz, usdcnortherncal2025kadrey, usdcnortherncal2026bartz†, thirdcircuit2026thomson†, uscadc2025thaler, highcourt2025getty, lgmuenchen2025gema, lgmuenchen2026suno, lghamburg2024ki, olghamburg2025ki, garante2023intelligenza, garante2024chatgpt, papini2026openai, edpb2024report, edpb2024opinion, edpb2026guidelines, edpb2024dutch, dpc2025statement, europeanparliament2025procedure, bundestag2026produkthaftung, usdcmdfla2025garcia, vismaya2026google, yang2025openai, hendrix2025breaking, mekelburg2026florida, ap2026states, draghi2024future, jia2021short, janssen2022gdpr, demirer2024data, abbott2000hard, sajadieh2026ai (arXiv 2606.15708 exists, title and authors match), hooker2024limitations, heim2024training, sastry2024computing, cooley2026south, japan2025act, hrw2024killer, oecd2024principles, oecd2025hiroshima, cencenelec2025update, microsoft2026iso, rosenberg2026how, bertuzzi2026eus, authorsguild2026important, anthropicsettlement2026, fli2026national†.
Minor bib notes, none blocking: (a) garante2026tribunale uses the same URL as garante2024chatgpt (docweb 10085432). That is acceptable, because the note on the judgment is printed at the top of that page, but the title describes a separate "Note". (b) iapp2026kings is by Joe Jones (IAPP) and could carry his name. (c) The new entries edpb2024press (M3), authorsguild2026what (M1) and optionally the Burges Salmon note (S1) need adding.

## Tally
Claims checked against a web source: 205 (about 60 in round 1 and 145 in this round). Confirmed: 193. Wrong: 2 (Thaler quotation; Paris count incomplete). Outdated: 4 (Bartz payment timing; Getty appeal status; Ross en banc status; FRONTIER Act / midterms outlook). Unsupported by cited source: 2 (EDPB "very unlikely"/"duly anonymised" quotations; China agents "first"). Could not verify: 4 (all low risk; substance confirmed from secondary sources). Arithmetic items recomputed: 6 (errors: 0). Bib entries checked: 78 (problems: 0 substantive, 3 minor notes).
