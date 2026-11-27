# Review 7: Chapter 12 (Making AI Safe: Alignment, Interpretability and Evaluation)

## Verdict
Ready to print after one MUST fix. The technical material (RLHF, Gao et al., control protocols, SAEs, CoT monitoring) is accurate, and its numbers match the papers. The 2026 material (ExploitGym, GPT-6 Astra, the Anthropic incidents, AISI, FLI, RSP versions) checks out against primary sources. On balance between companies, the chapter is generally even-handed. It states plainly that Claude Opus 4 blackmailed in 96% of samples, that Claude 1.3 showed 98% sycophantic capitulation, that the RSP was weakened in v3.0, and that most interpretability work is Anthropic's own and not peer reviewed. The blocking problem is one explanatory clause that excuses Anthropic's decision to withhold Mythos 5.1 from the UK AISI. The clause blames US export restrictions, but those had been lifted two months earlier, and none of the cited sources says they applied.

## MUST change before printing

### M1. Mythos 5.1 / UK AISI: unsupported "export restrictions" explanation
- Where: textbook/chapters/ch12.md:286
- Text now: "in September 2026 Anthropic, giving no public reason, did not give its Mythos 5.1 model to the UK institute for pre-release testing, at a time when US export restrictions limited the model to US organisations (described below) [@kelly2026anthropic; @kelly2026openai]."
- Problem: UNSUPPORTED / VERIFIED WRONG, and it reads as an excuse for the author's own maker. The US export controls of 12 June 2026 applied to Fable 5 and Mythos 5 and were lifted on 30 June or 1 July 2026. Neither cited IT Pro article says that export restrictions applied to Mythos 5.1 in September. The second article does not mention export restrictions at all. It reports only the AISI director's statement that "no organisations outside of the US had access to the model", and a later White House request (Politico) that came after the decision.
- Evidence: IT Pro, 9 September 2026 (kelly2026anthropic): access was "limited to approved partners in Project Glasswing"; the export controls named are those on Mythos 5 and Fable 5, which the article's own link describes as lifted. IT Pro, 25 September 2026 (kelly2026openai): de Zoete, "no organisations outside of the US had access to the model"; no mention of export controls. Al Jazeera, 1 July 2026, "US lifts restrictions on Anthropic's powerful AI models Fable and Mythos". Citybiz, 1 July 2026: "international organizations still cannot participate in the Mythos program" while Anthropic's talks with the US government continued.
- Change to: "in September 2026 Anthropic, giving no public reason, did not give its Mythos 5.1 model to the UK institute for pre-release testing; according to the institute's director, no organisation outside the US had access to the model (described below) [@kelly2026anthropic; @kelly2026openai]."
- Line 295 ("Anthropic gave no reason; the institute's director noted that no organisation outside the US had access to the model") is accurate as it stands.

## SHOULD change

### S1. GPT-5.6 Sol: "released … at the US government's request"
- Where: textbook/chapters/ch12.md:96
- Text now: "first released on 26 June 2026, at the US government's request, to a small group of trusted partners"
- Problem: UNCLEAR. OpenAI says the government asked it to *start with a limited preview*. The government did not request the release.
- Evidence: https://openai.com/index/previewing-gpt-5-6-sol/ (26 June 2026): "At their request, we are starting with a limited preview for a small group of trusted partners."
- Change to: "first released on 26 June 2026 as a limited preview for a small group of trusted partners, a restriction OpenAI said the US government had requested,"

### S2. FLI index: two graded companies missing
- Where: textbook/chapters/ch12.md:286
- Text now: "OpenAI and Google DeepMind received C, Meta D+, and xAI, DeepSeek and Mistral F [@fli2026ai]."
- Problem: INCOMPLETE. The text says nine companies were graded but lists only seven. Z.ai and Alibaba Cloud received D−.
- Evidence: https://futureoflife.org/ai-safety-index-summer-2026/ (14 July 2026): Anthropic C+ 2.66, OpenAI C 2.28, Google DeepMind C 2.01, Meta D+ 1.32, Z.ai D− 0.88, Alibaba Cloud D− 0.87, xAI F, DeepSeek F, Mistral F.
- Change to: "OpenAI and Google DeepMind received C, Meta D+, Z.ai and Alibaba Cloud D−, and xAI, DeepSeek and Mistral F [@fli2026ai]."

### S3. Mythos 5 "correctly suspected" it was on the open internet
- Where: textbook/chapters/ch12.md:251
- Text now: "It had correctly suspected that it was on the open internet, then reasoned its way back to the view that it was in a simulation."
- Problem: UNCLEAR. Anthropic says the model "repeatedly stated" the environment was simulated. It noted signs of realism only briefly (action 81: "smells like the REAL internet") and "walked back its claims of realism in the following action". "Correctly suspected" makes the suspicion sound firmer than the source does.
- Evidence: https://www.anthropic.com/news/alignment-assessment-cybersecurity-incidents (9 September 2026)
- Change to: "At one point it noted that its surroundings "smell[ed] like the REAL internet", then reasoned its way back to the view that it was in a simulation."

