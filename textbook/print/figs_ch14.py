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
    v22 = [2060, 2164]  # Grace et al. (2025), as reported for the 2022 round
    v23 = [2047, 2116]  # Grace et al. (2025)
    v24 = [2042, 2098]  # Grace et al. (2026), 2024 round (fielded Dec 2024)
    y = np.array([1.0, 0.0])
    ax.axvline(2026, color=G2, lw=0.6, ls=(0, (3, 2)), zorder=1)
    ax.text(2026, 1.5, "today", ha="center", va="bottom", fontsize=7, style="italic")
    for yi, a, b_, c in zip(y, v22, v23, v24):
        ax.plot([c, a], [yi, yi], color=G2, lw=1.0, zorder=2)
        ax.plot([a], [yi], "o", ms=5.5, mfc="white", mec=INK, mew=0.9, zorder=3)
        ax.plot([b_], [yi], "o", ms=5.5, mfc=G2, mec=INK, mew=0.9, zorder=3)
        ax.plot([c], [yi], "o", ms=5.5, mfc=INK, mec=INK, mew=0.9, zorder=4)
        # 2022 and 2023 labelled above, 2024 below, so close points never collide
        ax.text(a, yi + 0.17, str(a), ha="center", va="bottom", fontsize=7.5)
        ax.text(b_, yi + 0.17, str(b_), ha="center", va="bottom", fontsize=7.5)
        ax.text(c, yi - 0.17, str(c), ha="center", va="top", fontsize=7.5)
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
         ax.plot([], [], "o", ms=5.5, mfc=G2, mec=INK, mew=0.9, ls="none")[0],
         ax.plot([], [], "o", ms=5.5, mfc=INK, mec=INK, mew=0.9, ls="none")[0]]
    ax.legend(h, ["2022 survey", "2023 survey", "2024 survey"], loc="upper center", bbox_to_anchor=(0.38, -0.36),
              ncol=3, fontsize=7.2, handletextpad=0.4, columnspacing=1.6)
    ax.text(0.38, -0.58, "Values as reported for each round; the 2024 report's recomputation moves earlier rounds by up to six years.",
            transform=ax.transAxes, ha="center", va="top", fontsize=6.0, color=G1)
    F.save(fig, "fig-14-01")


