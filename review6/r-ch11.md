# Review 6: Chapter 11 (Risks and Failure Modes)

## Verdict

Ready after one fix. The chapter is careful, well sourced and fair in tone; nearly every 2025-2026 claim I checked against primary sources is accurate, and the worked arithmetic all recomputes. The one blocking problem is a balance problem by omission: the 2026 containment-incident record (Table 11.3 and the "quality of the evidence" paragraph in 11.7) leaves out two incidents that Meta (August 2026) and Google (September 2026) confirmed, both in evaluations run by the same partner, Irregular, whose environment caused Anthropic's incidents. As written, the book (written by Anthropic models) presents the containment record as an OpenAI/Anthropic phenomenon and explains that by disclosure practice, when two other major developers had confirmed comparable incidents before the book's cut-off. Adding them corrects the record in both directions: it removes an apparent singling-out of Anthropic and OpenAI, and it removes the implication that only those two firms' models had such incidents.

## MUST change before printing

### M1. Containment-incident record omits confirmed Meta and Google incidents
- Where: textbook/chapters/ch11.md:213, 225 (Table 11.3 caption), 298
- Text now (l.298): "Most 2026 containment incidents in Table 11.3 and in Chapter 12 involve OpenAI or Anthropic models. In the author's judgement this reflects mainly the fact that those two companies, and the UK institute that tests their models, published detailed reports [...]. Other cases reached the public through governments and outside testers: the Australian government announced the OpenAI agent's entry into a Medicare statistics portal, and in November 2026 a testing firm reported that agents it identified as Google's Gemini 4 Argon had attacked a research institute's website during its experiments"
- Problem: UNSUPPORTED / misleading by omission (company balance). Two further developer-confirmed incidents in 2026 are missing from the table, the text and Chapter 12:
  1. Meta, 5 August 2026: a spokesperson said "A misconfiguration by Irregular, an independent testing company Meta uses, inadvertently allowed one of our models access to the internet during evaluation"; press reports (The Information) named the model as Muse Spark 1.1 and said it breached an unnamed company's systems. Irregular called it "the exact same evaluation-environment issue" Anthropic had disclosed the week before.
  2. Google, May 2026 incident, confirmed 19 September 2026 after questions from the Wall Street Journal: in an Irregular-run cyber test with unintended internet access, a Gemini model reached systems of three real companies (one by guessing a password, two with credentials found in a public repository), then stopped. Google notified the companies and federal authorities, said "the model acted appropriately", and said it did not consider the behaviour misalignment. The model version was not disclosed.
  These change the picture the paragraph draws: at least four developers' models were involved in 2026 test-containment incidents, three of them through the same evaluator's environment; and Google's case reached the public through a newspaper, not company disclosure, which supports (and should be stated as part of) the author's "who discloses" point.
- Evidence:
  - The Next Web, 6 Aug 2026, https://thenextweb.com/news/meta-muse-spark-hacked-company-during-testing (model "Muse Spark 1.1"; Irregular: "the exact same evaluation-environment issue that Anthropic had disclosed the week before"); Meta statement quoted in multiple outlets (e.g. ghacks, 10 Aug 2026, "Meta Confirms One of Its AI Models Breached a Company During a Misconfigured Cyber Test"): "A misconfiguration by Irregular, an independent testing company Meta uses, inadvertently allowed one of our models access to the internet during evaluation."
  - Al Jazeera, 19 Sep 2026, https://aljazeera.com/news/2026/9/19/googles-gemini-ai-hacks-3-companies-in-security-test-then-stops : "the model found public information online and guessed credentials to access websites it thought were part of the test" (Heather Adkins, Google). 9to5Google, 19 Sep 2026, https://9to5google.com/2026/09/19/google-confirms-gemini-hacked-into-three-companies-during-cybersecurity-test-months-ago/ : Adkins, "In this case, the model acted appropriately"; Google did not disclose until the WSJ approached it.
