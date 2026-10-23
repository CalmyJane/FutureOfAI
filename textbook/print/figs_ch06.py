"""Figures for chapter 6, drawn from figures/specs/ in the house style."""
import math

import numpy as np
from matplotlib.patches import Ellipse, Rectangle

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
    # AlphaFold 2 pipeline after Jumper et al. 2021, Fig. 1e and Suppl. Algorithm 2 (spec fig-06-02)
    fig, ax = canvas(2.97, ylim=(0, 66))
    thin = dict(lw=0.5, color=G1, ms=6)

    def line(xs, ys, lw=0.5, color=G1):
        ax.plot(xs, ys, color=color, lw=lw, solid_capstyle="butt")

    def dot(x, y):
        ax.plot([x], [y], "o", color=INK, ms=2.2)

    # column 1: inputs
    box(ax, 0.5, 57, 30.5, 8, fill="white")
    label(ax, 15.75, 62.7, "Input sequence", fs=6.8)
    ax.text(15.75, 59.3, "MKTAYIAK\u2026", ha="center", va="center", fontsize=6.3, family="DejaVu Sans Mono",
            color=G1)
    box(ax, 3.5, 40, 11.5, 9, "Sequence\ndatabases", fs=6.2)
    box(ax, 18, 40, 13, 9, "MSA (related\nsequences)", fill="white", fs=6.2)
    box(ax, 3.5, 21, 11.5, 10, "Structure\ndatabase\n(PDB)", fs=6.2)
    box(ax, 18, 22, 13, 8, "Templates", fill="white", fs=6.2)
    arrow(ax, 9.25, 57, 9.25, 49.4, lw=0.7)
    arrow(ax, 15.4, 44.5, 17.6, 44.5, lw=0.7, ms=6)
    arrow(ax, 15.4, 26, 17.6, 26, lw=0.7, ms=6)
    # sequence down the left margin: to the structure database and on to the pair representation
    line([1.6, 1.6], [56.6, 17])
    arrow(ax, 1.6, 26, 3.3, 26, lw=0.7, ms=6)
    dot(1.6, 26)
    line([1.6, 34], [17, 17])
    line([34, 34], [17, 22])
    arrow(ax, 34, 22, 37.6, 22, **thin)
    # sequence along the top to the MSA representation
    line([31.4, 42], [61, 61])
    arrow(ax, 42, 61, 42, 53.6, **thin)

    # column 2: the two representations
    label(ax, 42, 52.3, "MSA representation", fs=6.3)
    cw = 1.5
    for r in range(5):
        for c in range(8):
            ax.add_patch(Rectangle((36 + c * cw, 42 + r * cw), cw, cw, fc=G3 if r == 4 else G4, ec=G1, lw=0.35))
    label(ax, 42, 39.6, "rows = sequences,", fs=5.8, italic=True, color=G1)
    label(ax, 42, 37.5, "columns = residues", fs=5.8, italic=True, color=G1)
    label(ax, 42, 31.6, "Pair representation", fs=6.3)
    pw = 1.45
    for r in range(6):
        for c in range(6):
            ax.add_patch(Rectangle((37.65 + c * pw, 20.5 + r * pw), pw, pw, fc=G4, ec=G1, lw=0.35))
    label(ax, 42, 18.6, "residue \u00d7 residue", fs=5.8, italic=True, color=G1)
    arrow(ax, 31.4, 46, 35.8, 46, lw=0.7, ms=6)
    arrow(ax, 31.4, 26, 37.5, 26, lw=0.7, ms=6)
    arrow(ax, 31.4, 30.4, 36.2, 42.6, **thin)   # template torsion angles become extra MSA rows

    # column 3: Evoformer
    box(ax, 52.5, 13, 26.5, 44, fill=G4)
    label(ax, 65.75, 54.2, "Evoformer", fs=7.2)
    label(ax, 65.75, 51.2, "(48 blocks)", fs=6.3)
    box(ax, 55, 41, 11, 7.5, "MSA", fill="white", fs=6.5)
    box(ax, 55, 21, 11, 7.5, "Pair", fill="white", fs=6.5)
    arrow(ax, 58.3, 40.6, 58.3, 29.0, lw=0.7, ms=6)
    arrow(ax, 62.7, 29.0, 62.7, 40.6, lw=0.7, ms=6)
    arrow(ax, 48.4, 45.5, 54.6, 45.5, lw=0.7, ms=6)
    arrow(ax, 46.6, 25, 54.6, 25, lw=0.7, ms=6)
    # triangle inset beside the pair lane
    I, J, K = (69, 21.5), (76, 21.5), (72.5, 27.5)
    line([I[0], K[0]], [I[1], K[1]], lw=0.7, color=G2)
    line([J[0], K[0]], [J[1], K[1]], lw=0.7, color=G2)
    line([I[0], J[0]], [I[1], J[1]], lw=1.5, color=INK)
    for (x, y), t, dx, dy in ((I, "i", -1.3, 0), (J, "j", 1.3, 0), (K, "k", 0, 1.6)):
        ax.plot([x], [y], "o", mfc="white", mec=INK, ms=3.2, mew=0.6)
        label(ax, x + dx, y + dy, t, fs=6, italic=True)
    label(ax, 72.5, 18.0, "triangle update:", fs=5.8, italic=True, color=G1)
    label(ax, 72.5, 15.8, "ik + jk \u2192 ij", fs=5.8, italic=True, color=G1)

    # column 4: structure module and output
    box(ax, 83, 23, 15, 14, "Structure\nmodule", fill="white", fs=6.8)
    label(ax, 90.5, 20.3, "residues as rigid", fs=5.8, italic=True, color=G1)
    label(ax, 90.5, 18.2, "bodies; invariant", fs=5.8, italic=True, color=G1)
    label(ax, 90.5, 16.1, "point attention", fs=5.8, italic=True, color=G1)
    arrow(ax, 79.4, 30, 82.6, 30, lw=0.7, ms=6)
    box(ax, 82, 43, 16, 21, fill="white")
    label(ax, 90, 61.4, "3D structure", fs=6.6)
    label(ax, 90, 58.8, "+ pLDDT", fs=6.6)
    t = np.linspace(0, 1, 120)
    xs = 84 + 12 * t
    ys = 53.2 + 2.2 * np.sin(t * 3.2 * math.pi)
    ax.plot(xs[:75], ys[:75], color=INK, lw=1.8, solid_capstyle="round")
    ax.plot(xs[74:], ys[74:], color=G3, lw=1.8, solid_capstyle="round")
    ax.plot([83.6, 85.8], [48.2, 48.2], color=INK, lw=1.8)
    label(ax, 86.6, 48.2, "high confidence", fs=5.8, ha="left", color=G1)
    ax.plot([83.6, 85.8], [45.8, 45.8], color=G3, lw=1.8)
    label(ax, 86.6, 45.8, "low confidence", fs=5.8, ha="left", color=G1)
    arrow(ax, 90.5, 37.4, 90.5, 42.6, lw=0.7, ms=6)

    # recycling: Evoformer and structure-module outputs back to the representations
    line([98.4, 99.6, 99.6, 42], [30, 30, 5, 5], lw=0.8, color=INK)
    line([81, 81], [30, 5], lw=0.8, color=INK)
    dot(81, 30)
    dot(81, 5)
    arrow(ax, 42, 5, 42, 16.6, lw=0.8)
    label(ax, 61.5, 7.2, "Recycling (4 passes in all)", fs=6.5, italic=True)
    save(fig, "fig-06-02")


@fig("fig-06-03")
def f0603():
    # timeline (spec fig-06-03)
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
    save(fig, "fig-06-03")
