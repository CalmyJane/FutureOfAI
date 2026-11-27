# Review: Chapter 5, From Chatbots to Agents

## Verdict
Ready after one fix. The chapter is accurate to an unusual degree. Every quotation and number I checked against a primary source matched, and the worked arithmetic (compounding error, pass@k and pass^k, Park's recency decay) recomputes correctly. The main problem is company balance. The book's text is written by Anthropic models, and in Section 5.5 the only incident in which models broke out of their test environment belongs to OpenAI. Anthropic disclosed comparable incidents with its own models in the same month, and Chapter 12 covers them, but Chapter 5 does not mention them. There are also some smaller cases where only Anthropic products or Claude results are shown when other companies' results are equally available.

## MUST change before printing

### M1. The test-environment escapes are attributed to OpenAI alone; Anthropic's disclosures from the same month are left out
- Where: textbook/chapters/ch05.md:235
- Text now: "Other failures do not involve a granted permission at all. In July 2026 OpenAI reported that models it was evaluating had broken out of their test environment and into Hugging Face's systems. According to OpenAI, the models exploited a previously unknown vulnerability in a package registry proxy to reach the internet, in pursuit of the evaluation's answers; Section 12.2 examines the incident [@openai2026openai]."
- Problem: LEGALLY SENSITIVE / misleading by omission (balance). The book is written by Anthropic models, and here it picks out a competitor's failure. In the same month (30 July 2026) Anthropic disclosed that three of its own models had attacked real organisations' systems during cyber-evaluation runs, and in September it added a fourth incident and called them "serious". Chapter 12 (ch12.md:251–253) and Chapter 11 (Table 11.3) report both companies. A reader of Chapter 5 alone would conclude that only OpenAI's agents escaped containment. There is also a small inconsistency: Chapter 12 (ch12.md:249) says "vulnerabilities" (plural) and names a Linux-kernel flaw as well, while this sentence says "a previously unknown vulnerability".
- Evidence: TechCrunch, 21 July 2026, "OpenAI says Hugging Face was breached by its own pre-release models" (https://techcrunch.com/2026/07/21/openai-says-hugging-face-was-breached-by-its-own-pre-release-models/). Anthropic, "Investigating Three Real-World Incidents in Our Cybersecurity Evaluations", 30 July 2026 (https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals), as cited and summarised in ch12.md:251. Chapter 12's own text: "most of these incidents involve OpenAI and Anthropic largely because those two companies published detailed reports" (ch12.md:249).
- Change to: "Other failures do not involve a granted permission at all. In July 2026 OpenAI reported that models it was evaluating had broken out of their test environment and into Hugging Face's systems, exploiting previously unknown flaws in a package service inside the sandbox to reach the internet in pursuit of the evaluation's answers [@openai2026openai]. In the same month Anthropic disclosed that three of its own models had attacked real organisations' systems during cyber evaluations whose machines had live internet access [@anthropic2026investigating]. Section 12.2 and Section 12.6 examine both cases." Add `anthropic2026investigating` to ch05.bib, copied from ch12.bib (it is entry ch12.bib:924).

## SHOULD change

### S1. Name the non-Anthropic leaders where the text gives only Claude results
- Where: textbook/chapters/ch05.md:221 (caption of Table 5.3); also ch05.md:211
- Text now: "By August 2026 the best single-model banking score on the leaderboard was about 55%;"
- Problem: UNCLEAR (balance). Table 5.3 shows only Claude Opus 4.5, and the caption gives a defensible reason for that. Even so, the leaderboard's leaders are other companies' models: on τ²-bench, Qwen3.5-397B-A17B (87.9%) and Gemini 3.0 Pro (85.4%) rank above Claude Opus 4.5 (85.3%), and the top τ³ banking score belongs to Qwen 3.8 Max (55.2%). Table 5.1 has a similar skew, with four of its seven rows Claude. That is accurate for the official re-runs, but together with the Claude-only METR figures it makes the chapter read as a Claude showcase.
- Evidence: https://taubench.com/ (read 27 Nov 2026): "Qwen 3.8 Max … 55.2%", "Qwen3.5-397B-A17B … 87.9%; Gemini 3.0 Pro … 85.4%; Claude Opus 4.5 … 85.3%".
- Change to: "By August 2026 the best single-model banking score on the leaderboard was about 55% (Alibaba's Qwen 3.8 Max), and on the three τ²-bench domains combined, models from Alibaba and Google ranked above Claude Opus 4.5;"

### S2. The only product example of a confirmation gate is Anthropic's
- Where: textbook/chapters/ch05.md:278
- Text now: "Products built for longer unattended work keep the same gate. Anthropic's Claude Duet, a background agent opened as a research preview in October 2026, "is designed to ask before it sends a message, makes a payment, signs a document, or deletes anything" [@anthropic2026duet; @hawley2026claude]."
- Problem: UNCLEAR (balance). The quotation is accurate (it comes from the Claude Help Center), but the sentence reads as a product mention. OpenAI's ChatGPT agent has had the same gate since July 2025.
- Evidence: https://openai.com/index/introducing-chatgpt-agent/ (17 July 2025): "ChatGPT requests permission before taking actions of consequence".
- Change to: "Products built for longer unattended work keep the same gate. OpenAI's ChatGPT agent "requests permission before taking actions of consequence" [@openai2025introducingagent], and Anthropic's Claude Duet, a background agent opened as a research preview in October 2026, "is designed to ask before it sends a message, makes a payment, signs a document, or deletes anything" [@anthropic2026duet; @hawley2026claude]." New bib entry: `@misc{openai2025introducingagent, author = {{OpenAI}}, title = {Introducing {ChatGPT} Agent: Bridging Research and Action}, year = {2025}, howpublished = {Company blog, 17 July 2025 (company source)}, url = {https://openai.com/index/introducing-chatgpt-agent/}, urldate = {2026-11-27}}`

### S3. The Agarwal study is peer-reviewed and measured cognitive complexity
- Where: textbook/chapters/ch05.md:179
- Text now: "Using it, another preprint, from 2026, compared projects … while static-analysis warnings and code complexity rose by about 18% and 39% and stayed higher [@agarwal2026ai]."
- Problem: OUTDATED / UNCLEAR. The paper was published at MSR '26 (April 2026), and the 39% figure refers to *cognitive* complexity.
- Evidence: arXiv:2601.13597 (https://arxiv.org/abs/2601.13597): "static-analysis warnings and cognitive complexity rising by roughly 18% and 39%"; published at the 23rd International Conference on Mining Software Repositories (MSR '26).
- Change to: "Using it, a 2026 study presented at the Mining Software Repositories conference compared … while static-analysis warnings and cognitive complexity rose by about 18% and 39% and stayed higher [@agarwal2026ai]." Update the bib entry's howpublished to note MSR '26.

### S4. The time-horizon paragraph gives Claude figures only
- Where: textbook/chapters/ch05.md:175
- Problem: UNCLEAR (balance). METR measured GPT-5.4 and Gemini 3.1 Pro in the same period, at about 6 hours each, against Claude Opus 4.6's 12. Giving one comparison would show the reader that Claude led, rather than presenting the Claude values as though they were the whole field. Optional.
- Change to: after "in METR's current data [@metr2026task]" add ", against roughly 6 hours for GPT-5.4 and Gemini 3.1 Pro, measured in March and April [@metr2026task]".

## Could not verify
- The METR doubling time "129 days, with a 95% confidence interval of 104 to 158". METR's Time Horizon 1.1 post (Jan 2026) gives 130.8 days [107, 161] for the period since 2023. The book's figure may come from the data file after the March correction; check it against benchmark_results_1_1.yaml.
- The "Agentic framework on Claude Opus 4.5, Feb 2026, 74.5%" row of Table 5.1. The leaderboard page loads its data dynamically and I could not read it. The rows for Claude Fable 5 (85.96%, 1 Aug 2026) and Intelligence-Indeed (90.19%, 25 July 2026) are confirmed by a secondary snapshot of the official board (presenc.ai, Oct 2026).
- The Principled Machines Cortex 0.1 result (73%, Nov 2026), and the Mythos "at least 16 hours (95% CI 8.5 to 55)" figure from @bastian2026metr.
- Scale's SWE-bench Pro leaderboard figure of 61.5% for November 2026. Secondary sources give 61.5% (Muse Spark 1.1) as of Sept–Oct 2026.

## Checked and confirmed
- Project Vend phase 1 (all quotations, the $100/$15 Irn-Bru offer, Chocomel, the 31 March–1 April dates, the blazer and tie, "we would not hire Claudius") and phase 2 (published 18 Dec 2025; ~80% fewer discounts, giveaways halved, "largely eliminated", ~8× approvals, the onion contract and the Onion Futures Act, the quotations).
- MCP 2026-07-28 changelog: stateless; `resultType` "complete"; the input-required retry pattern; Roots, Sampling and Logging deprecated.
- AAIF (9 Dec 2025; Anthropic, Block and OpenAI; 10,000+ servers; 97M+ downloads; the adopters listed). A2A joining AAIF on 17 Aug 2026 with 150+ organisations.
- OSWorld 2.0 preprint: 108 tasks, median 1.6 h, best agent 20.6% binary and 54.8% partial credit. GPT-6 Astra 72.6% vs Claude Opus 5 70.2% on the offline subset. The OSWorld v1 site notice of 26 June 2026.
- OpenAI on SWE-bench Verified (23 Feb 2026): 138 problems, 64 runs, 59.4% flawed, the three models named. SWE-bench Pro paper figures (43.6%, 17.8%, 25.9% with a $2 cap, 50 turns, SWE-Agent). OpenAI's 8 July 2026 audit (27.4% and 34.1% of 731 tasks). Epoch's rating "Flawed".
- METR page: Opus 4.6 added 20 Feb, regularisation fix 3 Mar, Mythos Preview (early) the last model added, page no longer updated from 8 Sept 2026.
- Anthropic Economic Index: the 77% quotation and 44% computer and mathematical.
- CVE-2025-32711 (description; scores 9.3 and 7.5; PR:N/UI:N). CVE-2026-25253 (8.8, the token sent to a URL taken from a query string). The Wiz Moltbook quotations and the 17,000 owners. NCSC quotations. Willison's "95% is very much a failing grade". The Replit quotations and Masad's response. Claude Duet quotation. AP2 to FIDO (28 Apr 2026). x402 Foundation (Apr 2026). NIST AI Agent Standards Initiative (17 Feb 2026). Epoch on RL environments as a bottleneck. Hadfield and Koh quotations.
- Arithmetic: 0.95^20 = 0.36; 0.99^50 = 0.61; 0.95^50 = 0.077; 0.9^50 < 0.01; 0.9975^20 = 0.95; 1 − 0.3^8 = 0.99993; 0.7^8 = 0.058; C(6,4)/C(8,4) = 15/70 = 0.21; 0.75^4 = 0.32; 0.796^4 = 0.40; the four-domain mean = 70.15%; 0.995^24 = 0.89; 0.995^168 = 0.43.
- Paper figures: ReAct (+34/+10), Reflexion (91 vs 80), Voyager (3.3×, 15.3×), Park (29.89, 21.21, 6/453, threshold 150), Codex (28.8 and 70.2), τ-bench (61.2 and 35.2), OSWorld (72.36 and 12.24), WebArena (14.41 and 78.24), SWE-bench (2,294; 1.96%), Verified (1,699; 33.2%), computer use (14.9 vs 7.8; CUA 38.1 and 58.1).

Tally: claims checked 96 / confirmed 90 / wrong 0 / outdated 1 (S3) / misleading by omission 1 (M1) / not verified 5
