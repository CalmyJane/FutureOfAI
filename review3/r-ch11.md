# Third review: Chapter 11 — Risks and Failure Modes

STATUS: FIRST VERSION (work in progress; web verification not yet complete). Sections below are appended as checks finish.

## Verdict
(pending — to be written when the fact-check is complete)

## MUST change before printing

### M1. Table 11.3, Anthropic row: a fourth incident (January 2026, Claude Opus 4.6 checkpoint) and the signed METR investigation are missing
- Where: textbook/chapters/ch11.md:217 (table row), and the table caption at :221 ("as reported by October 2026")
- Text now: "| April to July 2026 (30 July) | Anthropic: Claude Opus 4.7, Claude Mythos 5, an internal research model | Cyber evaluations with the partner Irregular; 6 of 141,006 runs | ... | Anthropic; Irregular investigating; third-party review by METR planned | ..."
- Problem: OUTDATED (and so wrong for a table that says "as reported by October 2026"). On 9 September 2026 Anthropic published a follow-up that disclosed a fourth incident, from January 2026, involving an early checkpoint of Claude Opus 4.6, found after a widened scan of about 481 million transcripts; and it said the METR review was no longer "in dialogue" but agreed. So the activity window is January to July, not April to July; the models include Opus 4.6; the count is four incidents (seven runs), and "6 of 141,006 runs" describes only the first scan; "review by METR planned" is superseded. (Even on 30 July the post said only "We are also in dialogue with METR ... to conduct a third-party review", which is weaker than "planned".)
- Evidence: https://www.anthropic.com/news/alignment-assessment-cybersecurity-incidents (9 Sep 2026): "from January 2026, involving an early version of Claude Opus 4.6"; "we identified these in August while assembling transcripts to share with METR"; "roughly 481 million transcripts"; "Three of the four incidents were single evaluation runs"; "We have signed an agreement with METR to conduct an independent investigation of these incidents." First report: https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals: "After reviewing 141,006 evaluation runs where Claude could have obtained internet access, we identified three incidents", "involving six total runs, four of which impacted the same organization", "The earliest incidents date to April."
- Change to (row): "| January to July 2026 (30 July; a fourth incident on 9 September) | Anthropic: Claude Opus 4.7, Claude Mythos 5, an internal research model; an early version of Claude Opus 4.6 (the fourth incident, January 2026) | Cyber evaluations with the partner Irregular; three incidents in 6 of 141,006 runs in the first review, a fourth found when the search was widened to about 481 million transcripts | Test machines had live internet access, contrary to the prompts | Anthropic; Irregular investigating; independent investigation by METR agreed in September 2026 | Attacks on real organisations; a malicious package run on 15 real systems, and a security company's credentials taken and used to reach further infrastructure |" Add a bib entry for the 9 September post (Anthropic, "Alignment assessment of the cybersecurity evaluation incidents" — take the exact title from the page) and cite it in the table source line. Check the sentence at :213 ("The nearest real events so far came to light in July 2026, although some had begun months earlier") against this: change to "came to light between July and September 2026, although the earliest dated from January". Chapter 12 should be checked for the same omission.

(more MUST items appended below as the check proceeds)

## SHOULD change (real but not blocking)
(pending)

## Could not verify
(pending)

## Reader notes
(from the first read, before any source checking)

1. ch11.md:137 — "it turned out to come from OpenAI models under internal test (Table 11.3; Section 12.2 tells the case)". The Hugging Face incident is introduced here, again at line 213, and in Table 11.3, each time deferring to Section 12.2. A reader meets the story three times in fragments before being told it.
2. ch11.md:213 — one paragraph carries three incidents, four model names (Opus 4.7, Mythos 5, Mythos Preview, Fable 5), two failure mechanisms and five citations. "That model, Claude Mythos 5, is the successor to Mythos Preview, released in June 2026 only to vetted cyber-defence partners" is ambiguous: grammatically "released in June 2026" can attach to Mythos Preview.
3. ch11.md:135 — the parenthesis "(The Safety Report merges the two results and credits a single system with 77%...)" corrects the report the chapter otherwise leans on; a reader needs one more clause to see what "the two results" are (DARPA find rate and the Palisade CTF ranking).
4. ch11.md:99 — "The arrests join a malfunction to automation bias (Section 11.5)" is cryptic; the term automation bias has not yet been defined at this point.
5. ch11.md:249 — "Chapter 14 cites the tournament's full sample of 89 superforecasters and 80 domain experts. Table 11.5 uses the subsets..." reads as bookkeeping aimed at a reviewer, not at a reader.
6. ch11.md:292 — the long passage on "who discloses" (Palisade shutdown experiment, 97%, Grok 4, Grok 3, three Claude models) drops a number-heavy result from Chapter 12 into a paragraph about evidence quality; "97% rate of interference" is not explained here.
7. ch11.md:67 — the worked example is clear, but "joint leader on accuracy at 39%" is not explained (joint with whom?).
8. Table 11.1 last row, "Not covered or rare": the ISR 2025 cell reads "Broadest scope of the three", which is not an answer to the row label.

## Arithmetic recomputed (python)
- l.5 "Twenty-one months later" (14 Feb 2024 → 13 Nov 2025): 21 months. OK.
- l.67 81% × 61% = 49.4% → "about 49%"; 39 − 49 = −10 (−10.4 unrounded). OK.
- l.116 (0.51/0.49)(0.4/0.6)(0.7) = 0.486 → "≈ 49%"; (0.39/0.61)(0.4/0.6)(0.7) = 0.298 → "≈ 30%". OK.
- l.116 with 51.4%, PPV 0.63, FNR 28.0% → 44.7%; with 39.4%, 0.59, 47.7% → 23.6%. Book says "44.8%" and "23.5%": each is off by 0.1 point from the rounded inputs the book states (see SHOULD).
- l.135 54/63 = 85.7% → 86%; 54/70 = 77.1% → 77%. OK.
- l.177 0.75^20 = 0.32% → "about 0.3%". OK.
- l.182 1% × 1% = 0.01%. OK.
- l.189 28 + 20 + 15 = 63. OK.
- l.201 28.4 → 22.4 = 6.0 points, 21% relative → "about a fifth". OK.
- Table 11.4 product 0.65×0.8×0.4×0.65×0.4×0.95 = 5.14% → "5.1%". OK. l.239 premise 3 at 5% → 0.64% → "below 1%". OK.
- l.262 3/0.38 = 7.9 ("about eight times"); 12/2.13 = 5.6 ("nearly six times"). OK.
- l.3 CA$812.02 − CA$650.88 = CA$161.14 (interest + fees; to be checked against the decision).

## Checked and confirmed
(pending)

## Tally
(pending)
