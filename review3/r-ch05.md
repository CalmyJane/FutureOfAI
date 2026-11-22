# Third review: Chapter 5 — From Chatbots to Agents

STATUS: WORKING DRAFT (first version, written before web verification; being appended to).

## Verdict
(pending: web verification in progress)

## MUST change before printing
(none recorded yet)

## SHOULD change (real but not blocking)
(none recorded yet)

## Could not verify
(none recorded yet)

## Reader notes (first read, before fact-check)
1. Line 131 refers to "Table 5.1 ... the best agent program built around a model scores higher than the best general-purpose model on its own" two paragraphs before OSWorld or the table have been introduced; a reader does not yet know what is being scored.
2. Line 155 is a number dump: 66.3%, 74.5%, 86.0%, 108 workflows, 1.6 hours, 21%, 54.8%, 72.6%, 54.8% again, in one paragraph, with three different benchmark versions.
3. Line 175 (METR paragraph) is hard going: 129 days, CI 104-158, 12 hours, 5-61 hours, 14.5 hours, a March correction, "at least 16 hours", CI 8.5-55, all in one paragraph and with two secondary sources (OfficeChai, The Decoder) for METR's own figures.
4. Line 205: "pass^1 of 0.80 would predict a pass^4 of about 0.40" while Table 5.3 gives retail pass^1 as 79.6%; consistent on rounding (0.796^4 = 0.401), fine, but the reader meets 0.80 before the table.
5. Line 211 "Averaged over the four domains" comes before the reader has been told clearly that the fourth (banking) domain belongs to tau-3-bench, while the sentence opens with tau-2-bench; the table caption sorts it out.
6. Line 322 "Who bears the loss ... remains ... a question for existing contract and payment law" — Section 5.7 (line 296) said the protocols "leave open who bears the loss"; it did not say the question is one for existing contract and payment law. Minor mismatch in the back-reference.

## Arithmetic recomputed (no errors so far)
- 0.995^24 = 0.887 (text 0.89), 0.995^168 = 0.431 (text 0.43). OK.
- 0.95^20 = 0.358 (0.36). 0.99^50 = 0.605 ("about 60%"). 0.95^50 = 0.077 ("about 8%"). 0.90^50 = 0.0052 ("below 1%"). OK.
- 1 - 0.05^2 = 0.9975; 0.9975^20 = 0.951 ("about 95%"). OK.
- pass@8 at p=0.7: 1 - 0.3^8 = 0.99993; pass^8 = 0.7^8 = 0.0576 ("about 0.06"). OK.
- C(8,4)=70, C(6,4)=15, 15/70 = 0.214; C(2,4)=0 so pass@4 = 1; (6/8)^4 = 0.316. OK.
- 0.80^4 = 0.41 ("about 0.40"; 0.796^4 = 0.401). OK.
- Table 5.3 mean: (84.0+79.6+92.3+24.7)/4 = 70.15 (text 70.2%). OK within rounding of inputs.
- 6/453 = 1.32% (text 1.3%). OK.
- CaMeL 84 - 77 = 7 points. OK.
- Figure 5.3 spec values recomputed for p = 0.99, 0.95, 0.90 at n = 1, 5, 10, 20, 30, 40, 50: all match; figs_ch05.py plots 100*p**n directly.

## Checked and confirmed
(pending)

## Tally
(pending)

---
## INTERIM FINDINGS LOG (pass 1, sections opening–5.5; to be merged into the final structure above)

