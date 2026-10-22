"""Figures for chapter 2, drawn from figures/specs/ in the house style."""
import math

import numpy as np

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


@fig("fig-02-01")
def f0201():
    fig, ax = canvas(2.2, ylim=(0, 50))
    node(ax, 8, 36, 4.2, fill="white", text="2", fs=9)
    node(ax, 8, 14, 4.2, fill="white", text="1", fs=9)
    label(ax, 8, 43, "input $x_1$", fs=7.5)
    label(ax, 8, 6.5, "input $x_2$", fs=7.5)
    # neuron
    c = node(ax, 52, 25, 11, fill=G4, lw=1.1)
    ax.plot([52, 52], [15.5, 34.5], color=INK, lw=0.6)
    label(ax, 46.5, 27, "Σ", fs=14)
    label(ax, 46.5, 20.5, "sum", fs=6.5)
    xs = np.linspace(54, 61, 30)
    ax.plot(xs, [21 + max(0, x - 57.5) * 1.6 for x in xs], color=INK, lw=0.9)
    label(ax, 57.5, 30.5, "ReLU", fs=6.5)
    arrow(ax, 12.5, 35, 41.5, 28)
    arrow(ax, 12.5, 15, 41.5, 22)
    label(ax, 26, 35.5, "weight 0.5", fs=7.5, rot=-12)
    label(ax, 26, 14.6, "weight −1", fs=7.5, rot=12)
    box(ax, 44, 44, 16, 4.5, "bias +0.2", fill="white", fs=7.5)
    arrow(ax, 52, 43.6, 52, 36.4)
    arrow(ax, 63.5, 25, 76, 25)
    box(ax, 77, 20.5, 19, 9, "output = 0.2", fill="white", fs=8)
    label(ax, 52, 7.5, "0.5 × 2 + (−1) × 1 + 0.2 = 0.2", fs=7.5, italic=True)
    label(ax, 86.5, 9, "inputs 1 and 1:\nsum = −0.3 → output 0", fs=6.5, color=G1)
    save(fig, "fig-02-01")


@fig("fig-02-02")
def f0202():
    fig, ax = canvas(2.6, ylim=(0, 60))
    cols = {0: [45, 33, 21], 1: [51, 39, 27, 15], 2: [39, 27]}
    xs = {0: 15, 1: 50, 2: 85}
    for a, b in ((0, 1), (1, 2)):
        for ya in cols[a]:
            for yb in cols[b]:
                ax.plot([xs[a], xs[b]], [ya, yb], color=G2, lw=0.5, zorder=1)
    ax.plot([xs[0], xs[1]], [45, 51], color=INK, lw=1.4, zorder=2)
    label(ax, 30, 52.5, "one weight", fs=7, italic=True)
    names = ["$x_1$", "$x_2$", "$x_3$"]
    for i, y in enumerate(cols[0]):
        node(ax, xs[0], y, 3.2, fill="white", text=names[i], fs=7.5).set_zorder(3)
    for y in cols[1]:
        node(ax, xs[1], y, 3.2, fill=G4, text="+b", fs=6.5).set_zorder(3)
    for i, y in enumerate(cols[2]):
        node(ax, xs[2], y, 3.2, fill=G4, text="+b", fs=6.5).set_zorder(3)
        label(ax, xs[2] + 9, y, f"output {i+1}", fs=7, ha="center")
    for k, t in ((0, "Input layer"), (1, "Hidden layer"), (2, "Output layer")):
        label(ax, xs[k], 58, t, fs=8, weight="bold")
    label(ax, 32.5, 8, "12 weights", fs=7.5)
    label(ax, 67.5, 8, "8 weights", fs=7.5)
    label(ax, 50, 2.5, "Total: 20 weights + 6 biases = 26 parameters", fs=7.5, italic=True)
    arrow(ax, 3, 2.5, 13, 2.5, lw=0.8)
    label(ax, 3, 5.6, "forward pass", fs=6.5, ha="left", color=G1)
    save(fig, "fig-02-02")


