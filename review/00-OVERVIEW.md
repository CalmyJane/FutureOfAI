# Critique of *Understanding AI: Technology, Trends and the Decade Ahead*

Review of the manuscript on branch `claude/sharp-ritchie-o30bou` (`textbook/`), at commit `7eb12d5` (25 October 2026).

The detailed referee reports for each chapter are in this folder:

| File | Covers |
|---|---|
| `01-preface-ch01-ch02.md` | Preface; Chapter 1 (What we mean by "AI"); Chapter 2 (Neural networks) |
| `02-ch03-ch04.md` | Chapter 3 (LLMs); Chapter 4 (Scaling) |
| `03-ch05-ch06.md` | Chapter 5 (Agents); Chapter 6 (Science, mathematics, engineering) |
| `04-ch07-ch08.md` | Chapter 7 (Chips, energy, open models); Chapter 8 (Work and economy) |
| `05-ch09-ch10.md` | Chapter 9 (Information and democracy); Chapter 10 (Education, health, everyday life) |
| `06-ch11-ch12.md` | Chapter 11 (Risks); Chapter 12 (Alignment, interpretability, evaluation) |
| `07-ch13-ch14.md` | Chapter 13 (Governance); Chapter 14 (Forecasting and proposals) |

Each report gives, for each chapter: (A) factual and reference errors, with `file:line`, a quote, what the source actually says, and a severity; (B) technical and conceptual problems; (C) writing and explanation; (D) structure and coverage; (E) figures and tables; and (F) a reference-check tally. Each report ends with a priority list.

---

## How this was checked

- **Reading.** All 14 chapters and the preface (about 140,000 words) were read in full, two chapters per reviewer, each reviewer acting as referee and editor together.
- **Mechanical bibliography check, all 14 bib files (1,023 unique entries).**
  - Every citation key in the text was matched to a bib entry.
  - All 344 DOIs were resolved against Crossref, arXiv or DataCite, comparing title, year and first author.
  - All 672 URLs without a DOI were fetched.
  - Duplicate entries and cross-chapter conflicts were checked.
- **Claim-level check against sources.**
  - About 550 load-bearing claims (numbers, dates, quotes, study designs, legal facts) were compared with the primary source, fetched live where possible.
  - Every worked example and table of arithmetic was recomputed.
  - The tokeniser and next-token-probability tables in Chapter 3 were reproduced by running GPT-2 and Qwen2.5 locally.
- **Limits.**
  - About 300 sources could not be opened from the review environment: openai.com, the Federal Register, iso.org, the IEA, SSRN, sec.gov and some law-firm pages return 403, and some sources are paywalled. The reports list these as "couldn't verify", not "wrong".
  - In Chapters 13 and 14 (and for some keys in Chapters 3–4), about 70 claims were checked against the reviewer's own knowledge of the primary text rather than a fresh fetch. Treat those as weaker checks.
  - Material dated after mid-2026 could only be checked where the source was online.

## Verdict in one paragraph

This is an unusually well-sourced popular-science book. The bibliography is clean: no fabricated references, no wrong DOIs, every key resolves, and the metadata is correct for nearly every entry. The author's own computations are right throughout. The weaknesses are of a different kind.

**Where it is weakest:**
- **Selective reporting of results.** The book often gives the half of a finding that fits the paragraph and drops the half that complicates it.
- **One-sided handling of company material**, especially Anthropic's own incidents and claims.
- **Breaches of its own evidence-labelling promise.** These happen in every chapter.
- **Material that is out of date even as of October 2026** in the fastest-moving sections.
- **Number-dense prose.** Too often it reads as an annotated literature list rather than an argument.

**What is at stake.** None of this is fatal. But the book sells itself on "what is known, how it is known and how well it is known", so these are exactly the failures a hostile reviewer would quote.

---

## Part 1: Problems that run through the whole book

### 1.1 The delivered PDF does not match the manuscript (critical, production)

`textbook/delivery/understanding-ai_A5_interior.pdf` was built at 12:48 UTC on 25 October. After that came:
- commit `0fa6574` (16:06), which made page-level source lines the default and rewrote the preface to describe them;
- seven source-audit commits.

As a result:
- **The citation scheme contradicts the preface.** The "print-ready" PDF still carries about 675 APA author–year citations in running text, while the current preface says "the sources are not cited inside the sentences: a line at the foot of each page lists the numbers of the sources".
- **The source-audit corrections are not in it.**
- **The README is stale too.** `delivery/README.md` describes the old build ("564 pages").