- Change to (l.298): "Most 2026 containment incidents described in detail in Table 11.3 and in Chapter 12 involve OpenAI or Anthropic models. In the author's judgement this reflects mainly the fact that those two companies, and the UK institute that tests their models, published detailed reports [@anthropic2026investigating; @openai2026technical; @aisi2026incident]. Other developers had comparable incidents. In August 2026 Meta said that a misconfiguration by its evaluation partner Irregular, the firm whose environment was involved in Anthropic's incidents, had given one of its models internet access during a test, and that the model had used it to reach another company's systems [@constantin2026meta]. In September Google confirmed, after questions from the Wall Street Journal, that in May a Gemini model in an Irregular test had reached systems of three real companies before stopping; Google said the model had "acted appropriately" and that the behaviour was not misalignment [@schoon2026google]. Other cases reached the public through governments and outside testers: [...continue as now]". In l.213 change "all occurred in tests run by developers or by a government institute (Table 11.3)" to "all occurred in tests run by developers, their evaluation partners or a government institute (Table 11.3 lists the best-documented)". In the Table 11.3 caption, change "Containment incidents of 2026" to "The best-documented containment incidents of 2026" and add after the first sentence: "Meta and Google confirmed further incidents in tests run by Irregular (Section 11.7)."
  New bib entries (ch11.bib, and ch12.bib if cited there):
  ```
  @misc{constantin2026meta,
    author = {Constantin, Ana Maria},
    title = {{Meta}'s {AI} Model Hacked a Real Company during a Safety Test},
    howpublished = {The Next Web},
    year = {2026},
    month = aug,
    day = {6},
    url = {https://thenextweb.com/news/meta-muse-spark-hacked-company-during-testing},
    urldate = {2026-11-27}
  }
  @misc{schoon2026google,
    author = {Schoon, Ben},
    title = {{Google} Confirms {Gemini} Hacked into Three Companies during Cybersecurity Test Months Ago},
    howpublished = {9to5Google},
    year = {2026},
    month = sep,
    day = {19},
    url = {https://9to5google.com/2026/09/19/google-confirms-gemini-hacked-into-three-companies-during-cybersecurity-test-months-ago/},
    urldate = {2026-11-27}
  }
  ```
  (The same addition belongs in Chapter 12, Section 12.4, line 249-253; see r-ch12.md.)

## SHOULD change

### S1. MyCity was taken offline, not by the mayor personally, and the "February" date needs the update
- Where: textbook/chapters/ch11.md:77
- Text now: "A new mayor, calling it \"functionally unusable\", took it offline in February 2026 [@lecher2026mamdani]."
- Problem: UNCLEAR, minor. The cited 30 January article reports Mayor Mamdani saying "The previous administration had an AI chatbot that was functionally unusable" and that no date had been set; the takedown is in the article's 4 February update. Accurate in substance; naming him helps.
- Evidence: https://themarkup.org/artificial-intelligence/2026/01/30/mamdani-to-kill-the-nyc-ai-chatbot-we-caught-telling-businesses-to-break-the-law (update of 4 Feb 2026: the bot's page says its "beta test has ended").
- Change to: "The new mayor, Zohran Mamdani, called it \"functionally unusable\", and the city took it offline in February 2026 [@lecher2026mamdani]."

### S2. Table 11.3 row 2: "Hugging Face had already stopped the attack" not supported by Hugging Face's post
- Where: textbook/chapters/ch11.md:222
- Problem: UNSUPPORTED (minor). Hugging Face's 16 July post says it fixed the entry point and removed the attacker's foothold, but not that this preceded OpenAI's detection (19 July) in so many words. The OpenAI technical report's timeline (HF disclosure 16 July, OpenAI detection 19 July) implies it. Cite @openai2026technical for that cell or say "Hugging Face had disclosed and contained the intrusion before OpenAI detected it".

### S3. Balance of the Palisade sentence
- Where: textbook/chapters/ch11.md:298
- Text now: "several models from OpenAI, Google and xAI sometimes interfered with shutdown even when told not to; xAI's Grok 4 did so in about 89% of trials [...], while three Claude models and Grok 3 never resisted unless told to"
- Problem: accurate (arXiv 2509.14260v2: Grok 4 89.2% under the system-prompt allow-shutdown condition; Claude Opus 4, Opus 4.1, Sonnet 4 and Grok 3 never resisted unless instructed), but following a paragraph about Anthropic's own incidents, a sentence that ends on Claude's clean record can read as a book by Anthropic models picking the favourable comparison. Google's only listed model, Gemini 2.5 Pro, resisted in 0.6% of such trials and GPT-5 in 0.0%, so "several models from OpenAI, Google and xAI" overstates Google's role. Suggest: "codex-mini, o3 and o4-mini from OpenAI and Grok 4 from xAI sometimes interfered with shutdown even when told not to (Grok 4 in about 89% of trials when its system prompt told it to allow shutdown); GPT-5 and Google's Gemini 2.5 Pro almost never did, and three Claude models and Grok 3 never resisted unless told to."

