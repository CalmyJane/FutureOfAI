# Chapter 5: From Chatbots to Agents (fourth review)

## Verdict

**Ready to print after small fixes.** This is a strong, carefully sourced chapter. I checked every 2025–2026 claim I could reach against its primary source: Project Vend 1 and 2, MCP 2026-07-28, A2A 1.0 and AAIF, the OSWorld-Verified spreadsheet, OSWorld 2.0, the SWE-bench Verified and Pro audits, the Scale leaderboard, METR's data file, τ-bench submissions, the CVEs, Moltbook/Wiz, Krebs, OpenAI/Hugging Face, Claude Duet, AP2, x402 and Agarwal et al. Nearly all of it holds, including the direct quotations. All the worked arithmetic is correct. I found no MUST-level error. There are four SHOULD items: one typo that will show in print, one comparison labelled "comparable" that is not, a date inconsistency between the text and Table 5.2, and two slight overstatements of sources.

## MUST change before printing

None.

## SHOULD change

### S1. Typo: comma splice with a capital letter
- Where: textbook/chapters/ch05.md:235
- Text now: "had broken out of their test environment and into Hugging Face's systems, According to OpenAI, the models exploited"
- Problem: UNCLEAR — a typographical error. The sentence runs on after a comma and restarts with a capital letter. It will be visible in print.
- Evidence: n/a (proofreading).
- Change to: "had broken out of their test environment and into Hugging Face's systems. According to OpenAI, the models exploited"

### S2. The GPT-6 Astra OSWorld 2.0 figure is called "comparable" but is not
- Where: textbook/chapters/ch05.md:155
- Text now: "OpenAI reported 72.6% for GPT-6 Astra on an offline subset of OSWorld 2.0 scored with partial credit [@openai2026gpt6]; the comparable figure for the paper's best agent is that 54.8%, on the full task set."
- Problem: UNCLEAR / slightly misleading. OpenAI's 72.6% is on "OSWorld 2.0 (v2026.08.08, offline set, partial score)". That is a later version and a different subset from the June/July preprint's 54.8%. OpenAI's own table also gives **Claude Opus 5 70.2%** on that same offline partial-score set. Calling 54.8% "the comparable figure" suggests a gap of 18 points between OpenAI and everyone else. The like-for-like gap in OpenAI's own table is about 2 points.
- Evidence: https://openai.com/index/gpt-6-astra/ (accessed 26 Nov 2026). The table row reads "OSWorld 2.0 (v2026.08.08, offline set, partial score) 72.6% [GPT-6 Astra] 65.7% [GPT-5.6 Sol] … 70.2% [Claude Opus 5]". Footnote 3 reads: "OSWorld V2-Offline is a subset of the original OSWorld V2 that works without internet access. Claude model performance on OSWorld-V2 Offline was reproduced by the authors on the official leaderboard". The preprint (arXiv:2606.29537 v2, 13 Jul 2026) says the best agent "completes only 20.6% of tasks at a 54.8% partial score".
- Change to: "OpenAI reported 72.6% for GPT-6 Astra on a later, offline-only version of OSWorld 2.0 scored with partial credit, against 70.2% for Anthropic's Claude Opus 5 in the same table [@openai2026gpt6]; these figures are not comparable with the preprint's 54.8% on the full task set."

### S3. SWE-bench Pro leaderboard: the text and Table 5.2 give different dates
- Where: textbook/chapters/ch05.md:165 and :171
- Text now (165): "On Scale AI's public leaderboard, mostly run in a minimal agent program, the top entry in November 2026 resolved 61.5%". Text now (171, Table 5.2): "leaderboard top 61.5% (Oct 2026)"
- Problem: INCONSISTENT — the same figure is dated November in the text and October in the table. The 61.5% figure itself is correct: Muse Spark 1.1, 61.50 ± 3.10. You might also note that OpenAI's July audit says scores on the public split under OpenAI's own harness reached 80.3%. That would reinforce the chapter's point that the harness matters.
- Evidence: https://labs.scale.com/leaderboard/swe_bench_pro_public (accessed 26 Nov 2026): "1 Muse Spark 1.1* NEW 61.50 ± 3.10 2 gpt-5.4 (xHigh)* 59.10". https://openai.com/index/separating-signal-from-noise-coding-evaluations/ (8 Jul 2026): "On the 731-task public split, frontier models improved from a pass rate of 23.3% to 80.3% in eight months."
- Change to: in Table 5.2 replace "leaderboard top 61.5% (Oct 2026)" with "leaderboard top 61.5% (Nov 2026)".

