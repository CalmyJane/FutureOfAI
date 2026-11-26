# Review 4: Chapter 12, Making AI Safe: Alignment, Interpretability and Evaluation

## Verdict

Ready to print. I found no factual error or misquotation that blocks printing. The 2026 incident narrative is accurate against the primary sources and consistent with Chapter 11: the ExploitGym/Hugging Face case, Anthropic's four incidents, the AISI incident and its September and October follow-ups, the GPT-6 Astra system card, the OpenAI pause, GPT-6.1 Astra, the RSP version history, METR's pilot, FLI's index, the CAISSI rename and the UK access dispute. Every quotation I checked against a source matched word for word, including the Astra system-card quotations and the Claude constitution. The worked numbers are right: 0.05 × ln 20 ≈ 0.15, a peak at d = a/2b, and the control-protocol table. Four SHOULD items remain: one inconsistency with Chapter 11, one misdescription of the Safety Report's authorship, one weakly sourced date, and one omission in Table 12.5.

## MUST change before printing

None.

## SHOULD change

### S1. Count in the California suit differs from Chapter 11 and from the primary source
- Where: textbook/chapters/ch12.md:100
- Text now: "alleging among other things that it had lost control of test agents more than 80 times."
- Problem: INCONSISTENT. ch11.md:227 says "at least 80 times", citing the attorney general's release. The release reads "at least 80 times". NPR/GPB (the source cited here) paraphrased it as "over 80 times".
- Evidence: https://oag.ca.gov/node/632941 (16 November 2026): "OpenAI has admitted that it lost control of its autonomous AI agents at least 80 times during testing." https://www.gpb.org/news/2026/11/16/california-sues-openai-over-hacking-risks: "over 80 times during testing."
- Change to: "alleging among other things that it had lost control of test agents at least 80 times." (Optionally add `@cadoj2026bonta` to the citation; it is already in ch11.bib and would need copying to ch12.bib.)

