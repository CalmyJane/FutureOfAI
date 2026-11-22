# Third review: verdict (22 November 2026)

Fourteen independent fact-checkers each read one chapter in full as a reader, then checked its statements against sources. They did not see the earlier reviews. Their reports are in this folder (`r-ch01.md` … `r-ch14.md`). Each report gives the exact replacement wording and any new bibliography entries for every item below. The production checks (PDF, cover, front matter) are the coordinator's own.

## Overall verdict: not ready to print as it stands; ready after the fixes below

The text is accurate. The fixes are short wording changes; nothing needs rewriting.

**Totals:**
- **Claims checked against a source:** about 2,610.
- **Confirmed:** about 2,470 (95%).
- **Wrong:** 18.
- **Out of date:** 40.
- **Worked examples and calculations:** about 300, all recomputed, none in error.
- **References checked:** more than 800. No invented sources were found.

**What stands in the way of printing:**
1. **35 must-fix items** (section A). Most are 2026 material that changed after the text was written, or a quotation that does not match its source. Three of them are legally sensitive statements about named companies.
2. **One significant omission that runs across chapters** (B1): the US government's June 2026 export-control restriction on Claude Fable 5 and Mythos 5.
3. **Production and front matter** (section C):
   - the cover was built for 590 pages, not 626;
   - the copyright page still has placeholders;
   - two figure captions run off the page.
4. **Author decisions** (section D):
   - the AI-authorship disclosure;
   - the ISBN and imprint;
   - a human expert read.

| Ch. | Verdict | Checked / confirmed | MUST |
|---|---|---|---|
| 1 | After MUST fixes | 168 / 157 | 3 |
| 2 | After MUST fix | 190 / 187 | 1 |
| 3 | After MUST fixes | 172 / 164 | 2 |
| 4 | After MUST fixes | 168 / 161 | 4 |
| 5 | After MUST fix | ≈285 / ≈280 | 1 |
| 6 | After MUST fixes | 167 / 152 | 4 |
| 7 | After MUST fixes | 236 / 222 | 5 |
| 8 | After MUST fixes | 196 / 186 | 2 |
| 9 | After MUST fixes | ≈250 / ≈236 | 2 |
| 10 | After MUST fix | 112 / 103 | 1 |
| 11 | After MUST fixes | 128 / 117 | 3 |
| 12 | After MUST fixes | 168 / 155 | 3 |
| 13 | After MUST fixes | 205 / 193 | 3 |
| 14 | After MUST fix | 168 / 158 | 1 |

## First decision: the cut-off date

The book says it is current to October 2026. Many must-fix items are events from November 2026:
- the US chip-rule changes of 9 and 19 November;
- Nvidia's chief executive resigning;
- new third-quarter productivity and job-cut figures;
- the 20 November Navier–Stokes proof.

**Recommendation:** move the stated cut-off to mid-November 2026 and apply these updates. They are short. Keeping "October" would let past-tense deadlines stand, but a reader in 2027 would be misled. If you move it, change the preface ("gathered and checked in October 2026"), the copyright page ("checked between 20 and 25 October") and the "as of October 2026" phrases. Some bib access dates (30 October, 3 November) already contradict the October claim.

## A. Must fix before printing

### Chapter 1
- **1-M1, ch01.md:240.** The MCP quotation is wrong. Anthropic called MCP "a new standard for connecting AI assistants to the systems where data lives"; "open standard" comes from another sentence.
- **1-M2, ch01.md:246 (Figure 1.3 caption, PDF p. 36).** The source list runs off the page, cut at "861, 87". It is sorted by number, so "in date order" is false. See C3.
- **1-M3, ch01.md:171.** Kasparov did not win the 1996 match "by four games to two". He won 4–2 on points, with three wins, two draws and one loss.

### Chapter 2
- **2-M1, ch02.md:78 and :228.** DeepSeek-V4 is no longer a "preview". Official versions came out on 31 July and 13 August 2026.

