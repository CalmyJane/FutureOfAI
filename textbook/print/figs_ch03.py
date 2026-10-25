"""Figures for chapter 3, drawn from figures/specs/ in the house style.

The tokenisation table-figure (spec tbl-03-01.md) became Tables 3.1 and 3.2 in ch03.md.
"""
import math

import numpy as np
from matplotlib.patches import Arc, Ellipse, Rectangle

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save

MONO = "DejaVu Sans Mono"


@fig("fig-03-01")
def f0301():
    """Embedding-space sketch (spec fig-03-01)."""
    fig, ax = canvas(2.8, ylim=(0, 63))
    # unlabelled axes
    arrow(ax, 3, 3, 3, 61, lw=0.6, ms=6)
    arrow(ax, 3, 3, 98, 3, lw=0.6, ms=6)
    label(ax, 97, 6.2, "2-D sketch of a space with hundreds or thousands of dimensions", fs=6.2, ha="right", italic=True, color=G1)

    def pt(x, y, t, dx=0, dy=2.6, ha="center"):
        ax.add_patch(F.Circle((x, y), 0.75, fc=INK, ec=INK, lw=0.5, zorder=3))
        label(ax, x + dx, y + dy, t, fs=7.6, ha=ha)

    # cluster 1: gender
    P = {"man": (10, 40), "woman": (21, 49), "king": (24, 34), "queen": (35, 43)}
    for k, (x, y) in P.items():
        dy = 2.6 if k in ("woman", "queen") else -2.8
        pt(x, y, k, dy=dy)
    arrow(ax, *P["man"], *P["woman"], lw=0.8, ms=6)
    arrow(ax, *P["king"], *P["queen"], lw=0.8, ms=6, ls="--")
    label(ax, 33.5, 37.0, "male → female", fs=6.4, italic=True, color=G1, ha="left")
    # cluster 2: capitals
    C = [("France", "Paris", 60, 44), ("Germany", "Berlin", 66, 33), ("Italy", "Rome", 58, 22)]
    for c, cap, x, y in C:
        pt(x, y, c, dx=-1.6, dy=0, ha="right")
        pt(x + 14, y + 5, cap, dx=1.6, dy=0, ha="left")
        arrow(ax, x, y, x + 14, y + 5, lw=0.8, ms=6, ls="--" if c != "France" else "-")
    label(ax, 72, 53.5, "country → capital", fs=6.4, italic=True, color=G1)
    # cluster 3: animals
    ax.add_patch(Ellipse((20, 15.5), 26, 13, fc=G4, ec=G2, lw=0.6, zorder=1))
    for t, x, y in (("cat", 14, 17), ("dog", 21, 13.5), ("horse", 26.5, 16.8)):
        pt(x, y, t, dy=-2.6 if t == "dog" else 2.6)
    label(ax, 35.5, 10, "animals", fs=6.4, italic=True, color=G1, ha="left")
    # inset
    box(ax, 5, 54, 28, 6, "king − man + woman ≈ queen", fill="white", fs=6.8, lw=0.6,
        style="round,pad=0,rounding_size=1")
    save(fig, "fig-03-01")


