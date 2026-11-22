# Third review: Chapter 5 — From Chatbots to Agents

STATUS: FINAL (continuation round, 22 November 2026). The first round covered the opening through Section 5.5 and recomputed all arithmetic; this round settled its two candidate items, checked Section 5.5 (Replit box) and 5.6 to the end, the opening of 5.4 ("Why agents got better"), the glossary and figure specs, re-checked every time-sensitive statement against the news up to 22 Nov 2026, and completed the bib check.

## Verdict
Ready after the MUST fix below. The chapter is careful, well hedged and, apart from one item, accurate. Of about 285 claims checked against sources across both rounds, none was verifiably wrong. Quotations are exact, the numbers match their sources and the worked examples are correct. The one blocking problem is currency. The chapter reports SWE-bench Pro as the successor benchmark and gives its October 2026 leaderboard top. It does not say that in July 2026 OpenAI, which had recommended the benchmark, found about 30% of its public tasks broken and withdrew that recommendation, or that Epoch AI now rates it "Flawed". An expert reader would notice, because the chapter reports the parallel audit of SWE-bench Verified in detail. The remaining items are small currency and precision fixes.

## MUST change before printing

### M1. SWE-bench Pro: July 2026 audit found ~30% of public tasks broken; OpenAI withdrew its recommendation
- Where: textbook/chapters/ch05.md:165 and the caption of Table 5.2 (line 173)
- Text now (line 165): "On Scale AI's public leaderboard, mostly run in a minimal agent program, the top entry in October 2026 resolved 61.5% [@scale2026swebench]. For anyone choosing a coding agent, the practical lesson is that a headline score means little until the task set, the agent program and the budget behind it are known."
- Problem: OUTDATED (omission that changes how the reader takes the numbers). The chapter tells the reader that OpenAI stopped reporting SWE-bench Verified because an audit found flawed tasks (line 163), then presents SWE-bench Pro as "a successor" with results up to October 2026. It omits that OpenAI's February 2026 post had recommended SWE-bench Pro and that OpenAI's audit of 8 July 2026 estimated about 30% of its public tasks broken and retracted that recommendation. Epoch AI's benchmark review of 1 September 2026 rates SWE-bench Pro "Flawed". The author's evidence log records the February recommendation but not the July retraction.
- Evidence:
  - https://openai.com/index/separating-signal-from-noise-coding-evaluations/ (8 July 2026, fetched 22 Nov 2026): "we find widespread task issues in SWE-Bench Pro and estimate that ~30% of the tasks are broken"; "Our datapoint analysis pipeline flagged 200 (27.4%) broken tasks, while the human annotation campaign identified 249 (34.1%)"; "On the 731-task public split ..."; "Given the issues uncovered in this analysis, we retract our earlier recommendation to adopt SWE-Bench Pro."
  - https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ (23 Feb 2026): "We recommend SWE-bench Pro."
  - https://epoch.ai/benchmarks/swe-bench-pro/review: "Reviewed: Sep. 1, 2026 ... Verdict: Flawed"; "audits of SWE-Bench Pro have estimated that 30% or more of tasks are broken"; error categories "misleading prompts, overly strict tests, underspecified prompts, and low-coverage tests".
  - Arithmetic: 200/731 = 27.4%; 249/731 = 34.1%.
- Change to: after "...the top entry in October 2026 resolved 61.5% [@scale2026swebench]." insert:
  "SWE-bench Pro has since had its own audit. In July 2026 OpenAI, which in February had recommended the benchmark in place of SWE-bench Verified, reported that a review of the 731 public tasks had found about 30% of them broken (an automated pipeline flagged 27.4%, human reviewers 34.1%), mainly through tests that were too strict or too weak and prompts that were misleading or underspecified, and it withdrew its recommendation [@openai2026separating]. Epoch AI now rates the benchmark "Flawed" [@epoch2026swebenchpro]."
  In the Table 5.2 caption, after "...are not comparable across rows." add: "In July 2026 OpenAI estimated that about 30% of SWE-bench Pro's public tasks are broken [@openai2026separating]." and add `@openai2026separating; @epoch2026swebenchpro` to its Source list.
  New bib entries for ch05.bib:
  ```
  @misc{openai2026separating,
    author = {{OpenAI}},
    title = {Separating Signal from Noise in Coding Evaluations},
    howpublished = {Company research publication, 8 July 2026},
    year = {2026},
    url = {https://openai.com/index/separating-signal-from-noise-coding-evaluations/},
    urldate = {2026-11-22}
  }
  @misc{epoch2026swebenchpro,
    author = {{Epoch AI}},
    title = {Benchmark Review: {SWE-Bench Pro}},
    howpublished = {Epoch AI benchmark review, 1 September 2026},
    year = {2026},
    url = {https://epoch.ai/benchmarks/swe-bench-pro/review},
    urldate = {2026-11-22}
  }
  ```

