"""Figures for chapter 9, drawn from figures/specs/ in the house style."""
import math

import numpy as np

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


@fig("fig-09-01")
def f0901():
    # Kirchenbauer et al. (2023), Fig. 6 legend and Sec. 7.1: T5-Large span attack on a
    # gamma = 0.5, delta = 2.0 soft watermark (multinomial sampling), 500 sequences of T = 200 +/- 5 tokens.
    eps = [0.0, 0.1, 0.3, 0.5, 0.7]
    auc = [0.998, 0.988, 0.954, 0.838, 0.696]
    ppl = [6.3, 13.1, 21.2, 28.4, 33.9]
    fig = F.figure(2.75)
    ax = fig.add_axes([0.12, 0.17, 0.74, 0.69])
    ax2 = ax.twinx()
    ax.set_xlim(-0.035, 0.735)
    ax.set_ylim(0.5, 1.0)
    ax2.set_ylim(0, 50)
    ax.set_xticks(eps)
    ax.set_xticklabels(["0", "0.1", "0.3", "0.5", "0.7"])
    ax.set_yticks([0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ax.set_yticklabels(["0.5", "0.6", "0.7", "0.8", "0.9", "1.0"])
    ax2.set_yticks(range(0, 51, 10))
    for a in (ax, ax2):
        a.tick_params(labelsize=7.5)
    ax2.spines["right"].set_visible(True)
    ax2.spines["top"].set_visible(False)
    # the left axis starts at AUC 0.5, which is chance level
    ax.text(0.725, 0.506, "AUC 0.5 = chance", fontsize=6.6, ha="right", va="bottom", color=G1, style="italic")
    ax.plot(eps, auc, color=INK, lw=1.3, marker="o", ms=4, mfc=INK, mec=INK, zorder=4, clip_on=False)
    ax2.plot(eps, ppl, color=G2, lw=1.3, ls=(0, (4, 2)), marker="s", ms=3.8, mfc="white", mec=G1, mew=0.8, zorder=3, clip_on=False)
    # value labels placed on the side of each point away from both lines
    auc_off = [(0, -6, "center", "top"), (0, -6, "center", "top"), (0, -6, "center", "top"),
               (5, 3, "left", "bottom"), (0, -6, "center", "top")]
    ppl_off = [(4, -4, "left", "top"), (4, -4, "left", "top"), (4, -4, "left", "top"),
               (4, -4, "left", "top"), (-4, 5, "right", "bottom")]
    for x, v, (dx, dy, ha, va) in zip(eps, auc, auc_off):
        ax.annotate(f"{v:.3f}", (x, v), xytext=(dx, dy), textcoords="offset points", ha=ha, va=va, fontsize=6.6)
    for x, v, (dx, dy, ha, va) in zip(eps, ppl, ppl_off):
        ax2.annotate(f"{v:.1f}", (x, v), xytext=(dx, dy), textcoords="offset points", ha=ha, va=va, fontsize=6.6, color=G1)
    ax.set_xlabel("Share of tokens replaced by the attacker (\u03b5)", fontsize=8)
    ax.set_ylabel("Detection AUC", fontsize=8)
    ax2.set_ylabel("Perplexity (lower = more fluent)", fontsize=8, rotation=270, labelpad=11)
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([], [], color=INK, lw=1.3, marker="o", ms=4, label="Detection AUC (left axis)"),
                       Line2D([], [], color=G2, lw=1.3, ls=(0, (4, 2)), marker="s", ms=3.8, mfc="white", mec=G1, mew=0.8,
                              label="Perplexity (right axis)")],
              loc="lower center", bbox_to_anchor=(0.5, 1.02), ncol=2, fontsize=7.3, handlelength=2.6)
    F.save(fig, "fig-09-01")