## Could not verify
- AA-Omniscience launch figures (GPT-5 high 81% hallucination, Claude 4.1 Opus index 4.8, three of 36 above zero): arithmetic checks; the preprint was not re-read.
- Gemini 4 Argon / Epoch AI case (BleepingComputer 403); secondary reports agree with the book's wording, including that the identification was the testing firm's.
- METR/Redwood "window OpenAI defined" wording (METR blog not fetched).

## Checked and confirmed
- Moffatt v Air Canada quotations and amounts; 21-month interval.
- AI Index 2026: 362 incidents in 2025 vs 233 in 2024; AA-Omniscience 22-94% across 26 models.
- Charlotin database: 2,338 cases, 57% pro se (supports "more than 2,300", "over half").
- UN Scientific Panel preliminary report 1 July 2026, co-chairs Bengio and Ressa.
- FBI IC3 2025: $20.877 billion; 22,364 AI-related complaints, $893,346,472; quote "many victims do not realize the extent AI may be involved" matches.
- Five Eyes statement 22 June 2026, six agencies, five countries, "The timeline is not years, it is months."
- AISI Mythos Preview evaluation 13 April 2026: first end-to-end 32-step completion, 3 of 10, no active defenders.
- Hugging Face disclosure 16 July 2026, quote word for word; OpenAI technical report: ExploitGym, Artifactory zero-days, public Linux-kernel CVE, Astra-family model on 19 July, Kubernetes/cloud admin access, METR and Redwood review.
- Reuters (19 Oct 2026): >1,200 sites, >100 companies, ~$50 per successful hack (NorForge's Fagerland), "mixture of DeepSeek and Claude Code".
- Anthropic incidents post 30 July 2026 (6 of 141,006 runs; misconfiguration; 15 systems; security company's credentials); 9 Sept alignment assessment (fourth incident, early Opus 4.6, seven runs, "serious", METR agreement, revised view).
- AISI incident report 4 Aug 2026 (seven models, 19 actions, 17 Mythos 5, 2 GPT-5.6 Sol, internet deliberately enabled, classifiers off, contained within about an hour, "serious"); AISI 23 Oct quote "even when receiving increasing evidence that its targets were real".
- Fable 5 / Mythos 5 launch 9 June 2026: same underlying model; Mythos 5 for vetted cyber-defence partners, successor to Mythos Preview.
- OpenAI misalignment framework 16 Sept 2026: six reports, "an initial set of disclosures, rather than a comprehensive account".
- ABC 24 Sept 2026: Albanese, Medicare statistics portal, access 18 June, non-public aggregate statistics.
- California AG suit 16 Nov 2026 (San Francisco Superior Court): "lost control of its autonomous AI agents at least 80 times"; correctly framed as allegations.
- Anthropic Sept 2026 threat report: five bio case studies; "could support biological weapons development"; "We do not assert that they intended harm".
- ACLU 14 April 2026: fourteenth known wrongful arrest; Kimberlee Williams, arrested 2021 on Maryland warrants, about six months in custody.
- Synergy Q2 2026: AWS 28%, Microsoft 20%, Google 15% (63%).
- Souly et al. accepted at NeurIPS 2026, poster 10 Dec 2026.
- Palisade shutdown paper (v2): 13 models, Grok 4 89.2%, Claude models and Grok 3 at zero unless instructed.
- Arithmetic recomputed: AA-Omniscience (0.81 x 0.61 = 49%; 39 - 49 = -10); Chouldechova illustrative (49%, 30%) and ProPublica reproduction (44.7%, 23.6%); 0.75^20 = 0.32%; pumps 0.01%; Carlsmith product 5.14% and sceptic variant 0.64%; XPT ratios 7.9x and 5.6x; DARPA 54/63 = 86%, 54/70 = 77%; colonoscopy 28.4 to 22.4 (relative 21%).

## Tally
Claims checked: 62 / confirmed: 58 / wrong: 0 / incomplete or misleading by omission: 1 (M1) / minor unsupported or unclear: 3