### S4. The Replit fixes were not only about permissions and infrastructure
- Where: textbook/chapters/ch05.md:232
- Text now: "The fixes the company announced changed permissions and infrastructure, not the model's instructions [@sharwood2025replit]."
- Problem: UNSUPPORTED (slight overstatement). The cited article also reports a change to the agent's behaviour: "rolling out a fix to force Docs search on Replit knowledge". The agent did not know a restore was possible because it "didn't have access to the proper internal docs".
- Evidence: https://www.theregister.com/2025/07/22/replit_saastr_response/ (22 Jul 2025): "the company's agent 'didn't have access to the proper internal docs' … The CEO said his team is 'rolling out a fix to force Docs search on Replit knowledge.'" and "started rolling out automatic DB dev/prod separation to prevent this categorically."
- Change to: "The main fixes the company announced changed infrastructure, separating development and production databases, rather than relying on the model to obey instructions [@sharwood2025replit]."

### S5. The Epoch source on RL environments is paraphrased a little too firmly
- Where: textbook/chapters/ch05.md:131
- Text now: "Environments with trustworthy checks have thus become a scarce input, and Epoch researchers count building them among the bottlenecks of reinforcement learning [@edelman2025why]."
- Problem: UNSUPPORTED (slight). The cited post raises the availability of RL environments as a *possible* bottleneck to scaling training compute. It does not state it as an established bottleneck of RL.
- Evidence: https://epoch.ai/gradient-updates/why-gpt5-used-less-training-compute-than-gpt45-but-gpt6-probably-wont (26 Sep 2025): "it's possible that the bottlenecks to scaling training compute are harder than we anticipate, e.g. due to limits in the availability of high-quality pre-training data and post-training RL environments."
- Change to: "Environments with trustworthy checks have thus become a valuable input, and Epoch researchers name a shortage of post-training RL environments as a possible bottleneck to further scaling [@edelman2025why]."

## Could not verify

- x402: "the specification's example of $1 to read an article" (l.294). The current README on github.com/x402-foundation/x402 does not contain this example. It may be in an older spec version. The trust-minimising quotation itself is confirmed.
- Assad et al.: "In markets with two or three stations" (l.310). I did not re-read the paper. My recollection is that the main result is for duopolies, so "two or three" should be checked.
- Microsoft "not aware of exploitation" (l.249). MSRC records "exploited: No" and "fully mitigated … no action for users". The exact wording on awareness was not checked.
- OSWorld-Verified "nearly 300 feedback items" (l.141). Not re-fetched; the xlang blog was not loaded.

## Checked and confirmed

