"""Figures for chapter 11, drawn from figures/specs/ in the house style."""
import math

import numpy as np

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


@fig("fig-11-01")
def f1101():
    fig, ax = canvas(3.8, ylim=(0, 92))
    box(ax, 40, 84.5, 20, 5.5, "AI risks", fill=G4, fs=9, weight="bold")
    cols = [
        ("Malicious use", [("Fraud and\ndeepfakes", "Ch. 9, 11.4", False), ("Manipulation", "Ch. 9", False),
                           ("Cyber operations", "11.4", False), ("Bio/chem\nweapons", "11.4", False)]),
        ("Malfunctions", [("Unreliable\noutputs", "11.2", False), ("Bias*", "11.3", True),
                          ("Loss of control", "11.6", False)]),
        ("Systemic risks", [("Labour market", "Ch. 8", False), ("Monoculture,\ncorrelated errors", "11.5", False),
                            ("Over-reliance\n(automation bias)", "11.5", False), ("Market\nconcentration", "Ch. 7", False),
                            ("Environmental\nharm*", "Ch. 7", True), ("Privacy*", "Ch. 10", True),
                            ("Copyright*", "Ch. 13", True)]),
    ]
    w, gap = 29.5, 4
    x0 = (100 - 3 * w - 2 * gap) / 2
    for i, (cat, items) in enumerate(cols):
        x = x0 + i * (w + gap)
        cx = x + w / 2
        arrow(ax, 50, 83.8, cx, 75.6, lw=0.8)
        box(ax, x, 69.5, w, 5.5, cat, fill=G4, fs=8.3, weight="bold")
        ax.plot([cx, cx], [68.8, 64.8], color=INK, lw=0.7)
        y = 64
        for name, tag, dashed in items:
            h = 6.6 if "\n" in name else 4.4
            p = box(ax, x, y - h, w, h, "", fill="white", lw=0.7)
            if dashed:
                p.set_linestyle((0, (3, 2)))
            label(ax, x + 1, y - h / 2, name, fs=7, ha="left")
            label(ax, x + w - 0.6, y - h / 2, tag, fs=6.2, ha="right", color=G1, italic=True)
            y -= h + 2.4
    label(ax, x0 - 0.4, 21, "* in 2025 report; outside 2026 report's scope", fs=6.3, ha="left", color=G1, italic=True)
    label(ax, x0 - 0.4, 18.6, "Surveillance and policing span all three\nfamilies (11.1, 11.3)", fs=6.3, ha="left",
          va="top", color=G1, italic=True)
    box(ax, x0, 2.2, 3 * w + 2 * gap, 3.8, "Categories interact (11.7)", fill=G4, fs=7, italic=True, lw=0.5,
        style="round,pad=0.4,rounding_size=0.8")
    save(fig, "fig-11-01")


def _bars(ax, groups, a, b, labs_a, labs_b, names, ylim, yticks, fmt):
    x = np.arange(len(groups))
    bw = 0.34
    ax.bar(x - bw / 2 - 0.01, a, bw, color=G1, edgecolor=INK, lw=0.5, label=names[0])
    ax.bar(x + bw / 2 + 0.01, b, bw, color="white", edgecolor=INK, lw=0.5, hatch="//////", label=names[1])
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    ax.tick_params(axis="x", length=0)
    ax.set_ylim(*ylim)
    ax.set_yticks(yticks)
    ax.set_yticklabels([fmt(t) for t in yticks])
    ax.yaxis.grid(True, color=G3, lw=0.4)
    ax.set_axisbelow(True)
    return x, bw


@fig("fig-11-02")
def f1102():
    with F.plt.rc_context({"hatch.linewidth": 0.4, "hatch.color": G2}):
        _f1102()


def _f1102():
    fig = F.figure(2.7)
    ax = fig.add_axes([0.13, 0.22, 0.85, 0.72])
    obs, ch = [0.60, 0.423], [1 / 3, 0.127]
    x, bw = _bars(ax, ["HELM\n(4 options)", "Hugging Face\n(mostly 10 options)"], obs, ch, None, None,
                  ["Observed agreement", "Chance agreement"], (0, 1.0), np.arange(0, 1.01, 0.2),
                  lambda t: f"{t * 100:.0f}%")
    for xi, v, t in zip(x - bw / 2, obs, ["60%", "42%"]):
        ax.text(xi, v + 0.02, t, ha="center", va="bottom", fontsize=7.5)
    for xi, v, t in zip(x + bw / 2, ch, ["33%", "13%"]):
        ax.text(xi, v + 0.02, t, ha="center", va="bottom", fontsize=7.5)
    ax.set_xlim(-0.6, 1.6)
    ax.set_ylim(0, 1.12)
    ax.spines["left"].set_bounds(0, 1.0)
    ax.set_ylabel("Agreement when both models are wrong")
    ax.legend(loc="upper center", ncol=2, fontsize=7.3, handlelength=1.4, handleheight=1.0,
              bbox_to_anchor=(0.5, 1.04))
    fig.text(0.13, 0.015, "Over 350 models; mean pairwise agreement. Chance assumes wrong answers chosen at random.",
             fontsize=6.3, color=G1, style="italic")
    F.save(fig, "fig-11-02")


@fig("fig-11-03")
def f1103():
    with F.plt.rc_context({"hatch.linewidth": 0.4, "hatch.color": G2}):
        _f1103()


def _f1103():
    fig = F.figure(2.9)
    ax = fig.add_axes([0.11, 0.22, 0.87, 0.72])
    cor, cor_sd = [79.7, 81.3, 82.3], [11.7, 10.1, 4.2]
    inc, inc_sd = [19.8, 24.8, 45.5], [14.0, 11.6, 9.1]
    x, bw = _bars(ax, ["Inexperienced", "Moderately\nexperienced", "Very\nexperienced"], cor, inc, None, None,
                  ["AI suggestion correct", "AI suggestion incorrect"], (0, 118), range(0, 101, 20),
                  lambda t: f"{t}")
    xa, xb = x - bw / 2 - 0.01, x + bw / 2 + 0.01
    ek = dict(fmt="none", ecolor=INK, elinewidth=0.6, capsize=2, capthick=0.6)
    ax.errorbar(xa, cor, yerr=cor_sd, **ek)
    ax.errorbar(xb, inc, yerr=inc_sd, **ek)
    for xi, v, s in zip(xa, cor, cor_sd):
        ax.text(xi, v + s + 1.5, f"{v:g}", ha="center", va="bottom", fontsize=7)
    for xi, v, s in zip(xb, inc, inc_sd):
        ax.text(xi, v + s + 1.5, f"{v:g}", ha="center", va="bottom", fontsize=7)
    ax.spines["left"].set_bounds(0, 100)
    ax.set_ylabel("Mammograms rated correctly (%)")
    ax.legend(loc="upper center", ncol=2, fontsize=7.3, handlelength=1.4, handleheight=1.0,
              bbox_to_anchor=(0.5, 1.04))
    fig.text(0.11, 0.015, "27 radiologists; 50 mammograms; the ‘AI’ was simulated by the researchers. "
             "Error bars: ± 1 SD.\nAll differences significant (P ≤ .003).", fontsize=6.3, color=G1, style="italic")
    F.save(fig, "fig-11-03")
