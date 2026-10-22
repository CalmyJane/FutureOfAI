"""Figures for chapter 6, drawn from figures/specs/ in the house style."""
import math

import numpy as np

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


@fig("fig-06-01")
def f0601():
    fig, ax = canvas(3.6, ylim=(0, 80))
    cx, cy, R, r = 50, 40, 30, 15
    stages = ["Read\nliterature", "Form\nhypothesis", "Design experiment\n/ simulation", "Collect\ndata", "Analyse\ndata", "Publish\nand review"]
    tags = ["automate: search,\nsummarise", "search: propose\ncandidates", "emulate: fast\nsurrogate", "predict: fill\ngaps", "automate: write\ncode", "automate: draft,\nreview"]
    checks = ["check\nsources", "expert\njudgement", "compare with\nreality", "held-out\ndata", "read the\ncode", "independent\nreplication"]
    import math
    ax.add_patch(F.Circle((cx, cy), r, fc=G4, ec=G2, lw=0.6, ls="--"))
    label(ax, cx, cy, "Scientific\ncycle", fs=8.5, weight="bold")
    for i in range(6):
        a = math.radians(90 - i * 60)
        x, y = cx + R * 1.25 * math.cos(a), cy + R * math.sin(a)
        box(ax, x - 9.5, y - 4, 19, 8, stages[i], fill="white", fs=6.8)
        tx, ty = cx + (R * 1.25 + 21) * math.cos(a), cy + (R + 8) * math.sin(a)
        tx = min(max(tx, 8), 92)
        label(ax, tx, ty if i not in (0, 3) else (y + 7.5 if i == 0 else y - 7.5), tags[i], fs=5.8, italic=True, color=G1)
        ix, iy = cx + (r - 6.5) * 1.25 * math.cos(a), cy + (r - 6) * math.sin(a)
        label(ax, ix, iy, checks[i], fs=5.4)
        b = math.radians(90 - (i + 1) * 60)
        x2, y2 = cx + R * 1.25 * math.cos(b), cy + R * math.sin(b)
        mx0, my0 = x + (x2 - x) * 0.32, y + (y2 - y) * 0.32
        mx1, my1 = x + (x2 - x) * 0.68, y + (y2 - y) * 0.68
        arrow(ax, mx0, my0, mx1, my1, lw=0.8, rad=-0.15)
    label(ax, 50, 1.5, "outer labels: the AI job at each stage · inner ring: the matching check", fs=6.2, italic=True, color=G1)
    save(fig, "fig-06-01")


@fig("fig-06-03")
def f0603():
    fig, ax = canvas(3.0, ylim=(0, 66))
    ev = [
        ("Jun 2023", "AlphaDev", "faster sorting routines\nadded to LLVM library", "p"),
        ("Dec 2023", "FunSearch", "larger cap sets than\npreviously known", "p"),
        ("Jan 2024", "AlphaGeometry", "25 of 30 olympiad\ngeometry problems", "p"),
        ("Jul 2024", "AlphaProof + AG2", "IMO 28/42 (silver level);\nup to 3 days' computing", "c"),
        ("Jun 2025", "AlphaEvolve", "4×4 complex matrices with\n48 multiplications", "c"),
        ("Jul 2025", "Gemini Deep Think", "IMO 35/42 (gold level),\nnatural language", "c"),
        ("Nov 2025", "AlphaEvolve + Tao et al.", "67 problems;\nseveral improved", "c"),
        ("Jan 2026", "GPT-5.2 Pro + Aristotle", "Erdős problem #728\nproved in Lean", "l"),
    ]
    y0 = 34
    ax.plot([3, 97], [y0, y0], color=INK, lw=0.9)
    for i, (d, n, t, k) in enumerate(ev):
        x = 7 + i * 12.3
        up = i % 2 == 0
        ax.plot([x, x], [y0, y0 + (9 if up else -9)], color=G2, lw=0.6)
        if k == "p":
            ax.plot([x], [y0], "o", color=INK, ms=4.5)
        elif k == "c":
            ax.plot([x], [y0], "o", mfc="white", mec=INK, ms=4.5)
        else:
            ax.plot([x], [y0], "s", color=INK, ms=4.5)
        yt = y0 + 10 if up else y0 - 10
        va = "bottom" if up else "top"
        ax.text(x, yt, f"{d}\n", fontsize=6.3, ha="center", va=va, color=G1)
        ax.text(x, yt + (2.2 if up else -2.6), n, fontsize=6.6, ha="center", va=va, weight="bold")
        ax.text(x, yt + (6.3 if up else -6.5), t, fontsize=5.7, ha="center", va=va, linespacing=1.1)
    from matplotlib.lines import Line2D
    h = [Line2D([], [], ls="", marker="o", color=INK, ms=4, label="peer-reviewed paper"),
         Line2D([], [], ls="", marker="o", mfc="white", mec=INK, ms=4, label="company announcement / preprint"),
         Line2D([], [], ls="", marker="s", color=INK, ms=4, label="Lean-verified proof")]
    ax.legend(handles=h, loc="lower center", ncol=3, fontsize=6.3, bbox_to_anchor=(0.5, -0.02))
    save(fig, "fig-06-03")
