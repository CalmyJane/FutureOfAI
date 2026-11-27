# Seventh review: whole-book and production checks

Scope: the AI-authorship disclosure (preface, copyright page, back cover), the front matter, PDF production (text overflow, blank gaps, figures, boxes, index, hyphenation, printed page numbers), the cover spine, and the consistency of repeated facts across chapters.

Files examined: `textbook/delivery/understanding-ai_A5_interior.pdf` (built 27 Nov 2026 03:15 UTC, 638 pages), `textbook/delivery/understanding-ai_cover_A5_PB.pdf` and its `_guides` version, `textbook/print/build.py` (`front_matter`, `AI_NOTE`), `textbook/print/cover.py`, `textbook/print/index.md`, `textbook/print/make_index.py`, `textbook/chapters/ch00-preface.md` and chapters 1–14.

Not reported because they are known and accepted: the ISBN placeholder; the model list "chiefly…"; the imprint text still to be pasted from myBoD; blank space before full-page figures; Table 11.3 running across pages; the wrapped Chapter 14 contents entry.

## Verdict

**Ready to print after one fix: rebuild the PDF from the current sources.** The disclosure is clear, honest and consistent across the preface, the copyright page and the back cover. It does not overclaim human review: it says three times that no independent human expert has reviewed the book. The layout checked clean. No text runs outside the text block on any of the 638 pages. All 46 figures render. None of the 69 boxes has its heading stranded at the foot of a page. The contents page numbers match. All 1,802 index locators were checked mechanically, and 1,799 of them are right. The cover spine matches 638 pages exactly.

The one blocking problem is a process one. The delivered PDF was built before the seventh-review fixes now being committed, so it no longer matches the sources (`check_build.py` fails). The remaining items are small typesetting and consistency fixes.

## MUST change before printing

### M1. The delivered interior PDF is stale: it was built before the seventh-review fixes
- Where: textbook/delivery/understanding-ai_A5_interior.pdf; textbook/delivery/BUILD-INFO.txt
- Text now: `python3 textbook/print/check_build.py` prints "delivery PDF is stale: rebuild with python3 textbook/print/figures.py && python3 textbook/print/build.py" (exit code 1)
- Problem: INCONSISTENT. The PDF is dated 27 Nov 03:15 UTC. Fixes have been committed since then, for example `f6d5611 2026-11-27 09:05 "Seventh review fixes: chapters 3-4"` and `7eab3ed 09:02 "Seventh review fixes: chapter 9"`. Every check in this report was made on the 03:15 build. The index is generated from the laid-out pages (`make_index.py`: "Run after a full build, then build again"), so any change in text length can move index locators, the source line at the foot of each page, and the page count. The page count fixes the spine width.
- Evidence: the `check_build.py` output above; `git log` (read only).
- Change to: after the last chapter fix, run `figures.py`, then `build.py`, then `make_index.py`, then `build.py` again, and confirm that `check_build.py` passes. If the page count is no longer 638, rebuild the cover with `cover.py --pages <N>` (spine = N/2 × 0.12 mm + 0.6 mm) and update "638 pages" in `delivery/README.md`. Then re-run the overflow and index checks described under "Checked and confirmed". Each takes a few seconds with `pdftotext -bbox`.

## SHOULD change

### S1. The preface says every finding was corrected. That is true only once this round's fixes are all in
- Where: textbook/chapters/ch00-preface.md:52
- Text now: "The errors and out-of-date statements these rounds found were corrected before printing, except where a finding was judged on re-checking to be mistaken."
- Problem: UNSUPPORTED (conditional). This is a factual claim about the seventh round as well. It becomes false if any MUST item in `review7/` is left unapplied or is deferred to the "proof-day checks" list.
- Evidence: n/a (it depends on the fix log for this round).
- Change to: either confirm that every review7 MUST item has been applied or explicitly rejected, or soften the sentence to: "The errors and out-of-date statements these rounds found were corrected before printing, except where a finding was judged on re-checking to be mistaken or could not be resolved; the latter are listed in the project's working logs."

