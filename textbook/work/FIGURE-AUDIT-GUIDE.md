# Figure audit guide

You are the independent auditor (and fixer) for the figures of ONE or TWO chapters of the book *Understanding AI* (current to October 2026). Mistakes in figures are easy to make; your job is to find and fix every one.

Files: specs `figures/specs/fig-NN-*.md` (and `tbl-*` for converted tables, which are Markdown tables in the chapter); drawing code `print/figs_chNN.py` (house style and helpers in `print/figstyle.py`, examples in other `print/figs_ch*.py`); output `figures/svg/fig-NN-MM.svg`; chapter text `chapters/chNN.md` (captions are the `![Figure N.M: …](figures/fig-NN-MM.svg){#fig:NN-MM}` lines); evidence log `work/evidence-chNN.md`.

Draw: `cd /home/user/FutureOfAI/textbook/print && python3 figures.py fig-NN-MM`. Render for checking at 300 dpi: `python3 preview_hi.py /tmp/claude-0/-home-user-FutureOfAI/e5cd2544-62ba-505f-83f9-34211b2169e5/scratchpad/<name>.png fig-NN-MM` and Read the PNG (crop with ImageMagick `convert in.png -crop WxH+X+Y out.png` to inspect details).

## For every figure in your chapters
1. **Draw any figure whose spec exists but has no code or SVG** (new figures from the deepening pass), and redraw any whose spec changed. Check that every `figures/fig-NN-MM.svg` referenced in the chapter exists and that numbering is sequential in order of appearance; spec file names/headers must match.
2. **Data against source.** For data charts, check every plotted value, label, unit, date and axis scale against the spec AND against the cited source itself (re-open the source via WebFetch / data files / Crossref; WebSearch is unavailable; `https://r.jina.ai/https://…` can read pages that block fetches). Check derived numbers by computation. Check that bars/points are drawn at the right values (read the code; look at the rendered axis positions).
3. **Content against text.** Labels, numbers, names and dates in the figure must agree with the chapter text and caption. The caption must describe exactly what is drawn, name its source, and say "schematic, not to scale" where applicable. Diagrams must be technically correct (e.g. arrows in the right direction, correct component names, correct counts such as parameters or layers).
4. **Legibility and craft.** No overlapping or clipped text, no text crossing lines or boxes, minimum font ~5.8 pt at print size (113 mm width), consistent greyscale house style, legend entries matching marks, sensible axis ticks, no orphan symbols, correct spelling (British), consistent capitalisation.
5. Fix problems: edit `print/figs_chNN.py` (only your chapters' modules), the spec, and if needed the caption in the chapter (captions only; do not change other text — if the TEXT is wrong, report it). Redraw and re-check at 300 dpi until clean.
6. Also check the Markdown tables in your chapters (values against source, caption, numbering).

## Report
For each figure/table: OK, or what was wrong and how it was fixed (with the source checked). List anything you could not verify and any text errors you found but did not fix. Do not commit.
