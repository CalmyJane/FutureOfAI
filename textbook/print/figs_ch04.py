"""Figures for chapter 4, drawn from figures/specs/ in the house style."""
import math
from datetime import date

import numpy as np
from matplotlib.lines import Line2D
from matplotlib.ticker import FixedLocator, NullFormatter, NullLocator

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


def year(d):
    """ISO date string -> decimal year."""
    y, m, dd = (int(v) for v in d.split("-"))
    start = date(y, 1, 1).toordinal()
    return y + (date(y, m, dd).toordinal() - start) / (date(y + 1, 1, 1).toordinal() - start)


@fig("fig-04-01")
def f0401():
    # Schematic only: loss = a * C^-b + c, no real data, no numbers on the axes.
    fig = F.figure(2.5)
    ax = fig.add_axes([0.07, 0.11, 0.9, 0.86])
    a, b, c = 5.0, 0.25, 0.15
    L = lambda C: a * C ** -b + c
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(10 ** -0.3, 10 ** 10.6)
    ax.set_ylim(0.11, 7)
    for axis in (ax.xaxis, ax.yaxis):
        axis.set_major_locator(NullLocator())
        axis.set_minor_locator(NullLocator())
        axis.set_major_formatter(NullFormatter())
        axis.set_minor_formatter(NullFormatter())
    # fitted segment through the small runs, then the extrapolation
    cf = np.logspace(0, 3.4, 100)
    ax.plot(cf, L(cf), color=INK, lw=1.3)
    ce = np.logspace(3.4, 10.6, 200)
    ax.plot(ce, L(ce), color=INK, lw=1.2, ls=(0, (1.2, 2.2)))
    # small runs (filled), slightly scattered around the trend
    xs = np.logspace(0.2, 3.2, 7)
    jit = [1.04, 0.97, 1.03, 0.98, 1.02, 0.97, 1.02]
    ax.plot(xs, L(xs) * np.array(jit), "o", color=INK, ms=3.8, zorder=3)
    # planned large run (hollow)
    xp = 10 ** 8.3
    ax.plot([xp], [L(xp)], "o", mfc="white", mec=INK, mew=1.0, ms=5.5, zorder=3)
    # irreducible loss
    ax.axhline(c, color=G2, lw=0.8, ls="--")
    ax.text(10 ** 0.0, c * 1.07, "Irreducible loss", fontsize=7.5, va="bottom", color=G1)
    ax.text(10 ** 0.2, 1.55, "Small training runs", fontsize=7.5, ha="left", va="top")
    ax.text(10 ** 2.15, 2.25, "Fitted trend", fontsize=7.5, ha="left", va="bottom", style="italic")
    # above the dotted line: the curve falls away to the right, so the label never crosses it
    ax.text(10 ** 5.3, L(10 ** 5.3) * 1.15, "Extrapolation", fontsize=7.5, ha="left", va="bottom", style="italic")
    ax.annotate("Planned large run\n(prediction)", xy=(xp, L(xp)), xytext=(10 ** 9.0, 0.36), fontsize=7.5,
                ha="center", va="bottom", arrowprops=dict(arrowstyle="-", color=G2, lw=0.6, shrinkB=4))
    ax.set_xlabel("Training compute (log scale)", labelpad=4)
    ax.set_ylabel("Test loss (log scale)", labelpad=4)
    F.save(fig, "fig-04-01")


# Epoch AI, Notable AI Models (epochai2026data): label, date, FLOP, confident?
EPOCH = [
    ("Perceptron Mark I", "1957-01-01", 694894.94, False),
    ("NETtalk", "1987-06-06", 28328002560, True),
    ("LeNet-5", "1998-11-01", 2810937600000, True),
    ("AlexNet", "2012-09-30", 4.7e17, True),
    ("Transformer", "2017-06-12", 7.4245248e18, True),
    ("BERT-Large", "2018-10-11", 2.85e20, True),
    ("GPT-3", "2020-05-28", 3.14e23, True),
    ("Chinchilla", "2022-03-29", 5.76e23, True),
    ("GPT-4", "2023-03-15", 2.1e25, False),
    ("Llama 3.1 405B", "2024-07-23", 3.8e25, True),
    ("Grok 3", "2025-02-17", 3.5e26, False),
    ("GPT-4.5", "2025-02-27", 3.8e26, False),
]