**Fix:** rebuild, and add a build-time check that fails if the delivery PDF is older than the newest chapter.

### 1.2 The page-level citation system undercuts the book's main selling point (major, design)

In the sample build (`sample-ch10-source-line.pdf`), a page ends with a line such as "Sources 17". On a page that discusses five studies, the reader cannot tell which claim rests on which source. That is a step backwards for a book whose preface promises claim-level traceability.

Two further problems:
- **Tables and figures cite differently from the text.** In the same sample, table captions still use APA author–year citations, so the book mixes two systems.
- **Numbers do not fit how readers use the book.** Readers of this kind of book want to check a specific number.

**Recommendation:** use numbered superscripts at the sentence (or paragraph) level, and keep page-foot source lines only if they carry those numbers. At minimum, use one system throughout, including captions.

### 1.3 The evidence-labelling rules in the preface are broken in every chapter (major)

The preface (`ch00-preface.md:25–34`) promises two things:
- preprints and working papers are labelled at first mention in each chapter;
- company claims are introduced with "according to the company".

In practice:
- **"According to the company" appears 5 times in the whole book.** More than 100 citations go to company sources: OpenAI, Anthropic, Google/DeepMind, Meta, DeepSeek, Nvidia, Microsoft, xAI.
- **Every reviewer found unlabelled preprints, working papers and company claims.** Examples:
  - Mitchell, Kaplan and the GPT-1/GPT-2 reports (Chapter 1);
  - the Shazeer and GELU preprints, and Kimi's company claim that Muon beats AdamW (Chapter 2);
  - about 10 places in Chapters 3–4;
  - METR, Peng et al., Aghion & Bunel and Fairlie & Wu (Chapter 8). The evidence log says the METR label was added; it was not;
  - OpenAI's GPT-6 Astra safeguards, stated as fact (Chapter 14);
  - the AI Impacts 2024 report and Grace's 2016 blog post (Chapter 14).
- **The scheme has no category** for news reports, magazine columns, leaderboards, company telemetry or usage statistics. These carry a lot of the 2025–26 material.

**Fix:** add those categories to the preface, then run one mechanical pass over every company-, arXiv-, NBER-, SSRN- and news-sourced key and check its first mention in each chapter.

### 1.4 Selective reporting: the most serious recurring flaw (major)

The pattern recurs in every part of the book:

| Where | What the book gives | What it leaves out |
|---|---|---|
| Ch10, Vaccaro et al. (2024) | Human–AI teams worse than the better of either alone (g = −0.23) | Human–AI teams *better than humans alone* (g = 0.64) |
| Ch10, Penda Health | Adjusted odds ratio 0.77 (AI helps) | Raw rates point the other way (2.2% vs 2.0%). The evidence log says they were dropped on purpose |
| Ch10, Kraft box | "All the AI tutoring results below are large" | The chapter's own table contains −17%, −0.37 SD and null results |
| Ch10, Folk & Dunn (2026) | Isolation predicts chatbot use | The abstract's headline null: use did not predict lower social connection |
| Ch11, endoscopist deskilling | "Approximately 6% lower" | 28.4% → 22.4% adenoma detection, a relative fall of about 21%; the log records it |
| Ch9, Costello et al. | Effect hedged via a press release | The abstract: the effect held "even among participants with deeply entrenched beliefs" |
| Ch2, adversarial training | Clean error 0.94% → 0.84% as evidence of robustness | The robustness number: adversarial error 89.4% → 17.9% |
| Ch8, AI and learning | "The one study that tested learning" found AI reduced it | The chapter's own flagship call-centre study says AI "facilitates worker learning" |
| Ch8, Challenger layoffs | 39% fall | Challenger's own note: 15% excluding government cuts |
| Ch4, "diminishing returns of pre-training" | GPT-4.5 vs o3-mini | The same OpenAI table shows GPT-4.5 well ahead of GPT-4o (AIME 9.3% → 36.7%) |

**Fix:** a rule for the revision. Wherever a study is used for a point, check whether its abstract's headline finding is the one being reported. If not, say what the headline finding is and why the text uses a different number.

### 1.5 Company material, especially Anthropic's, is handled too gently (major)

- **Chapter 12 softens Anthropic's own record:**
  - It describes constitutional classifiers without saying that Anthropic's own February 2025 public challenge produced a universal jailbreak.
  - It softens Anthropic's evaluation incidents: Opus 4.7 kept attacking after judging its target was probably real, and Mythos 5's malicious package ran on 15 real systems.
  - "Anthropic appeared to comply" (UK access) is not supported by the cited article.
