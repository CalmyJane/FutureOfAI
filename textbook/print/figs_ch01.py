"""Figures for chapter 1, drawn from figures/specs/ in the house style."""
import math

import numpy as np
from matplotlib.patches import Ellipse, Rectangle

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


@fig("fig-01-01")
def f0101():
    fig, ax = canvas(3.2, ylim=(0, 72))
    sq = "round,pad=0,rounding_size=3"
    # nested regions, outermost first (alternating fills distinguish the levels)
    box(ax, 1, 1, 98, 70, fill="white", lw=0.9, style=sq)
    label(ax, 3.5, 67.2, "Artificial intelligence", fs=8.5, ha="left", weight="bold")
    box(ax, 29, 4, 68, 59, fill=G4, lw=0.8, style=sq)
    label(ax, 31.5, 59.5, "Machine learning", fs=8.2, ha="left", weight="bold")
    box(ax, 44, 7, 51, 48, fill="white", lw=0.8, style=sq)
    label(ax, 46.5, 51.5, "Deep learning", fs=8, ha="left", weight="bold")
    label(ax, 92.5, 51.5, "AlexNet (2012)", fs=6.5, ha="right", italic=True, color=G1)
    box(ax, 54, 18, 39, 29, fill=G4, lw=0.8, style=sq)
    label(ax, 56.5, 43.7, "Foundation models", fs=7.6, ha="left", weight="bold")
    # generative AI: dotted, overlaps the foundation-model region and extends beyond it
    ax.add_patch(Ellipse((75, 25), 42, 24, fill=False, ec=INK, lw=0.8, ls=(0, (1, 1.6))))
    label(ax, 75, 15.3, "Generative AI", fs=6.8, italic=True)
    box(ax, 57.5, 22.5, 15, 11, "", fill="white", lw=0.7, style="round,pad=0,rounding_size=1.5")
    label(ax, 65, 29.6, "LLMs", fs=7.5, weight="bold")
    label(ax, 65, 25.6, "GPT-3 (2020)", fs=6, italic=True, color=G1)
    box(ax, 75.5, 22.5, 15, 11, "Image/audio\ngenerators", fill="white", lw=0.7, fs=6.6,
        style="round,pad=0,rounding_size=1.5")
    # symbolic AI, inside AI but outside machine learning
    box(ax, 4, 24, 21, 20, "", fill=G4, lw=0.7, style="round,pad=0,rounding_size=2")
    label(ax, 14.5, 38.5, "Symbolic AI", fs=7.8, weight="bold")
    label(ax, 14.5, 33.5, "Expert systems", fs=6.6)
    label(ax, 14.5, 29.2, "MYCIN (1970s)", fs=6, italic=True, color=G1)
    # example inside ML but outside DL
    label(ax, 36.5, 13, "Support\nvector\nmachines", fs=6.3, italic=True, color=G1)
    # agents: a usage pattern drawn across the boundaries
    ax.add_patch(F.FancyBboxPatch((30.5, 34.5), 41, 6.2, boxstyle="round,pad=0,rounding_size=1.2",
                                  fc=G3, ec=INK, lw=0.7, ls=(0, (3, 2)), zorder=3))
    ax.text(51, 37.6, "Agents (model + tools + loop)", fontsize=7, ha="center", va="center",
            style="italic", zorder=4)
    label(ax, 3.5, 4.2, "Schematic, not to scale", fs=6, ha="left", italic=True, color=G1)
    save(fig, "fig-01-01")


