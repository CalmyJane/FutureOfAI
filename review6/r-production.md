# Review 6: whole-book and production checks

Scope: the AI-authorship disclosure (preface, copyright page, back cover); front matter; the interior PDF `textbook/delivery/understanding-ai_A5_interior.pdf` (636 pages, built 27 Nov 2026 02:28 UTC); the cover `textbook/delivery/understanding-ai_cover_A5_PB.pdf`; and cross-chapter consistency of repeated facts.

Method: `pdftotext` (raw and `-layout`); a pdfplumber scan of every page for text bounding boxes, blank vertical space above the source line, and grey box rectangles that touch the top or foot of the text block; rendered contact sheets of all 46 figure pages and of every page the scan flagged; an automatic check of 30 randomly sampled index entries (seed 6) against the raw text of each cited page, with misses checked by hand; and grep across `ch*.md` for repeated facts.

Known and accepted, not reported again: the ISBN placeholder and barcode box; the model list "chiefly…"; blank space before full-page figures at about pp. 84 and 432 (see S1 for their current state).

## Verdict

**Ready to print from a production standpoint.** I found nothing that must change. No text runs off the page, all 46 figures render, the index sample is correct (30 of 30), the spine matches 636 pages exactly, and no repeated fact contradicts itself across chapters. The disclosure is clear and honest. The SHOULD items are layout polish, plus one sentence in the disclosure that stays true only if this round's findings are actually applied.

## MUST change before printing

None.

## SHOULD change

### S1. Blank gaps of a quarter to two-fifths of a page before full-page figures (9 pages)
- Where: PDF pp. 37, 62, 66, 121, 180, 183, 225, 326, 464 (layout from `textbook/print/build.py`)
- Text now: the body text ends well above the source line. The blank depth, measured from the last text line to the source line, out of a text block of about 500 pt: p. 37 ≈ 149 pt; p. 62 ≈ 121; p. 66 ≈ 160; p. 121 ≈ 115; p. 180 ≈ 199; p. 183 ≈ 177; p. 225 ≈ 203; p. 326 ≈ 199; p. 464 ≈ 135. On each, the next page starts with a full-page figure (Figures 1.3, 2.5, 2.6, 4.1, 6.1, 6.2, 7.2, 10.2, 14.2).
- Problem: UNCLEAR (layout). Gaps of 4 to 7 cm look like a missing block to a reader. The worst are pp. 180, 225 and 326, each about 40% empty.
- Accepted pages: p. 84 is now full (Figure 3.2 sits on it). **p. 434** (≈ 350 pt, about 70% of the text block, empty before Figure 13.2 on p. 435) is the accepted "~432" case. If it was smaller before, it has got worse.
- Change to: let the following paragraph(s) flow into the gap and float the figure to the top of the next page. Alternatively, narrow the "move figure to fill gap" pass so that it also tries moving the figure one page later. No text change.

### S2. Table 11.3 is set in six narrow columns and runs over three pages
- Where: textbook/chapters/ch11.md:213–227 (PDF pp. 370–372)
- Text now: "Table 11.3: The best-documented containment incidents of 2026 in tests of frontier models…"
- Problem: UNCLEAR (layout). The last column is about 2 cm wide. One row (the Hugging Face / OpenAI incident) fills the whole of p. 371 at two or three words per line, and the table continues on p. 372. It is hard to read as a table.
- Change to: drop or merge a column (for example, merge "Setting" into "Developer and models"), or set the long "Real-world effect" text as numbered notes under the table. The text needs no other change.

### S3. The disclosure's "corrected before printing" holds only if this round is applied
- Where: textbook/chapters/ch00-preface.md:52
- Text now: "The errors and out-of-date statements these rounds found were corrected before printing, except where a finding was judged on re-checking to be mistaken."
- Problem: UNSUPPORTED (conditional). This is accurate only if every MUST item from review 6 and every wrong or outdated SHOULD item is applied, or explicitly rejected after re-checking, before the PDF is rebuilt. If some are deferred, the sentence overclaims.
- Change to: either apply all of them, or write: "Most errors and out-of-date statements these rounds found were corrected before printing; the rest were judged on re-checking to be mistaken or minor."

