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
    ax.add_patch(Ellipse((74, 25), 40, 24, fill=False, ec=INK, lw=0.8, ls=(0, (1, 1.6))))
    label(ax, 74, 15.3, "Generative AI", fs=6.8, italic=True)
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
    ax.add_patch(F.FancyBboxPatch((26.5, 34.5), 45, 6.2, boxstyle="round,pad=0,rounding_size=1.2",
                                  fc=G3, ec=INK, lw=0.7, ls=(0, (3, 2)), zorder=3))
    ax.text(49, 37.6, "Agents (model + tools + loop)", fontsize=7, ha="center", va="center",
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
    ax.plot([4.5, 4.5], [5.1, 15.9], color=G1, lw=0.5)
    ax.text(5.5, 16.2, "One annotator, 1,500 images (5.1%)", fontsize=6.6, ha="right", va="bottom")
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


# ---- fig-01-03: timeline (vertical, so every label fits on one line) -------

def _ty(year):
    """Piecewise-linear year -> y (top = 1950): compressed 1950-2005, expanded 2008-2026.5."""
    if year <= 2005:
        return 75 - (year - 1950) * (35 / 55)
    return 36 - (year - 2008) * (33 / 18.5)


RESEARCH = [
    (1950, "Turing's imitation game (1950)"),
    (1956, "Dartmouth workshop (1956)"),
    (1959, "Samuel's checkers learner (1959)"),
    (1969, "Perceptrons critique (1969)"),
    (1973, "Lighthill report (1973)"),
    (1986, "Backpropagation paper (1986)"),
    (2009, "ImageNet dataset (2009)"),
    (2012, "AlexNet wins ImageNet (2012)"),
    (2016, "AlphaGo beats professionals (2016)"),
    (2017, "Transformer (2017)"),
    (2020, "GPT-3 (2020)"),
    (2021, "'Foundation model' coined (2021)"),
    (2024 + 8.5 / 12, "Reasoning models, o1 (Sept 2024)"),
    (2025, "DeepSeek-R1 (2025)"),
]
DEPLOY = [
    (1977, "First AI winter (c. 1974–80)"),
    (1979, "MYCIN evaluation (1979)"),
    (1984, "'AI winter' warning, AAAI (1984)"),
    (1990, "Second AI winter (from c. 1987; end disputed)"),
    (1997, "Deep Blue beats Kasparov (1997)"),
    (2022 + 10.5 / 12, "ChatGPT released (Nov 2022)"),
    (2023 + 10.5 / 12, "OECD definition revised (Nov 2023)"),
    (2024.4, "EU AI Act adopted (2024)"),
    (2024 + 10.5 / 12, "Model Context Protocol (Nov 2024)"),
    (2025 + 6.5 / 12, "700M weekly ChatGPT users (Jul 2025)"),
    (2026 + 1.5 / 12, "900M weekly users, company (Feb 2026)"),
]
AX = 50


def _spread(ys, gap, lo, hi):
    """Push label positions apart (ys sorted top->bottom) to at least `gap`, within [lo, hi]."""
    out = list(ys)
    for _ in range(200):
        moved = False
        for i in range(1, len(out)):
            d = out[i - 1] - out[i]
            if d < gap:
                s = (gap - d) / 2
                out[i - 1] += s
                out[i] -= s
                moved = True
        out = [min(hi, max(lo, y)) for y in out]
        for i in range(1, len(out)):  # enforce after clamping
            if out[i - 1] - out[i] < gap - 1e-6:
                if out[i - 1] >= hi - 1e-6:
                    out[i] = out[i - 1] - gap
                elif out[i] <= lo + 1e-6:
                    out[i - 1] = out[i] + gap
        if not moved:
            break
    return out


def _side(ax, items, sign, gap=2.8):
    ys = [_ty(y) for y, _ in items]
    ly = _spread(ys, gap, 1.6, 76)
    for (yr, txt), y, yl in zip(items, ys, ly):
        winter = "AI winter (" in txt
        x0 = AX + sign * 1.0
        x1 = AX + sign * 4.0
        x2 = AX + sign * 6.5
        if not winter:
            ax.plot([x0, x1, x2], [y, y, yl], color=G2, lw=0.45, zorder=1)
            ax.add_patch(F.Circle((AX, y), 0.6, fc="white" if sign < 0 else INK, ec=INK, lw=0.6, zorder=3))
        ax.text(x2 + sign * 0.6, yl, txt, fontsize=6.8, ha="left" if sign > 0 else "right", va="center",
                style="italic" if winter else "normal", color=INK)


@fig("fig-01-03")
def f0103():
    fig, ax = canvas(3.6, ylim=(0, 80))
    # winter bands (approximate dates)
    ya, yb = _ty(1974), _ty(1980)
    ax.add_patch(Rectangle((AX - 3, yb), 6, ya - yb, fc=G4, ec=G3, lw=0.4, hatch="//////", zorder=0))
    # second winter: start c. 1987, end disputed -> no closing edge, band fades out
    ya, yb = _ty(1987), _ty(1993)
    ax.add_patch(Rectangle((AX - 3, yb), 6, ya - yb, fc=G4, ec="none", hatch="//////", zorder=0))
    ax.patches[-1].set_edgecolor(G3)
    ax.patches[-1].set_linewidth(0)
    ax.plot([AX - 3, AX + 3], [ya, ya], color=G3, lw=0.4, zorder=0)
    n = 8
    for i in range(n):
        y0, y1 = _ty(1993 + 4 * i / n), _ty(1993 + 4 * (i + 1) / n)
        ax.add_patch(Rectangle((AX - 3, y1), 6, y0 - y1, fc=G4, ec="none", alpha=1 - (i + 1) / (n + 1), zorder=0))
    # axis with a break between 2005 and 2008
    ax.plot([AX, AX], [76.5, _ty(2005) - 0.6], color=INK, lw=0.9, zorder=2)
    ax.plot([AX, AX], [_ty(2008) + 0.8, 1.0], color=INK, lw=0.9, zorder=2)
    for dy in (0, 1.1):
        by = _ty(2005) - 1.4 - dy
        ax.plot([AX - 1.3, AX + 1.3], [by + 0.5, by - 0.5], color=INK, lw=0.8)
    marks = [_ty(y) for y, t in RESEARCH + DEPLOY if "AI winter (" not in t]
    for yr in (1960, 1970, 1980, 1990, 2000, 2010, 2020):
        y = _ty(yr)
        if min(abs(y - m) for m in marks) < 1.3:
            continue
        ax.plot([AX - 0.9, AX + 0.9], [y, y], color=INK, lw=0.7, zorder=2)
    _side(ax, RESEARCH, -1)
    _side(ax, DEPLOY, +1)
    label(ax, AX - 3, 79, "Research milestones", fs=7, ha="right", weight="bold")
    label(ax, AX + 3, 79, "Deployment and policy", fs=7, ha="left", weight="bold")

    # era brackets along the left edge
    def era(a, b, x, txt, ty):
        ya, yb = _ty(a), _ty(b)
        ax.plot([x + 1, x, x, x + 1], [ya, ya, yb, yb], color=INK, lw=0.6)
        ax.text(x + 1.6, ty, txt, fontsize=6.4, ha="left", va="center", weight="bold", color=G1, linespacing=1.1)
    era(1956, 1988, 0.6, "Symbolic\nAI", _ty(1979))
    era(1990, 2005, 0.6, "Statistical\nML", _ty(1997.5))
    era(2012, 2026.4, 0.6, "Deep\nlearning", _ty(2015.5))
    era(2020, 2026.4, 2.2, "LLMs and\nagents", _ty(2023.2))
    label(ax, AX + 2.2, _ty(2006.5), "axis compressed before 2005", fs=5.9, ha="left", italic=True, color=G1)
    save(fig, "fig-01-03")