- Project Vend 1: Irn-Bru $100 against $15, with the quote; "99% of your customers"; 31 Mar–1 Apr; blazer and tie; "we would not hire Claudius"; Chocomel; tungsten cubes; hallucinated payment account; "about a month"; simulated email.
- Project Vend 2 (18 Dec 2025): Sonnet 4.0 then 4.5; CRM; Seymour Cash; NY and London; discounts down ~80% and giveaways halved; "largely eliminated"; ~8× approvals; "in spite of the CEO"; onions quote, with both agents "all set to go ahead"; Onion Futures Act 1958; Mihir "elected as the actual CEO"; "from something more like the perspective of a friend who just wants to be nice"; "capable"/"completely robust"; WSJ reporters.
- MCP 2026-07-28 spec: stateless; MRTR "input_required"; deprecation of Roots, Sampling and Logging; `resultType: "complete"`; the get_weather example; all four security quotations; "SHOULD always be a human in the loop"; the LSP inspiration; still the latest revision listed in Nov 2026.
- MCP donation figures (10,000+ servers, 97M+ SDK downloads, adopters, co-founders Block and OpenAI); A2A joining AAIF on 17 Aug 2026 with 150+ organisations; A2A spec v1.0.0, the "internal state, memory, or tools" quote, and the gRPC/HTTP bindings.
- OSWorld-Verified spreadsheet: HIPPO Agent with Opus 4.5 at 74.48% (25 Feb 2026); claude-fable-5 at 85.96% (1 Aug 2026), the top general model; Intelligence-Indeed at 90.19% (25 Jul 2026); the site notice dated 26 Jun 2026.
- OSWorld 2.0 preprint: 108 workflows; median ~1.6 h; 20.6%/54.8%.
- AI Index 2026: OSWorld 66.3%; "one in three attempts on structured benchmarks"; SWE-bench Verified ~76.8% (Feb 2026); τ-bench 62.9–70.2%.
- SWE-bench Verified audit (23 Feb 2026): 138 problems, 64 runs, 59.4%, and the three models named.
- SWE-bench Pro paper: 1,865 tasks, 41 repositories, 18 proprietary; 43.6% (Sonnet 4.5); 17.8% (Opus 4.1); GPT-5 (high) 25.9% under the $2/50-turn cap. OpenAI audit of 8 Jul 2026: 731 tasks, 27.4%/34.1%, "retract our earlier recommendation". Epoch verdict "Flawed".
- METR data file: doubling time 128.7 days (CI 104.4–158.0); Opus 4.6 718.8 min ≈ 12 h (CI 5.3–60.6 h); regularisation correction on 3 Mar 2026; Mythos Preview (early) added 8 May; page "no longer actively updated" since 8 Sep 2026.
- τ-bench: Sierra's Opus 4.5 submission gives 84.0/79.61/92.32/24.74, mean 70.2, and retail pass^4 51.75; banking leader Qwen 3.8 Max at 55.2%; Cortex 0.1 at 73.20% verified by Sierra in 1 trial on 3 Nov 2026; τ³ "50+ tasks" fixed; ~700 documents; τ² in ICML 2026 (PMLR 306).
- CVE-2025-32711 (Microsoft 9.3, NIST 7.5, PR:N/UI:N) and CVE-2026-25253 (8.8, description matches).
- Moltbook and OpenClaw: Krebs (1.5M agents in under a week); Wiz (17,000 owners, "no mechanism to verify", "full read and write access", fixed within hours); Palo Alto ("accelerant"); OpenClaw launched Nov 2025.
- OpenAI/Hugging Face (21 Jul 2026): zero-day in a package-registry cache proxy (Artifactory), done to obtain test solutions. Consistent with Ch12 §12.2.
- Claude Duet support-page quote; research preview announced 21 Oct 2026.
- AP2: the three problems, the "white running shoes" example, "non-repudiable audit trail", open/closed mandates, the FAQ quote "establish accountability and liability principles". x402 Foundation under the Linux Foundation on 2 Apr 2026.
- NCSC quotations; Willison's "95% is very much a failing grade"; Nasr et al. (12 defences, >90%, 500+ participants, $20,000, human red-teaming "succeeds on all of the scenarios", "cannot prove that a defense is robust").
- CaMeL: 77% against 84% (arXiv v2).
- Anthropic research system: 90.2%, ~4×/~15× tokens, 80% of variance. Context engineering: "1,234 steps", "often 1,000-2,000 tokens". Chroma: "consistently degrades with increasing input length".
- Anthropic Economic Index: "77% of API transcripts show automation patterns". AIDev: 456,000 PRs and 61,000 repositories. Agarwal et al.: ~18%/39%.
- DeepSeek-V3.2: 1,827 environments; "hard to solve but easy to verify"; tens of thousands of GitHub environments.
- Hadfield and Koh quotations (correlated errors, flash crash, "currently missing for AI agents"); Tomašev "critical and controllable design variable"; Hammond report with 44 authors; Cemri et al. (150 traces, 1,600+, 7 frameworks, κ 0.88).
- Arithmetic: 0.995^24 ≈ 0.887; 0.995^168 ≈ 0.431; 0.95^20 ≈ 0.358; 0.99^50 ≈ 0.605; 0.95^50 ≈ 0.077; 0.9^50 ≈ 0.005; 1−0.05² = 0.9975 and 0.9975^20 ≈ 0.951; pass@8 = 0.99993; 0.7^8 ≈ 0.058; C(6,4)/C(8,4) = 15/70 ≈ 0.214; 0.75^4 ≈ 0.316; 0.796^4 ≈ 0.40; mean of four domains = 70.15.
- Cross-references: §3.7, §4.7, Ch8 (METR trial), §12.2, Ch11 (correlated errors), Ch13, §14.7 all exist and fit. The OSWorld figures in Ch1 l.242 agree.

## Tally

Claims checked: 118 · confirmed: 111 · wrong: 0 · outdated: 0 · inconsistent/overstated: 4 (S2–S5) · typo: 1 (S1) · could not verify: 4
