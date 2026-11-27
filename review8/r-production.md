# Review 8: whole-book and production checks

Reviewed 27 November 2026. Scope: AI-authorship disclosure (preface, copyright page, back cover), front matter, the PDF itself (overflow, blank gaps, figures, boxes, page numbers, contents, hyphenation, index sample of 30), cover spine against the page count, and consistency of facts that recur across chapters.

Build status: `python3 textbook/print/check_build.py` prints "delivery PDF matches the sources". `BUILD-INFO.txt` records 638 pages, which matches `pdfinfo` (638 pages, A5, 419.528 x 595.276 pt, built 27 Nov 2026 09:19 UTC). The cover was built two minutes later.

Known and accepted, not reported: ISBN placeholder (copyright page and cover barcode box); "chiefly…" model list; imprint text still to come from myBoD; blank space before full-page figures (e.g. p. 84); Table 11.3 running across pages 372–373; the wrap of the Chapter 14 entry in the contents.

## Verdict

Ready to print after the SHOULD items, at the author's discretion. Nothing in the production checks blocks printing. The PDF is current. No text runs off any page. All 46 figures render. All 69 boxes are labelled correctly and none has its title stranded at a page foot. Printed page numbers match the PDF pages. The contents page is correct. The 30 sampled index entries all point to the right pages. The spine width is correct for 638 pages. The AI disclosure is clear and honest. One condition applies: the preface says that errors found in review "were corrected before printing". That stays true only if the MUST items from this eighth round are fixed or are formally rejected after re-checking.

## MUST change before printing

None.

## SHOULD change

### S1. Proper nouns lower-cased in the reference list (APA sentence-casing slips)
- Where: `textbook/bib/*.bib` (titles not protected with braces). It shows in the printed References, pp. 519–630.
- Text now (as printed): "South korea's AI basic act: Overview and key takeaways"; "New york enacts AI chatbot safeguards for minors"; "Governor newsom signs SB 53, advancing california's world-leading artificial intelligence industry"; "Mayor mamdani and chancellor samuels put students first…"; "It's the golden state, not the wild west: Attorney General Bonta sues OpenAI…"; "Staff at the US center for AI safety are reporting to the White House…"; "Center for advancing innovation and standards for Super Intelligence (CAISSI), formerly center for AI standards and innovation (CAISI)"; "On the Navier–Stokes millennium prize problem"; "Docket no. 25-449, thaler v. Perlmutter"; "Joint case management statement, kadrey v. Meta platforms, inc."; "…class action settlement, bartz v. Anthropic PBC"; "In re OpenAI, inc. Copyright infringement litigation; The New York Times Company v. Microsoft corporation"; "Guidance for industry and food and drug administration staff"; "H.R. 2683, remote access security act (119th congress)"; "H.R. 9925 – FRONTIER act, 119th congress"; "S.Amdt. 2814 … 119th congress"; "The Bletchley declaration by countries attending the AI safety summit"; "The electric vehicles (smart charge points) regulations 2021"; "OECD employment outlook 2026"; "PwC 2026 global AI jobs barometer"; "The beige book".
- Problem: UNCLEAR (presentation). APA sentence case keeps proper nouns capitalised, and that includes the names of statutes, courts, cases, agencies, places and named reports. `fix_bib_case.py` protects most of these but misses the entries above. They look like errors to any careful reader, and some read oddly ("formerly center for AI standards"). This does not block printing.
- Evidence: the bib sources have the capitals, for example `ch13.bib:948` `{South Korea's {AI} Basic Act…}`, `ch10.bib:1287` `{New York Enacts…}`, `ch13.bib:141` `{Governor Newsom signs…California's…}`, `ch10.bib:894` (Mamdani, Samuels), `ch10.bib:1314`/`ch11.bib:921` (Golden State, Wild West), `ch12.bib:329` (Center for…), `ch06.bib` OpenAI Navier–Stokes entry (Millennium Prize), `ch13.bib:820` (Thaler), `ch13.bib:811` (Kadrey, Meta Platforms, Inc.), `ch13.bib:793` (Bartz), `ch10.bib:1222` and `ch10.bib:1231` (In re OpenAI, Inc. Copyright Infringement Litigation; Microsoft Corporation), `ch10.bib:1015` (Food and Drug Administration), `ch07.bib:1022` (Remote Access Security Act, 119th Congress), `ch13.bib:477` (FRONTIER Act, 119th Congress), the S.Amdt. 2814 entry, the Bletchley Declaration entry, `ch14.bib:350`/`ch14.bib:864` (Electric Vehicles (Smart Charge Points) Regulations), `ch08.bib:801` (Employment Outlook), `ch08.bib:262` (Global AI Jobs Barometer), `ch08.bib:714` (Beige Book). Also check the Burke (2026) entry ("US Center for AI Safety").
- Change to: wrap the proper-noun runs in braces, e.g. `{South Korea's {AI} {Basic Act}: Overview and Key Takeaways}`, `{{New York} Enacts…}`, `{Governor {Newsom} signs {SB} 53, advancing {California's}…}`, `{Order…, {Bartz v. Anthropic PBC}, …}`, `{{H.R.} 2683, {Remote Access Security Act} ({119th Congress})}`, `{{The Bletchley Declaration} by Countries Attending the {AI Safety Summit}…}`, `{{OECD Employment Outlook} 2026: …}`, `{The {Beige Book}: …}`, and so on. Then rebuild.

