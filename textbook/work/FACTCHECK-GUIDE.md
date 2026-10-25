# Fact-check guide

You are the independent fact-checker for ONE chapter of the course text *Understanding AI* (current to 22 October 2026). Files: `chapters/chNN.md`, `bib/chNN.bib`, `work/evidence-chNN.md` (the writer's log), and the writer's flags given in your prompt. Writer guide for context: `work/WRITER-GUIDE.md`.

The shared WebSearch budget is exhausted: do NOT call WebSearch. Use WebFetch on URLs/DOIs from the bib and evidence log, plus metadata APIs (https://api.crossref.org/works/DOI, https://export.arxiv.org/api/query?id_list=ID, https://api.openalex.org/works/doi:DOI, https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&format=json, PubMed). If a domain blocks you (403), try an alternative mirror (arXiv, PMC, Crossref abstract, OpenAlex, publisher DOI page, Wayback Machine `https://web.archive.org/web/2026/URL`).

## Work through, in this order
1. **Writer's flags** (in your prompt): resolve each one. Verify, correct, soften, or cut.
2. **Every number, date, quotation and attribution** in the chapter: check it against the source. Prioritise numbers in figures and specs (`figures/specs/fig-NN-*.md`) too. Correct wrong values in the chapter, spec and caption (if a figure's data changes, list it in your report so the figure is redrawn).
3. **Bibliography**: every entry must have correct authors, year, title, venue (volume/issue/pages where they exist), and a working DOI or URL. Fix entries. Preprints that have since been published at a peer-reviewed venue should cite the published version (update the text label "preprint" accordingly). Keep keys unchanged unless a key is wrong in a way that matters; if you change a key, change every use in the chapter.
4. **Evidence labels**: preprints labelled as preprints; company claims as "according to the company"; opinions attributed.
5. **Claims without citation** that need one: add a verified source or cut/soften the claim.
6. **Errors of reasoning or emphasis**: overstated causal claims, one-sided debates, outdated "latest" claims (as of Oct 2026).
7. **Safety**: no operational detail on weapons, pathogens, toxins, cyber-attack techniques or self-harm.

## Rules
- Edit only your chapter's files (`chapters/chNN.md`, `bib/chNN.bib`, `work/evidence-chNN.md`, `figures/specs/fig-NN-*.md`). Use the Edit tool for targeted changes; keep the writer's voice and structure. Do not restructure; do not add new sections.
- If you cannot verify a claim at all, cut or soften it. Never leave an unverified number.
- Add a section `## Fact-check (date)` at the end of the evidence log listing each change and each remaining uncertainty.
- After editing, run `cd /home/user/FutureOfAI/textbook && pandoc chapters/chNN.md --citeproc --bibliography bib/chNN.bib -o /dev/null` and confirm no warnings.
- Report: number of claims checked, list of corrections (old → new), cuts, figure data changes, and remaining uncertainties. Do not commit.
