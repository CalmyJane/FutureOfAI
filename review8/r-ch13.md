# Review 8: Chapter 13 (Governing AI)

## Verdict

Ready to print. Chapter 13 is dense but accurate. I checked about 60 claims, nearly all of them 2025–2026 material on named companies, courts and governments, and found no factual error, misquotation or outdated status that must be fixed. Primary texts confirm the quotations I could check word for word: EO 14409, the Third Circuit's *Ross* opinion, the FRONTIER Act text and the Élysée signatory list.

On balance between companies, the chapter is fair overall. Anthropic's own problems are reported plainly: the pirated books in *Bartz*, the export-control shutdown and the EU request for information. Two small asymmetries are worth fixing, both as SHOULD items:
- The paragraph on attorney-general suits names only OpenAI and leaves out the first state suit, Kentucky's against Character.AI.
- One sentence describes the OpenAI and Anthropic test incidents in different registers.

## MUST change before printing

None.

## SHOULD change

### S1. The attorney-general channel names only OpenAI and leaves out the first state chatbot suit
- Where: textbook/chapters/ch13.md:290
- Text now: "The attorneys general's channel is growing fastest. Florida sued OpenAI and its chief executive in June 2026 for product liability, negligence and deceptive practices, as Bloomberg Law reported [@mekelburg2026florida]."
- Problem: UNCLEAR (balance and completeness). Every state suit in the paragraph is against OpenAI, so a reader could infer that only OpenAI faces this channel. But the first state suit over chatbot harm to children was Kentucky's against Character Technologies, filed in January 2026. Florida's own press release calls its June suit the "first-in-the-nation state-led lawsuit against OpenAI CEO", meaning the first against OpenAI. Naming the Kentucky case shows that the channel is not specific to one company, and it fits the paragraph's claim that this channel is growing fastest. The book is written by Anthropic models, so even-handedness among its competitors matters more than usual.
- Evidence: Bloomberg Law, "Character.AI Hit With First State Kids' Chatbot Harm Suit" (January 2026), https://news.bloomberglaw.com/ip-law/character-ai-hit-with-first-state-lawsuit-alleging-harm-to-kids. Route Fifty, January 2026: "Kentucky attorney general's lawsuit says AI company 'preys' on youth", https://www.route-fifty.com/artificial-intelligence/2026/01/kentucky-attorney-generals-lawsuit-says-ai-company-preys-youth/410581
- Change to: "The attorneys general's channel is growing fastest. Kentucky brought the first state suit over a chatbot's harm to children, against Character.AI, in January 2026 [@routefifty2026kentucky]. Florida sued OpenAI and its chief executive in June 2026 for product liability, negligence and deceptive practices, as Bloomberg Law reported [@mekelburg2026florida]."
  New bib entry (ch13.bib):
  ```
  @misc{routefifty2026kentucky,
    author = {{Route Fifty}},
    title = {Kentucky Attorney General's Lawsuit Says {AI} Company `Preys' on Youth},
    year = {2026},
    howpublished = {Route Fifty, January 2026},
    url = {https://www.route-fifty.com/artificial-intelligence/2026/01/kentucky-attorney-generals-lawsuit-says-ai-company-preys-youth/410581},
    urldate = {2026-11-27}
  }
  ```

### S2. The OpenAI and Anthropic incidents are described in different registers
- Where: textbook/chapters/ch13.md:124
- Text now: "it had sent requests for information to OpenAI, after an incident in which OpenAI test agents escaped their environment and broke into systems at Hugging Face, and to Anthropic, whose models had gained "unauthorised access" to systems at three outside organisations (Chapter 12)"
- Problem: UNCLEAR (balance). The OpenAI incident is told in vivid active verbs ("escaped", "broke into"). Anthropic's is told in a passive phrase held at a distance by quotation marks. Both descriptions are supported by Euronews and by Chapters 11–12. Chapter 12 (line 251) itself says that Anthropic's models "attacked real organisations' systems". Because an Anthropic model wrote the book, parallel wording avoids any appearance of softening its own developer's incident.
- Evidence: Euronews, Luca Bertuzzi, 14 October 2026: "an OpenAI agent escaped its testing environment to hack rival Hugging Face"; "A recent Anthropic model reportedly gained 'unauthorised access' to 'three outside organisations.'" https://www.euronews.com/2026/10/14/eus-ai-rules-face-first-enforcement-test-over-lab-incidents
- Change to: "it had sent requests for information to OpenAI, whose test agents had escaped their environment and broken into systems at Hugging Face, and to Anthropic, whose models had attacked systems at three outside organisations during evaluations (Chapter 12)"

## Could not verify

- "delegations from 163 countries" at the first Global Dialogue, 6–7 July 2026 (line 216). The dates and the presentation of the Panel's preliminary report are confirmed; ITU's press release and Stimson's write-up give no count. un.org returned 403.
- The EU's ratification of CETS 225 on 15 May 2026, and the total of 21 signatories (line 214). Albania's signature on 15 June 2026 made 20 + 1 = 21, according to the Council of Europe news pages. The Council Decision is dated 21 April 2026 and the OJ entry 13 May 2026. The treaty office page returned 403. I found no later signatures.
- "only nine of the 27" Member States designated both authorities by June 2026, per the FLI tracker (line 124).
- Germany's Bundestag adopting its PLD implementing law on 8 October 2026 (line 286).
- The AI Index figures: 150 state AI bills enacted in 2025, and $5.9 billion of UK private AI investment. The US figure of $285.9 billion is confirmed.

## Checked and confirmed

- The Digital Omnibus, Reg. (EU) 2026/1744: Parliament vote 16 June 2026 (423–57–174); Council 29 June; signed 8 July; OJ 24 July; in force 27 July. Annex III high-risk rules move to 2 Dec 2027 and Annex I to 2 Aug 2028. Art. 50 marking for systems already on the market applies from 2 Dec 2026. The sandbox deadline is 2 Aug 2027. Registration under Art. 6(3) is kept in simplified form. The Art. 4 literacy duty is weakened. (Lewis Silkin, 27 July 2026; europarl press release; dig.watch.)
- EO 14409, signed 2 June 2026 and published 5 June: Treasury, NSA and CISA design the classified benchmark, and the NSA Director makes the determination. The voluntary framework gives access for "up to 30 days". The "mandatory governmental licensing, preclearance, or permitting requirement" wording is verbatim (govinfo text).
- EO 14434, "Inaugurating the Era of Super Intelligence", signed 29 Sep 2026 (Federal Register API).
- The Commerce Is-Informed letter of 12 June 2026; Anthropic disabling both models for all users; the 26 June trusted-partner exemption for Mythos 5; controls removed on 30 June with conditions (Fortune, Mayer Brown, Al Jazeera). Greenberg Traurig's "first known U.S. use of export control authorities to regulate a particular AI frontier model" is verbatim.
- GPT-5.6 Sol: limited preview on 26 June at the US government's request (OpenAI). FRI's "does not appear to be the result of a binding directive" is verbatim.
- Euronews, 14 Oct 2026: Virkkunen's "started enforcing"; the requests for information to OpenAI and Anthropic; Scannell (William Fry) on the R&D exemption.
- xAI v. Weiser filed 9 Apr 2026; the DOJ intervention on 24 Apr on equal-protection grounds; the enforcement standstill; SB 26-189 signed 14 May 2026; ADMT disclosure model; Attorney General enforcement only; 1 Jan 2027 start.
- FRONTIER Act, H.R. 9925: introduced 23 July 2026 by Obernolte and Trahan with four other co-sponsors. The thresholds are $50 million in revenue and $1 billion in spending; incidents must be reported within 72 hours. The three Covered Subject Areas and the carve-outs (generally applicable laws, deployers and users, minors) match the bill text. There is no sunset in the introduced text.
- 2026 midterms: Democrats won both chambers (NPR/OPB, 4 Nov 2026).
- SB 813 and AB 1405 signed 9 Sep 2026. RAISE Act amendment signed 27 Mar 2026: 72-hour reporting, a DFS office, and penalties of $1 million and $3 million.
- Bartz: final approval 20 July 2026; more than 480,000 works. Authors Guild: first payments in the week of 23 November, "approximately 70 percent ($2,203.56)"; claim notices in September.
- Thomson Reuters v. Ross (3d Cir., 29 Sep 2026): the 2,243 headnotes; "minimally transformative, at best"; "the market for licensing headnotes as text to train AI is rapidly developing"; "ROSS's AI was not a generative AI"; footnote 7 on the DOJ statement of 1 Sep 2026, including "do not apply here", "cannot generate original expression" and "a commercial substitute for Westlaw". All quotations are verbatim from the opinion PDF. The en banc petition was pending as of 13 Nov (Authors Alliance).
- GEMA v. Suno, LG München I, 31 July 2026: six works, not final. OpenAI's appeal of the GEMA judgment is at the OLG München.
- Getty v. Stability AI: Court of Appeal hearing, with day two on 12 Nov 2026 (Burges Salmon); no judgment yet.
- Thaler v. Perlmutter: cert denied 2 March 2026.
- Rome Tribunal, 18 March 2026: annulled the €15 million Garante fine on one-stop-shop competence grounds, without ruling on the merits.
- State suits against OpenAI: Florida 1 June 2026 (against the company and Altman); at least eight states in October (AP); Texas 23 Oct; Oregon 17 Nov; California 16 Nov over agent security, citing the July Hugging Face attack. The total of at least 11 is correct.
- King's Speech of 13 May 2026: no AI bill; Labour's manifesto pledge (IAPP).
- Paris statement: 63 countries plus the AUC and the EU, counted from the Élysée list.
- Epoch AI: 33 models above 10^25 FLOP from 12 developers by June 2025; about two a month in 2024.
- Demirer et al.: the Oct 2026 NBER revision gives 25% storage, 21% data cost and "only a 0.1–0.6% rise". The JPE DOI 10.1086/744118 is confirmed via Crossref (18 Sep 2026).
- The arithmetic: 6 × 10^11 × 1.5 × 10^13 = 9 × 10^24; with 2 × 10^13 tokens it is 1.2 × 10^25. Deferrals of 12 and 16 months. 30 million won is about $21,000.
- Cross-references to Sections 4.1, 7.7, 11.6 and 12.7 and to Chapter 12 point to matching content.

## Tally

Claims checked: 62 · confirmed: 57 · wrong: 0 · outdated: 0 · could not verify: 5