### S4. Contents: Chapter 14's title wraps and leaves its dot leader alone on a line
- Where: PDF p. 5 (generated TOC); title from textbook/chapters/ch14.md:1
- Text now: "Chapter 14: Forecasting the Next Ten Years: Methods, Scenarios and Open Problems" / next line: ". . . . 451"
- Problem: UNCLEAR (typographic). It is the only TOC entry that breaks this way.
- Change to: allow the TOC entry to wrap with a hanging indent so that the page number follows the second line of the title ("…Scenarios and / Open Problems . . . 451"), or use a slightly smaller TOC font.

### S5. Imprint: use BoD's exact imprint text from myBoD
- Where: textbook/print/build.py:143
- Text now: "Publisher: BoD · Books on Demand, Überseering 33, 22297 Hamburg, bod@bod.de / Print: Libri Plureos GmbH, Friedensallee 273, 22763 Hamburg"
- Problem: UNSUPPORTED (could not confirm the wording). BoD's own publications give the company as "Books on Demand GmbH, Überseering 33, 22297 Hamburg" (BoD press brochure 2025, https://www.bod.de/bodfiles/GLOBAL-Storage/documents/press-documents/bod-press-brochure-2025.pdf). The line omits "GmbH". I could not confirm the printer line against an official BoD template. The mandatory imprint text depends on the BoD contract model, so it should be copied from myBoD.
- Change to: paste the imprint block myBoD generates for this project. At minimum, write "BoD · Books on Demand GmbH".

## Could not verify

- **Outer margin of the reference numbers.** On every even References page (pp. 518–626) the hanging reference numbers start 28.3 pt (10.0 mm) from the trim edge. Body text everywhere stays at least 14.8 mm from the outer edge and 15 mm on the right. 10 mm is probably within BoD's safe zone, but the myBoD preflight should confirm it.
- The exact BoD imprint wording and the Libri Plureos address (S5).
- Whether p. 434's gap changed since the earlier build. Earlier review folders are excluded by the brief, so I could not compare.
- PDF/X conformance. Not tested here; it needs the printer's preflight, as `delivery/README.md` already says.

## Checked and confirmed