@fig("fig-01-02")
def f0102():
    fig = F.figure(2.9)
    ax = fig.add_axes([0.12, 0.2, 0.86, 0.76])
    years = ["2010", "2011", "2012", "2013", "2014", "2015"]
    teams = ["NEC", "XRCE", "SuperVision\n(AlexNet)", "Clarifai", "GoogLeNet", "ResNet\n(MSRA)"]
    err = [28.2, 25.8, 16.4, 11.7, 6.7, 3.57]
    x = np.arange(6)
    cols = [G3, G3, G1, G1, G1, G1]
    ax.bar(x, err, width=0.62, color=cols, edgecolor=INK, linewidth=0.5, zorder=2)
    ax.axhline(5.1, color=INK, lw=0.8, ls=(0, (4, 2.5)), zorder=3)
    for xi, e in zip(x, err):
        y = e + 0.5 if xi != 5 else 5.7
        ax.text(xi, y, f"{e:g}", ha="center", va="bottom", fontsize=7.2)
    # 2012 with extra training data
    ax.plot([1.69, 2.31], [15.3, 15.3], color="white", lw=0.9, zorder=4)
    ax.annotate("15.3 with extra\ntraining data", xy=(2.31, 15.3), xytext=(2.62, 19.8), fontsize=6.6,
                ha="left", va="center", linespacing=1.1,
                arrowprops=dict(arrowstyle="-", color=G1, lw=0.5, shrinkA=1, shrinkB=0))
    # annotator line label
    ax.annotate("One annotator, 1,500 images (5.1%)", xy=(4.5, 5.1), xytext=(4.62, 13.2), fontsize=6.6,
                ha="right", va="bottom",
                arrowprops=dict(arrowstyle="-", color=G1, lw=0.5, shrinkA=0, shrinkB=0,
                                connectionstyle="angle,angleA=0,angleB=90,rad=0"))
    ax.set_xticks(x)
    ax.set_xticklabels([f"{y}\n{t}" for y, t in zip(years, teams)], fontsize=7, linespacing=1.1)
    ax.tick_params(axis="x", length=0, pad=3)
    ax.set_ylim(0, 30)
    ax.set_xlim(-0.55, 5.55)
    ax.set_yticks(range(0, 31, 5))
    ax.tick_params(axis="y", labelsize=7.5)
    ax.set_ylabel("Top-5 classification error (%)", fontsize=8)
    h = [F.FancyBboxPatch((0, 0), 1, 1, fc=G3, ec=INK, lw=0.5), F.FancyBboxPatch((0, 0), 1, 1, fc=G1, ec=INK, lw=0.5)]
    ax.legend(h, ["Non-deep methods", "Deep neural networks"], loc="upper right", fontsize=7,
              handlelength=1.2, handleheight=0.8, bbox_to_anchor=(1.0, 1.02))
    F.save(fig, "fig-01-02")


# ---- fig-01-03: timeline -------------------------------------------------

def _tx(year):
    """Piecewise-linear year -> x: compressed 1950-2005, expanded 2008-2026.5."""
    if year <= 2005:
        return 2 + (year - 1950) * (44 / 55)
    return 52 + (year - 2008) * (46 / 18.5)


ABOVE = [
    (1950, "Turing's imitation game, 1950"),
    (1956, "Dartmouth workshop, 1956"),
    (1959, "Samuel's checkers learner, 1959"),
    (1969, "Perceptrons critique, 1969"),
    (1973, "Lighthill report, 1973"),
    (1986, "Backpropagation paper, 1986"),
    (2009, "ImageNet dataset, 2009"),
    (2012, "AlexNet wins ImageNet, 2012"),
    (2016, "AlphaGo beats professionals, 2016"),
    (2017, "Transformer, 2017"),
    (2020, "GPT-3, 2020"),
    (2021, "'Foundation model' coined, 2021"),
    (2024, "Reasoning models (o1), 2024"),
    (2025, "DeepSeek-R1, 2025"),
]
BELOW = [
    (1979, "MYCIN evaluation, 1979"),
    (1984, "'AI winter' warning (AAAI), 1984"),
    (1997, "Deep Blue beats Kasparov, 1997"),
    (2022 + 10.5 / 12, "ChatGPT released, Nov 2022"),
    (2023 + 10.5 / 12, "OECD definition revised, Nov 2023"),
    (2024.4, "EU AI Act adopted, 2024"),
    (2024 + 10.5 / 12, "Model Context Protocol, Nov 2024"),
    (2025 + 6.5 / 12, "700M weekly ChatGPT users, Jul 2025"),
    (2026 + 1.5 / 12, "900M weekly users (company), Feb 2026"),
]


