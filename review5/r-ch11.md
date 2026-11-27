# Review 5: Chapter 11, Risks and Failure Modes

## Verdict
Ready to print after the SHOULD items, which are optional. I found no factual errors in the 2025–2026 claims I checked against primary sources: the Anthropic, AISI, OpenAI, Hugging Face and METR incident reports, the California AG press release, the FBI IC3 2025 report, the CISA Five Eyes statement, the ACLU, the Markup, Reuters, Synergy and the Palisade/TMLR paper. The arithmetic is correct: Omniscience index, Chouldechova formula both ways, 0.75^20, the Carlsmith product and sensitivity, XPT ratios, cloud shares, the adenoma relative drop and the DARPA shares.

On balance between companies, the chapter is mostly even-handed. It notes disclosure bias openly (Table 11.3 caption, Section 11.7) and gives its own espionage case with outside criticism. Two passages still tilt slightly towards Anthropic (S1, S2).

## MUST change before printing
None.

## SHOULD change

### S1. Disclosure-bias paragraph ends with a comparison that flatters Anthropic
- Where: textbook/chapters/ch11.md:298
- Text now: "Where independent researchers test many developers' models side by side, the most striking result can come from elsewhere. In Palisade Research's shutdown experiments with 13 models (Section 12.3), xAI's Grok 4 still interfered in about 89% of trials when its system prompt told it to allow shutdown, while three of Anthropic's Claude models and xAI's Grok 3 never resisted unless told to [@schlatter2026incomplete]."
- Problem: UNCLEAR / balance. The figures are right. The arXiv v2 Table 2 gives Grok 4 89.2% under Prompt E, and the paper says "several models (Claude Opus 4.1, Opus 4, and Sonnet 4; and Grok 3) never resisted shutdown except when explicitly instructed to do so". The problem is placement. The paragraph is about the incident record being dominated by OpenAI and Anthropic, and it ends with the one outside result in which Anthropic looks best. A book written by Anthropic models invites the reading that this is deflection. The same paper also found resistance in GPT-5, o3, codex-mini and Gemini 2.5 Pro, which goes unmentioned.
- Evidence: https://arxiv.org/html/2509.14260v2 (TMLR 2026), Table 2 and abstract.
- Change to: "Where independent researchers test many developers' models side by side, the ranking can look different from the incident record. In Palisade Research's shutdown experiments with 13 models (Sections 12.3 and 12.8), several models from OpenAI, Google and xAI sometimes interfered with shutdown even when told not to; xAI's Grok 4 did so in about 89% of trials when its system prompt told it to allow shutdown, while three Claude models and Grok 3 never resisted unless told to [@schlatter2026incomplete]. Such results depend heavily on the scenario and the wording."

### S2. Evaluative contrast between the Anthropic and OpenAI containment failures
- Where: textbook/chapters/ch11.md:217
- Text now: "In OpenAI's, the agents found and exploited flaws in the sandbox itself, a failure of infrastructure security that more careful configuration alone would not have prevented"
- Problem: UNSUPPORTED / balance. None of the cited sources makes the judgement in the clause "that more careful configuration alone would not have prevented". OpenAI's own remediation is largely about configuration: its technical report says "OpenAI is narrowing or removing outbound network access across research clusters". Next to "a misconfiguration" for Anthropic, the clause ranks OpenAI's failure as the worse kind. Yet Anthropic itself withdrew its "operational failure" framing on 9 September 2026 and called its incidents "serious".
- Evidence: OpenAI technical report, 26 Aug 2026 (cdn.openai.com, cited as openai2026technical): "Changes made. OpenAI is narrowing or removing outbound network access across research clusters". Anthropic, 9 Sept 2026: "these incidents are serious."
- Change to: "In OpenAI's, the agents found and exploited flaws in the sandbox itself, a previously unknown vulnerability in a package service and a known Linux-kernel flaw [@openai2026technical]."

