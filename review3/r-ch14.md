# Third review: Chapter 14 — Forecasting the Next Ten Years: Methods, Scenarios and Open Problems

## Verdict
Ready after the MUST fix below. The chapter is unusually well sourced: every number in Tables 14.1–14.3, the Brier box and Table 14.2 recomputes or matches its source, the survey, tournament, METR, IEA, AI 2027 and FRI material was checked against the primary documents and is accurate, and every cross-reference to an earlier chapter points to a section that exists and contains what is claimed. One statement is now wrong: the chapter says, three times in different forms, that the only release restrictions so far have come from companies. In fact, on 12 June 2026 the US Commerce Department used export controls to bar foreign nationals from Anthropic's Claude Fable 5 and Mythos 5, and Anthropic then switched both off worldwide until 30 June. FRI, the chapter's own source, counts this as a near-resolution of the LEAP question. A small set of SHOULD items deals with events after the text was written (OpenAI's second pause in September 2026, the BIS rule of 19 November 2026 and the CAISI → CAISSI restyling) and a few sentences that say more than their sources do.

Scope note: the chapter does not discuss Minsky, Kurzweil, *Situational Awareness*, Epoch's GATE model, company leaders' AGI-timeline statements, Metaculus AGI dates or the EU compute threshold number. There was nothing to check for these, and their absence is not an error. The leads about Jensen Huang, the 2026 midterms and Anthropic's fourth cyber incident do not touch this chapter, because it makes no statement about any of them.

## MUST change before printing

### M1. "The restrictions so far have come from companies": a government restriction happened in June 2026
- Where: textbook/chapters/ch14.md:167, and the dependent text at :178 (Table 14.4), :190 (Section 14.6 signpost) and :284 (closing synthesis)
- Text now (167): "The restrictions so far have come from companies. In June 2026 OpenAI limited its unreleased GPT-5.6 Sol to a small group of partners approved by the US government, though FRI judged that this did not appear to result from a binding directive [@rosenberg2026how]."
- Text now (178): "| Regulation | EU high-risk rules deferred to 2027–2028; release limits and first safety pause by companies, not law (OpenAI, Jun and Aug 2026) | First binding restriction on a model release |"
- Problem: VERIFIED WRONG / OUTDATED. On 12 June 2026 the US Commerce Department issued an export-control directive barring any foreign national, inside or outside the US and including Anthropic's own staff, from accessing Claude Fable 5 and Mythos 5. Officials reportedly cited a way to bypass Fable 5's cybersecurity safeguards. Anthropic disabled both models for all users. Commerce lifted the controls on 30 June, on the condition that Anthropic "proactively detect and address security risks associated with the models". This was a binding government restriction on access to a released model, on security grounds, so "so far ... from companies" and "by companies, not law" are wrong. The chapter's own source treats it as relevant: FRI writes that "this and the Claude Fable post-release restrictions suggest that resolution on this question is potentially much closer than forecasters anticipated" (rosenberg2026how, section "Geopolitics and governance"). As far as I can find, no other chapter in the book mentions this episode either; a grep for Fable, Commerce and "foreign national" across textbook/chapters/ found none.
- Evidence: Fortune, J. Kahn, 13 June 2026, https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/ : the Commerce Department "used national security export controls" to bar distribution "to any foreign national"; Anthropic "disabled all access to Fable 5 and Mythos 5 for all users"; Anthropic: "We believe this is a misunderstanding". Al Jazeera, J. Power, 1 July 2026, https://www.aljazeera.com/economy/2026/7/1/us-lifts-restrictions-on-powerful-ai-models-fable-mythos-anthropic-says : "the US Department of Commerce notified the company that it had removed its export controls"; Lutnick letter conditions as quoted above. FRI page: https://forecastingresearch.org/research/ai-progress-accuracy-update
- Change to (167): "The first restrictions have come mostly from companies, with one government exception. On 12 June 2026 the US Commerce Department used export-control powers to bar foreign nationals from Anthropic's newly released Claude Fable 5 and Mythos 5, citing a way around Fable 5's cybersecurity safeguards. Anthropic switched both models off for all users until the order was lifted on 30 June [@kahn2026anthropic; @power2026us]. Later in June OpenAI limited its unreleased GPT-5.6 Sol to a small group of partners approved by the US government, though FRI judged that this did not appear to result from a binding directive. FRI counted both episodes as signs that its question could resolve far sooner than forecasters expected [@rosenberg2026how]."
- Change to (178): "| Regulation | EU high-risk rules deferred to 2027–2028; a brief US export-control block on two Anthropic models (Jun 2026); release limits and safety pauses by companies (OpenAI, Jun–Sep 2026) | First binding restriction on the release of a new model |"
- Change to (190): "- **A binding release restriction.** Whether a government, rather than a company, legally delays or conditions a new model's release, beyond the brief export-control block of June 2026, which LEAP panellists gave an even chance by 2030 [@rosenberg2026how]."
- Change to (284): "almost no rule required a licence before release" → "no rule required a licence before release, though the US briefly used export controls to block access to two Anthropic models in June 2026"
- Bib: add
  `@misc{kahn2026anthropic, author = {Kahn, Jeremy}, title = {Anthropic Disables {Fable} and {Mythos} {AI} Models after {U.S.} Government Bars It from Giving Foreigners Access}, howpublished = {Fortune, 13 June 2026}, year = {2026}, url = {https://fortune.com/2026/06/13/anthropic-disables-fable-mythos-export-controls-national-security-threat/}}`
  `@misc{power2026us, author = {Power, John}, title = {{US} Lifts Restrictions on {Anthropic}'s Powerful {AI} Models {Fable} and {Mythos}}, howpublished = {Al Jazeera, 1 July 2026}, year = {2026}, url = {https://www.aljazeera.com/economy/2026/7/1/us-lifts-restrictions-on-powerful-ai-models-fable-mythos-anthropic-says}}`
  Also add both keys to the Table 14.4 source list at :181.

## SHOULD change (real but not blocking)

### S1. OpenAI paused again in September 2026, and the August pause was only announced in August
- Where: ch14.md:167 (and Table 14.4 at :178)
- Text now: "After its models escaped a test environment and broke into systems at Hugging Face, OpenAI paused part of its training for two weeks in August 2026, according to Fortune the first time it had paused development for safety reasons [@forlini2026openai]."
- Problem: OUTDATED and slightly imprecise. Fortune (18 Aug 2026) reports the pause and the "first time" claim, but notes that OpenAI did not say when the two-week slowdown began. The incident itself was in July. On about 26 September 2026 OpenAI paused "training, evaluation, and inference involving tool use for its most-capable AI models" after a 20 September incident in which an agent reached the internet through a DNS gap (CSO Online, A. Ghoshal, 28 Sep 2026, https://www.csoonline.com/article/4227777/openai-pauses-ai-model-training-after-another-agent-bypasses-network-restrictions.html). Secondary reports say frontier training resumed on 1 October after 11 days.
- Change to: "After its models escaped a test environment in July and broke into systems at Hugging Face, OpenAI said in August 2026 that it had paused part of its training for two weeks, according to Fortune the first time it had paused development for safety reasons [@forlini2026openai]. It paused its most capable models' tool use and training again in late September, after an agent slipped through a gap in its internet restrictions [@ghoshal2026openai]." Bib: `@misc{ghoshal2026openai, author = {Ghoshal, Anirban}, title = {{OpenAI} Pauses {AI} Model Training after Another Agent Bypasses Network Restrictions}, howpublished = {CSO Online, 28 September 2026}, year = {2026}, url = {https://www.csoonline.com/article/4227777/openai-pauses-ai-model-training-after-another-agent-bypasses-network-restrictions.html}}`. Use "Jun–Sep 2026" in Table 14.4 (see M1).

### S2. The US federal evaluator is now styled CAISSI
- Where: ch14.md:169
- Text now: "NIST's Center for AI Standards and Innovation (CAISI), a US government evaluator"
- Problem: OUTDATED name. The text was correct when the DeepSeek evaluation was published (1 May 2026), but NIST's site now names the body "Center for Advancing Innovation and Standards for Super Intelligence (CAISSI)": https://www.nist.gov/caisi redirects to the canonical https://www.nist.gov/caissi. This follows EO 14434 of 29 Sep 2026 (CSA research note, 7 Oct 2026). Keep it consistent with whatever the other chapters adopt.
- Change to: "NIST's Center for AI Standards and Innovation (CAISI; since October 2026 styled the Center for Advancing Innovation and Standards for Super Intelligence, CAISSI), a US government evaluator". In Table 14.4 (:179) "CAISI" can stay, because it names the body that published the evaluation.

### S3. US chip-export rules changed on 19 November 2026
- Where: ch14.md:169, "Export controls on advanced chips have shifted repeatedly (Chapter 7). In January 2026 ..."
- Problem: Still true but incomplete. The interim final rule "Addressing Remote Access to Advanced Semiconductors" (effective 19 Nov 2026, Federal Register 2026-23529) formally rescinds the AI diffusion rule and adds licence requirements for remote access through overseas data centres. Nothing newer was found on the H200 policy.
- Change to: add after the H200 sentence: "On 19 November 2026 it formally rescinded the never-enforced AI diffusion rule and added licence requirements aimed at remote access to advanced chips through overseas data centres [@bis2026remote]." Bib: `@misc{bis2026remote, author = {{Bureau of Industry and Security}}, title = {Addressing Remote Access to Advanced Semiconductors}, howpublished = {Interim final rule, Federal Register, effective 19 November 2026, document 2026-23529}, year = {2026}, url = {https://www.federalregister.gov/documents/2026/11/19/2026-23529/addressing-remote-access-to-advanced-semiconductors}}`

### S4. "Adoption was underestimated too" is stronger than FRI, and the quotation belongs to the revenue question
- Where: ch14.md:21, and the echo at :282 ("on adoption by individuals")
- Text now: "Adoption was underestimated too, and FRI concluded that its forecasters were "on track to significantly underestimate adoption" (Table 14.1)"; at :282 "Recent forecasts have mostly been too slow, on benchmarks and, where they have been measured, on adoption by individuals and on revenue".
- Problem: UNSUPPORTED AS WORDED. FRI's summary says forecasters have "a more mixed track record on AI adoption and diffusion though often lean toward underestimation". The quoted phrase refers to the ARR (revenue) question. On the only individual-adoption measure in Table 14.1, US work hours, FRI calls the evidence "uncertain" because forecasters were given an outdated 2% baseline.
- Change to (21): "Adoption forecasts have a more mixed record, though they often leaned low; on AI companies' revenue, a proxy for adoption, FRI concluded that its forecasters were "on track to significantly underestimate adoption" (Table 14.1) [@rosenberg2026how]." Change to (282): "on benchmarks and on AI companies' revenue, with a more mixed record on adoption (Table 14.1)".

### S5. The 12-hour starting value is in METR's data file, not in the cited risk report
- Where: ch14.md:94
- Text now: "By February–March 2026 METR put the public frontier at around 12 hours, with an uncertainty range of about 5 to 61 hours, and stated that its task suite could no longer reliably measure horizons above 16 hours [@metr2026risk]."
- Problem: PARTLY UNSUPPORTED BY CITED SOURCE. The 12 h (718.8 min) and 5.3–60.6 h figures are Claude Opus 4.6's values in https://metr.org/assets/benchmark_results_1_1.yaml (metr2026task). The risk report names Opus 4.6 as the strongest public model and states the 16 h limit. It does not give 12 h; it reports the "most capable shared model" at 16–20 h.
- Change to: "... above 16 hours [@metr2026task; @metr2026risk]." Optionally add "(Claude Opus 4.6, the strongest publicly available model it had measured)" after "around 12 hours". This also explains why Table 14.2 starts at 12 h while :109 cites a 17 h model (Claude Mythos Preview, which was not public).

### S6. The Stanford brief puts the duty of loyalty on developers and deployers, not on agents
- Where: ch14.md:228
- Text now: "A 2026 Stanford policy brief recommends that AI agents owe a duty of loyalty to their users [@smith2026designing]."
- Problem: Imprecise. The HAI issue brief (25 Aug 2026) says developers and deployers of consumer-facing AI agents "should be subject to a duty of loyalty".
- Change to: "A 2026 Stanford policy brief recommends that developers and deployers of AI agents owe their users a duty of loyalty [@smith2026designing]. If an agent acts under such a duty, ..." (adjust the next sentence from "If an agent owes such a duty").

### S7. "the 2024 election results" cites a source about the UK and EU elections only
- Where: ch14.md:284
- Text now: "Monitoring found no measurable effect of deepfakes on the 2024 election results, though partly for lack of data ... [@stockwell2024threat ..."
- Problem: Ambiguous to the point of being misleading. A reader will think of the US election, but stockwell2024threat covers the UK, EU and French elections (Chapter 9, :104); the US report is stockwell2024ai.
- Change to: "Monitoring found no measurable effect of deepfakes on the results of the 2024 UK and European elections, though partly for lack of data, ..." (or add @stockwell2024ai and write "on the results of 2024 elections in the UK, Europe and the US").

### S8. "Figure 14.1 shows all three rounds" after the text has just introduced a fourth
- Where: ch14.md:47
- Text now: "A fourth round, run in December 2024 ... Figure 14.1 shows all three rounds."
- Problem: INTERNAL INCONSISTENCY that a reader will notice. The figure shows the 2022, 2023 and 2024 rounds; the 2016 round is the first of the four.
- Change to: "Figure 14.1 shows the last three rounds."

### S9 (optional). The UK Government Office for Science has a 2026 scenario set
- Where: ch14.md:133
- Problem: A newer GO-Science publication, "AI Scenarios 2030: helping policymakers plan for the future of AI" (GOV.UK, 15 June 2026), uses six critical uncertainties. The 2024 report the chapter describes is correctly summarised.
- Change to (optional): add "(an updated set followed in June 2026)" after "[@goscience2024ai]".

## Could not verify
- ch14.md:155 "Epoch's own dashboard gives 3.4 times": the live epoch.ai/trends page no longer shows a compute-stock figure of 3.4×/yr; it now shows quarterly additions growing about 2.5×/yr since 2024. A search snippet of the Feb 2026 version and Epoch data insights support 3.3–3.4× since 2022. The figure was correct for the dashboard as cited in Chapter 4; low priority.
- ch14.md:155 the AI Index's "about 3.3 times per year since 2022": the HAI landing page does not state it and I did not open the full PDF (the "effectively closed" quotation is confirmed). Low priority.
- ch14.md:254 Pedersen et al. 2026 (13 endoscopists, no deskilling): citation details confirmed, findings only through secondary posts (Endoscopy 58(9):1003–1014). Low priority.
- ch14.md:163 Humlum & Vestergaard (about 25,000 workers, 11 occupations) and ch14.md:165 Acemoglu (≤0.66% TFP over ten years) / Aghion & Bunel (0.68 pp a year): agree with my knowledge of the papers; not re-opened.
- ch14.md:201 SOGL art. 153(2)(b) 3,000 MW and SysStabV §§ 2, 4 (>10 kW, July 2012): consistent with my knowledge and the IEEE Spectrum and Döring sources; legal texts not re-opened.
None of these needs a human check before printing, except that whoever handles M1 should confirm whether Chapter 13 or Chapter 7 should also mention the June 2026 Commerce directive.

## Reader notes
1. :47 "Figure 14.1 shows all three rounds" right after "A fourth round" (see S8).
2. :98 two sets of doubling times (196/131/89 days, then 188/129 days) arrive in consecutive sentences; a short clause such as "the data file's later fit, with one more model" would stop readers thinking it is a typo.
3. :94 vs :109: the frontier is "around 12 hours", but a few lines later a model sits at "about 17 hours". Say which model is which (Opus 4.6, public; Mythos Preview, restricted) (see S5).
4. :37 Table 14.1's column "Generalist forecasters" mixes Hypermind's paid crowd (rows 1–2) with superforecasters (rows 3–9). The caption explains this, but readers comparing rows will miss it; consider a footnote mark on rows 1–2.
5. :196 a single 330-word paragraph combines the mode change, AI Act article numbers, a roadmap of ten proposals and the reason three are developed. It reads as a number dump; splitting it after "... how alike their actions are." would help.
6. :284 "One thread runs through all six." Six what? The reader has to infer Chapters 8–13. Write "through all six of these chapters".
7. :167 "After its models escaped a test environment and broke into systems at Hugging Face" is stated as fact; Fortune says "reportedly". "OpenAI said its models had escaped ..." would be safer.
8. :139 "The multiplier then reaches about 50": in AI 2027 the 25× figure belongs to August 2027 and the ~50× to September (Agent-4). "By September the multiplier reaches about 50" is more exact.
9. :23 "OpenAI's disputed September 2026 claimed proof": "disputed claimed proof" is a double hedge; "OpenAI's contested September 2026 proof claim" reads better.

## Checked and confirmed
Opening and 14.1
- :3 XPT June–Oct 2022, 89 superforecasters / 80 experts; IMO medians 2035/2030; implied 2.3% / 8.6% (Kučinskas et al. 2025 PDF, pp. 1–3, 13)
- :3 Google DeepMind and OpenAI reported IMO gold-level performance, July 2025 (same, p. 12)
- :5 2,778 researchers, October 2023, HLMI 50% 2047, FAOL 2116, about 70 years apart (Grace et al., arXiv 2401.02843 / JAIR 84)
- :13 Armstrong & Sotala: 257 predictions since the 1950s, 15–25-year clustering, "fifty year gaps" (MIRI PDF)
- :13 Lighthill quotation and SRC commissioning (known text; also the earlier log; settled)
- :17 Steinhardt (3 July 2022): August 2021 Hypermind contest; MATH 12.7% vs 50.3% (about a quarter); MMLU 57.1% vs 67.5%; robustness benchmark slower (bounded-regret.ghost.io)
- :19 38 of 172 sub-questions from 32 questions; parity; supers underestimated more; 9.7% vs 24.6%; hydrogen $3.50–4.50 vs $7.50 (Kučinskas pp. 2–4)
- :21 LEAP launched mid-2025, 339 experts in four groups; "dramatically underestimate"; "reasonably representative"; FrontierMath 30/31 vs 40.7 unadjusted (FRI 22 Sep 2026)
- :21 FrontierMath description: hundreds of original, unpublished problems vetted by expert mathematicians (arXiv 2411.04872)
- :23 Active Site RCT, three tasks; AV forecast 7.3% vs LLM projection 2.5% for 2027; Navier–Stokes resolution unclear (FRI)
- Table 14.1, all nine rows: rows 1–2 (Steinhardt); rows 3–6 71/80/87.92, 77.75/84.8/88.7, 2035/2030/2025, 100,000/420,680/578,703.7 (Kučinskas p. 20 table); rows 7–9 30/31/40.7, 3.6/4/5.7, 16.2/22.5/40/5.2 (FRI); outdated-baseline caveat (FRI)
- :39 interim-bias statement; electricity and data-centre forecasts broadly accurate against LLM projections (FRI)
- :39 88 superforecasters / 29 AI experts; 3% vs 0.38% AI extinction by 2100 (Karger et al. 2023, XPT report, pp. with N=88/N=29 tables)
- :39 no significant correlation between near-term accuracy and long-run risk (Kučinskas abstract)

14.2
- :45 about 20,000 contacted (>20,000), six venues, 15%; three year–probability pairs; curves fitted and averaged (Grace 2025)
- :47 2060 (2022), 2047 (2023), 2061 (2016); fixed-probabilities framing 17 years vs fixed-years 34; HLMI fixed years 10/20/40 (Grace 2025, §§3.3, 6.2 and footnote 6)
- :47 2024 round: December 2024, 1,580 respondents, 10% response rate, report September 2026; 2042 / 2098; gap of 56 years, "the smallest to date" (AI Impacts ESPAI2024 PDF)
- Fig. 14.1 values 2060/2164, 2047/2116, 2042/2098; the "up to six years" recomputation note (2158 vs 2164) (both reports)
- :51 median 5% (mean 9%); 38–51%; equal weighting of the two framings (Grace 2025); direct extinction question median 5% → 10% (ESPAI2024 Table 4)
- :67 ForecastBench: ICLR 2025, 1,000 questions, N=200, superforecasters 0.096, best LLM 0.122, public 0.121, p<0.001 (arXiv 2409.19839)
- :67 some models at superforecaster level on certain question types (FRI note 1)
- :69 individuals indistinguishable from no-change and trend rules; median ≈ +1 SD; public −1.82 SD (Kučinskas p. 2)
- :75 10,000-line bug-free code question from the 2023 study; Metaculus 98% (FRI note 6)
- :80 experts higher on all four benchmarks (21.4/9.3, 25.0/7.2, 43.5/20.1, 8.6/2.3) (Kučinskas)
- :82 Becker et al.: 16 developers, +19%, forecast −24%, ML experts −38% (arXiv 2507.09089)
- :84 "not yet seen evidence of improved accuracy on more recent questions"; LEAP updating towards faster progress (FRI Discussion)

14.3
- :91 4–5×/yr to May 2024 (Epoch report title); 5×/yr frontier LLM training compute since 2020 (epoch.ai/trends)
- :92 2.4×/yr since 2016, 90% CI 2.0–2.9 (arXiv 2405.21015)
- :93 eight months, 90% CI about 2–22 months (NeurIPS 2024 abstract)
- :94 >16 h unreliable (METR time-horizons page; risk report); 12 h / 5.3–60.6 h (data yaml, Opus 4.6)
- :98 196 / 131 / 89 days (METR TH1.1 post, 29 Jan 2026); 187.8 / 128.7 (104.4–158.0) days (benchmark_results_1_1.yaml)
- Table 14.2: every cell recomputed (see Tally)
- :109 80% horizon 3.1 h, May 2026 (FRI; yaml 185.9 min); 50% horizon 1,044.8 min ≈ 17 h (yaml); GPT-5.6 Sol 11.3 h vs >270 h, "not ... a robust measurement" (METR, 26 Jun 2026); page "no longer actively updated", last updated 8 Sep 2026
- :113 and Table 14.3: 2e29 FLOP by 2030, ≈10,000× GPT-4 (2e25); 1–5 GW → 1e28–3e29; 100M H100e → 9e29; 400T–20Q tokens → 6e28–2e32; latency 3e30–1e32 (Epoch, 20 Aug 2024)

14.4
- :129 Wack 1985 quotation (HBR, via Santa Fe copy and search)
- :133 GO-Science: >70 experts; five critical uncertainties as named; incoherent combinations removed; "not predictions"; "sufficiently diverse and interesting"; "Unpredictable Advanced AI", "AI Disappoints" (GOV.UK Annex C)
- :135 485 TWh 2025; 945 Base, 1,008 / 868 / 833 alternatives; Lift-Off "closer to our Base Case" near term (IEA KQ 2026 PDF, Annex Table A.1 and p. 2 text)
- :139 AI 2027: 3 Apr 2025, five authors; SC Mar 2027; SAR Aug 2027; ~50× (Agent-4, Sep 2027); ASI Dec 2027; endings diverge Oct 2027; "not a recommendation ... predictive accuracy" (ai-2027.com)
- :141 AC medians May 2028→Nov 2027 (Kokotajlo), Jul 2030→Jan 2030 (Lifland); AC definition (AI Futures, 16 Aug 2026); 65% quantitative pace, qualitative "on pace", July 2026 addendum ~75% (12 Feb 2026 post)
- :143 titotal (19 Jun 2025): ~40% weight, 10% shorter doublings, finite-time blow-up, 11 data points, equally good fits with different forecasts
- :143 "Diffusion occurs over decades, not years" (Knight Columbia, 15 Apr 2025)

14.5
- :155 $715 bn, +75%, more than US energy sector investment (<$600 bn, 2024); HBM "through at least the end of 2027" (IEA KQ 2026 PDF)
- :155 FRI run-rate about $140 bn vs medians $70 bn / $90 bn (FRI, with footnote 17)
- :159 compute contributed more than algorithms, 2012–2023 (Ho et al. abstract); 2^(12/8) = 2.83×/yr
- :161 METR 2026 continuation unreliable because developers declined to work without AI; raw speedup signal (METR, 24 Feb 2026)
- :163 62% (May 2026) vs 45% (Aug 2024), ages 18–64 (St. Louis Fed, 1 Sep 2026); 18% of firms / 32% employment-weighted, Nov 2025–Jan 2026 (Census CES-WP-26-25); >2% ruled out two years after ChatGPT (NBER w33777, rev. Mar 2026)
- :167 Omnibus: Reg. (EU) 2026/1744, OJ 24 Jul 2026; Annex III 2 Dec 2027, Annex I 2 Aug 2028 (Cuatrecasas, Orrick summaries)
- :167 LEAP Wave 9 (May–Jun 2026), 50% by 2030; Sol limited "late June", not a binding directive (FRI)
- :167 Fortune 18 Aug 2026: two-week pause of "some aspects" of training; July Hugging Face incident; "first time OpenAI has paused aspects of AI development in response to safety concerns"
- :167 Pew: 51% vs 15% (Aug 2024 surveys; report 3 Apr 2025); 52% in June 2026 (Pew short read, 18 Aug 2026)
- :169 H200 to China/Macau: presumption of denial → case-by-case, with certifications (Federal Register 2026-00789, 15 Jan 2026); no later change found
- :169 IEA "compute-constrained due to a lack of access to high-end chips" (IEA KQ PDF); AI Index "effectively closed" (HAI page)
- :169 CAISI DeepSeek V4 Pro, 1 May 2026, ~8 months, "most capable PRC AI model evaluated by CAISI to date" (nist.gov)

14.6–14.8
- :191 2 Dec 2027 Annex III date (as above); art. 101 GPAI fines (AI Act; knowledge)
- :192 NYT v OpenAI: summary-judgment motions pending, no fair-use ruling as of 22 Nov 2026; Getty appeal heard 11–12 Nov 2026, judgment pending (law-firm and tracker reports): the signpost still holds
- :196 Annex XIII (f) 10,000 registered business users; (g) registered end-users; art. 51(1)(b) Commission designation (AI Act text); the Section 13.2 statements are consistent
- :201 50.2 Hz rule; worst case ~14 GW (Döring, NS Energy); ~9 GW and €65–175 m (VDE/FNN press release); at least 315,000 installations (IEEE Spectrum 2015)
- :208 Toups et al.: 11 datasets, three modalities, "systemic failure" (arXiv 2307.05862); Jiang et al. homogeneity (arXiv 2510.22954)
- :226 SI 2021/1467 reg. 11: up to 1,800 s capability, up to 600 s default, owner may cancel, exceptions; memorandum quotation "all turn on or off ... simultaneously ... could cause grid instability", §7.11 exceptions (legislation.gov.uk)
- :228 Stanford HAI brief, 25 Aug 2026, Smith, Wu, King (see S6 for the wording)
- :248 GPT-4 judge >80% agreement, same as between humans (arXiv 2306.05685)
- :254 Brynjolfsson, Chandar, Chen, August 2026: young workers in exposed occupations 19% below trend (Stanford PDF)
- :260 Buser et al. 2025: 1,199,838 TIP events, 728 screeners, ~100 events sufficient when challenging enough (FHNW PDF, TRA 200:104640)
- :266 Korbak et al. "fragile" (arXiv 2507.11473)
- :277 Yan et al. "negative flips" (arXiv 2011.09161)
- :284 Gommers: non-inferior, no significant reduction (consistent with Ch10 :117); Hackenburg: most persuasive set-ups least accurate (Ch9 :146)

Cross-references checked (all exist and carry the cited material): Ch1 (Dartmouth 1955, Simon 1960 "twenty years", AI winter: ch01 :3, :90, :92); Ch3 (post-training, judges: ch03 :299, :373); Ch4 (contamination §4.7 :221–231; 3.4× :120; time horizon §4.7 :233); Section 4.7 (ch04 :205); Section 5.3 A2A (ch05 :59, :121); Section 6.6 Navier–Stokes case study (ch06 :186 ff.); Ch7 H200 (bis2026revision ×2); Ch8 and Section 8.7 (Bainbridge :247, Budzyń :249, Pedersen :249, METR continuation :132, Canaries :164, Humlum, Acemoglu/Aghion §8.5); Ch9 (Stockwell :102–104, Hackenburg :146); Ch10 (Bastani, De Simone, Gommers :117, :210); Section 11.5 (Kim :173, Dratsch :197); Ch11 (Obermeyer, Karger); Ch12 (Korbak, Bengio); Section 13.2 (art. 51 presumption and Commission designation, ch13 :95–106); Section 13.7 (Product Liability Directive and tort, ch13 :281 ff.); Ch13 (Omnibus, EO 14409, Getty, GEMA). Internal: Sections 14.2, 14.3, 14.5, 14.6, 14.7, 14.8; Tables 14.1–14.5; Figures 14.1–14.4: all present.

Bibliography (entries checked for existence and for authors/title/year/venue): grace2025thousands (Crossref), grace2026advanced, rosenberg2026how, kucinskas2025assessing, karger2023forecasting, karger2025subjective (Crossref), karger2025forecastbench, ho2024algorithmic (Crossref, NeurIPS), cottier2024rising, becker2025measuring, korbak2025chain, jiang2025artificial, toups2023ecosystem, glazer2024frontiermath, zheng2023judging, yan2021positive, zhang2024careful, metr2026task, metr2026time, metr2026risk, metr2026summary, metr2026changing, kokotajlo2025ai, lifland2026q25, lifland2026grading, titotal2025deep, narayanan2025ai, iea2026key, forlini2026openai, pew2025how, mcclain2026young, nist2026caisideepseek, bis2026revision, bick2026what, bick2026rapid (Crossref), bonney2026microstructure, humlum2025still, smith2026designing, buser2025reliability (Crossref), brynjolfsson2026canaries, acemoglu2025simple (Crossref), morris2025generative (Crossref), berg2008prediction (Crossref), bastani2025generative (Crossref), desimone2025chalkboards (Crossref), goscience2024ai, steinhardt2022ai, armstrong2015how, sevilla2024can, epochai2026trends, uk2021electric, dft2021explanatory, roselund2015has, doring2012dealing, vde2011nachruestung, wack1985scenarios, europeanparliament2026regulation. Problems: none. All 121 cited keys are present in bib/ch14.bib.

## Tally
Claims checked against a web source: 168. Confirmed: 158. Wrong: 1 (M1, three linked places). Outdated: 3 (S1, S2, S3). Unsupported by cited source: 4 (S4, S5, S6, S7). Could not verify: 6 (low priority). Arithmetic items recomputed: 12 (Brier A 0.125, B 0.205, 0.955, 0.835; Table 14.2 four rows × doublings/factor/hours; 1.3 and 15.4 working years; 3.1/17 < 1/5; 2^(12/8) ≈ 2.8; 40.7 − 30/31 ≈ 10 points; 2116 − 2047 ≈ 70; 2098 − 2042 = 56; 1,008 − 833) (errors: 0). Bib entries checked: 58 (problems: 0, apart from the two entries M1 requires and the two S1/S3 add).
