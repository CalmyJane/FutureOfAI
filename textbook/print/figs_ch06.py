"""Figures for chapter 6, drawn from figures/specs/ in the house style."""
import math

import numpy as np
from matplotlib.patches import Ellipse

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


@fig("fig-06-01")
def f0601():
    fig, ax = canvas(3.6, ylim=(0, 86))
    cx, cy = 50, 45
    W, H = 19, 8
    # stage centres, clockwise from the top
    P = [(50, 76), (76, 61), (76, 29), (50, 14), (24, 29), (24, 61)]
    stages = ["Read\nliterature", "Form\nhypothesis", "Design experiment\n/ simulation", "Collect\ndata",
              "Analyse\ndata", "Publish\nand review"]
    # AI-job tags, placed outside each box: (x, y, ha)
    tags = [("Automate: search, summarise", 50, 83, "center"),
            ("Search: propose\ncandidates", 87.4, 61, "left"),
            ("Emulate: fast\nsurrogate", 87.4, 29, "left"),
            ("Predict: fill gaps", 50, 6.6, "center"),
            ("Automate:\nwrite code", 12.6, 29, "right"),
            ("Automate:\ndraft, review", 12.6, 61, "right")]
    checks = ["Check\nsources", "Expert\njudgement", "Compare with\nreality", "Test on\nheld-out data",
              "Read the\ncode", "Independent\nreplication"]
    ax.add_patch(Ellipse((cx, cy), 36, 44, fc=G4, ec=G2, lw=0.6, ls="--"))
    label(ax, cx, cy, "Scientific\ncycle", fs=9.5)
    CP = [(50, 61), (59.5, 52.5), (59.5, 37.5), (50, 29), (40.5, 37.5), (40.5, 52.5)]
    for i in range(6):
        x, y = P[i]
        box(ax, x - W / 2, y - H / 2, W, H, stages[i], fill="white", fs=6.8)
        t, tx, ty, ha = tags[i]
        label(ax, tx, ty, t, fs=6, italic=True, color=G1, ha=ha)
        label(ax, CP[i][0], CP[i][1], checks[i], fs=6)
    # clockwise arrows between the stage boxes
    A = [((60.4, 75), (68, 65.6), -0.25), ((76, 56.4), (76, 33.6), 0), ((68, 24.4), (60.4, 15), -0.25),
         ((39.6, 15), (32, 24.4), -0.25), ((24, 33.6), (24, 56.4), 0), ((32, 65.6), (39.6, 75), -0.25)]
    for (x0, y0), (x1, y1), rad in A:
        arrow(ax, x0, y0, x1, y1, lw=0.8, rad=rad)
    label(ax, 50, 1.4, "Outer tags = AI job; inner ring = verification", fs=6.3, italic=True, color=G1)
    save(fig, "fig-06-01")


@fig("fig-06-02")
def f0602():
    # timeline (spec fig-06-03; renumbered after fig-06-02 became Table 6.1)
    fig, ax = canvas(3.2, ylim=(0, 72))
    ev = [
        ("Jun 2023", "AlphaDev", "Faster sorting routines\nadded to LLVM C++ library", "p"),
        ("Dec 2023", "FunSearch", "Larger cap sets than\npreviously known", "p"),
        ("Jan 2024", "AlphaGeometry", "25 of 30 olympiad\ngeometry problems", "p"),
        ("Jul 2024", "AlphaProof +\nAlphaGeometry 2", "IMO 28/42 (silver level);\nup to 3 days' computing", "c"),
        ("May 2025", "AlphaEvolve", "4×4 complex matrices\nwith 48 multiplications", "c"),
        ("Jul 2025", "Gemini Deep Think", "IMO 35/42 (gold); natural\nlanguage; certified", "c"),
        ("Nov 2025", "AlphaEvolve with\nTao et al.", "67 problems; several\nimproved (PNAS 2026)", "c"),
        ("Jan 2026", "GPT-5.2 Pro +\nAristotle", "Erdős #728 (intended\nversion) proved in Lean", "l"),
    ]
    y0 = 37
    ax.plot([2, 98], [y0, y0], color=INK, lw=0.9)
    r = fig._get_renderer()
    inv = ax.transData.inverted()

    def height(t):
        bb = t.get_window_extent(renderer=r)
        return inv.transform((0, bb.y1))[1] - inv.transform((0, bb.y0))[1]

    for i, (d, n, t, k) in enumerate(ev):
        x = 8 + i * 12
        up = i % 2 == 0
        sgn = 1 if up else -1
        ax.plot([x, x], [y0, y0 + sgn * 6], color=G2, lw=0.6)
        if k == "p":
            ax.plot([x], [y0], "o", color=INK, ms=4.5)
        elif k == "c":
            ax.plot([x], [y0], "o", mfc="white", mec=INK, ms=4.5)
        else:
            ax.plot([x], [y0], "s", color=INK, ms=4.5)
        # stack away from the axis: date, then name, then description; each block measured
        yy = y0 + sgn * 7
        va = "bottom" if up else "top"
        for txt, kw, gap in ((d, dict(fontsize=6.3, color=G1), 0.6),
                             (n, dict(fontsize=7.2, linespacing=1.05), 0.9),
                             (t, dict(fontsize=5.9, linespacing=1.12), 0)):
            h = ax.text(x, yy, txt, ha="center", va=va, **kw)
            yy += sgn * (height(h) + gap)
    from matplotlib.lines import Line2D
    h = [Line2D([], [], ls="", marker="o", color=INK, ms=4, label="peer-reviewed paper"),
         Line2D([], [], ls="", marker="o", mfc="white", mec=INK, ms=4, label="company announcement / preprint"),
         Line2D([], [], ls="", marker="s", color=INK, ms=4, label="Lean-verified proof")]
    ax.legend(handles=h, loc="lower center", ncol=3, fontsize=6.3, bbox_to_anchor=(0.5, -0.02),
              handletextpad=0.3, columnspacing=1.2)
    save(fig, "fig-06-02")