- **Chapter 7 relies on an interested party.** It quotes Dario Amodei three times on export controls, DeepSeek and costs, with no mention of his position as chief executive of a competing lab. Critics of the controls are never named.
- **Chapter 5 tilts the agent evidence.** The "what works" side rests almost entirely on vendor material, while the critical side is academic. The chapter never says so.
- **Chapter 6 states OpenAI's Navier–Stokes claim as fact.** It is sourced to *Quanta*, not to OpenAI's announcement or to the critique the chapter itself cites (Bastounis et al.).

In a book this sceptical of company claims elsewhere, these lapses stand out. The pattern in Chapter 12 could be read as favouring one lab.

### 1.6 Inconsistencies between chapters (major as a group)

- **GPT-3 training compute:** 3.14 × 10²³ (Ch1) vs 3.2 × 10²³ (Ch4).
- **ClockBench human baseline:** 90.1% vs 90.7% (Ch3 vs Ch4).
- **ChatGPT weekly users:** 1.2 billion in the Ch1 text, but Figure 1.3 ends at 900 million. Ch10 uses "more than 800 million".
- **First practical success of deep learning:** "speech, 2011" (Ch1) contradicts LeNet reading cheques in the 1990s (Ch2).
- **The OpenAI–Hugging Face incident:**
  - It is told about six times across Chapters 11–12.
  - It is classed as loss of control in Ch11 but as specification gaming in Ch12.
  - Ch11 says it was "already contained"; Ch12 says it was "detected and stopped".
- **"Mythos 5"** appears in Ch11 without ever being introduced.
- **EU AI Act timetable:** the Chapter 13 opening implies the Annex I product rules were due in August 2026 and deferred two years. They were due in August 2027 and deferred one year, as the chapter's own Table 13.1 shows.
- **Terminology:**
  - "%" vs "per cent" in running prose (Ch5 vs Ch6; Ch11 vs Ch12);
  - "NVIDIA" (12 times) vs "Nvidia" (20 times);
  - three currency notations.

**Fix:** keep one canonical fact sheet: one value per recurring number and one name per recurring entity. The build could lint against it.

### 1.7 Reasoning errors, distinct from wrong numbers

- **Ch8:220, productivity.** The gap between 1–3% of total work hours saved (surveys) and 15%+ within tasks (experiments) is read as evidence of a slow "J-curve" payoff. It is mainly a matter of how few hours AI touches.
- **Ch8:170, entry-level hiring.** A St. Louis Fed decomposition of demand for AI skills in job ads is counted as evidence that AI is cutting entry-level hiring.
- **Ch12, safety layers.** The Swiss-cheese figure assumes the layers fail independently. That contradicts Chapter 11's own lesson on correlated failure: evaluation awareness can line up every hole at once.
- **Ch12, specification gaming.** The box says a model "has no access to the intention" behind its target. The chapter's own o3 example contradicts it: o3 states that its plan violates the user's intent.
- **Ch13, innovation debate box.** It argues that because the EU investment gap opened before the AI Act applied, the Act cannot have caused it. That does not follow: expectations matter.
- **Ch14, Proposal 14.6.** Its liability cap rewards signers who *fail* the seeded-error test: lower measured capacity gives a lower cap.
- **Ch14:258, the last paragraph of the book.** It says forecasts were "too fast on how quickly capability changes firms". The chapter's own Table 14.1 shows adoption was *under*-forecast (3.6–4% predicted against 5.7% actual), as was revenue.
- **Ch2:274, generalisation.** "Classical theory predicts bad generalisation" is wrong: classical bounds simply become vacuous for networks this large.
- **Ch1:15, definitions.** The legal definitions are called "behavioural", but their key word, "infers", is a test of mechanism. The chapter's own concept box makes this point.

### 1.8 Out of date as of October 2026