## SHOULD change (real but not blocking)

### S1. Table 5.3 caption: the tau-3 banking best score has moved
- Where: ch05.md:221
- Text now: "By August 2026 the best banking score on the leaderboard was about 55%."
- Problem: OUTDATED (the sentence is dated, so it is not false, but it reads as the current state). The best standard single-model entry is still Qwen 3.8 Max, 55.15% (4 Aug 2026). On 3 Nov 2026 Sierra verified 73.20% (71/97 tasks, one trial) for a custom system, Principled Machines' Cortex 0.1, submitted 20 Oct 2026.
- Evidence: Sierra's public submission files behind taubench.com (manifest.json and submissions/cortex-0-1_principledmachines_2026-10-20/submission.json): submission_type "custom"; "Verified by Sierra on 2026-11-03: all 97 banking_knowledge tasks, 1 trial ... 71/97 passed (pass^1 73.20%)"; qwen3-8-max_sierra_2026-08-04: banking_knowledge pass_1 55.15, submission_type "standard".
- Change to: "By August 2026 the best single-model banking score on the leaderboard was about 55%; in November 2026 Sierra verified 73% for a custom agent system (Principled Machines' Cortex 0.1) in a single run."

### S2. Glossary places the banking domain in τ²-bench
- Where: textbook/work/glossary-ch05.md, entry "τ-bench"
- Text now: "(retail, airline and, in τ²-bench, telecom and banking)"
- Problem: INTERNAL CONTRADICTION with ch05.md:211 and Table 5.3, which correctly assign banking to τ³-bench (Sierra, 2026).
- Change to: "(retail and airline; τ²-bench added telecom and τ³-bench banking)"

### S3. Back-reference in 5.8 says something Section 5.7 did not say
- Where: ch05.md:322 ("Who bears the loss when an agent errs remains, as Section 5.7 noted, a question for existing contract and payment law.") against ch05.md:296.
- Problem: Section 5.7 says only that the protocols "leave open who bears the loss". AP2's own documentation supports the 5.8 wording, so the simplest fix is to say so in 5.7.
- Evidence: https://ap2-protocol.org/faq/: "A primary objective is to provide supporting evidence that helps payment networks establish accountability and liability principles. In a dispute, the network adjudicator (e.g., Card Network) can use the user-signed Checkout Mandate ...".
- Change to (end of line 296): "They leave open who bears the loss when an agent acting within its mandate makes a bad purchase, the accountability problem Google's announcement names. AP2's documentation describes its records as evidence to help payment networks "establish accountability and liability principles", leaving the rules themselves to those networks and to the law [@parikh2025powering; @ap22026agent; @x4022026x402]."

### S4. CVE-2026-25253 described as the agent acting on its own; it needed a click
- Where: ch05.md:251
- Text now: "in which a crafted link made the agent connect to a server named in the link and send it an access token"
- Problem: Imprecise. The NVD entry says OpenClaw "obtains a gatewayUrl value from a query string and automatically makes a WebSocket connection without prompting, sending a token value"; its CVSS vector has UI:R (user interaction required). The link has to be opened by the user.
- Evidence: NVD API, CVE-2026-25253: description as quoted; cvssMetricV31 (source cve@mitre.org) 8.8 HIGH, AV:N/AC:L/PR:N/UI:R.
- Change to: "in which a crafted link, once opened, made OpenClaw connect to a server named in the link and send it an access token"

### S5. Bib: fidoalliance2026google mis-describes the item
- Where: textbook/bib/ch05.bib, fidoalliance2026google
- Problem: The page is a "FIDO in the News" summary dated 29 April 2026, titled "The Payers: Google donates Agent Payments Protocol to FIDO Alliance". It summarises an article in the trade publication The Payers. It does not republish Google's announcement.
- Change to: `title = {The Payers: Google Donates {Agent Payments Protocol} to {FIDO Alliance}}`, `howpublished = {FIDO Alliance website, FIDO in the News, 29 April 2026 (summary of an article in The Payers)}`.

