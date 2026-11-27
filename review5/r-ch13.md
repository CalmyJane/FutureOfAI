# Review 5: Chapter 13, Governing AI: Law, Policy and International Coordination

## Verdict
Ready to print after one small factual fix. The chapter is accurate, carefully attributed and well dated. Every 2026 development I could check against a source is right, including the Digital Omnibus dates and regulation number, Colorado SB 26-189, the Commerce export control on Anthropic's models, the FRONTIER Act, the 2026 midterms, the Third Circuit *Ross* ruling, the final approval in *Bartz*, the Council of Europe ratification count, the state suits against OpenAI, the denial of certiorari in *Thaler* and the revised Demirer figures. The worked FLOP example is correct. One number on the UK is wrong, and one sentence in the closing paragraph is hard to parse. Allegations against named companies are framed as allegations throughout, and I found nothing defamatory.

## MUST change before printing

### M1. UK response to the AI Opportunities Action Plan: wrong count
- Where: textbook/chapters/ch13.md:194
- Text now: "The government accepted 47 of the 50 recommendations in the *AI Opportunities Action Plan* by the entrepreneur Matt Clifford (January 2025)"
- Problem: VERIFIED WRONG. The government's own response (the cited source, @dsit2025opportunities) marks 48 recommendations "Agree" and two "Partially agree": Recommendation 13, the copyright-cleared British media dataset, and Recommendation 21, immigration routes for AI graduates. None is marked as rejected or as "consult". The figure 47 appears in one law-firm summary (Wiggin), which counted a recommendation that was subject to consultation separately. The primary document does not support that count.
- Evidence: https://www.gov.uk/government/publications/ai-opportunities-action-plan-government-response/ai-opportunities-action-plan-government-response (13 January 2025). I tallied the response column: 48 × "Agree", plus "Recommendation 13 … Partially agree." and "Recommendation 21 … Partially agree." Burges Salmon gives the same count: "Government agreed with 48 recommendations in its Response and partially agreed with two."
- Change to: "The government agreed to 48 of the 50 recommendations in the *AI Opportunities Action Plan* by the entrepreneur Matt Clifford (January 2025), and partially agreed to the other two, including "AI Growth Zones" with easier access to power and planning [@dsit2025ai; @dsit2025opportunities]."

## SHOULD change

### S1. Closing paragraph: sentence that misparses
- Where: textbook/chapters/ch13.md:306
- Text now: "with a federal frontier bill that would trade audits and incident reports for pre-emption that stalled in committee"
- Problem: UNCLEAR. As written, "that stalled in committee" seems to describe the pre-emption, not the bill. "Stalled" is also slightly stronger than the status given in Section 13.3. As of 17 September 2026 the bill had been referred to Energy and Commerce and had not had a hearing (Broadband Breakfast, 17 Sep 2026), which is consistent with line 150.
- Evidence: https://broadbandbreakfast.com/11-ai-bills-cleared-committee-this-summer-but-none-has-reached-the-house-floor/ (17 Sep 2026): "It was introduced July 23 and sits with the Energy and Commerce Committee … had not had a hearing."
- Change to: "and a federal frontier bill, which would trade audits and incident reports for pre-emption, had not left committee [@uscongress2026frontier]."

### S2. Omnibus legislative steps: add the signature date
- Where: textbook/chapters/ch13.md:52
- Text now: "The European Parliament approved the agreed text on 16 June 2026 [@councileu2026proposal] and the Council on 29 June, and it was published on 24 July"
- Problem: UNCLEAR (minor). The text is correct, but the regulation is formally "of 8 July 2026", the date of signature. Some readers who look up the instrument will see that date and wonder about the gap.
- Evidence: White & Case alert, July 2026: "Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026 … entered into force three days later, on 27 July 2026". Lewis Silkin (9 Jul 2026) cites the Council press release of 29 June 2026.
- Change to: "… and the Council on 29 June; it was signed on 8 July and published on 24 July"

## Could not verify
- The Getty v Stability Court of Appeal hearing dates of 11–12 November 2026 (line 250). Skeleton arguments dated October 2026 are on judiciary.uk, so the appeal was live, but I found no listing that confirms the exact dates.
- "petition for rehearing en banc pending (Nov 2026)" for *Thomson Reuters v. Ross* (Table 13.4). The prose does not mention this, and I found no independent report of it.
- The FLI tracker's count of "nine of the 27" member states that had designated both authorities by June 2026 (line 124).
- The Tribunal of Rome annulling the Garante's €15 million fine in March 2026, and the competence reasoning (line 274).
- The 6 October 2025 date for withdrawal of the AI Liability Directive (line 286), and the Bundestag's adoption of the PLD implementing law on 8 October 2026.
- The UN Global Dialogue in Geneva on 6–7 July 2026 with "163 countries" (line 216).
- The DOJ statement of interest of 1 September 2026 in the OpenAI MDL (line 242).
- The UK figure of $5.9 billion private AI investment in the 2026 AI Index. I found it only in secondary sources (the US figure of $285.9 billion is confirmed).

