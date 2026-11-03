# Publication-readiness review: *Understanding AI: Technology, Trends and the Decade Ahead*

Reviewer scope: the book as a product. This covers production (PDF), front and back matter, legal and rights risk, consistency across chapters, currency at 3 November 2026, and market positioning. Chapter content accuracy is out of scope, except where it touches these areas.
Object reviewed: `textbook/delivery/understanding-ai_A5_interior.pdf`. It has 590 pages and was built on 30 Oct 2026, with BUILD-INFO sources hash `55afa82a…`. The sources in `textbook/chapters`, `bib`, `print` and `work` were also reviewed. No book files were edited.

---

## 1. Verdict: **needs major work** (packaging and production, not a rewrite)

The text is in better shape than the package around it. The typesetting is clean, the cross-references resolve, en-GB spelling is consistent and the glossary is good. But a publisher could not accept this file today, for five reasons:

1. **The AI-authorship disclosure is inaccurate, and this has knock-on rights problems.** The preface says the book was "assisted by AI tools". The repository shows it was drafted chapter by chapter by autonomous agents. `textbook/work/WRITER-GUIDE.md:3` says "You write ONE chapter of a university course text", and `PROJECT_STATE.yaml` records `collaboration: mode: "autonomous"`. That affects the © line, retailer declarations and author warranties in any publishing contract.
2. **There is no index**, and there is no about-the-author page. A 590-page evidence-led nonfiction book needs an index. ISBN and imprint are still placeholders.
3. **The PDF is not demonstrably PDF/X-4, although README says it is.** The file header is `%PDF-1.3`, which PDF/X-4 does not allow because it needs 1.6 or later. The source lines were stamped in a post-processing pass after WeasyPrint wrote the file. The file has not been preflighted.
4. **Layout:** about 25–30 mid-chapter pages are 30–60% empty because figures or tables float to the next page. One table caption is cut off from its table. The figure text is about 6 pt.
5. **Sources can only be traced to the page, not the claim.** Pages cite an average of 5.5 sources and up to 19, with no link from a claim to its source. In a book whose selling point is "every claim sourced", this weakens the core promise.

The content is very current up to about 25 Oct 2026. It is already missing several late-September and October developments (§5), so it will need one more news pass at proof stage.

---

## 2. Blocking issues (fix before publication)

### B1. The AI disclosure understates AI authorship, and the copyright line rests on it
- **Where:** `chapters/ch00-preface.md`, "How the book was made". The PDF prints it on p. 10: "The research, drafting and checking of this book were assisted by AI tools, including large language models of the kind it describes. Every factual claim was checked against the source cited for it…"
- **Problem:** The repository shows an autonomous AI pipeline. Drafting was done by writer agents, checking by fact-check agents, and the "reader panel" was simulated (`work/panel2/`). `textbook/delivery/README.md` itself still says "A human expert review of this 2026 material before publication is still recommended." Readers will take "assisted" and "every factual claim was checked" to mean human authorship and human checking. That is misleading.
- **Consequences:**
  - (a) Amazon KDP asks publishers to tell it about AI-generated content, which includes text drafted by AI even if it was then edited. "AI-assisted" content need not be declared, so the wrong label here is a platform-policy breach.
  - (b) In the US, purely AI-generated text is not protected by copyright. Thaler v. Perlmutter (D.C. Cir., 18 Mar 2025) and the US Copyright Office's *Copyright and AI, Part 2* (Jan 2025) both say so. "© 2026 Jan Göbel. All rights reserved." (p. 4) may be partly unenforceable. Any US registration would have to disclaim AI-generated material.
  - (c) Standard author warranties ("original work by the Author") would be untrue.
- **Fix:**
  - Write an accurate statement that says what AI did (drafting, research, checking) and what the human author did (direction, selection, review, approval).
  - Remove or qualify "Every factual claim was checked" unless a human did the checking.
  - Get a human subject-expert read, as README already recommends.
  - Take advice on the copyright notice and on how to declare the book to the distributor.

### B2. No index
- **Where:** The contents list on p. 5 ends with Glossary (465) and References (495).
- **Problem:** The book has 590 pages, 1,160 references, about 400 named people, organisations, laws and models, and 14 chapters meant to be read "on their own". A reader cannot find, for example, *Bartz v. Anthropic*, METR or SB 53 without an index. The glossary (409 terms) gives no page locators. Reviewers and libraries will mark the book down for this.
- **Fix:** Add a subject and name index of about 15–25 pages. As a minimum, add page locators to the glossary. Pandoc and WeasyPrint can produce one through `target-counter()` on index anchors.

