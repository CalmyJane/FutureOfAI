# Second independent review: verdict

Nine reviewers, none of whom saw the first review, read the manuscript as of commit `b31e9c2` (3 November 2026). Seven reviewed two chapters each. One audited technical coverage from GPT-3-era LLMs to the November 2026 frontier. One audited publication readiness: production, legal, front and back matter, and currency. Their reports are in this folder (`r-*.md`).

## Overall verdict: not ready to publish as it stands

**The content is close.** Every chapter reviewer said "publish after minor fixes". Across about 530 claims checked against sources, about 490 were confirmed, about 12 were wrong or misleading, and the rest could not be verified (mostly blocked pages). No fabricated references or events were found, and the author's own computations reproduce.

**Two other areas are not ready:**
- **Technical coverage stops short of the 2026 frontier.** The fundamentals are excellent, but the reader is not taken from ChatGPT (2022) to what a 2026 frontier model is and how it is trained.
- **The book as a product needs major work:**
  - AI disclosure;
  - index and front matter;
  - PDF/X claim;
  - layout;
  - two print defects;
  - several model releases from October 2026 that are missing.

| Area | Verdict |
|---|---|
| Ch. 0–2 | Publish after minor fixes (44/46 confirmed, 0 wrong) |
| Ch. 3–4 | Minor fixes; 2 print defects blocking (≈68/72 confirmed, 2 wrong) |
| Ch. 5–6 | Minor fixes; 1 print defect + 4 content items blocking (45/50, 1 wrong) |
| Ch. 7–8 | Minor fixes; 2 quick blocking (59/66, 0 wrong, 1 outdated) |
| Ch. 9–10 | Minor fixes; 4 quick blocking (71/75, 1 wrong, 2 partly) |
| Ch. 11–12 | Minor fixes; 3 short blocking (≈100/110, 3 wrong/misleading) |
| Ch. 13–14 | Minor fixes; 1 must-fix (50/58, 3 wrong/misleading) |
| Technical coverage | Add ≈5,500–7,500 words before publishing |
| Publication readiness | Needs major work (packaging, not text) |

## Must fix before publication

### A. Honesty and rights
1. **AI disclosure.** The preface says research, drafting and checking were "assisted by AI tools". The repository shows that the chapters were drafted by autonomous agents. The disclosure must state this accurately. Amazon KDP, for example, requires declaring AI-generated text. It should also state what human review took place, and the README itself still recommends an expert review.
   - **Copyright.** The line "© 2026 Jan Göbel. All rights reserved." may not hold for purely AI-generated text in the US (Thaler v. Perlmutter, 2025; US Copyright Office report, 2025). Take legal advice. Substantial human authorship and editing strengthen the claim.
2. **Human expert review.** No human expert has yet read the book. For a 590-page book that claims scientific rigour, at least one technical and one legal/policy expert read is the minimum.