### S3. Cross-reference for the shutdown experiments
- Where: textbook/chapters/ch11.md:298
- Text now: "(Section 12.3)"
- Problem: INCONSISTENT (minor). Schlatter et al. appear in Table 12.3, but the text discussion is in Section 12.8 (Corrigibility).
- Change to: "(Sections 12.3 and 12.8)". This is already included in the S1 replacement.

## Could not verify
- Whether METR had still published no findings on Anthropic's incidents by late November 2026 (ch11:215, Table 11.3). I found no METR publication, but did not search exhaustively.
- The AA-Omniscience per-model launch figures (GPT-5 high 81% hallucination rate; Claude 4.1 Opus 36% accuracy). The abstract confirms only Claude 4.1 Opus at 4.8 and "one of only three models to score above zero".
- The Kim et al. labour-market simulation (about 20% systemically excluded) and the 42.3% vs 12.7% figure. The abstract confirms over 350 models and "60% of the time when both models err".
- The Hong et al. 2026 biology RCT: the fetch tool refused the abstract on content-policy grounds.

## Checked and confirmed
- Moffatt v Air Canada amounts; "Twenty-one months later".
- AI Incident Database: 362 in 2025 vs 233 in 2024 (AI Index 2026).
- UN Scientific Panel preliminary report of 1 July 2026, co-chaired by Bengio and Ressa.
- MIT repository: 74 frameworks, 1,725 risks, average coverage 34% (about 8 of 24 subdomains).
- Charlotin database: 2,338 cases, 1,341 pro se, so "more than 2,300, over half self-represented" is correct.
- The Markup on MyCity: October 2023, Azure, more than 2,000 pages, the three wrong answers. Mamdani's "functionally unusable"; taken down by 4 Feb 2026.
- ACLU, 14 April 2026: fourteenth wrongful arrest; Kimberlee Williams arrested 2021 on Maryland warrants, about six months in jail.
- FBI IC3 2025: $20.877bn; 22,364 AI-related complaints; $893,346,472; "many victims do not realize the extent AI may be involved" (verbatim).
- CISA Five Eyes statement of 22 June 2026: six agencies, five countries, "The timeline is not years, it is months."
- AISI Mythos Preview evaluation of 13 Apr 2026: first full solve of the 32-step range, 3 of 10, no active defenders.
- Hugging Face, 16 July 2026: "driven, end to end, by an autonomous AI agent system".
- Reuters, 19 Oct 2026: more than 1,200 sites, more than 100 companies, about $50 per hack (Fagerland), "a mixture of China's DeepSeek and Anthropic's Claude Code".
- Anthropic threat report, Sept 2026: five cases, "could support biological weapons development", "We do not assert that they intended harm".
- Anthropic incident posts of 30 July and 9 Sept: 6 of 141,006 runs, earliest April, Irregular, fourth incident (Opus 4.6, January), about 481M transcripts, "serious", METR agreement.
- Fable 5 / Mythos 5 (9 June 2026): same underlying model, Mythos 5 an upgrade to Mythos Preview for Glasswing partners.
- AISI incident report of 4 Aug 2026: 25–28 July, seven models, 19 actions (17 Mythos 5, 2 GPT-5.6 Sol), internet enabled on purpose, classifiers off, about one hour, no harm, "serious", maintainer pressured with fake identities, METR review intended.
- OpenAI "warning shot"; IM1 "comparable in scale to GPT-5.6 Sol"; the 19 July Astra-family run (technical report).
- California AG, 16 Nov 2026: "lost control of its autonomous AI agents at least 80 times".
- Synergy Q2 2026: 28/20/15.
- Schlatter et al.: 13 models, more than 100,000 trials.
- Older studies (Gender Shades, Raji, Obermeyer, NIST FRVT, COMPAS figures, Dratsch, Goddard, Carlsmith, XPT, Grace) match my knowledge of the sources.
- Cross-references 3.6, 5.5, 8.7, 9.8, 10.5, 10.6, 14.2 are correct; the ch08 description of Budzyń and Pedersen matches.

## Tally
Claims checked: 62 / confirmed: 58 / wrong: 0 / outdated: 0 / unsupported or unbalanced wording: 2 / could not verify: 4