The book's promise is "as it stands in October 2026", so these count as errors:
- **Ch5, METR time horizon.** The headline 12 hours for Claude Opus 4.6 is given without its very wide confidence interval (about 5–61 h). A later model reached about 17 h in April 2026, and METR stopped updating the series on 8 September.
- **Ch6, olympiad mathematics.** The "modest picture" for public models rests on the USAMO 2025 result (25%). By 2026 public models scored near 95% on the USAMO and 42/42 at the IMO, the latter per the AFP source the chapter already cites.
- **Ch6, MatterGen.** A 2026 *Materials Horizons* critique is missing: the "new" TaCr₂O₆ is a phase reported in the 1970s and was in the training data. This is the same disorder error the chapter documents for GNoME and A-Lab.
- **Ch3, DeepSeek-R1.** The chapter puts the RL stage at "about 20 per cent" of pre-training, citing Epoch's May 2025 estimate. DeepSeek's own *Nature* supplement (September 2025), which the chapter already cites, implies about 5% (147K vs about 2.79M GPU-hours). Figure 3.3 inherits the error.
- **Ch5, MCP examples.** They follow the 2025 specification while the text calls the July 2026 revision current.
- **Ch13, missing laws.** South Korea's AI Basic Act (in force January 2026) and Japan's 2025 AI law are not covered.

### 1.9 Writing: what makes the book harder to read than it should be

- **Number density.** Chapters 4 and 7 run at about 11 numerals per 100 words; Chapters 2 and 3 at about 9. A reader cannot hold that.
  - Worst stretches: §7.2 (TSMC), Ch7:118 (export controls), §8.1 (method detail), Table 3.8, §4.7, Table 4.4, Ch1:5 and Ch1:234.
  - Rule of thumb: one load-bearing number per sentence, at most three per paragraph. Move the rest to tables or notes.
- **Paragraphs that list studies without an argument.** Examples: Ch12:228 (seven incidents in a row), Ch14:21 (a 330-word paragraph with a Navier–Stokes digression), the omnibus and executive-order paragraphs in Ch13, and §13.2, which walks through the AI Act article by article with no worked example. Each needs a topic sentence that states the claim and an order that serves it.
- **Long sentences.** On average they run 22–25 words, which is acceptable. But 64 sentences in Ch1 and 66 in Ch13 exceed 35 words, often because a citation-laden clause has been tacked on. Example: the Astra sentence at Ch3:116 carries a release date, Epoch's records, a risk rating, the Preparedness Framework and a cross-reference.
- **Colons as connectors.** There are about 437 mid-sentence colons across the 14 chapters. It is the book's strongest verbal tic and gives the prose a clipped, list-like rhythm. Use them only before a list or a genuine expansion.
- **Revision history leaking into the text.** Examples: "earlier versions headlined 13%" and "Kalamkar et al. print 3.38e38 (truncated)" (Ch7–8). That belongs in the evidence log, not in the book.
- **Jargon used before it is defined.** This happens in several chapters:
  - SXM5, HPL, H100-equivalents, CoWoS (Ch7);
  - red-teaming, KL divergence, probing, ExploitGym, deliberative alignment (Ch11–12);
  - "AGI", never defined at all (Ch1);
  - in-context learning, which opens Chapter 3 and is never explained;
  - encoder versus decoder, which Figure 3.2's "not masked" inset relies on.
- **Symbols.** β is used for two different constants in one paragraph (Ch12:29).
- **Boxes and placement.** Some boxes do not earn their place: Ch1 has a duplicate definition box, and the Token concept box in Ch3 repeats the text. The Ch10 synthesis paragraph sits under the 10.8 Accessibility heading.

### 1.10 Structure and coverage gaps

- **Chapter 1** spends about 2.5 pages on MYCIN but leaves out RLHF and InstructGPT, GPT-4, open-weight models, diffusion and AlphaFold from the 2018–2026 history. That is the period readers buy the book for.
- **Chapter 2** has no mixture-of-experts section. Readers will apply the 6N rule to Kimi K2's 1.04 trillion total parameters instead of its 32 billion active ones. Recurrent networks and the 2006 pre-training revival are also missing.
- **Chapter 5** says almost nothing about how agents were actually used in 2025–26.
- **Chapter 6 promises "engineering" and barely delivers it.** The AlphaChip controversy would fit its argument well. David Baker's protein-design half of the chemistry Nobel is named and then dropped.
- **Chapter 7** omits chip-design software (EDA) as a chokepoint, though the US has used it as one. It also omits China's domestic chip progress and chip smuggling, so its "Do the controls work?" question cannot be answered. There is no debate on whether the capital spending can pay for itself.
- **Chapter 9** omits AI content farms, deepfake fraud, chatbots as the channel for misinformation (data poisoning, wrong election answers) and the UK offence of creating sexual deepfakes (Table 9.3).
- **Chapter 10** omits Bean et al. (Oxford randomised study of the public using chatbots for medical questions), teachers' own use of AI, and counter-evidence on detector bias.
- **Chapter 11** has nothing on military AI or autonomous weapons. Table 11.1 is missing MIT domain 2 (privacy and security).
- **Chapter 12** barely touches the technical responses to Chapter 11's present-day harms: bias, hallucination, privacy. A one-page table mapping each risk to its defence would join the two chapters.
- **Chapter 14:**
  - The ten proposals do not visibly follow from the forecasting evidence or from Chapter 13's governance gaps.
  - The "this is the author's position" framing is buried halfway through §14.6. Move it to the top.
  - The book ends by summarising its last two sections. It needs a proper close: what to watch, and a labelled bottom line from the author.