@fig("fig-02-03")
def f0203():
    fig = F.figure(2.5)
    ax = fig.add_axes([0.08, 0.12, 0.6, 0.82])
    w = np.linspace(-0.2, 1.2, 200)
    loss = (w - 0.5) ** 2
    ax.plot(w, loss, color=INK)
    ax.set_xlabel("Weight")
    ax.set_ylabel("Loss")
    ax.set_xticks([])
    ax.set_yticks([])
    pts = [0.2, 0.32, 0.41, 0.46]
    for a, b in zip(pts, pts[1:]):
        ax.annotate("", xy=(b, (b - 0.5) ** 2 + 0.01), xytext=(a, (a - 0.5) ** 2 + 0.01),
                    arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.9, mutation_scale=7))
    ax.plot([0.2], [0.09], "o", color=INK, ms=4)
    ax.annotate("start", xy=(0.2, 0.09), xytext=(-0.15, 0.02), fontsize=8,
                arrowprops=dict(arrowstyle="-", color=G2, lw=0.6))
    ax.plot([0.5], [0], "o", mfc="white", mec=INK, ms=4.5)
    ax.text(0.5, -0.05, "minimum (lowest loss)", ha="center", fontsize=7.5)
    tx = np.array([0.04, 0.36])
    ax.plot(tx, 0.09 - 0.6 * (tx - 0.2), color=G2, lw=0.8)
    ax.annotate("slope = gradient", xy=(0.07, 0.168), xytext=(-0.17, 0.3), fontsize=7, color=G1,
                arrowprops=dict(arrowstyle="-", color=G2, lw=0.6))
    ax.annotate("", xy=(0.95, (0.95 - 0.5) ** 2), xytext=(0.2, 0.09),
                arrowprops=dict(arrowstyle="-|>", color=G2, lw=0.9, ls="--", mutation_scale=7, shrinkA=0, shrinkB=0,
                                connectionstyle="arc3,rad=-0.35"))
    from matplotlib.lines import Line2D
    ax.legend(handles=[Line2D([], [], color=INK, lw=1, marker=">", ms=3, label="moderate learning rate"),
                       Line2D([], [], color=G2, lw=1, ls="--", label="too large: overshoots")],
              loc="upper center", fontsize=7, handlelength=2.2)
    ax.set_ylim(-0.07, 0.5)
    ax.set_xlim(-0.2, 1.25)
    # inset: contour map
    ax2 = fig.add_axes([0.72, 0.22, 0.27, 0.62])
    tt = np.linspace(0, 2 * np.pi, 200)
    for r in (0.25, 0.5, 0.75, 1.0):
        ax2.plot(1.8 * r * np.cos(tt), r * np.sin(tt), color=G2, lw=0.6)
    path = np.array([[-1.6, 0.7], [-0.9, -0.5], [-0.6, 0.35], [-0.25, -0.18], [-0.08, 0.06], [0, 0]])
    ax2.plot(path[:, 0], path[:, 1], color=INK, lw=0.9, marker="o", ms=2)
    ax2.set_aspect("equal")
    ax2.axis("off")
    ax2.set_title("two weights, seen from above", fontsize=7, pad=2)
    F.save(fig, "fig-02-03")


@fig("fig-02-04")
def f0204():
    fig = F.figure(2.3)
    ax = fig.add_axes([0.08, 0.14, 0.9, 0.8])
    t = np.linspace(0, 10, 300)
    train = 0.08 + 0.9 * np.exp(-t / 1.6)
    val = 0.25 + 0.75 * np.exp(-t / 1.6) + 0.018 * np.maximum(0, t - 4) ** 1.4
    ax.plot(t, train, color=INK, label="Training error")
    ax.plot(t, val, color=INK, ls="--", label="Validation error")
    i = np.argmin(val)
    ax.axvline(t[i], color=G2, ls=":", lw=1)
    ax.axvspan(0, t[i], color=G4, zorder=0)
    ax.text(t[i] + 0.1, 0.95, "early stopping point", fontsize=7.5, color=G1)
    ax.text(t[i] / 2, 0.95, "underfitting → good fit", fontsize=7.5, ha="center")
    ax.text(8.6, 0.95, "overfitting", fontsize=7.5, ha="center")
    ax.annotate("", xy=(9.6, train[-1]), xytext=(9.6, val[-1]), arrowprops=dict(arrowstyle="<->", lw=0.7, color=G1))
    ax.text(9.45, (train[-1] + val[-1]) / 2, "generalisation\ngap", fontsize=7, ha="right", va="center", color=G1)
    ax.set_xlabel("Training time (epochs)")
    ax.set_ylabel("Error")
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(0, 1.05)
    ax.set_xlim(0, 10)
    ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.62), fontsize=7.5)
    F.save(fig, "fig-02-04")
