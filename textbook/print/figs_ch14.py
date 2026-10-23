"""Figures for chapter 14, drawn from figures/specs/ in the house style."""
import math

import numpy as np
from matplotlib.patches import Rectangle

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


@fig("fig-14-01")
def f1401():
    # dot plot: a bar from an arbitrary start year would give bar length no meaning
    fig = F.figure(2.3)
    ax = fig.add_axes([0.25, 0.36, 0.72, 0.52])
    groups = ["High-level machine\nintelligence (HLMI)", "Full automation\nof labour (FAOL)"]
    v22, n22 = [2060, 2164], [461, 202]
    v23, n23 = [2047, 2116], [1714, 774]
    y = np.array([1.0, 0.0])
    ax.axvline(2026, color=G2, lw=0.6, ls=(0, (3, 2)), zorder=1)
    ax.text(2026, 1.5, "today", ha="center", va="bottom", fontsize=7, style="italic")
    for yi, a, na, b_, nb in zip(y, v22, n22, v23, n23):
        ax.plot([b_, a], [yi, yi], color=G2, lw=1.0, zorder=2)
        ax.plot([a], [yi], "o", ms=5.5, mfc="white", mec=INK, mew=0.9, zorder=3)
        ax.plot([b_], [yi], "o", ms=5.5, mfc=INK, mec=INK, mew=0.9, zorder=3)
        # 2023 (earlier year) labelled to its left edge, 2022 to its right edge, so labels never collide
        ax.text(a - 2.5, yi + 0.17, str(a), ha="left", va="bottom", fontsize=7.5)
        ax.text(b_ + 2.5, yi + 0.17, str(b_), ha="right", va="bottom", fontsize=7.5)
        ax.text(a - 2.5, yi - 0.17, f"n = {na}", ha="left", va="top", fontsize=6.2, color=G1)
        ax.text(b_ + 2.5, yi - 0.17, f"n = {nb:,}", ha="right", va="top", fontsize=6.2, color=G1)
    ax.set_xlim(2020, 2180)
    ax.set_ylim(-0.55, 1.5)
    ax.set_xticks(range(2020, 2181, 20))
    ax.tick_params(axis="x", labelsize=7.5)
    ax.set_yticks(y)
    ax.set_yticklabels(groups, fontsize=7.8)
    ax.tick_params(axis="y", length=0, pad=5)
    ax.spines["left"].set_visible(False)
    ax.set_xlabel("Year at which aggregate forecast reaches 50% probability", fontsize=7.8)
    h = [ax.plot([], [], "o", ms=5.5, mfc="white", mec=INK, mew=0.9, ls="none")[0],
         ax.plot([], [], "o", ms=5.5, mfc=INK, mec=INK, mew=0.9, ls="none")[0]]
    ax.legend(h, ["2022 survey", "2023 survey"], loc="upper center", bbox_to_anchor=(0.38, -0.36), ncol=2,
              fontsize=7.2, handletextpad=0.4, columnspacing=1.6)
    ax.text(0.38, -0.58, "n = number of respondents answering that question", transform=ax.transAxes, ha="center",
            va="top", fontsize=6.2, color=G1)
    F.save(fig, "fig-14-01")


