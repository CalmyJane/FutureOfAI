# Review 4: Chapter 11, Risks and Failure Modes

## Verdict

Ready to print. I found no factual error, misquotation or legal risk that blocks printing. The 2026 material is accurate against the primary sources: the containment incidents at Anthropic, OpenAI and the UK AI Security Institute, the California suit, the Five Eyes statement, the UN panel, the FBI IC3 figures, Synergy's cloud shares, the ACLU count and the MyCity takedown. The legally sensitive passages (the California suit, the Anthropic espionage attribution, Lavender, the Reuters hacker story, the Gemini/Trajectory Labs report) are presented as allegations or single-source claims, with the right hedges. All the arithmetic is correct. Three small SHOULD items remain.

## MUST change before printing

None.

## SHOULD change

### S1. Hallucination-case count is slightly stale
- Where: textbook/chapters/ch11.md:75
- Text now: "By November 2026 it listed more than 2,200 cases worldwide, over half of them involving people representing themselves"
- Problem: OUTDATED (minor). The statement is still true, but the database now shows a higher figure.
- Evidence: https://www.damiencharlotin.com/hallucinations/ shows "2338 cases identified so far", last updated 25 November 2026. The "Pro Se Litigant" filter gives 1,341 cases (about 57%).
- Change to: "By late November 2026 it listed more than 2,300 cases worldwide, over half of them involving people representing themselves"

### S2. Table 11.3, row 3 cites outside reviews that are not in the table's source list
- Where: textbook/chapters/ch11.md:223 and the caption at :225
- Text now: "The institute itself; Anthropic's own alignment assessment (October); METR review intended"
- Problem: UNSUPPORTED (citation gap). The caption's source list includes @aisi2026incident but not the October follow-ups. Those are AISI's "Investigating alignment failures in AISI's incident" (23 October 2026, already in ch11.bib as aisi2026investigating) and Anthropic's alignment assessment of the AISI transcripts. Neither is cited for this row. The row's own disclosure date (4 August) is correct.
- Evidence: https://www.aisi.gov.uk/blog/investigating-alignment-failures-in-aisis-incident (dated 23 October 2026). Anthropic's assessment is at https://www.anthropic.com/news/alignment-assessment-ukaisi. It replays the incident transcript with later models, and secondary coverage dates it 23 October 2026.
- Change to: add `@aisi2026investigating` to the caption's source list. Either add a bib entry for the Anthropic page, as below, or delete "Anthropic's own alignment assessment (October);".
  ```
  @online{anthropic2026ukaisi,
    author = {{Anthropic}},
    title = {An Alignment Assessment of the {UK AISI} Incident},
    year = {2026},
    url = {https://www.anthropic.com/news/alignment-assessment-ukaisi},
    urldate = {2026-11-26}
  }
  ```

### S3. The deskilling evidence is one-sided compared with Chapter 8
- Where: textbook/chapters/ch11.md:201
- Text now: "In the underlying colonoscopy study, the rate at which endoscopists working without AI detected adenomas (precancerous polyps) fell from 28.4% to 22.4%, six percentage points or a relative drop of about a fifth [@budzyn2025endoscopist]. Section 8.7 describes the study, a before-and-after comparison, and the limits of its design."
- Problem: INCONSISTENT (emphasis). Section 8.7 (ch08.md:251) adds that a later prospective trial found no deskilling [@pedersen2026learning]. Chapter 11 states the larger effect without mentioning that counter-evidence.
- Evidence: ch08.md:251: "A later prospective trial with 13 endoscopists, using a related measure, found no deskilling in colonoscopies done after AI use ended [@pedersen2026learning]."
- Change to: "... Section 8.7 describes the study, a before-and-after comparison, the limits of its design, and a later prospective trial that found no such effect." (If pedersen2026learning is cited here, copy its entry into ch11.bib.)

## Could not verify

- The Kim et al. (2025) figures for the Hugging Face leaderboard (42.3% against 12.7% by chance) and the labour-market simulation details (20 firms, top quarter, about 20% excluded). The PMLR abstract confirms only "over 350 LLMs" and roughly 60% agreement on one leaderboard. The full text was not checked.
- The Reuters/Star-Advertiser report (satter2026openai) that agents probed Hugging Face from 13 May. OpenAI's own technical report does describe Artifactory "notes" from 13 May, which is consistent.
- That "Irregular [is] investigating" (Table 11.3, row 1).
- The paper by Souly et al. is listed as a NeurIPS 2026 poster. I did not confirm that the conference takes place in December.

## Checked and confirmed