### S2. Back cover says "fact-checked" without the copyright page's limit
- Where: `textbook/print/cover.py:213-221` (back-cover "WRITTEN WITH AI" note)
- Text now: "Most of the text of this book was generated by the AI models Claude Opus 5.5 and Claude Fable 5.2, working under the author's direction, and fact-checked by the same models. No independent human expert has reviewed it."
- Problem: UNCLEAR, mild overclaim. The copyright page (`build.py:25`) says "fact-checked (where sources could be read online)". The preface says books, paywalled articles and some websites "could not always be opened". On the back cover, the one place a buyer reads before buying, the qualifier is missing. Read alone, "fact-checked" suggests complete checking.
- Change to: "…working under the author's direction, and checked against its sources, where they could be read online, by the same models. No independent human expert has reviewed it. The preface explains how it was made." (This adds one line, which the text block has room for above the ISBN box.)

### S3. Chapter 5 says Claude Mythos Preview was "released"; other chapters say it was withheld
- Where: `textbook/chapters/ch05.md:176` (Section 5.x, the time-horizon paragraph)
- Text now: "an early version of Claude Mythos Preview (released April 2026)"
- Problem: INCONSISTENT. Ch03:437 has "withheld from general release over its cyber capabilities", ch11:137 has "which the company chose not to release generally", and ch14:109 has "which was not publicly available".
- Change to: "an early version of Claude Mythos Preview (announced in April 2026 but not released generally)"

### S4. Words hyphenated across a page turn, including names
- Where: PDF pp. 221/222 "Janu-|ary", 229/230 "Represent-|atives", 273/274 "Micro-|work", 304/305 "AI Over-|views", 329/330 "AI-spe-|cific", 337/338 "Alpha-|bet". (A broader point: personal and company names are also auto-hyphenated within pages, e.g. "Brynjolfs-son" p. 265, "Bletch-ley" p. 436, "Nath-aniel" p. 15, "Califor-nia" p. 206.)
- Problem: UNCLEAR (typography). Splitting a word across a page turn, and a company name ("Alpha-bet") in particular, is a recognised fault in book setting. Six cases in 638 pages is few, and each can be fixed by hand.
- Change to: in each of the six source sentences, wrap the word in `[…]{.nohy}`, which already exists in `book.css:128`. For example ch10 "including [Alphabet]{.nohy}, Meta", ch07 "fiscal year ending [January]{.nohy} 2026", ch07 "House of [Representatives]{.nohy}", ch08 "[Microwork]{.nohy}", ch09 "AI [Overviews]{.nohy}", ch10 "[AI-specific]{.nohy}". Re-check the six page feet after rebuilding.

