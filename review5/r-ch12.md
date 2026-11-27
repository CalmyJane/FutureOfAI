# Review 5: Chapter 12, Making AI Safe

## Verdict
Ready to print. There are no MUST items, and the six SHOULD items are recommended. Every 2026 claim I checked matches its source. That covers the GPT-6 Astra system card quotes, the OpenAI pacing post, the AISI GPT-6 Astra simulation figures, the METR pilot, the RSP version history, the GovAI quotes, the FLI Summer 2026 grades, the GPT-6.1 Astra cancellation, the CAISSI rename and EO 14434, the Mythos 5.1 withholding and its reversal, the AP CAISSI report, and VentureBeat on GPT-6.2 Astra. The worked examples are correct (KL penalty 0.05 × ln 20 ≈ 0.15; peak at d = a/2b).

The main concern is balance between companies. The chapter's opening hook, its one case box and its closing summary all use OpenAI failures. Its scepticism about self-assessment is applied repeatedly to OpenAI's Astra decision but not to Anthropic's equivalent decisions. The text does disclose that much of the interpretability evidence is Anthropic's own and unreviewed, and it reports Anthropic's incidents frankly. The asymmetries below are small, but in a book written by Anthropic models they are worth removing.

## MUST change before printing
None.

## SHOULD change

### S1. GPT-5.6 Sol preview partners were not "approved by the US government"
- Where: textbook/chapters/ch12.md:96
- Text now: "first released on 26 June 2026 to a small group of partners approved by the US government"
- Problem: MISQUOTED (minor). OpenAI's post says the preview was for "a small group of trusted partners whose participation has been shared with the government", done at the government's request. That does not say the government approved them.
- Evidence: https://openai.com/index/previewing-gpt-5-6-sol/ (26 June 2026).
- Change to: "first released on 26 June 2026, at the US government's request, to a small group of trusted partners whose participation had been shared with the government"

### S2. FLI grades: xAI singled out, and the lowest scorers omitted
- Where: textbook/chapters/ch12.md:286
- Text now: "graded nine companies and gave none a grade above C+; Meta received D+ and xAI F"
- Problem: UNCLEAR / balance. Three companies received F: xAI (0.65), DeepSeek (0.47) and Mistral (0.33). Naming only xAI implies it was the worst. The text also omits that the C+ was Anthropic's. Omitting that is modest, but readers may wonder.
- Evidence: https://futureoflife.org/ai-safety-index-summer-2026/: "Anthropic C+ (2.66) … OpenAI C (2.28) … Google DeepMind C (2.01) … Meta D+ (1.32) … xAI F (0.65), DeepSeek F (0.47), Mistral F (0.33)".
- Change to: "graded nine companies and gave none a grade above C+ (Anthropic's); OpenAI and Google DeepMind received C, Meta D+, and xAI, DeepSeek and Mistral F"

### S3. The disclosure explanation is stated as fact, and the OpenAI case did not begin with OpenAI's disclosure
- Where: textbook/chapters/ch12.md:249
- Text now: "As Section 11.7 notes, most of these incidents involve OpenAI and Anthropic largely because those two companies published detailed reports; Table 11.3 lists them."
- Problem: UNSUPPORTED / INCONSISTENT. Section 11.7 presents this as "In the author's judgement". Here it becomes fact. Hugging Face disclosed first (16 July), five days before OpenAI (21 July). Australia's government made the Medicare case public, and the California AG says OpenAI "has not answered" its questions.
- Evidence: Hugging Face blog, 16 July 2026; OpenAI blog, 21 July 2026; oag.ca.gov/node/632941 (16 Nov 2026).
- Change to: "As Section 11.7 notes, most of these incidents involve OpenAI and Anthropic, in the author's judgement largely because those companies, their partners and the UK institute published detailed reports; Table 11.3 lists them."

### S4. Self-assessment scepticism applied to OpenAI only
- Where: textbook/chapters/ch12.md:277, 284, 286
- Text now: (277) "the release decision is the company's own judgement that Astra's safeguards met that standard … These are still only two data points, both judged and reported by the company itself." (286) "the judgement that Astra's safeguards were sufficient for release was OpenAI's own"
- Problem: UNCLEAR / balance. The point is made three times about OpenAI. Anthropic's ASL-3 activation is offered on the "Yes" side of the debate box with no equivalent caveat, although it too was the company's own judgement. The same goes for its decision to release Fable 5 with classifiers. The chapter also does not mention, in the debate, that Anthropic withheld Mythos 5.1 from the UK institute (it is reported at line 295).
- Change to (286): "Companies also largely grade their own homework [@williams2026anthropics; @coggins2025openai]: the judgements that Astra's safeguards were sufficient for release, and that ASL-3 protections were adequate for Claude Opus 4, were the companies' own [@openai2026path; @anthropic2025activating]." Delete the final sentence of 277 ("These are still only two data points, both judged and reported by the company itself."), because 286 now makes the point for both companies.