### S2. The copyright page and back cover say "fact-checked" without the preface's limits
- Where: textbook/print/build.py:24–29 (`AI_NOTE`); back cover text in textbook/print/cover.py
- Text now: copyright page: "…and fact-checked and reviewed by the same models, working under the direction of the author." Back cover: "…working under the author's direction, and fact-checked by the same models."
- Problem: UNCLEAR, a mild overclaim compared with the preface. The preface (ch00-preface.md:52) says the checks were made "against the cited sources wherever those sources could be read online", and that books, paywalled articles and some websites "could not always be opened". On its own, "fact-checked" implies more. The back cover is the text a buyer reads.
- Evidence: ch00-preface.md:52 as quoted.
- Change to (copyright page): "…and checked against their cited sources, where these could be opened, by the same models, working under the direction of the author." Optional on the back cover, where space is tight: "…and checked against their sources by the same models."

### S3. Hyphenation splits brand and model names at their internal capitals
- Where: PDF pages 35, 93, 95 (twice), 118 ("Deep‐Seek"); 197, 405 ("Deep‐Mind"); 302, 320, 335, 442, 469 ("Chat‐GPT"); 95, 241 ("Muon‐Clip"); 120 ("Web‐Text2"); 126 ("Iso‐FLOP"); 172 ("Agent‐Dojo"); 188 ("Graph‐Cast"); 211 ("Fun‐Search"); 415 ("Exploit‐Gym"); 459 ("Forecast‐Bench"). That is about 22 line ends.
- Text now: for example p. 35: "The Chinese company Deep‐ / Seek reported in December 2024…"; p. 302: "Bisbee and colleagues (2024) asked Chat‐ / GPT…"
- Problem: UNCLEAR (typography). `hyphens: auto` (book.css:28) treats these as compounds. A reader sees a hyphen that is not part of the name ("Chat-GPT", "Deep-Seek"), and this is a book that spells model names exactly. Ordinary word hyphenation (U+2010 at line ends, about 1,745 cases) was checked and is fine. No numbers or URLs are split by soft hyphenation.
- Evidence: `pdftotext -layout` of the 03:15 build. Line ends ending in U+2010 and followed by a capital letter were listed and filtered by hand.
- Change to: in `build.py`, wrap the names in a no-hyphenation span after pandoc runs, for example `body = re.sub(r'\b(DeepSeek[\w.-]*|DeepMind|ChatGPT|MuonClip|WebText2|IsoFLOP|AgentDojo|GraphCast|FunSearch|ExploitGym|ForecastBench|OpenAI|AlphaFold|AlphaEvolve)\b', r'<span style="hyphens:none">\1</span>', body)` (text nodes only), or add `.nohy { hyphens: manual }` and apply it to those words. Re-check the lines that change.

