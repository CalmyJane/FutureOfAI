# Third review: Chapter 1 — What We Mean by "AI": Definitions and a Short History

## Verdict
Ready after the MUST fixes below. The chapter is carefully sourced. Almost every date, number and quotation I checked against the primary text is right, including the Dartmouth proposal, Shannon, Lighthill, MYCIN, the ImageNet and transformer results, Table 1.4, the OECD and EU definitions with their paragraph pinpoints, and all the 2026 items (DevDay 1.2B, GPT-6 Astra, Opus 5.5, Gemini 4 Argon/Carbon, OSWorld-Verified 85.96%). Three things are verifiably wrong and must be fixed: one direct quotation is not what the source says (the MCP announcement); the Figure 1.3 caption runs off the printed page and calls a numerically sorted list "in date order"; and the 1996 Deep Blue match result is misstated. The remaining items are currency updates (ClockBench, November model releases), primary-source substitutions that the preface's own labelling policy calls for, and small wording fixes. The preface overstates when the checking was done.

## MUST change before printing

### M1. MCP quotation is not Anthropic's wording
- Where: textbook/chapters/ch01.md:240
- Text now: "In November 2024 Anthropic released the Model Context Protocol, which it describes as "an open standard for connecting AI assistants to the systems where data lives" [@anthropic2024introducing]."
- Problem: VERIFIED WRONG (misquotation). The announcement says "a new standard for connecting AI assistants to the systems where data lives". The phrase "open standard" appears in a different sentence, about "AI systems" and "data sources". The book's quotation merges the two.
- Evidence: https://www.anthropic.com/news/model-context-protocol (Published Nov 25, 2024): "Today, we're open-sourcing the Model Context Protocol (MCP), a new standard for connecting AI assistants to the systems where data lives, including content repositories, business tools, and development environments." Later on the page: "It provides a universal, open standard for connecting AI systems with data sources".
- Change to: "In November 2024 Anthropic released the Model Context Protocol as open source, describing it as "a new standard for connecting AI assistants to the systems where data lives" [@anthropic2024introducing]."

### M2. Figure 1.3 caption is cut off in the printed book and the source list is not "in date order"
- Where: textbook/chapters/ch01.md:246 (caption), and the delivered PDF p. 36. The caption text comes from textbook/figures/specs/fig-01-03.md.
- Text now (PDF p. 36): "Sources: winter bands and eras [770]; milestones, in date order, [52, 79, 159, 162, 174, 175, 230, 307, 317, 373, 484, 519, 550, 579, 597, 637, 660, 682, 718, 722, 763, 838, 857, 861, 87" (the line runs past the right edge of the page and the remaining numbers are lost)
- Problem: VERIFIED WRONG in the print output. I rendered the page at 110 dpi: the bracketed list does not wrap and is truncated at "87". The build also sorts the numbers numerically, so "in date order" is false as printed. The same overflow affects the Figure 13.2 caption (PDF text line "[147, 259, 270, … 1102,"), which is outside this chapter.
- Evidence: textbook/delivery/understanding-ai_A5_interior.pdf, page 36 (pdftotext line length 121 characters, against about 100 for every other line; the rendered image shows the cut).
- Change to: in the caption, replace "milestones, in date order, @turing1950computing; …" with "milestones @turing1950computing; …" (drop "in date order,"). Then make the build wrap the bracketed number list in captions, for example by letting srcnotes.lua emit the numbers without a no-break group or by inserting break opportunities after the commas, and rebuild. If the build cannot be changed before print, shorten the caption to: "Sources: winter bands and eras @mitchell2021why; milestones as cited where each is discussed in Sections 1.1–1.7." Check Figure 13.2 at the same time.

### M3. The 1996 Kasparov–Deep Blue score is misstated
- Where: textbook/chapters/ch01.md:171
- Text now: "The world champion Garry Kasparov had beaten IBM's chess computer Deep Blue by four games to two in 1996"
- Problem: VERIFIED WRONG. Kasparov won the 1996 match 4–2 on points: three wins, two draws and one loss. He did not win four games.
- Evidence: https://www.ibm.com/history/deep-blue: "Deep Blue won the first game … But Kasparov recovered and won the match 4–2."
- Change to: "The world champion Garry Kasparov had beaten IBM's chess computer Deep Blue 4–2 in 1996, with three wins, two draws and one loss"

