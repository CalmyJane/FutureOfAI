"""Figures for chapter 9, drawn from figures/specs/ in the house style."""
import math

import numpy as np

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


@fig("fig-09-03")
def f0903():
    fig = F.figure(3.6)
    ax = fig.add_axes([0.335, 0.215, 0.645, 0.725])
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
        ("Massachusetts psychedelics\nballot measure, non-extreme\nvoters (pro vs anti AI)", 22.73, (17.00, 28.46)),
    ]
    ya = [11.4, 10.3, 9.2, 8.0]
    yb = [5.6, 4.3, 3.0, 1.5]
    h = 0.66
    for (lab, v), y in zip(A, ya):
        ax.barh(y, v, height=h, color=G3, edgecolor=INK, lw=0.5)
        ax.text(v + 0.4, y, f"{v:.1f}", va="center", fontsize=7)
    for (lab, v, ci), y in zip(B, yb):
        ax.barh(y, v, height=h, color=G1, edgecolor=INK, lw=0.5)
        ax.errorbar(v, y, xerr=[[v - ci[0]], [ci[1] - v]], fmt="none", ecolor=INK, elinewidth=0.7, capsize=2.2, capthick=0.7)
        ax.text(ci[1] + 0.5, y, f"{v:.2f}", va="center", fontsize=7)
    ax.set_yticks(ya + yb)
    ax.set_yticklabels([a[0] for a in A] + [b[0] for b in B], fontsize=6.5, linespacing=1.05)
    ax.tick_params(axis="y", length=0, pad=4)
    ax.spines["left"].set_visible(False)
    # dashed reference line at 0, interrupted where the group headings run
    for y0, y1 in ((0.5, 6.4), (7.3, 12.0)):
        ax.plot([0, 0], [y0, y1], color=INK, lw=0.9, ls=(0, (3, 2)), clip_on=False)
    ax.set_xlim(0, 30)
    ax.set_ylim(0.5, 12.9)
    ax.set_xticks(range(0, 31, 5))
    ax.tick_params(axis="x", labelsize=7.5)
    ax.set_xlabel("Persuasive effect (points on a 0\u2013100 scale)", fontsize=8)
    ax.text(-0.5, 12.5, "Hackenburg et al. (2025), UK, 707 policy issues: treatment minus control",
            transform=ax.get_yaxis_transform(), fontsize=7, weight="bold", ha="left", va="center")
    ax.text(-0.5, 6.85, "Lin et al. (2025), elections: gap between opposing AI advocates",
            transform=ax.get_yaxis_transform(), fontsize=7, weight="bold", ha="left", va="center")
    ax.text(18.6, 9.7, "Durability: 36\u201342% of the\nconversation effect remained\nafter one month (Hackenburg\net al.); slightly more than\none third after more than\na month (Lin et al., US).",
            fontsize=6.1, va="center", ha="left", linespacing=1.15,
            bbox=dict(boxstyle="round,pad=0.4,rounding_size=0.3", fc=G4, ec=G2, lw=0.5))
    fig.text(0.015, 0.012, "Dashed line at 0: average effect of campaign contact and ads in US general\nelections \u2248 0 (Kalla & Broockman 2018, 49 field experiments). Whiskers: 95% CIs.",
             fontsize=6.4, ha="left", va="bottom", color=G1, style="italic", linespacing=1.15)
    F.save(fig, "fig-09-03")


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
    ax.set_ylim(0.4, 1.0)
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
    ax.axhline(0.5, color=G2, lw=0.7, ls=(0, (4, 2.5)), zorder=1)
    ax.text(0.72, 0.507, "chance (AUC 0.5)", fontsize=6.6, ha="right", va="bottom", color=G1, style="italic")
    ax.plot(eps, auc, color=INK, lw=1.3, marker="o", ms=4, mfc=INK, mec=INK, zorder=4, clip_on=False)
    ax2.plot(eps, ppl, color=G2, lw=1.3, ls=(0, (4, 2)), marker="s", ms=3.8, mfc="white", mec=G1, mew=0.8, zorder=3, clip_on=False)
    for x, v in zip(eps, auc):
        ax.annotate(f"{v:.3f}", (x, v), xytext=(0, 5.5), textcoords="offset points", ha="center", va="bottom", fontsize=6.6)
    for x, v in zip(eps, ppl):
        ax2.annotate(f"{v:.1f}", (x, v), xytext=(0, -6), textcoords="offset points", ha="center", va="top", fontsize=6.6, color=G1)
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
             ("Edit", "Editor adds signed\nmanifest 2 (\u201copened\u201d);\nmanifest 1 kept inside"),
             ("Publish", "Platform displays\nContent Credentials"),
             ("Validate", "Signatures, certificates\nand hashes; does the\nhard binding match?")]
    w, hgt, yb = 20.5, 15.5, 53
    xs = [0.6 + i * 26.4 for i in range(4)]
    for (t, sub), x in zip(steps, xs):
        box(ax, x, yb, w, hgt, "", fill="white")
        label(ax, x + w / 2, yb + hgt - 2.7, t, fs=7.6, weight="bold")
        label(ax, x + w / 2, yb + 6.0, sub, fs=6.1, italic=True, color=G1)
    ym = yb + hgt / 2
    for a, b in zip(xs, xs[1:]):
        arrow(ax, a + w + 0.8, ym, b - 0.8, ym)
    # callout above Validate
    cx = xs[3] + w / 2
    box(ax, xs[3] - 1.5, 74.5, w + 3, 7.0, "", fill=G4, lw=0.6, style="round,pad=0.4,rounding_size=2")
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
    ax.add_patch(F.FancyBboxPatch((0.6, 1.0), 99.4, 33.0, boxstyle="round,pad=0.3,rounding_size=1.5",
                                  fc="none", ec=G2, lw=0.5, ls=(0, (2, 2))))
    label(ax, 2.2, 31.2, "Inside each manifest", fs=7.2, weight="bold", ha="left")
    # assertions
    box(ax, 2.2, 2.6, 37.5, 25.0, "", fill="white", lw=0.7)
    label(ax, 2.2 + 37.5 / 2, 25.0, "Assertions", fs=7.2, weight="bold")
    items = ["Actions: \u201ccreated\u201d or \u201copened\u201d, then edits;",
             "    AI output marked trainedAlgorithmicMedia",
             "Ingredients: earlier files and their manifests",
             "Hard binding: hash of the file\u2019s bytes",
             "Soft binding: watermark or fingerprint"]
    for i, t in enumerate(items):
        bullet = "" if t.startswith(" ") else "\u2022 "
        label(ax, 3.6, 21.0 - i * 3.9, bullet + t.strip() if bullet else "    " + t.strip(), fs=6.0, ha="left")
    # claim
    box(ax, 46.0, 9.0, 19.0, 15.5, "", fill="white", lw=0.7)
    label(ax, 55.5, 21.6, "Claim", fs=7.2, weight="bold")
    label(ax, 55.5, 14.6, "Lists every\nassertion by its\ncryptographic hash", fs=6.1, italic=True, color=G1)
    # claim signature
    box(ax, 71.5, 9.0, 27.0, 15.5, "", fill="white", lw=0.7)
    label(ax, 85.0, 21.6, "Claim signature", fs=7.2, weight="bold")
    label(ax, 85.0, 14.6, "COSE_Sign1, made with the\nkey of an X.509 certificate;\nRFC 3161 time-stamp", fs=6.1, italic=True, color=G1)
    arrow(ax, 40.4, 16.75, 45.3, 16.75)
    label(ax, 42.85, 19.0, "hashed", fs=6.0, italic=True, color=G1)
    arrow(ax, 65.7, 16.75, 70.8, 16.75)
    label(ax, 68.25, 19.0, "signed", fs=6.0, italic=True, color=G1)
    save(fig, "fig-09-02")


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
