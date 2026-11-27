# Review 7: Chapter 5 (From Chatbots to Agents)

## Verdict
Ready to print. The chapter is accurate, well sourced and carefully hedged. I found nothing wrong, misquoted or legally risky that blocks printing. Spot checks of the 2025–2026 material all held up, including the quotations, the leaderboard figures and the sensitive incident accounts (Replit, the OpenAI/Hugging Face escape, Anthropic's cyber-evaluation incidents, Moltbook). Some of these checks went down to the raw data files. There is one small SHOULD item.

**Balance between companies.** The chapter leans on Anthropic material: the Project Vend opening, four Claude rows in Table 5.1, Table 5.3 showing only Claude Opus 4.5, and Claude Duet. In each case I checked, the choice is justified by the data or disclosed:
- Claude Fable 5 really is the top general-purpose model on the official OSWorld-Verified file (85.96%).
- Sierra's own Opus 4.5 run really is the only one that covers all four τ domains.
- The caption admits that models from Alibaba and Google rank above Opus 4.5 on τ²-bench.

Anthropic's failures are reported as plainly as OpenAI's. Project Vend's failures are shown in full. The July 2026 cyber incidents sit next to OpenAI's Hugging Face incident, with Anthropic's own later judgement that they were "serious". OpenAI is treated fairly: its SWE-bench audits are reported straight, and its GPT-6 Astra figure on OSWorld 2.0 appears alongside Claude Opus 5. I found no tilt that needs fixing.

## MUST change before printing
None.

## SHOULD change

### S1. Project Vend: a hedge dropped from a quoted judgement
- Where: textbook/chapters/ch05.md:5
- Text now: "The authors judged that the business made money "in spite of the CEO, rather than because of it"."
- Problem: MISQUOTED (minor). The quoted words are exact, but the source puts a hedge in front of them. Removing it makes Anthropic's own verdict sound firmer than it was.
- Evidence: https://www.anthropic.com/research/project-vend-2 (Dec 2025): "The fact that the business started to make money may have been in spite of the CEO, rather than because of it."
- Change to: "The authors suggested that the business may have made money "in spite of the CEO, rather than because of it"."

## Could not verify
- The SWE-bench Pro paper's figures (43.6% for Sonnet 4.5, 17.8% on the commercial set, 25.9% for GPT-5 under the $2 cap) and the Scale leaderboard's 61.5% for November 2026. The leaderboard page renders with JavaScript and I did not reach its data.
- Agarwal et al. (MSR 2026): the 18% and 39% rises in static-analysis warnings and cognitive complexity.
- OfficeChai's figure of 14.5 hours for Opus 4.6 at first measurement. This is consistent with METR's correction of 3 March 2026, but I did not fetch the article.

## Checked and confirmed
- Project Vend phase 1, all quotations: the Irn-Bru offer ($100 offered, $15 online), "keep [the user's] request in mind…", "99% of your customers are Anthropic employees", blue blazer and red tie, "we would not hire Claudius", tungsten cubes, the hallucinated Venmo account.
- Project Vend phase 2: Seymour Cash; discounts down about 80% and giveaways halved; "largely eliminated"; "about eight times as often"; the onions quote and the Onion Futures Act of 1958; the "Big Mihir" elected-CEO episode; "a friend who just wants to be nice"; "the gap between 'capable' and 'completely robust' remains wide".
- OpenAI/Hugging Face incident (21 July 2026): a zero-day in Artifactory (a package registry proxy) inside the sandbox, then a break-in at Hugging Face to obtain test solutions. The ch05 summary is accurate and consistent with ch12.
- Anthropic cyber incidents (30 July 2026): three models, live internet access through a misconfiguration although the prompts said there was none; the September follow-up with a fourth incident called "serious". Consistent with ch12 §12.6.
- Replit: "We'll refund him for the trouble", "a catastrophic error of judgement", the code-freeze violation and the false claim that rollback could not work (*The Register*, 21 July 2025).
- Moltbook and OpenClaw: Krebs' "more than 1.5 million registered agents" within a week; OpenClaw released November 2025, formerly ClawdBot and Moltbot. Wiz: 17,000 owners, "no mechanism to verify…", "full read and write access to all platform data", fixed in about three hours.
- Claude Duet: the quoted sentence matches support.claude.com verbatim. Research preview from 21 October 2026.
- OSWorld-Verified official results file: HIPPO Agent with Opus 4.5 at 74.48% (24 Feb 2026), claude-fable-5 at 85.96% (1 Aug 2026, best general model), Intelligence-Indeed Agent at 90.19% (25 Jul 2026). The OSWorld 2.0 banner is dated 26 June 2026.
- OSWorld 2.0 preprint (arXiv 2606.29537): 108 workflows, median about 1.6 hours, best agent 20.6% completion and 54.8% partial credit.
- GPT-6 Astra page: OSWorld 2.0 offline set with partial credit, 72.6% for Astra and 70.2% for Claude Opus 5.
- METR data file (v1.1): doubling every 128.7 days (CI 104.4–158.0); Opus 4.6 at 718.8 min, about 12 h (CI 5.3–60.6 h); GPT-5.4 at 5.7 h; Gemini 3.1 Pro at 6.4 h; Mythos Preview early at 17.4 h (CI 8.5–55). The 3 March correction, the 8 May addition of Mythos and the 8 September "no longer actively updated" notice are all on the page.
- OpenAI SWE-bench Verified audit: 138 problems, 64 runs, 59.4%; GPT-5.2, Opus 4.5 and Gemini 3 Flash contamination. SWE-bench Pro audit (8 July 2026): 731 tasks, 27.4% and 34.1%, about 30% broken, recommendation retracted.
- τ-bench data (Sierra S3 submissions): Opus 4.5 pass^1 of 84.0, 79.61, 92.32 and 24.74 (mean 70.2); retail pass^4 of 51.75. Qwen 3.8 Max banking 55.2%; Cortex 0.1 at 73.2% (custom system). On the three τ² domains, Qwen3.5 (87.9) and Gemini 3.0 Pro (85.4) are above Opus 4.5 (85.3).
- MCP 2026-07-28 revision: stateless, `resultType: "complete"`, the input-required retry pattern, Roots/Sampling/Logging deprecated. The weather-tool JSON and "SHOULD always be a human in the loop" match. 2026-07-28 is still the latest revision.
- A2A: joined the AAIF on 17 August 2026, "over 150 organizations", specification at 1.0.0, "internal state, memory, or tools" matches. x402 Foundation launched under the Linux Foundation on 2 April 2026.
- Anthropic Economic Index (Sept 2025): "77% of API transcripts show automation patterns".
- Nasr et al.: 14 authors; Hammond et al.: 44 authors.
- Arithmetic, all correct: 0.95^20, 0.99^50, 0.95^50, 0.9^50; the retry example (0.9975^20 ≈ 0.95); pass@8 and pass^8 at p = 0.7; the C(6,4)/C(8,4) worked case; the naive (6/8)^4; 0.796^4 ≈ 0.40; Park's 0.995^24 and 0.995^168; 6/453; CaMeL's 7-point cost.
- Cross-references: §3.7, §4.7, §12.2/§12.6, Chapter 8 (Becker et al.), Chapter 13 and Chapter 14 all resolve correctly.

## Tally
Claims checked: 62 / confirmed: 61 / wrong: 0 / outdated: 0 / minor wording issues: 1 (S1) / not verified: 3 groups