## SHOULD change (real but not blocking)

### S1. ClockBench figure is no longer the leading score
- Where: ch01.md:253. Text: "By October 2026 the leading model scored 83.3% on ClockBench … against 90.7% for the average human".
- Problem: OUTDATED. On 22 Nov 2026 the leaderboard shows Claude Fable 5.2 Max at 87.8% (released 9 Nov 2026), Gemini 4 Carbon High at 85.0% and Gemini 4 Argon High at 83.3%. The average human is still 90.7%. I could not establish whether Carbon's 85% was posted before 31 October, so "By October 2026" may already have been wrong. The debate's conclusion ("it has not closed") still holds.
- Evidence: https://clockbench.ai/ (read 22 Nov 2026): "Top Model Accuracy 87.8 % … 1 Claude Fable 5.2 Max 87.8% … 2 Gemini 4 Carbon High 85% … 3 Gemini 4 Argon High 83.3%"; SD Times, 9 Nov 2026, "Anthropic introduces Claude Fable 5.2, Mythos 5.2".
- Change to: "On 25 October 2026 the leading model scored 83.3% on ClockBench, a clock-reading leaderboard run by an independent developer, against 90.7% for the average human; by late November a newer model had reached 87.8% [@clockbench2026clockbench]." Update the bib urldate to 2026-11-22. Alternatively keep October-only wording as "On 25 October 2026 …" and drop the second clause.