@fig("fig-03-02")
def f0302():
    """Decoder-only transformer with attention inset (spec fig-03-02)."""
    fig, ax = canvas(3.6, ylim=(0, 80))
    cols = [20, 29, 38, 47, 56]
    toks = ["The", "␣cat", "␣sat", "␣on", "␣the"]
    # 1 tokens
    for x, t in zip(cols, toks):
        box(ax, x - 3.9, 2, 7.8, 5, "", fill="white", lw=0.6, style="round,pad=0,rounding_size=0.8")
        ax.text(x, 4.5, t, ha="center", va="center", fontsize=6.3, family=MONO)
        arrow(ax, x, 7.2, x, 11.3, lw=0.6, ms=5)
    label(ax, 14.5, 4.5, "Tokens", fs=6.8, ha="right", italic=True, color=G1)
    # 2 embedding + position
    box(ax, 15.5, 11.5, 45, 5, "Embedding", fill=G4, fs=7.5, lw=0.7, style="round,pad=0,rounding_size=1")
    box(ax, 0.5, 11.5, 10.5, 5, "Position\ninfo", fill="white", fs=6.2, lw=0.6, style="round,pad=0,rounding_size=1")
    arrow(ax, 11.2, 14, 15.3, 14, lw=0.6, ms=5)
    label(ax, 13.2, 16.1, "+", fs=8)
    # 3 transformer block; each token's vector runs up its own residual stream (vertical line)
    box(ax, 2, 20.5, 62, 29, "", fill="white", lw=0.9, style="round,pad=0,rounding_size=2")
    label(ax, 9, 46.1, "Transformer\nblock", fs=7.0, weight="bold")
    label(ax, 2.5, 18.6, "residual stream", fs=5.9, ha="left", italic=True, color=G1)
    ax.plot([15.2, 19.4], [18.6, 18.6], color=G1, lw=0.4)
    # masked attention: information flows from earlier tokens (and the token itself) into each stream
    box(ax, 15.5, 22, 45, 12, "", fill=G4, lw=0.5, style="round,pad=0,rounding_size=1")
    label(ax, 9, 29.5, "Masked\nattention", fs=6.6)
    label(ax, 9, 23.9, "itself and\nearlier only", fs=5.9, italic=True, color=G1)
    ay = 25.0
    for j in range(1, 5):
        for i in range(j):
            d = cols[j] - cols[i]
            a = F.FancyArrowPatch((cols[i], ay), (cols[j], ay), arrowstyle="-|>", mutation_scale=4,
                                  lw=0.45, color=G1, connectionstyle=f"arc3,rad={-0.3 if d > 10 else -0.45}",
                                  shrinkA=1, shrinkB=1, zorder=3)
            ax.add_patch(a)
    for x in cols:
        # attention to itself: a small loop at each point
        ax.add_patch(Arc((x + 1.0, ay - 1.0), 2.0, 2.0, theta1=150, theta2=100, lw=0.45, color=G1, zorder=3))
    # residual streams (drawn over the attention box)
    for x in cols:
        ax.plot([x, x], [16.7, 49.5], color=INK, lw=0.7, zorder=2.5)
        ax.add_patch(F.Circle((x, ay), 0.6, fc=INK, ec=INK, zorder=4))
    # feed-forward: reads from the stream, processes each token on its own, adds its result back
    label(ax, 9, 38.9, "Feed-\nforward", fs=6.6)
    fy, fh = 37.2, 4.4
    for x in cols:
        box(ax, x + 1.4, fy, 4.6, fh, "", fill=G4, lw=0.5, style="round,pad=0,rounding_size=0.8")
        label(ax, x + 3.7, fy + fh / 2, "FF", fs=6.2, color=G1)
        ax.plot([x, x + 3.7, x + 3.7], [35.7, 35.7, fy], color=INK, lw=0.5, zorder=2.5)
        ax.plot([x + 3.7, x + 3.7, x + 2.2], [fy + fh, 43.6, 43.6], color=INK, lw=0.5, zorder=2.5)
        arrow(ax, x + 2.6, 43.6, x + 0.75, 43.6, lw=0.5, ms=4)
        ax.add_patch(F.Circle((x, 43.6), 0.8, fc="white", ec=INK, lw=0.5, zorder=4))
        ax.plot([x - 0.5, x + 0.5], [43.6, 43.6], color=INK, lw=0.5, zorder=5)
        ax.plot([x, x], [43.1, 44.1], color=INK, lw=0.5, zorder=5)
    # × N bracket
    ax.plot([65, 66.2, 66.2, 65], [21, 21, 49, 49], color=INK, lw=0.6)
    ax.text(68.6, 35, "× N blocks\n(e.g. 96 in GPT-3)", fontsize=6.2, rotation=90, ha="center", va="center",
            linespacing=1.1)
    # 4 output layer (only the last position's vector is used to predict the next token)
    arrow(ax, cols[-1], 49.0, cols[-1], 53.3, lw=0.6, ms=5)
    box(ax, 15.5, 53.5, 45, 4.5, "Output layer", fill=G4, fs=7.2, lw=0.7, style="round,pad=0,rounding_size=1")
    arrow(ax, 38, 58.2, 38, 61.0, lw=0.6, ms=5)
    # 5 next-token probabilities
    label(ax, 15.5, 77.5, "Next-token probabilities", fs=7, ha="left", weight="bold")
    probs = [("␣edge", 7.3), ("␣floor", 5.2), ("␣table", 4.9), ("␣bed", 4.4)]
    sc = 3.6  # units per percentage point (0-10% -> 36 units)
    x0 = 27
    for k, (t, p) in enumerate(probs):
        y = 74.2 - k * 2.9
        ax.text(x0 - 1, y, t, ha="right", va="center", fontsize=6.1, family=MONO)
        ax.add_patch(Rectangle((x0, y - 1.0), p * sc, 2.0, fc=G1, ec="none"))
        label(ax, x0 + p * sc + 0.8, y, f"{p}%", fs=6.4, ha="left")
    ax.plot([x0, x0], [63.9, 75.6], color=INK, lw=0.5)
    label(ax, x0 + 0.8, 62.6, "… 50,000+ other tokens", fs=6.3, ha="left", italic=True, color=G1)

    # inset: attention from "its"
    box(ax, 72, 2, 27.5, 76, "", fill="white", lw=0.6, style="round,pad=0,rounding_size=1.5")
    label(ax, 85.75, 74.3, "Attention from 'its'\n(encoder, layer 5 of 6)", fs=6.5, weight="bold")
    words = "The Law will never be perfect , but its application should be just".split()
    top, step = 66.5, 4.6
    ys = [top - i * step for i in range(len(words))]
    src_y = ys[words.index("its")]
    sx, wx = 77.5, 87.5
    for w, y in zip(words, ys):
        if w == "its":
            continue
        strong = w in ("Law", "application")
        ax.plot([sx + 0.6, wx - 0.8], [src_y, y], color=INK if strong else G3, lw=2.0 if strong else 0.5,
                solid_capstyle="round", zorder=2)
    for w, y in zip(words, ys):
        label(ax, wx, y, w, fs=6.6, ha="left", weight="bold" if w in ("Law", "application") else "normal")
    label(ax, sx, src_y, "its", fs=7, ha="right", weight="bold")
    label(ax, 85.75, 4.2, "after Vaswani et al. (2017), Fig. 4", fs=5.8, italic=True, color=G1)
    save(fig, "fig-03-02")