### S5. Inconsistent capitalisation in one box title
- Where: `textbook/chapters/ch05.md` (the `.box .deeper` at line 49/50)
- Text now: "**Going deeper: how a generative agent decides what to recall**"
- Problem: INCONSISTENT. The other 68 box titles capitalise the word after the colon (e.g. "Going deeper: What 'top-5 error' measures", "Going deeper: Three further open problems").
- Change to: "**Going deeper: How a generative agent decides what to recall**"

### S6. The preface's corrections route may not reach the author
- Where: `textbook/chapters/ch00-preface.md:56` (end of "How the book was made")
- Text now: "Corrections are welcome and can be sent through the publisher;"
- Problem: UNCLEAR. With BoD, the publisher of record is a self-publishing service provider. There is no evidence that it forwards readers' factual corrections to authors. A book that relies on readers to catch AI errors needs a route that is sure to work.
- Change to: "Corrections are welcome and can be sent to [author's e-mail or web address];" (or keep the current wording if the author has confirmed that BoD forwards such mail).

## Could not verify

- Preface: "In one of them about 2,600 statements were checked against their sources". The brief puts the review logs out of bounds, so this could not be checked. The eighth round's own count belongs in 00-VERDICT.
- Preface: "The errors and out-of-date statements these rounds found were corrected before printing". This depends on what happens to this round's findings (see Verdict).
- Copyright-page imprint (BoD and Libri Plureos addresses): accepted as to be pasted from myBoD, not checked further.

## Checked and confirmed