### Chapter 3
- **3-M1, ch03.md:448 and Table 3.9.** "The largest open models of 2026" leaves out the two largest: Kimi K3 (2.8 trillion parameters, July 2026) and Qwen3.8 (2.4 trillion, August 2026).
- **3-M2, ch03.md:243.** "FlashAttention saves time but not memory" contradicts the cited paper ("Fast and Memory-Efficient"). It saves both; it does not reduce the quadratic arithmetic or the KV cache.

### Chapter 4
- **4-M1, ch04.md:120 and bib `epochai2026trends`.** Epoch's dashboard was updated on 5 November 2026. The 3.4×/yr installed-compute figure was removed; the new figure is 2.5×/yr for AI chips sold each quarter.
- **4-M2, ch04.md:229 and ch01.md:253.** ClockBench is now led by Claude Fable 5.2 at 87.8%, not Gemini 4 Argon at 83.3%.
- **4-M3, ch04.md:258.** "Best reported HLE scores rose … to 54.8%" is wrong. 54.8% is the top of Scale AI's leaderboard; developers report up to 65.0% with tools.
- **4-M4, ch04.md:82.** The Chinchilla figure is misstated. The paper says "over 4.2 trillion tokens"; its three methods give 3.7, 4.3 and 12.0 trillion.

### Chapter 5
- **5-M1, ch05.md:165 and the Table 5.2 caption.** SWE-bench Pro is presented as the working successor benchmark. OpenAI found about 30% of its public tasks broken (8 July 2026) and withdrew its recommendation; Epoch rated it "Flawed" (1 September).

### Chapter 6
- **6-M1, ch06.md:223, Navier–Stokes credit dispute (fairness).** The book gives OpenAI's 8 September position but omits its 10 September finding that the prompts "could not have influenced the system". "OpenAI denied it" misstates what OpenAI denied.
- **6-M2, ch06.md:227.** The case study is out of date. Buckmaster and Alpöge posted an AI-assisted blow-up proof on 20 November 2026; it is not yet confirmed.
- **6-M3, ch06.md:242.** Beel et al. are misquoted. "a rushed undergraduate paper" is not in the source.
- **6-M4, ch06.md:266.** The AI co-scientist is called "a company preprint", but it was published in *Nature* on 19 May 2026.

### Chapter 7
- **7-M1, ch07.md:116, :133 and the Fig. 7.2 spec.** The Affiliates-rule suspension was extended on 9 November to 10 January 2027, and China matched it.
- **7-M2, ch07.md:128, :143, :316 and the Fig. 7.2 caption.** BIS formally rescinded the diffusion rule, including the model-weights control, on 19 November 2026 (91 FR 74970). It also put remote access to large compute for China-headquartered firms, and five more countries, under licence.
- **7-M3, ch07.md:141 and :242.** Jensen Huang resigned as Nvidia's CEO on 11 November 2026. Write "then chief executive".
- **7-M4, ch07.md:49 and :271.** The Muse Spark Open facts are cited to Meta's April post about a different, closed model. Cite the 15 October post instead.
- **7-M5, ch07.md:326.** The EU call provides for "up to seven" AI gigafactories, not four.

### Chapter 8
- **8-M1, ch08.md:221.** The BLS productivity figures are Q2. The Q3 release of 5 November is available: 3.6% annualised, 2.1% year on year, 2.2% a year since 2019.
- **8-M2, ch08.md:156.** Challenger's October report says AI is no longer the leading reason for 2026 job cuts; market and economic conditions overtook it.

### Chapter 9
- **9-M1, ch09.md:126 and :128.** The US midterms are written as still to come. The chapter also misses the main AI incident of the campaign: the Storm-1516 deepfakes about James Talarico, who won his seat.
- **9-M2, ch09.md:241, :246 and Table 9.3.** The UK has, since 29 June 2026, made it an offence to make or supply intimate-image generators (Crime and Policing Act 2026, s. 99). "Gone further in one respect" is now wrong.

