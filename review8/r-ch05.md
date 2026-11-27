# Review 8: Chapter 5 (From Chatbots to Agents)

## Verdict
Ready to print after the SHOULD fixes. This is a careful, well-sourced chapter. I spot-checked about 70 claims. Nearly all of the 2025–26 material, quotations and arithmetic checked out against primary sources: Project Vend phase 2, the MCP 2026-07-28 changelog and security text, A2A/AAIF, METR's data file, OpenAI's SWE-bench audits, τ-bench, Wiz/Moltbook, Replit, the OpenAI/Hugging Face and Anthropic cyber-evaluation incidents, and Claude Duet. I found nothing wrong enough to block printing.

On balance between companies, the chapter leans on Anthropic material (Project Vend, MCP, Anthropic's engineering guidance, Table 5.3, four Claude rows in Table 5.1). It usually labels that material as vendor-reported, and it is often critical of Anthropic (Project Vend, the cyber-evaluation incidents). Two places select figures in a way that flatters Claude against OpenAI (S1, S2). They are easy to fix.

## MUST change before printing
None.

## SHOULD change

### S1. SWE-bench Pro: the uncapped Claude score sits next to a capped GPT-5 score
- Where: textbook/chapters/ch05.md:165
- Text now: "In that setting the best model, Claude Sonnet 4.5, resolved 43.6% of the public problems. On the commercial set, reported in a separate table, the best score was 17.8% (Claude Opus 4.1). In an earlier run capped at $2 per task, GPT-5 at its high reasoning setting resolved 25.9% of the public set"
- Problem: UNCLEAR / balance. Every figure is correct, but the only OpenAI number given comes from the $2-capped run. In the same uncapped main setting, GPT-5 (high) scored 41.8%, close to Claude's 43.6%. As written, readers will infer a large gap between Claude and GPT-5 that the paper does not show.
- Evidence: https://arxiv.org/html/2509.16941v2. Table 1 (public, N=731): Claude Sonnet 4.5 43.6%, GPT-5 (high) 41.8%. Table 5 ("Models are capped at 50 turns and a cost limit of $2"): GPT-5 (high) 25.9%, GPT-5 (medium) 23.3%, Claude Opus 4.1 22.7%.
- Change to: "In that setting the best model, Claude Sonnet 4.5, resolved 43.6% of the public problems and GPT-5 at its high reasoning setting 41.8%. On the commercial set, reported in a separate table, the best score was 17.8% (Claude Opus 4.1). In an earlier run capped at $2 per task, the same GPT-5 setting resolved 25.9% and Claude Opus 4.1 22.7%"

### S2. OSWorld: OpenAI's self-reported human-surpassing score is left out
- Where: textbook/chapters/ch05.md:155 (and Table 5.1, lines 143–151)
- Text now: "On the revised benchmark, scores above the original student baseline had been reported: in the official leaderboard's own re-runs, an agent program built on Claude Opus 4.5 scored 74.5% in an entry dated February 2026, and by August the best general-purpose model, Anthropic's Claude Fable 5, reached 86.0%"
- Problem: UNCLEAR / balance. Four of the seven rows in Table 5.1 are Anthropic systems. The table and text include self-reported company figures for Claude 3.5 Sonnet and OpenAI CUA. However, they omit the most widely reported 2026 milestone: OpenAI's launch claim that GPT-5.4 scored 75.0% on OSWorld-Verified (March 2026), "surpassing human performance at 72.4%". The 86.0% Fable 5 figure is correct (official board, 85.96%, 1 August 2026). A reader could still conclude that only Anthropic systems crossed the human baseline.
- Evidence: https://openai.com/index/introducing-gpt-5-4 (5 March 2026) reports a state-of-the-art "75.0% success rate … surpassing human performance at 72.4%" on OSWorld-Verified. The official board (osworld-v1.xlang.ai, via presenc.ai table as of 1 October 2026) lists Claude Fable 5 85.96%, 2026-08-01.
- Change to: insert after "…scored 74.5% in an entry dated February 2026,": " OpenAI reported 75.0% for GPT-5.4 in March 2026 in its own evaluation,". Optionally add a Table 5.1 row: "GPT-5.4 (company-reported) | Mar 2026 | OSWorld-Verified | 75.0% | 72.36%". Add a bib entry:
  ```
  @misc{openai2026introducinggpt54,
    author = {{OpenAI}},
    title = {Introducing {GPT-5.4}},
    year = {2026},
    howpublished = {Company blog (company source), 5 March 2026},
    url = {https://openai.com/index/introducing-gpt-5-4/},
    urldate = {2026-11-27}
  }
  ```

### S3. SWE-bench Pro: the "leaderboard top 61.5%" needs its harness context
- Where: textbook/chapters/ch05.md:165 and Table 5.2, line 171
- Text now: "On Scale AI's public leaderboard, mostly run in a minimal agent program, the top entry in November 2026 resolved 61.5%"
- Problem: UNCLEAR. The figure is correct: Scale lists Muse Spark 1.1 at 61.50 with the mini-swe-agent harness. However, OpenAI's July 2026 paper, which the book cites in the next sentences, says frontier models on the same 731-task public split "improved from a pass rate of 23.3% to 80.3% in eight months" with their own harnesses. Without that, a reader takes 61.5% as the best known performance.
- Evidence: https://openai.com/index/separating-signal-from-noise-coding-evaluations/ (8 July 2026): "On the 731-task public split, frontier models improved from a pass rate of 23.3% to 80.3% in eight months." Scale leaderboard: "Muse Spark 1.1* 61.50 ± 3.10" (* = mini-swe-agent harness).
- Change to: "On Scale AI's public leaderboard, mostly run in a minimal agent program, the top entry in November 2026 resolved 61.5%; developers using their own agent programs reported up to about 80% by mid-2026 [@openai2026separating]."

## Could not verify
- Nasr et al. published at the USENIX Security Symposium 2026 (bib nasr2025attacker). The arXiv page still reads "Preprint. Under review", and I could not find the title in the excerpts of the accepted-paper list I could open. Please check the USENIX Sec '26 programme.
- Table 5.3 caption: the τ²-bench pass^4 observed value of 0.52 for Opus 4.5 (retail), and "in November 2026 Sierra verified 73% for … Principled Machines' Cortex 0.1". Neither appears on the taubench.com front page.
- CVE-2026-25253: I could not load the NVD page. Secondary sources (Mend, SonicWall, OSV) give CVSS 8.8 and the gatewayUrl token-leak description, which is consistent with the text.

## Checked and confirmed
- Project Vend phase 1 quotations and phase 2 (anthropic.com/news/project-vend-2): "in spite of the CEO…", "eight times as often", ~80% fewer discounts, "largely eliminated", onions quote, "perspective of a friend…", "capable/completely robust", New York and London, Sonnet 4.0→4.5.
- MCP 2026-07-28: stateless, per-request version/clientInfo, `resultType: "complete"`, MRTR "input_required" retry, Roots/Sampling/Logging deprecated. Security quotations verbatim, LSP inspiration, "Functions for the AI model to execute".
- AAIF/MCP (December 2025, Block and OpenAI); A2A joined AAIF 17 August 2026 with 150+ organisations; A2A v1.0; x402 Foundation under the Linux Foundation on 2 April 2026.
- METR data file: doubling 128.7 d (CI 104–158); Opus 4.6 12.0 h (5.3–60.6); GPT-5.4 5.7 h; Gemini 3.1 Pro 6.4 h; Mythos Preview early 17.4 (8.5–55.1); last added 8 May; "no longer actively updated" 8 September.
- OpenAI SWE-bench Verified audit (138 problems, 64 runs, 59.4%, GPT-5.2/Opus 4.5/Gemini 3 Flash); SWE-bench Pro audit (731, 27.4%/34.1%, ~30%, recommendation retracted); SWE-bench Pro paper figures.
- GPT-6 Astra table: OSWorld 2.0 offline partial 72.6% vs Claude Opus 5 70.2%; OSWorld 2.0 preprint 20.6%/54.8%; Fable 5 85.96% on the official board.
- τ²-bench: Opus 4.5 three-domain mean 85.3% (= (84.0+79.6+92.3)/3); Qwen and Gemini ranked above; best banking score Qwen 3.8 Max 55.2%; τ³ >50 tasks fixed, ~700 documents.
- OpenAI/Hugging Face breakout (zero-day in package proxy, pursuit of ExploitGym answers); Anthropic three incidents (misconfiguration gave live internet; prompts said none), fourth incident and "serious" (9 September).
- Wiz/Moltbook (~17,000 owners, 1.5M agents, quotations, fixed within hours); Replit (Register: "a catastrophic error of judgement", "Unacceptable…", dev/prod separation).
- Agarwal et al. (~18% / ~39%, gains only where the agent was the first AI tool); Hammond et al. (44 authors, 3 failure modes, 7 risk factors); Claude Duet quotation (help centre) and 21 October 2026 preview.
- Arithmetic: 0.95^20≈0.36; 0.99^50≈0.61; 0.95^50≈0.08; 0.9^50<0.01; 0.9975^20≈0.95; pass@8 and pass^8 at p=0.7; C(6,4)/C(8,4)=15/70; (0.75)^4≈0.32; 0.796^4≈0.40; 0.995^24≈0.89; 0.995^168≈0.43; the Jensen argument for pass^k.
- Cross-references: §3.7, §4.7, §12.2, §12.6 and Chapters 8, 11, 13, 14 exist and match. Ch01 and Ch04 figures (86%, 12 h, 129 days) are consistent; Ch11's account of the incidents is consistent.

## Tally
Claims checked: ~70 · confirmed: ~67 · wrong: 0 · misleading by selection: 2 (S1, S2) · outdated: 0 · unverified: 3
