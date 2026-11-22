# Third review: Chapter 13 — Governing AI: Law, Policy and International Coordination

STATUS: FIRST VERSION (work in progress, 11 Nov 2026). Full read of chapter, bib, and arithmetic done; web verification under way. Sections below are filled in as checks complete.

## Verdict
(pending completion of web checks)

## MUST change before printing
(pending)

## SHOULD change (real but not blocking)
(pending)

## Could not verify
(pending)

## Reader notes (from first read, before fact-checking)
1. ch13.md:5 — "Every rule below is therefore dated, with its status as of October 2026." The chapter then uses three different cut-offs: "As of 25 October 2026" (l.151), "As of 22 October 2026" (l.215), "as of October 2026" elsewhere. A reader cannot tell which is the real cut-off.
2. ch13.md:125 — the paragraph on enforcement drops two dramatic incidents (an OpenAI agent that "escaped a test environment and broken into systems at Hugging Face"; an Anthropic model that "gained unauthorised access to systems at three outside organisations") into a sentence about requests for information, with only "(Chapter 12)" as support and one Euronews citation. For a reader who has not just read Chapter 12 this is abrupt, and the statements are presented as fact about named companies.
3. ch13.md:125 — "Some lawyers argue that the Act's research exemption puts such testing beyond its reach." No source, no name; reads as filler.
4. ch13.md:21 and :221 — the standards story (requested May 2023, most delayed drafts aimed at Q4 2026) is told twice in nearly the same words.
5. ch13.md:106 and :119 — the Epoch count of models above 10^25 FLOP is given twice ("33 ... by June 2025" and "dozens ... by mid-2025").
6. ch13.md:159 — "California has since begun to build the independent checks these laws lack" sits inside the New York paragraph; SB 813 and AB 1405 are introduced in one sentence with no explanation of what they do for a developer.
7. ch13.md:243 — the Thomson Reuters paragraph is very dense (interlocutory appeal, statement of interest, footnote, consolidated New York cases) and the final sentence about the NYT suit is hard to parse.
8. ch13.md:307 — the closing paragraph is a long recap with 15 citations and four "developments to watch"; it reads as a list.
9. Table 13.1 row "AI in machinery" mixes a structural change into a table of dates; column headings ("Original date", "After omnibus") do not fit that row.
10. ch13.md:195 — "The UK's most consequential AI decision of 2026 concerned copyright" is asserted without support and the decision (a report that defers a decision) hardly fits "most consequential".

## Arithmetic recomputed (all correct)
- l.106: 6 × 1e11 × 1.5e13 = 9e24 FLOP (correct); with 2e13 tokens = 1.2e25 (correct); 1e26/1e25 = 10x; 1e25/1e23 = 100x (correct).
- Table 13.1 caption: 2 Aug 2026 -> 2 Dec 2027 = 16 months; 2 Aug 2027 -> 2 Aug 2028 = 12 months (correct).
- l.141: 20 Jan 2025 + 3 days = 23 Jan 2025 (EO 14179 date; correct).
- l.182: 24 April + 3 days = 27 April 2026 (to be confirmed against minute order).
- l.241: 23 June + 2 days = 25 June 2025 (Kadrey; correct).

## Checked and confirmed
(pending)

## Tally
(pending)

---
## INTERIM WORKING NOTES (to be folded into the sections above in the final version)

### Findings so far (11 Nov 2026)
- CANDIDATE SHOULD/MUST — ch13.md:238 "with first payments expected by mid-November": official settlement site still says "on or before November 15, 2026", but a joint stipulation of 23 Oct 2026 (Dkt. 694, reported by settlementinsight.com, updated 10 Nov 2026) moves the initial distribution to the week of 23 November; no payment confirmed as sent by 10 Nov. Suggested: "with first payments expected in the second half of November 2026".
- CANDIDATE SHOULD — ch13.md:251 "No appeal decision had been reported by October 2026" and :307 "how the Court of Appeal rules on Getty's 'infringing copy' point": still true, but the Court of Appeal heard Getty's appeal on 11 Nov 2026 (MLex, 11 Nov 2026). Could add "the appeal was heard in November 2026".
- CANDIDATE SHOULD — ch13.md:209 "signed by 63 countries and the EU": Élysée list has 63 countries plus the EU and the African Union Commission.
- CANDIDATE SHOULD — ch13.md:151/307 FRONTIER Act "still in committee": true; but 3 Nov 2026 midterms gave Democrats majorities in both chambers of the next Congress (Foley, 4 Nov 2026), and commentators expect pre-emption to stall; chapter contains no forward-looking midterm statement.

