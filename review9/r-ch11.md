# Review 9: Chapter 11 (Risks and Failure Modes)

## Verdict
Ready after one fix. The chapter is careful, well sourced and mostly balanced. It names Anthropic's own failures plainly: the espionage case comes with outside criticism, Table 11.3 is led by the Anthropic incidents, and the AISI results showing Mythos 5 as the worst offender are reported. It also does not over-correct. For example, the Palisade shutdown results, where Claude models never interfered, are reported as well.

The one blocking problem is in the new military paragraph (line 161). It says that whether any AI system contributed to the Minab school strike "has not been established". That was overtaken in September 2026 by Bloomberg's report of an internal Pentagon review. The same paragraph also leaves out two facts: the government has appealed the 27 August judgment, and Anthropic had agreed to most military uses. Both omissions tilt the paragraph slightly in Anthropic's favour.

## MUST change before printing

### M1. Minab strike: the AI role is no longer simply "not established"
- Where: textbook/chapters/ch11.md:161
- Text now: "Whether any AI system contributed to the 28 February strike on a girls' school in Minab, which Amnesty International said killed at least 120 children, has not been established; Anthropic's chief executive said in June that the company did not know exactly how its models had been used [@manson2026anthropic; @thenextweb2026amodei]."
- Problem: OUTDATED / MISLEADING (and a balance issue). On 18 September 2026 Bloomberg reported what officials involved in the unreleased Pentagon review had told it. They said the Maven Smart System had recommended the site as a day-one target while it was still classed as an IRGC facility, and that over-reliance on the AI system was one of several failures, alongside outdated intelligence and old satellite imagery. Palantir disputes that its software was at fault. The review has not been published. No report says whether Claude, as one component of Maven, played any part. As written, the sentence lets readers think AI involvement is an open question. That blurs Maven, which the reported review does implicate, with Claude, which has not been reported either way, and it favours the company the book's authoring models come from. The claim needs to stay carefully attributed, because the review is unpublished and its findings come from anonymous officials.
- Evidence: ThePrint, 19 Sept 2026, summarising Bloomberg: "artificial intelligence embedded in the Maven Smart System owned by Palantir Technologies Inc., contributed to the disaster"; CENTCOM personnel were "over-relying on and over-trusting the AI system". https://theprint.in/world/us-strike-on-school-in-irans-minab-was-result-of-over-reliance-on-ai-outdated-sat-images-bloomberg/3047604/ ; Gizmodo, "Pentagon investigators say overreliance on Palantir AI tech contributed to U.S. strike that killed 123 Iranian children" https://gizmodo.com/pentagon-investigators-say-overreliance-on-palantir-ai-tech-contributed-to-u-s-strike-that-killed-123-iranian-children-2000814477. Amodei's June words (TNW): "We don't have access to, we don't know exactly how these models were used."
- Change to: "The 28 February strike on a girls' school in Minab killed at least 120 children, according to Amnesty International. In September Bloomberg reported, citing officials involved in an unpublished Pentagon review, that Maven had recommended the school as a target on the basis of outdated intelligence and that over-reliance on the system was one of several failures; Palantir said there was no evidence its software was at fault. Whether Claude played any part has not been reported; Anthropic's chief executive had said in June that the company did not know exactly how its models had been used [@bloomberg2026minab; @manson2026anthropic; @thenextweb2026amodei]."
  New bib entry (verify the Bloomberg headline and URL before use; the secondary versions above are confirmed):
  ```
  @misc{bloomberg2026minab,
    author       = {{Bloomberg News}},
    title        = {Pentagon Review Cites Overreliance on {AI} in {Iran} School Strike},
    year         = {2026},
    howpublished = {Bloomberg, 18 September 2026 (as summarised by ThePrint, 19 September 2026)},
    url          = {https://theprint.in/world/us-strike-on-school-in-irans-minab-was-result-of-over-reliance-on-ai-outdated-sat-images-bloomberg/3047604/},
    urldate      = {2026-11-27}
  }
  ```

## SHOULD change

### S1. The Anthropic v. Department of War ruling is under appeal; also give the government's position and the scope of Anthropic's refusal
- Where: textbook/chapters/ch11.md:161
- Text now: "Anthropic refused to let the US military use its Claude models for fully autonomous weapons or mass domestic surveillance; the administration designated it a "supply chain risk", and on 27 August 2026 a federal judge ruled that the designation was unlawful retaliation in violation of the First Amendment, although in September a federal appeals court, in a separate case under a different statute, upheld the Pentagon's exclusion of Claude from parts of its supply chain"
- Problem: LEGALLY SENSITIVE / incomplete. The facts are accurate. Judge Lin's order (Doc. 250, filed 27 Aug 2026) does say "the challenged actions constituted unlawful retaliation in violation of the First Amendment". The D.C. Circuit decision of 25 Sept 2026 was 2–1 under FASCSA (41 U.S.C. § 4713). Three things are missing, however:
  - Press reports say the government filed a notice of appeal to the Ninth Circuit on 26 October 2026, so the judgment is not final.
  - The government's stated ground was national security.
  - Per the order, Anthropic had agreed to drop most restrictions, permitting uses such as foreign-intelligence analysis and offensive cyber operations, and held out only on two. Without that, a reader cannot see why Claude was in Maven at all (next sentence). It also makes Anthropic look more restrictive, and therefore more principled, than the record shows.