@fig("fig-09-02")
def f0902():
    fig, ax = canvas(3.75, ylim=(0, 84))
    dash = (0, (4, 2.5))
    # ---- main path: four steps -------------------------------------------------
    steps = [("Create", "Camera or AI tool signs\nmanifest 1; its actions\nbegin with \u201ccreated\u201d"),
             ("Edit", "Editor adds manifest 2\n(\u201copened\u201d); manifest 1\nbecomes an ingredient"),
             ("Publish", "Platform displays\nContent Credentials"),
             ("Validate", "Signatures, certificates\nand hashes; does the\nhard binding match?")]
    w, hgt, yb = 20.0, 15.5, 53
    xs = [0.6 + i * 26.2 for i in range(4)]
    for (t, sub), x in zip(steps, xs):
        box(ax, x, yb, w, hgt, "", fill="white")
        label(ax, x + w / 2, yb + hgt - 2.7, t, fs=7.6, weight="bold")
        label(ax, x + w / 2, yb + 6.0, sub, fs=6.1, italic=True, color=G1)
    ym = yb + hgt / 2
    for a, b in zip(xs, xs[1:]):
        arrow(ax, a + w + 0.8, ym, b - 0.8, ym)
    # callout above Validate
    cx = xs[3] + w / 2
    box(ax, xs[3], 74.5, w, 7.0, "", fill=G4, lw=0.6, style="round,pad=0.4,rounding_size=2")
    label(ax, cx, 79.6, "Provenance \u2260 truth", fs=7.4, italic=True, weight="bold")
    label(ax, cx, 76.4, "Records origin, not accuracy", fs=6.0, italic=True, color=G1)
    ax.plot([cx, cx], [74.0, yb + hgt + 0.5], color=G2, lw=0.5)
    # optional watermark embedded at creation
    ax.add_patch(F.FancyBboxPatch((xs[0] + 1.5, 39.5), w - 3, 7.5, boxstyle="round,pad=0.3,rounding_size=1",
                                  fc="white", ec=INK, lw=0.7, ls=":"))
    label(ax, xs[0] + w / 2, 43.25, "Optional invisible\nwatermark in content", fs=6.1)
    ax.plot([xs[0] + w / 2, xs[0] + w / 2], [47.4, yb - 0.5], color=G2, lw=0.5, ls=":")
    # ---- recovery path (dashed) --------------------------------------------------
    gx = (xs[1] + w + xs[2]) / 2
    sx, sw = xs[1] + 2.0, 18.5
    box(ax, sx, 39.5, sw, 7.5, "Manifest stripped\n(e.g. re-encoding)", fill=G4, fs=6.4, lw=0.7)
    arrow(ax, gx, ym - 0.6, sx + sw - 3.5, 47.6, ls="--", lw=0.8)
    lx, lw_ = xs[2] + 2.5, 19.0
    box(ax, lx, 39.5, lw_, 7.5, "Soft-binding lookup in\na cloud repository", fill=G4, fs=6.4, lw=0.7)
    arrow(ax, sx + sw + 0.6, 43.25, lx - 0.6, 43.25, ls="--", lw=0.8)
    arrow(ax, lx + lw_ + 0.6, 43.25, cx, yb - 0.6, ls="--", lw=0.8, rad=0.35)
    label(ax, xs[3] + 3.6, 40.6, "copy of the\nmanifest", fs=6.0, italic=True, color=G1, ha="left")
    # ---- inside one manifest -----------------------------------------------------
    ax.add_patch(F.FancyBboxPatch((0.6, 1.0), 98.5, 33.0, boxstyle="round,pad=0.3,rounding_size=1.5",
                                  fc="none", ec=G2, lw=0.5, ls=(0, (2, 2))))
    label(ax, 2.2, 31.2, "Inside each manifest", fs=7.2, weight="bold", ha="left")
    # assertions
    box(ax, 2.2, 2.6, 35.5, 25.0, "", fill="white", lw=0.7)
    label(ax, 2.2 + 35.5 / 2, 25.0, "Assertions", fs=7.2, weight="bold")
    items = [(0, "\u2022 Actions: \u201ccreated\u201d or \u201copened\u201d, then edits;"),
             (1, "AI output marked trainedAlgorithmicMedia"),
             (0, "\u2022 Ingredients: earlier files and their manifests"),
             (0, "\u2022 Hard binding: hash of the file\u2019s bytes"),
             (0, "\u2022 Soft binding: watermark or fingerprint")]
    for i, (ind, t) in enumerate(items):
        label(ax, 3.4 + 1.6 * ind, 21.0 - i * 3.9, t, fs=6.0, ha="left")
    # claim
    box(ax, 45.5, 9.0, 18.5, 15.5, "", fill="white", lw=0.7)
    label(ax, 54.75, 21.6, "Claim", fs=7.2, weight="bold")
    label(ax, 54.75, 14.6, "Lists every\nassertion by its\ncryptographic hash", fs=6.1, italic=True, color=G1)
    # claim signature
    box(ax, 71.5, 9.0, 26.0, 15.5, "", fill="white", lw=0.7)
    label(ax, 84.5, 21.6, "Claim signature", fs=7.2, weight="bold")
    label(ax, 84.5, 14.6, "COSE_Sign1, made with the\nkey of an X.509 certificate;\nRFC 3161 time-stamp", fs=6.1, italic=True, color=G1)
    arrow(ax, 38.3, 16.75, 44.9, 16.75)
    label(ax, 41.6, 19.0, "hashed", fs=6.0, italic=True, color=G1)
    arrow(ax, 64.6, 16.75, 70.9, 16.75)
    label(ax, 67.75, 19.0, "signed", fs=6.0, italic=True, color=G1)
    save(fig, "fig-09-02")


