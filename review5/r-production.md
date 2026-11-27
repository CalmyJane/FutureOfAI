# Fifth review: whole-book and production checks

Scope: the AI-authorship disclosure (preface, copyright page, back cover), the front matter and imprint, the PDF interior (`textbook/delivery/understanding-ai_A5_interior.pdf`, 632 pages, built 26 Nov 2026 23:38 UTC), the cover (`understanding-ai_cover_A5_PB.pdf`), a sample of the index, and cross-chapter consistency of the most repeated facts. The ISBN placeholder is known and accepted, so it is not reported here.

## Verdict

**Ready to print after one fix to the disclosure text, plus some optional layout clean-up.**

- The disclosure is clear and honest. Its tone is right, and it does not claim any human expert review. One sentence will be false once this fifth round is applied: it says four review rounds were run and that the fourth was the final check.
- The production is sound:
  - No text runs off the page.
  - No figure is broken.
  - Every printed folio matches its PDF page.
  - All 17 table-of-contents page numbers are correct.
  - The 30 sampled index entries are all correct, and an automated pass over all 455 page-number entries found nothing that points to a wrong page.
  - The cover spine matches the page count exactly.
- The remaining layout faults are cosmetic: box headings stranded at the foot of a page, and two pages left about two-thirds empty in front of full-page figures.

## MUST change before printing

### M1. The preface undercounts the review rounds and calls the fourth round "final"
- Where: textbook/chapters/ch00-preface.md:52 (printed on page 11)
- Text now: "Four such review rounds were run. In the third, about 2,600 statements were checked against their sources; the fourth, a final check before printing, re-examined the facts in every chapter."
- Problem: VERIFIED WRONG once this round is applied. The fifth round (this one, `review5/`) is being run and its corrections applied before printing. The printed statement would then misstate how the book was checked, which is the one thing the disclosure exists to describe accurately.
- Evidence: `review5/BRIEF.md` (26 November 2026): "Fifth review … Your review is the last check before the author prints it."
- Change to: "Five such review rounds were run. In the third, about 2,600 statements were checked against their sources; the fourth and fifth, the last before printing, re-examined the facts in every chapter."

## SHOULD change

### S1. "Corrected before printing" is absolute
- Where: textbook/chapters/ch00-preface.md:52
- Text now: "The errors and out-of-date statements these rounds found were corrected before printing."
- Problem: UNSUPPORTED (slight overclaim). Review rounds also raise findings that are judged mistaken or are deliberately left as they are. The sentence says every finding led to a correction, and the reader cannot check that.
- Change to: "The errors and out-of-date statements these rounds found were corrected before printing, except where a finding was judged on re-checking to be mistaken."

### S2. The disclosure points readers to logs they cannot see, and gives no contact for corrections
- Where: textbook/chapters/ch00-preface.md:52 and :56
- Text now: "claims that rest on them are listed as unverified in the project's working logs." / "Corrections are welcome, and responsibility for the published text, including its errors, lies with the author."
- Problem: UNCLEAR. The working logs are not published, so this tells readers something is listed somewhere they cannot reach. "Corrections are welcome" gives no address. The only email in the book is BoD's.
- Change to: "… claims that rest on them were recorded as unverified in the project's working logs, which are not published." Then add a contact for corrections (an email address or web page) after "Corrections are welcome", or drop the invitation.

### S3. Two different wordings of "no independent human expert review"
- Where: back cover (textbook/print/cover.py:217–219): "No independent human expert has reviewed it." Copyright page (textbook/print/build.py AI_NOTE) and preface (ch00-preface.md:54): "No independent human expert has reviewed the whole book."
- Problem: INCONSISTENT. "The whole book" implies that an expert has reviewed part of it. Nothing in the book says that happened, and `textbook/delivery/README.md` still recommends "A human expert review … before publication". The back-cover wording is the more accurate one.
- Change to: "No independent human expert has reviewed it." (copyright page). "At the time of printing, no independent human expert has reviewed the book." (preface). If an expert did review some chapters, say which ones instead.

### S4. Box headings stranded at the foot of a page
- Where (printed pages):
  - p. 60: "Going deeper: What frontier training recipes looked like, 2023–2026" (ch03)
  - p. 172: "Debate: Can prompt injection be solved inside the model?" (ch05)
  - p. 237: "Case study: The 'DeepSeek moment', January 2025" (ch07)
  - p. 238: "Concept: Open-weight is not the same as open source" (ch07)
  - p. 327: "Going deeper: What makes medical AI evidence strong" (ch10)