@fig("fig-14-02")
def f1402():
    fig = F.figure(2.8)
    ax = fig.add_axes([0.07, 0.13, 0.6, 0.83])
    t = np.linspace(0, 10, 300)
    yr = 2026 + t

    # fast acceleration: bends sharply upward from about 2028 and leaves the chart (schematic)
    fast = 1 + 0.45 * t + 0.35 * (np.exp(t / 1.9) - 1)
    U = fast + 0.15 * t + 0.03 * t ** 2
    L = 1 + 0.06 * t
    ax.fill_between(yr, L, U, color=G4, lw=0)
    ax.fill_between(yr, 1 + 0.3 * t, 1 + 0.62 * t, color=G3, lw=0, alpha=0.7)
    ax.plot(yr, fast, color=INK, lw=1.1, ls="-")
    ax.text(2031.4, 11.4, "Fast acceleration\n(e.g. AI 2027)", fontsize=7, va="center", ha="right", linespacing=1.1)
    paths = [
        (1 + 0.45 * t, (0, (5, 2)), "Trend continues"),
        (1 + 0.3 * t, (0, (1.2, 1.5)), "Normal technology:\nslow diffusion"),
        (1 + 1.3 * (1 - np.exp(-t / 2)), (0, (5, 1.5, 1.2, 1.5)), "Plateau: power\nor data limits"),
    ]
    for yv, ls, lab in paths:
        ax.plot(yr, yv, color=INK, lw=1.1, ls=ls)
        ax.text(2036.3, yv[-1], lab, fontsize=7, va="center", ha="left", linespacing=1.1, clip_on=False)
    ax.plot([2026], [1], "o", ms=3.5, color=INK, clip_on=False, zorder=5)
    ax.text(2026.2, 0.45, "today", fontsize=7, style="italic", va="center")
    ax.annotate("Narrow: present is\n(mostly) known", xy=(2026.6, 1.3), xytext=(2026.3, 7.0), fontsize=6.8,
                style="italic", color=G1, va="center", ha="left",
                arrowprops=dict(arrowstyle="-", color=G2, lw=0.6, shrinkA=6, shrinkB=1, relpos=(0.12, 0)))
    ax.annotate("Wide: many futures\nremain possible", xy=(2035.0, 9.0), xytext=(2032.7, 11.3), fontsize=6.8,
                style="italic", color=G1, va="center", ha="left",
                arrowprops=dict(arrowstyle="-", color=G2, lw=0.6, shrinkA=4, shrinkB=1, relpos=(0.6, 0)))
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
        label(ax, x0, 78, title, fs=8, ha="left", va="baseline", weight="bold")
        sig = x0 + 7
        win = 30  # default random delay window: up to 600 s = 10 minutes
        # tick strip of device starts
        ya = 57
        ax.plot([x0, x0 + W], [ya, ya], color=INK, lw=0.7)
        arrow(ax, x0 + W - 1, ya, x0 + W + 0.6, ya, lw=0.7, ms=5)
        label(ax, x0 + W / 2 + 4, ya - 3.6, "Time (minutes)", fs=6.6)
        ax.plot([sig, sig], [17, 71], color=G1, lw=0.7, ls=(0, (3, 2)))
        label(ax, sig + 1, 72, "Price signal", fs=6.6, ha="left", italic=True)
        # bracket marking the 10-minute random-delay window
        ax.plot([sig, sig, sig + win, sig + win], [ya - 1.2, ya - 2.0, ya - 2.0, ya - 1.2], color=G2, lw=0.5)
        label(ax, sig + 0.6, ya - 3.6, "10 min", fs=6, ha="left", color=G1)
        if k == 0:
            xs = sig + rng.uniform(0, win, 26)
            for xv in xs:
                ax.plot([xv, xv], [ya, ya + 4], color=G1, lw=0.6)
            ov = [sig + 3, sig + 14, sig + 25]
            for xv in ov:
                ax.plot([xv, xv], [ya, ya + 7], color=INK, lw=1.0)
                ax.plot([xv], [ya + 7.6], "o", ms=2.2, mfc="white", mec=INK, mew=0.7)
            label(ax, x0 + 30, 68.5, "owner override", fs=6.4, italic=True)
            ax.plot([x0 + 22.5, sig + 3.4], [68.5, ya + 8.4], color=G2, lw=0.5)
            ax.plot([x0 + 26.5, sig + 14.4], [66.8, ya + 8.4], color=G2, lw=0.5)
            ax.plot([x0 + 33.5, sig + 24.6], [66.8, ya + 8.4], color=G2, lw=0.5)
        else:
            xs = sig + rng.uniform(0.2, 1.6, 26)
            for xv in xs:
                ax.plot([xv, xv], [ya, ya + 4], color=INK, lw=0.6)
            for xv in sig + rng.uniform(4, win, 3):
                ax.plot([xv, xv], [ya, ya + 4], color=G1, lw=0.6)
            label(ax, sig + 3.5, 64.5, "agents cancel\ndelay together", fs=6.4, italic=True, ha="left")
        # load sketch: the same devices start in both panels, so the final load is the same;
        # what differs is how fast it arrives
        yb, y0, y1, yref = 19, 22, 46, 38
        ax.plot([x0, x0], [yb, 50], color=INK, lw=0.6)
        ax.plot([x0, x0 + W], [yb, yb], color=INK, lw=0.6)
        label(ax, x0 - 2, 34, "Load", fs=6.6, rot=90)
        if k == 0:
            xx = [x0, sig, sig + win, x0 + W]
            yy = [y0, y0, y1, y1]
            ax.plot(xx, yy, color=INK, lw=1.2)
            label(ax, sig + 12.5, 28.5, "Same total load arrives\ngradually over 10 min", fs=6.4, italic=True,
                  ha="left")
        else:
            xx = [x0, sig, sig + 1.2, sig + win, x0 + W]
            yy = [y0, y0, y1 - 2.5, y1, y1]
            ax.plot(xx, yy, color=INK, lw=1.2)
            label(ax, sig + 3, 48.6, "Load step", fs=6.6, italic=True, ha="left")
            # dimension arrow: size of the reference incident, measured from the starting load
            xr = sig + 18
            ax.plot([sig + 1.5, xr + 2], [y0, y0], color=G2, lw=0.5, ls=(0, (1.5, 1.5)))
            ax.plot([xr - 2, xr + 2], [yref, yref], color=INK, lw=0.7)
            ax.add_patch(F.FancyArrowPatch((xr, y0), (xr, yref), arrowstyle="<|-|>", mutation_scale=5,
                                           lw=0.6, color=INK, shrinkA=0, shrinkB=0))
            label(ax, xr + 1.5, (y0 + yref) / 2, "Reference incident:\n3,000 MW\n(continental Europe)", fs=6.4,
                  ha="left")
    box(ax, 12, 7.5, 76, 5, "Random delay up to 600 s by default; owner may cancel (UK SI 2021/1467, reg. 11)",
        fill=G4, fs=6.4, style="square,pad=0.6")
    label(ax, 50, 1.5, "Schematic, not to scale. Hypothetical mechanism, not a recorded event.", fs=6.4,
          italic=True, color=G1)
    save(fig, "fig-14-04")
