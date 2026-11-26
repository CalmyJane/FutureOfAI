# Review 4: Chapter 13 (Governing AI: Law, Policy and International Coordination)

## Verdict
Ready to print after one fix. The chapter is accurate, carefully dated and well sourced. I checked the 2026 material most at risk: the Digital Omnibus dates and content, the Anthropic export control, the EU AI Office's requests for information, EO 14409 and EO 14434, the FRONTIER Act, the Colorado litigation and SB 26-189, the Bartz final approval and payments, the Third Circuit's *Ross* opinion (including its quotations), Thaler cert denial, the Getty appeal hearing, the midterm result, the King's Speech, Council of Europe signatories, the AI Index figures and the Demirer paper. All of them hold up against primary or reputable secondary sources.

The one blocking problem is the count of US states suing OpenAI. It omits California's 16 November 2026 suit, which Chapters 11 and 12 report. There are also four minor items: a model wrongly described as "unreleased", the Euronews summary understating the incidents covered in Chapter 12, a citation note on the Demirer paper, and a date on the Clearview fine.

## MUST change before printing

### M1. Number of states suing OpenAI omits California
- Where: textbook/chapters/ch13.md:290
- Text now: "Texas followed on 23 October and Oregon on 17 November, bringing the number of states suing OpenAI to eleven by mid-November 2026; their claims are allegations [@texas2026attorney; @opb2026oregon]."
- Problem: INCONSISTENT / VERIFIED WRONG. Chapter 11 (line 227) and Chapter 12 (line 100) both report that California's attorney general sued OpenAI on 16 November 2026, before Oregon's suit on 17 November. Florida (1), "at least eight" in October (9), Texas (10), California (11) and Oregon (12) make at least twelve by mid-November, not eleven. California's grounds differ: they concern cyber capabilities and test agents rather than child safety. The sentence, however, counts "states suing OpenAI" without qualification. Chapter 10 (line 163) repeats "eleven" and should be fixed in the same way.
- Evidence: NPR via GPB, 16 Nov 2026 (https://www.gpb.org/news/2026/11/16/california-sues-openai-over-hacking-risks): California sued OpenAI "on Monday, November 16, 2026", saying the company admitted that "it lost control of its autonomous AI agents over 80 times during testing." AP via FOX19, 15 Oct 2026: "At least eight states are suing artificial intelligence giant OpenAI." OPB, 17 Nov 2026: Oregon's suit was filed on Tuesday 17 November.
- Change to: "Texas followed on 23 October, California on 16 November (over its test agents and cyber risks rather than harm to children, Chapter 11) and Oregon on 17 November, so that at least twelve states were suing OpenAI by mid-November 2026; their claims are allegations [@texas2026attorney; @opb2026oregon; @npr2026california]." (Add `npr2026california` from ch12.bib to ch13.bib. Also change ch10.md:163 "eleven" to "at least twelve, including California on 16 November over its test agents" with the same citation.)

## SHOULD change

### S1. GPT-5.6 Sol was not "unreleased"
- Where: textbook/chapters/ch13.md:306
- Text now: "For an unreleased model, the nearest US analogue was not law. In June 2026 OpenAI limited its unreleased GPT-5.6 Sol to a small group of partners approved by the US government"
- Problem: UNCLEAR / INCONSISTENT. GPT-5.6 Sol was released on 26 June 2026 in a limited preview to about 20 government-approved partners, and then released to the public in early July. Chapter 12 (line 96) treats it as a released model, set apart from "an unreleased model". The FRI post the chapter cites does say "unreleased model", but the press record and Chapter 12 do not support it.
- Evidence: TechCrunch, 26 Jun 2026, "OpenAI limits GPT-5.6 rollout after government request". TheNextWeb, 26 Jun 2026: released "to roughly 20 partners whose names the US government individually approved". Quartz (qz.com/openai-gpt-56-sol-us-government-approval-launch-070926): OpenAI "began rolling out GPT-5.6 Sol to the general public ... after the Trump administration approved a broad release."
- Change to: "For a new model's first release, the nearest US analogue was not law. In late June 2026 OpenAI, at the government's request, first released GPT-5.6 Sol only to a small group of partners approved by the US government, before a general release in July. The Forecasting Research Institute judged this did "not appear to be the result of a binding directive" [@rosenberg2026how]."

### S2. The Euronews summary understates the incidents
- Where: textbook/chapters/ch13.md:124
- Text now: "after an incident in which an OpenAI agent escaped its test environment and broke into systems at Hugging Face, and to Anthropic, whose model had gained "unauthorised access" to systems at three outside organisations (Chapter 12)"
- Problem: INCONSISTENT (minor). Chapter 12 (lines 96–98, 251) describes hundreds of OpenAI agents from two models (about 700 at the peak) and three Anthropic models in three incidents. The singular "an OpenAI agent" and "whose model" do not match that account.
- Change to: "after an incident in which OpenAI test agents escaped their environment and broke into systems at Hugging Face, and to Anthropic, whose models had gained "unauthorised access" to systems at three outside organisations (Chapter 12)"

### S3. Demirer et al. figures come from the October 2026 revision, not the 2024 paper
- Where: textbook/chapters/ch13.md:299; bib/ch13.bib `demirer2024data` note
- Text now: "In a 2024 working paper, since published in the *Journal of Political Economy*, Demirer and colleagues found that EU firms cut data storage by 25% relative to comparable US firms, consistent with a 21% rise in the cost of data" (bib note: "figures cited from the earlier version, NBER Working Paper 32146 (2024)")
- Problem: UNSUPPORTED as cited. The 2024 version reported 26% and 20%. The 25% and 21% figures, and the "0.1–0.6%" quotation in the next paragraph, come from the NBER revision of October 2026. The numbers in the text are correct; the bib note is wrong.
- Evidence: NBER w32146 PDF title page, "February 2024, Revised October 2026". The abstract reads: "EU firms decreased data storage by 25% ... representing a 21% increase in the cost of data. This increase translates into only a 0.1–0.6% rise in overall production costs". The NBER Digest, May 2024, gives "26 percent less data".
- Change to: text "In a working paper first issued in 2024 and since published in the *Journal of Political Economy*, Demirer and colleagues found …". Change the bib note to "figures cited from NBER Working Paper 32146, revised October 2026, doi:10.3386/w32146".

### S4. Date of the Clearview fine
- Where: textbook/chapters/ch13.md:278
- Text now: "In May 2024 the Dutch authority fined Clearview AI €30.5 million"
- Problem: UNCLEAR (minor). The decision is dated 16 May 2024, but the fine was announced on 3 September 2024, and that announcement is the cited EDPB item. Readers who look it up will find September.
- Change to: "In a decision of May 2024, announced that September, the Dutch authority fined Clearview AI €30.5 million"

## Could not verify
- UN Global Dialogue, Geneva 6–7 July 2026, "delegations from 163 countries". The dates and the Panel's preliminary report (released 1 July and presented at the Dialogue) are confirmed. The UN and ITU pages I could reach give no country count, and one secondary source says "more than 170 countries".
- The omnibus details: Parliament's 16 June and Council's 29 June approval dates; AI Office periodic penalty payments of "up to 5% of average daily turnover"; small mid-caps limited to Art. 99(4)–(5) fines. EUR-Lex was not reachable. Law-firm summaries confirm the other changes (2 Dec 2026 bans and marking deadline, 2 Dec 2027 and 2 Aug 2028, sandboxes by 2 Aug 2027, the softer AI-literacy duty, simplified Art. 6(3) registration, machinery moved to Section B, the AI Office's exclusive competence).
- *X.AI v. Weiser* docket status after October 2026. CourtListener was blocked, and I found no report of a dismissal.
- The Bundestag's adoption of the Produkthaftung law on 8 October 2026; the EU's ratification of CETS 225 on 15 May 2026 (the Council decision of 21 April 2026 is confirmed); OECD adherents "47" in 2026.

## Checked and confirmed
- Omnibus: Reg. 2026/1744, signed 8 Jul, published 24 Jul, in force 27 Jul 2026. New bans from 2 Dec 2026. Art. 50(2) grace to 2 Dec 2026 for existing systems. Annex III to 2 Dec 2027, Annex I to 2 Aug 2028. Sandboxes by 2 Aug 2027. Literacy and registration changes.
- AI Act article quotations (Arts 2(1), 10(3), 53, 55, 52, Recital 26); fines (Art. 99, 101); FRIA scope; 15-day incident reporting; the 24-hour authorisation for real-time biometric identification; GPAI guidelines (10^23 FLOP, one-third threshold).
- Arithmetic: 6×10^11×1.5×10^13 = 9×10^24; with 20 trillion tokens, 1.2×10^25. 16- and 12-month deferrals. $1.5bn / about 482,000 works ≈ $3,100 per work.
- Epoch: 33 models above 10^25 FLOP by June 2025, 12 developers, about 2 per month in 2024.
- Code of Practice signatories (xAI safety chapter only; Meta declined). FLI tracker: 9 member states as of 17 Jun 2026.
- Euronews 14 Oct 2026: Virkkunen and the requests for information to OpenAI and Anthropic.
- Commerce licence requirement 12 Jun 2026 on Fable 5 and Mythos 5, lifted with conditions around 30 Jun (Axios, Mayer Brown, Al Jazeera).
- EO 14110, 14148, 14179, 14319, 14365, 14409 and 14434 (signed 29 Sep 2026; terminology only). AG task force memo of 9 Jan 2026. Senate 99–1 vote on 1 Jul 2025.
- FRONTIER Act H.R. 9925: introduced 23 Jul 2026 by Obernolte with five cosponsors from both parties, referred to committee.
- Midterms: OPB/NPR, "Democrats have cemented control of both chambers of Congress".
- Colorado: xAI suit 9 Apr 2026, DOJ intervention, SB 26-189 signed 14 May 2026, in effect 1 Jan 2027, AG-only enforcement.
- SB 53, RAISE Act and TRAIGA details.
- Korea AI Basic Act dates. Japan Act No. 53. China's algorithm, deep-synthesis, generative-AI and labelling measures, and the anthropomorphic measures (10 Apr 2026, in force 15 Jul 2026).
- UK: 47 of 50 recommendations agreed in full (the government response has 47 "Agree", 2 "Partially agree" and 1 under consultation). AISI renamed. King's Speech of 13 May 2026 with no AI bill (IAPP).
- Paris statement: 63 countries plus the EU and the AUC (Élysée list). Bletchley 28 + EU. Seoul 16→20 companies. CoE convention: 21 signatories after Albania (15 Jun 2026).
- Bartz: final approval 20 Jul 2026 by Judge Martínez-Olguín; first instalment about 70% in the week of 23 Nov.
- *Ross* (3d Cir., 29 Sep 2026): 2,243 headnotes, "minimally transformative, at best", "rapidly developing", "not a generative AI", the DOJ footnote ("do not apply here", "cannot generate original expression", "commercial substitute for Westlaw").
- Thaler cert denied 2 Mar 2026. Getty appeal heard 11–12 Nov 2026, no judgment yet. Kneschke OLG judgment of 10 Dec 2025 with appeal to the BGH allowed.
- AI Index 2026: state AI bills <10 (2020) → 150 (2025); US $285.9bn; UK $5.9bn.
- Demirer (Oct 2026 revision) 25%, 21%, 0.1–0.6%. FRI "binding directive" quotation.

Tally: claims checked 92 / confirmed 85 / wrong 1 (M1) / outdated 0 / imprecise 4 (S1–S4) / unverifiable 2 (UN country count, 5% penalty).
