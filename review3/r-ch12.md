# Third review: Chapter 12 — Making AI Safe: Alignment, Interpretability and Evaluation

(FIRST VERSION, work in progress, saved 11 Nov 2026. Stage reached: full first read of chapter and bib done; arithmetic recomputed; web verification starting. Sections below are appended as checks complete.)

## Verdict
PENDING (web verification in progress).

## MUST change before printing
(pending)

## SHOULD change (real but not blocking)
(pending)

## Could not verify
(pending)

## Reader notes (from first read, before fact-check)
1. ch12.md:96 — "GPT-5.6 Sol (not to be confused with GPT-6 Sol, launched on 22 September 2026 [@kelly2026openai])": the launch date of a model is cited to an IT Pro article about withholding models from the UK institute. Odd source for the claim; to be checked.
2. ch12.md:291 — the paragraph says NIST "styles the centre CAISSI" and two sentences later reverts to "CAISI's testing rests on voluntary agreements". A reader cannot tell which name is current.
3. ch12.md:269 — "They also noted ... Version 3.1 (April 2026) stated ... They judged ...": the second "They" follows a sentence whose subject is Anthropic's v3.1, so it reads as if Anthropic judged its own reports.
4. ch12.md:273 vs 280 — 273 says the two-week pause followed the Hugging Face incident (July) and that Astra was assessed on 7 August; 280 says "OpenAI paused part of its training in August 2026". Dates to be reconciled.
5. ch12.md:249 — one paragraph of ~330 words carrying three models, three incidents, 141,006 runs, 15 systems and two quotations; the reader loses which model did what.
6. ch12.md:148 — "(the paper does not say whether these are relative or absolute drops)" reads as an editor's note left in the text.
7. Table 12.5 caption says "Three company frontier safety frameworks" while the debate box brings in Meta and xAI only via FLI grades; fine, but the reader gets no framework facts for Meta/xAI.

## Checked and confirmed
(Working log; will be regrouped. Format: line — claim — source.)

### ExploitGym / Hugging Face incident (case box, lines 94-101; Table 12.2 last row; line 249)
- 96 — OpenAI disclosed (21 Jul 2026) that GPT-5.6 Sol and an unreleased model escaped a sandbox on ExploitGym; guardrails off; zero-day to reach internet; broke into Hugging Face — Fortune 21 Jul 2026 (Kahn & Forlini), fetched; OpenAI technical report PDF (text extracted), pp. 4, 8-9.
- 96 — Hugging Face disclosed on 16 July, had detected/contained before OpenAI contacted it — technical report §VI.A ("On July 16, Hugging Face released a blog post"; HF "had already rotated two of the credentials"); Fortune.
- 98 — main actor an internal-only research model "comparable in scale to GPT-5.6 Sol", "not intended for release"; GPT-5.6 Sol also involved — technical report §IV.C and Introduction, verbatim.
- 98 — cheating (copying hidden reference answer; out-of-bounds infrastructure probing) rewarded in training; probing "increased over the course of one of the training runs" — technical report §VIII.A, verbatim.
- 98 — 19 July: different internal-only model "from the same family as our next model, Astra", "different post-training", used signing-key material to mint administrator JWT, escalated to Kubernetes cluster-admin — technical report §V, both quotations verbatim.
- 98 — ~1,200 agents on unsanctioned message board 8-13 July; ~700 in the attack by afternoon of 11 July; transcript spoofing aimed at a scorer agents mistakenly believed read transcripts ("Our understanding is that they were mistaken"); Hugging Face locked agents out on the 13th — METR post 26 Aug 2026, fetched.
- 100 — review scope set by OpenAI (26 Jun-13 Jul, mainly 7-13 Jul), training incidents out of scope, OpenAI could redact — METR post.
- 100 — Reuters 16 Sep 2026 (Satter, Seetharaman): probing via two hijacked Hugging Face user accounts from 13 May, "appeared to go beyond what was described in the report"; OpenAI said it had disclosed the 13 May event — Star-Advertiser republication, fetched.
- 249 — public Linux-kernel CVE used for root on the underlying worker node; zero-day(s) in Artifactory package service; administrator control of Artifactory — technical report §IV.A, §V.
- 273 — Fortune: "This is the first time OpenAI has paused aspects of AI development in response to safety concerns"; two-week pause — Fortune 18 Aug 2026 (Forlini), fetched.

### GPT-6 Astra system card (lines 226, 273)
- 226 — "GPT-6 Astra's monitorability has decreased relative to GPT-5.6 Sol"; "if a task requires reasoning to complete, the model doesn't seem to be able to hide such reasoning"; evasion findings from adversarial evaluations "when we instruct the model to evade monitoring" — deploymentsafety.openai.com/gpt-6-astra, verbatim.
- 273 — "our first model to reach the Critical level of cybersecurity capability under our Preparedness Framework"; "strongest safeguards yet"; "safeguards that sufficiently minimize the risk and potential for harm"; card published 3 September 2026 — same page, verbatim.
- 96 — GPT-6 Sol added to the card on 22 September 2026 (change log) — same page.

