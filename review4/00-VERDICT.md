# Fourth review: verdict (26–27 November 2026)

The fourth review was planned for the Fable 5.2 model. The account's Fable usage limit was reached before any reviewer could start, so the review ran on Opus 5.5. It used eight fresh reviewers. Seven each covered two chapters (the first also covered the preface), and one did whole-book production and disclosure. None of them had seen the earlier reviews or work logs. A Fable 5.2 review is scheduled for after the limit resets (2 December 2026) and will write to `review5/`.

## Overall verdict: ready to print after the fixes below, all of which have been applied

| Ch. | MUST | SHOULD | Main points |
|---|---|---|---|
| Preface | 2 | 3 | The disclosure must give the correct number of review rounds and must not overclaim the checking. Add who "the author" is in "calculation by the author". |
| 1 | 0 | 3 | Go row of Table 1.3 ("without handicap"); ClockBench runner-up; a cross-reference in Ch. 4 |
| 2 | 0 | 1 | DeepSeek-V4-Pro figures attributed to the technical report |
| 3 | 0 | 5 | xAI renamed SpaceXAI, then SpaceXSI; anti-distillation safeguard dated to Fable 5.1; Sora shutdown; primary sources for November releases |
| 4 | 0 | 2 | Cross-reference to Section 1.7; HLE leaderboard date |
| 5 | 0 | 5 | OSWorld figures not comparable; SWE-bench Pro date; two slight overstatements; a typo |
| 6 | 0 | 4 | Missing claimed Riemann-hypothesis Lean proof and Anthropic's zeta-zeros result (balance); spliced quotation; ECMWF wording; date of a statement |
| 7 | 2 | 8 | Ironwood quotation ("more than 24x"); Kimi K3 4-bit training scope; gallium/germanium suspension due to expire 27 November; Three Mile Island; "first use" attributed |
| 8 | 2 | 2 | Dell'Acqua "19 percentage points"; METR's confidence intervals |
| 9 | 0 | 1 | NewsGuard count dated to its June update |
| 10 | 0 | 1 | State lawsuits: eleven over harms to children, plus California's separate suit |
| 11 | 0 | 3 | Hallucination-case count; sources for the October outside review; the later colonoscopy trial |
| 12 | 0 | 4 | "At least 80 times"; Safety Report authorship; GPT-6 Sol date source; OpenAI's Frontier Governance Framework |
| 13 | 1 | 4 | State-lawsuit count (fixed before the report arrived); GPT-5.6 Sol release status; Euronews summary; Demirer revision; Clearview dates |
| 14 | 0 | 3 | GPT-5.6 Sol; unsupported "due in October"; source for the UK scenarios |
| Production | 4 | 9 | ISBN placeholders; imprint overflowed onto p. 5; preface review count; index errors (Contents page indexed, mixed word senses); back-cover caveat; copyright line; blank gaps; index cap note and duplicate entries; consistency |

**Totals:** 11 MUST and 58 SHOULD items. No invented sources were found. Every worked example and calculation recomputes.

## Applied
- **Every chapter MUST and SHOULD item:**
  - each is logged under "Fourth review fixes" in `textbook/work/evidence-chNN.md`;
  - the Chapter 6 Riemann-hypothesis item was added only as far as its facts could be confirmed from primary sources (see the Ch. 6 evidence log).
- **Production:**
  - The imprint now fits on p. 4. The copyright padding is reduced, leaving room for BoD's FSC logo.
  - Boxes may now break across pages. This removes the large blank gaps; the book is now about 632 pages, down from 646.
  - The index:
    - no longer cites the Contents page;
    - counts ambiguous terms ("bias", "epoch", "circuit", "momentum", "feature", "environment") only in the chapters that use the technical sense;
    - drops "resolution";
    - turns duplicates into "see" references;
    - renames "Copyright cases" to "copyright";
    - restricts "Dartmouth" and "Epoch AI";
    - gains a note on how frequent entries are shortened.
  - The back cover now says "No independent human expert has reviewed it". Its barcode placeholder text appears only on the guides proof.
  - The copyright line is narrowed to the author's human-authored contributions, pending legal advice.
  - The preface and the copyright page now state:
    - four review rounds;
    - that sources were checked only where they could be read online;
    - that the figures, index and cover were made by the same AI agents;
    - who "the author" is.

## Still open (author)
1. **ISBN.** Get the ISBN from BoD, rebuild the interior and the cover with it, and use BoD's spine width.
2. **Model list in the disclosure.** The disclosure says "chiefly Claude Opus 5.5 and Claude Fable 5.2". Fable 5.2 was released on 9 November 2026, after the work began on 20 October. If you know which other models were used, name them.
3. **"Approved the text for publication."** If you read the whole book, say "read and approved".
4. **Copyright line:** take legal advice.
5. **Human expert read:** none yet. If one happens, change the preface sentence.
6. **Proof-day checks:** see `textbook/delivery/README.md`.