### B3. Placeholders and missing front/back matter
- **p. 4:** "ISBN: [to be assigned]" and "Publisher and printer: [imprint details]".
- **Missing:** an about-the-author page (the reader learns nothing about Jan Göbel's expertise, which matters for a book that judges evidence), acknowledgements, edition or impression line, country of printing, CIP or British Library statement, trademark notice and a not-professional-advice disclaimer. The last matters because Ch. 10 covers health and mental-health chatbots and Ch. 13 covers law.
- **Fix:** Fill these in or remove them before upload. Add a one-paragraph author biography that states the author's credentials and any conflicts of interest. The preface asks this of every other source ("where a person has a stake… the stake is stated").

### B4. The PDF/X-4 claim is not demonstrated
- **Evidence:**
  - `pdfinfo` reports PDF version **1.3**, and the first bytes of the file are `%PDF-1.3`. PDF/X-4 is based on PDF 1.6.
  - The XMP declares `GTS_PDFXVersion PDF/X-4` and there is an sRGB OutputIntent. `TrimBox` and `BleedBox` are set equal to `MediaBox`.
  - `build.py:349` writes PDF/X-4, but `stamp_pagelines()` then rewrites the file to add the source lines. Those lines use extra non-subset `AAAAAA+EBGaramond-*` fonts with WinAnsi encoding, which reportlab adds. That rewrite is the likely cause of the version downgrade.
  - The file is untagged (`Tagged: no`).
- **Also embedded:** DejaVu Serif, DejaVu Serif Bold, DejaVu Sans Mono and **WenQuanYi Zen Hei Medium Oblique**. These are fallback fonts that the colophon does not mention ("Set in EB Garamond, with Noto Serif Devanagari"). The mono font is used for `o200k_base` and token tables (p. 74). The fallback glyphs should be located and either replaced or credited.
- **Fix:**
  - Run a real preflight: callas pdfToolbox, Acrobat Preflight PDF/X-4, or the printer's own checker.
  - Make the stamping step keep the PDF 1.6+ header and the X-4 conformance.
  - Check the printer's colour requirements. The interior is greyscale but stored as RGB. KDP accepts this. Other printers may require greyscale or CMYK.

---

## 3. Major issues

### M1. Large blank areas where figures and tables float
I rendered 52 pages at 70 dpi: 1, 3, 4, 5, 7, 10, 11, 13, 19, 35, 36, 45, 57, 60, 61, 65, 74, 82, 83, 109, 110, 116, 126, 135, 150, 166, 167, 170, 205, 213, 214, 215, 224, 249, 285, 305, 349, 380, 385, 402, 416, 428, 436, 444, 455, 463, 465, 480, 495, 530, 589 and 590. I also rendered 8 more at 50 dpi.

A whitespace scan of every page finds 32 mid-chapter pages where more than 25% of the text block is white. The worst are:

| Page | Share of text block left white | What is happening |
|---|---|---|
| 35 | 51% | Fig 1.3 pushed to p. 36 |
| 60 | 56% | |
| 68 | 43% | |
| 82 | 60% | Fig 3.2 pushed |
| 135 | about 35% | Fig 5.1 pushed after the concept box |
| 140, 157 | 39% each | |
| 166 | 44% | |
| 189 | 48% | |
| 227 | 55% | |
| 274 | 41% | |
| 284 | 51% | |
| 320 | 43% | |
| 380 | about 65% white below the figure | |
| 444 | 46% | |
| 454 | 49% | |

**Fix:** let text flow past floats (`float: top` or deferred placement), shrink oversized figures, or allow a figure at the foot of the page.

### M2. Table caption cut off from its table
Table 7.3's caption sits at the foot of p. 215 and the table starts on p. 216. Check every table for this. Set `break-after: avoid` on captions, or move table captions below the table as figure captions are.

### M3. Figure text is about 6 pt
- On Fig 1.3 (p. 36) and Fig 13.2 (p. 416), labels measure roughly 5.5–6.5 pt at print size (from a 150-dpi crop). Fig 1.3 holds 40 or more labels plus a caption with 37 source numbers.
- At A5 most publishers set a minimum of 7 pt.
- **Fix:** rotate or enlarge to a full page, or split the figure. Check every timeline and forest plot: Figs 1.3, 8.2, 9.3, 13.2 and 14.4.

### M4. Source lines show only which sources a page uses
- The **Sources** line at the foot of each page lists reference numbers, with pinpoints such as "353 (art. 113)". In practice, p. 13 lists 111 · 353 (art. 113) · 461 · 671 · 1069. A reader can work out that 1069 (SEC) supports "fines from US regulators", but only by checking each one.
- On average a page lists 5.5 sources. Pages 197 and 418 list 19 and 18. Page 224's line runs to two lines and crowds the folio.
- Pages 244, 284, 297 and 371 have no source line because they continue tables whose sources are in the caption on the previous page. That is defensible, but the reader is not told.
- So the system works for checking a page, but not for checking a claim. For a book that promises "every factual claim… sourced", this is the main usability weakness.
- **Fix:** keep the clean text but add small superscript markers that key to the numbers in the source line, for example "¹ 1069". Alternatively, order each line by first use and say so in the preface. The repository's `sample-ch10-source-notes.pdf` shows an alternative was already prototyped.

### M5. The audience and genre are muddled, and the length is high for a trade book
- `PROJECT_STATE.yaml` says "university course text". README and the preface say it is nonfiction, "not a course text", with no learning aids.
- The book has about 152,000 words of running text (about 197,000 with references), 590 A5 pages, equations and worked arithmetic.
- That is long for a trade book. Comparable titles run 250–380 pages (§6). Without exercises it is also not a textbook.
- **Fix:** pick one. Either cut to about 110,000 words for a trade or crossover edition, or put back course apparatus and position it for university adoption. See §6.

### M6. Currency: late-Sept to Oct 2026 developments are missing
See §5.

### M7. Hyphenation density and ladders
- pdftotext finds about 2,590 end-of-line hyphenations in about 450 body pages, roughly 5.7 per page. There are **114 runs of three or more hyphenated lines in a row**.
- Some breaks are poor: "cent-ral" and "Nath-aniel" (p. 13), "reas-on" (p. 10), "Ja-panese" (p. 13), "evid-ence".
- **Fix:** set `hyphenate-limit-lines: 2` and `hyphenate-limit-chars: 6 3 3`. Add exceptions for proper names. Loosen justification slightly.

---

## 4. Minor issues

### Contents list (p. 5)
- All page numbers are correct. I checked all 14 chapters, the glossary and the references against the PDF.
- The Chapter 14 entry wraps so that the dot leader and "431" sit alone on a second line. Shorten the TOC entry, for example to "Forecasting the Next Ten Years".
- Part titles carry no page numbers. That is acceptable.

### Running heads and folios
- Running heads are consistent: "Understanding AI" on versos, the chapter title on rectos. Openers and blank pages have none.
- Every body page has a folio. Ch14's long recto head ("Forecasting the Next Ten Years: Methods, Scenarios and Open Problems") fits, but only just.
- Blank pages (2, 6, 12, 104, 130, 132, 164, 232, 234, 264, 330, 362, 396, 430, 464) are all correct recto-start blanks.

### Widows and orphans
None detected by a heuristic scan. One possible stranded line was flagged, a lone "2025" on p. 422.

### Preface inconsistency
The preface says "about a thousand references". The list has **1,160**.

### Reference list (APA 7)
I sampled 40 entries.
- **Proper nouns wrongly lower-cased by CSL sentence-casing:**

  | Ref | As printed |
  |---|---|
  | 30, 36 (and the Meta 10-K) | "form 10-k… december 31" |
  | 49 | "Golden gate Claude" |
  | 61 | "Project vend" |
  | 68 | "Claude Fable 5 and claude Mythos 5" |
  | 246 | "South korea's" |
  | 328 | "2 august 2017" |
  | Gray & Suri | "silicon valley" |
  | 852 | "rs 10,300 crore" |
  | 1000 | "navier-stokes… millennium prize" |
  | Two EU entries | "european union", "european parliament" |

  That is about 9 of the 40 sampled entries, so expect 150 to 250 across the list. **Fix:** protect proper nouns with `{}` in the .bib files.
- **"et al." inside the reference list** in about 109 entries (e.g. ref 47, Anil et al.). APA 7 lists up to 20 authors.
- **Dates:** house style "(2025). … 14 November 2025." is used almost everywhere. Three entries use "(2026, September)", which is the APA format. Choose one.
- **No "n.d." entries.** Only 7 entries lack a URL or DOI, all books or a 1958 newspaper, which is acceptable.
- **The same work cited twice:**
  - acemoglu2024simple and acemoglu2025simple (refs 6 and 7: working paper and journal version)
  - argyle2022out and argyle2023out
  - kraft2019interpreting and kraft2020interpreting
  - chen2025reasoning and anthropic2025reasoning (paper and blog)

  Cite the version of record, or say why both are cited.
- **Ref 1046:** a court order hosted on a law firm's website. Prefer PACER or CourtListener.

### Glossary
I checked 30 definitions, including double descent, logit, CASP, CRPS, RLAIF, orthogonality thesis, specification gaming, HPL, DFT, active parameters, alignment faking and pre-emption. **All 30 are substantively correct.** One leaks context from its chapter: "active learning… (here, by DFT calculations)". The ordering puts "50% time horizon" and "510(k)" first, which is acceptable.

### Smaller points
- **Straight quotes in figures:** for example "'AI winter' warning" in Fig 1.3.
- **Model naming:** GPT-5.6 Sol (9 mentions) and GPT-6 Sol (1) are both used deliberately. `ch12.md:96` says "not to be confused with GPT-6 Sol", but a lay reader will still be confused. Add both to a short "models named in this book" table.
- **State lawsuit counts:** ch10:163 says "ten had sued OpenAI". ch13:287 says "Florida… In October at least eight more states". These are consistent, since Texas was a separate suit on 23 Oct, but give one figure in both places.
- **Running text uses "10,000x"** (p. 109) alongside "times" elsewhere.

---

## 5. Currency check: 1 Oct to 3 Nov 2026

The book is very current up to about 25 Oct. It covers:
- GPT-6 Astra (3 Sep) and GPT-6 Sol (22 Sep)
- Gemini 4 Argon (on ClockBench)
- the Mythos 5 and Fable 5 family
- Bartz final approval (20 Jul)
- the October state AG suits
- the EU Digital Omnibus
- the TAKE IT DOWN Act deadline.

The following are **absent from the text** (grep of all chapters). A November 2026 reader would expect several of them. All are reported by several outlets, but I checked secondary coverage only, not the labs' own pages. Verify before adding.

| Development (date) | Relevance | Status in book |
|---|---|---|
| **Claude Opus 5.5** (22 Sep 2026). Anthropic says it matches Fable 5.1 at 40% lower cost. Also **Opus 5 / Fable 5.1** | Anthropic's current public flagship | Book's newest Anthropic models are Opus 4.7, Fable 5 and Mythos 5. "Opus 5" never appears, so the Anthropic line-up is out of date |
| **Meta Muse Spark Open** (15 Oct 2026), an 816B MoE model with open weights under a restrictive Muse licence. Meta's closed-to-open reversal | Central to Ch 7's open-models section and Table 7.5 | Meta's newest model in the book is Llama 4 (Apr 2025). The Muse family is not mentioned at all |
| **OpenAI GPT-6 Pro "parallel agents"** in ChatGPT (16 Oct 2026) | Ch 5 agents | Absent |
| **Anthropic Claude Duet** research preview (21 Oct 2026), a proactive background agent with approval gates for send, spend, sign and delete | Ch 5 agents and ch 12 oversight | Absent |
| Chinese open releases: DeepSeek V4.1 (29 Oct), Kimi K3.1 (23 Oct), Qwen3.6 (21 Oct) | Ch 7 open models. Book has DeepSeek-V4 and Qwen3.5 | Absent (minor) |
| **Musk v. Altman**: jury, adopted by the court, rejected Musk's claims as time-barred (18 May 2026) | Ch 13 governance and OpenAI structure | Absent |
| **Anthropic SEC filing** (2 Nov 2026): about $17bn Q3 revenue and more than $895bn in planned spending before an IPO (Bloomberg) | Ch 7 cost concentration, Ch 8 economy | After the book's cut-off. Add at proof stage |
| Copyright docket: summary-judgement motions on fair use pending in *In re OpenAI* (SDNY, Judge Stein), *Concord v. Anthropic* (argued 21 Oct), *Andersen v. Stability* (hearing 4 Nov) | Ch 13 copyright | Check the wording "no appellate ruling yet" etc. A ruling could land between proof and print |
| Vietnam's AI Law (in force 1 Mar 2026); Japan's revised enforcement decree (Jul 2026) | Ch 13 Asia lane and Fig 13.2 | Vietnam absent |
| ChatGPT "more than 1.2 billion weekly users" (late Sep 2026, ch01:5) | Opening paragraph | **Could not verify.** The latest figure I found is 900M (Feb 2026, TechCrunch). Verify the cited source |

**Recommendation:** freeze the text with a dated "Developments after October 2026" note. Run a final one-day news pass at proof, and put the model names in one place, such as a "Models named in this book" table. That way the next edition only needs one page updated.

---

## 6. Legal and rights risk

### Defamation
- I reviewed 62 hits for alleged, accused, fraud, illegal, misled, deceptive, pirated, criminal, threaten and similar words, across chapters 1, 5 and 9–13.
- Statements about named living people and companies are consistently attributed to a source ("according to TechCrunch… alleging", "according to the court record") or framed as allegations. Examples: the Nate founder fraud charge (ch01:268), Steve Kramer's fine and acquittal (ch09:3; the acquittal is correctly reported), Romania, X and Grok (ch09), Anthropic's pirated-library finding (ch13:231, quoting the court).
- **Low risk.** One point to watch: claims that "GPT-5.6 Sol… broke into an outside company's systems" (ch12 table) and "Claude Mythos 5 published a malicious software package… run on 15 real systems" (ch12:249). Both are attributed to company or AISI reports. Keep the attribution in the table cell as well. It currently says "Company claim and report; independent review", which is good.

### Privacy and minors
- Suicide and minor cases (ch10:163, ch13:285–289) name no children. They refer to cases only by caption (*Garcia*, "the Raine case") and give no methods. That is appropriately restrained.
- No private individuals are named outside court or public records.

### Quotations
- There are 1,122 quoted passages totalling about 6,600 words. The longest are about 37 words, from EU legislation.
- No song lyrics or poems. Fair dealing and fair use risk is **low**.

### Figures adapted from third-party originals
- Schematics "after" Goodfellow et al. (Figs 1.1, 2.6a), Vaswani et al. Fig 1 (3.2), Reason's Swiss-cheese model (12.x) and the EU risk pyramid (13.1).
- Data redraws from IEA (7.3, 7.4), Epoch (4.2), METR (4.3) and published studies (8.2, 9.3).
- All are redrawn rather than copied, and the underlying data are facts. The EU and Epoch materials are reusable under open licences.
- **Low risk**, but a publisher will want a permissions log. Confirm the IEA licence for *Energy and AI* (CC BY 4.0 is likely) and keep the "after X" credits.

### Trademarks
Model and product names are used descriptively. Add a standard trademark notice to the copyright page.

### Title conflict
"Understanding AI" is the name of Timothy B. Lee's widely read AI newsletter. *Understanding Deep Learning* (Prince, MIT Press 2023) and *Understanding Artificial Intelligence* (Sabouret, CRC 2020) already exist. This is not an infringement risk, but it is a discoverability and confusion risk (§7).

---

## 7. Positioning

| Comparable | Length | Audience | How this book differs |
|---|---|---|---|
| Narayanan & Kapoor, *AI Snake Oil* (Princeton UP, 2024) | about 360 pp | General, sceptical | This book is broader (technical and policy) and two years newer. Theirs has a clear argument and known authors |
| Mitchell, *Artificial Intelligence: A Guide for Thinking Humans* (2019) | about 340 pp | General, explanatory | This book explains LLMs and agents, which Mitchell predates |
| Mollick, *Co-Intelligence* (2024) | about 250 pp | Business and general | This book is evidence-led, not practical advice |
| Hao, *Empire of AI* (2025); Suleyman, *The Coming Wave* (2023) | 300–500 pp | Narrative trade | This book has no narrative and no access journalism |
| International AI Safety Report 2026; Stanford AI Index 2026 (free) | 200–400 pp | Policy | The closest substitutes for Parts III–IV, and free. This book's advantage is synthesis and explanation for non-specialists |

**What sets it apart:**
- It labels the strength of evidence throughout.
- It is current to October 2026.
- It covers mechanisms, with worked equations, as well as economics, law and forecasting, in one volume.
- It has 1,160 sources.

**Weaknesses against the comparables:**
- an author with no stated credentials and AI-generated text (see B1)
- length
- a short shelf life for the 2026 material.

**Title:** "Understanding AI" is generic and already taken in the market. "The Decade Ahead" overpromises, since only Ch 14 looks forward. Consider a title that names the selling point, for example *AI on the Evidence: What We Know About Artificial Intelligence in 2026, and How We Know It*. Or keep the title and change the subtitle to "An evidence-based guide, 2026 edition". Putting "2026" on the cover makes a virtue of the dating and sets up later editions.

---

## 8. What works
- The contents page numbers, all section cross-references (checked automatically: every "Section N.M" resolves), running heads and folios are correct. Recto chapter starts and part openers follow convention.
- The typography is restrained and professional: EB Garamond, well-styled boxes, clean tables (e.g. Table 13.1, p. 402).
- en-GB spelling is consistent. The US spellings that appear are proper nouns only (Defense, Center, Department of Labor).
- The glossary (409 terms) is accurate and readable.
- Evidence labelling (company claim, preprint, news report) is consistently applied, which lowers legal risk.
- Sensitive cases are handled responsibly.

## 9. Spot-check tally

| Check | Sample | Result |
|---|---|---|
| PDF pages inspected | 52 at 70 dpi, 8 at 50 dpi, 2 crops at 150 dpi, plus a whitespace scan of all 590 | 32 pages with large gaps; 1 caption cut off from its table; about 6 pt figure text; TOC wrap |
| TOC page numbers | 17 | 17 correct |
| Glossary definitions | 30 | 30 correct (1 with context leakage) |
| Reference entries (APA) | 40 | 31 clean; 9 casing errors; plus 109 list-wide "et al." deviations, 3 inconsistent date formats, 4 pairs citing the same work twice; 0 "n.d." |
| Defamation-term hits | 62 | 0 problematic; all attributed or framed as allegations |
| Quotation length | 1,122 quotations | None over about 40 words; no lyrics or poems |
| Cross-chapter consistency | Model names, ChatGPT users, Bartz settlement, METR horizons, state suits | Consistent; Sol/GPT-6 Sol naming liable to confuse |
| Currency items (Oct 2026) | 10 | 7 missing developments; 1 statistic unverifiable (1.2bn weekly users); others covered |

---

## 10. Prioritised pre-publication checklist
1. **Rewrite the AI disclosure** accurately (B1). Get advice on the © notice, the distributor's AI declaration and contract warranties. Commission a human subject-expert read.
2. **Assign the ISBN and imprint.** Add an about-the-author page, acknowledgements, edition line, trademark notice and not-professional-advice disclaimer (B3).
3. **Build an index**, or at least add page locators to the glossary (B2).
4. **Preflight the PDF to PDF/X-4** with a real tool. Fix the 1.3 header and the stamping step. Locate or replace the DejaVu and WenQuanYi fallback glyphs and update the colophon. Confirm the printer's colour specification (B4).
5. **Repaginate the floats.** Remove the 25–30 half-empty pages and keep table captions with their tables (M1, M2).
6. **Enlarge figure text to at least 7 pt.** Redesign Figs 1.3 and 13.2 (M3).
7. **Add claim-level markers** to the source-line system, or document how it is ordered (M4).
8. **Run a final news pass at proof:**
   - Claude Opus 5 and 5.5, and Fable 5.1
   - Meta Muse Spark Open
   - GPT-6 Pro parallel agents
   - Claude Duet
   - Musk v. Altman
   - Anthropic's S-1 figures
   - pending fair-use summary judgements
   - re-verify the 1.2bn ChatGPT figure

   Add a "Models named in this book" table and a dated cut-off note (§5).
9. **Clean the bibliography:**
   - protect proper nouns with braces
   - list all authors (up to 20) instead of "et al."
   - use one date style
   - merge the duplicated works.

   Change the preface's "about a thousand" to 1,160.
10. **Tune hyphenation**: no more than 2 hyphenated lines in a row; fix name breaks. Fix the TOC wrap and the "(here,…)" glossary leak.
11. **Decide the positioning** (trade vs course text) and the length. Reconsider the title and subtitle (§7).
12. **Keep a permissions log** for adapted figures (IEA, Goodfellow, Vaswani, Reason, EU).