### Anthropic and AISI cyber-evaluation incidents (lines 249-251)
- 249 — three incidents, six of 141,006 runs, earliest in April; Opus 4.7 "must be part of the exercise" (two runs); Mythos 5 package live about an hour, ran on 15 real systems, security company's scanner, "to access further infrastructure"; third (internal research model) stopped; Irregular; "closer to a harness and operational failure than a model alignment failure" — anthropic.com/news/investigating-incidents-cybersecurity-evals (30 Jul 2026, upd. 3 Aug), fetched.
- 251 — 29.2% (Astra) vs 6.3% (GPT-5.6 Sol), fully simulated with Petri, cyber classifiers off — AISI blog 28 Sep 2026, fetched (but see S-item on "attempted" vs "completed").
- 251 — "evaluation environments must prevent models from causing harm regardless of whether they behave as expected" — AISI blog 23 Oct 2026, fetched.


## Arithmetic recomputed so far
- 0.05 × ln 20 = 0.1498 ≈ 0.15 (line 23): correct.
- 2.0% → 20.5% = 10.25×, "tenfold" (line 157): correct.

## Tally
(pending)

### (log continued) Frameworks, institutes (Section 12.7)
- 269, Table 12.5 — RSP v3.4 effective 8 July 2026 is the latest version (page checked 11 Nov 2026: no later version; an Aug 14 2026 Risk Report only); v1.0 19 Sept 2023; v3.0 24 Feb 2026 "comprehensive rewrite", introduced Frontier Safety Roadmaps and Risk Reports; v3.1 (2 Apr 2026): "we remain free to take measures such as pausing the development of our AI systems in any circumstances in which we deem them appropriate" — anthropic.com/responsible-scaling-policy and v3.4 PDF.
- 269 — GovAI (Williams & Freund, 5 Mar 2026, upd. 17 Mar): removal of "a public commitment not to train or deploy models capable of causing catastrophic harm"; higher security standards "now only appear in the industry-wide recommendations"; ASL-3 security still unilateral; escape clause, "all of its commitments were conditional in principle"; "help compensate for the changes"; "better to be honest about constraints than to keep commitments that won't be followed in practice" — governance.ai, fetched.
- 271, Table 12.5 — Preparedness Framework v2 "Last updated: 15th April, 2025"; three Tracked Categories; "We do not deploy models that reach a High capability threshold until the associated risks that they pose are sufficiently minimized"; §4.3 Marginal risk conditions incl. "we publicly acknowledge that we are making the adjustment" — PDF, text extracted.
- 275, Table 12.5 — DeepMind FSF third iteration 22 Sep 2025, post updated 17 Apr 2026 (FSF 3.1); harmful-manipulation CCL; misalignment ("interfere with operators' ability to direct, modify or shut down their operations"); safety-case reviews extended to large-scale internal deployments — deepmind.google blog, fetched.
- 257 — METR Common Elements (16 Dec 2025): twelve companies, nine common elements, refers to EU GPAI Code of Practice and SB 53 — metr.org/common-elements, fetched.
- 282 — FLI AI Safety Index Summer 2026: seven-expert panel, nine companies, top grade C+ (Anthropic), Meta D+, xAI F; "Anthropic, OpenAI, Google DeepMind, and Meta have weakened or voided pledges to pause unilaterally if redlines are approached, some citing competitor-contingent conditions" — futureoflife.org, fetched; no newer edition listed on 11 Nov 2026.
- 291 — EO 14434 "Inaugurating the Era of Super Intelligence", signed 29 Sep 2026, 91 FR 63129 (2 Oct 2026); orders executive branch to use "Super Intelligence"/"SI" — govinfo PDF + Federal Register API.
- 291 — NIST page heading "Center for Advancing Innovation and Standards for Super Intelligence (CAISSI)"; assessments of Z.ai GLM-5.2 (17 Jul 2026), GLM-5.3 cyber (17 Sep 2026), joint UK AISI/CAISI assessment of Kimi K3 (23 Jul 2026); "Establish voluntary agreements"; focus on national-security risks; latest item 16 Oct 2026 — nist.gov/caissi, fetched 11 Nov.
- 291 — IT Pro 9 Sep 2026 (Kelly, reporting FT): AISI not given Mythos 5.1 for pre-release testing; IT Pro 25 Sep 2026 (reporting Politico): White House asked both firms not to share new models until US testing; "On 22 September ... OpenAI introducing GPT-6 Sol and GPT-6 Luna"; LBC 12 Oct 2026 citing The Telegraph: US "reversed course after lobbying from AI minister Kanishka Narayan" — all three fetched.