@fig("fig-04-02")
def f0402():
    fig = F.figure(3.0)
    ax = fig.add_axes([0.12, 0.12, 0.86, 0.85])
    ax.set_yscale("log")
    ax.set_xlim(1955, 2026)
    ax.set_ylim(1e5, 1e27 * 1.6)
    ax.set_xticks(range(1960, 2021, 10))
    ax.yaxis.set_major_locator(FixedLocator([10.0 ** k for k in range(6, 28, 3)]))
    ax.yaxis.set_minor_locator(FixedLocator([10.0 ** k for k in range(5, 28)]))
    ax.yaxis.set_minor_formatter(NullFormatter())
    ax.set_yticklabels([f"$10^{{{k}}}$" for k in range(6, 28, 3)])
    ax.tick_params(axis="y", which="minor", length=0)
    ax.grid(True, which="minor", axis="y", color=G4, lw=0.6)
    ax.grid(True, which="major", axis="y", color=G3, lw=0.6)
    ax.set_axisbelow(True)
    # label offsets in points (dx, dy, ha)
    off = {
        "Perceptron Mark I": (5, 0, "left"),
        "NETtalk": (-5, 0, "right"),
        "LeNet-5": (-5, 0, "right"),
        "AlexNet": (-5, 0, "right"),
        "Transformer": (-5, 0, "right"),
        "BERT-Large": (-5, 0, "right"),
        "GPT-3": (-5, 0, "right"),
        "Chinchilla": (-3, -8, "center"),
        "GPT-4": (-5, 0, "right"),
    }
    for lab, d, v, conf in EPOCH:
        x = year(d)
        if conf:
            ax.plot([x], [v], "o", color=INK, ms=4, zorder=3)
        else:
            ax.plot([x], [v], "o", mfc="white", mec=INK, mew=0.9, ms=4, zorder=3)
        if lab in off:
            dx, dy, ha = off[lab]
            ax.annotate(lab, (x, v), xytext=(dx, dy), textcoords="offset points", fontsize=7,
                        ha=ha, va="center")
    # Grok 3 and GPT-4.5 are ten days and 0.04 orders of magnitude apart, so their markers
    # coincide at this scale: one shared label. Llama 3.1 405B sits just above-right of GPT-4,
    # so its label goes below the cluster with a leader line.
    g3 = dict((e[0], e) for e in EPOCH)
    xg = (year(g3["Grok 3"][1]) + year(g3["GPT-4.5"][1])) / 2
    ax.annotate("Grok 3, GPT-4.5", (xg, 3.65e26), xytext=(-5, 0), textcoords="offset points",
                fontsize=7, ha="right", va="center")
    xl, vl = year(g3["Llama 3.1 405B"][1]), g3["Llama 3.1 405B"][2]
    ax.annotate("Llama 3.1 405B", (xl, vl), xytext=(2025.6, 10 ** 24.45), textcoords="data",
                fontsize=7, ha="right", va="center",
                arrowprops=dict(arrowstyle="-", color=G2, lw=0.5, shrinkA=1, shrinkB=2.5))
    h = [Line2D([], [], ls="", marker="o", color=INK, ms=4, label="estimate within ×3"),
         Line2D([], [], ls="", marker="o", mfc="white", mec=INK, ms=4, label="estimate within ×10")]
    ax.legend(handles=h, loc="upper left", fontsize=7, handletextpad=0.3, borderaxespad=0.2)
    ax.set_xlabel("Publication date")
    ax.set_ylabel("Training compute (FLOP, log scale)")
    F.save(fig, "fig-04-02")