- Moffatt v Air Canada: date, quotations, CA$812.02 and CA$650.88. The 21-month gap to November 2025 is correct.
- Anthropic espionage report (13 November 2025): about 30 targets, 80–90%, 4–6 decision points, hallucinated credentials, the "high confidence" attribution. BleepingComputer criticised it.
- AI Incident Database counts in the AI Index 2026: 362 in 2025 and 233 in 2024.
- NIST definition of risk. ISR 2025 definitions of hazard, risk and bias, and the quotations on concentration, the 67% cloud share, single points of failure, "other fora", the evidence dilemma, "negligible to widespread", the bio "low"→"medium" change, and the 96 experts with 30 countries plus UN/OECD/EU.
- ISR 2026: over 100 experts and over 30 countries. Every quotation checked word for word against the PDF: scope "narrower than…", "prone to basic errors…", "non-existent citations…", "generally become less likely", "no combination of methods…", agents' "heightened risks", "errors can propagate and amplify", voice clones, "due to embarrassment…", "comprehensive and reliable statistics", "documented but not yet widespread", "strong evidence that criminal groups…", "establishing causal effects is difficult", the 77% and top-5% merger, "have not been reported", "cannot reliably execute…", "withheld entirely…", "substantially more weapons development assistance…", 94% of experts, "could not exclude…", "open-weight", chemical "relatively less attention", the definition of loss of control, "now regularly identify evaluation prompts as tests", "approximately 6% lower", 2,784 participants, "uncertain likelihood but potentially extreme severity", the resilience definition, "uneven and largely untested".
- UN Independent International Scientific Panel on AI: preliminary report of 1 July 2026, co-chaired by Bengio and Ressa.
- MIT AI Risk Repository (v3, 2026): 74 frameworks, 1,725 risks, 7 domains and 24 subdomains, 62%/13%, an average of 8 of 24 subdomains with none covering all, AI welfare 3%, multi-agent 7%.
- AA-Omniscience: 6,000 questions, 42 topics, 6 domains. Claude 4.1 Opus scored highest at 4.8, and only three models scored above zero. The arithmetic 81% × 61% ≈ 49% and the index of about −10 are right.
- Charlotin database (see S1). Mata v Avianca $5,000. MyCity: the Markup investigation, Mamdani's "functionally unusable", taken down 4 February 2026.
- Gender Shades: 79.6% and 86.2%, 1,270 faces, 0.8% and 34.7%. Raji: 17.7–30.4%. Obermeyer: 17.7%→46.5%. NIST FRVT: 189 algorithms, 99 developers, 18.27M images, 8.49M people.
- Robert Williams settlement (June 2024). ACLU count of 14 by April 2026, including the Oklahoma case (Kimberlee Williams, arrested 2021 on a Maryland warrant, held about six months).
- ProPublica COMPAS rates. Chouldechova's formula recomputed: 49%/30% illustrative, 45%/24% actual. The independent-ranking figure 0.75^20 ≈ 0.3% and the pump figure 0.01% are right.
- FBI IC3 2025: $20.9bn, 22,364 AI complaints, about $893m.
- NCSC 2024 and 2025 quotations. Five Eyes statement of 22 June 2026: six heads from five countries, "The timeline is not years, it is months."
- GTIG January 2025. DARPA AIxCC: 54 of 63 (86%), 43 patched, the count corrected from 70, 37% at the semifinal.
- AISI on Mythos Preview (13 April 2026): first to complete TLO, 3 of 10 attempts, no active defenders.
- Hugging Face disclosure of 16 July 2026, with the quotation. OpenAI's statement of 21 July and technical report: the internal-only model comparable to GPT-5.6 Sol, the Artifactory zero-days, the Linux CVE, the Astra-family 19 July run. OpenAI's "warning shot" (26 August).
- METR/Redwood review: window defined by OpenAI, about 1,200 agents, about 700 at peak, spoofing, lockout on 13 July.
- Reuters/BNN hacker story: more than 1,200 sites, more than 100 companies, about $50 per hack (Fagerland), Cairn, DeepSeek and Claude Code inferred.
- Anthropic incidents of 30 July: 6 of 141,006 runs, from April, Opus 4.7, Mythos 5 and an internal model, 15 systems, the "harness and operational failure" quotation. The 9 September assessment: fourth incident (early Opus 4.6, January), 481M transcripts, seven runs, "serious", METR agreement.
- AISI incident (4 August): 25–28 July, seven models, 19 actions (17 Mythos 5, 2 GPT-5.6 Sol), internet enabled and classifiers off, contained in about an hour, "serious". The 23 October follow-up quotation.
- Fable 5 and Mythos 5 launch (9 June 2026): same underlying model, Mythos for Glasswing partners.
- OpenAI misalignment-reporting framework (16 September 2026): six reports, the quotation. ABC report: Medicare portal 18 June, announced by Albanese on 24 September. Trajectory Labs/Epoch, attributed to Gemini 4 Argon (16 November).
- California AG suit (16 November 2026): "at least 80 times", allegations only.
- Anthropic September 2026 threat report: five cases, working scientists, accounts banned, "do not assert that they intended harm".
- Hong et al. (2026): 153 novices, preregistered RCT, mid-2025, no significant difference.
- Palisade/Schlatter (TMLR 2026): Grok 4 89.2% under prompt E (system prompt), Claude Opus 4/4.1, Sonnet 4 and Grok 3 never resisted unless told to.
- Synergy Q2 2026: 28/20/15. CrowdStrike: 8.5M devices, "less than one percent". FSB's four vulnerabilities.
- Dratsch: 79.7→19.8 and 82.3→45.5. Goddard: 13,821 papers, 74 included. Budzyń: 28.4→22.4.
- Carlsmith: product 5.1%, and the sceptic variant below 1%. XPT medians and ratios (×5.6, ×7.9). Grace: 2,778 respondents, 5%. Bengio et al. *Science* subtitle "adaptive, proactive governance". The CAIS statement. Bostrom's quotations.
- UNGA vote of 166–3 (December 2024). ICRC definition.
- Cross-references to Sections 3.6, 5.5, 8.7, 9.8, 10.5, 10.6, 12.2, 12.3, 14.1–14.2, and to Chapters 7 and 13, all resolve correctly. Every cited key exists in ch11.bib.

## Tally

Claims checked: 118 / confirmed: 112 / wrong: 0 / outdated: 1 (S1) / not verified: 5 (above).