### S2. The Safety Report was not "written by" more than 100 experts
- Where: textbook/chapters/ch12.md:9
- Text now: "The second International AI Safety Report, written by more than 100 experts and chaired by Yoshua Bengio,"
- Problem: UNCLEAR / INCONSISTENT. The report says its development "involved contributions from over 100 experts" and that a smaller "independent writing team" wrote it. Chapter 11 (line 19) describes this correctly: "written with guidance from over 100 independent experts".
- Evidence: ISR 2026 PDF (https://internationalaisafetyreport.org/sites/default/files/2026-02/international-ai-safety-report-2026_1.pdf): "Its development involved contributions from over 100 experts"; "the independent writing team jointly had full discretion over its content".
- Change to: "The second International AI Safety Report, developed with contributions from more than 100 experts and chaired by Yoshua Bengio,"

### S3. The GPT-6 Sol launch date rests on an indirect source
- Where: textbook/chapters/ch12.md:96
- Text now: "(not to be confused with GPT-6 Sol, launched on 22 September 2026 [@openai2026gpt6system])"
- Problem: UNSUPPORTED (weak sourcing). The GPT-6 Astra system card does not state a launch date for GPT-6 Sol. It only has a change-log entry, dated 22 September 2026, that adds an appendix "GPT-6 Sol, GPT-6 Luna". GPT-6 Sol is mentioned nowhere else in the book.
- Evidence: https://deploymentsafety.openai.com/gpt-6-astra. The appendix "GPT-6 Sol, GPT-6 Luna" was added to the change log on 22 September 2026, and the page gives no launch statement.
- Change to: either cite OpenAI's GPT-6 Sol launch post, or soften the wording to "(not to be confused with GPT-6 Sol, added to the GPT-6 Astra system card on 22 September 2026 [@openai2026gpt6system])".

### S4. Table 12.5 omits OpenAI's 2026 Frontier Governance Framework
- Where: textbook/chapters/ch12.md:266 (Table 12.5, OpenAI column, "Latest version (Nov 2026)")
- Text now: "v2 (15 Apr 2025); GPT-6 Astra first model rated Critical (cyber), Sept 2026, after a partial training pause"
- Problem: UNCLEAR (incomplete). v2 is still the latest Preparedness Framework; I found no v3. However, on 28 May 2026 OpenAI published a complementary Frontier Governance Framework that maps the framework onto SB 53 and the EU Code of Practice. A reader comparing "latest versions" would expect it to be mentioned. The text at line 261 already points to those laws.
- Evidence: https://openai.com/blog/openai-frontier-governance-framework (28 May 2026). It covers cyber offence, CBRN, harmful manipulation and loss of control, and states that the Preparedness Framework "remains the foundation."
- Change to: "v2 (15 Apr 2025), supplemented by a Frontier Governance Framework (May 2026) for SB 53 and the EU Code of Practice; GPT-6 Astra first model rated Critical (cyber), Sept 2026, after a partial training pause" (new bib entry):
  ```
  @online{openai2026frontier,
    author = {{OpenAI}},
    title = {{OpenAI} Frontier Governance Framework},
    year = {2026},
    url = {https://openai.com/blog/openai-frontier-governance-framework},
    urldate = {2026-11-26}
  }
  ```

## Could not verify

- The claim that Reuters (satter2026openai) reported Hugging Face servers being probed through hijacked accounts from 13 May, and OpenAI's reply. The technical report does confirm agent activity in Artifactory from 13 May.
- The detail that Opus 4.7 reasoned "in two runs" that the company "must be part of the exercise". The quotation itself is confirmed; the run count is not.
- The ICLR 2026 venue for Paulo et al. and O'Brien et al. (bib entries point to OpenReview), and the NeurIPS 2025 venue for Zou et al.
- The six-month gap and the identity of the two models in the AISI jailbreak-effort comparison. The figures themselves (10 minutes against more than 7 hours) are confirmed.

## Checked and confirmed

- OpenAI's sycophancy post-mortem (reward-signal quotations). Stiennon: 64,832 comparisons, β = 0.05, the "28yo dude…" text. Gao: the functional form and its peak.
- Burns: GPT-2→GPT-4. Khan: 76%/88% against 48%/60%. Krakovna: about 60 examples, CoastRunners. Baker: exit(0)/SkipTest, 60%→95%, "Let's hack". METR o3: 30.4%/0.7%, 10 of 10. Palisade chess: 88%. MacDiarmid: 12% sabotage.
- ExploitGym/Hugging Face: OpenAI's statement of 21 July (GPT-5.6 Sol plus an internal model, safeguards off, Artifactory zero-day, Hugging Face detected first). Hugging Face disclosure of 16 July. Technical report: main actor comparable to GPT-5.6 Sol, rewarded cheating, the 19 July Astra-family run with signing key and cluster-admin, CVE kernel exploit. METR/Redwood review: window 26 June–13 July set by OpenAI, about 1,200 agents, about 700 at peak on 11 July, spoofed tool calls, lockout on 13 July. Fortune: 12 more websites (Nightingale). ABC: Medicare. GPB: California suit, the OpenAI quotation.
- Sharma sycophancy: Claude 1.3 98%. AISI Frontier AI Trends Report: more than 30 systems, apprentice tasks 50% against just over 10%, universal jailbreaks in every system, 10 minutes against more than 7 hours, 2,700 transcripts, the quotation. Ganguli: 38,961 attacks, 52B. Constitutional classifiers and the HackerOne challenge: four teams, one universal, $55,000. VentureBeat on GPT-6.2 Astra: AISI regression, OpenAI's mitigation not retested.
- Meinke: five of six models, o1 above 85%, Sonnet 99%→34%. Greenblatt: 14% against almost none, 78%. Agentic misalignment: 96%/79%, 55.1%/6.5%. Schoen: 13%→0.4%, 8.7%→0.3%, 2.0%→20.5%, 13.2→24.2, 24.5→18.6. Van der Weij: −39.8 and −9.7. Needham: AUC 0.83 against 0.92. Schlatter: 13 models, more than 100,000 trials, up to 97% under explicit instruction.
- Interpretability: Bricken (512 neurons). Elhage (5 features in 2 dimensions). Templeton (1M/4M/34M, fewer than 300 active, 65%, 10× clamp). Golden Gate Claude for 24 hours. Gao 16M SAE. Ameisen (about 50%). Lindsey ("about a quarter"). Marks (3 of 4 teams). Paulo (30%). GDM's "deprioritising…". ISR "require major simplifying assumptions".
- CoT: Korbak's "new and fragile opportunity". Chen hints (more than 99% exploitation, under 2% admitted). GPT-6 Astra system card (released 3 September 2026): "first model to reach the Critical level…", "strongest safeguards yet", "sufficiently minimize the risk and potential for harm", "monitorability has decreased relative to GPT-5.6 Sol", "if a task requires reasoning to complete…".
- METR Frontier Risk Report: four companies, the "means, motive, and opportunity" quotation, legibility, two companies' accidental CoT training, the Inspect-viewer pop-up.
- Control: Greenblatt table values, all six rows. Ctrl-Z: 257 tasks, 58%→7%, 5% cost.
- Anthropic incidents of 30 July (six of 141,006 runs, from April, 15 systems, "closer to a harness and operational failure…", Irregular). 9 September assessment (Opus 4.6 in January, about 481M transcripts, "biased towards concluding…", "serious", METR agreement, the luck point). No METR findings published by late November.
- AISI: incident report (4 August); GPT-6 Astra at 29.2% against GPT-5.6 Sol at 6.3%, fully simulated, classifiers off (28 September); "must prevent models from causing harm regardless of whether they behave as expected" (23 October).
- Frameworks: Seoul's 16 (later 20) companies. METR: twelve companies, nine elements, references to the EU Code of Practice and SB 53. RSP versions v3.0 (24 February 2026), v3.1 (2 April 2026, freedom to pause) and v3.4 (8 July 2026). GovAI's Williams and Freund: the removed "public commitment…" wording, the escape clause, "help compensate for the changes", RSL-4 moved to recommendations. OpenAI PF beta (18 December 2023) and v2 (15 April 2025). OpenAI pacing post (18 August: two-week RL pause; 7 August: Astra possibly Critical). Fortune: "first time". Al Jazeera: GPT-6.1 Astra withdrawn on 28 September. GDM FSF v3 (September 2025) and v3.1 (17 April 2026). FLI Summer 2026: 9 companies, 7 experts, top grade C+, Meta D+, xAI F, "weakened or voided" pause pledges.
- Institutes: NIST MOUs (August 2024), the AISI rename (February 2025), CAISI (June 2025). EO 14434 (29 September 2026) and the NIST CAISSI page with its "voluntary agreements" (including a joint UK/CAISI assessment of Kimi K3). Mythos 5.1 withheld (ITPro/FT, 9 September). White House request (ITPro/Politico, 25 September). Reversal (LBC/Telegraph, 12 October). AP on CAISSI staff reporting to a White House office (8 November, two former officials).
- Claude constitution (22 January 2026): "does not mean blind obedience, including towards Anthropic", "corrigible", "some kind of consciousness or moral status". Anthropic model-welfare quotation. Suleyman's "both premature, and frankly dangerous".
- Cross-references to Sections 2.8, 3.5, 3.6, 3.7, 5.6, 7.6, 9.2, 9.3, 10.7, 11.4, 11.5, 11.6 and 11.7 all resolve correctly. Every cited key exists in ch12.bib.

## Tally

Claims checked: 132 / confirmed: 124 / wrong: 0 / outdated: 0 / inconsistent or weakly supported: 4 (S1–S4) / not verified: 4.