- **Disclosure, three places.** Preface "How the book was made" (pp. 10–11), copyright page (p. 4) and back cover all say that most of the text was generated by AI, name the models and Anthropic, say that checking was done by the same models, and say "No independent human expert has reviewed it." The preface adds that the author did not write most sentences, that the reviews were AI instances, that unreadable sources were logged as unverified, and that "every review round found quotations that did not match their sources." This is clear and not overclaimed, except S3. The copyright claim is limited to "selection, arrangement, editing and human-authored contributions", which fits the disclosure (legal advice is already on the to-do list).
- **Front matter order.** Half-title p. 1, blank p. 2, title p. 3 (title, subtitle, author), copyright p. 4, contents p. 5, blank p. 6, preface p. 7. Chapters and part titles start on recto pages, with blank versos at 12, 14, 146, 214, 250, 280, 314, 346, 380, 450, 484 and 628.
- **TOC page numbers.** All 22 entries checked against the pages: Part pages 13, 145, 249, 345, 449; Chapters 1–14 at 15, 43, 75, 117, 147, 179, 215, 251, 281, 315, 347, 381, 415, 451; Glossary 485; References 517; Index 629. Printed folios equal PDF page numbers.
- **No overflow.** The rightmost glyph on any page is at x = 377 pt (15 mm from the trim), and no body text falls below the source line.
- **Figures.** 46 captions in the PDF and 46 image references in the chapters. A contact sheet of all 46 figure pages shows every figure drawn, none clipped or blank.
- **Boxes.** Ten long boxes continue across pages (pp. 38–39, 72–73, 142–143, 211–212, 238–239, 245–246, 268–269, 375–376, 396–397, 445–446). This is normal for boxes of this length. No box heading sits alone at a page foot: the two closest cases (Debate boxes on pp. 238 and 445) carry the heading plus two lines.
- **Index, sample of 30 entries, all correct.** SWE-bench, machine learning, tool use, AI agent, kernel (convolutional), soft binding, distillation, attribution graph, algorithmic efficiency, correlated failure, RoPE, METR, Huawei, sliding-window attention, scheming, GPT-3, ECMWF, sovereign AI, AUC, export control, KL penalty, synthetic media, combinatorial explosion, scalable oversight, workflow (agentic), influence operation, linear probe, Llama, pooling, AI tutor. Every listed page contains the term. The apparent misses were the hyphenated compounds "machine-learning", "AI-agent" and "attribution-graph", "RoPE" without its expansion, and the caption "export-control" on p. 226. No index entry or page list is hyphenated at a line end, and the index text has no U+2010 or soft hyphens. The body text's U+2010 characters are ordinary end-of-line hyphenation; the only mid-line one is the name Sanchez-Gonzalez in the References.
- **Spine.** 636 pages = 318 leaves × 0.12 mm = 38.16 mm, + 0.6 mm = **38.76 mm**. The cover sheet is 977.272 pt = 344.76 mm = 5 + 148 + 38.76 + 148 + 5. The guide PDF states "spine 38.76 mm". The spine text sits inside the safe zone.
- **Preface counts.** "More than 1,200 references": the list ends at 1,314 (p. 627). "Fourteen chapters… five parts" is correct.
- **Cross-chapter facts, all consistent.**
  - GPT-3: 175 billion parameters and 300 billion tokens (ch01, ch02, ch03, ch04).
  - METR time horizon: seven-month doubling (2019–early 2025) in ch01, ch04, ch14; 129 days since 2023 and 188 since 2019 in ch04, ch05, ch14; Claude Opus 4.6 at about 12 h (CI 5–61 h) in ch04, ch05, ch14; Mythos Preview at "at least 16 hours" (data file about 17) in ch04, ch05, ch14.
  - ChatGPT at 1.2 billion weekly users on 29 Sept 2026 (ch01, ch03); ch10's 800 million is dated "at the time" (Oct 2025).
  - IEA data-centre electricity: 485 TWh in 2025 and about 950 TWh (945) in 2030 (ch07, ch14).
  - EU AI Act: in force 1 Aug 2024; GPAI duties 2 Aug 2025; the Digital Omnibus moved high-risk dates to 2 Dec 2027 and 2 Aug 2028, in force 27 Jul 2026 (ch08, ch09, ch10, ch13).
  - ClockBench: Gemini 4 Argon at 83.3% on 25 Oct; Claude Fable 5.2 Max at 87.8% versus Gemini 4 Carbon at 85.0% in late November (ch01, ch04).
  - Model release months: GPT-6 Astra on 3 Sept 2026; Opus 5.5 in Sept 2026; Gemini 4 Argon in Sept and Carbon on 28 Oct, generally available 10 Nov; Fable 5.2 on 9 Nov (ch01, ch03, ch04).
  - Nobel prizes 2024 (ch01, ch06); Dartmouth proposal 31 Aug 1955 (ch01, ch14); Bletchley, 28 countries plus the EU (ch13); SB 53 signed 29 Sept 2025 and in effect 1 Jan 2026 (ch13).

## Tally

Production and consistency claims checked: 112 (22 TOC entries, 30 index entries with 140 page references, spine, figure count, 46 figure pages, 636 pages scanned for overflow, gaps and boxes, about 25 cross-chapter facts, 3 disclosure texts). Confirmed: 107. Wrong: 0. Outdated: 0. Layout or wording issues: 5 (S1–S5).