### S4. One index locator is wrong: "International Mathematical Olympiad, 133"
- Where: textbook/print/index_entities.txt:45 (`International Mathematical Olympiad | IMO | Mathematical Olympiad`); textbook/chapters/ch04.md:177
- Text now: ch04.md:177: "The 2024 AIME is a US qualifying exam for the Mathematical Olympiad whose answers are integers that can be checked automatically."
- Problem: VERIFIED WRONG (index) and UNCLEAR (text). The bare pattern "Mathematical Olympiad" sends the IMO entry to p. 133. That page is about the AIME, which qualifies students for the *USA* Mathematical Olympiad (USAMO), not the IMO. The sentence itself is ambiguous for the same reason.
- Evidence: Mathematical Association of America, AMC programme: the AIME is the stage between the AMC 10/12 and the USAMO/USAJMO (https://maa.org/student-programs/amc/).
- Change to: ch04.md:177: "The 2024 AIME is a US qualifying exam for the USA Mathematical Olympiad whose answers are integers that can be checked automatically." Also remove `| Mathematical Olympiad` from index_entities.txt:45, because "USA Mathematical Olympiad" would still match that bare pattern. Then regenerate the index (M1). Note for information: "Alibaba, 78, 131" are found only through "Qwen". That is acceptable, but a "see also Qwen" cross-reference would help.

### S5. The METR doubling time is described differently in Chapters 4 and 14
- Where: textbook/chapters/ch04.md:237; textbook/chapters/ch14.md:98; textbook/chapters/ch05.md:175
- Text now: ch04: "That is above the 16 hours beyond which METR considers its suite unreliable [@metr2026task]. Excluding such points, the horizon has doubled about every 129 days since 2023." ch14: "using the doubling times in METR's later data file, a refit with one more model, added in May 2026: 188 days since 2019 and 129 days since 2023 (range 104–158)".
- Problem: INCONSISTENT. Chapter 4 says the 129-day figure *excludes* the >16-hour point (Claude Mythos Preview, early version). Chapter 14 says it is a refit *with* the model added in May 2026, which is that same Mythos point. Both cannot describe the same fit. METR's page says only "Measurements above 16 hrs are unreliable with our current task suite" and that Mythos Preview (early) was added on 8 May 2026. It does not say whether the trend fit includes it.
- Evidence: https://metr.org/time-horizons/ (read 27 Nov 2026): "Measurements above 16 hrs are unreliable with our current task suite"; the page "is no longer actively updated" (last updated 8 September 2026).
- Change to: check the data file `benchmark_results_1_1.yaml` and state the basis once. If the 129/188-day figures come from METR's fit as published, change ch04 to: "On METR's fit in the same data file, the horizon has doubled about every 129 days since 2023." If they are the author's fit without the Mythos point, change ch14 to: "…using doubling times fitted to METR's later data file without the point above 16 hours: 188 days since 2019 and 129 days since 2023 (range 104–158)", and mark it as the author's calculation.

## Could not verify

- Whether METR's published 129-day and 188-day fits include the Mythos Preview point (see S5). The data file was not opened.
- That the reference count stays "more than 1,200" after the rebuild. It is 1,320 numbered entries in the 03:15 build, so this is safe. `delivery/README.md` still says 1,244 and 462 index entries (index.md has 457). That is outside the book, but worth updating.

## Checked and confirmed

- **Disclosure (preface, ch00-preface.md:50–58).** It says plainly that "Most of this book was generated by AI" and that "The author did not write most of the sentences in it". It says that checking was done by the same models, and that "no independent human expert has reviewed the book". It warns that "AI-written text can be fluent and wrong at the same time" and that every round found mismatched quotations. It names the conflict of interest (Anthropic is both the maker of the models and a subject of the book). Responsibility is placed with the author. The figure of "about 2,600 statements" matches the third-review count (about 2,610). Nothing overclaims human review.
- **Copyright page (PDF p. 4).** The AI note agrees with the preface and points to it. The copyright line is limited to "selection, arrangement, editing and human-authored contributions". The dates (current to late November 2026; sources checked 20 Oct – 26 Nov 2026) agree with preface line 48.
- **Back cover.** It carries a "WRITTEN WITH AI" panel: "No independent human expert has reviewed it. The preface explains how it was made." The blurb's summary of contents matches the parts and chapters (including EU/US/China/UK law and the ten-year scenarios). The preface's "ten research programmes" was checked: Proposals 14.1–14.10 exist.
- **Front matter.** Half-title (p. 1), blank (p. 2), title page (p. 3), copyright (p. 4), contents (p. 5), blank (p. 6), preface from p. 7. All 18 contents entries match the actual start pages (Preface 7 … Index 631). Running heads are correct for every chapter, the Glossary, the References and the Index. Printed folios equal PDF page numbers on every numbered page. Part pages and front pages are unnumbered, as intended.
- **Text overflow.** Every word box on all 638 pages (`pdftotext -bbox`) lies inside the text block (to within 1 pt) and inside the top and bottom bounds. The only exception is the deliberately hanging reference numbers in the References (pp. 519–630), which still sit 10 mm from the trim.
- **Blank gaps.** Every page whose largest empty band exceeds 25% of the text block was listed (about 45 pages). All are chapter or part ends, intentional blanks, or (pp. 37, 66, 84, 180, 183, 225, 326, 436, 466) the page before a full-page figure, which is accepted.
- **Figures.** All 46 figures (1.1–14.4) were found by caption and inspected on contact sheets. Figs 4.2 and 13.2 were checked at 130 dpi. All are vector, with no missing glyphs, clipping or overlapping labels. The Fig. 10.2 inset agrees with the text and Table 10.2 (1,614 devices).
- **Boxes.** All 69 boxes in the sources were found in the PDF. None has its heading in the last five lines of a page. Box splits use cloned borders (`box-decoration-break: clone`).
- **Index.** 457 entries with 1,802 locators were checked mechanically against the page text, allowing for joined hyphenation, abbreviations and plurals. 1,799 match. The ones that do not are p. 133 for the IMO (S4) and two Alibaba pages that are found only through Qwen. A random sample of 30 entries was checked by hand: external validation, Chinchilla, GraphCast, predetermined change control plan, AlexNet, Anthropic, τ-bench, loss of control, automation bias, general-purpose AI model, multiple sequence alignment, algorithmic monoculture, latent diffusion, dangerous-capability evaluation, AI governance, attention head, Hugging Face, heuristic, ambient scribe, deliberative alignment, attrition, Meta, high-bandwidth memory, Alibaba, tensor core, mixture of experts, calibration, data leakage, parameter, parallel test-time compute. All are correct except the two Alibaba/Qwen locators.
- **Cover.** The sheet is 344.88 × 220.0 mm. 5 + 148 + (638/2 × 0.12 + 0.6 = 38.88) + 148 + 5 = 344.88 mm, so it matches exactly. The `cover.py` paper constant ("weiss" 0.012 cm per leaf) is correct. Spine text sits inside the safe zone. All fonts are embedded in both PDFs. The barcode box is left for BoD, as intended.
- **Cross-chapter facts (consistent).** ChatGPT released 30 Nov 2022 and 1.2 billion weekly users in Sept 2026 (ch01, ch03; ch10's "800 million at the time" refers to Oct 2025). GPT-3: 175 billion parameters, 300 billion tokens, 3.14 × 10^23 (ch01, ch02, ch03, ch04). DeepSeek-V3: 671B/37B and $5.576M (ch03, ch04, ch07). Llama 3.1: 16,384 H100s and 3.8 × 10^25 (ch03, ch04). EU 10^25 FLOP threshold (ch01, ch07, ch13). AI Act dates and the Digital Omnibus (27 Jul 2026 in force; Annex III moved to 2 Dec 2027; marking grace period and new bans from 2 Dec 2026), checked across ch08, ch09, ch10 and ch13. GPT-6 Astra (3 Sep 2026), GPT-6.1 Astra held back (ch12 and ch14 agree), GPT-6.2 (17 Nov). Claude Opus 4.6 at 12 hours and Mythos Preview at "at least 16 hours" (ch04, ch05, ch14). Nobel prizes 2024 (ch01, ch06). IMO 2025 gold (ch01, ch04, ch06). Nvidia data-centre revenue quadrupled ($47.5B to $193.7B: ch07, checked arithmetically). AI Act fines (ch13). About 15 "Section N.N" cross-references were spot-checked for topic (for example 7.1, 9.1, 11.5, 11.6, 12.7, 13.2, 14.3) and all point to the right material.
- Observation, not an item: continuation pages of long tables (pp. 312, 339, 371–372, 391) carry no source line, because the table's sources are in its caption on the first page. That fits the caption convention stated in the preface.

## Tally

Claims and checks: 61 (disclosure statements 9, front-matter elements 6, contents entries 18, cover and spine 3, cross-chapter facts 25). Of these, 56 confirmed, 1 wrong (index p. 133 for the IMO), 1 inconsistent (the METR fit), 1 outdated or stale (the PDF build), and 2 conditional or overclaiming (S1, S2). Mechanical checks: 638 pages for overflow, 46 figures, 69 boxes, 1,802 index locators (30 checked by hand), about 1,800 hyphenated line ends.