- Problem: Layout. On each of these pages the box opens with its heading or frame on the last line, and the whole body continues overleaf. This looks broken in print. Boxes that split with 1–3 body lines at the foot (pp. 53, 236, 333, 397, 443) are acceptable.
- Change to: keep the box heading with its first lines, e.g. `break-after: avoid` on the box title plus `orphans: 3` inside boxes in textbook/print/book.css, or `break-inside: avoid` for short boxes. Then rebuild and recheck the index and the source lines, because pages may shift.

### S5. Large blank gaps in front of full-page figures
- Where (printed pages, blank share of the text area): p. 84 (about 65%, in front of Figure 3.2 on p. 85), p. 432 (about 60%, in front of Figure 13.2), and pp. 37, 180, 183, 223, 297, 473 (about 30–35% each).
- Problem: Layout. When a figure will not fit, the text stops and the rest of the page stays empty. On pp. 84 and 432 this reads as a mistake.
- Change to: let the following text flow on past the figure (float the figure to the next page top), or move the figure's anchor paragraph earlier in ch03 and ch13. At the very least, fix pp. 84 and 432.

### S6. The Chapter 14 table-of-contents entry leaves its page number on a line of its own
- Where: Contents, p. 5: "Chapter 14: Forecasting the Next Ten Years: Methods, Scenarios and Open Problems" followed by ". . . 449" alone on the next line.
- Problem: Layout. Every other entry fits on one line.
- Change to: wrap the title inside the entry (hanging indent, leader on the second line), or use a shorter TOC title, e.g. "Chapter 14: Forecasting the Next Ten Years".

### S7. DeepSeek-V3 GPU-hours described differently in Chapters 3 and 7
- Where: textbook/chapters/ch03.md:361
- Text now: "That is roughly 5% of the 2.79 million GPU-hours the company reported for training its base model, DeepSeek-V3"
- Problem: INCONSISTENT. Chapter 7 (ch07.md:218) correctly says the 2.788 million total includes context extension and post-training (124,000 hours). Pre-training of the base model alone was about 2.66 million.
- Change to: "That is roughly 5% of the 2.79 million GPU-hours the company reported for the full training of DeepSeek-V3"

### S8. Index: "τ-bench" is filed under B
- Where: Index, p. 625, between "batch normalisation" and "benchmark".
- Problem: Minor. A reader looks for it under T or under symbols at the head of the index.
- Change to: file it under T (as "tau-bench, see τ-bench") or under "0–9 and symbols".

## Could not verify

- "In the third, about 2,600 statements were checked against their sources" (preface). The earlier review logs are out of bounds for this review.
- The cover spine will be replaced by BoD's own figure when the project is set up (`--spine-mm`). Recheck it then.
- The interior has not been through a PDF/X preflight (the README says the same). Run BoD's upload check.

## Checked and confirmed

- **Disclosure:**
  - All three places name the models (Claude Opus 5.5, Claude Fable 5.2, made by Anthropic).
  - All three say that most of the text was AI-generated and that the same models checked it.
  - All three say there was no independent human expert review, and they point to the preface.
  - The preface's "How the book was made" is candid. It covers what the author did and did not do, the limits of online checking, the conflict of interest (Anthropic models describing Anthropic), and that every round found misquotations.
  - "The author" is defined (p. 10) as the book as directed by Calmy Jane, with calculations carried out by the AI agents.
  - No statement claims human fact-checking.
