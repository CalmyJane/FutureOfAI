# Third independent read and fact-check: one chapter per reviewer

Today is 11 November 2026. The book is about to go to print.

**Book:** "Understanding AI: Technology, Trends and the Decade Ahead" (Jan Göbel), a 626-page, heavily sourced nonfiction book on AI. It says it is current to the end of October 2026. Repo: `/home/user/FutureOfAI`, book in `textbook/`.

**The author's question:** "Read it again as an independent reader and fact-check all the statements. Is it ready to publish? If not, tell me exactly what must definitely be changed."

You review ONE chapter (given in your task). You are a fresh, demanding reader and fact-checker. The text was drafted with heavy AI assistance and has had two earlier reviews, so the easy errors are gone. What remains is likely to be subtle: a number that is close but not what the source says, a claim attributed to the wrong paper, a quotation that is a paraphrase, a 2026 event that changed after the text was written, an overstatement of what a study found, or a reference that does not say what it is cited for.

## Your files
- `textbook/chapters/chNN.md` — the chapter (pandoc Markdown; citations are `[@key, pinpoint]`). Read ALL of it, in order, first.
- `textbook/bib/chNN.bib` — its references (most have a URL or DOI).
- `textbook/figures/specs/fig-NN-*.md`, `tbl-NN-*.md` and `textbook/figures/svg/fig-NN-*.svg` — figures (grep the SVG for `<text`/label strings rather than reading it whole; many SVGs render text as paths, in which case use the spec and `textbook/print/figs_chNN.py`, which holds the plotted values).
- `textbook/work/glossary-chNN.md` — glossary entries for this chapter.
- `textbook/work/evidence-chNN.md` — the author's log of earlier checks. It is large: grep it for a claim when you want a lead to a source. Treat it as leads, not as truth.

Do NOT read `review/`, `review2/`, `textbook/work/panel*/` or other files in `review3/`: your read must be independent. Do NOT edit any book file. Do NOT commit to git. Your only output is your report file.

## Tools
Load web tools first: ToolSearch with query `select:WebFetch,WebSearch`. Useful endpoints: Crossref `https://api.crossref.org/works/<doi>`, arXiv `https://export.arxiv.org/abs/<id>`, Semantic Scholar, the URL in the bib entry. If a page blocks you, try the arXiv/PDF version, an official mirror, or a web search for the exact figure. WebSearch `mode: "standard"` by default; `"extended"` only for hard, very recent items.

## What to do

### 1. Read as a reader (first)
Read the whole chapter once, start to finish, as a curious non-specialist who paid for the book. Note where you stumble: an unexplained term, a contradiction with something said earlier in the chapter, a paragraph that repeats, a sentence that reads as machine-written filler, a number dump, a cross-reference that points nowhere, a figure or table that does not match the text around it.

### 2. Fact-check (the main job)
Go through the chapter section by section and check its checkable statements against sources. The goal is coverage of the whole chapter, not a small sample.

- **Must be web-verified against a source, every one:** each number, date, name, ranking, quotation and legal provision about events from 2025 and 2026; every direct quotation of any date; every claim about what a named living person or a named company did or said that could harm their reputation; every "first", "largest", "only", "record" claim.
- **Older, settled material** (history, textbook mechanisms, classic papers): check against your own knowledge as you read, and web-verify anything specific where you have the slightest doubt (years, author names, parameter counts, benchmark scores, who did what first).
- **Arithmetic and worked examples:** recompute every one (use Bash/python).
- **Tables and figures:** check values against the cited source and against the running text.
- **Reference check:** for at least 25 bib entries (prefer 2025–2026 ones and anything odd-looking), confirm the work exists and that authors, title, year, venue match. For the claims you check, confirm the cited source actually supports the sentence it is attached to, including the pinpoint where one is given.
- **Currency:** for every statement about a state of affairs that can change (which model leads, a law's status, a pending case, a deadline, a user count, a suspended rule, an election, a planned release), search for news between 25 October and 11 November 2026 and say whether it still holds. The US midterm elections were on 3 November 2026; any forward-looking statement about them is now stale.
- Aim for at least 120 claims checked against a web source, and more if you can. Work efficiently: fetch a cited source once and check all claims that rest on it.

**Your own knowledge has a cutoff.** The book covers events up to late October 2026 that you may not know. An unfamiliar 2026 model, law or incident is NOT an error unless a web search fails to find it or a source contradicts it. Equally, never mark a 2025–2026 claim "confirmed" from memory: confirm from a source or mark it unverified.

### 3. Judge fairness and legal exposure
Flag any negative statement about a named person or organisation that is stronger than its source, any company claim presented as established fact, and any one-sided treatment of a live dispute.

## Report
Write to `/home/user/FutureOfAI/review3/r-chNN.md`. Save a first version early and keep appending, so that nothing is lost if you run out of room.

```
# Third review: Chapter N — <title>

## Verdict
One of: ready to print as is / ready after the MUST fixes below / needs more work. Three to five sentences of reasons.

## MUST change before printing
Only things that are verifiably wrong, outdated as of 11 Nov 2026, unsupported by their cited source, legally risky, or that would embarrass the author in front of an expert. Each item:
### M1. <short title>
- Where: textbook/chapters/chNN.md:LINE
- Text now: "exact quote"
- Problem: what is wrong (state whether VERIFIED WRONG, OUTDATED, UNSUPPORTED BY CITED SOURCE, or INTERNAL CONTRADICTION)
- Evidence: URL + the exact words or number in the source
- Change to: "exact replacement text" (and any bib change)

## SHOULD change (real but not blocking)
Same format, briefer.

## Could not verify
Claims you tried to check and could not (blocked page, paywall, no source found). Location, quote, what you tried. Say which of these matter enough that a human should check them before printing.

## Reader notes
At most ten points from your first read: where a reader stumbles or loses trust. Quote the text.

## Checked and confirmed
A compact list (one line each) of the claims you verified as correct, grouped by section, with the source used. This is the evidence that the check covered the chapter.

## Tally
Claims checked against a web source: N. Confirmed: N. Wrong: N. Outdated: N. Unsupported by cited source: N. Could not verify: N. Arithmetic items recomputed: N (errors: N). Bib entries checked: N (problems: N).
```

Rules for the report:
- Quote the book's text exactly and give the line number.
- Never report something as wrong on the strength of memory or a search snippet alone: open the source. If two sources disagree, say so and name the better one.
- Give the exact replacement wording, so the author can apply it without further research.
- No padding, no praise beyond the verdict, no general advice.

Your final message to the coordinator (it is not shown to the author directly): the verdict, the tally line, and every MUST item in one line each (location, what is wrong, the fix), in at most 30 lines.