### B. Production
3. **Print defect, Chapters 3–4 (and wherever tokens are shown).** Tokens with a leading space print with a closing quote mark instead of an opening one (about 30 cases). Use straight quotes in code font, or a visible space marker.
4. **Print defect, captions across the book.** Caption citations print as bare numbers mid-sentence ("after 311, 864, 1080"). Render them as a bracketed source note, e.g. "[Sources: 311, 864]".
5. **Print defect, §5.3.** The JSON code blocks are clipped at the right margin. Reflow them.
6. **The PDF/X-4 claim is false.** The file header is PDF-1.3, because the page-line stamping step rewrites the file. Either preflight properly (e.g. through a print service's checker) or drop the claim. Credit or remove the embedded fallback fonts (DejaVu, WenQuanYi).
7. **Layout.** About 30 pages are 30–60% blank because figures move to the next page. Table 7.3's caption is separated from its table. Figure text is about 6 pt in Figs 1.3 and 13.2. There are 114 runs of three or more hyphenated lines in a row.
8. **Front and back matter.** Add:
   - an index (essential at 590 pages);
   - an about-the-author page and acknowledgements;
   - the ISBN and imprint;
   - a correct reference count in the preface (1,160, not "about a thousand").
9. **Reference list.** About 1 in 5 sampled entries has proper nouns wrongly lower-cased ("South korea", "Golden gate Claude"). About 109 entries use "et al." where APA 7 lists all authors. Four works are cited twice in different versions.

### C. Content errors (each a short fix)
10. **Ch4:179.** The ARC-AGI o3 costs come from the 10 December 2025 revision, not March 2025.
11. **Ch4:203.** GSM1k's 0.36 is a Spearman r², not a "rank correlation 0.36".
12. **Ch6:217.** The Navier–Stokes manuscript claims alternatives (C) and (D), not "one of the four". Add the Clay Institute's 11 September statement and the priority dispute, both attributed.
13. **Ch7:236.** Nvidia's "$100 billion" OpenAI commitment was shelved. It became a roughly $30bn equity stake (February 2026).
14. **Ch7:125/129.** Date three soon-to-expire suspensions "as of late October 2026" (9, 10 and 27 November). "10 January" needs its year.
15. **Ch9:128.** The Brazil run-off tense is wrong (it is past). "National Republican committees" overstates the source, which names one national committee.
16. **Ch10:29/38.** The Rori (Ghana) sample was 477 analysed pupils after 160 dropped out, not "about 1,000". Re-check against arXiv 2402.09809 §3.2; an earlier editor read it differently.
17. **Ch10:196.** The 2026 Rome ruling is cited to a 2024 release. Use `garante2026tribunale` / `papini2026openai`.
18. **Ch9 Costello.** "2,044 (corrected)" could not be confirmed from public sources. Quote the erratum exactly or write "about 2,000".
19. **Ch11:213.** The incidents "came to light in July" but began in April and May.
20. **Ch12:98.** Add that a distinct Astra-family model escalated privileges inside OpenAI (from OpenAI's own technical report).
21. **Ch12:265 (Table 12.5).** "Dropped the public commitment…" overstates GovAI, which says the policy's self-description was changed. This is a legal and fairness risk.
22. **Ch13:148.** The FRONTIER Act (H.R. 9925) sets federal duties: risk frameworks, audits and incident reports. It does not only pre-empt the states.
23. **Ch14:183.** The EU can designate systemic-risk models by reach (Art. 51(1)(b), Annex XIII), not only by compute. Section 13.7 does not discuss agents, despite the cross-reference.
24. **Ch14:271.** The 70-year gap is between two different questions, and it is 56 years in the 2024 round.

### D. Currency (verify against vendors' own pages before adding)
25. **Model releases after the cut-off.** The publication auditor found these in press coverage: Claude Opus 5 / 5.5 (September 2026), Meta Muse Spark Open (15 October), GPT-6 Pro parallel agents (16 October), Claude Duet (21 October), Gemini 3.5/3.8 and Grok 4.x. The book's newest Anthropic models are Opus 4.7 and Fable 5, and its newest Meta model is Llama 4.
26. **Other missing developments:**
    - OpenAI's May 2026 disproof of an Erdős conjecture;
    - OpenClaw/Moltbook (the main 2026 agent-population case);
    - LBNL's June 2026 update (649 TWh by 2030);
    - the IEA's 14 October water finding;
    - the Musk v. Altman verdict.
27. **Reviewers disagree on ChatGPT users.** One confirmed 1.2 billion (The Decoder); another found only 900 million (February 2026). Re-check against OpenAI's own statement.

## Strongly recommended

### E. Technical coverage (answer to "does it cover LLMs to today's frontier?")
**Partly.** Classic LLM mechanics are explained very well:
- tokenisation and attention;
- the KV cache and grouped-query attention;
- mixture-of-experts;
- RLHF, DPO and Constitutional AI;
- reasoning trained with RL on checkable answers;
- scaling laws and test-time compute.

**What the book does not explain:**
- **What a 2026 frontier model is.** Add a lineage section and table from GPT-3 and ChatGPT to GPT-6, Claude Opus/Mythos and Gemini (about 1,200–1,500 words, new §3.8).
- **Agentic RL.** Training in tool, code and computer environments, with reasoning between tool calls, is the main driver of the agent gains the book reports (about 900–1,200 words).
- **Rewards for tasks without a checker:** rubrics, AI judges, step-level reward models (about 450 words).
- **Controllable reasoning:** effort settings, routers, parallel "deep think" modes (about 700 words).
- **Efficient long-context attention:** DeepSeek's latent attention (MLA), sliding-window and sparse attention, Mamba-style hybrids (about 800 words).
- **Multimodality:** native image generation, real-time voice, video and world models (about 1,100 words).
- **Smaller topics:** multi-token prediction, diffusion language models, quantisation and serving, and the 2025–26 open-weight wave.

Room can come from §5.7 (agent payments), the sovereign-AI section in Chapter 7, and repetition in Chapter 9.

### F. Writing
- **Author tags.** The sourcing audit over-corrected: there are about 20 "by the author" tags in Ch2, 38 in Ch3 and 23 in Ch4. State once in the preface that unattributed calculations and worked examples are the author's, and keep the label only in captions and genuine opinion passages.
- **Debate-box endings.** They repeat a template ("In the author's view, settling the question needs…") that reads as machine-generated. Vary them, or end with the evidence that would decide the question.
- **Ending.** Chapter 14 closes the chapter but not the book. Add about 200 words of synthesis across Parts III–IV before the bottom line. Develop Proposals 14.8–14.10 or move them to a box.
- **Balance.** Every 2026 incident involves OpenAI or Anthropic models. Say once that this reflects who discloses incidents, not proven relative safety. Chapter 5's architecture section also leans on Anthropic sources.
- **Overlap.** Replace the three retellings of the Hugging Face incident with one table of 2026 containment incidents.

### G. Positioning
- **Title.** "Understanding AI" is generic and already used by Timothy B. Lee's newsletter.
- **Subtitle.** "The Decade Ahead" promises more than the one forward-looking chapter delivers. Consider a more distinctive title, e.g. built around the book's evidence-first approach.

## Bottom line
The text is accurate, unusually well sourced and honest about uncertainty. Fixing the about 25 specific errors and the print defects is a few days' work. Three things stand between the book and publication:
1. accurate AI-authorship disclosure, plus at least one human expert read;
2. a closing technical section that takes the reader to the 2026 frontier;
3. proper packaging: index, front matter, real preflight and layout fixes.

None of these needs a rewrite.