### S2. Opening figure: cite OpenAI's own DevDay recap, not only the press
- Where: ch01.md:5
- Problem: The preface says that "where a primary document exists, the book cites it instead". OpenAI's recap is primary and confirms the figure; Engadget and The Decoder are secondary. The sentence itself is correct.
- Evidence: https://openai.com/index/devday-2026-recap/ (dated September 29, 2026): "…developers can directly launch new native experiences to our collective 1.2B weekly users."
- Change to: keep the sentence and cite "[@openai2026devday; @bonifacic2026openai]". New bib entry: @misc{openai2026devday, author={{OpenAI}}, title={{DevDay} 2026 Recap}, year={2026}, howpublished={Company blog, 29 September 2026 (company source)}, url={https://openai.com/index/devday-2026-recap/}, urldate={2026-11-22}}. The same change could apply to the Figure 1.3 caption key.

### S3. Nate case: cite the DOJ release
- Where: ch01.md:272 ("according to TechCrunch … [@rollet2025fintech]")
- Problem: A primary document exists (preface policy), and for a criminal allegation against a named person the indictment announcement is the better source. As of 22 Nov 2026 I found no reported plea, trial or verdict, so "charged … alleging" remains accurate.
- Evidence: US Attorney SDNY, "Tech CEO Charged In Artificial Intelligence Investment Fraud Scheme", https://www.justice.gov/usao-sdny/pr/tech-ceo-charged-artificial-intelligence-investment-fraud-scheme (April 2025), together with the SEC parallel action (Litigation Release LR-26282).
- Change to: "…and in April 2025 federal prosecutors in New York charged the founder of the shopping app Nate with securities and wire fraud, alleging that transactions presented as automated were largely processed by human workers [@usdoj2025techceo]." Add a bib entry for the DOJ release, keeping TechCrunch if wanted.

### S4. "first set out" for scaling laws
- Where: ch01.md:222. Text: "the scaling laws, first set out in a 2020 preprint [@kaplan2020scaling]".
- Problem: An expert will object to "first". Power-law scaling of error with data and model size was reported earlier, by Hestness et al. 2017 ("Deep Learning Scaling is Predictable, Empirically", arXiv:1712.00409). Kaplan et al. is the influential formulation for language models.
- Change to: "the scaling laws, set out for language models in an influential 2020 preprint [@kaplan2020scaling]".

### S5. Quotation wording: "non-trivial"
- Where: ch01.md:15. Text: 'understand language "in some nontrivial sense"'.
- Problem: The source reads "in some non-trivial sense", and Ch. 3 (ch03.md:400) quotes it with the hyphen. The two chapters are inconsistent.
- Evidence: Michael et al. 2023, ACL, statement 4-1: "could understand natural language in some non-trivial sense" (https://aclanthology.org/2023.acl-long.903.pdf).
- Change to: "in some non-trivial sense".

### S6. Brown et al. 1990 vocabulary
- Where: ch01.md:157. Text: "With a vocabulary of about a thousand words in each language".
- Problem: The English vocabulary was 1,000 words but the French was 1,700.
- Evidence: https://aclanthology.org/J90-2002.pdf: "we limited the English vocabulary to the 1,000 most frequently used words … We chose the French vocabulary to be the 1,700 most frequently used French words".
- Change to: "With vocabularies limited to the 1,000 commonest English and 1,700 commonest French words".

### S7. Cross-reference to "the Stanford group mentioned in Section 1.3"
- Where: ch01.md:222 (and ch01.md:78)
- Problem: INTERNAL CONTRADICTION. Section 1.3 never mentions Stanford; it says "a report by more than 100 researchers".
- Change to (line 78): "The term was introduced in 2021 in a report by more than 100 researchers, most of them at Stanford University, posted as a preprint, …"

### S8. "62% … used it"
- Where: ch01.md:234
- Problem: In context "it" reads as ChatGPT, but the St. Louis Fed figure is for generative AI of any kind ("the share of adults using AI rose from 45% to 62%", adults 18–64, May 2026).
- Change to: "62% of US adults aged 18 to 64 used generative AI [@bick2026what]."

### S9. Model list after October (optional currency note)
- Where: ch01.md:242
- Problem: Nothing in the sentence is wrong, but two relevant events followed the cut-off: Gemini 4 Carbon became generally available to developers, enterprises and consumers on 10 Nov 2026, and Anthropic released Claude Fable 5.2 on 9 Nov 2026.
- Evidence: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/ ("Nov 10, 2026 … Developers, enterprises, scientists, and consumers can now try our latest frontier model"); SD Times 9 Nov 2026.
- Change to (only if the author wants to go past October): add "; Carbon became generally available on 10 November."

### S10. Preface and copyright page understate when checking took place
- Where: ch00-preface.md:48 ("The evidence in this book was gathered and checked in October 2026.") and the copyright page ("Web sources were checked between 20 and 25 October 2026").
- Problem: INTERNAL CONTRADICTION. The bibliographies carry access dates of 30 October (16 entries) and 3 November 2026 (9 entries), for example openai2026gpt6system urldate 2026-11-03. Chapter 1 cites a source dated 28 October, and the fig-01-03 spec records vendor checks in November 2026.
- Change to: preface "The book covers events to the end of October 2026; its sources were gathered and checked up to November 2026." Copyright page "Web sources were checked between 20 October and 22 November 2026", or whatever the final check date is.

### S11. Preface AI-assistance statement is absolute
- Where: ch00-preface.md:52. Text: "Every factual claim was checked against the source cited for it".
- Problem: This review still found a quotation that does not match its source (M1). An absolute claim invites a reader to hold the book to it.
- Change to: "Factual claims were checked against the sources cited for them in several independent rounds, and the logs of those checks were kept."

### S12. Bib: mccarthy2006proposal page range
- Where: textbook/bib/ch01.bib, mccarthy2006proposal, `pages = {12}`.
- Problem: The AI Magazine 27(4) reprint runs over several pages; a single page number looks like an error. I could not open the AAAI page (bot wall) to confirm the range.
- Change to: `pages = {12--14}` after checking. Also, the Further reading entry "Twelve pages" (ch01.md:287) matches neither the reprint nor the 13-page McCarthy PDF transcription. Change it to "A short proposal that shows …".

## Could not verify
- Shannon 1950 wording "one variation per microsecond" (ch01.md:88). The transcription PDF (vision.unipv.it) and course slides read "micro-second". I could not see a scan of the original Philosophical Magazine typesetting, and I am not certain it does not read "micro-microsecond". Either way, "over 10^90 years" holds (10^120 µs ≈ 3×10^106 years). Low priority.
- Whether Gemini 4 Carbon's 85% ClockBench score was posted before 31 October 2026. The Wayback snapshot of 26 Oct returned 403. This matters only if the author keeps "By October 2026" (see S1).
- AI Magazine 2006 reprint of the Dartmouth proposal: pages, and whether the budget ($13,500) appears in the reprint as opposed to the original typescript. The AAAI site blocks automated access. The figure itself is confirmed from McCarthy's transcription (jmc.stanford.edu/articles/dartmouth/dartmouth.pdf).
- Lighthill report original pages (chilton-computing.org.uk did not resolve). I confirmed both quotations via Wikipedia's quotation and search results; the evidence log records an earlier direct read.
- Drew McDermott's "hurriedly changes the names…" sentence: confirmed only as quoted in Haigh 2024. The panel's full text is behind the AAAI wall; the AITopics abstract confirms "deep unease … will eventually result in disaster."
- Samuel 1959 "8 to 10 hours" (paraphrase; the abstract reads "8 or 10 hours of machine-playing time" from memory). It is not in quotation marks; harmless.

None of these needs a human check before printing, except the S1 date question if the "By October 2026" wording is kept.

## Reader notes
1. ch01.md:246 / PDF p. 36: the Figure 1.3 caption visibly runs off the page (M2), and the page below the figure is about one-third blank.
2. ch01.md:222: "the Stanford group mentioned in Section 1.3". A reader looks back and finds no Stanford (S7).
3. ch01.md:171: "IBM's words … 32 processors" followed immediately by "a 30-processor IBM computer". The book explains the two sources, but a reader may think it is a typo. Consider "IBM's history page says 32 processors; the builders' own account says 30 general-purpose processors driving 480 chess chips".
4. ch01.md:234: "62% … used it". It is unclear whether "it" means ChatGPT or generative AI (S8).
5. ch01.md:7: "Soviet, Japanese and continental European research traditions are left aside", yet Japan's Fifth Generation project and the UK's Alvey programme appear in 1.5. The intent (traditions, not funding programmes) is fine; "Soviet, Japanese and continental European research traditions" could become "…research traditions (as opposed to their funding programmes)". Optional.
6. ch01.md:29: the AGI paragraph packs five definitions and an EU legal threshold into one paragraph. Consider splitting at "The EU AI Act does not use the term AGI".
7. ch01.md:211–220: the four-model paragraph plus Table 1.4 repeats the same numbers twice (GLUE 80.5/72.8, 175 billion). Some readers will skim.
8. ch01.md:240: "in skilled-human working time" is jargon. "measured by how long the tasks take skilled people" reads more easily.
9. Further reading, ch01.md:287: "Twelve pages" (S12).

## Checked and confirmed

**Opening and §1.1**
- Dartmouth proposal dated 31 Aug 1955; McCarthy (Dartmouth), Minsky (Harvard), Rochester (IBM), Shannon (Bell Telephone Laboratories); Rockefeller Foundation; "2 month, 10 man study"; $13,500 total; conjecture quotation verbatim; seven aspects as listed; "major obstacle …" quote; "a large part of human thought …" quote; section 4 "try all possible answers in order. This method is inefficient"; "significant advance … for a summer" (jmc.stanford.edu PDF).
- ChatGPT 1.2B weekly users at DevDay, 29 Sep 2026 (openai.com DevDay recap; Engadget live blog; The Decoder). No newer company figure up to 22 Nov 2026 (searches; a 3 Nov interview repeats 1.2B).
- ChatGPT released Nov 2022 as a "research preview" (Chatterji et al. 2025, OpenAI-hosted PDF).
- AI Act Chapters I–II applicable from 2 Feb 2025 (art. 113); SEC fines for AI washing (SEC 2024-36).
- Haigh: English-language histories construct AI "as an almost entirely Anglo-American project" (Yale PDF print of CACM column).
- Turing 1950 opening sentence, imitation game, 50 years, 10^9 storage, 70% after five minutes (standard text).
- Michael et al. 2023: May–June 2022 survey, 51/49 split.
- Solomonoff (IEEE Spectrum, 6 May 2023): 18 June–17 Aug 1956, "a few dozen", came and went, Newell and Simon talk "early in the summer".
- SEP: "Ten thinkers attended", including Newell and Simon; LT "a remarkable achievement"; elementary theorems in the propositional calculus.
- Newell & Simon 1956 bibliographic data (Crossref: IRE Trans. Inf. Theory 2(3):61–79).
- AI100 2016: Nilsson definition verbatim (ai100.stanford.edu).
- Legg & Hutter: "70-odd" definitions (arXiv 0706.3639).
- OpenAI charter AGI definition (well known; bib date 9 Apr 2018).
- Morris et al.: Competent AGI at least 50th percentile of skilled adults on most cognitive tasks; "as of this writing in September 2023"; Emerging AGI; short essay writing, simple coding (arXiv 2311.02462v4).
- AI Act arts. 3(63)–3(65) and 51 (10^25) (text as quoted in Commission guidelines and the Act).

**§1.2 Definitions**
- OECD memorandum p. 4: 2019 and 2023 texts verbatim, Russell & Norvig basis, adoption 8 Nov 2023; p. 6 "will likely emerge", "exercise judgement"; p. 7 LLM "plausible response" and recommender "narrow down" examples; p. 9 build phase and "gained significant momentum" (OECD PDF).
- Commission guidelines C(2025) 5053 final, Brussels 29.7.2025: para 7 not binding/CJEU; para 9 seven elements; para 39 "search and optimisation methods" and "early generation expert systems intended for medical diagnosis"; para 41 "may nevertheless fall outside"; para 42 regression, "transcend 'basic data processing'", "consolidated manner for many years"; para 46 database/spreadsheet; para 48 minimax chess "without requiring prior learning from data"; paras 49–50 simple prediction; para 62 "No automatic determination or exhaustive lists"; para 63 "vast majority" (ec.europa.eu PDF).
- Guidelines first published 6 Feb 2025 (digital-strategy.ec.europa.eu news item).
- Recital 12 wording (quoted via guidelines para 39 and the Act).
- 15 U.S.C. 9401(3) wording incl. "use model inference to formulate options for information or action"; NDAA enacted 1 Jan 2021 (knowledge, consistent with Cornell LII entry in bib).
- Table 1.1: all cells consistent with the four texts.
- No change to Art. 3(1) or the definition guidelines in 2026 found (search, incl. Digital Omnibus coverage).

**§1.3 Terms**
- LeCun, Bengio, Hinton 2015 quotation (standard abstract).
- Bommasani et al.: 2021, 114 authors, "critically central yet incomplete character" (arXiv API); "inherited by all the adapted models downstream" (abstract).
- Wooldridge & Jennings 1995 abstract: "The concept of an agent has become important in both artificial intelligence (AI) and mainstream computer science" (Semantic Scholar).
- Samuel 1959 bibliographic data (Crossref).

**§1.4 Symbolic AI and MYCIN**
- Shannon 1950: "of the order of 30 legal moves", "about 10^3 possibilities", "about 40 moves", "10^120 variations", "over 10^90 years" (transcription PDF).
- Simon 1960 quotation and date (Mitchell 2021; Quote Investigator: The New Science of Management Decision, p. 38). Minsky "Within a generation…" (Mitchell 2021, citing Minsky 1967 p. 2).
- Lighthill: both quotations; July 1972 / 1973; Science Research Council (Wikipedia quotation; search results).
- Mitchell: Lighthill plus the DoD "American Study Group" report; "led to sharp funding decreases and a downturn in enthusiasm for AI in both countries" (arXiv PDF).
- Haigh: "the 'first AI winter' of the 1970s never happened"; 1970s "steady growth" (Yale PDF).
- Buchanan & Shortliffe: RULE036 text p. 71; "grew to about 500" rules p. 71; backward chaining, subgoals, "Questions are asked … when rules fail" p. 71; CF −1 to +1 p. 81; worked example 0.3 → 0.44, MD 0.1, CF 0.34 p. 260; Combining Function 1 p. 255; "eight or nine rules", 0.999, CF 0.8 → 0.199, "counterintuitive", "occasionally led MYCIN to reach incorrect inferences", 0.2 threshold, revised CF = (MB − MD)/(1 − min(MB, MD)), stores a running CF, "approximately 1977" p. 216; "shallow" and "largely (but not entirely) true of MYCIN" p. 672; "explicitly our initial intention", "laid to rest in 1978" p. 673; "too expensive" p. 701; "would not be a cost-effective tool … meningitis and bacteremia", "not readable as text" p. 702 (Columbia chapter PDFs 4, 5, 10, 11, 36).
- Yu et al. 1979: 8 evaluators, 9 human prescribers, 10 meningitis cases, MYCIN 65%, five faculty 42.5–62.5% (PubMed 480542).

**§1.5 Boom and second winter**
- Haigh: XCON by McDermott (CMU) for DEC VAX; 480 rules; DEC "boasted" >$40M/year; Lisp workstation start-ups; Emycin shell; Fifth Generation and Alvey; SCI 1983 and its assumption about expert systems, language and vision; speech progressed, other projects disappointed; ALV abandoned "At the end of 1987"; "proved unsustainable"; hire new experts; DEC 59 technical staff by 1989; "most widely publicized application of AI"; wages; Cyc from 1983, ~2,000 person-years, 30 million rules, private company; McDermott's "AI Winter" and "hurriedly changes the names" (Yale PDF).
- AAAI-84 panel "deep unease … will eventually result in disaster" (AITopics abstract).
- Mitchell: "about five years after McDermott's warning, a new AI winter set in"; "often unable to generalize or adapt when faced with new situations"; SCI as response to Fifth Generation (arXiv PDF).

**§1.6 Statistical turn**
- Bahl, Jelinek, Mercer 1983 and Jelinek 1976 bibliographic data (Semantic Scholar/Crossref titles and years).
- Huang, Baker, Reddy 2014: "A pivotal change in the representation of knowledge in speech recognition"; "the Dragon, Harpy, and Sphinx I/II systems were all based on a single, relatively simple modeling principle of joint global optimization"; WER in DARPA evaluations; Microsoft and IBM Switchboard results "following the deep learning framework" (kk.org PDF copy of CACM article).
- Brown et al. 1990: Pr(S)Pr(T|S); Hansards kept "By law" in both languages; hear → bravo (.992); 73 sentences; 5% exact; 48% reasonable (ACL Anthology PDF).
- Mitchell: "meteoric rise of machine learning", "inspired by statistics rather than by neuroscience or psychology", "then-discredited field of AI".
- Haigh: neural-network work "pursued under other brands, such as machine learning and pattern recognition".
- Banko & Brill 2001: four learners; confusion sets incl. {then, than}; one billion words against corpora "of only one million words or less"; trade-off quotation verbatim (ACL Anthology PDF).
- Halevy, Norvig, Pereira 2009: 2006 trillion-word corpus, sequences up to five words, "a million times larger than the Brown Corpus", "simple models and a lot of data trump…" (Google PDF).
- IBM: 1996 Kasparov won 4–2 (see M3); May 1997 New York, 3.5–2.5, six games; "first computer system to defeat a reigning world champion under standard tournament time controls"; "brute force computing power"; 32 processors; 200 million positions/s; goal to beat the world's best; "heralding a future in which supercomputers and artificial intelligence could simulate human thinking" (ibm.com/history/deep-blue).
- Campbell et al. 2002: "30-node (30-processor) IBM RS/6000 SP computer and 480 single-chip chess search engines" p. 60; "large majority of the features and weights … created/tuned by hand"; comparison training on pawn-shelter weights, "increased prior to the 1997 match" p. 76 (course-site PDF copy).
- Russakovsky et al. 2015: 1,000 classes, ~1.2M training images (arXiv PDF).

**§1.7 Deep learning to 2026**
- Seide et al. 2011: 309 hours; 27.4% → 18.5%; "33% relative improvement"; Switchboard RT03S (ISCA PDF).
- Krizhevsky et al. 2012: 15.3% vs 26.2%; 60 million parameters; five to six days on two GTX 580 3GB (NeurIPS PDF).
- Russakovsky: SuperVision 16.4% (official data); 2010 NEC 28.2; 2011 XRCE 25.8; 2013 Clarifai 11.7; 2014 GoogLeNet 6.7; annotator A1 trained on 500 images and annotated 1,500 test images at 5.1%; A2 258 images; top-5/top-1/hierarchical "same ordering", top-5 "the simplest" (arXiv PDF). Figure 1.2 values all match (figs_ch01.py).
- He et al. 2016: up to 152 layers, 3.57% (abstract). He et al. 2015: 4.94%, "surpass human-level" (abstract).
- AlphaGo: Nature Jan 2016; Fan Hui 5–0; "a feat previously thought to be at least a decade away"; self-play RL (Nature abstract, known); Lee Sedol 4–1 March 2016, Seoul.
- Vaswani et al.: "based solely on attention mechanisms, dispensing with recurrence and convolutions entirely"; 28.4 BLEU EN-DE; "by over 2 BLEU"; "significantly less time to train" (arXiv PDF).
- Table 1.3: all five rows match the sources above.
- GPT-1: 12-layer; BooksCorpus "over 7,000 unique unpublished books"; "9 out of the 12 tasks" (OpenAI PDF).
- GPT-2: 117M "equivalent to the original GPT"; 1542M; WebText "slightly over 8 million documents … 40 GB"; "7 out of 8 … zero-shot" (OpenAI PDF).
- BERT: 340M; BooksCorpus 800M + Wikipedia 2,500M words; GLUE 80.5 vs OpenAI GPT 72.8 (ACL Anthology PDF).
- GPT-3: 175B, "10x more than any previous non-sparse language model", 300B tokens, 3.14E+23 (arXiv PDF). Table 1.4 all cells confirmed.
- InstructGPT: 1.3B preferred to 175B GPT-3 (arXiv PDF).
- Chatterji et al. 2025: 700 million weekly users by July 2025, ~10% of world adults (OpenAI-hosted PDF; NBER abstract).
- GPT-4 report: images, "top 10% of test takers" (arXiv abstract). Martínez 2024: ~62nd percentile first-time takers, ~48th among those who passed (Semantic Scholar abstract).
- LLaMA Feb 2023, "LLaMA-13B outperforms GPT-3 (175B) on most benchmarks" (arXiv). DeepSeek-V3 Dec 2024, comparable to leading closed-source models (arXiv abstract).
- GANs 2014, DDPM June 2020 (arXiv). AlphaFold 2 "competitive with experimental structures in a majority of cases" (Nature abstract).
- Nobel physics 2024 Hopfield and Hinton, "for foundational discoveries and inventions that enable machine learning with artificial neural networks" (8 Oct 2024); chemistry: half to Hassabis and Jumper "for protein structure prediction" (9 Oct 2024) (nobelprize.org).
- Bick, Blandin, Deming, Management Science 72(10):8440–8456 (2026), abstract: work adoption faster than the PC, overall adoption "has outpaced both PCs and the internet" (Crossref).
- St. Louis Fed blog 1 Sep 2026: 45% → 62%, ages 18–64, May 2026 (WebFetch).
- Microsoft 7 May 2026: US "from 24th to 21st", Q1 2026, 31.3%, ages 15–64, telemetry (WebFetch).
- o1 "trained with large-scale reinforcement learning to reason using chain of thought" (arXiv abstract). DeepSeek-R1 Nature 17 Sep 2025: "can be incentivized through pure reinforcement learning"; R1 used "thousands of cold-start data" (Nature page).
- METR: posted 18 Mar 2025; "doubling approximately every seven months since 2019" (arXiv); NeurIPS 2025 DOI resolves (Crossref).
- OSWorld 2024: humans 72.36%, best model 12.24% (arXiv; NeurIPS DOI resolves).
- OSWorld-Verified: best "General model" 85.96% (307.73/358), dated 1 Aug 2026; still the latest entries on 22 Nov 2026 (results xlsx).
- GPT-6 Astra system card published 3 Sep 2026 (deploymentsafety.openai.com). Claude Opus 5.5, 22 Sep 2026 (anthropic.com). Gemini 4 Argon, 30 Sep 2026, "rolling out to a set of trusted cyber defenders through our Fairwind Program". Gemini 4 Carbon, 28 Oct 2026, "available to a subset of cyber defenders" (blog.google).
- Figure 1.3 dated labels: all 23 research and 12 deployment/policy labels match the text and sources (BERT Oct 2018, GPT-3 May 2020, DDPM Jun 2020, AlphaFold Jul 2021, foundation model Aug 2021, InstructGPT Mar 2022, GPT-4 Mar 2023, o1 Sep 2024, R1 Jan 2025, ChatGPT 30 Nov 2022, LLaMA Feb 2023, OECD Nov 2023, AI Act 2024, Nobels Oct 2024, MCP 25 Nov 2024, Sept 2026 releases, DevDay 29 Sep 2026). Winter bands "c. 1974–80" and "from c. 1987" are consistent with Mitchell (spring of the 1960s and early 1970s, then the winter, then an upturn from the early 1980s; new winter in the late 1980s) and are labelled approximate.

**Debate box and §1.8**
- Sutton, 13 Mar 2019: "general methods that leverage computation are ultimately the most effective, and by a large margin"; chess search, statistical methods winning in speech, deep learning in speech and vision (incompleteideas.net).
- Marcus 2018: ten concerns; "must be supplemented by other techniques if we are to reach artificial general intelligence" (arXiv).
- AI Index 2026: Gemini Deep Think 35 points (gold), IMO 2025; ClockBench top model 50.6% in March 2026 (topline 50.1%), so "about half" is right (AI Index PDF).
- ClockBench average human 90.7% (clockbench.ai); top-model figure now outdated (S1).
- Tesler: "Tesler's Theorem (ca. 1970)", both wordings verbatim (nomodes.com).
- AI100: "AI effect" / "odd paradox" sentence and "continual endeavor to push forward the frontier of machine intelligence" (ai100.stanford.edu).
- Haigh: "a less controversial alternative to artificial intelligence"; "flipped to refer primarily to deep learning and generative systems".
- SEC 18 Mar 2024: Delphia and Global Predictions, $400,000 total, Gensler "AI washing" (WebFetch sec.gov).
- FTC 25 Sep 2024: five actions, "seized on the hype surrounding AI", DoNotPay "the world's first robot lawyer", Khan "no AI exemption from the laws on the books" (WebFetch ftc.gov).
- SEC Presto, 14 Jan 2025: settled cease-and-desist over claims about orders handled without human intervention; no penalty, so the book rightly does not say "fined" (WebFetch sec.gov).
- Nate: April 2025 charges against Albert Saniger (SDNY securities and wire fraud); no later disposition found (search).
- Suchman 2023: AI as uncontroversial "thing"; "stabilization of AI as a figure enables further investments"; "travel under the sign of AI" (Semantic Scholar abstract; Crossref BD&S 10(2)).
- Mitchell: springs/winters wording verbatim; Fallacy 2 "Easy things are easy and hard things are hard".

**Preface**
- Reference count: the PDF reference list ends at no. 1244, so "more than 1,200" is correct. 626 pages (pdfinfo; BUILD-INFO).
- Footer source lines with pinpoints in brackets exist (e.g. "373 (art. 113)"). Captions use the same numbers (but see M2).
- Fourteen chapters in five parts match the table of contents. Chapter 14 has ten labelled proposals (14.1–14.10). Chapter 3 tables are "computed by the author" with settings.
- Chapter 1 follows the labelling policy: preprints labelled at first mention (Bommasani, Mitchell, Kaplan, Marcus, Chatterji working paper); company claims attributed; Sutton essay and Haigh column identified. Exceptions: S2 and S3 (press cited where a primary source exists).

## Tally
Claims checked against a web source: 168. Confirmed: 157. Wrong: 3 (M1, M3, plus M2 print defect). Outdated: 1 (S1 ClockBench; S9 currency note not counted as wrong). Unsupported by cited source: 0 (S6 and S8 are imprecise wording, counted under confirmed-with-note). Could not verify: 6. Arithmetic items recomputed: 12 (errors: 0): Table 1.2 MB 0.44, CF 0.34, revised 0.378; 0.999 − 0.8 = 0.199; 1 − 0.4^8 ≈ 0.999; GPT-1→GPT-3 ×1,496; Seide 32.5% ≈ 33%; Shannon 30² ≈ 10³, (10³)^40 = 10^120, 10^120 µs ≈ 3×10^106 yr > 10^90; OSWorld 307.73/358 = 85.96%; Banko 1B/1M = 1,000×. Bib entries checked: 62 (problems: 1, mccarthy2006proposal pages; plus 2 new entries recommended in S2 and S3).