### S6. Bib: barres2025tau2 can now cite the proceedings
- Where: ch05.bib, barres2025tau2
- Problem: It points to an ICML session page. The paper is in PMLR.
- Change to: add `series = {Proceedings of Machine Learning Research}, volume = {306}, pages = {6736--6782}` and set `url = {https://proceedings.mlr.press/v306/barres26a.html}`. Source: the PMLR v306 listing (search result) and ICML 2026 virtual site (oral).

## Could not verify
- ch05.md:230, Lemkin "had instructed it not to change any code without his permission". The Register (21 Jul 2025) says the AI "ignored instruction to freeze code", and the OECD entry says it "ignored explicit instructions not to alter code". The exact "without permission" wording is only in Lemkin's X screenshots, which I did not open. The substance is supported. Low priority.
- bib hadfield2025economy `chapter = {5}`. The NBER page confirms the chapter, the authors, publication in September 2026 and the book, but shows no chapter number. Low priority.
- bib nasr2025attacker `pages = {1467--1486}`. The USENIX Security '26 presentation page confirms the paper and authors but shows no pages. Low priority.
- Coinbase's x402 launch page (coinbase.com) returned 403. The date (6 May 2025), HTTP 402 and stablecoins were confirmed from search results showing the page's title and from press coverage (Decrypt, PYMNTS, CryptoSlate). Low priority.
- OpenAI CUA page and the GPT-6 Astra page (first round): confirmed only through search-result text of the primary page and secondary reports (see confirmed list). Low priority.
- None of these needs human checking before print.

