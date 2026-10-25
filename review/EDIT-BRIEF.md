# Editing brief: applying the review to *Understanding AI*

Repo: /home/user/FutureOfAI (branch claude/epic-brown-l6rmum). Book source: textbook/.
You are an expert editor and fact-checker revising your assigned chapters so that every item in the review is fixed.

## Your files (edit ONLY these)
- textbook/chapters/chNN.md for your chapters
- textbook/bib/chNN.bib for your chapters
- textbook/print/figs_chNN.py and textbook/figures/specs/fig-NN-*.md / tbl-NN-*.md for your chapters
- textbook/work/evidence-chNN.md and textbook/work/glossary-chNN.md for your chapters
Never edit other chapters, the preface, build scripts, or anything outside textbook/. Do NOT git commit, push, or run the PDF build. Other editors are working on other chapters at the same time.

## What to do
1. Read the review file for your chapters (path given below) in full, and the overview `review/00-OVERVIEW.md` (sections 1.3, 1.4, 1.6, 1.9) for book-wide rules.
2. Fix EVERY item in sections A–E of your review: factual errors, omissions, selective reporting, conceptual problems, writing, structure/coverage gaps, figures/tables. Where the review offers wording, you may use it, but check it.
3. Verify before you write. For each correction or new claim, check the primary source online (WebFetch/WebSearch; load with ToolSearch "select:WebFetch,WebSearch"; Crossref API https://api.crossref.org/works/<doi>, arXiv https://export.arxiv.org/abs/<id>). If the reviewer was wrong, do not make the change; note why in the evidence log. If a source cannot be accessed, phrase cautiously and note it in the log. Never invent numbers, quotes or references. Every new reference gets a complete, correct bib entry (with DOI or URL) in your chapter's bib.
4. Add the coverage the review asks for, but concisely (a paragraph or a short box, not a new section unless the review says so). Keep each chapter's length roughly where it is: cut number dumps and repetition to pay for additions. Target: no more than ~3 numbers in a paragraph of running prose; move detail to tables.
5. Writing rules: en-GB spelling; replace most mid-sentence colons with full stops or proper connectives (keep colons only before lists or a genuine expansion); paragraphs open with a topic sentence stating the point; define every technical term at first use; remove all revision-history traces ("earlier versions said…", "truncated", notes to self). Keep the author's sober, precise voice. No filler, no hype.
6. Citations: keep pandoc keys `[@key]` exactly as now (the build turns them into numbered page-foot source lines). Every factual sentence you add must carry a citation. Table and figure captions keep their "Source: [@key]" form.
7. Log every change (one line each: what changed, why, source URL) under a new heading `## Revision after external review (Oct 2026)` at the end of your evidence log(s). Fix any log lines that disagree with the text.
8. If you change a figure script, run `python3 -m py_compile textbook/print/figs_chNN.py` to check syntax (the figures will be redrawn centrally). Keep specs in sync.

## Book-wide conventions (apply in your chapters)
- Percentages: write "%" (not "per cent") in running prose, tables and captions.
- Company name "Nvidia" in prose (NVIDIA only inside a product name if the product uses it).
- US dollars: "$" (e.g. $48, $1.2 billion); no "US$" or "USD". Euros "€", pounds "£".
- GPT-3 training compute: 3.14 × 10^23^ FLOP (Brown et al. 2020).
- ClockBench human baseline: 90.7% (check clockbench.ai once; if the page says otherwise use the page and log it).
- ChatGPT weekly users: the latest figure is 1.2 billion (OpenAI, late Sept 2026). Older figures are fine only when dated ("in October 2025, with more than 800 million weekly users…").
- Deep learning history: convolutional networks were in commercial use for reading cheques in the 1990s (LeNet); 2011–2012 (speech recognition, then ImageNet) marks the start of the modern deep-learning wave. Do not call 2011 speech the "first practical success".
- Evidence labels (the preface is being extended to say this): at FIRST mention in each chapter, label (a) preprints ("a preprint", "an unreviewed paper"), (b) working papers ("a working paper"), (c) company claims ("according to the company", "the company reports", "OpenAI says" — any clear attribution), (d) news reports where they are the only source ("according to Reuters"), (e) leaderboards and company usage data ("on the LMArena leaderboard", "OpenAI's own usage figures"), (f) bank/consultancy research. Go through every company, arXiv, NBER/SSRN/working-paper and news key in your chapter and check its first mention.
- Company material must get the same scepticism as anything else: report companies' own failures and critics as fully as their successes; disclose an interested party's stake when quoting them.
- Selective-reporting rule: whenever you use a study, check that the number you give is the headline finding of its abstract. If you give a different number, also give the headline one and say why.

## Final message
Return a concise summary (≤25 lines): what you changed per review item group, any review items you rejected (with reason), any items left undone, new references added, and anything the central editor must handle (preface, build, cross-chapter facts).