### Chapter 10
- **10-M1, ch10.md:165 and Table 10.3.** New York's AI-companion bill for minors was signed on 28 October 2026 (Chapter 368). This was already wrong at the October cut-off.

### Chapter 11
- **11-M1, ch11.md:213, :217 and :221 (Table 11.3, Anthropic row).** The fourth incident (January 2026, an early Claude Opus 4.6) is missing. So is the independent METR investigation, which was agreed in September.
- **11-M2, ch11.md:218 (OpenAI row).** The row omits the OpenAI test agent's entry into Australia's Medicare statistics portal (18 June, made public 24 September) and OpenAI's own disclosures of 16 September.
- **11-M3, ch11.md:292 and the caption.** Two cases weaken the "who discloses" framing:
  - the 13 November Epoch/Trajectory report on agents that Trajectory Labs identified as Gemini 4 Argon;
  - the 16 November California lawsuit against OpenAI (allegations only).

  The caption should say the list reflects who publishes reports.

### Chapter 12
- **12-M1, ch12.md:249.** The book quotes and criticises Anthropic's July "harness and operational failure" framing. Anthropic withdrew it on 9 September and called the incidents "serious". The fourth incident and the METR investigation are also missing.
- **12-M2, ch12.md:269 and Table 12.5 (legally sensitive).** A truncated GovAI quotation turns Anthropic's conditional commitment into an unconditional one. Restore "…unless we have implemented safety and security measures that will keep risks below acceptable levels".
- **12-M3, ch12.md:273, :280 and :284.** "A pause of a few weeks is so far a single data point" no longer holds. OpenAI shelved GPT-6.1 Astra on 28 September for failing its alignment standards.

### Chapter 13
- **13-M1, ch13.md:238.** Bartz payments were not made "by mid-November". The first instalment, about 70% or $2,203.56 per work, is scheduled for the week of 23 November.
- **13-M2, ch13.md:247.** The Thaler quotation drops "eligible": "requires all eligible work to be authored in the first instance by a human being".
- **13-M3, ch13.md:277.** The EDPB "quotations" come from the press release, not Opinion 28/2024. The Opinion says "insignificant" and uses a "necessity test".

### Chapter 14
- **14-M1, ch14.md:167, :178, :190, :284 and Table 14.4.** "The restrictions so far have come from companies, not law" is wrong. See B1.

## B. Fix across chapters

1. **US export control on Claude Fable 5 and Mythos 5 (12–30 June 2026).** Commerce required a licence for foreign nationals' access, including inside the US. Anthropic switched both models off for all customers until Commerce lifted the control on 30 June, with conditions. It was the first use of export controls to block access to an AI service. The coordinator confirmed this independently (Mayer Brown, Greenberg Traurig, Bloomberg Law, Just Security). No chapter mentions it.
   - Ch. 14 must correct its claim (14-M1).
   - Ch. 7 (export controls) and Ch. 13 (US policy) should each add a sentence.
2. **Anthropic's fourth incident and the METR investigation:** Ch. 11 and Ch. 12 must agree.
3. **The 19 November BIS rule:** Ch. 7 (must) and Ch. 14 (S3).
4. **The US evaluator's name:** NIST now styles it CAISSI. Use one name in Ch. 12 and Ch. 14.
5. **ClockBench:** Ch. 1 and Ch. 4 must give the same figure.
6. **Kimi K3 and Qwen3.8:** Ch. 3 (must) and Ch. 7 (S3).
7. **OpenAI's training pauses:** the August pause and a second one in late September, in Ch. 12 and Ch. 14. Date them consistently and say they were announced, not when they began.
8. **New frontier releases after the cut-off:**
   - Claude Fable 5.2 and Mythos 5.2 (9 November);
   - GPT-6.2 Astra and Sol (17 November);
   - Gemini 4 Carbon general availability (10 November).

   No sentence becomes false except the ClockBench claim, but Section 3.8's caption should say "to the end of October 2026" or name the cut-off you choose.