### Confirmed so far (source)
- Reg. (EU) 2026/1744: dated 8 July 2026, OJ 24 July 2026, in force 27 July 2026; Annex III -> 2 Dec 2027; Annex I -> 2 Aug 2028; new bans (intimate imagery, CSAM) from 2 Dec 2026, provider trigger "intended purpose" or "reasonably foreseeable and reproducible"; Art. 50(2) grace to 2 Dec 2026; sandbox by 2 Aug 2027; machinery moved Section A -> B; AI Office exclusive competence + exceptions (Cuatrecasas legal flash July 2026; artificialintelligenceact.eu omnibus reproduction; Cooley 3 Aug 2026).
- Omnibus Art. 4 "take measures to support"; Art. 4a; Art. 5(1)(ba)/(bb); Art. 75c(5) "shall not exceed 5 %"; Art. 99(6a) paras 4 and 5 "whichever is lower"; Art. 111(4); Art. 40(2) "without undue delay" (artificialintelligenceact.eu reproduction).
- Art. 6(3) registration kept with simplified procedure; proposal would have removed it (Cooley, Van Eecke & Regenhardt, 3 Aug 2026).
- Euronews 14 Oct 2026 (Bertuzzi): Virkkunen "Our AI Office has started enforcing these rules"; requests for information to OpenAI and Anthropic; incidents as described; lawyers' research-exemption argument (Barry Scannell, William Fry).
- FLI tracker: "9 Member States have designated both market surveillance and notifying authorities", last updated 17 June 2026.
- GPAI Code: published 10 July 2025; three chapters; signatories incl. Anthropic, Google, Microsoft, Mistral AI, OpenAI; xAI Safety and Security chapter only; Meta not listed (Commission page, last update 7 Oct 2026).
- Epoch: "over 30" models (33 listed) above 1e25 FLOP, 12 developers, June 2025, ~2/month in 2024; open-weights models among them (epoch.ai data insight). Epoch trends: frontier training compute 5x/year since 2020.
- FRONTIER Act H.R. 9925: introduced 23 July 2026, Obernolte + 5 cosponsors (Trahan, Houchin, Peters, Franklin, Subramanyam); referred to E&C and Science; large developer >$50m revenue and >=$1bn AI development spend; framework; annual audit; 72-hour incident report to Under Secretary; Sec. 8 suspension power; three covered subject areas; savings clauses (govinfo bill text).
- EO 14409 (2 June 2026): Treasury, NSA, CISA classified benchmark; NSA Director determines covered frontier models; "up to 30 days before they plan to release such models to other trusted partners"; no "mandatory governmental licensing, preclearance, or permitting requirement" (govinfo FR text).
- EO 14434 (29 Sept 2026) "Inaugurating the Era of Super Intelligence": terminology only (search results incl. whitehouse.gov, Wiley).
- AG memo 9 Jan 2026: "sole responsibility", three grounds (DOJ PDF, OCR text).
- Colorado: xAI suit 9 Apr 2026; DOJ 24 Apr; magistrate judge order 27 Apr (14 days after PI ruling); SB 26-189 signed 14 May 2026, repeals and reenacts, 30-day explanation, correction, human review, deceptive trade practice, no private right of action, 1 Jan 2027 (leg.colorado.gov; McDermott).
- RAISE Act: signed 19 Dec 2025; chapter amendment signed 27 Mar 2026; effective 1 Jan 2027; 72 hours; DFS office funded pro rata by large developers; $1m/$3m; >1e26; >$500m (Wiley; DWT).
- California SB 813 and AB 1405 signed 9 Sept 2026 (Governor press release).
- AI Index 2026: state AI bills "fewer than 10 in 2020 to 150 in 2025"; US $285.9bn; UK $5.9bn (PDF ch. 8 and ch. 4).
- CoE convention: 21 signatories, 1 ratification (EU, 15 May 2026), not in force (two secondary trackers dated 29 Sept and 13 Oct 2026; official table blocked).
- UN Global Dialogue: Geneva 6-7 July 2026, 163 countries, Panel "Preliminary Report" (un.org).
- Paris statement: 63 countries + EU + African Union Commission; US and UK absent (elysee.fr).
- Bartz final approval order 20 July 2026: $1.5bn; 482,460 works on Works List; "about $3,000, less costs and fees"; destruction of LibGen/PiLiMi files (order text). Notices 2-4 Sept 2026 (settlement site).
- Thomson Reuters v. Ross (3d Cir., filed 29 Sept 2026): interlocutory (s.1292(b)); 2,243 headnotes; all quotes verbatim; fn 7 DOJ statement of interest 1 Sept 2026 (opinion PDF).
- NYT/OpenAI MDL: no fair-use ruling as of 11 Nov 2026 (summary-judgment briefing in progress).
- Getty permission to appeal: IPKat 7 Jan 2026, quote verbatim.

### Continuation notes (22 Nov 2026)
- Bartz payments: Authors Guild page updated 20 Nov 2026: "first payments ... expected to go out during the week of November 23"; ~70% ($2,203.56) first instalment. -> MUST (l.238 outdated).
- Getty appeal: heard 11-12 Nov 2026 (Burges Salmon 12 Nov 2026 "second day"); no judgment by 22 Nov.
- Paris: Élysée list = 63 countries + African Union Commission + EU (counted).
- Midterms: Democrats won both chambers (NPR/OPB 4 Nov 2026). H.R. 9925 still only referred (congress.gov API, actions 23 Jul 2026). E&C chair signalled vote unlikely this year (Continental Currents).
- Thaler quote misses "eligible" (DC Cir. opinion p.: "requires all eligible work to be authored in the first instance by a human being").
- China agents doc: "first" not in cited Xinhua/gov.cn text; MLex and NYU Shanghai RITS call it first.
- Confirmed: anthropomorphic measures (5 depts, 10 Apr, 15 Jul 2026, security assessment, filing, minors/elderly); Cybersecurity Law amendment; GAIGAP "international public good"; India summit PIB; UK AOAP 47 agree/2 partial/1 consult; AISI 14 Feb 2025 quote; IAPP King's Speech 13 May 2026 + manifesto; UK copyright report para 27 quote; AI Action Plan "burdensome"; EO 14319, 14179, 14365 quotes (govinfo); Senate RCV 363 99-1; Texas HB 149; SB 53 (secondary); Colorado case stayed/open; Bartz 2025 quotes; Kadrey quotes & distribution claim pending (SJ hearing Feb 2027); NYT MDL no fair-use ruling (replies due 20 Nov 2026); Thaler cert denied 2 Mar 2026; USCO Part 3 still pre-publication; GEMA v OpenAI & v Suno press releases; LAION LG/OLG; UMG-Udio 29/30 Oct 2025; WMG-Suno 25 Nov 2025.