### Candidate MUST: SWE-bench Pro presented as the working successor; July 2026 OpenAI audit not mentioned
- Where: ch05.md:165 and Table 5.2 (line 171)
- OpenAI post "Separating signal from noise in coding evaluations", 8 July 2026 (openai.com/index/separating-signal-from-noise-coding-evaluations; 403 to me), reported by The Decoder 9 Jul 2026 (https://the-decoder.com/openai-finds-roughly-30-percent-of-popular-ai-coding-test-is-broken/), Gigazine 9 Jul 2026, Faros 16 Jul 2026: on the 731 public tasks, pipeline flagged 200 (27.4%) as broken, five human developers flagged 249 (34.1%), OpenAI estimates ~30% broken and withdrew its earlier recommendation of SWE-bench Pro. Not in evidence-ch05.md.

### Candidate SHOULD: tau-3 banking caption
- Table 5.3 caption "By August 2026 the best banking score on the leaderboard was about 55%": still the best standard (single-model) entry (Qwen 3.8 Max 55.15, 4 Aug 2026). A custom system (Principled Machines Cortex 0.1) was verified by Sierra on 3 Nov 2026 at 73.2% (submission.json in Sierra's public bucket).

### Confirmed so far (source opened)
- Vend 1 (anthropic.com/research/project-vend-1): 27 Jun 2025; "about a month"; fridge, baskets, iPad; Slack; web search/notes/email; Andon Labs as wholesaler via non-real email tool; two Chocomel suppliers; Irn-Bru $100 vs $15, quote; 25% discount, "99% of your customers are Anthropic employees"; 31 Mar–1 Apr; blue blazer/red tie; "we would not hire Claudius"; metal cubes below cost; made-up Venmo account.
- Vend 2 (project-vend-2): 18 Dec 2025; Sonnet 4 then 4.5; CRM, cost-visible inventory, browser; Seymour Cash; NY and London; discounts −80%, giveaways halved; "largely eliminated"; "about eight times as often"; "in spite of the CEO, rather than because of it"; onion quote; Onion Futures Act 1958; staff + WSJ reporters; Mihir "elected" CEO; "friend who just wants to be nice"; "capable"/"completely robust".
- Building Effective Agents (19 Dec 2024): both definitions, "higher costs, and the potential for compounding errors", simplest solution.
- Context engineering (29 Sep 2025): compaction, note-taking, 1,234 steps Pokémon example, "often 1,000-2,000 tokens".
- Chroma Context Rot (14 Jul 2025): 18 models; "model performance consistently degrades with increasing input length".
- MCP spec 2026-07-28 (tools, overview, changelog, versioning pages): get_weather definition verbatim; tools/call request and response incl. "resultType": "complete" and isError; examples omit required _meta; SHOULD human in the loop; annotations untrusted; hosts/clients/servers; LSP inspiration; resources/prompts/tools; elicitation; all four security quotes; "MCP itself cannot enforce..."; stateless; MRTR retry; Roots/Sampling/Logging deprecated; 2026-07-28 still "current" on 11 Nov 2026.
- MCP intro: "Think of MCP like a USB-C port for AI applications."
- MCP launch 25 Nov 2024, open standard. Donation 9 Dec 2025: AAIF under Linux Foundation, co-founded Anthropic/Block/OpenAI; "more than 10,000" servers; "97M+" monthly SDK downloads; ChatGPT, Cursor, Gemini, Microsoft Copilot, VS Code.
- A2A: 9 Apr 2025, "more than 50 technology partners", complements MCP; LF 23 Jun 2025 "more than 100"; AAIF blog 17 Aug 2026 "over 150 organizations"; spec 1.0.0 latest; Agent Card; task states; "without needing access to each other's internal state, memory, or tools"; JSON-RPC, gRPC, HTTP+JSON bindings.
- Computer use (22 Oct 2024): public beta; quote; 14.9% vs 7.8%; 22.0% with more steps; scrolling/dragging/zooming.
- OpenAI CUA (openai.com 403; confirmed via search-result text of the primary page): 23 Jan 2025; raw pixel data; virtual mouse and keyboard; 38.1% OSWorld; 58.1% WebArena.
- OSWorld-Verified blog 28 Jul 2025: "nearly 300 feedback items"; ~two months; categories.
- OSWorld-Verified results file (osworld-v1.xlang.ai/static/data/osworld_verified_results.xlsx, last-modified 7 Aug 2026, fetched 11 Nov 2026): Intelligence-Indeed Agent 90.19 (25 Jul 2026, agentic framework); claude-fable-5 85.96 (1 Aug 2026, general model; best general model); HIPPO Agent w/ Opus 4.5 74.48 (25 Feb 2026). Still the top entries today. Notice "2026-06-26: OSWorld 2.0 is now available! Please visit OSWorld 2.0 for the latest version." confirmed.
- OSWorld 2.0 (arXiv 2606.29537, v1 28 Jun, v2 13 Jul 2026): 108 workflows; median ~1.6 h; best 20.6% at 54.8% partial.
- GPT-6 Astra 72.6% on offline subset of OSWorld 2.0 (The Batch 11 Sep 2026; partial-credit scoring per search-result text of datalearner/tabbit; openai.com 403).
- AI Index 2026 PDF (text extracted): "still fail roughly one in three attempts on structured benchmarks"; Claude Opus 4.5 66.3% OSWorld, Source Epoch AI, human 72.35%; SWE-bench Verified "low-to-mid 70s", ≈76.8% as of Feb 2026, mini-SWE-agent-v2 only; tau-bench pass@1 62.9–70.2%. arXiv 2606.15708 exists, 23 authors match bib.
- OpenAI "Why we no longer evaluate SWE-bench Verified" (23 Feb 2026; openai.com 403; search-result text of primary page): 138 problems, 64 runs, 59.4%.
- SWE-bench Pro (arXiv 2509.16941 v2 HTML): 1,865 / 41 repos / 18 proprietary from startups; SWE-Agent, 50 turns, augmented statements; Sonnet 4.5 43.6% (Table 1); Opus 4.1 17.8% commercial (Table 2); GPT-5 (high) 25.9% with $2 cap (Table 5).
- Scale leaderboard (fetched 11 Nov 2026): top Muse Spark 1.1 61.50; top entries run with mini-swe-agent.
- METR time-horizons page + benchmark_results_1_1.yaml: doubling 128.7 days (104.4–158.0) from 2023 on; Opus 4.6 11.98 h (5.28–60.56); Mythos Preview (early), release 7 Apr 2026, CI 8.48–55.07 h; "Measurements above 16 hrs are unreliable with our current task suite"; 3 Mar 2026 regularisation correction; "no longer actively updated", last updated 8 Sep 2026.
- The Decoder 10 May 2026 (Bastian): "at least 16 hours", CI 8.5–55. OfficeChai 21 Feb 2026: ~14.5 h. Kwa note 22 Jan 2026: quoted heading present.
- Anthropic Economic Index 15 Sep 2025: "77% of API transcripts show automation patterns"; 44% computer and mathematical.
- Li et al. arXiv 2507.15003: 456,000+ PRs, five agents, 61,000 repos. Agarwal et al. arXiv 2601.13597: 18% and 39%.
- Becker et al. arXiv 2507.09089: 16 devs, 246 tasks, 19% slower, expected 24% faster.
- tau2/tau3 (taubench.com + Sierra public submission.json): Opus 4.5 airline 84.0, retail 79.61, telecom 92.32, banking 24.74; retail pass^4 51.75; 50+ tasks fixed (Feb 2026); ~700 documents (Mar 2026). tau2 arXiv 2506.07982: "significant performance drops".
