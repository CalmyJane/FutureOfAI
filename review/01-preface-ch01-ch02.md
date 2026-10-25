# Referee report: Preface, Chapter 1 and Chapter 2

*Understanding AI: Technology, Trends and the Decade Ahead* (Jan Göbel, October 2026). Reviewed 25 October 2026.

**Scope:** `chapters/ch00-preface.md`, `chapters/ch01.md` (287 lines), `chapters/ch02.md` (337 lines), `bib/ch01.bib`, `bib/ch02.bib`, figure specs `fig-01-0*` and `fig-02-0*`, and the SVGs (text labels extracted from the matplotlib comments).

**Method:**
- I read every line of all three files.
- I checked every DOI: Crossref for 53 DOIs, the arXiv API for 12 arXiv DOIs, and doi.org for 3 AI Magazine DOIs.
- I opened these primary sources: Shannon (1950), LeCun et al. (1998), Mitchell (2021), Buchanan & Shortliffe (1984, chapters 10–11), the Commission guidelines C(2025) 5053, the OECD memorandum, Seide et al. (2011), Zech et al. (2018), Goodfellow et al. (2015), Nakkiran et al. (2019), the Kimi K2 report, the DeepSeek-V4 abstract, the NVIDIA Q2 FY27 release, the St. Louis Fed post of 1 September 2026, the Microsoft diffusion post of 7 May 2026, TechCrunch, The Decoder, ClockBench and IBM's Deep Blue page.
- I recomputed every worked number with a script.

**How findings are labelled:**
- **Verified wrong** means I read the source and it contradicts or fails to support the text.
- **Couldn't verify** means I could not reach the source, or did not re-open it myself.
- The author's evidence logs were used as leads only.

---

## 0. Preface (ch00-preface.md)

### (A) Factual / reference

- **P-A1 (minor; verified OK).** At line 5 the preface says there are "more than a thousand references". I counted 1,014 distinct keys that are both cited in the chapters and present in the bib files (1,023 bib entries, some of them orphans). The claim is true, but only just. If orphan entries are pruned, or chapters are cut, it can drop below 1,000. Either keep the count under review or say "about a thousand".
- **P-A2 (major; the promise is not kept).** Line 28 says preprints and working papers "are labelled as such where they are first mentioned in a chapter". Chapters 1 and 2 break this rule repeatedly; the cases are listed under 1-A6 and 2-A6. Line 30 says company claims are introduced with "according to the company", and this is also applied unevenly. The most visible gaps:
  - GPT-2's "state of the art" results (an OpenAI report, not peer-reviewed);
  - Kimi K2's "Muon outperformed AdamW";
  - Microsoft's telemetry rankings.
- **P-A3 (minor).** Line 38 says "Every number is given with the year it refers to". Some numbers have no year:
  - ch01:152, Cyc's "some 30 million rules" (no year; the source is from 2024);
  - ch01:110, MYCIN's "about 500 rules";
  - ch02:242, the H100 specification (product page, no date).

  Either soften the promise ("Time-sensitive numbers are dated") or add the years.

### (B) Conceptual

- **P-B1 (major).** The labelling scheme on lines 25–32 has no category for several source types that Chapters 1–2 lean on heavily:
  - news reports (TechCrunch, The Decoder, Science News);
  - magazine columns and opinion pieces (Haigh in *CACM*, Hendler's IEEE editorial, Halevy et al., Sutton's blog essay);
  - company technical reports posted on arXiv (Llama, Llama 3, DeepSeek-V3/V4, Kimi K2);
  - company product pages and telemetry (NVIDIA, Microsoft);
  - community leaderboards (ClockBench, OSWorld-Verified);
  - encyclopedias (the Stanford Encyclopedia of Philosophy).

  The chapters improvise labels for these ("reported by the press", "in a preprint essay", "Its developers report"), so the reader cannot apply the preface's rules. Suggested fix: add two bullets.
  - "**News reports and commentary** (journalism, magazine columns, essays) are identified as such."
  - "**Company technical reports**, even when posted on arXiv, are treated as company claims for performance results, and as reliable descriptions of the company's own methods."
- **P-B2 (major).** Line 5 promises that sources are not cited inside sentences but listed by number at the foot of each page. The chapters, however, depend on pinpoint citations: "[@europeancommission2025guidelines, paras 42, 46, 48–50]", "[@buchanan1984rule, pp. 698–699, 701–702]", "[@goodfellow2016deep, sec. 6.5.1]". With page-foot numbers only, those pinpoints are lost, or they reappear as clutter in the footer.
  - Fix: decide whether pinpoints are printed (for example "12, paras 42–48") and say so in the preface.

### (C) Writing

- **P-C1.** The opening clichés weaken a book that sells itself on rigour: "Public discussion of AI swings between promise and alarm"; "for readers who want the substance rather than the headlines". Open with the method instead. Suggested opening: "This book reports what is known about artificial intelligence in October 2026, how it is known, and how well."
- **P-C2 (minor; inconsistency).** Parts I–III put the comma inside the bold ("**Part I, How AI Works (Chapters 1–4),**"). Part IV has no comma: "**Part IV, Risk, Safety and Governance (Chapters 11–13)** asks". Make them consistent.
- **P-C3.** The preface has no author statement:
  - who the author is and what relevant expertise or conflicts of interest they have;
  - whether AI tools were used in research, drafting or fact-checking.

  For a book that asks readers to "judge methods", disclosing AI assistance is close to obligatory in 2026. One sentence would do.

### (D) Structure

- **P-D1.** There is no "how to read this book" guidance, for example that Chapter 2's *Going deeper* boxes and equations can be skipped without losing the thread. Chapter 2 is much more mathematical than the line "No programming is assumed" suggests.
- **P-D2.** The preface's description of Chapter 2, "from a single artificial neuron to deep networks, with worked examples of backpropagation and convolution", is delivered. The description of Chapter 1, "the history of the field from the 1950s and the competing definitions", is delivered for 1950–2017, but the 2018–2026 history is thin (see 1-D1).

---

## Chapter 1: What We Mean by "AI"

