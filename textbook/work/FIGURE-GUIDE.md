# Figure drawing guide

You draw figures for the course text *Understanding AI* from specs in `figures/specs/fig-NN-MM.md`.

- Code: `print/figs_chNN.py` (one module per chapter; create it if missing, copying the import header of `print/figs_ch05.py`). Register each figure with `@fig("fig-NN-MM")` and end it with `save(fig, "fig-NN-MM")` (diagrams via `canvas()`) or `F.save(fig, ...)` (charts via `F.figure()` + `fig.add_axes`). Read `print/figstyle.py` (house style and helpers) and `print/figs_ch02.py`, `print/figs_ch05.py` as examples. Do not edit figstyle.py, figures.py or other chapters' modules.
- Draw: `cd textbook/print && python3 figures.py fig-NN-MM ...` → `figures/svg/fig-NN-MM.svg`.
- Check visually: `python3 preview.py /tmp/claude-0/-home-user-FutureOfAI/e5cd2544-62ba-505f-83f9-34211b2169e5/scratchpad/<name>.png fig-NN-MM ...` then Read the PNG. Iterate until there are NO overlapping labels, no text crossing lines or boxes, no clipped text, and nothing too small (min font ~5.8 pt; figures are printed 113 mm wide on A5).
- Style: greyscale only (INK, G1–G4), EB Garamond, thin lines, generous whitespace. Simple beats complete: if a spec has more elements than fit legibly, drop decoration, never data. Width is fixed (4.45 in); choose height 2.2–3.6 in.
- Data: plot exactly the numbers in the spec. Never invent data. Schematic charts need no numeric axes.
- **Table-figures:** do NOT draw them. Instead convert into a pandoc pipe table placed in the chapter Markdown where the image reference was, with caption line `: Table N.M: caption {#tbl:NN-MM}` directly after the table; keep it to ≤5 columns and short cell text (merge or drop the least important column, e.g. source keys go into the caption). Replace "Figure N.M" references in that chapter's text with "Table N.M" and renumber the remaining figures in that chapter (files, ids, captions, in-text references) so they run 1, 2, 3 without gaps.
- Report: list of figures drawn, any spec content you dropped or changed, and any table conversions.