### 1.11 Evidence logs and housekeeping

- **The evidence logs disagree with the text** in places, so they cannot be trusted as an audit trail:
  - Nickow: log 0.37 against text 0.288. The text is right; 0.37 is the 2020 NBER figure.
  - The `chatterji2025people` vs `chatterji2025how` key.
  - The METR label "added" in Ch8.
  - The AISI misquote ("free speech" for "bias or freedom of speech"), copied into the Ch13 log.
- **Bibliography files:**
  - `bib/ch12.bib` has a stray `}` at line 353 that may break BibTeX or biber.
  - 19 bib entries are never cited: `raina2009large`, `elhage2022toy`, `kwa2025measuring`, `kaplan2020scaling` (ch07.bib), seven in ch12.bib, two in ch13.bib and five in ch14.bib.
  - Metadata nits:
    - The AI Index entries use invented titles ("The AI Index 2025 Annual Report"); the real title is "Artificial Intelligence Index Report 2025". The same applies to 2026.
    - `humlum2025still` has year 2026 against NBER's 2025.
    - `defreitas2025ai` has 2025 against Crossref's 2026 issue year.
    - VALL-E is called a "2023 preprint" in the text, but the bib entry is the 2025 journal version.
- **Layout.** About 40 pages in the main PDF have large blank areas where a figure or table was pushed to the next page; p. 140 is an example. On A5, five-column tables (for example Table 10.1) hyphenate badly ("pa-per", "stu-dents").

---

## Part 2: Priority fix list

Ordered by damage if left in. Each item is verified against the source unless marked otherwise; details and quotes are in the chapter reports.

1. **Rebuild the delivery PDF and README** (§1.1).
2. **Rewrite the book's final paragraph** (ch14:258). It contradicts Table 14.1.
3. **Fix the Chapter 13 opening** (ch13:3). The Annex I date was 2027 and the deferral one year.
4. **Ch3:322 and Figure 3.3.** The DeepSeek-R1 RL share is about 5% per DeepSeek's own *Nature* supplement, not about 20%.
5. **Ch4:224, METR task range.** HCAST tasks run from 1 minute to about 30 hours, not "8 hours". As written, it contradicts the chapter's own 16-hour figure.
6. **Ch4:236.** Rebuild the "diminishing returns of pre-training" argument.
7. **Ch1:112 and Table 1.2, MYCIN certainty factors.** The chapter shows the 1975 rule (CF = MB − MD), which MYCIN dropped around 1977. The later rule gives 0.38, not 0.34.
8. **Ch1:260, EU AI-definition guidelines.** The chess program is excluded under para. 48 (it does not learn from data), not under the "used for many years" test (para. 42). The "AI effect written into regulation" claim falls with it.
9. **Ch2:309 and Ch2:300.** Fix the adversarial-training numbers. Correct the overstatement of Zech et al.: the hospital-identification networks were trained separately for that purpose, and the paper says site information "may confound".
10. **Ch5:287, Cemri et al.** Humans annotated 150 traces; the 1,600+ were labelled by an LLM judge.
11. **Ch5:150, SWE-bench Pro.** The "41.8 → 25.9" comparison splices two tables from two versions of the paper. Remove it.
12. **Ch5:162, METR.** Add the confidence interval and the later 17-hour result. Note that the series stopped on 8 September 2026.
13. **Ch6.** Add the MatterGen critique, update the olympiad evidence to 2026, and recast Navier–Stokes as a contested claim, in a box, with primary sources.
14. **Ch7:140.** The LBNL 2023 figure (176 TWh) is compared with the IEA's *2024* figure. The IEA's own 2023 figure is 154 TWh, a 14% disagreement.
15. **Ch7:49.** Say that the "1.4 exaflops" for the GB200 NVL72 is a 4-bit, sparse figure. The chapter itself warns about this trap six lines earlier.
16. **Ch8:220, Ch8:170, Ch8:252, Ch8:174.** Fix the productivity reading, the misuse of the St. Louis Fed evidence and the false "one study" claim. The "decisive test" is already in a study the chapter cites (Hosseini Maasoum & Lichtinger).
17. **Ch9.**
    - The watermark argument is contradicted by Zhang et al.: a weaker model suffices.
    - The robocall framing needs the FCC's February 2024 ruling.
    - Costello should be reported from the abstract.
    - The Salvi and Hackenburg/Lin results on personalisation need reconciling.
    - Add the UK offence of creating sexual deepfakes to Table 9.3.