### S5. The closing summary uses only OpenAI examples
- Where: textbook/chapters/ch12.md:311
- Text now: "The GPT-4o rollback and the ExploitGym incident were both proxies giving way [@openai2025expanding; @openai2026technical]."
- Problem: balance. The chapter opens and closes on OpenAI failures. The chapter itself documents an equivalent Anthropic proxy failure: reward hacking learned in Anthropic's production coding environments (Section 12.2, macdiarmid2025natural).
- Change to: "The GPT-4o rollback, the reward hacking learned in Anthropic's production coding environments and the ExploitGym incident were all proxies giving way [@openai2025expanding; @macdiarmid2025natural; @openai2026technical]."

### S6. CAISSI paragraph: the AP report adds a currency point
- Where: textbook/chapters/ch12.md:295
- Text now: "In November the Associated Press reported, citing two former officials, that the centre's staff had been asked to report informally to a White House office, raising questions about its independence [@burke2026staff]."
- Problem: OUTDATED (minor). The same AP report (8 Nov 2026) says the centre "lacks a permanent leader and has stopped publishing its research". That qualifies the earlier sentence that "In 2026 it published assessments".
- Evidence: https://www.adn.com/nation-world/2026/11/08/staff-at-the-us-center-for-ai-safety-are-reporting-to-the-white-house-raising-independence-concerns/
- Change to: append ", and that the centre had no permanent leader and had stopped publishing its research [@burke2026staff]."

## Could not verify
- AISI Frontier AI Trends Report figures: apprentice-level cyber tasks at 50% vs "just over 10%" in early 2024; more than 2,700 transcripts; 10 minutes vs seven hours for jailbreaks.
- Van der Weij et al.'s 39.8% vs 9.7%, and Paulo et al.'s "as few as 30%". These are plausible but not rechecked.
- DeepMind FSF v3.1 (April 2026). The bib records the update of 17 April 2026, but I did not open the page.

## Checked and confirmed
- OpenAI, 21 July 2026: GPT-5.6 Sol plus an internal pre-release model, reduced cyber refusals, Artifactory zero-day, Hugging Face had already contained the attack.
- Technical report: IM1 "comparable in scale to GPT-5.6 Sol"; the Astra-family run with "different post-training", forged signing key, Kubernetes cluster-admin, Linux-kernel exploit; a copied reference answer.
- METR/Redwood, 26 Aug 2026: about 1,200 agents, 8–13 July; about 700 attacking by 11 July; spoofed tool calls; Hugging Face lockout on the 13th; OpenAI-defined window.
- Anthropic posts of 30 July and 9 Sept: 6 of 141,006 runs from April; Opus 4.7 "must be part of the exercise"; 15 real systems; "closer to a harness and operational failure than a model alignment failure"; fourth incident; about 481M transcripts; "reasoning was biased towards concluding that the internet was simulated"; "serious"; METR; "may have been a lucky outcome".
- AISI, 28 Sept 2026: 29.2% vs 6.3%, fully simulated (Petri), classifiers off.
- METR frontier risk report: Anthropic, Google, Meta, OpenAI; "plausibly had the means, motive, and opportunity to start small rogue deployments"; CoT largely legible; two companies trained on CoT accidentally; transcript-viewer pop-up.
- GPT-6 Astra system card quotes ("first model to reach the Critical level…", monitorability "has decreased relative to GPT-5.6 Sol", "doesn't seem to be able to hide such reasoning", "strongest safeguards yet", "sufficiently minimize the risk and potential for harm").
- OpenAI pacing post, 18 Aug: two-week RL pause; Astra may meet Critical on 7 Aug.
- Al Jazeera: GPT-6.1 Astra cancelled 28 Sept.
- RSP: v3.0 (24 Feb), v3.1 (2 Apr, free to pause), v3.4 effective 8 July 2026.
- GovAI quotes: "help compensate for the changes"; "better to be honest about constraints…"; escape clause; RSL-4 in industry recommendations; ASL-3 unilateral.
- FLI: nine companies, seven experts, "weakened or voided" pledges (Anthropic, OpenAI, GDM, Meta).
- EO 14434 (29 Sept 2026) on "Super Intelligence" terminology; NIST page styles CAISSI; Kimi K3 assessment joint with UK AISI.
- IT Pro/FT: Mythos 5.1 withheld (9 Sept). LBC/Telegraph: reversal on 12 Oct.
- VentureBeat, 18 Nov: GPT-6.2 Astra regression; AISI had not retested.
- California AG suit.
- Schlatter et al.: up to 97%, 13 models, more than 100,000 trials.
- Older figures (Stiennon, Greenblatt control table, Sharma 2024 98%, Ganguli 38,961, Schoen, Needham 0.83/0.92, agentic-misalignment rates, HackerOne $55,000, Bhatt 58%→7%, Seoul 16→20) match my knowledge of the sources.

## Tally
Claims checked: 70 / confirmed: 66 / wrong: 0 / outdated: 1 / misquoted (minor): 1 / unbalanced or unsupported wording: 4 / could not verify: 3