# METR-Horizon-v1.1, is_sota rows (metr2026task): label, date, p50, ci_low, ci_high (minutes)
METR = [
    ("GPT-2", "2019-02-14", 0.053778, 0.009994, 0.141825),
    ("GPT-3 (davinci-002)", "2020-05-28", 0.144057, 0.093319, 0.221209),
    ("GPT-3.5", "2022-03-15", 0.599247, 0.255148, 1.115905),
    ("GPT-4", "2023-03-14", 3.987428, 1.93292, 7.995283),
    ("GPT-4 (Nov 2023)", "2023-11-06", 4.044959, 1.866859, 8.443226),
    ("GPT-4o", "2024-05-13", 6.991195, 4.001482, 12.905741),
    ("Claude 3.5 Sonnet (Jun)", "2024-06-20", 11.395377, 5.489734, 22.384214),
    ("o1-preview", "2024-09-12", 20.326586, 11.716193, 33.379877),
    ("Claude 3.5 Sonnet (Oct)", "2024-10-22", 20.522872, 10.144026, 40.82028),
    ("o1", "2024-12-05", 38.831588, 21.164512, 64.95249),
    ("Claude 3.7 Sonnet", "2025-02-24", 60.388937, 33.006168, 104.226017),
    ("o3", "2025-04-16", 119.732634, 74.615398, 190.943818),
    ("GPT-5", "2025-08-07", 203.012577, 112.641357, 405.551565),
    ("Gemini 3 Pro", "2025-11-18", 224.325884, 139.565157, 379.235434),
    ("Claude Opus 4.5", "2025-11-24", 292.994594, 161.717714, 623.704698),
    ("GPT-5.2", "2025-12-11", 352.249302, 198.067494, 815.177445),
    ("Claude Opus 4.6", "2026-02-05", 718.80683, 316.685725, 3633.786163),
    ("Claude Mythos Preview (early)", "2026-04-07", 1044.780145, 508.876789, 3304.261235),
]


@fig("fig-04-03")
def f0403():
    fig = F.figure(3.0)
    ax = fig.add_axes([0.13, 0.12, 0.85, 0.85])
    ax.set_yscale("log")
    ax.set_xlim(2018.7, 2026.6)
    ax.set_ylim(0.005, 14000)
    ax.set_xticks(range(2019, 2027))
    ticks = [(1 / 60, "1 sec"), (10 / 60, "10 sec"), (1, "1 min"), (10, "10 min"), (60, "1 hour"),
             (240, "4 hours"), (960, "16 hours"), (2880, "2 days")]
    ax.yaxis.set_major_locator(FixedLocator([t for t, _ in ticks]))
    ax.yaxis.set_minor_locator(NullLocator())
    ax.set_yticklabels([s for _, s in ticks])
    ax.grid(True, which="major", axis="y", color=G4, lw=0.6)
    ax.set_axisbelow(True)
    ax.axhline(960, color=G2, lw=0.8, ls="--")
    ax.text(2018.85, 960 * 1.12, "16 h: METR reliability limit", fontsize=7, va="bottom", color=G1)
    off = {
        "GPT-2": (5, 0, "left"),
        "GPT-4": (-5, 4, "right"),
        "Claude 3.7 Sonnet": (-6, 9, "right"),
        "o3": (5, -5, "left"),
        "GPT-5": (-5, 8, "right"),
        "Claude Opus 4.6": (-14, 12, "right"),
        "Claude Mythos Preview (early)": (8, 27, "right"),
    }
    for lab, d, p, lo, hi in METR:
        x = year(d)
        hollow = p > 960
        ax.plot([x, x], [lo, hi], color=G1, lw=0.7, zorder=2)
        ax.plot([x], [p], "o", ms=3.6, zorder=3, mew=0.9,
                mfc="white" if hollow else INK, mec=INK)
        if lab in off:
            dx, dy, ha = off[lab]
            lead = dict(arrowprops=dict(arrowstyle="-", color=G2, lw=0.5, shrinkA=1, shrinkB=3)) \
                if lab == "Claude Opus 4.6" else {}
            ax.annotate(lab, (x, p), xytext=(dx, dy), textcoords="offset points", fontsize=7,
                        ha=ha, va="center", **lead)
    ax.set_xlabel("Model release date")
    ax.set_ylabel("50% time horizon (log scale)")
    F.save(fig, "fig-04-03")