## Checked and confirmed
- Digital Omnibus: Regulation (EU) 2026/1744, Council adoption 29 June 2026, OJ 24 July, in force 27 July. Annex III high-risk moved to 2 Dec 2027 and Annex I to 2 Aug 2028. The 12- and 16-month deferrals are correctly computed.
- AI Act basics: OJ 12 July 2024, in force 1 Aug 2024, bans from 2 Feb 2025, GPAI duties from 2 Aug 2025. The provisions match the cited articles: Art. 5(3) 24-hour authorisation, Art. 6(3) profiling carve-out, Art. 10(3) quotation, Art. 27 FRIA scope, Art. 52 two-week notification, Art. 73 15 days, Art. 99 fine tiers.
- Commission GPAI guidelines of 18 July 2025 (10^23 FLOP; one-third of compute for fine-tuning). Code of Practice of 10 July 2025, with xAI signing only the safety chapter and Meta declining.
- FLOP box arithmetic: 6 × 10^11 × 1.5 × 10^13 = 9 × 10^24, and with 2 × 10^13 tokens it is 1.2 × 10^25.
- Euronews, 14 Oct 2026: Virkkunen at the Dublin summit, requests for information to OpenAI and Anthropic, "unauthorised access" to three outside organisations, and Scannell's view that the Act does not apply to testing.
- US executive orders: EO 14110 trigger at 10^26, revoked 20 Jan 2025. EO 14179 "global AI dominance". EO 14319 (Woke AI). EO 14365 of 11 Dec 2025. EO 14409 of 2 June 2026, including the classified benchmark, access of up to 30 days and the "mandatory governmental licensing, preclearance, or permitting" disclaimer.
- Commerce licence requirement for Claude Fable 5 and Mythos 5 from 12 June 2026, withdrawn on 30 June with commitments. This is consistent with Ch. 7.
- Senate vote of 99–1 on 1 July 2025. FRONTIER Act H.R. 9925 introduced 23 July 2026 by Obernolte with five co-sponsors. Democrats won both chambers on 3 Nov 2026.
- SB 53: signed 29 Sep 2025, in force 1 Jan 2026, 10^26, more than 50 people or $1 billion, 15 days or 24 h, $500m revenue, $1m penalty. RAISE Act signed 19 Dec 2025. Texas HB 149: signed 22 June 2025, in force 1 Jan 2026, 60-day cure period, 36-month sandbox.
- Colorado: SB 24-205 due to take effect 30 June 2026. xAI v. Weiser filed in April 2026. DOJ intervention on 24 April (Equal Protection). SB 26-189 signed 14 May 2026, enforced by the AG as a deceptive trade practice with no private right of action, duties from 1 Jan 2027.
- China: algorithm provisions from 1 Mar 2022, deep synthesis rules from 10 Jan 2023, generative AI measures from 15 Aug 2023 (seven agencies), labelling measures from 1 Sep 2025, Cybersecurity Law amendment in force 1 Jan 2026.
- UK: AISI renamed in Feb 2025 with the quotation "not focus on bias or freedom of speech". Data (Use and Access) Act Royal Assent 19 June 2025. The March 2026 copyright report dropped the opt-out as the preferred option.
- Korea: AI Basic Act enacted 21 Jan 2025, in force 22 Jan 2026, fines of 30 million won. Japan: Act No. 53 of 4 June 2025.
- Summits: Bletchley (28 countries plus the EU). Seoul (16 companies, later 20). Paris statement signed by 63 countries, the EU and the AU Commission (I counted the Élysée list), without the US or UK. India AI Impact Summit, Feb 2026.
- Council of Europe convention: opened 5 Sep 2024. 21 signatories after Albania signed on 15 June 2026. The EU ratified on 15 May 2026, and this is the only ratification.
- UN resolutions 78/265 and 79/325, the panel of 40 experts, and the 166–3 vote on lethal autonomous weapons in Dec 2024.
- *Bartz*: ruling of 23 June 2025 with the quotations; $1.5 bn settlement given final approval by Judge Martínez-Olguín on 20 July 2026; about 482,460 works. *Kadrey*: 25 June 2025, 13 authors, 50 words.
- *Thomson Reuters v. Ross*: Third Circuit, 29 Sep 2026, 2,243 headnotes, "minimally transformative, at best".
- UMG–Udio settlement (Oct 2025) and Warner–Suno settlement (Nov 2025). *Thaler*: D.C. Cir. 18 Mar 2025, cert denied 2 Mar 2026.
- *Getty v Stability* [2025] EWHC 2863 (Ch), 4 Nov 2025, with permission to appeal on the infringing-copy point. *GEMA v OpenAI*, 11 Nov 2025. *LAION*, Hamburg 27 Sep 2024.
- Garante order of 30 Mar 2023 and €15 m fine in Dec 2024. EDPB Opinion 28/2024. Clearview €30.5 m. Meta EU training from 27 May 2025.
- PLD 2024/2853: in force 8 Dec 2024, transposition by 9 Dec 2026.
- *Garcia*: ruling by Judge Conway in May 2025 and settlement in January 2026. Raine suit filed Aug 2025 and seven SMVLC suits in Nov 2025.
- Florida sued OpenAI on 1 June 2026 and eight states sued on 14 Oct 2026. With Texas and Oregon that makes eleven, as stated.
- Draghi report quotation. Janßen et al. ("about a third", entry halved). Demirer et al.: NBER revision of Oct 2026 gives 25%, 21% and 0.1–0.6%, matching the text.
- 2026 AI Index: US private AI investment of $285.9 bn.
- Cross-references to Section 4.1, Section 7.7, Section 11.6, Section 12.7 and Chapter 12 (Hugging Face and the Anthropic incidents) all point to matching content.

## Tally
Claims checked: 96 / confirmed: 85 / wrong: 1 / outdated: 0 / unclear: 2 / could not verify: 8
