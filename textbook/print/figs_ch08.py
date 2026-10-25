"""Figures for chapter 8, drawn from figures/specs/ in the house style."""
import math

import numpy as np

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


@fig("fig-08-01")
def f0801():
    fig, ax = canvas(2.25, ylim=(0, 50))
    steps = [
        ("Exposure", "What AI could do", "Exposure indices"),
        ("Adoption", "Is it used?", "Surveys, usage logs"),
        ("Task\nproductivity", "Time, quality,\noutput", "Experiments (RCTs)"),
        ("Firm\nresponse", "Hire, reassign,\nexpand", "Firm data"),
        ("Economy-wide\noutcomes", "Jobs, wages,\nGDP", "Payroll, national\naccounts"),
    ]
    bw, gap, x0 = 16.6, 3.2, 1.4
    by, bh = 24, 15
    for i, (t, sub, ex) in enumerate(steps):
        x = x0 + i * (bw + gap)
        box(ax, x, by, bw, bh, fill=G4 if i < 3 else "white", lw=0.8, style="round,pad=0,rounding_size=1.2")
        label(ax, x + bw / 2, by + bh - 4.4, t, fs=7.5, weight="bold", va="center")
        label(ax, x + bw / 2, by + 3.6, sub, fs=6.3, color=G1, va="center")
        label(ax, x + bw / 2, by - 3.6, ex, fs=6.3, italic=True, va="top")
        if i < 4:
            arrow(ax, x + bw + 0.1, by + bh / 2, x + bw + gap - 0.1, by + bh / 2, lw=0.9, ms=7)
    # dashed bracket over boxes 4 and 5
    xl = x0 + 3 * (bw + gap)
    xr = x0 + 4 * (bw + gap) + bw
    yt = by + bh + 2.2
    ax.plot([xl, xl, xr, xr], [yt - 1.2, yt, yt, yt - 1.2], color=INK, lw=0.7, ls=(0, (3, 2)))
    label(ax, (xl + xr) / 2, yt + 3.2, "Substitute or complement?", fs=7.2, italic=True)
    # narrowing wedge: amount of causal evidence
    wx0, wx1 = x0, x0 + 4 * (bw + gap) + bw
    wy = 6.5
    ax.fill([wx0, wx1, wx1, wx0], [wy + 3.6, wy + 0.25, wy - 0.25, wy - 3.6], color=G3, ec=G1, lw=0.5)
    label(ax, wx0 + 1.5, wy, "Evidence on AI's own effects", fs=6.8, ha="left", va="center")
    label(ax, wx1, wy - 3.9, "less →", fs=6.3, ha="right", va="top", italic=True, color=G1)
    label(ax, wx0, wy - 3.9, "more", fs=6.3, ha="left", va="top", italic=True, color=G1)
    save(fig, "fig-08-01")


@fig("fig-08-02")
def f0802():
    H = 3.9
    fig = F.figure(H)
    L, W = 0.42, 0.555
    # Panel A
    A = [
        ("Noy & Zhang", "RCT; n=453; 2023", -40, None, True),
        ("Peng et al.", "RCT; n=95; 2022", -55.8, (-89, -21), True),
        ("Dell'Acqua et al., inside frontier", "RCT; n=758; 2023", -25.1, None, True),
        ("METR early 2025", "RCT; n=16; 2025", 19, (2, 39), True),
        ("METR late 2025, returning devs", "RCT; n=10; from Aug 2025", -18, (-38, 9), True),
        ("METR late 2025, new devs", "RCT; n=47; from Aug 2025", -4, (-15, 9), True),
    ]
    B = [
        ("Brynjolfsson et al.", "quasi-exp.; n=5,172; 2020–21", 15, None, False),
        ("Dell'Acqua et al., inside frontier", "RCT; n=758; 2023", 12.2, None, True),
        ("Cui et al.", "3 field RCTs; n=4,867; 2022–23", 26.08, (5.9, 46.3), True),
    ]
    # layout in inches, converted to figure fractions
    rowh = 0.245
    yb = 0.80                                   # bottom of panel B axes
    btop = yb + rowh * len(B)
    btitle = btop + 0.12                        # top of the "B" panel title
    abot = btitle + 0.52                        # room for panel A ticks and axis label
    axA = fig.add_axes([L, abot / H, W, rowh * len(A) / H])
    axB = fig.add_axes([L, yb / H, W, rowh * len(B) / H])

    def panel(ax, rows, xlim, ticks, xlabel):
        n = len(rows)
        for i, (name, meta, est, ci, rct) in enumerate(rows):
            y = n - 1 - i
            if ci:
                ax.plot(ci, [y, y], color=INK, lw=0.9, solid_capstyle="butt")
                for c in ci:
                    ax.plot([c, c], [y - 0.13, y + 0.13], color=INK, lw=0.9)
            ax.plot([est], [y], marker="o", ms=4.6, mfc=INK if rct else "white", mec=INK, mew=0.9, zorder=3)
            ax.text(xlim[0] - (xlim[1] - xlim[0]) * 0.03, y + 0.21, name, ha="right", va="center", fontsize=7.2)
            ax.text(xlim[0] - (xlim[1] - xlim[0]) * 0.03, y - 0.25, f"({meta})", ha="right", va="center",
                    fontsize=6.1, color=G1)
        ax.axvline(0, color=G2, lw=0.7)
        ax.set_xlim(*xlim)
        ax.set_ylim(-0.6, n - 0.4)
        ax.set_yticks([])
        ax.spines["left"].set_visible(False)
        ax.set_xticks(ticks)
        ax.set_xticklabels([("+" if t > 0 else "−" if t < 0 else "") + str(abs(t)) for t in ticks], fontsize=7)
        ax.xaxis.grid(True, color=G4, lw=0.6)
        ax.set_axisbelow(True)
        ax.set_xlabel(xlabel, fontsize=7.6, labelpad=2)
        return ax

    panel(axA, A, (-100, 50), [-100, -75, -50, -25, 0, 25, 50], "Change in time to complete task (%)")
    tr = axA.get_xaxis_transform()
    axA.text(-100, -0.33 / (rowh * len(A)), "← faster", ha="left", va="center", fontsize=6.3, style="italic", color=G1, transform=tr)
    axA.text(50, -0.33 / (rowh * len(A)), "slower →", ha="right", va="center", fontsize=6.3, style="italic", color=G1, transform=tr)
    panel(axB, B, (-10, 50), [-10, 0, 10, 20, 30, 40, 50], "Change in output (%)")
    fig.text(0.01, 1 - 0.054 / H, "A  Time per task", fontsize=8.2, weight="bold", va="top")
    fig.text(0.01, btitle / H, "B  Output", fontsize=8.2, weight="bold", va="top")
    from matplotlib.lines import Line2D
    fig.legend(handles=[Line2D([], [], ls="", marker="o", ms=4.6, mfc=INK, mec=INK, label="randomised"),
                        Line2D([], [], ls="", marker="o", ms=4.6, mfc="white", mec=INK, label="quasi-experimental")],
               loc="upper right", bbox_to_anchor=(0.995, 1.005), ncol=2, fontsize=7, handletextpad=0.2,
               columnspacing=1.0)
    fig.text(0.01, 0.005, "Cui et al. interval (approx.) computed from the reported standard error.\n"
             "Years are approximate data-collection periods.", fontsize=6.2, color=G1, style="italic",
             va="bottom", linespacing=1.2)
    F.save(fig, "fig-08-02")