@fig("fig-09-03")
def f0903():
    # Two panels with separate axes: the studies measure different quantities
    # (treatment minus control; gap between two opposing AI advocates).
    fig = F.figure(4.6)
    axA = fig.add_axes([0.335, 0.665, 0.6, 0.27])
    axB = fig.add_axes([0.335, 0.2, 0.6, 0.33])
    A = [
        ("Static AI message (GPT-4o)", 6.1),
        ("Static AI message (GPT-4.5)", 6.9),
        ("Average AI conversation", 9.4),
        ("\u201cMaximal persuasion\u201d\nAI conversation", 15.9),
    ]
    B = [
        ("US 2024 presidential (Harris\nvs Trump), n = 2,306", 2.88, (2.02, 3.74)),
        ("Canada 2025 (Carney vs\nPoilievre), baseline", 10.05, (7.52, 12.57)),
        ("Poland 2025 (Trzaskowski\nvs Nawrocki), baseline", 9.94, (6.68, 13.20)),
        ("Massachusetts psychedelics\nballot measure, n = 193\nnon-extreme voters", 22.73, (17.00, 28.46)),
    ]
    h = 0.66
    ya = [4, 3, 2, 1]
    for (lab, v), y in zip(A, ya):
        axA.barh(y, v, height=h, color=G3, edgecolor=INK, lw=0.5)
        axA.text(v + 0.3, y, f"{v:.1f}", va="center", fontsize=7)
    axA.set_yticks(ya)
    axA.set_yticklabels([a[0] for a in A], fontsize=6.5, linespacing=1.05)
    axA.set_xlim(0, 20)
    axA.set_ylim(0.4, 4.6)
    axA.set_xticks(range(0, 21, 5))
    axA.set_xlabel("Effect: treatment minus control (points, 0\u2013100 scale)", fontsize=7.5)
    axA.set_title("A  Hackenburg et al. (2025), UK, 707 policy issues", fontsize=7.5, weight="bold", loc="left", x=-0.52)
    yb = [4, 3, 2, 1]
    for (lab, v, ci), y in zip(B, yb):
        axB.barh(y, v, height=h, color=G1, edgecolor=INK, lw=0.5)
        axB.errorbar(v, y, xerr=[[v - ci[0]], [ci[1] - v]], fmt="none", ecolor=INK, elinewidth=0.7, capsize=2.2, capthick=0.7)
        axB.text(ci[1] + 0.5, y, f"{v:.2f}", va="center", fontsize=7)
    axB.set_yticks(yb)
    axB.set_yticklabels([b[0] for b in B], fontsize=6.5, linespacing=1.05)
    axB.set_xlim(0, 32)
    axB.set_ylim(0.4, 4.6)
    axB.set_xticks(range(0, 31, 5))
    axB.set_xlabel("Gap between pro-A and pro-B AI advocates (points, 0\u2013100 scale)", fontsize=7.5)
    axB.set_title("B  Lin et al. (2025), election experiments", fontsize=7.5, weight="bold", loc="left", x=-0.52)
    for ax in (axA, axB):
        ax.tick_params(axis="y", length=0, pad=4)
        ax.tick_params(axis="x", labelsize=7.2)
        ax.spines["left"].set_visible(False)
    fig.text(0.015, 0.012, "Durability: 36\u201342% of the conversation effect remained after one month (A); slightly\nmore than one third after more than a month (B, US). Whiskers: 95% CIs.",
             fontsize=6.4, ha="left", va="bottom", color=G1, style="italic", linespacing=1.15)
    F.save(fig, "fig-09-03")


@fig("fig-09-04")
def f0904():
    fig = F.figure(2.9)
    ax = fig.add_axes([0.1, 0.27, 0.86, 0.6])
    cats = ["Clicked a traditional\nsearch result link", "Clicked a link inside\nthe AI summary", "Ended browsing session\non this page"]
    w_ai = [8, 1, 26]
    wo = [15, None, 16]
    x = np.arange(3)
    bw = 0.32
    for i in range(3):
        ax.bar(x[i] - bw / 2, w_ai[i], bw, color=G1, edgecolor=INK, lw=0.5)
        ax.text(x[i] - bw / 2, w_ai[i] + 0.6, f"{w_ai[i]}%", ha="center", va="bottom", fontsize=7.5)
        if wo[i] is None:
            ax.text(x[i] + bw / 2, 0.6, "n/a", ha="center", va="bottom", fontsize=7, color=G1, style="italic")
        else:
            ax.bar(x[i] + bw / 2, wo[i], bw, color=G3, edgecolor=INK, lw=0.5)
            ax.text(x[i] + bw / 2, wo[i] + 0.6, f"{wo[i]}%", ha="center", va="bottom", fontsize=7.5)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=7.5)
    ax.tick_params(axis="x", length=0, pad=5)
    ax.set_ylim(0, 30)
    ax.set_yticks(range(0, 31, 10))
    ax.tick_params(axis="y", labelsize=7.5)
    ax.set_ylabel("Share of search page visits (%)", fontsize=7.8)
    ax.set_xlim(-0.6, 2.6)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(fc=G1, ec=INK, lw=0.5, label="With AI summary"), Patch(fc=G3, ec=INK, lw=0.5, label="Without AI summary")],
              loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, fontsize=7.5, handlelength=1.4, handleheight=0.9)
    fig.text(0.1, 0.02, "18% of the 68,879 Google searches studied produced an AI summary.",
             fontsize=6.8, ha="left", va="bottom", style="italic", color=G1)
    F.save(fig, "fig-09-04")
