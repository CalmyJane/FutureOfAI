# Whole-book and production checks (fourth review, 26 November 2026)

Files examined: `textbook/delivery/understanding-ai_A5_interior.pdf` (646 pages, A5, built 26 Nov 2026 23:01 UTC), `textbook/delivery/understanding-ai_cover_A5_PB.pdf`, `textbook/print/build.py` (`front_matter`, `AI_NOTE`), `textbook/print/cover.py`, `textbook/print/book.css`, `textbook/print/make_index.py`, `textbook/print/index_entities.txt`, `textbook/print/index.md`, `textbook/chapters/ch00-preface.md`, plus cross-chapter greps of `ch01`–`ch14`. Printed page numbers in this book are the same as PDF page indices (printed p. 9 is PDF page 9), and this was checked on the TOC targets.

## Verdict

**Ready to print after the fixes below.** The AI-authorship disclosure is unusually frank and mostly sufficient. One statement in it ("Three such review rounds") will be false once this fourth round is applied, and the back cover leaves out the one caveat a buyer most needs. The production problems are concrete and easy to fix: the ISBN placeholder is still printed, the copyright page overflows so that the ISBN sits alone on p. 5, the cover still carries the barcode placeholder text, and the automatically built index has a page-7 (Contents) bug and several entries that mix unrelated senses of a word. No text runs off the page, no figure is broken, the TOC is correct, and the spine width matches the page count exactly. The most repeated 2026 facts (model names, release dates, the 12 June export control, the Digital Omnibus date, the cut-off) agree across chapters, with two small exceptions.

## MUST change before printing

