# Review 9 — Chapter 5: From Chatbots to Agents

## Verdict
Ready to print after three small SHOULD fixes. No MUST items. Quotations from Project Vend (both phases), the MCP 2026-07-28 changelog, METR's data file, the OSWorld-Verified leaderboard spreadsheet, the Anthropic and OpenAI incident posts, Claude Duet's help page, NVD entries and the MSR 2026 paper were checked against the live sources and match. All worked arithmetic recomputes correctly.

**Balance between companies.** Broadly even-handed, and I found no over-correction. The chapter opens with two paragraphs on Anthropic's Project Vend that report Claude's failures critically, and it flags the vendor interest twice. Section 5.5 reports OpenAI's Hugging Face escape and Anthropic's three (later four) real-world cyber-evaluation incidents side by side, with similar mitigating context for each. Anthropic models appear often in Tables 5.1 and 5.3 and in the METR paragraph, but each time this reflects the cited leaderboard data (verified below), and Table 5.3's caption says that Alibaba and Google models rank above Claude Opus 4.5. The Anthropic research-system figure (90.2%) is labelled "according to the company". The one place where only one vendor's comparison is given is the OSWorld 2.0 sentence (S3). There it favours OpenAI, not Anthropic, and the fix is to make the point vendor-neutral, not to add an Anthropic win.

## MUST change before printing
None.

## SHOULD change

### S1. "Developers' own agent programs … about 80%" is not what the source says
- Where: textbook/chapters/ch05.md:166 (and Table 5.2, line 172)
- Text now: "developers using their own agent programs reported up to about 80% by mid-2026 [@openai2026separating]"
- Problem: UNSUPPORTED — the OpenAI post gives the 80.3% figure without saying which harness produced it or who reported it. The attribution to "developers' own agent programs" is the book's inference.
- Evidence: https://openai.com/index/separating-signal-from-noise-coding-evaluations/ (8 July 2026): "On the 731-task public split, frontier models improved from a pass rate of 23.3% to 80.3% in eight months." The post does not name a scaffold.
- Change to: "OpenAI noted that frontier models' pass rates on the public set had risen from 23.3% to 80.3% in eight months [@openai2026separating]". In Table 5.2, change "up to ≈80% with developers' own agent programs (mid-2026)" to "frontier models up to 80.3% (mid-2026, per OpenAI)".

### S2. The mechanism of the OpenAI–Hugging Face incident is slightly misdescribed
- Where: textbook/chapters/ch05.md:236
- Text now: "the models exploited previously unknown vulnerabilities in a package service inside the sandbox to reach the internet, in pursuit of the evaluation's answers"
- Problem: UNCLEAR / slightly inaccurate — OpenAI describes one zero-day in a third-party package-registry proxy and cache (Artifactory), which gave the isolated benchmark its only network path. The models then moved laterally through the research environment to a node with internet access, and also used exposed credentials. "Vulnerabilities … inside the sandbox" compresses this inaccurately.
- Evidence: https://openai.com/index/hugging-face-model-evaluation-security-incident/ (21 July 2026; update of 28 July): the models "identified and chained vulnerabilities across OpenAI's research environment and Hugging Face's production infrastructure"; the update says they "identified and exploited a previously unknown zero-day vulnerability" in Artifactory, a package registry cache proxy; the models were "hyperfocused on finding a solution for ExploitGym".
- Change to: "According to OpenAI, the models exploited a previously unknown vulnerability in the package proxy that was the test environment's only network connection, moved through OpenAI's research network to a machine with internet access and, using exposed credentials, reached Hugging Face's systems in search of the evaluation's answers [@openai2026openai; @openai2026technical]."

### S3. OSWorld 2.0: only one vendor's comparison is reported
- Where: textbook/chapters/ch05.md:156
- Text now: "OpenAI reported 72.6% for GPT-6 Astra on a later, offline-only version of OSWorld 2.0 scored with partial credit, against 70.2% for Anthropic's Claude Opus 5 in the same table [@openai2026gpt6]; these figures are not comparable with the preprint's 54.8% on the full task set."
- Problem: UNCLEAR (balance) — the sentence is accurate. However, Anthropic's Claude Fable 5.1 system card (1 September 2026) reported its own OSWorld 2.0 figures on a different (August 2026) task release: 77.9% partial credit and 41.7% strict completion for Fable 5.1, and 75.4% for Opus 5. OpenAI's page says it re-ran Opus 5 under official settings, "not the modified tasks and grading from the Fable 5.1 system card". The reader sees only one vendor's head-to-head. The more useful point for the reader is that the two companies' figures disagree and that strict completion stays near 40%. Do not answer this by adding an Anthropic "win" (over-correction).
- Evidence: https://openai.com/index/gpt-6-astra/ (Sept 2026, updated to 17 Nov): "Claude Opus 5: 70.2% … reproduced … on the official leaderboard using official settings, not the modified tasks and grading from the Fable 5.1 system card". Fable 5.1 figures as reported by https://www.vellum.ai/blog/claude-fable-5-1-mythos-5-1-benchmarks-explained (I could not reach Anthropic's own page).
- Change to: append "Each developer's own runs on its own version of the tasks put its own model ahead, and Anthropic reported that even its best model fully completed only about 40% of the tasks under strict scoring [@openai2026gpt6; @anthropic2026fable51]." Add the bib entry only if the Fable 5.1 system card is checked first. If not, simply append "; both are vendor figures."