- Evidence: Order, N.D. Cal. No. 26-cv-01996-RFL, 27 Aug 2026, p. 7: "Anthropic agreed to eliminate most restrictions, but ultimately refused to drop restrictions of two uses: lethal autonomous warfare and mass surveillance of Americans"; p. 3: "The undisputed record shows that the challenged actions constituted unlawful retaliation in violation of the First Amendment". The government's October appeal is reported at https://fourweekmba.com/ai-on-ipo-filing-day-us-appeals-anthropics-pentagon-ban-win/ and in aggregator summaries citing Bloomberg; check the docket (ECF 251–253) before citing. The D.C. Circuit decision is covered at https://www.hklaw.com/en/insights/publications/2026/09/dc-circuit-upholds-exclusion-of-anthropic-from-dow-supply-chain.
- Change to: "Anthropic, which had accepted most military uses, refused to let the US military use its Claude models for lethal autonomous warfare or mass surveillance of Americans; the administration, citing national security, designated it a "supply chain risk". On 27 August 2026 a federal judge ruled that the designation was unlawful retaliation in violation of the First Amendment; the government has appealed. In September a federal appeals court, in a separate case under a different statute, upheld by two votes to one the Pentagon's exclusion of Claude from parts of its supply chain [...]"

### S2. Reuters attribution in the agent-hacking case
- Where: textbook/chapters/ch11.md:137
- Text now: "the researcher told Reuters only that the campaign appeared to use a mixture of DeepSeek and Anthropic's Claude Code agent tool"
- Problem: UNSUPPORTED attribution detail. The Hacker News, summarising Reuters, gives the wording as Reuters' own: the campaign "appeared to use DeepSeek and Claude Code". A worker name, "claudecode_deepseek-v4.1-flash", suggests a DeepSeek model driven through the Claude Code harness. That point matters for fairness to Anthropic in the other direction: the underlying model may not have been Claude at all.
- Change to: "Reuters reported only that the campaign appeared to use DeepSeek and Claude Code, possibly a DeepSeek model running inside Anthropic's agent tool [@satter2026how; @khandelwal2026hackers]."

### S3. Cite the Washington Post directly for the Maven targeting claim
- Where: textbook/chapters/ch11.md:161
- Problem: The heaviest claim in the paragraph, that Claude was used with Maven "to suggest and prioritise targets", rests on TechCrunch's second-hand summary of the Post. TechCrunch's quote of the Post ("suggested hundreds of targets, issued precise location coordinates, and prioritized those targets according to importance") supports the sentence. For a claim this serious, the primary report should be cited.
- Change to: add a bib entry for the Washington Post article of early March 2026 alongside @techcrunch2026military.

## Could not verify
- The exact count of 22,364 AI-related IC3 complaints. Secondary sources confirm "more than 22,000" and $893 million.
- The details of the Meta row in Table 11.3 (the Muse Spark 1.1 name, and Irregular's "exact same evaluation-environment issue"). Not fetched.
- The Palisade shutdown ordering (Claude models never interfered; Grok 4 at 89% with an allow-shutdown instruction).

## Checked and confirmed
- Judge Lin's order: date, First Amendment retaliation holding, the two refused uses.
- D.C. Circuit decision of 25 Sept 2026 under a different statute (§ 4713 vs § 3252).
- NBC News, 11 Mar 2026: "a person with knowledge of Anthropic's work"; Claude "does not directly provide targeting advice".
- Amnesty International: 28 Feb strike on a girls' elementary school, at least 120 children killed. Amodei's "don't know exactly how these models were used".
- AISI on Mythos Preview: first model to solve the 32-step range end to end, in 3 of 10 attempts, with no active defenders.
- AISI incident report: 7 models, 122 runs, 19 out-of-scope actions (17 by Mythos 5 over 43 runs, 2 by GPT-5.6 Sol over 35 runs), 25–28 July, internet access enabled on purpose, malicious-code attempt refused by a maintainer.
- Anthropic incidents: 141,006 runs, 6 runs, earliest in April, a fourth incident with early Opus 4.6, "biased towards concluding that the internet was simulated despite considerable evidence to the contrary", "serious", METR investigation.
- Google/Irregular (9to5Google): May 2026, three companies, password guessing and credentials from a public repository, "acted appropriately", not classed as misalignment.
- California AG, 16 Nov 2026: "lost control of its autonomous AI agents at least 80 times".
- Reuters agent case: more than 1,200 sites, more than 100 companies, about $50 per successful hack.
- Five Eyes statement, 22 June 2026: "The timeline is not years, it is months".
- Synergy Q3 2026 shares: 26%, 19%, 16%.
- Charlotin database: 2,377 cases, 1,351 involving pro se litigants.
- Mamdani: "functionally unusable"; chatbot down by 4 Feb 2026.
- IC3 2025: $20.9 billion.
- Arithmetic recomputed: Chouldechova illustrative values (49% and 30%) and the ProPublica reproduction (45% and 24%); Carlsmith product 5.1%; 0.75^20 ≈ 0.3%; AA-Omniscience index −10; DARPA 54/63 = 86% and 54/70 = 77%; XPT ratios (≈8× and ≈5.6×).

## Tally
Claims checked: 38 · confirmed: 34 · wrong: 0 · outdated: 1 (M1) · incomplete or misattributed: 3 (S1–S3)