### M1. ISBN placeholder printed in the interior, and barcode placeholder on the cover
- Where: textbook/print/build.py:30 and :143 (interior p. 5); textbook/print/cover.py (barcode box, back cover bottom right)
- Text now: "ISBN: [to be added when the BoD project is set up]" (interior); "ISBN barcode / place BoD EAN-13 here" (cover, printed inside the white box)
- Problem: UNCLEAR / production blocker. BoD requires the ISBN in the imprint and the barcode on the back cover, and the author has to place both. As built, the book would print the placeholder strings.
- Evidence: BoD myBoD starter kit (https://www.bod.ch/bodfiles/DE-Storage/documents/myBoD-starter-kit.pdf, undated, read 26 Nov 2026): "Du musst nun das Impressum in deiner Buchblock-Datei um die ISBN ergänzen und deine Coverdatei mit dem Barcode … versehen"; "Die ISBN und der Barcode sind verpflichtende Bestandteile des Impressums von Titeln, die veröffentlicht werden."
- Change to: rebuild with `BOOK_ISBN=978-3-…` and `python3 textbook/print/cover.py --pages 646 --isbn 978-3-… --spine-mm <myBoD value>`. Make sure the cover's barcode box no longer contains the placeholder text: either it holds the EAN-13 barcode or it is left plain white if BoD inserts the barcode itself.

### M2. The copyright page overflows: the ISBN line falls alone onto p. 5 (a recto)
- Where: textbook/print/book.css:46 (`.copyright { … padding-top: 88mm; … }`); PDF pp. 4–5
- Text now: p. 4 holds the imprint down to "Print: Libri Plureos GmbH, Friedensallee 273, 22763 Hamburg"; p. 5 holds only "ISBN: [to be added …]"; p. 6 is blank.
- Problem: VERIFIED WRONG (layout). The imprint, ISBN included, belongs on page 4. A one-line page 5 also looks like an error. Adding the real ISBN will not fix it, because the line is the same length.
- Evidence: rendered p. 4 at 60 dpi: the text block ends at the foot of the page and the ISBN line is pushed onto the next page. BoD starter kit (URL above): "Wir empfehlen, das Impressum auf der vierten Buchseite einzusetzen", and it asks for space to be left at the top of p. 4 for the FSC logo, which BoD prints in automatically.
- Change to: in book.css, `padding-top: 70mm;` (or about 65 mm). This still leaves the top of p. 4 free for BoD's FSC mark and keeps all of the imprint, ISBN included, on p. 4. Check after rebuilding that p. 5 has gone and that the TOC still starts on a recto (p. 5, or p. 7 with a blank p. 6).

### M3. The process statement in the preface will be false after this review round
- Where: textbook/chapters/ch00-preface.md:52 (printed p. 13); also the copyright page date range, textbook/print/build.py:137
- Text now: "Three such review rounds were run. In the last, about 2,600 statements were checked against their sources; the errors and out-of-date statements it found were corrected before printing."
- Problem: INCONSISTENT / overclaim risk. This is a fourth independent review round, of the same kind ("separate instances, which had not seen the earlier work"). Once its fixes are applied, "Three" and "the last … about 2,600" no longer describe the process. A disclosure that misstates the checking process is exactly what the brief asks us to catch. Likewise, "Web sources were checked between 20 October and 26 November 2026" on the copyright page must cover the dates of any fixes applied after 26 November.
- Evidence: textbook/delivery/README.md item 12 ("Third independent review … 22–26 November 2026 … about 2,610 claims"); review4/BRIEF.md (fourth review, 26 November 2026).
- Change to: "Four such review rounds were run. In the third, about 2,600 statements were checked against their sources; the fourth, a final check before printing, re-examined the facts in every chapter. The errors and out-of-date statements these rounds found were corrected before printing." Also update the copyright-page date range to the date the last fix was checked.

### M4. Index: the Contents page is indexed, and several entries point to pages about a different meaning of the word
- Where: textbook/print/make_index.py:41 (`main_range`); textbook/print/index_entities.txt:16, 17, 22; glossary-derived entries "bias (in a neuron)", "epoch", "circuit", "resolution", "environment (reinforcement learning)", "momentum", "feature"
- Text now (index, pp. 639–645), for example:
  - "alignment, 7, …", "data centre, 7, …", "interpretability, 7, …", "large language model (LLM), 7, …", "risk, 7, …", "scenario, 7, …"
  - "bias (in a neuron), 47, 48, 51, 58, 331, 362, 364, 375"
  - "epoch, 11, 59, 133, 135, 136, 138, 147, 249"
  - "circuit, 90, 120, 212, 227, 229, 233, 411, 451"
  - "resolution, 87, 193, 448, 449, 465, 469"
  - "Dartmouth workshop (1956), 17, 18, 44, 343, 464"
  - "environment (reinforcement learning), 19, 21, 112, …"; "momentum, 21, …"; "feature, 17, …"
- Problem: VERIFIED WRONG.
  1. `main_range` starts at the first page whose first 80 characters contain " Preface ", and that page is the Contents page (p. 7). Six entries therefore cite p. 7, where the word appears only in a chapter title.
  2. Plain string matching mixes senses. In "bias (in a neuron)", pp. 331, 362, 364 and 375 are about detector bias, algorithmic bias and automation bias. In "epoch", pp. 11, 133, 147 and 249 are about Epoch AI, the organisation. In "circuit", pp. 212, 227, 229 and 233 are chip circuits and p. 451 is the "Third Circuit" court. In "resolution", p. 87 is anaphora resolution, p. 193 grid resolution, p. 448 UN resolutions and p. 465 forecast-question resolution. In "Dartmouth workshop", p. 343 is Dartmouth College's Therabot trial. On pp. 19 and 21 "environment" is from the AI definitions, not RL. On p. 21 "momentum" is "gained significant momentum". On p. 17 "feature" is "feature of intelligence".
- Evidence: the 30-entry sample (every 15th entry, 134 page references) found the term on all 134 pages, once U+2010 line-end hyphens are joined and abbreviations and patterns such as Qwen and MSA are allowed for. But 4 of the 8 references for "bias (in a neuron)" are to a different sense, and "Copyright cases" (8 references) points to general mentions of copyright (pp. 10, 357, 358 are not cases). The targeted checks listed above were done with page-text extracts.
- Change to:
  1. In make_index.py:41 take the start page as the first page whose text *starts with* "Preface", by deleting `or " Preface " in t[:80]`.
  2. In index_entities.txt, change line 22 to `Epoch AI | Epoch AI` (drop the bare `Epoch` pattern) and line 17 to `Dartmouth workshop (1956) | Dartmouth workshop | Dartmouth proposal | Dartmouth summer`.
  3. For the glossary entries "bias (in a neuron)", "circuit", "resolution", "environment (reinforcement learning)", "momentum" and "feature", either restrict them by hand to the chapter page ranges where the technical sense is used (bias 47–58; circuit 90, 120, 411; epoch 59; momentum 60–64; environment 112 onwards in Ch 3–5; drop "resolution", or limit it to 465–469 under the heading "resolution (of a forecast question)"), or drop them. Then rebuild, regenerate the index and rebuild again.

## SHOULD change

### S1. The back-cover disclosure leaves out the main caveat and suggests full checking
- Where: textbook/print/cover.py:214–218
- Text now: "Most of the text of this book was generated by the AI models Claude Opus 5.5 and Claude Fable 5.2, working under the author's direction, and checked by the same models against its cited sources. The preface explains how it was made."
- Problem: UNCLEAR. The back cover is what a buyer reads. "Checked … against its cited sources" reads as though everything was checked. The preface is more careful: it reports checks of samples, says that checks "reduce that risk but do not remove it", and says that "no independent human expert has reviewed the whole book". That last fact is missing from the cover.
- Change to: "Most of the text of this book was generated by the AI models Claude Opus 5.5 and Claude Fable 5.2, working under the author's direction, and fact-checked by the same models. No independent human expert has reviewed it. The preface explains how it was made." (This fits the same five lines.)

### S2. Copyright line on a largely AI-generated text
- Where: textbook/print/build.py:140 (p. 4)
- Text now: "© 2026 Calmy Jane. All rights reserved."
- Problem: LEGALLY SENSITIVE. German law (§ 2(2) UrhG, "persönliche geistige Schöpfungen") and US law protect only human authorship. The book itself reports (Ch 13, p. 451) that in Thaler v. Perlmutter the D.C. Circuit held on 18 March 2025 that the Copyright Act requires human authorship. A blanket claim over text the preface says the author "did not write" may overstate the rights held. The delivery README already lists "take legal advice on the copyright line" as an open to-do.
- Change to (pending legal advice): "© 2026 Calmy Jane (selection, arrangement, editing and human-authored contributions). All rights reserved to the extent permitted by law."

### S3. Scope of the disclosure: figures, tables, index and cover
- Where: textbook/print/build.py:24–28 and :138; ch00-preface.md:52
- Text now: "Figures drawn for this edition." / "Most of the text of this book was generated by AI …"
- Problem: UNCLEAR. If, as the build scripts suggest (`figs_chNN.py`, `make_index.py`, `cover.py`), the figures, the index and the cover design were also produced by the same AI agents, the disclosure should say so rather than speak only of "text".
- Change to (if accurate): "Figures, tables, index and cover were also produced by the same AI models under the author's direction."

### S4. "Every factual statement is sourced" is stronger than the process supports
- Where: ch00-preface.md:5 (p. 9)
- Text now: "Every factual statement is sourced."
- Problem: UNCLEAR / slight overclaim. The sourcing audit worked per paragraph (README item 10), and the preface itself exempts unlabelled worked examples and the author's calculations.
- Change to: "Every paragraph that states a fact cites its sources."

### S5. Large blank gaps in mid-chapter pages (boxes and figures that do not fit, so they are pushed to the next page)
- Where (printed pages, approximate share of the text block left empty): **p. 400 (≈85%, two lines then blank before the ExploitGym box)**, p. 88 (≈75%), p. 114 (≈75%), p. 148 (≈70%), p. 446 (≈65%), p. 487 (≈60%), and about half a page on pp. 74, 200, 342, 379, 384 and 409.
- Problem: production quality. The README says that a layout pass moves figures to fill gaps, but these gaps remain.
- Change to: let the boxes split across pages (`break-inside: auto` for `.box` longer than half a page), or allow the following text to flow ahead of the float on those pages. Check p. 400 first.

### S6. Index structure: silent 8-page cap, duplicate entries, misnamed heading
- Where: textbook/print/make_index.py:20 (`MAX_PAGES = 8`); index_entities.txt:16
- Problem: UNCLEAR. 119 of 461 entries reach the cap and silently drop pages. For example, "OpenAI", "Anthropic" and "China" each list 8 pages, although each appears on dozens. The cap is not stated anywhere for the reader. There are also duplicate entries: "AUC" and "area under the curve (AUC)"; "time horizon", "time horizon (50%)" and "50% time horizon". The heading "Copyright cases" collects every mention of the word "copyright".
- Change to: add a note under the index heading: "For frequently mentioned names and terms, the index lists the first page and the pages with the most mentions." Merge the duplicates into "see" cross-references (for example "AUC, see area under the curve"). Rename the heading to "copyright".

### S7. GPT-5.6 Sol: released or unreleased? (cross-chapter)
- Where: textbook/chapters/ch12.md:96 vs ch13.md:306
- Text now: ch12: "OpenAI disclosed that GPT-5.6 Sol (…) and an unreleased model had escaped …"; ch13: "In June 2026 OpenAI limited its unreleased GPT-5.6 Sol to a small group of partners approved by the US government"
- Problem: INCONSISTENT. Chapter 12's "and an unreleased model" implies that GPT-5.6 Sol was released, while Chapter 13 calls it unreleased.
- Change to (ch12:96): "OpenAI disclosed that GPT-5.6 Sol (available only to a small group of approved partners; not to be confused with GPT-6 Sol, launched on 22 September 2026) and an internal-only research model had escaped …"

### S8. "First use of export controls" stated as fact in Ch 7, attributed in Ch 13 and 14
- Where: ch07.md:135
- Text now: "in the first use of export controls to block access to an AI service"
- Problem: INCONSISTENT. ch13.md:144 has "in what law firms described as the first known use …", and ch14.md:167 has "Law-firm analyses described it as the first known use …".
- Change to: "in what law firms described as the first known use of export controls to block access to an AI service"

### S9. Stale "As of October 2026" qualifiers in a book current to late November
- Where: ch13.md:183; ch06.md:231
- Text now: "As of October 2026 the federal case remained open"; "As of October 2026, research groups were still examining the paper and the Lean code"
- Problem: OUTDATED framing. The copyright page claims currency to late November 2026.
- Change to: re-check both and write "As of late November 2026 …" if they still hold (the chapter reviewers for Ch 6 and Ch 13 should confirm the facts).

## Could not verify
- BoD's maximum page count for an A5 paperback on white paper (646 pages). No official figure was found. Check in myBoD when the project is created.
- PDF/X-4 conformance. The PDF claims it but has not been preflighted (README says so). Run the myBoD preflight.
- The final spine width from myBoD. The calculated value below matches BoD's formula, but BoD's own value overrides it (`--spine-mm`).

## Checked and confirmed
- **Spine:** 646 pages = 323 leaves × 0.12 mm = 38.76 mm, + 0.6 mm = 39.36 mm. The cover PDF is 978.973 × 623.622 pt = 345.36 × 220.0 mm = 5 + 148 + 39.36 + 148 + 5 by 5 + 210 + 5. ✔ (cover.py uses `weiss` = 0.012 cm per leaf.)
- **Page count:** 646 pages (even), not the ~626 given in the brief. The cover was built for 646 (`cover.py --pages` default 646; BUILD-INFO `pages: 646`).
- **Text running off the page:** none. Across all pages, word boxes stay within x = 43–363 pt (versos) and 57–377 pt (rectos) and y = 19–574 pt. The only words outside the text block are the hanging reference numbers in the reference list (pp. 529–637, at x = 28 or 43 pt), which is intended, and they are about 10 mm from the trim.
- **Figures:** all 46 figures (vector, embedded SVG) were rendered and inspected. None is broken, clipped or blank. Dense ones (Fig. 7.2, 13.2) were checked at 110 dpi and their labels are legible.
- **Fonts:** all fonts are embedded in the interior (12) and the cover (8).
- **TOC:** all 18 targets checked (Preface 9, Chapters 1–14 at 17/47/79/123/153/185/221/257/287/321/355/391/427/463, Glossary 497, References 529, Index 639), all correct. Part pages are at 15, 255, 353 and 461.
- **Title, half-title and imprint:** half-title p. 1, title p. 3 (title, subtitle, author), imprint p. 4. The imprint wording matches BoD's template ("Verlag: BoD · Books on Demand, Überseering 33, 22297 Hamburg, bod@bod.de"; "Druck: Libri Plureos GmbH, Friedensallee 273, 22763 Hamburg"; DNB notice), per the BoD starter kit. The top of p. 4 is left free for the FSC mark.
- **Disclosure consistency:** the preface, copyright page, back cover and README agree on the models (Claude Opus 5.5, Claude Fable 5.2), on "most of the text" and on the author's role. The preface's "about 2,600 statements" matches README's 2,610. The preface's "more than 1,200 references" matches the PDF, whose reference list runs to no. 1,293. (README's "1,244" is stale but not printed.)
- **Cut-off:** "current to late November 2026" (copyright page), "November 2026" (preface), "as of late November 2026" (ch13:5), and "when this book went to press" (Getty appeal, ch13:250) are consistent. Table 3.9 is explicitly limited to the end of October, and the November releases follow in the text (ch03:449).
- **Cross-chapter facts that agree:**
  - GPT-6 Astra released 3 Sept 2026 (ch04:122) and GPT-6 Sol 22 Sept (ch12:96), consistent with "Sep 2026" (ch03 table) and "In September" (ch01:244, ch12:277).
  - GPT-6.1 Astra withheld on 28 Sept (ch12:277, ch14:167).
  - Claude Opus 5.5 in Sept 2026 (ch01:244, ch03 table). Claude Fable 5.2 / Mythos 5.2 on 9 Nov (ch01:255, ch03:449, ch04:229).
  - ClockBench 83.3% (Gemini 4 Argon, 25 Oct) and 87.8% (Fable 5.2 Max) in both ch01:255 and ch04:229.
  - Commerce licence for Fable 5 / Mythos 5 on 12 June, lifted 30 June (ch07:135, ch13:144, ch14:167). Mythos 5 released in June (ch03, ch11:215).
  - Digital Omnibus in force 27 July 2026, Regulation (EU) 2026/1744 (ch09:233, ch13:3, ch13:52, Fig. 13.2).
  - OpenAI's training pause announced 18 Aug after the July Hugging Face incident (ch12:277/284, ch14:167).
  - METR: Mythos Preview "at least 16 hours" / about 17 hours, and series stopped in Sept 2026 (ch04:237, ch05:175, ch14:109).
  - Kimi K3 2.8T/104B active, DeepSeek-V4-Pro 1.6T/49B active, Muse Spark Open 816B/42B active, 15 Oct (ch02, ch03, ch07).
  - Epoch compute: GPT-6 Astra 9.4 × 10^26 FLOP ≈ 2.5 × GPT-4.5's 3.8 × 10^26 ≈ 3,000 × GPT-3's 3.14 × 10^23 (ch03:451, ch04:122/251). Arithmetic ✔.

## Tally
- Claims and checks: 30 index entries (134 page references) + 12 targeted index entries; 18 TOC targets; 46 figures; 646 pages scanned for overflow and gaps; spine and cover dimensions; 4 disclosure locations; about 25 cross-chapter facts.
- Confirmed: TOC 18/18; figures 46/46; spine ✔; cross-chapter facts 23/25; index sample 130/134 page references in the right sense.
- Wrong: 4 MUST items (ISBN/barcode placeholders, imprint overflow, review-round count, index page-7 bug and mixed senses). Cross-chapter inconsistencies: 2 (S7, S8).
- Outdated: 2 (S9).