@fig("fig-14-02")
def f1402():
    fig = F.figure(2.8)
    ax = fig.add_axes([0.07, 0.13, 0.6, 0.83])
    t = np.linspace(0, 10, 300)
    yr = 2026 + t

    def sig(x):
        return 1 / (1 + np.exp(-x))
    # fast acceleration: bends sharply upward around 2027-2029, then keeps rising
    fast = 1 + 0.45 * t + 5.0 * (sig((t - 2.4) / 0.55) - sig(-2.4 / 0.55))
    U = fast + 0.13 * t + 0.012 * t ** 2
    L = 1 + 0.06 * t
    ax.fill_between(yr, L, U, color=G4, lw=0)
    ax.fill_between(yr, 1 + 0.3 * t, 1 + 0.62 * t, color=G3, lw=0, alpha=0.7)
    paths = [
        (fast, "-", "Fast acceleration\n(e.g. AI 2027)"),
        (1 + 0.45 * t, (0, (5, 2)), "Trend continues"),
        (1 + 0.3 * t, (0, (1.2, 1.5)), "Normal technology:\nslow diffusion"),
        (1 + 1.3 * (1 - np.exp(-t / 2)), (0, (5, 1.5, 1.2, 1.5)), "Plateau: power\nor data limits"),
    ]
    for yv, ls, lab in paths:
        ax.plot(yr, yv, color=INK, lw=1.1, ls=ls)
        ax.text(2036.3, yv[-1], lab, fontsize=7, va="center", ha="left", linespacing=1.1, clip_on=False)
    ax.plot([2026], [1], "o", ms=3.5, color=INK, clip_on=False, zorder=5)
    ax.text(2026.2, 0.45, "today", fontsize=7, style="italic", va="center")
    ax.annotate("Narrow: present is\n(mostly) known", xy=(2026.6, 1.25), xytext=(2026.3, 5.2), fontsize=6.8,
                style="italic", color=G1, va="center", ha="left",
                arrowprops=dict(arrowstyle="-", color=G2, lw=0.6))
    ax.annotate("Wide: many futures\nremain possible", xy=(2035.2, 9.6), xytext=(2030.6, 11.2), fontsize=6.8,
                style="italic", color=G1, va="center", ha="left",
                arrowprops=dict(arrowstyle="-", color=G2, lw=0.6))
    ax.set_xlim(2026, 2036)
    ax.set_ylim(0, 12.2)
    ax.set_xticks(range(2026, 2037, 2))
    ax.tick_params(axis="x", labelsize=7.5)
    ax.set_yticks([])
    ax.set_xlabel("Year", fontsize=8)
    ax.set_ylabel("AI capability and real-world impact (schematic)", fontsize=7.5)
    F.save(fig, "fig-14-02")


def _agent(ax, x, y, s=2.2):
    ax.add_patch(F.FancyBboxPatch((x - s, y - s * 0.8), 2 * s, 1.6 * s, boxstyle="round,pad=0,rounding_size=0.8",
                                  fc=G3, ec=INK, lw=0.6))
    ax.plot([x - s * 0.4, x + s * 0.4], [y + 0.2, y + 0.2], "o", ms=1.4, color=INK)
    ax.plot([x, x], [y + s * 0.8, y + s * 1.3], color=INK, lw=0.6)


@fig("fig-14-03")
def f1403():
    fig, ax = canvas(2.9, ylim=(0, 66))
    label(ax, 1, 62, "A. Conventional evaluation", fs=8, ha="left", va="baseline", weight="bold")
    label(ax, 52, 62, "B. Population-level evaluation", fs=8, ha="left", va="baseline", weight="bold")
    ax.plot([48.5, 48.5], [2, 64], color=G2, lw=0.5)
    # Panel A
    box(ax, 1, 25, 11, 10, "One model\ninstance", fill=G4, fs=6.8)
    tasks = ["Task 1", "Task 2", "Task 3", "…", "Task N"]
    ty = [50, 40, 30, 20, 10]
    for t, y in zip(tasks, ty):
        if t == "…":
            ax.plot([23.5] * 3, [y - 2, y, y + 2], "o", ms=1.3, color=INK)
            continue
        box(ax, 18.5, y - 3, 10, 6, t, fill="white", fs=6.6, style="square,pad=0.2")
        arrow(ax, 12.8, 30, 18.1, y, lw=0.6, ms=5)
        arrow(ax, 28.9, y, 34.2, 30, lw=0.6, ms=5)
    box(ax, 35, 25, 11.5, 10, "Average\naccuracy", fill=G4, fs=6.8)
    # Panel B
    copies = ["Copy 1 (user A)", "Copy 2 (user B)", "…", "Copy N (user Z)"]
    cy = [52, 41, 30.5, 20]
    tgt = [45, 41, None, 37]
    for c, y, ty_ in zip(copies, cy, tgt):
        if c == "…":
            ax.plot([57.5] * 3, [y - 2, y, y + 2], "o", ms=1.3, color=INK)
            continue
        _agent(ax, 57.5, y)
        label(ax, 57.5, y - 5, c, fs=6.2)
        arrow(ax, 60.2, y, 70.6, ty_, lw=0.6, ms=5)
    box(ax, 71, 35, 26, 12, "", fill=G4)
    label(ax, 84, 43, "One stress scenario", fs=7.2)
    label(ax, 84, 38.5, "e.g. sudden price change", fs=6.3, italic=True, color=G1)
    arrow(ax, 84, 34.4, 84, 30.2, lw=0.7, ms=6)
    # bar-chart icon
    base = 19.5
    for i, (hgt, lab) in enumerate(((10, "X"), (3, "Y"), (2, "Z"))):
        bx = 73 + i * 9
        ax.add_patch(Rectangle((bx, base), 4.5, hgt, fc=G1 if i == 0 else G3, ec=INK, lw=0.5))
        label(ax, bx + 2.25, base - 2.6, "Action " + lab, fs=6)
    ax.plot([71.5, 97.5], [base, base], color=INK, lw=0.6)
    arrow(ax, 84, 15.2, 84, 11.0, lw=0.7, ms=6)
    box(ax, 66.5, 1.5, 32, 9, "Action concentration =\nshare choosing the most common action", fill="white", fs=6.4)
    save(fig, "fig-14-03")


