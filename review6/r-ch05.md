# Review 6: Chapter 5, From Chatbots to Agents

## Verdict
Ready to print. I found nothing wrong, misquoted or legally risky. Every quotation and number I checked against its source matches, including the 2026 material: METR's data file, OpenAI's two SWE-bench audits, the MCP 2026-07-28 changelog, the A2A 1.0 specification, both incident disclosures, Claude Duet, the NVD records and the AI Index figures. All the worked arithmetic recomputes correctly. Two small wording fixes are listed below.

**Balance between companies.** The chapter names Anthropic models often: Project Vend, four of the seven rows in Table 5.1, Table 5.3, the METR examples and Claude Duet. In each case I checked, the source data support the choice:
- Claude models do top the METR series and the OSWorld-Verified board.
- Table 5.3's caption explains why it uses Claude Opus 4.5 (only Sierra's run reports all four domains for that model) and says that Alibaba and Google models rank above it.
- Anthropic's own failures get the same frankness as other companies' failures. Examples are "we would not hire Claudius", "in spite of the CEO", and Anthropic's cyber-evaluation incidents, reported next to OpenAI's Hugging Face breakout.
- The OpenAI material (SWE-bench audits, CUA, ChatGPT agent, GPT-6 Astra's OSWorld 2.0 lead over Claude Opus 5) is reported neutrally and credited where it is due.

I saw no favouring of any company and no over-correction. The Replit case is carefully hedged ("rests largely on one user's account").

## MUST change before printing
None.

## SHOULD change

### S1. When METR stopped updating its time-horizon series
- Where: textbook/chapters/ch05.md:175
- Text now: "The last model METR measured before it stopped updating the series in September 2026 was an early version of Claude Mythos Preview (April 2026)."
- Problem: UNCLEAR — METR's change log shows the last model added on 8 May 2026 (Mythos Preview, early). On 8 September 2026 METR only "Clarified that this page is no longer actively updated". So the series effectively stopped in May, not September. Also, METR says it measured the early Mythos version "during a limited time window in March 2026"; 7 April 2026 is the model's release date in METR's data.
- Evidence: https://metr.org/time-horizons/ (change log: "September 8th, 2026: Clarified that this page is no longer actively updated." / "May 8th, 2026: Added Claude Mythos Preview (early)…"); https://the-decoder.com/metr-says-it-can-barely-measure-claude-mythos-palo-alto-networks-warns-of-autonomous-ai-attackers/ (10 May 2026: "an early version of Claude Mythos Preview during a limited time window in March 2026").
- Change to: "The last model METR added to the series, in May 2026, before saying in September that the page was no longer updated, was an early version of Claude Mythos Preview (released April 2026)."

### S2. "Best general-purpose model" in Table 5.1 needs a date
- Where: textbook/chapters/ch05.md:150 and 155
- Text now: "Claude Fable 5 (best general-purpose model) | Aug 2026" and "by August the best general-purpose model, Anthropic's Claude Fable 5, reached 86.0%"
- Problem: UNCLEAR — the official leaderboard loads by script, and I could not read it directly to confirm the ranking as of November. Third-party mirrors agree on 86.0% (Yutori entry dated 1 Aug 2026; Developers Digest ranks it first as of 17 Oct 2026). However, BenchLM lists a self-reported Qwen3.8 Max at 86.1%, and Steel describes Fable 5's 86% as self-reported from the system card. The text body already says "by August". The table label should say the same, so it does not read as a claim about November.
- Evidence: https://yutori.com/leaderboards/osworld-verified.md (via search snippet); https://benchlm.ai/benchmarks/osworld-verified (via search snippet).
- Change to (table cell): "Claude Fable 5 (best general-purpose model, Aug 2026)"

## Could not verify
- That the 86.0% (Fable 5), 90.2% (Intelligence-Indeed) and 74.5% (Opus 4.5 framework) rows are *official re-runs*. The leaderboard page is rendered by JavaScript. Press coverage confirms 90.2% for Intelligence-Indeed's agent (announced 27 July 2026; reportedly a single run).
- Principled Machines' Cortex 0.1 at 73% verified by Sierra in November 2026. It does not appear in the taubench.com text I could fetch.
- Krebs's "less than a week after launch" (Wiz independently confirms the 1.5 million registered agents and 17,000 owners). The Palo Alto Networks "accelerant" quote. Cemri et al.'s kappa values. The human red-teaming details in Nasr et al. (not in the abstract).

## Checked and confirmed
- Project Vend 1: Sonnet 3.7, about a month, Irn-Bru $100/$15 and quote, "99% of your customers…", 31 March–1 April, blazer and tie, Chocomel, metal cubes, invented Venmo account, "we would not hire Claudius".
- Project Vend 2 (18 Dec 2025): Sonnet 4/4.5, Seymour Cash, SF/NY/London, about 80% fewer discounts, giveaways halved, "largely eliminated", 8:1 approvals, "in spite of the CEO…", onions and the 1958 Onion Futures Act, the elected-CEO episode, "friend who just wants to be nice", "capable/completely robust".
- MCP: AAIF donation on 9 Dec 2025 (Block, OpenAI; 10,000+ servers; 97M+ downloads; named adopters). The 2026-07-28 revision is stateless with per-request protocol version, `resultType: "complete"`, an input-required retry pattern, and Roots, Sampling and Logging deprecated.
- A2A: spec 1.0, quote about internal state, three bindings, task states. Joined AAIF on 17 Aug 2026, backed by "over 150 organizations".
- OSWorld 2.0 preprint (28 June 2026): 108 tasks, median 1.6 h, 20.6%/54.8%. GPT-6 Astra page: 72.6% vs Claude Opus 5 70.2% on the offline, partial-credit set. Banner dated 26 June 2026.
- AI Index 2026: OSWorld 66.3%, "one in three", SWE-bench Verified about 76.8% (Feb 2026, mini-SWE-agent), τ-bench 62.9–70.2%.
- OpenAI, 23 Feb 2026: 138 problems, 64 runs, 59.4%, GPT-5.2/Opus 4.5/Gemini 3 Flash recall, SWE-bench Pro recommended. July audit: 731 tasks, 27.4%/34.1%/about 30%, recommendation retracted. Epoch rates it "Flawed" (1 Sept 2026). Scale top score 61.5% (Muse Spark 1.1, mini-swe-agent).
- SWE-bench Pro paper: 43.6% (Sonnet 4.5), 17.8% (Opus 4.1 commercial), 25.9% GPT-5 high at a $2 cap, 50 turns, 1,865/41/18.
- METR data: Opus 4.6 718.8 min ≈ 12.0 h (CI 5.3–60.6 h); GPT-5.4 5.7 h; Gemini 3.1 Pro 6.4 h; doubling 128.7 days (104–158); Mythos at least 16 h (8.5–55); regularisation correction on 3 March 2026.
- τ-bench: Opus 4.5 combined τ² score 85.3% = mean of 84.0/79.6/92.3. Qwen 3.8 Max banking 55.2%. Qwen and Gemini above Opus 4.5. 50+ fixed tasks; about 700 documents.
- Incidents: OpenAI/Hugging Face (21 July 2026; zero-day in the package proxy; aimed at test solutions). Anthropic, three incidents (30 July 2026; prompt said no internet). Fourth incident, "these incidents are serious" (9 Sept 2026).
- Claude Duet quote, research preview opened 21 Oct 2026. NIST AI Agent Standards Initiative, 17 Feb 2026. AP2 to FIDO, 29 Apr 2026. x402 Foundation, 2 Apr 2026.
- CVE-2025-32711 (description, 9.3 Microsoft / 7.5 NIST, PR:N/UI:N). CVE-2026-25253 (description, 8.8). Wiz quotes, 17,000 owners, fix within hours.
- Replit: "catastrophic error of judgement", rollback claim false, CEO "Unacceptable", refund, dev/prod separation.
- Anthropic Economic Index "77%… automation patterns", "little less than half". Agarwal et al. at MSR '26, +18%/+39%.
- Arithmetic: 0.995^24 = 0.887; 0.995^168 = 0.431; 0.95^20 = 0.358; 0.99^50 = 0.605; 0.95^50 = 0.077; 0.9^50 = 0.005; 0.9975^20 = 0.951; 1 − 0.3^8 = 0.99993; 0.7^8 = 0.058; C(6,4)/C(8,4) = 15/70 = 0.214; 0.75^4 = 0.316; 0.796^4 = 0.401; Table 5.3 mean 70.15; CaMeL 84 − 77 = 7; Jensen-inequality claim correct.
- Cross-references: Sections 3.7, 4.7 (12 h, 129 days, 16 h consistent with ch04), 12.2 and 12.6 (incidents consistent with ch12), and Chapter 8 (Becker) all point to the right places.

## Tally
Claims checked: 118 / confirmed: 116 / wrong: 0 / outdated or imprecise: 2