**What works.** The chapter uses primary sources unusually well: the Dartmouth proposal, the MYCIN book, the Commission guidelines, the OECD memorandum and 15 U.S.C. 9401. The opening built on the Dartmouth funding request is vivid. The point that the legal definitions put a 1970s expert system inside "AI" and possibly leave a minimax chess program outside is a genuinely illuminating hook. The caution about ImageNet's "human-level" baseline (one annotator, 1,500 images) is exemplary. The closing synthesis (ll. 276–278) is good. Nearly all numbers I checked are correct.

### (A) Factual / reference errors

**1-A1. MYCIN's certainty-factor arithmetic describes a scheme MYCIN abandoned. Major; verified incomplete and misleading.**
- *Where:* ch01:112 and Table 1.2 (ll. 114–120).
- *The text says:* "MYCIN kept a measure of belief (MB) and a measure of disbelief (MD) for each hypothesis … the final certainty factor was CF = MB − MD." The table caption adds: "contrary evidence is kept separately and subtracted at the end."
- *What the source says:* The worked example on p. 260 comes from the 1975 model reprinted as chapter 11. Chapter 10 of the same book records that this behaviour "was counterintuitive and occasionally led MYCIN to reach incorrect inferences". In its example, eight or nine supporting rules give MB ≈ 0.999, and one disconfirming rule with CF 0.8 then cuts the CF to 0.199. The developers therefore "changed both the definition of a CF and the corresponding combining function" to CF = (MB − MD)/(1 − min(MB, MD)). MYCIN "simply stores the current cumulative CF value". "Beginning in approximately 1977 these changes were incorporated into all EMYCIN systems." (Buchanan & Shortliffe 1984, ch. 10, §10.2; https://people.dbmi.columbia.edu/shortliffe/Buchanan-Shortliffe-1984/Chapter-10.pdf)
- *Consequence:* Under the revised rule, step 3 of Table 1.2 gives 0.34/(1 − 0.1) = 0.378, not 0.34. The caption's "kept separately and subtracted at the end" is exactly what was dropped. This is also a better story: it shows the brittleness of ad hoc uncertainty schemes.
- *Fix:* Keep the table, but retitle it "MYCIN's original (1975) combining rule". Add one sentence: "The rule misbehaved when a single piece of strong contrary evidence wiped out many supporting rules, and from about 1977 MYCIN used a revised formula, CF = (MB − MD)/(1 − min(MB, MD)), which here gives 0.38 [@buchanan1984rule, ch. 10]."

**1-A2. The guidelines do not "write the AI effect into regulatory practice" for chess. Major; verified misreading.**
- *Where:* ch01:260 (also ch01:29, 45, 278).
- *The text says:* the guidelines "suggest that such a program may not count as an AI system at all, and treat the fact that a method 'has been used in consolidated manner for many years' as one indication that it falls outside [paras 42, 48]. In effect, the guidelines write the AI effect into regulatory practice."
- *What the source says:* The "consolidated manner" indicator sits in **para 42**, which covers *systems for improving mathematical optimisation* such as linear or logistic regression. The chess example is in **para 48** (classical heuristics). It is excluded for a different reason: such systems "apply predefined rules or algorithms to derive solutions … without requiring prior learning from data". Familiarity is not the reason. (C(2025) 5053 final; https://ai-act-service-desk.ec.europa.eu/sites/default/files/2025-08/commission_guidelines_on_the_definition_of_an_artificial_intelligence_system_established_by_regulation_eu_20241689_ai_actenglish_nf2skcqfrtjdfggjavcodopcwz4_112455.PDF)
- *Consequence:* The rhetorical payoff of §1.8 rests on combining two separate criteria.
- *Fix:* "The guidelines suggest that such a program may not count, because it applies predefined rules without learning from data (para 48). Elsewhere they treat long, 'consolidated' use of a statistical method such as regression as a sign that it falls outside (para 42). Together, these come close to writing the AI effect into regulatory practice."

**1-A3. The "behavioural" claim contradicts the chapter's own concept box. Major; conceptual error.**
- *Where:* ch01:15 says "Most modern definitions, including the legal ones in Section 1.2, follow the same behavioural approach."
- *The problem:* The OECD and EU definitions turn on "infers", which is a claim about *how* outputs are produced. The chapter's own concept box (l. 70) says so: "the system derives how to respond … instead of only executing rules a person wrote down." That is a criterion about mechanism. It is the opposite of Turing's purely behavioural test, and it is why a minimax chess program that plays superbly may fall outside.
- *Fix:* "Modern legal definitions keep Turing's focus on outputs but add a condition about mechanism: the system must *infer* how to produce them. As Section 1.2 shows, that condition, not behaviour, decides the hard cases."

**1-A4. The debate box uses the chapter's own numbers as evidence for Sutton when they do not test his claim. Major; logic.**
- *Where:* ch01:247 says "task-specific networks gave way to general pre-trained ones, with gains such as the 33% relative cut in speech errors in 2011 or BERT's 7.7-point gain on GLUE in 2018."
- *The problem:*
  - BERT's 7.7 points is measured against GPT-1 (72.8 → 80.5; Devlin et al. 2019), which was itself a general pre-trained model. It shows one general pre-trained model beating another.
  - Seide et al. replaced a learned Gaussian-mixture model with a learned DNN, which is learned-versus-learned, not hand-built knowledge versus computation.
- *Fix:* Drop both numbers, or replace them with genuine instances, for example GPT-2 or GPT-3 zero-shot or few-shot results against task-specific fine-tuned systems, or the HMM-versus-Hearsay contrast already in §1.6.

**1-A5. DeepSeek-R1 and "pure reinforcement learning". Minor; verified as quoted, but misleading.**
- *Where:* ch01:236 says DeepSeek reported that reasoning "can be incentivized through pure reinforcement learning", "without human-written examples of step-by-step reasoning".
- *The problem:* That holds for DeepSeek-R1-*Zero*. The released DeepSeek-R1 was trained with a multi-stage pipeline that included supervised "cold-start" data containing long chain-of-thought examples (Guo et al., *Nature* 645:633–638).
- *Fix:* "… reported that such abilities can emerge from reinforcement learning alone (in an experimental model, R1-Zero), although the released model also used a small set of written examples."

**1-A6. Labelling violations against the preface's rules. Minor to major in aggregate.**
- `mitchell2021why` is first cited at l. 97 (Simon and Minsky quotes) with no label. "In an essay posted as a preprint" only appears at l. 101. Move the label to l. 97.
- `kaplan2020scaling` (l. 230) is an arXiv preprint and is unlabelled here (Chapter 2 does label it).
- `radford2018improving` and `radford2019language` are OpenAI reports, not peer-reviewed, and are unlabelled (ll. 219, Table 1.4). "Set state-of-the-art results … 'in a zero-shot setting'" is a company performance claim.
- `bick2026what` is a Federal Reserve Bank blog post, not peer-reviewed; l. 234 presents it like a paper.
- `lavistaferres2026state` is Microsoft's own telemetry on a company blog. "From Microsoft's data" is close to the rule but not "according to the company".
- `clockbench2026clockbench` (l. 249) is a privately run leaderboard; the reader is not told who runs it or how.
- `osworld2026verified`: the label is fine, but the text should say "leaderboard".

**1-A7. Bick et al. attribution. Minor; verified.**
- *Where:* l. 234: "In their first working paper the same authors found that … adoption 'has outpaced both PCs and the internet' [@bick2026rapid]."
- *What the source says:* The cited item is the peer-reviewed *Management Science* article, 72(10):8440–8456 (2026), confirmed via Crossref (DOI 10.1287/mnsc.2025.02523). It has three authors, without Schumacher, so they are not "the same authors" as `bick2026what`.
- *Fix:* "In a peer-reviewed article, Bick, Blandin and Deming found …"

**1-A8. Date of the EU guidelines. Minor; verified incomplete.**
- *Where:* l. 43: "the European Commission issued guidelines on the definition, dated 29 July 2025."
- *What the sources say:* The guidelines were first published on 6 February 2025 (approved draft, C(2025) 924) and formally adopted as C(2025) 5053 on 29 July 2025. Readers who know the widely reported February release will be confused.
- *Fix:* "… published in February 2025 and formally adopted on 29 July 2025."

**1-A9. Table 1.1 header. Minor; internal inconsistency.** The column reads "US statute (2021)", while the text calls it "the National Artificial Intelligence Initiative Act of 2020". The Act was enacted on 1 January 2021 within the FY2021 NDAA. Use "US statute (2020 Act)" and explain once.

**1-A10. "First large practical success came in speech, not vision". Minor; contradicted within the book.**
- *Where:* l. 186.
- *The problem:* Chapter 2 opens with LeNet-5 reading bank cheques commercially in the late 1990s (LeCun et al. 1998: "in commercial use in the NCR Corporation line of check recognition systems").
- *Fix:* "Deep learning's first large success of the 2010s came in speech."

**1-A11. Transformer parallelism. Minor; technical imprecision.** l. 204 says a transformer "processes all the words of a passage at once rather than one after another". This is true in training and when reading a prompt. Generation is still one token at a time (Chapter 3 says so). Add "during training".

**1-A12. Shannon's "over 10^90 years". Minor; couldn't verify the original typesetting.**
- The widely circulated transcription (https://vision.unipv.it/IA1/ProgrammingaComputerforPlayingChess.pdf) reads "one variation per micro-second … over 10^90 years", which matches the text.
- The arithmetic, however, gives 10^120 µs ≈ 3 × 10^106 years. Some reprints say "micro-microsecond", which gives ≈ 3 × 10^100 years.
- "Over 10^90" is literally true, but it understates the figure by more than ten orders of magnitude. A careful reader who does the sum will be puzzled.
- *Fix:* Add "(a deliberately conservative figure)", or check the *Phil. Mag.* original.

**1-A13. Simon and Minsky quotes. Minor; verified against Mitchell, not against the primaries.**
- Mitchell (arXiv v2, l. 55–58) has "In 1960 Herbert Simon declared …" and "Within a generation...the problems of creating 'artificial intelligence' …". The book matches Mitchell.
- The Simon line is usually sourced to *The Shape of Automation for Men and Management* (1965).
- Minsky's 1967 original is usually quoted as "the problem". I could not access the primaries.
- Either cite the primaries, or say "as quoted by Mitchell".

**1-A14. Deep Blue. Minor; verified incomplete.** IBM's page calls the 1997 match "the rematch". Kasparov had won the 1996 match. Omitting this makes 1997 look like a single, inevitable event. Add half a sentence.

**1-A15. Seide et al. baseline. Minor; verified.** The 27.4% baseline is the maximum-likelihood-trained GMM on the same 309 h. The paper's table also lists a discriminatively trained (BMMI) GMM baseline (https://www.isca-archive.org/interspeech_2011/seide11_interspeech.pdf), against which the relative gain is smaller. The system also relied on DBN pre-training, which the chapter never mentions (see 2-D2). Say "against a standard maximum-likelihood baseline".

**1-A16. OSWorld numbers lack the human baseline. Minor.**
- l. 238 gives 12% → 66.3% → "about 86%" across two benchmark versions with no human reference.
- The OSWorld paper reports humans at 72.36%, so the 2026 figures exceed the original human baseline. That is the most informative fact, and it is missing.
- Add the baseline, and note that OSWorld-Verified is a corrected task set, so the numbers are not directly comparable.

**1-A17. Cross-chapter inconsistency. Minor.** GPT-3 training compute is given as 3.14 × 10^23 (ch01 Table 1.4) and as 3.2 × 10^23 (ch04 Table, l. 90). Harmonise.

**1-A18. Medical expert system "qualifies". Minor; overstated.** l. 29: "a rule-based medical adviser of the 1970s qualifies as an AI system". Para 39 gives early medical expert systems as an *example of the included technique category*. Para 62 says "No automatic determination" is possible. Use "would normally qualify".

**1-A19. Broussard. Minor.** l. 270 introduces "Scholars of technology" and then describes Broussard as "the journalist and software developer". She is a professor of data journalism at NYU. Use "the data-journalism professor and former software developer".

**1-A20. Secondary sources where primaries exist. Minor.**
- Lee Sedol 4–1 is cited to *Science News*.
- The Nate fraud case is cited to TechCrunch; the SDNY/DOJ release is the primary source (the log says it could not be fetched; try again or cite the indictment docket).
- The ChatGPT 900M and 1.2B figures are company figures reported by the press, and the text says so.

**Bib entries, Chapter 1.**
- `mccarthy2006proposal`: pages = {12}. The AI Magazine reprint runs pp. 12–14 (from memory; the DOI is not in Crossref, and doi.org resolves to AAAI OJS). Couldn't verify.
- `sajadieh2026ai`: the bib title "The AI Index 2026 Annual Report" differs from the arXiv record "Artificial Intelligence Index Report 2026" (arXiv:2606.15708, v1 14 Apr 2026). Align it. The odd 2606 ID for an April posting is genuine in the arXiv API.
- No fabricated or mismatched references were found. All 39 Crossref-registered DOIs in ch01.bib match author, year, title, venue, volume and pages.

### (B) Technical / conceptual problems

1. **AGI is used but never defined (major).** l. 249 quotes Marcus on reaching "artificial general intelligence". A chapter titled "What We Mean by 'AI'" has no section on narrow versus general AI, AGI, or "frontier AI", even though Legg and Hutter's breadth point (l. 25) sets it up perfectly and Chapters 11–14 surely depend on the term. Add a short subsection after "Researchers' definitions". Cover:
   - the AGI definitions in circulation (Legg–Hutter style breadth, "economically valuable work", and the company definitions);
   - why the term is contested;
   - that no legal text defines it, although the EU AI Act's "general-purpose AI model" and "systemic risk" come closest.
2. **The HMM paragraph (l. 160)** names Harpy among systems built on "joint global optimization". This follows Huang et al. However, Harpy (1976) was a compiled network with beam search, not an HMM system. Either keep the quote with "in Huang and colleagues' account" or drop Harpy.
3. **Generative AI (l. 83)** is defined by its output alone. The chapter gives no history of the generative techniques (GANs 2014, diffusion 2020, text-to-image 2022), which leaves "Generative AI" an empty box in Figure 1.1.
4. **Scaling laws (l. 230)** "describe how a language model's error falls". Use "loss (prediction error on held-out text)". "Error" will be read as task error rate.
5. **"Self-supervision … hiding a word in a sentence and asking the model to predict it" (l. 85)** describes BERT-style masking. GPT-style next-token prediction is the more relevant example for the rest of the book; give both.

### (C) Writing and explanation

- **Number-dumping in the opening (l. 5).** Readers meet 30 Nov 2022, 5 Dec, 1 million, July 2025, 700 million, 10%, February 2026, 900 million, September 2026 and 1.2 billion, plus two provenance caveats, in four sentences on page 1. Keep one contrast, for example "a 1955 proposal for ten men and $13,500; in 2026, a product OpenAI says reaches more than 1.2 billion people a week". Move the rest to §1.7 or Chapter 8.
- **The adoption paragraph (l. 234)** is the worst offender: 62%, 45%, 39%, 24th, 28.3%, 21st and 31.3% from four sources and two methods. In a history chapter it breaks the narrative. Keep one figure from each method and send the rest to Chapter 8.
- **Chronology slip (l. 238):** "During 2025 and 2026 came agents built around language models. In November 2024 Anthropic released …" Use "From late 2024 …".
- **Trivia that interrupts the argument (l. 21):** "(the itemised costs add up to $13,000, although the typed total reads $13,500)". Cut it or move it to a note.
- **§1.2 reads like a legal memo.** Two block or near-verbatim quotations of the same definition, a seven-element breakdown, a four-bullet exclusion list with paragraph pinpoints, a table, and then a concept box that restates the definition a fourth time (l. 70). Cut the concept box or merge its spam-filter and tax-formula examples into the text, which is the box's only new content. Trim the bullets to two examples.
- **Paragraphs that list sources without a through-line.** l. 101 (Lighthill → Mitchell → Haigh → Hendler) and l. 270 (Broussard, Crawford, Suchman in one sentence each) list views without weighing them. For l. 270, either engage one critic properly, for example Suchman's argument and what it implies for the definitions in §1.2, or compress to one sentence with a forward reference.
- **Debate box ending (l. 249).** The ClockBench update reads like a late patch. A rise from about 50% to 83.3% in seven months arguably favours Sutton's side, yet it is presented as Marcus's evidence ("still below the average human"). Either say so ("the gap closed fast, which is Sutton's point; it has not closed, which is Marcus's") or drop the update.
- **Jargon before definition.**
  - "Gaussian-mixture component of a standard HMM recogniser" (l. 186);
  - "GLUE" (Table 1.4, l. 247), never defined;
  - "downstream tasks" (l. 85);
  - "deep convolutional neural network" (l. 188) needs a forward reference to §2.6;
  - "reinforcement learning" (l. 202) is glossed adequately.
- **Weak heading:** "The breakthroughs, with numbers" (l. 184). Try "Deep learning's breakthroughs, 2011–2017".
- **Style consistency (en-GB):** "70 per cent" (l. 13) and "one per cent" (l. 166) sit beside "%" everywhere else; Chapter 3 uses "per cent". Pick one house style. "Natural-language researchers" (l. 15) versus "NLP" elsewhere. US spellings appear only inside quotations, which is correct.
- **AI-prose tells** are few. Watch the stacked "In effect, …", "The lesson many researchers drew was …" and "Both readings fit the record so far." The chapter is mostly clean. Its main weakness is density, not tone.

### (D) Structure and coverage

- **1-D1 (major). The balance is inverted.**
  - MYCIN gets a rule quotation, a mechanism explanation, a table and a case study, about 2.5 pages.
  - 2017–2026, the period readers care most about, gets about six paragraphs.
  - Missing milestones a reader would expect in a 2026 history:
    - instruction tuning and RLHF (InstructGPT 2022, the key ingredient of ChatGPT, mentioned only as "further trained", l. 234);
    - GPT-4 (2023) and the multimodal shift;
    - open-weight models (Llama 2023, DeepSeek);
    - AlphaFold and the 2024 Nobel prizes (Hinton/Hopfield; Hassabis/Jumper);
    - the 2018 Turing Award;
    - diffusion and image generation.

  Cut MYCIN by about a third (keep the evaluation case study, which is excellent) and add a compact 2018–2026 subsection.
- **1-D2. The connectionist thread has gaps.**
  - Hopfield (1982) and the PDP volumes (1986) are missing.
  - LSTM (1997) is missing.
  - The 2006 deep-belief-net pre-training that restarted deep learning is missing; Chapter 2 quotes Glorot's "before 2006" without explaining it either.
  - LeNet appears only in Chapter 2.
  - One sentence on each would make the 2011–2012 "breakthroughs" less miraculous.
- **1-D3.** There is no narrow-versus-general section (see B1).
- **1-D4. The perspective is mostly US/UK.** Japan appears only as a prompt for US spending, and the Soviet and European traditions are absent. This is acceptable for a short history, but say so.
- **Ending.** The closing paragraph (l. 278) is a good synthesis. The chapter has no bridge to Chapter 2, which follows with the mechanism; one sentence would help.

### (E) Figures and tables

- **Fig 1.2:** All values match Russakovsky et al. and the logs: 28.2, 25.8, 16.4 (15.3 with extra data), 11.7, 6.7, 3.57 and human 5.1. The axis starts at 0 and the caption caveat is good. No issues.
- **Fig 1.3:**
  1. It stops at "900M weekly users, company figure (Feb 2026)", while the text (l. 5) gives 1.2 billion in September 2026. Update it, or explain the cut-off.
  2. The era band "Deep learning 2011→" contradicts Chapter 2's LeNet (1998).
  3. The caption lists 25 citation keys, an unreadable wall in print. Use "Sources: see text, Sections 1.1–1.7".
  4. 2017–2026 is crowded with policy events, while research milestones after 2018 are only GPT-3, o1 and R1. GPT-4 (2023) and RLHF/InstructGPT (2022) are missing.
- **Fig 1.1:** The labels are consistent with the caption. Check that the "Generative AI" region is not drawn wholly inside "Foundation models". The text (l. 89) says not every generative model is a foundation model or a deep network, so if the SVG nests it, the figure contradicts the text. (From the extracted labels I could not confirm the geometry.)
- **Table 1.1:** See 1-A9 on the year. The row label "Core verb" contains phrases, not verbs; use "Core function".
- **Table 1.2:** The arithmetic is correct (0.3 + 0.2 × 0.7 = 0.44; 0.44 − 0.10 = 0.34), but the scheme is outdated (1-A1).
- **Table 1.3:** The 1990 row's "Earlier approach: rule-based systems (not compared)" is an empty comparison. Either compare (for example Systran) or drop the row. The 2016 row is not a measure.
- **Table 1.4:** All cells are consistent with the sources (117M via the GPT-2 paper, footnoted; 340M; 1.5B; 175B; 300B tokens; 3.14 × 10^23). The ≈1,500× growth is correct (175,000/117 = 1,496).

### (F) Reference-check tally, Chapter 1

| Item | Count |
|---|---|
| Citation keys used | 76 (all present in ch01.bib; no orphans) |
| DOIs in ch01.bib | 39 Crossref DOIs match; 7 arXiv DOIs match via the arXiv API; 3 AI Magazine DOIs resolve |
| References judged real and essentially correct | 76/76 (no fabricated references) |
| Bib metadata problems | 2 minor (`mccarthy2006proposal` pages, unconfirmed; `sajadieh2026ai` title) |
| Claims verified wrong or misleading | 1-A1, 1-A2, 1-A3, 1-A4 (major); 1-A5, 1-A7, 1-A8, 1-A10, 1-A11, 1-A14, 1-A18 (minor) |
| Claims verified OK myself | Dartmouth quotes; Mitchell quotes; Shannon numbers (against the transcription); EU guidelines paras 7, 39, 41, 42, 48–50, 62, 63 and C(2025) 5053 date; OECD pp. 4/6/7/9; Seide 27.4 → 18.5, 309 h, 7 × 2048; IBM Deep Blue quotes and numbers; Bick 45% → 62% (ages 18–64); Microsoft 24th → 21st, 31.3% (ages 15–64); OpenAI 900M (TechCrunch) and 1.2B (The Decoder); ClockBench 83.3% vs 90.7%; Kwa NeurIPS 2025; DeepSeek-R1 *Nature*; all arithmetic |
| Couldn't verify myself (relied on the log or could not access) | Hendler 2008 quotes (closed access); Haigh 2024 specifics (480 rules, $40M, 59 staff, 2,000 person-years, 30M rules); Bachant & McDermott; Buchanan & Shortliffe pp. 673–702; Solomonoff/SEP attendance; AI Index figures (28.3%, 66.3%, 50.6%); OSWorld-Verified 85.96%; Simon/Minsky primaries; Shannon original typesetting |

---

## Chapter 2: How Neural Networks Learn

**What works.** This is the strongest of the three files. I recomputed every worked example with a script, and all of them are correct:
- the neuron total 0.2;
- the matrix layer (−3.4, 1.8);
- softmax 0.659/0.242/0.0986 and losses 0.417/2.317;
- the one-weight descent (0.36 → 0.0144; the 1 − 8η factor; divergence above 0.25);
- the full nine-parameter backprop box (p = 0.6225, L = 0.4741; updated L = 0.3021);
- the momentum sum 6.51;
- Adam's first step;
- 0.25^10 ≈ 9.5 × 10^−7 and 0.0256^10 ≈ 1.2 × 10^−16;
- He's σ = 0.0625;
- 3.4 × 10^10 FLOPs and reuse ≈ 2,731;
- H100 590/295 ops per byte;
- 4.8 × 10^11 weights;
- ε·m·n = 10.5.

The backprop *Going deeper* box, with its finite-difference check, is a model of how to teach the mechanism. Caveats are handled carefully, for example the ReLU after the residual addition and the "Schematic" label on double descent. The closing paragraph ties failures back to the loss function, and it is excellent.

### (A) Factual / reference errors

**2-A1. Adversarial training: the wrong number is offered as evidence of robustness. Major; verified wrong.**
- *Where:* ch02:309: "Training on adversarial examples improves robustness: in the 2015 study it cut a digit-recognition network's ordinary test error from 0.94% to 0.84%."
- *What the source says:* 0.94% → 0.84% is the error on clean test data, which shows adversarial training acting as a *regulariser*. The robustness result in the same paper is that the error rate on adversarial examples "fell to 17.9%" from 89.4% (Goodfellow, Shlens & Szegedy 2015, §6; https://arxiv.org/abs/1412.6572).
- *Fix:* "Training on adversarial examples helps: in the 2015 study it cut a digit network's error on adversarial examples from 89.4% to 17.9%, and slightly improved its ordinary test error (0.94% to 0.84%). Later work showed that such defences are often broken by stronger attacks."

**2-A2. The pneumonia case overstates what Zech et al. showed. Major; verified overstatement.**
- *Where:* ch02:300.
- *The text says:* "The networks identified which system an NIH or Mount Sinai X-ray came from with 99.95% and 99.98% accuracy … The training loss could be reduced by learning where an image came from, and gradient descent duly learned it."
- *What the source says:* The 99.95% and 99.98% figures come from CNNs trained *specifically to predict the hospital system* ("CNNs were able to directly detect hospital system"). The paper did not show that the pneumonia model itself used site information. It says such information "may confound predictions" and lists as its "primary limitation" that "we cannot fully assess what other factors might be contributing". The strongest evidence is an experiment the book omits. When both training sites had equal prevalence, external performance held up (P = 0.88). When a 10-fold prevalence difference was introduced, internal performance rose but did not transfer to Indiana University. (https://doi.org/10.1371/journal.pmed.1002683; abstract.)
- *Fix:*
  - Replace "The networks identified" with "Separate networks trained for the purpose identified …".
  - Replace the last sentence with: "When the authors made the two training hospitals differ tenfold in pneumonia rates, the model scored better on held-out images from those hospitals but not on the third. That pattern is what one expects if the model learns where an image came from."
  - Also note that the labels were derived from radiology reports by text mining ("a simulated pneumonia screening task").

**2-A3. "Classical learning theory predicts … will memorise its data and generalise badly." Major-ish; conceptual misstatement.**
- *Where:* l. 274.
- *The problem:* Classical capacity-based theory (VC dimension, Rademacher complexity) gives *upper bounds* on the generalisation gap. For such networks the bounds become vacuous; the theory does not predict failure. Zhang et al.'s point is exactly that these bounds "cannot explain" the observed generalisation. Margin-based and norm-based theories predate 2017 and do not predict failure either.
- *Fix:* "Classical learning theory bounds the gap between training and test error by the model's capacity. For networks that can fit random labels, those bounds say nothing useful, so the theory cannot explain why such networks generalise."

**2-A4. LeNet cheque volume. Minor; source internally inconsistent.**
- *Where:* l. 3: "reading … millions of bank cheques a month".
- *What the source says:* LeCun et al. (1998) support this in the introduction ("reading millions of checks per month in several banks across the United States"). The abstract of the same paper says "reads several million checks per day" (https://gwern.net/doc/ai/nn/cnn/1998-lecun.pdf).
- *Fix:* Keep the conservative figure, but attribute it ("according to its developers"). Also say "a system built around LeNet-5". The deployed reader was a graph transformer network from NCR that used LeNet-5 as its character recogniser.

**2-A5. "Networks with more than a few layers nonetheless remained hard to train for another two decades." Minor; overstated, with a gap.**
- *Where:* l. 151.
- *The problem:* LeNet-5 (seven layers, 1998), which the chapter itself celebrates, trained fine. The difficulty applied mainly to deep fully connected sigmoid networks. The chapter quotes Glorot and Bengio's "before 2006" but never says what happened in 2006: Hinton, Osindero and Teh's layer-wise pre-training of deep belief nets, which Seide et al. (2011) still used.
- *Fix:* "Deep fully connected networks proved hard to train until the mid-2000s, when layer-wise pre-training (Hinton and colleagues, 2006) and then better activations and initialisations made them practical; convolutional networks such as LeNet, with few parameters per layer, were the exception."

**2-A6. Preprint and company-report labelling (minor individually, major in aggregate).** These are unlabelled at first mention, contrary to the preface:
- `shazeer2020glu` (l. 37), arXiv only;
- `hendrycks2016gaussian` (l. 37), arXiv only;
- `hu2024minicpm` (l. 157), bib says arXiv preprint (couldn't confirm a COLM 2024 version);
- `touvron2023llama`, `grattafiori2024llama`, `deepseekai2024deepseekv3`, `kimiteam2025kimi` and `deepseekai2026deepseekv4` (ll. 157, 180, 188, 244), company technical reports;
- `radford2019language` (l. 194), company report.

The Kimi K2 claim that Muon "outperformed AdamW at equal compute" is a company performance claim and needs "according to the company". DeepSeek-V4 is described in its own abstract as "a preview version", so say so. Note that `kaplan2020scaling`, `goyal2017accurate` and `ba2016layer` *are* labelled correctly.

**2-A7. Kimi K2 "a model of about a trillion parameters". Minor; verified as stated, but misleading without the MoE caveat.**
- *What the source says:* Kimi K2 is a mixture-of-experts model with 1.04 T total and 32 B activated parameters (arXiv:2507.20534, l. 358 of the PDF text). The schedule detail is verified: 2e-4 constant for 10 T tokens after a 500-step warm-up, then cosine to 2e-5 over 5.5 T.
- *Why it matters:* §2.4's 6N rule applies to *active* parameters. A reader will multiply by 10^12 and overestimate compute by about 30 times. DeepSeek-V4 (1.6 T total, 49 B active; verified from the abstract) has the same issue.
- *Fix:* Add a short "total versus active parameters" sentence where Kimi K2 is introduced, or in §2.2's parameter-count paragraph.

**2-A8. XOR and *Perceptrons*. Minor; historically imprecise.**
- l. 41 says Minsky and Papert's 1969 book "proved this and related limits".
- That a single linear threshold unit cannot compute XOR was elementary and known earlier. The book's substantive theorems concern parity and connectedness for perceptrons of limited *order* (limited receptive fields).
- The causal story ("contributed to a backlash") is itself contested among historians (for example Olazaran 1996).
- *Fix:* "XOR is the simplest example of a limit that Minsky and Papert's 1969 book *Perceptrons* analysed in depth for single-layer perceptrons."

**2-A9. Cybenko. Minor; imprecise.** l. 74 says "can approximate any continuous function". The theorem covers continuous functions on a bounded (compact) region of input space. Add "over a bounded range of inputs". Hornik et al. (1989) is the usual co-citation.

**2-A10. "In 2016 Goodfellow and colleagues found that …" Minor.** l. 180: the quoted line ("seems to depend largely on the user's familiarity with the algorithm") is an aside in a textbook, not a finding. Use "remarked".

**2-A11. Vera Rubin. Minor; verified.**
- l. 244: "which Nvidia said in August 2026 was in full production".
- The 26 August 2026 results release does say "Vera Rubin, now in full production". The same release also says it is "ramping into full production", and NVIDIA was already using the phrase in January 2026; the cited Aubrey blog is dated 5 January 2026.
- Product-status news will age badly in a mechanism chapter. Move it to Chapter 7, and keep only "newer chips push to 4-bit arithmetic".

**2-A12. Beniaguev et al. Minor; missing nuance.** "Needed a network of five to eight layers" (l. 317) holds for the model neuron *with NMDA receptors*. Without NMDA-dependent dendritic nonlinearities, a much shallower network sufficed. That contrast is the scientifically interesting point (dendrites do the extra computation). Add half a sentence.

**Bib entries, Chapter 2.**
- `micikevicius2017mixed`: the key says 2017 but year = 2018 (ICLR 2018). This is cosmetic, but the rendered citation will say 2018 while the key suggests 2017. That is fine if intended.
- `raina2009large` is in ch02.bib but not cited. Remove it, or cite it at l. 240: GPU training of deep networks in 2009 is a useful precursor to AlexNet.
- `hu2024minicpm`: couldn't verify whether a peer-reviewed version (COLM 2024) exists. If it does, update the entry and drop the preprint label.
- All 29 Crossref DOIs in ch02.bib match. The 6 arXiv DOIs and the DeepSeek-V4 arXiv ID (2606.19348, v1 26 April 2026) resolve with matching titles and authors. The 11 keys shared with ch01.bib are byte-identical in both files.

### (B) Technical / conceptual problems

1. **How did the 1958 perceptron learn without a slope? (Clarity gap.)** l. 21 says a threshold "has no slope, and gradient-based learning … needs a slope". A careful reader immediately asks how Rosenblatt's machine learned. Add one sentence: "Rosenblatt used an error-correction rule that works for a single layer of threshold units; it gives no way to adjust hidden layers, which is why gradients, and smooth activations, became necessary."
2. **"Convolution" is cross-correlation.** At l. 224 and in Fig. 2.5 the kernel is not flipped. This is standard ML usage, and Goodfellow et al. §9.1 note it. One clause prevents confusion for readers who know signal processing.
3. **Adam's "scale cancels" (l. 178)** holds exactly at step 1 and for consistent gradients. With noisy gradients, m̂/√v̂ is well below 1, which is why Adam's effective steps shrink in noisy directions. Add "when gradients are consistent".
4. **Muon (l. 180):** "passes each weight matrix's accumulated gradient through a matrix iteration (Newton–Schulz)" is accurate but tells a general reader nothing. Use: "it approximately orthogonalises each matrix update, so that every direction in the matrix is changed by a similar amount".
5. **The saddle-point claim (l. 110)** rests on a 2015 review that summarises results for idealised models. Present it as "evidence, mostly from theory on simplified models and from experiments, suggests …".
6. **Brain-scale comparison left hanging (l. 317).** The text says parameters correspond to synapses, not neurons, but never gives the synapse count (of order 10^14), which is the number the sentence sets up. Add it with a source.
7. **Missing learning paradigms.** The whole chapter is supervised learning. Chapter 1 has defined self-supervision, and Chapter 3 depends on reinforcement learning (RLHF, reasoning models). Two sentences in §2.3 on self-supervised and reinforcement learning, as variants of "define a loss and descend it", would connect the chapters.
8. **Recurrent networks are never introduced, but are referred to.** l. 188 says gradient clipping was "proposed … for recurrent networks". RNNs and LSTMs, the dominant sequence models from 1997 to 2017, are absent from both Chapter 1 and Chapter 2. Either add a short paragraph in §2.6 or drop the reference.

### (C) Writing and explanation

- **§2.5 becomes a catalogue.** "Making deep networks trainable" runs about 3,000 words and drops model names at a rate a general reader cannot absorb.
  - l. 157: Llama's tenth-of-peak decay, MiniCPM's WSD, Kimi K2's 10 trillion constant-rate tokens.
  - l. 180: Llama, Llama 3, DeepSeek-V3, Kimi K2, DeepSeek-V4.
  - l. 188: Llama and DeepSeek-V3 clip at 1.0.
  - l. 194: GPT-2, Llama, RMSNorm.

  Each fact is correct, but together they read as an evidence log. Keep the *ideas* (warm-up, decay, momentum, Adam, AdamW, initialisation, normalisation, residuals) in the main text. Move the "who uses what in 2024–26" material into one short *Going deeper* box: "What frontier training recipes looked like in 2025–26".
- **Jargon before definition:**
  - "linear projection" (l. 37);
  - "sub-layer" and "LayerNorm(x + Sublayer(x))" (l. 194), when transformer sub-layers are not introduced until Chapter 3;
  - "exploding attention values" (l. 180), when attention is not yet introduced;
  - "Inception image network" (l. 192);
  - "recurrent networks" (l. 188);
  - "mixture-of-experts" is needed but absent (2-A7).

  Add forward references ("(Chapter 3)") or plain glosses.
- **Terminology.** "Total" for the pre-activation is a reasonable teaching choice and is used consistently. Mention once that the literature calls it the "pre-activation" or "logit", so that readers can follow Chapter 3 and the sources.
- **Thin subsection:** "Forgetting and opacity" (l. 311) gives opacity one sentence. Either merge it into the closing paragraph, which already points to interpretability, or give it a concrete example.
- **§2.8 joins two topics** ("How networks fail, and the brain analogy"). The brain material is good, but it is a separate argument. Make it §2.9, or make it a box with the debate.
- **Fig 2.5 caption notation:** "(−1 × 0 × 3) + (0 × 0 × 3) + (+1 × 1 × 3) = 3" reads as triple products. Write "3 × (−1 × 0) + 3 × (0 × 0) + 3 × (+1 × 1) = 3", or "each column of three pixels contributes …".
- **Scale exemplar is dated.** l. 5 and l. 76 use GPT-3 (2020, 175 B) as *the* large network. In a book dated October 2026, add a current open model, for example DeepSeek-V4-Pro (1.6 T total, 49 B active, already in the bib). That also introduces the total-versus-active distinction.
- **Prose quality.** The chapter is generally clear and well paced in §§2.1–2.4. The opening anecdote and the closing paragraph are strong. Few AI-prose tells; "The fog image misleads." is effective.

### (D) Structure and coverage

- **2-D1.** It delivers the preface's promise of worked examples of backpropagation and convolution.
- **2-D2. Missing pieces a reader would expect:**
  - the 2006 pre-training revival (see 2-A5);
  - RNNs and LSTMs (B8);
  - mixture-of-experts and total-versus-active parameters (2-A7);
  - the learning paradigms (B7);
  - the role of training *data* (quality, deduplication, contamination), which matters for §2.7's generalisation discussion; one paragraph with a forward reference to Chapters 3–4 would suffice.
- **2-D3.** The debate box is balanced. Its last paragraph ("Settling the question needs …") is good practice and should be the model for Chapter 1's box.
- **2-D4. Possible redundancy with Chapter 1.** AlexNet (60 M parameters, 5–6 days, two GTX 580s) and ResNet (152 layers, 3.57%) appear in both chapters. Chapter 2 could simply refer back.

### (E) Figures and tables

- **Fig 2.1** (labels 0.5, −1, +0.2, total 0.2; inputs 1 and 1 give −0.3 → 0): correct.
- **Fig 2.2** (4 × 3 and 2 × 4 matrices, 12 + 8 weights + 6 biases = 26): correct.
- **Fig 2.3** (0.2 → 0.44 → 0.488 → 0.4976; η = 0.5 overshoots to 1.4 with loss 3.24; slope −2.4): all correct.
- **Fig 2.4** (top-1 errors 27.94/28.54 for plain networks, 27.88/25.03 for ResNets; 10-crop validation; axis starts at 24% and is clearly marked): consistent with He et al. 2016, Table 2.
- **Fig 2.5:**
  1. The 3 × 3 feature map is 0, 3, 3 in every row: *two* window positions straddle the boundary. The text's "0 where there is no edge, 3 where there is one" is fine, but say that the edge shows up in two adjacent columns. That is a nice teaching point about receptive fields.
  2. Panel (d) pools an unrelated 4 × 4 grid (1 3 0 2 / 4 2 1 0 / 0 1 5 2 / 2 0 3 1 → 4 2 / 2 5, which is correct). The caption, "shrinking a 4 × 4 map to 2 × 2", never says the grid is a new example, so readers will look for where the 4 × 4 map came from. Add "(a separate example)".
  3. The note "a fully connected layer from 25 pixels to 9 outputs would need 225 weights" is correct.
- **Fig 2.6:** Schematic and labelled as such. Fine.
- **Table 2.1:** All values correct (σ(0.2) = 0.550, slope 0.248; tanh(0.2) = 0.197, slope 0.961).
- **Table 2.2:** Correct; the weights follow Goodfellow et al. §6.1.
- **Table 2.3:** All nine gradients and the updated values reproduce to four decimal places.
- **Table 2.4:** Consistent with the three papers (batch 128/256/~25k + 25k tokens; LR schedules; weight decay 5e-4/1e-4/not reported; Adam β₂ = 0.98; dropout 0.5/none/0.1; label smoothing 0.1; LRN/BN/LN; init 0.01 Gaussian/He/not reported).
- **Table 2.5:** Consistent with Zhang et al. (2017), Table 1, as I remember it (89.05/85.75/9.78; 81.22/76.07/9.86; 99.90/99.82). I did not re-open the paper. Not verified this session.

### (F) Reference-check tally, Chapter 2

| Item | Count |
|---|---|
| Citation keys used | 66 (all present in ch02.bib); 1 orphan bib entry (`raina2009large`) |
| DOIs in ch02.bib | 29 Crossref DOIs match; 6 arXiv DOIs plus 1 arXiv ID (DeepSeek-V4) match via the arXiv API |
| References judged real and essentially correct | 66/66 (no fabricated references) |
| Bib metadata problems | 2 minor (`micikevicius2017mixed` key/year; `hu2024minicpm` venue unconfirmed) plus 1 orphan |
| Claims verified wrong or misleading | 2-A1, 2-A2, 2-A3 (major); 2-A5, 2-A7, 2-A8, 2-A9, 2-A10, 2-A12 (minor) |
| Claims verified OK myself | LeNet 345,308 connections / 60,000 parameters / 0.35% train / 0.95% test; Zech numbers (158,323; 34.2/1.2/1.0%; 0.861; 0.931/0.815; 99.95/99.98%); Goodfellow 57.7% panda → 99.3% gibbon, ε = 0.007; Nakkiran "(even quadrupling)"; Kimi K2 schedule and MuonClip; DeepSeek-V4 Muon; NVIDIA Rubin August 2026 release; all worked arithmetic and Tables 2.1–2.3 |
| Consistent with my knowledge, not re-fetched | AlexNet details (ReLU 6× faster on CIFAR-10; 2,048× augmentation; weight decay quote); ResNet numbers; Adam defaults; Glorot/He quotes; Srivastava MNIST 1.60/1.25/1.06%; Geirhos 95.9/22.1/63.9%; Recht 3–15 / 11–14 pp; BN "14 times fewer"; Santurkar quotes; H100 67/1,979 TFLOPS, 3.35 TB/s; Kaplan 6N and d_model > n_ctx/12; Zhang Table 1 |
| Couldn't verify | `hu2024minicpm` venue; McCulloch & Pitts p. 115 and Rosenblatt p. 387 pinpoints; NYT p. 25 (via Ananthaswamy) |

---

## Overall priorities (in order)

1. Fix the six substantive errors: 1-A1 (MYCIN certainty factors), 1-A2 (guidelines and the AI effect), 1-A3 ("behavioural" definitions), 1-A4 (debate-box evidence), 2-A1 (adversarial-training numbers) and 2-A2 (Zech overstatement). Also fix 2-A3 (classical theory).
2. Make the preface's evidence-labelling scheme complete (P-B1), then apply it consistently (1-A6, 2-A6).
3. Chapter 1: define AGI and narrow AI; rebalance towards 2018–2026; cut the number-dumps (l. 5, l. 234) and the duplicate definition box.
4. Chapter 2: move model-specific training trivia into one box; add total-versus-active parameters (MoE), the 2006 revival, RNNs, and a sentence on how the perceptron learned without gradients.
5. Figures: update Fig 1.3 (1.2B, LeNet era, caption wall); say that Fig 2.5(d) is a separate example.