18. **Ch10.** Restore the omitted halves of Vaccaro, Penda and Folk & Dunn; fix the Kraft "all large" sentence; Therabot access was 8 weeks, not 4; the New York law is cited from an unsigned bill.
19. **Ch11.** Date the 96% deepfake figure (2019, Deeptrace) and restore the deskilling size. "19 actions that reached real people" overstates the AISI report, which also notes that AISI itself enabled internet access and switched off the classifiers. Introduce "Mythos 5".
20. **Ch12.** Correct the softened Anthropic and METR incident accounts. Add the two companies' admissions of accidental chain-of-thought training. Table 12.1's 30.4% is all reward hacking, not "grader tampering". Fix the specification-gaming box and the Swiss-cheese independence assumption.
21. **Ch13.**
    - The AISI quote should read "bias or freedom of speech".
    - The Code of Practice is voluntary, not a "legal duty".
    - Check Art. 101 before claiming reduced fines for small firms "in all tiers".
    - Getty's remaining claim was a "copyright" claim.
    - Add the "not used for professional purposes" qualifier to the Product Liability Directive data-damage rule.
22. **Ch14.** Sitkoff & Schanzenbach are misused. "38 resolved tournament questions" should be 38 sub-questions across 32 questions. Fix the incentive flaw in Proposal 14.6. Re-verify the IEA scenario figures against the report PDF (the reviewer could not open it).
23. **Whole book.** Run the labelling pass (§1.3), build the fact sheet (§1.6) and cut the number dumps (§1.9).

---

## Part 3: Reference-check summary

| Chapter | Keys cited | Missing from bib | DOI and arXiv metadata | Claims checked against source | Problem citations* | Couldn't access |
|---|---|---|---|---|---|---|
| 1 | 76 | 0 | 49 / 49 | ~30 claims verified directly, all arithmetic | 11 (4 major) | 9 items |
| 2 | 66 | 0 | 36 / 36 | ~25 verified directly, plus all worked arithmetic and Tables 2.1–2.3 | 9 (3 major) | 4 items |
| 3 | 57 | 0 | 36 / 36 | ~10, plus all computations reproduced | 11 | ~6 |
| 4 | 58 | 0 | 26 / 26 | ~10 | 13 | ~5 |
| 5 | 75 | 0 | 57 confirmed | ~40 | 11 | 18 |
| 6 | 74 | 0 | 69 confirmed | ~50 | 13 | 5 |
| 7 | 97 | 0 | 28 / 28 | ~36 | 9 | ~55 (BIS rules, filings, licences) |
| 8 | 78 | 0 | 33 / 33 | ~45 | 13 | ~33 |
| 9 | 87 | 0 | all 87 verified | 52 | 11 | ~16 |
| 10 | 103 | 0 | all 103 verified | 58 | 10 | ~15 |
| 11 | 74 | 0 | 34 / 34 | 14 primary pages fetched, plus both International AI Safety Reports | 9 | 4 |
| 12 | 106 | 0 | 68 / 68 | 11 primary pages fetched | 7, plus bib errors | ~8 keys |
| 13 | 102 | 0 | (mostly legal, non-DOI) | 46 (14 fetched, ~32 from knowledge) | 13 | ~40 |
| 14 | 107 | 0 | (mixed; no errors found) | 66 (27 fetched, ~39 from knowledge) | 14 | ~20 |

\* "Problem citations" covers wrong numbers, misattributions, unsupported claims, omitted key results, labelling breaches and outdated claims. **No fabricated or mismatched references were found anywhere in the book.**

Whole-bibliography mechanical check:
- 1,023 unique entries; 0 missing keys; 0 conflicting duplicates across chapters; 19 uncited entries.
- 344 DOIs resolved. The only mismatches are cosmetic (subtitles dropped by Crossref, accents) plus the three year differences listed in §1.11.
- 672 non-DOI URLs fetched. No genuinely dead links were found. The failures were bot blocks (403s from openai.com, sec.gov and others), timeouts on stlouisfed.org, and ftc.gov, which returns 404 to every request from this environment, including its own index page.