@fig("fig-14-04")
def f1404():
    fig, ax = canvas(3.4, ylim=(0, 82))
    rng = np.random.default_rng(3)
    for k, (x0, title) in enumerate(((2, "A. Human overrides (today)"), (53, "B. Agent overrides (hypothetical)"))):
        W = 44
        label(ax, x0, 79, title, fs=8, ha="left", weight="bold")
        sig = x0 + 7
        # tick strip
        ya = 57
        ax.plot([x0, x0 + W], [ya, ya], color=INK, lw=0.7)
        arrow(ax, x0 + W - 1, ya, x0 + W + 0.6, ya, lw=0.7, ms=5)
        label(ax, x0 + W / 2, ya - 3.6, "Time (minutes)", fs=6.6)
        ax.plot([sig, sig], [17, 71], color=G1, lw=0.7, ls=(0, (3, 2)))
        label(ax, sig + 1, 72, "Price signal", fs=6.6, ha="left", italic=True)
        if k == 0:
            xs = sig + rng.uniform(0, 30, 26)
            for xv in xs:
                ax.plot([xv, xv], [ya, ya + 4], color=G1, lw=0.6)
            ov = [sig + 3, sig + 18.5, x0 + 41]
            for xv in ov:
                ax.plot([xv, xv], [ya, ya + 7], color=INK, lw=1.0)
                ax.plot([xv], [ya + 7.6], "o", ms=2.2, mfc="white", mec=INK, mew=0.7)
            label(ax, x0 + 30, 68.5, "owner override", fs=6.4, italic=True)
            ax.plot([x0 + 30, sig + 19], [66.6, ya + 8.4], color=G2, lw=0.5)
            ax.plot([x0 + 35.5, x0 + 40.3], [66.6, ya + 8.4], color=G2, lw=0.5)
        else:
            xs = sig + rng.uniform(0.2, 1.6, 26)
            for xv in xs:
                ax.plot([xv, xv], [ya, ya + 4], color=INK, lw=0.6)
            for xv in sig + rng.uniform(4, 30, 3):
                ax.plot([xv, xv], [ya, ya + 4], color=G1, lw=0.6)
            label(ax, sig + 3.5, 64.5, "agents cancel\ndelay together", fs=6.4, italic=True, ha="left")
        # load sketch
        yb, yr = 19, 38
        ax.plot([x0, x0], [yb, 50], color=INK, lw=0.6)
        ax.plot([x0, x0 + W], [yb, yb], color=INK, lw=0.6)
        label(ax, x0 - 2, 34, "Load", fs=6.6, rot=90)
        ax.plot([x0, x0 + W], [yr, yr], color=INK, lw=0.7, ls=(0, (6, 2, 1.5, 2)))
        if k == 0:
            xx = np.linspace(x0, x0 + W, 100)
            yy = yb + 2 + np.clip((xx - sig) / 30, 0, 1) * 11
            ax.plot(xx, yy, color=INK, lw=1.2)
            label(ax, x0 + W - 0.5, yr + 3.6, "Reference incident: 3,000 MW\n(continental Europe)", fs=6.4, ha="right")
            label(ax, sig + 17, 22.6, "Load rises gradually", fs=6.6, italic=True, ha="left")
        else:
            xx = [x0, sig, sig + 1.2, x0 + W]
            yy = [yb + 2, yb + 2, 46, 46]
            ax.plot(xx, yy, color=INK, lw=1.2)
            label(ax, sig + 3, yr - 3.8, "Reference incident: 3,000 MW\n(continental Europe)", fs=6.4, ha="left")
            label(ax, sig + 3, 48.6, "Load step", fs=6.6, italic=True, ha="left")
    box(ax, 12, 7.5, 76, 5, "Random delay up to 600 s by default; owner may cancel (UK SI 2021/1467, reg. 11)",
        fill=G4, fs=6.4, style="square,pad=0.6")
    label(ax, 50, 1.5, "Schematic, not to scale. Hypothetical mechanism, not a recorded event.", fs=6.4,
          italic=True, color=G1)
    save(fig, "fig-14-04")