- **Build current:** check_build.py passes, and BUILD-INFO gives 638 pages, which equals the PDF.
- **Spine:** the cover sheet is 977.613 pt = 344.88 mm wide, which is 5 + 148 + spine + 148 + 5. That gives a spine of 38.88 mm. The expected spine is 638 / 2 × 0.12 mm + 0.6 mm = 38.28 + 0.6 = 38.88 mm, so they match exactly. Height is 220 mm (210 + 2 × 5 bleed). `cover.py` uses 0.012 cm per leaf for "weiss" and defaults to 638 pages.
- **Overflow:** word bounding boxes (`pdftotext -bbox`) never pass the text block. The right edge is at most 362.97 pt on versos and 377.14 pt on rectos, and the page width is 419.5 pt. The only words outside the left text edge are the reference numbers in the References, which hang in the margin by design (10 mm from the trim). No unresolved `[@…]` citations, no "??" and no replacement characters appear.
- **Blank gaps:** every page with a gap of more than 150 pt was looked at. All are figures, tables, part or chapter openings, chapter ends, or the accepted gap before a full-page figure.
- **Figures:** there are 46 figure captions, Figure 1.1 to 14.4 in sequence, and 46 image references in the chapter sources. All 46 figure pages were rendered and all images are present and intact. Figures 7.2 and 13.2 were viewed at 80 dpi, with legible labels and no clipping.
- **Boxes:** there are 69 boxes. Each class (concept, case, debate, deeper) matches its title prefix, and no box title is the last or second-to-last line of a page.
- **Page numbers:** the printed folio equals the PDF page on every numbered page. Only the half-title, title, copyright, contents and part-title pages are unnumbered.
- **Contents:** all 20 entries (Preface 7, Ch1 15 … Ch14 453, Glossary 487, References 519, Index 631) match the actual opening pages.
- **Cross-references:** every "Section N.M", "Table N.M" and "Figure N.M" reference resolves to an existing number (113 sections, 62 tables, 46 figures). All 36 cross-chapter section references were spot-read, and each points to a section on that topic.
- **Index, 30 random entries (seed 8):** decoder, ghost work, Google, California, context window, Redwood Research, AI tutor, artificial neuron, chain rule, deskilling, synthetic data, latent diffusion, cross-entropy, grouped-query attention, polarisation, AI agent, initialisation, Japan, induction head, gradient, Kimi, momentum, test-time compute, H100, attribution graph, jagged technological frontier, deepfake, self-supervised learning, Agent Card, recurrent neural network. That is 30 entries with 136 page locators, and every locator is correct. The two apparent misses were hyphenated compounds, "AI-agent team" on p. 359 and "attribution-graph authors" on p. 403. To match words hyphenated at line ends, the page text was searched with the U+2010 line-end hyphens rejoined. The index itself (pp. 631–638) and the References use `hyphens: manual` and contain no U+2010 line-end breaks.
- **Fonts:** all fonts are embedded. The only fallback glyph in the whole PDF is a single "␣" (U+2423, visible-space marker) on p. 85, set in DejaVu Serif. It is intended and renders correctly. No missing glyphs.
- **Hyphenation:** the body has 1,867 automatic U+2010 line-end breaks. No numbers are split, and the only breaks involving numbers are the "175-billion-para-meter" type. Page-turn cases are in S4.
- **Disclosure:** the copyright page, the preface ("How the book was made", pp. 10–11) and the back cover agree on what matters most. AI generated most of the text. The same models checked it, and the copyright page and preface say where the checking stopped. No independent human expert has reviewed it. The author directed and approved the work and is responsible for it. The preface also names the conflict of interest (the models' maker, Anthropic, is a subject of the book), warns that "AI-written text can be fluent and wrong at the same time", and does not claim human review. The copyright line "(selection, arrangement, editing and human-authored contributions)" is suitably limited. Only S2 overclaims slightly.
- **Preface claims checked against the book:** five parts and 14 chapters as described. Four box types are used. Every chapter has a "Further reading" section (14 of 14). The glossary exists. "More than 1,200 references": the list runs to 1,319. Table 3.1 gives tokeniser settings ("tiktoken 0.14.0 on 22 Oct…"). The uncited paragraphs containing numbers are only worked examples, formulas or the author's own signposts (ch02 ×2, ch05 ×1, ch14 ×1), which the preface allows for.
- **Cross-chapter repeated facts, consistent:** ChatGPT launch (Nov 2022) and 1.2 billion weekly users (ch01, ch03). GPT-3 at 175 billion parameters and 300 billion tokens (ch01–04, ch07). METR time horizons: ~12 h for Claude Opus 4.6, CI 5–61 h, 16 h reliability limit, the 14.5 h early figure, Mythos Preview "at least 16 hours" and ~17 h, doubling 129 days since 2023 and 188 since 2019 (ch04, ch05, ch14). IEA data-centre electricity of 485 TWh in 2025 and ~950 (945) TWh in 2030 with a range of 833–1,008 (ch07, ch14). EU Digital Omnibus in force 27 July 2026, high-risk rules moved to 2 Dec 2027 and 2 Aug 2028, Article 50 duties from 2 Aug 2026 (ch08, ch09, ch13, ch14, Fig. 13.2). Commerce Department licence for Fable 5 and Mythos 5 of 12, 26 and 30 June 2026 (ch07, ch13). State suits against OpenAI, at least eleven by mid-November, with California on 16 November (ch10, ch11, ch13). IMO 2025 gold-level results (ch01, ch04, ch06). Dartmouth proposal of 1955 (ch01, ch14). Grok images of January 2026 (ch09, ch11).

## Tally

Claims and production checks: 74 (30 index entries; 20 contents entries; spine; overflow; gaps; 46 figures counted as one check; 69 boxes as one check; page numbering; cross-references; 6 disclosure statements; 6 preface claims; 12 cross-chapter facts; reference casing; hyphenation). Confirmed: 66. Wrong or inconsistent: 6 (S1–S6, none blocking). Outdated: 0. Could not verify: 2.