- **Front matter order:** half-title (p. 1), blank (p. 2), title page (p. 3), copyright page (p. 4), contents (p. 5), blank (p. 6), preface (p. 7). Every chapter and part opens on a recto.
- **Imprint:** the publisher line (BoD · Books on Demand, Überseering 33, 22297 Hamburg) and the printer line (Libri Plureos GmbH, Friedensallee 273, 22763 Hamburg) match BoD's current imprint template ([myBoD starter kit](https://www.bod.ch/bodfiles/DE-Storage/documents/myBoD-starter-kit.pdf); address confirmed in [BoD press brochure 2025](https://www.bod.de/bodfiles/GLOBAL-Storage/documents/press-documents/bod-press-brochure-2025.pdf)). The DNB notice and the copyright line are in order.
- **Page numbers:** all 612 numbered pages carry a folio equal to their PDF page number. All 17 contents page numbers land on the right headings (Preface 7 … Index 625).
- **Overflow:** a rendered ink-bounds check of all 632 pages found no text or figure beyond the standard margins. The reference-list numbers hang about 4 mm into the margin, which is deliberate and safe.
- **Figures:** all 58 figure pages were rendered and inspected. All are intact and legible, with no missing glyphs or clipped labels at review resolution.
- **Index sample of 30, all correct:** overfitting, Digital Omnibus, scenario, expert system, SGD, pooling, transformer block, scaling law, representation learning, layer normalisation, Artificial Hivemind, HBM, softmax, difference-in-differences, reliability, 50% time horizon, cyber operations, benchmark, goal misgeneralisation, HPL, task-based framework, deskilling, GPT-4, linear probe, algorithmic bias, N-version programming, AlphaEvolve, query/key/value, Dartmouth workshop, implied truth effect. The automated pass over 455 entries found 30 with a page lacking the exact headword. In every case the page has a variant: a hyphenated compound ("linear-attention", "fair-use defence"), an abbreviation (UK, US, IMO, MoE) or the full form ("reinforcement learning with verifiable rewards").
- **Cover:** the sheet is 344.52 × 220.0 mm, so the spine is 344.52 − 10 − 296 = 38.52 mm. That equals 632 / 2 × 0.12 + 0.6 = 38.52 mm. The spine text sits inside its 2.5 mm safe zone, and the barcode field is clear on the back.
- **Reference count:** 1,306 numbered references, so "more than 1,200" (preface) holds.
- **Repeated facts consistent across chapters:**
  - Dartmouth proposal dated 31 Aug 1955 (ch01, ch14).
  - GPT-3: 175 billion parameters, 300 billion tokens, 3.14 × 10^23 FLOP (ch01–04).
  - AlexNet: 60 million parameters; 15.3% / 16.4% top-5 error, with the difference explained (ch01, ch02).
  - ChatGPT released 30 Nov 2022 (ch01, ch03).
  - ChatGPT weekly users: 1.2 billion at DevDay, 29 Sep 2026 (ch01, ch03); 800 million "at the time" in ch10 is correctly dated.
  - IEA data-centre electricity: 485 TWh in 2025 and about 950 TWh (945 in tables) in 2030 (ch07, ch14).
  - METR doubling times: 7 months (ch01), 188 and 129 days (ch04, ch14), with the January 2026 figures of 196/131/89 days explained (ch14).
  - The Mythos Preview horizon of "at least 16 hours" (ch04, ch05).
  - ClockBench: 83.3%, then 87.8% vs 85.0% (ch01, ch04).
  - GPT-6 Astra: September 2026, 9.4 × 10^26 FLOP, about 3,000 × GPT-3 (ch01, ch03, ch04).
  - Fable 5 / Mythos 5 dates and the export-licence episode (ch03, ch07, ch11, ch13, ch14).
  - EU AI Act dates: in force 1 Aug 2024; Art. 5 from 2 Feb 2025; GPAI from 2 Aug 2025; Art. 50 from 2 Aug 2026; Omnibus deferrals to 2 Dec 2027 and 2 Aug 2028 (ch08, ch09, ch10, ch13, ch14).
  - Nobel prizes, October 2024 (ch01, ch06).
- **Not printed, so not counted:** `textbook/delivery/README.md` is stale. It gives 1,244 references (now 1,306), 462 index entries and "46 figures". Update it if it goes to anyone.

## Tally

| Group | Checked | Confirmed | Wrong | Outdated / inconsistent |
|---|---|---|---|---|
| Disclosure and imprint statements | 14 | 10 | 1 (M1) | 3 (S1–S3) |
| Repeated cross-chapter facts | 16 | 15 | 0 | 1 (S7) |
| Index entries (manual sample) | 30 | 30 | 0 | 0 |
| Production checks (folios, TOC, overflow, figures, spine) | 5 groups | 5 | 0 | 0 |
| Layout faults | – | – | – | 4 (S4–S6, S8) |

Totals: 1 MUST, 8 SHOULD.
