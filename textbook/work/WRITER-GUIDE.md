# Writer guide: *Understanding AI: Technology, Trends and the Decade Ahead* (course text)

You write ONE chapter of a university course text on AI. Today is 2026-10-22; the book is current to October 2026. Read the brief (`/home/user/FutureOfAI/textbook/artifacts/00-brief.md`) and your chapter's entry in the outline (`/home/user/FutureOfAI/textbook/artifacts/07-outline.md`); also skim the neighbouring entries to avoid overlap. You may consult the previous book's verified evidence files in `/home/user/FutureOfAI/book/work/evidence-chapter-*.md` as leads, but re-verify anything you use.

## 1. Voice and readability
- **Audience:** first-year undergraduates from any discipline, plus a technical minority. Clear, calm, precise; British spelling.
- **No fiction:** no invented people, scenes or dialogues, and no first-person anecdotes. Examples must be real and sourced.
- **Sentences and paragraphs:** average 15–22 words with natural variation; paragraphs of 3–6 sentences.
- **Concepts:** define every technical term the first time, in plain words, then use it consistently. Give each abstraction a concrete example or analogy within two sentences, and say where the analogy breaks down.
- **Maths:** no maths beyond school level in the main text. Equations, if any, go into a "Going deeper" box, each explained in words.
- **Neutral and fair:**
  - present contested questions as debates, with the best evidence on each side;
  - attribute opinions ("Acemoglu (2024) argues…");
  - do not editorialise;
  - avoid hype words (revolutionary, unprecedented, game-changing, transformative) and doom language.
- **Avoid machine-prose habits:**
  - "not X but Y" reflexes;
  - habitual lists of three;
  - em-dash chains (use commas, colons and parentheses; at most a few dashes per chapter);
  - closing morals.

## 2. Chapter template (Markdown, exact structure)
```
# Chapter N: Title

::: {.objectives}
**After working through this chapter you should be able to:**

- … (3–5 objectives, each starting with a verb: explain, compare, evaluate, …)
:::

Opening (1–3 paragraphs): a real, documented case or fact that motivates the chapter, with citation.

## N.1 Section title
…text with citations…

![Figure N.1: Caption that explains what the figure shows and why it matters. Source: … or "Diagram by the author."](figures/fig-NN-01.svg){#fig:NN-01}

::: {.box .concept}
**Key concept: Term**

Two to five sentences.
:::

::: {.box .case}
**Case study: Title**

A real case, sourced.
:::

::: {.box .debate}
**Debate: Question?**

Position A, with its evidence; position B, with its evidence; what would settle it.
:::

::: {.box .deeper}
**Going deeper: Title**

Optional technical detail.
:::

## N.x …

## Summary
- 5–8 bullets.

## Key terms
term one · term two · … (8–15 terms, each also defined in your glossary file)

## Discussion questions
1. … (4–6 questions; at least one asks students to evaluate evidence, one to apply a concept to a new case)

## Further reading
- Author (Year). *Title*. One sentence on why to read it. [@key]
```
- Leave a blank line after the bold label inside every box.
- Use 4–7 numbered sections. Use 2–4 figures and 2–5 boxes per chapter.
- Refer to every figure in the text ("Figure 3.2 shows…").
- **Length:** 5,500–6,500 words in the body (from the objectives to the end of the last numbered section). Check with `wc -w`.

## 3. Citations: the evidence standard
- **Format:** pandoc citation syntax with BibTeX keys: `[@vaswani2017attention]`, `[@kaplan2020scaling; @hoffmann2022training]`, or in-text `@acemoglu2024simple argues …`. Key format: firstauthorsurname + year + firstsignificanttitleword, lowercase, ASCII only.
- **What needs a citation:** every non-obvious factual claim: numbers, dates, study results, quotations, legal facts and attributions.
- **Verify before citing:** use WebSearch / WebFetch (load them via ToolSearch "select:WebSearch,WebFetch"). Never cite from memory. For each source, confirm that it exists, its authors, year and venue, and that it actually supports your sentence. Copy numbers exactly; give the sample, the setting and the date. If you cannot verify a claim, cut it.
- **Hierarchy:** peer-reviewed papers, official statistics and primary legal texts come first; then major preprints (label them "preprint"); then reports from recognised institutions (IEA, OECD, Stanford HAI, Epoch AI, METR); then company announcements (label them "according to the company"). Use journalism only for events, and prefer reputable outlets.
- **Quotations:** at most about 25 words, used sparingly, in quotation marks, with page or section where available.
- **Recency:** prefer the latest data available as of October 2026, and give the year of the data.
- **Bibliography file:** write `/home/user/FutureOfAI/textbook/bib/chNN.bib` (NN = two-digit chapter) with one BibTeX entry per key used. Fields:
  - `author` (as "Surname, Given and Surname, Given"; institutions in double braces `{{International Energy Agency}}`);
  - `title`, `year`;
  - `journal` / `booktitle` / `publisher` / `institution`, with `volume`, `number` and `pages` when available;
  - `doi` (without the URL prefix) when one exists, else `url`;
  - `urldate = {2026-10-22}` for web sources.
  - Entry types: `@article`, `@inproceedings`, `@book`, `@techreport`, `@misc` (for web pages, preprints and announcements: put "arXiv preprint arXiv:XXXX" or "Company blog" in `howpublished`), `@incollection`, `@legislation` → use `@misc` with `howpublished`.
  - Every bib entry must be cited in your chapter, and every citation must have an entry.
- **Evidence log:** write `/home/user/FutureOfAI/textbook/work/evidence-chNN.md`: one line per key with the claim it supports, the exact number or quote, the URL you checked, and the evidence type (peer-reviewed / preprint / official / institutional report / company claim / news).

## 4. Figures
You do NOT draw figures. For each figure, write a spec file `/home/user/FutureOfAI/textbook/figures/specs/fig-NN-MM.md` containing:
- **type:** diagram | bar chart | line chart | timeline | scatter | table-figure
- **purpose:** what the student should understand from it
- **caption:** the final caption, ending with "Source: [citation key(s)]" or "Diagram by the author."
- **content:**
  - for diagrams: every box and label, the arrows between them, and a layout suggestion (left→right, top→bottom), using short labels (≤ 4 words);
  - for charts: exact data points with units, axis labels, scale (linear/log), and a source key for every number. Never invent data. A conceptual chart must say "schematic, not to scale" in the caption.

Figures are greyscale-friendly line diagrams in one house style, drawn centrally.

## 5. Glossary
Write `/home/user/FutureOfAI/textbook/work/glossary-chNN.md`: one line per key term, in the format `**term**: definition in 1–2 plain sentences.`

## 6. Safety constraints
- No operational detail about weapons, pathogens, toxins, drug resistance, cyber-attack techniques or self-harm. Discuss such risks only at the level of policy and of published risk assessments.
- Biology and medicine appear only at a high level (for example, "AlphaFold predicts a protein's 3D structure from its sequence").

## 7. Deliver
- Write the chapter to `/home/user/FutureOfAI/textbook/chapters/chNN.md`, plus the bib, evidence, glossary and figure-spec files. Do not touch other chapters' files.
- In your final message, report:
  - the word count;
  - the number of citations and unique sources;
  - the figure list;
  - any claims you dropped because you could not verify them;
  - any uncertainty the fact-checker should look at first.
