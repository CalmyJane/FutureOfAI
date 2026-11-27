# Review 6: Chapter 13, Governing AI: Law, Policy and International Coordination

## Verdict

Ready to print after one fix. This is a careful, well-sourced chapter. Almost every 2025–2026 legal and policy claim I checked held up against primary or reputable secondary sources: the Digital Omnibus dates, the Bartz final approval, the Third Circuit's *Ross* ruling, the 2026 midterm result, the state suits against OpenAI, the FRONTIER Act, SB 813/AB 1405, GEMA v Suno, Thaler cert denial, the Paris count and the Global Dialogue. It also stays measured towards named companies and labels allegations as allegations. One sentence about the UK's response to the Clifford plan misstates which recommendations were only partially agreed. The remaining items are precision fixes.

## MUST change before printing

### M1. AI Growth Zones were not one of the two "partially agreed" recommendations
- Where: textbook/chapters/ch13.md:194
- Text now: "The government agreed to 48 of the 50 recommendations in the *AI Opportunities Action Plan* by the entrepreneur Matt Clifford (January 2025), and partially agreed to the other two, including "AI Growth Zones" with easier access to power and planning [@dsit2025ai; @dsit2025opportunities]."
- Problem: VERIFIED WRONG / MISLEADING. Read naturally, "including" attaches to "the other two", so the sentence says AI Growth Zones were partially agreed. Law-firm summaries of the government response say the two partial agreements were (1) exploring how the immigration system could attract top AI graduates and (2) a copyright-cleared British media training dataset, which DCMS and DSIT would consult on separately. AI Growth Zones were agreed in full and became flagship policy.
- Evidence: Burges Salmon, "UK AI Opportunities Action Plan and government response published" (Jan 2025): "the government has agreed to 48 of the 50 practical recommendations and partially agreed to two", including "establish a copyright-cleared British media asset training data set (for which government partially agrees as DCMS and DSIT will consult separately)" (https://www.burges-salmon.com/articles/102jtpd/uk-ai-opportunities-action-plan-and-government-response-published). BCS summary: "The government partially agreed with the recommendation to explore how the existing immigration system can be used to attract graduates..." (https://www.bcs.org/articles-opinion-and-research/ai-opportunities-action-plan-a-summary/).
- Change to: "The government agreed to 48 of the 50 recommendations in the *AI Opportunities Action Plan* by the entrepreneur Matt Clifford (January 2025), among them "AI Growth Zones" with easier access to power and planning, and partially agreed to the other two [@dsit2025ai; @dsit2025opportunities]."

## SHOULD change

### S1. GPT-5.6 Sol partners were "shared with", not "approved by", the government
- Where: textbook/chapters/ch13.md:306
- Text now: "On 26 June 2026 OpenAI, at the government's request, first released GPT-5.6 Sol only to a small group of partners approved by the US government, before a general release from 9 July"
- Problem: UNSUPPORTED (overstatement). OpenAI's post confirms the request but describes the partners only as ones "whose participation has been shared with the government". It does not say the government approved them. This borders on misleading, because it makes the government look like a gatekeeper.
- Evidence: OpenAI, "Previewing GPT-5.6 Sol", 26 June 2026: "At their request, we are starting with a limited preview for a small group of trusted partners whose participation has been shared with the government" (https://openai.com/index/previewing-gpt-5-6-sol/).
- Change to: "...first released GPT-5.6 Sol only to a small group of trusted partners whose participation it had shared with the US government, before a general release from 9 July"

### S2. GEMA v OpenAI is under appeal
- Where: textbook/chapters/ch13.md:252 and Table 13.4 (line 265)
- Text now: "Neither judgment was final." / "First instance, not final"
- Problem: OUTDATED (minor). OpenAI has appealed the November 2025 judgment to the Higher Regional Court of Munich (OLG München). Saying so is more informative and parallels the Getty row.
- Evidence: Coverage of the Suno judgment of 31 July 2026 (e.g. LTO, beck-aktuell, https://www.beck-aktuell.de/heute-im-recht/rechtsprechung/lg-muenchen-i-42O76325-ki-generator-suno-urheberrechte-verletzt-gema-2026-07-31) notes that the same chamber ruled against OpenAI in November 2025 and that OpenAI has appealed to the OLG München.
- Change to (table): "First instance; OpenAI appeal pending at Higher Regional Court, Munich"

### S3. Bartz: per-work figure and first instalment
- Where: textbook/chapters/ch13.md:237
- Text now: "about $3,000 per work before costs and fees ... a first instalment of about 70 per cent of the per-work amount"
- Problem: UNCLEAR (minor). The Authors Guild page gives the first instalment as $2,203.56, "approximately 70 percent". That implies a net per-work amount of about $3,150 after the reduced fee award. The text is not wrong, but the gross and net figures are mixed. The Guild also says payments were "expected to go out during the week of November 23", which can be stated more firmly now.
- Evidence: Authors Guild, updated 20 Nov 2026: "Only approximately 70 percent ($2,203.56) will be paid out now"; "440,490 of the 482,460 eligible works were claimed" (https://authorsguild.org/advocacy/artificial-intelligence/what-authors-need-to-know-about-the-anthropic-settlement/).
- Change to: "...a first instalment of about $2,200 per work (roughly 70 per cent of the net amount) was due to be paid in the week of 23 November 2026"

## Could not verify
- Anthropomorphic-AI interim measures (April 2026, in force 15 July 2026) and the 8 May 2026 AI-agent guidelines (Xinhua, gov.cn). Not checked.
- Council of Europe convention "21 signatories" as of November 2026. The CoE reported 21 after Albania signed on 15 June 2026. I could not confirm that no later signature or ratification occurred (coe.int returned 403).
- FLI tracker: "nine of the 27" member states by June 2026.
- Colorado magistrate's minute order (27 April 2026) and SB 26-189 signature on 14 May 2026. I confirmed DOJ's 24 April intervention and its equal-protection theory, but not the docket entries.
- EO 14409 details (classified cyber benchmark; 30-day voluntary access).

## Checked and confirmed
- Digital Omnibus: Reg. (EU) 2026/1744, published 24 July 2026, in force 27 July 2026. Annex III moved to 2 Dec 2027 and Annex I to 2 Aug 2028. New bans apply from 2 Dec 2026. Art. 50 marking for legacy systems by 2 Dec 2026. Sandboxes by 2 Aug 2027. AI-literacy duty softened. Art. 6(3) registration kept but simplified. Machinery handled through its own regulation (Lewis Silkin; White & Case; Cuatrecasas).
- Table 13.1 arithmetic: deferrals of 16 months (Annex III) and 12 months (Annex I) are correct.
- 10^25 FLOP worked example: 6 × 10^11 × 1.5 × 10^13 = 9 × 10^24; with 2 × 10^13 tokens it is 1.2 × 10^25. Correct.
- Euronews (14 Oct 2026): Virkkunen said "Our AI Office has started enforcing these rules". There were RFIs to OpenAI and Anthropic, the Hugging Face escape, Anthropic "unauthorised access" at three organisations, and Scannell (William Fry) on development and testing.
- 2026 midterms: Democrats won both chambers.
- FRONTIER Act H.R. 9925: introduced 23 July 2026 by Obernolte with five bipartisan co-sponsors; 72-hour incident reporting.
- SB 813 and AB 1405 signed 9 Sept 2026.
- Florida (June 2026), eight states (14 Oct 2026), Texas and Oregon suits; the count of eleven is consistent.
- Bartz final approval on 20 July 2026 by Judge Martínez-Olguín, after Alsup retired. 482,460 works.
- *Thomson Reuters v. Ross*, 3d Cir., 29 Sept 2026: 2,243 headnotes, "minimally transformative, at best", developing licensing market, non-generative framing. The en banc petition is pending (Authors Alliance, 13 Nov 2026).
- *Kadrey*: "in most cases the answer will likely be yes", 13 authors, 25 June 2025.
- *Thaler*: cert denied 2 March 2026.
- GEMA v Suno: LG München I, 31 July 2026, 42 O 763/25, largely for GEMA, not final.
- Getty appeal heard in Nov 2026 (IPKat guest post; Burges Salmon).
- Paris statement: 63 countries plus the AU Commission and the EU (Élysée list).
- UN Global Dialogue: Geneva, 6–7 July 2026; "Delegations from 163 countries"; Panel preliminary report of 1 July 2026; 40 members.
- CoE convention: EU ratification in May 2026 was the first party; 21 signatories as of June 2026.
- Demirer et al.: 25% storage, 21% cost of data, "only a 0.1–0.6% rise".
- AI Index 2026: US $285.9bn; UK $5.9bn is the largest European figure.
- Commerce IIL of 12 June 2026 on Fable 5 and Mythos 5; Anthropic disabled the models for all users (Mayer Brown, GT Law).
- EO 14110 trigger quote, EO 14179 quote, EO 14319 quote, Senate 99–1 on 1 July 2025, EO 14365 Colorado quote, SB 53 thresholds and deadlines, Texas HB 149 quote, Korea fine of 30m won (about $21k).
- Not rechecked here because they are long-established: Art. 5 list, Art. 99/101 fines, Bletchley, Seoul and Hiroshima details.

## Tally
Claims checked: 72 · Confirmed: 66 · Wrong/misleading: 2 (M1, S1) · Outdated: 1 (S2) · Unclear: 1 (S3) · Could not verify: 5 groups