@fig("fig-03-03")
def f0303():
    """Training pipeline (spec fig-03-03)."""
    fig, ax = canvas(3.3, ylim=(0, 74))
    rs = "round,pad=0,rounding_size=1.2"
    pill = "round,pad=0,rounding_size=2.4"
    # columns: (x0, width)
    C = [(1, 27), (31, 22), (56, 22), (81, 19)]
    SY, SH = 32, 11   # stage boxes
    PY, PH = 15, 6.5  # output pills
    stages = [("Pre-training", "predict next token"), ("Instruction\ntuning", "supervised fine-tuning"),
              ("Preference\ntraining", "RL or DPO"), ("Reasoning RL", "reward correct\nanswers")]
    outs = [("Base model", "continues text"), ("Instruction\nmodel", None), ("Chat\nassistant", None),
            ("Reasoning\nmodel", None)]
    for k, ((x, w), (st, sub), (o, osub)) in enumerate(zip(C, stages, outs)):
        cx = x + w / 2
        fill = G4
        box(ax, x, SY, w, SH, "", fill=fill, lw=0.9 if k == 0 else 0.7, style=rs,
            )
        two = "\n" in st
        label(ax, cx, SY + SH - (3.4 if two else 2.6), st, fs=7.6, weight="bold")
        label(ax, cx, SY + (3.4 if "\n" in sub else 2.2 if two else 3.0), sub, fs=6.1, italic=True, color=G1)
        ow = min(w - 2, 17)
        box(ax, cx - ow / 2, PY, ow, PH, "", fill="white", lw=0.8, style=pill,
            )
        if osub:
            label(ax, cx, PY + 4.3, o, fs=7, weight="bold")
            label(ax, cx, PY + 1.8, osub, fs=6.1, italic=True, color=G1)
        else:
            label(ax, cx, PY + PH / 2, o, fs=6.8, weight="bold")
        arrow(ax, cx, SY - 0.2, cx, PY + PH + 0.3, lw=0.8, ms=6)
    # links from each output to the next stage
    for k in range(3):
        (x, w), (nx, nw) = C[k], C[k + 1]
        ox = x + w / 2 + min(w - 2, 17) / 2
        arrow(ax, ox + 0.2, PY + PH / 2, nx - 0.3, SY + 2.5, lw=0.8, ms=6, ls="--" if k == 2 else "-")
    label(ax, 76.8, 27.5, "branch", fs=5.9, italic=True, color=G1, ha="right")
    # inputs
    IY = 52
    # web-scale text as a cylinder
    cx = C[0][0] + C[0][1] / 2
    cw, ch = 17, 11
    ax.add_patch(Rectangle((cx - cw / 2, IY), cw, ch, fc=G4, ec="none"))
    ax.plot([cx - cw / 2] * 2, [IY, IY + ch], color=INK, lw=0.7)
    ax.plot([cx + cw / 2] * 2, [IY, IY + ch], color=INK, lw=0.7)
    ax.add_patch(Ellipse((cx, IY), cw, 3, fc=G4, ec=INK, lw=0.7))
    ax.add_patch(Rectangle((cx - cw / 2 + 0.35, IY), cw - 0.7, 0.01 + 0, fc=G4, ec="none"))
    ax.add_patch(Ellipse((cx, IY + ch), cw, 3, fc="white", ec=INK, lw=0.7))
    # hide the upper half of the bottom ellipse outline
    ax.add_patch(Rectangle((cx - cw / 2 + 0.3, IY + 0.05), cw - 0.6, 1.6, fc=G4, ec="none"))
    label(ax, cx, IY + 6.6, "Web-scale text", fs=6.8, weight="bold")
    label(ax, cx, IY + 3.4, "trillions of tokens", fs=6, italic=True, color=G1)
    arrow(ax, cx, IY - 1.7, cx, SY + SH + 0.3, lw=0.8, ms=6)
    # demonstrations
    x, w = C[1]
    box(ax, x + 1.5, IY, w - 3, 8, "Written\ndemonstrations", fill="white", fs=6.4, lw=0.6, style=rs)
    arrow(ax, x + w / 2, IY - 0.3, x + w / 2, SY + SH + 0.3, lw=0.8, ms=6)
    # human + AI feedback -> reward model
    x, w = C[2]
    box(ax, x - 1.5, 62, 12, 9.5, "Human\nrankings\n(RLHF)", fill="white", fs=6.1, lw=0.6, style=rs)
    box(ax, x + 11.5, 62, 12, 9.5, "Principles +\nAI feedback\n(RLAIF)", fill="white", fs=6.1, lw=0.6, style=rs)
    box(ax, x + 2, 48.5, 18, 6.5, "Reward model\n(not used by DPO)", fill=G4, fs=6.2, lw=0.6, style=rs)
    arrow(ax, x + 4.5, 61.8, x + 8, 55.2, lw=0.7, ms=5)
    arrow(ax, x + 17.5, 61.8, x + 14, 55.2, lw=0.7, ms=5)
    arrow(ax, x + w / 2, 48.3, x + w / 2, SY + SH + 0.3, lw=0.8, ms=6)
    # checkable problems
    x, w = C[3]
    box(ax, x + 0.5, IY, w - 1, 9.5, "Problems with\ncheckable\nanswers", fill="white", fs=6.2, lw=0.6, style=rs)
    arrow(ax, x + w / 2, IY - 0.3, x + w / 2, SY + SH + 0.3, lw=0.8, ms=6)
    # compute annotation under the row
    def brace(xa, xb, txt):
        y = 8.5
        ax.plot([xa, xa, xb, xb], [y + 1.2, y, y, y + 1.2], color=G1, lw=0.6)
        label(ax, (xa + xb) / 2, y - 1.3, txt, fs=6.5, italic=True, color=G1, va="top")
    brace(C[0][0], C[0][0] + C[0][1], "most compute")
    brace(C[1][0], C[2][0] + C[2][1], "far less data")
    brace(C[3][0], C[3][0] + C[3][1], "small but\ngrowing share")
    save(fig, "fig-03-03")