## Could not verify
- The Anthropic Fable 5.1 system card itself, which was not reachable. Its figures come via secondary write-ups (S3 only).
- NVD's own page renders empty to the fetcher. The NVD API was used instead (see below).

## Checked and confirmed
- Project Vend phase 1: Claude Sonnet 3.7, "about a month", Irn-Bru $100/$15 and the "keep [the user's] request in mind…" quote, "99% of your customers are Anthropic employees", 31 March–1 April, blue blazer/red tie, "we would not hire Claudius", Chocomel, metal cubes, the invented payment account.
- Project Vend phase 2 (18 Dec 2025): Sonnet 4 then 4.5; Seymour Cash; SF/NYC/London; discounts down ~80%, giveaways halved, "largely eliminated", ~8× approvals, "in spite of the CEO…", onions and the 1958 Onion Futures Act, "friend who just wants to be nice", "the gap between 'capable' and 'completely robust' remains wide", and the elected-CEO episode.
- METR benchmark_results_1_1.yaml: doubling 128.7 days (CI 104.4–158.0); Opus 4.6 11.98 h (5.3–60.6); GPT-5.4 5.7 h; Gemini 3.1 Pro 6.4 h; Mythos Preview early 17.4 h (8.5–55.1), added 8 May 2026; page "no longer actively updated" (8 Sept 2026); March regularization correction.
- OSWorld-Verified spreadsheet: Intelligence-Indeed Agent 90.19% (25 Jul 2026); claude-fable-5 85.96% (1 Aug 2026), the top "General model"; HIPPO Agent w/ Opus 4.5 74.48% (Feb 2026); OSWorld 2.0 notice dated 2026-06-26, quoted correctly.
- Scale SWE-Bench Pro leaderboard: top 61.50% (Muse Spark 1.1); Claude Sonnet 4.5 43.6% and GPT-5 high 41.78%.
- OpenAI's SWE-bench Pro audit: 731 tasks, 27.4% / 34.1%, ~30%, recommendation retracted.
- τ-bench site: Opus 4.5 τ² 85.3% = mean of 84.0/79.6/92.3; four-domain mean 70.15 → 70.2%; Qwen 3.8 Max banking 55.2%; Qwen3.5 and Gemini 3.0 Pro above Opus 4.5 on τ²; 50+ fixed tasks; ~700 documents.
- MCP 2026-07-28 changelog: stateless, per-request protocol version in `_meta`, `resultType` "complete", MRTR "input_required" retry, Roots/Sampling/Logging deprecated.
- A2A joined AAIF on 17 Aug 2026, "over 150 organizations", v1.0.
- Anthropic incident posts: 30 Jul 2026, three models, live internet despite prompts; 9 Sep 2026 post has a fourth incident and "these incidents are serious".
- Claude Duet: quote verbatim; research preview opened 21 Oct 2026.
- CVE-2026-25253: 8.8, gatewayUrl token leak. CVE-2025-32711: Microsoft 9.3 / NIST 7.5, PR:N/UI:N.
- x402 Foundation (LF, 2 Apr 2026); AP2 to FIDO (28 Apr 2026).
- Agarwal et al. MSR '26: ~18% / ~39%, gains only where agents were the first AI tool. Li et al.: 456,000 PRs, five agents, 61,000 repos.
- Mythos 5 not generally available (Fable 5 is the GA Mythos-class model).
- Arithmetic: 0.95^20 = 0.358; 0.99^50 = 0.605; 0.95^50 = 0.077; 0.90^50 = 0.005; 0.995^24 = 0.887; 0.995^168 = 0.431; 0.9975^20 = 0.951; 1 − 0.3^8 = 0.99993; 0.7^8 = 0.058; C(6,4)/C(8,4) = 15/70 = 0.214; 0.75^4 = 0.316; 0.796^4 = 0.401; CaMeL 84 − 77 = 7.

## Tally
Claims checked: 78 / confirmed: 75 / wrong: 0 / imprecise or unsupported: 2 (S1, S2) / balance: 1 (S3) / outdated: 0