## C. Production and front matter (coordinator's check of the PDF, 626 pp)

1. **Cover.**
   - The paperback cover and the BoD imprint page exist only on branch `claude/festive-ptolemy-904hwh`, built for 590 pages with a 36.0 mm spine.
   - At 626 pages on the same paper the spine is about 38.2 mm (626/2 × 0.12 mm + 0.6 mm). Rebuild with `--pages 626`, and take BoD's own figure once the project is set up.
   - Bring `cover.py`, the Inter/JetBrains fonts and the imprint changes to `build.py` onto the current branch.
2. **Copyright page (PDF p. 4).** It still prints "ISBN: [to be assigned]" and "Publisher and printer: [imprint details]". The festive branch has BoD's imprint text and an `BOOK_ISBN` variable; merge it.
3. **Captions running off the page.** The source lists under Figure 1.3 (p. 36) and Figure 13.2 (p. 432) are cut at the right margin. The fix is to make `print/srcnotes.lua` / CSS wrap long bracketed lists. Checked every page: no other text touches the edge.
4. **Blank space.**
   - 29 pages have a vertical gap of more than 30% of the page. Some are chapter ends, the rest are figures pushed to the next page.
   - The worst mid-chapter cases are pp. 68, 82, 192, 295 and 332.
   - p. 388 carries only two lines.
   - Worth one layout pass, not blocking.
5. **Index.** Of 1,843 page references, 33 point to a page that does not contain the term. Examples: "Alibaba" 76/77/129, "Dartmouth workshop" 333/450, "United States" 18/227. Regenerate or prune them; not blocking.
6. **Colour.** None found: the interior is greyscale throughout, which fits a black-and-white print order. The PDF header is 1.6 and all fonts are embedded. The PDF/X-4 claim still needs a real preflight (the printer's checker).

## D. Decisions only the author can make

1. **AI disclosure (preface, "How the book was made").** It still says research, drafting and checking were "assisted by AI tools". The chapters were drafted by AI agents and checked by AI reviewers. Say so plainly, and say what human review took place. Print-on-demand platforms such as Amazon KDP require AI-generated text to be declared. Soften "Every factual claim was checked": this review found quotations that did not match their sources.
2. **Copyright line.** "© 2026 Jan Göbel. All rights reserved." Protection for AI-generated text is limited in the US (Thaler v. Perlmutter, D.C. Cir. 2025; US Copyright Office report, 2025). Take legal advice; your own substantial editing strengthens the claim.
3. **ISBN, imprint, about-the-author, acknowledgements.**
4. **Human expert read.** At least one technical and one legal/policy reader. This review is thorough but is itself AI work.
5. **Title.** "Understanding AI" is generic and shared with Timothy B. Lee's newsletter (raised in the second review; still open).

## E. Check again on the day you send the files to the printer

- China's gallium/germanium/antimony ban suspension ends **27 November 2026**; the November extension did not cover it (7-S1).
- Bartz first payments in the week of 23 November (13-M1).
- The BLS revised Q3 productivity figure is due **8 December 2026** (8-M1).
- The Getty v Stability Court of Appeal judgment is reserved (13-S1).
- The ROSS rehearing petition at the Third Circuit is pending (13-S2).
- The METR investigation of the Anthropic incidents has published no findings yet (11-M1).
- Any new frontier release after your chosen cut-off.
- One sentence about a named candidate rests on secondary reports (9-M1, Talarico deepfake): confirm it against NewsGuard's own post.

## F. Should-fix items

About 100 smaller items: imprecise wording, a source that supports a slightly weaker claim, a newer figure, a missing bib detail. They are in the SHOULD sections of each report. None is blocking, but several touch named people or companies and are cheap to fix:
- 6-S4: name Alpöge's employer;
- 6-S6: the EMS wording;
- 12-S2: AISI's "completed" vs "attempted";
- 13-S6: attribute the lab incidents to Euronews;
- 14-S6: the Stanford brief's duty of loyalty.

Doing them all is recommended.