def _place(ax, fig, items, y0, step, sign, split, fs=6.2, xmax=99.5, xmin=0.5):
    """Greedy stacking: each label goes on the lowest row where it neither overlaps another label
    nor crosses a leader line, and its own leader crosses no label."""
    r = fig._get_renderer()
    inv = ax.transData.inverted()
    placed = []  # (x, row, a, b)
    right = sorted(i for i in items if _tx(i[0]) >= split)
    left = sorted((i for i in items if _tx(i[0]) < split), reverse=True)
    for year, text in right + left:
        x = _tx(year)
        t = ax.text(0, 0, text, fontsize=fs)
        bb = t.get_window_extent(r)
        t.remove()
        w = inv.transform((bb.width, 0))[0] - inv.transform((0, 0))[0]
        done = False
        for row in range(16):
            for ha in (("right",) if x >= split else ("left",)):
                a, b = (x - 0.6, x - 0.6 + w) if ha == "left" else (x + 0.6 - w, x + 0.6)
                if b > xmax or a < xmin:
                    continue
                ok = True
                for (px, prow, pa, pb) in placed:
                    if prow == row and not (b + 1.2 < pa or a > pb + 1.2):
                        ok = False
                    if prow > row and a - 0.8 <= px <= b + 0.8:
                        ok = False  # an existing leader passes through this label
                    if row > prow and pa - 0.8 <= x <= pb + 0.8:
                        ok = False  # our leader would pass through an existing label
                if ok:
                    placed.append((x, row, a, b)); print(text, row, round(a,1), round(b,1))
                    yl = y0 + sign * step * row
                    ax.plot([x, x], [AXY + sign * 1.0, yl - sign * 0.2], color=G2, lw=0.45, zorder=1)
                    ax.text(a, yl + sign * 0.15, text, fontsize=fs, ha="left",
                            va="bottom" if sign > 0 else "top", color=INK)
                    node(ax, x, AXY, r=0.75, fill="white", lw=0.7)
                    done = True
                    break
            if done:
                break
        if not done:
            raise RuntimeError("no room for " + text)


AXY = 36


@fig("fig-01-03")
def f0103():
    fig, ax = canvas(3.6, ylim=(0, 80))
    # winter bands (approximate dates)
    for a, b, txt in ((1974, 1980, "First AI winter"), (1988, 1993, "Second AI winter")):
        xa, xb = _tx(a), _tx(b)
        ax.add_patch(Rectangle((xa, AXY - 8.5), xb - xa, 17, fc=G4, ec=G2, lw=0.4, hatch="////", zorder=0))
        ax.patches[-1].set_edgecolor(G3)
        ax.text((xa + xb) / 2, AXY - 8.2, txt, fontsize=5.8, rotation=90, ha="center", va="bottom",
                style="italic", color=INK, zorder=2,
                bbox=dict(fc=G4, ec="none", pad=0.4))
    # axis with break
    ax.plot([1, _tx(2005) + 0.5], [AXY, AXY], color=INK, lw=0.9, zorder=1)
    ax.plot([_tx(2008) - 1.5, 99.5], [AXY, AXY], color=INK, lw=0.9, zorder=1)
    for dx in (0, 1.3):
        bx = _tx(2005) + 1.6 + dx
        ax.plot([bx - 0.5, bx + 0.5], [AXY - 1.3, AXY + 1.3], color=INK, lw=0.8)
    for yr in (1950, 1960, 1970, 1980, 1990, 2000, 2010, 2015, 2020, 2025):
        x = _tx(yr)
        ax.plot([x, x], [AXY - 0.9, AXY + 0.9], color=INK, lw=0.7, zorder=1)
    _place(ax, fig, ABOVE, AXY + 3.0, 3.1, +1, 60)
    _place(ax, fig, BELOW, AXY - 3.0, 3.1, -1, 60)
    # era brackets along the top
    def era(a, b, row, txt, open_end=False):
        y = 74 + row * 3.6
        xa, xb = _tx(a), _tx(b)
        ax.plot([xa, xa, xb], [y - 1, y, y], color=INK, lw=0.6)
        if open_end:
            arrow(ax, xb - 2, y, xb + 0.3, y, lw=0.6, ms=5)
        else:
            ax.plot([xb, xb], [y, y - 1], color=INK, lw=0.6)
        ax.text((xa + xb) / 2, y + 0.4, txt, fontsize=6.6, ha="center", va="bottom", weight="bold")
    era(1956, 1988, 0, "Symbolic AI")
    era(1990, 2005, 0, "Statistical ML")
    era(2012, 2026.4, 0, "Deep learning", True)
    era(2020, 2026.4, 1, "LLMs and agents", True)
    label(ax, 1, 1.5, "Axis compressed before 2005. Above: research milestones; below: deployment and policy.",
          fs=5.9, ha="left", italic=True, color=G1)
    save(fig, "fig-01-03")