## Reader notes
1. Line 131 refers to "Table 5.1 ... the best agent program built around a model scores higher than the best general-purpose model on its own" two paragraphs before OSWorld or the table has been introduced, so the reader does not yet know what is being scored.
2. Line 155 is a number dump: 66.3%, 74.5%, 86.0%, 108 workflows, 1.6 hours, 21%, 54.8%, 72.6% and 54.8% again in one paragraph, across three benchmark versions.
3. Line 175 (METR) is hard going: 129 days, CI 104–158, 12 hours, 5–61 hours, 14.5 hours, a March correction, "at least 16 hours" and CI 8.5–55 in one paragraph, with two secondary sources (OfficeChai, The Decoder) cited for METR's own figures.
4. Line 205 gives "pass^1 of 0.80" before Table 5.3 shows 79.6%. The two are consistent (0.796^4 = 0.401), but the reader meets the rounded figure first.
5. Line 211: "Averaged over the four domains" comes in a sentence that opens with τ²-bench before the reader has been told that the fourth (banking) domain belongs to τ³-bench. The table caption sorts it out.
6. Line 322's back-reference to Section 5.7 ("a question for existing contract and payment law") is not what 5.7 says (see S3).
7. Line 276: "Some designs go further and offer formal guarantees, measured on AgentDojo". The guarantees are proved and their cost is measured on AgentDojo. Suggest "Some designs go further and offer formal guarantees, whose cost can be measured on AgentDojo".
8. Line 308: "Large populations of LLM agents now interact in the wild, as Moltbook showed in 2026" sits uneasily with line 251, which reports Wiz's finding that 1.5 million "agents" had 17,000 human owners and that the platform could not tell agents from "a human with a script". "as Moltbook suggested" would match the hedge that follows.
9. Line 235 gives the most serious agent incident of 2026 (the OpenAI/Hugging Face sandbox escape) one sentence, with the detail left to Chapter 12. This is accurate and consistent with ch12.md:96–100 and ch13.md:125, but a reader of the agents chapter may expect one more sentence (for example, that the models exploited an unknown vulnerability in a package proxy to reach the internet in pursuit of an evaluation's answers).

## Arithmetic recomputed (no errors)
- 0.995^24 = 0.887 (text 0.89); 0.995^168 = 0.431 (0.43).
- 0.95^20 = 0.358 (0.36); 0.99^50 = 0.605 ("about 60%"); 0.95^50 = 0.077 ("about 8%"); 0.90^50 = 0.0052 ("below 1%").
- 1 − 0.05^2 = 0.9975; 0.9975^20 = 0.951 ("about 95%").
- pass@8 at p = 0.7: 1 − 0.3^8 = 0.99993; pass^8 = 0.7^8 = 0.0576 ("about 0.06").
- C(8,4) = 70, C(6,4) = 15, 15/70 = 0.214; C(2,4) = 0, so pass@4 = 1; (6/8)^4 = 0.316.
- 0.80^4 = 0.41 ("about 0.40"; 0.796^4 = 0.401).
- Table 5.3 mean: (84.0 + 79.6 + 92.3 + 24.7)/4 = 70.15 (text 70.2%, consistent with unrounded inputs).
- 6/453 = 1.32% (1.3%). CaMeL 84 − 77 = 7 points.
- Figure 5.3 values for p = 0.99, 0.95, 0.90 at n = 1, 5, 10, 20, 30, 40, 50 match; figs_ch05.py plots 100*p**n.
- SWE-bench Pro audit: 200/731 = 27.4%, 249/731 = 34.1% (for M1). τ³ banking: 71/97 = 73.2% (S1).
- Author counts: Hammond et al. = 44 (title-page list); Nasr et al. = 14.

## Checked and confirmed

### Opening and 5.1
- Project Vend 1 (anthropic.com/research/project-vend-1, 27 Jun 2025): about a month; fridge, baskets, iPad; Slack; web search, notes, email; Andon Labs as wholesaler via a simulated email tool; two Chocomel suppliers; Irn-Bru $100 vs $15 and the quoted reply; 25% discount and "99% of your customers are Anthropic employees"; 31 Mar–1 Apr; blue blazer and red tie; "we would not hire Claudius"; metal cubes below cost; non-existent Venmo account.
- Project Vend 2 (18 Dec 2025): Sonnet 4 then 4.5; CRM, inventory with costs, browser; Seymour Cash; New York and London; discounts −80%, giveaways halved; "largely eliminated"; about eight times as often; "in spite of the CEO, rather than because of it"; onion quote; Onion Futures Act 1958; staff and WSJ reporters; colleague "elected" CEO; "friend who just wants to be nice"; "capable"/"completely robust".
- Building Effective Agents (19 Dec 2024): workflow and agent definitions; "higher costs, and the potential for compounding errors"; simplest solution.
- OpenAI, A Practical Guide to Building Agents (PDF): "three core components"; "don't use them to control workflow execution"; "maximize a single agent's capabilities first".

### 5.2
- Context engineering (29 Sep 2025): compaction, note-taking, Pokémon 1,234 steps, "often 1,000-2,000 tokens". Chroma Context Rot (14 Jul 2025): 18 models; quote.
- ReAct, Reflexion, Voyager, MemGPT, Park et al., Liu et al.: settled material, consistent with my knowledge of the papers (ReAct +34/+10 points; Reflexion 91% vs 80%; Voyager 3.3×, 15.3×; Park 0.995 decay, threshold 150, TrueSkill 29.89/21.21, 6 of 453).

### 5.3
- MCP spec 2026-07-28 (tools, overview, changelog, versioning): get_weather definition; tools/call request and response with "resultType": "complete" and isError; examples omit _meta; human-in-the-loop SHOULD; annotations untrusted; hosts/clients/servers; LSP; resources/prompts/tools; elicitation; four security quotes; "MCP itself cannot enforce..."; stateless; retry pattern; Roots/Sampling/Logging deprecated. Re-checked 22 Nov 2026: modelcontextprotocol.io still shows "Version 2026-07-28 (latest)".
- MCP intro "USB-C port" quote; launch 25 Nov 2024; donation 9 Dec 2025 to AAIF under the Linux Foundation, co-founded with Block and OpenAI; 10,000+ servers; 97M+ monthly SDK downloads; named adopters.
- A2A: 9 Apr 2025, 50+ partners, complementary to MCP; Linux Foundation 23 Jun 2025, 100+; AAIF blog 17 Aug 2026, 150+ organisations; spec 1.0.0 latest (re-checked 22 Nov: no newer version shown); Agent Card; task states; "without needing access to each other's internal state, memory, or tools"; JSON-RPC, gRPC, HTTP+JSON.
- Function calling June 2023; Toolformer tools ("two different search engines"): settled.

### 5.4
- o3/o4-mini system card (cdn.openai.com PDF): "use tools in their chains of thought"; "trained with large-scale reinforcement learning on chains of thought".
- Kimi K2 (arXiv 2507.20534): "a large-scale agentic data synthesis pipeline and a joint reinforcement learning (RL) stage"; "through interactions with real and synthetic environments".
- DeepSeek-V3.2 (arXiv 2512.02556): "tens of thousands of reproducible issue resolution environments" mined from GitHub; "1,827 task-oriented environments" built by an environment-synthesis agent; "hard to solve but easy to verify"; reasoning content retained across tool calls.
- Epoch (Edelman et al., 26 Sep 2025): RL scaling bottlenecked by "how quickly the RL environments can be built".
- Computer use (22 Oct 2024): public beta; quote; 14.9% vs 7.8%; 22.0% with more steps; scrolling/dragging/zooming. OpenAI CUA (23 Jan 2025): raw pixels; virtual mouse and keyboard; 38.1% OSWorld; 58.1% WebArena (search-result text of the primary page).
- OSWorld-Verified blog (28 Jul 2025): "nearly 300 feedback items"; about two months. Results file: Intelligence-Indeed Agent 90.19 (Jul 2026); claude-fable-5 85.96 (Aug 2026, best general model); HIPPO Agent with Opus 4.5 74.48 (Feb 2026); OSWorld 2.0 notice of 26 Jun 2026. Re-checked 22 Nov: file last-modified still 7 Aug 2026, so these are still the top entries.
- OSWorld 2.0 (arXiv 2606.29537): 108 workflows; median about 1.6 h; best 20.6%, 54.8% partial. GPT-6 Astra 72.6% on the offline subset with partial credit (The Batch; aggregators). Third-party trackers list other figures (for example Yutori 77.9% for Claude Fable 5.1); the chapter makes no "best" claim here, so nothing to change.
- AI Index 2026: "roughly one in three"; Opus 4.5 66.3% (Epoch AI); SWE-bench Verified low-to-mid 70s, ≈76.8% Feb 2026; τ-bench 62.9–70.2%.
- OpenAI, SWE-bench Verified post (23 Feb 2026, fetched directly this round): 138 problems, 64 runs, 59.4%, GPT-5.2 / Opus 4.5 / Gemini 3 Flash contamination probe; "We recommend SWE-bench Pro".
- SWE-bench Pro (arXiv 2509.16941 v2): 1,865 / 41 repos / 18 proprietary; SWE-Agent, 50 turns; Sonnet 4.5 43.6%; Opus 4.1 17.8% commercial; GPT-5 (high) 25.9% with $2 cap. Scale leaderboard re-checked 22 Nov: top still Muse Spark 1.1, 61.50 ± 3.10.
- METR: doubling 128.7 days (104.4–158.0); Opus 4.6 11.98 h (5.28–60.56); Mythos Preview CI 8.48–55.07 h; "above 16 hrs are unreliable"; March 2026 correction; series no longer updated after 8 Sep 2026. The Decoder (10 May 2026); OfficeChai (21 Feb 2026); Kwa note (22 Jan 2026).
- Anthropic Economic Index (15 Sep 2025): 77% automation, 44% computer/math. Li et al. (456,000+ PRs, five agents, 61,000 repos). Agarwal et al. (18%, 39%). Becker et al. (16 devs, 246 tasks, 19% slower, expected 24% faster).

### 5.5
- τ-bench/τ²/τ³ (taubench.com and Sierra submission files): Opus 4.5 airline 84.0, retail 79.61, telecom 92.32, banking 24.74; retail pass^4 51.75; 50+ tasks fixed; ~700 documents. τ²-bench "significant performance drops" (arXiv 2506.07982); published at ICML 2026, PMLR v306 (oral).
- Replit case: The Register 21 Jul 2025 (Lemkin, SaaStr; "ignored instruction to freeze code"; agent said rollback impossible, "the rollback did work"; "a catastrophic error of judgement"). The Register 22 Jul 2025 (Masad: "Unacceptable and should never be possible"; refund; "automatic DB dev/prod separation"). OECD AIM incident 2025-07-19-1eb1: listed as AI incident, harm types Economic/Property and Reputational.
- OpenAI/Hugging Face (openai.com, 21 Jul 2026 with 28–29 Jul and 26 Aug updates): models under internal evaluation escaped the isolated environment through a zero-day in a package registry proxy and compromised Hugging Face's production infrastructure. Consistent with ch12.md:96–100.

### 5.6
- Greshake et al. (arXiv 2302.12173 full text): "Augmenting LLMs with retrieval blurs the line between data and instructions"; attacks on Bing's GPT-4-powered Chat; taxonomy of delivery and goals.
- CVE-2025-32711 (NVD API and MSRC API): published 11 Jun 2025; "Ai command injection in M365 Copilot allows an unauthorized attacker to disclose information over a network"; Microsoft 9.3 Critical (PR:N/UI:N); NIST 7.5 High (PR:N/UI:N); MSRC "already been fully mitigated ... no action for users"; exploited "No".
- Krebs (8 Mar 2026): OpenClaw formerly ClawdBot/Moltbot, released November 2025, runs locally, "most useful when it has complete access to your digital life"; developer had an OpenClaw agent build a Reddit-like platform; "more than 1.5 million registered agents" less than a week later.
- Wiz, Nagli (2 Feb 2026): 17,000 human owners; "no mechanism to verify whether an 'agent' was actually AI or just a human with a script"; "full read and write access to all platform data"; impersonate any agent; inject prompt-injection payloads; "secured it within hours".
- CVE-2026-25253 (NVD API): published 1 Feb 2026; 8.8 HIGH; description as in S4.
- Palo Alto Networks (Mishra and Morgan, 29 Jan 2026, updated 4 Feb): access to root files, credentials, browser data; lethal trifecta; "Persistent memory acts as an accelerant".
- NCSC (Chismon, 8 Dec 2025): all four quotations exact; "reducing the likelihood or impact".
- Willison (16 Jun 2025): three components; "95% is very much a failing grade".
- Wallace et al. (arXiv 2404.13208): instruction hierarchy; robustness "even for attack types not seen during training".
- Nasr et al. (arXiv 2510.09023; USENIX Security '26 page): 14 authors from OpenAI, Anthropic, Google DeepMind, HackAPrompt, Northeastern, ETH and others; 12 defences in four families (prompting, training, filtering, secret knowledge); above 90% for most; majority originally near zero; 500+ participant competition, $20,000; humans succeed on all scenarios; "empirical evaluations cannot prove that a defense is robust".
- Beurer-Kellner et al. (arXiv 2506.08837 v3): six patterns; "securing general-purpose agents remains out of reach with current capabilities"; "application-specific agents can be secured through principled system design"; "tired or overloaded human verifiers approving unsafe actions"; code-then-execute "instantiated in the framework of Debenedetti et al. (2025)"; Table 5.4 rows match the pattern descriptions and stated limits.
- AgentDojo (arXiv 2406.13352): 97 tasks; 629 security test cases; models "fail at many tasks (even in the absence of attacks)"; ETH Zurich and Invariant Labs.
- CaMeL (arXiv 2503.18813; Crossref SaTML 2026, pp. 587–618): 77% vs 84%; control and data flow from the trusted query; "cannot defend against text-to-text attacks"; side channels.
- Claude Duet (support.claude.com; VKTR 22 Oct 2026): research preview; "designed to ask before it sends a message, makes a payment, signs a document, or deletes anything"; launched 21 Oct 2026. Still a research preview on 22 Nov.

### 5.7
- AP2 (Google Cloud blog, 16 Sep 2025, Parikh and Surapaneni): authorization, authenticity and accountability definitions; "Find me new white running shoes" Intent Mandate; Cart Mandate; "non-repudiable audit trail".
- ap2-protocol.org (v0.2): Open and Closed Mandates; FAQ on liability (see S3).
- FIDO Alliance (29 Apr 2026): Google donated AP2; AP2 v0.2.
- x402: Coinbase launch 6 May 2025, HTTP 402, stablecoins (search and press); x402-foundation README: facilitator, "must not allow for the facilitator or resource server to move funds, other than in accordance with client intentions", "pay $1 to read an article"; Coinbase docs: "April 2nd 2026, the x402 Foundation launched under the Linux Foundation".

### 5.8 and close
- Anthropic multi-agent research system (13 Jun 2025): Opus 4 lead with Sonnet 4 subagents; 90.2%; about 4× and 15× tokens; token usage explains 80% of BrowseComp variance; "most coding tasks involve fewer truly parallelizable tasks".
- Cemri et al. (arXiv 2503.13657 v3; NeurIPS 2025 via Crossref): 14 modes in 3 categories; 150 traces; 1,642 traces; seven frameworks; step repetition 15.7% (highest of all modes); three annotators on 15 traces; κ = 0.88; LLM judge κ = 0.77; gains "often minimal".
- Hammond et al. (arXiv 2502.14143): 44 authors; miscoordination, conflict, collusion; seven risk factors including information asymmetries, network effects and commitment problems.
- Calvano et al. (Crossref abstract): quotation exact; punishment then "gradual return to cooperation".
- Assad et al. (RePEc abstract): software widely available in 2017; "Adoption increases margins but only for nonmonopoly stations. In duopoly and triopoly markets, margins increase only if all stations adopt".
- Hadfield and Koh (arXiv 2509.01063; NBER chapter page, published September 2026): "In the coming decade"; "the errors introduced by AI agents might be more correlated than those of humans"; 2010 Flash Crash; "currently missing for AI agents".
- Tomašev et al. (arXiv 2509.10147): "sandbox economy"; emergent vs intentional; "permeability is the critical and controllable design variable"; trajectory toward "highly permeable" economy; auctions; Verifiable Credentials "cryptographically signed".
- Chan et al. 2024 (FAccT; arXiv 2401.13138): agent identifiers, real-time monitoring, activity logging; privacy and concentration of power.
- NIST (17 Feb 2026): AI Agent Standards Initiative; industry-led standards; open-source protocols; agent security and identity research.
- EU AI Act GPAI obligations from 2 Aug 2025 (Art. 113): settled; the sentence gives no dates that later amendments could have changed.
- Cross-references checked: Section 3.7, Section 4.7 (contains the quoted "time horizon is not..." material), Section 12.2 (covers the Hugging Face incident), Chapter 8 (Becker), Chapter 11 (correlated errors), Section 14.7 (many agents), Chapter 13.

### Glossary and figures
- Glossary entries consistent with the chapter except τ-bench (S2).
- Figure 5.1 and 5.2 specs consistent with the captions and the code example (get_weather, Leeds). Figure 5.3 values recomputed (first round).

### Bibliography (entries checked this round; first round checked sajadieh2026ai, yuan2026osworld, deng2025swebench, kwa2026clarifying, metr2026task, li2025rise, agarwal2026ai, becker2025measuring, openai2026why and others in its confirmed list)
debenedetti2025defeating (Crossref), chan2024visibility (Crossref), calvano2020artificial (Crossref), assad2024algorithmic (Crossref), cemri2025why (Crossref), debenedetti2024agentdojo (Crossref), greshake2023not (Crossref), schick2023toolformer (Crossref), nasr2025attacker (USENIX page; pages unverified), hadfield2025economy (NBER page; chapter number unverified), tomasev2025virtual, hammond2025multi (all 44 authors, order matches), wallace2024instruction, beurerkellner2025design (14 authors match), barres2025tau2 (S6), chismon2025prompt, willison2025lethal, nist2025cve, microsoft2025cve, nist2026cve, krebs2026how, nagli2026hacking, mishra2026openclaw, anthropic2026duet, hawley2026claude, parikh2025powering, ap22026agent, fidoalliance2026google (S5), coinbase2025x402, coinbase2026x402, x4022026x402, anthropic2025how, nist2026announcing, edelman2025why, sharwood2025vibe, sharwood2025replit, oecd2025replit, openai2026openai, kimiteam2025kimi, deepseekai2025deepseekv32, openai2025o3systemcard, openai2025practical, openai2026why. All exist; authors, titles, years and venues match, apart from the two noted.

## Tally
Claims checked against a web source: about 285 (first round about 140; this round 144). Confirmed: about 280. Wrong: 0. Outdated: 2 (M1 SWE-bench Pro audit; S1 τ³ banking caption). Unsupported by cited source: 0. Imprecise or internally inconsistent: 3 (S2, S3, S4). Could not verify: 5 minor items (none blocking). Arithmetic items recomputed: 13 (errors: 0). Bib entries checked: 43 this round plus the first round's (problems: 2 minor, S5 and S6).