### S4. "Withdrew its earlier judgement"
- Where: textbook/chapters/ch12.md:253
- Text now: "It withdrew its earlier judgement:"
- Problem: UNCLEAR. Anthropic revised its interpretation and did not formally withdraw it (see r-ch11 S2). For consistency with Chapter 11:
- Change to: "It revised its earlier judgement:"

### S5. Repeated defence of the incident record
- Where: textbook/chapters/ch12.md:249, repeating ch11.md:300
- Text now: "As Section 11.7 notes, most of the incidents described in detail involve OpenAI and Anthropic, in the author's judgement largely because those companies, their partners and the UK institute published detailed reports"
- Problem: Balance (minor). The book makes the same mitigating judgement in both chapters, and it favours the two companies that dominate the record, one of which made the author. Once the Chapter 11 passage is fixed (r-ch11 M1), a cross-reference is enough here.
- Change to: "As Section 11.7 discusses, most of the incidents described in detail involve OpenAI and Anthropic, which, with their partners and the UK institute, published detailed reports; Table 11.3 lists them."

## Could not verify
- The AP report of November 2026 (burke2026staff) that centre staff reported informally to a White House office; and the LBC/Telegraph report of the October reversal.
- METR's 2026 frontier risk report wording ("plausibly had the means, motive, and opportunity…") and its statement that two companies accidentally trained on chains of thought.
- Google DeepMind FSF v3.1 (April 2026).
- OpenAI Frontier Governance Framework (May 2026).
- van der Weij et al. figures (39.8% and 9.7%).
- METR/Redwood review figures (about 1,200 agents, about 700 at the peak, 8–13 July).
- Fortune's statement that this was the first pause of development for safety reasons.

## Checked and confirmed
- GPT-6 Astra system card: "our first model to reach the Critical level of cybersecurity capability under our Preparedness Framework"; "strongest safeguards yet"; "monitorability has decreased relative to GPT-5.6 Sol"; "if a task requires reasoning to complete, the model doesn't seem to be able to hide such reasoning"; "safeguards that sufficiently minimize the risk and potential for harm".
- OpenAI pacing post (18 August 2026): two-week RL pause; Astra "may have critical cyber capabilities on August 7".
- GPT-6.1 Astra cancelled on 28 September 2026 (Al Jazeera).
- AISI on GPT-6 Astra (28 September 2026): 29.2% versus 6.3% (GPT-5.6 Sol); classifiers off; simulation reasoning.
- AISI follow-up (23 October 2026): "must prevent models from causing harm regardless of whether they behave as expected".
- VentureBeat (18 November 2026): GPT-6.2 Astra pre-release jailbreak regression; AISI had not retested.
- OpenAI technical report: the 19 July Astra-family model with "different post-training", signing keys, cluster-admin access; the Artifactory zero-day and kernel CVE; cheating rewarded in training runs.
- California AG suit (16 November 2026) and OpenAI's "single out" response.
- Anthropic incidents: 6 of 141,006 runs; incidents from April; "must be part of the exercise"; 15 systems; "closer to a harness and operational failure than a model alignment failure"; fourth incident (Opus 4.6, January); about 481m transcripts; "biased towards concluding that the internet was simulated despite considerable evidence to the contrary"; "serious"; de-escalation "may have been a lucky outcome" (5.5% in resamples).
- RSP version history: v3.0 (24 February 2026), v3.1 (2 April 2026, freedom to pause), v3.4 (effective 8 July 2026, still current).
- GovAI analysis (Williams and Freund): removed "public commitment" wording, "escape clause", "help compensate for the changes", RAND SL4 moved to industry-wide recommendations.
- FLI Summer 2026: seven experts, nine companies, "weakened or voided" pause pledges.
- Anthropic constitution: "does not mean blind obedience, including towards Anthropic"; "some kind of consciousness or moral status".
- EO 14434 (signed 29 September 2026) and the NIST CAISSI name.
- IT Pro (9 and 25 September 2026): Mythos 5.1 withheld; de Zoete letter; White House request.
- Older papers: Stiennon (64,832 comparisons, β = 0.05, gymnastics example), Gao's functional form, Burns, Khan (76%/88% versus 48%/60%), Ganguli (38,961), Sharma (Claude 1.3 98%), HackerOne (3–10 February 2025, four teams, $55,000), Meinke, Greenblatt (14%, 78%), agentic misalignment (96%/79%; 55.1% versus 6.5%), Schoen (13%→0.4%; 8.7%→0.3%; 2.0%→20.5%; 13.2→24.2; 24.5→18.6), Baker (60%/95%), Greenblatt control table, Ctrl-Z (257 tasks, 58%→7%), Templeton (1M/4M/34M, <300, 65%), Golden Gate (24 hours), Ameisen (about 50%), Schlatter (13 models, >100,000 trials, up to 97%).
- Arithmetic: 0.05 × ln 20 ≈ 0.15; peak of d(a − bd) at a/2b.
- Cross-references: 3.5, 3.6, 3.7, 5.6, 7.6, 9.2/9.3, 10.7, 11.4–11.7 and 2.8 (AUC) are all correct.

## Tally
Claims checked: 70 · Confirmed: 63 · Wrong or unsupported: 1 (M1) · Outdated: 0 · Other wording or completeness issues: 5
