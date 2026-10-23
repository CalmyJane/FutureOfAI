"""Figures for chapter 2, drawn from figures/specs/ in the house style."""
import matplotlib.pyplot as plt
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
    fig, ax = canvas(2.85, ylim=(0, 66))
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
        label(ax, xs[k], 63.5, t, fs=8, weight="bold")
    # weight matrices of Section 2.2
    label(ax, 32.5, 58, "$W_1$: 4 × 3", fs=7.5)
    label(ax, 67.5, 58, "$W_2$: 2 × 4", fs=7.5)
    label(ax, 32.5, 8, "12 weights", fs=7.5)
    label(ax, 67.5, 8, "8 weights", fs=7.5)
    label(ax, 50, 2.5, "Total: 20 weights + 6 biases = 26 parameters", fs=7.5, italic=True)
    arrow(ax, 1, 2.5, 19, 2.5, lw=1.1, ms=10)
    label(ax, 1, 5.8, "forward pass", fs=6.5, ha="left", color=G1)
    save(fig, "fig-02-02")


@fig("fig-02-03")
def f0203():
    """Worked example of Section 2.3: input 2, target 1, loss (2w - 1)^2, start w = 0.2."""
    L = lambda w: (2 * w - 1) ** 2  # noqa: E731
    path_a = [0.2]
    for _ in range(3):                       # learning rate 0.1: w <- w - 0.1 * 4(2w - 1)
        w = path_a[-1]
        path_a.append(w - 0.1 * 4 * (2 * w - 1))
    w_b = 0.2 - 0.5 * 4 * (2 * 0.2 - 1)      # learning rate 0.5
    assert [round(v, 6) for v in path_a] == [0.2, 0.44, 0.488, 0.4976]
    assert abs(w_b - 1.4) < 1e-9 and abs(L(w_b) - 3.24) < 1e-9 and abs(L(0.2) - 0.36) < 1e-9

    fig = F.figure(2.55)
    # main panel: whole curve, overshoot path
    ax = fig.add_axes([0.085, 0.15, 0.5, 0.8])
    w = np.linspace(-0.05, 1.5, 300)
    ax.plot(w, L(w), color=INK, lw=1.2)
    ax.set_xlim(-0.05, 1.55)
    ax.set_ylim(-0.12, 3.75)
    ax.set_xticks([0, 0.2, 0.5, 1, 1.4])
    ax.set_xticklabels(["0", "0.2", "0.5", "1", "1.4"], fontsize=7)
    ax.set_yticks([0, 1, 2, 3])
    ax.set_yticklabels(["0", "1", "2", "3"], fontsize=7)
    ax.set_xlabel("Weight $w$", fontsize=8, labelpad=2)
    ax.set_ylabel("Loss", fontsize=8, labelpad=2)
    ax.plot([0.2], [L(0.2)], "o", color=INK, ms=3.6, zorder=4)
    ax.plot([0.5], [0], "o", mfc="white", mec=INK, ms=4, zorder=4)
    ax.plot([w_b], [L(w_b)], "o", mfc=G2, mec=G1, ms=3.6, zorder=4)
    ax.annotate("", xy=(w_b, L(w_b)), xytext=(0.2, L(0.2)),
                arrowprops=dict(arrowstyle="-|>", color=G1, lw=0.9, ls=(0, (3, 2)), mutation_scale=8,
                                shrinkA=3, shrinkB=3, connectionstyle="arc3,rad=-0.3"))
    ax.text(0.62, 2.95, "learning rate 0.5:\novershoots", fontsize=6.8, color=G1, ha="center", va="center")
    ax.text(1.34, 3.24, "$w$ = 1.4\nloss 3.24", fontsize=6.6, ha="right", va="center")
    ax.text(0.23, 0.55, "start\n$w$ = 0.2, loss 0.36", fontsize=6.6, ha="left", va="bottom")
    ax.text(0.5, -0.06, "minimum", fontsize=6.6, ha="center", va="top", color=G1)
    # zoom frame
    zx, zy = (0.15, 0.53), (-0.03, 0.42)
    ax.add_patch(plt.Rectangle((zx[0], zy[0]), zx[1] - zx[0], zy[1] - zy[0], fill=False, ec=G2, lw=0.6, ls=":"))
    # close-up panel: learning rate 0.1
    az = fig.add_axes([0.68, 0.15, 0.3, 0.8])
    wz = np.linspace(zx[0], zx[1], 200)
    az.plot(wz, L(wz), color=INK, lw=1.2)
    az.set_xlim(*zx)
    az.set_ylim(*zy)
    az.set_xticks([0.2, 0.44, 0.5])
    az.set_xticklabels(["0.2", "0.44", "0.5"], fontsize=7)
    az.set_yticks([0, 0.36])
    az.set_yticklabels(["0", "0.36"], fontsize=7)
    az.set_xlabel("Weight $w$ (close-up)", fontsize=8, labelpad=2)
    for a, b in zip(path_a, path_a[1:]):
        if b - a > 0.02:
            az.annotate("", xy=(b, L(b)), xytext=(a, L(a)),
                        arrowprops=dict(arrowstyle="-|>", color=INK, lw=0.9, mutation_scale=7, shrinkA=2, shrinkB=2))
    for v in path_a:
        az.plot([v], [L(v)], "o", color=INK, ms=2.6 if v > 0.2 else 3.6, zorder=4)
    tx = np.array([0.16, 0.25])
    az.plot(tx, L(0.2) - 2.4 * (tx - 0.2), color=G2, lw=0.8)
    az.text(0.255, 0.355, "slope = gradient\n= −2.4", fontsize=6.4, color=G1, ha="left", va="top")
    az.text(0.445, 0.07, "0.44", fontsize=6.4, ha="right", va="bottom")
    az.annotate("0.488, then 0.4976", xy=(0.49, 0.003), xytext=(0.43, 0.17), fontsize=6.4, ha="center",
                arrowprops=dict(arrowstyle="-", color=G2, lw=0.5, shrinkA=1, shrinkB=2))
    az.text(0.34, 0.39, "learning rate 0.1:\neach step closes 80%\nof the gap", fontsize=6.6,
            ha="center", va="top")
    F.save(fig, "fig-02-03")


@fig("fig-02-04")
def f0204():
    """(a) residual block after He et al. 2016, Fig. 2; (b) He et al. 2016, Table 2."""
    fig = F.figure(2.6)
    # panel (a): diagram in canvas units
    ad = fig.add_axes([0.0, 0.0, 0.42, 1.0])
    ad.set_xlim(0, 42)
    ad.set_ylim(0, 62)
    ad.axis("off")
    cx = 17
    label(ad, 1, 59.5, "(a)", fs=8.2, weight="bold", ha="left")
    label(ad, cx - 2.2, 56.5, "$x$", fs=8.5, ha="right")
    arrow(ad, cx, 58.5, cx, 49.6)
    box(ad, cx - 8, 44.5, 16, 4.6, "weight layer", fill=G4, fs=7.5)
    arrow(ad, cx, 44.1, cx, 35.6)
    label(ad, cx + 1.4, 39.8, "ReLU", fs=7, ha="left")
    box(ad, cx - 8, 30.5, 16, 4.6, "weight layer", fill=G4, fs=7.5)
    arrow(ad, cx, 30.1, cx, 21.4)
    label(ad, cx - 1.4, 25.6, "$F(x)$", fs=8, ha="right")
    node(ad, cx, 19, 2.3, fill="white", text="+", fs=9)
    # shortcut: from the input line round the right of the boxes into the adder
    ad.plot([cx, cx + 14], [53.5, 53.5], color=INK, lw=0.9)
    ad.plot([cx + 14, cx + 14], [53.5, 19], color=INK, lw=0.9)
    arrow(ad, cx + 14, 19, cx + 2.4, 19, ms=7)
    label(ad, cx + 15.3, 37, "shortcut\n(identity): $x$", fs=6.8, ha="left", rot=0)
    arrow(ad, cx, 16.6, cx, 6)
    label(ad, cx + 1.4, 13.2, "$F(x) + x$", fs=8, ha="left")
    label(ad, cx + 1.4, 8.2, "ReLU", fs=7, ha="left")
    # panel (b): bar chart
    ab = fig.add_axes([0.53, 0.2, 0.46, 0.66])
    data = {"Plain network": (27.94, 28.54), "Residual network\n(ResNet)": (27.88, 25.03)}
    bw = 0.34
    for g, (name, (v18, v34)) in enumerate(data.items()):
        for k, (v, col) in enumerate(((v18, G3), (v34, G1))):
            x = g + (k - 0.5) * (bw + 0.03)
            ab.bar(x, v - 24, bw, bottom=24, color=col, ec=INK, lw=0.5)
            ab.text(x, v + 0.08, f"{v:.2f}", ha="center", va="bottom", fontsize=6.8)
    ab.set_ylim(24, 30)
    ab.set_yticks([24, 25, 26, 27, 28, 29, 30])
    ab.set_yticklabels([str(t) for t in range(24, 31)], fontsize=7)
    ab.set_xlim(-0.6, 1.6)
    ab.set_xticks([0, 1])
    ab.set_xticklabels(list(data), fontsize=7.2)
    ab.tick_params(axis="x", length=0)
    ab.set_ylabel("Top-1 error (%)", fontsize=7.6, labelpad=2)
    ab.text(0, 29.45, "deeper is worse", fontsize=6.8, ha="center", style="italic")
    ab.text(1, 29.45, "deeper is better", fontsize=6.8, ha="center", style="italic")
    from matplotlib.patches import Patch
    ab.legend(handles=[Patch(fc=G3, ec=INK, lw=0.5, label="18 layers"), Patch(fc=G1, ec=INK, lw=0.5, label="34 layers")],
              loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2, fontsize=7, handlelength=1.1,
              handleheight=0.8, columnspacing=1.2, borderaxespad=0.2)
    fig.text(0.47, 0.955, "(b)", fontsize=8.2, weight="bold", va="center")
    fig.text(0.53, 0.015, "ImageNet validation, 10-crop testing; axis starts at 24%", fontsize=6.2,
             color=G1, style="italic")
    F.save(fig, "fig-02-04")


@fig("fig-02-05")
def f0205():
    """Convolution and pooling worked example of Section 2.6; every number computed here."""
    img = np.array([[0, 0, 0, 1, 1]] * 5)
    ker = np.array([[-1, 0, 1]] * 3)
    fmap = np.array([[int((img[r:r + 3, c:c + 3] * ker).sum()) for c in range(3)] for r in range(3)])
    assert fmap.tolist() == [[0, 3, 3]] * 3
    pin = np.array([[1, 3, 0, 2], [4, 2, 1, 0], [0, 1, 5, 2], [2, 0, 3, 1]])
    pout = pin.reshape(2, 2, 2, 2).max(axis=(1, 3))
    assert pout.tolist() == [[4, 2], [2, 5]]

    s = 4.4  # cell size
    fig, ax = canvas(3.25, ylim=(0, 72))

    def grid(x0, ytop, a, fills, fmt=str, fs=7.5, colors=None, bold=None):
        n_r, n_c = a.shape
        for r in range(n_r):
            for c in range(n_c):
                x, y = x0 + c * s, ytop - (r + 1) * s
                ax.add_patch(plt.Rectangle((x, y), s, s, fc=fills(a[r, c]), ec=INK, lw=0.5))
                tc = colors(a[r, c]) if colors else INK
                wt = "bold" if bold is not None and bold[r, c] else "normal"
                ax.text(x + s / 2, y + s / 2, fmt(a[r, c]), ha="center", va="center", fontsize=fs, color=tc,
                        weight=wt)

    def kfmt(v):
        return "+1" if v > 0 else ("−1" if v < 0 else "0")

    top = 58
    # (a) image
    xi = 3
    label(ax, 1, 70, "(a)", fs=8.2, weight="bold", ha="left")
    label(ax, xi + 2.5 * s, 62, "Image (5 × 5)", fs=7.5)
    grid(xi, top, img, lambda v: G1 if v == 0 else "white", colors=lambda v: "white" if v == 0 else INK)
    # highlighted window: rows 1-3, columns 2-4
    ax.add_patch(plt.Rectangle((xi + s, top - 3 * s), 3 * s, 3 * s, fill=False, ec=INK, lw=2.0, zorder=5))
    # kernel
    xk = 36
    label(ax, 30.5, top - 2.5 * s, "∗", fs=12)
    label(ax, xk + 1.5 * s, 62, "Kernel (3 × 3):\nvertical-edge detector", fs=7.2)
    grid(xk, top - s, ker, lambda v: "white", fmt=kfmt)
    # (c) feature map
    xm = 75
    label(ax, 61, top - 2.5 * s, "=", fs=11)
    label(ax, 67.5, 70, "(c)", fs=8.2, weight="bold", ha="left")
    label(ax, xm + 1.5 * s, 62, "Feature map (3 × 3)", fs=7.5)
    grid(xm, top - s, fmap, lambda v: G3 if v else "white")
    ax.add_patch(plt.Rectangle((xm + s, top - 2 * s), s, s, fill=False, ec=INK, lw=2.0, zorder=5))
    label(ax, xm + 1.5 * s, top - 4 * s - 2.6, "5 − 3 + 1 = 3 positions\nper row and column", fs=6.3, color=G1)
    # (b) the highlighted calculation
    label(ax, 1, 31.5, "(b)", fs=8.2, weight="bold", ha="left")
    label(ax, 8, 31.5, "Highlighted window, column by column:  (−1) × 0 × 3 rows  +  0 × 0 × 3 rows  "
          "+  (+1) × 1 × 3 rows  =  3", fs=7.0, ha="left")
    arrow(ax, xi + 2.5 * s, top - 3 * s - 0.4, xi + 2.5 * s, 34, lw=0.7, color=G1, ms=6)
    arrow(ax, 93.5, 34, xm + 1.5 * s, top - 2 * s - 0.4, lw=0.7, color=G1, ms=6, rad=0.35)
    # (d) max pooling
    yp = 24
    label(ax, 1, 26.5, "(d)", fs=8.2, weight="bold", ha="left")
    xp = 9
    blockfill = {(0, 0): "white", (0, 1): G4, (1, 0): G4, (1, 1): "white"}
    for r in range(4):
        for c in range(4):
            x, y = xp + c * s, yp - (r + 1) * s
            ax.add_patch(plt.Rectangle((x, y), s, s, fc=blockfill[(r // 2, c // 2)], ec=G2, lw=0.4))
            is_max = pin[r, c] == pout[r // 2, c // 2]
            ax.text(x + s / 2, y + s / 2, str(pin[r, c]), ha="center", va="center", fontsize=7.5,
                    weight="bold" if is_max else "normal")
    for k in (0, 2, 4):
        ax.plot([xp + k * s] * 2, [yp, yp - 4 * s], color=INK, lw=0.9 if k == 2 else 0.7)
        ax.plot([xp, xp + 4 * s], [yp - k * s] * 2, color=INK, lw=0.9 if k == 2 else 0.7)
    arrow(ax, xp + 4 * s + 2, yp - 2 * s, xp + 4 * s + 11, yp - 2 * s)
    xo = xp + 4 * s + 13
    for r in range(2):
        for c in range(2):
            x, y = xo + c * s, yp - s - (r + 1) * s
            ax.add_patch(plt.Rectangle((x, y), s, s, fc=blockfill[(r, c)], ec=INK, lw=0.7))
            ax.text(x + s / 2, y + s / 2, str(pout[r, c]), ha="center", va="center", fontsize=7.5, weight="bold")
    label(ax, xo + 2 * s + 4, yp - 2 * s, "2 × 2 max pooling:\nkeep the largest value\nin each block "
          "(4 × 4 → 2 × 2)", fs=7, ha="left")
    label(ax, 50, 2, "9 weights + 1 bias, reused at every position (a fully connected layer from "
          "25 pixels to 9 outputs would need 225 weights)", fs=6.3, color=G1, italic=True)
    save(fig, "fig-02-05")


@fig("fig-02-06")
def f0206():
    fig = F.figure(2.45)
    # (a) overfitting over training time
    ax = fig.add_axes([0.045, 0.13, 0.43, 0.76])
    t = np.linspace(0, 10, 300)
    train = 0.08 + 0.9 * np.exp(-t / 1.6)
    val = 0.25 + 0.75 * np.exp(-t / 1.6) + 0.018 * np.maximum(0, t - 4) ** 1.4
    ax.plot(t, train, color=INK, label="Training error")
    ax.plot(t, val, color=INK, ls="--", label="Validation error")
    i = np.argmin(val)
    ax.axvline(t[i], color=G2, ls=":", lw=1)
    ax.axvspan(0, t[i], color=G4, zorder=0)
    ax.text(t[i] + 0.15, 1.0, "early\nstopping point", fontsize=6.5, color=G1, va="top")
    ax.text(t[i] / 2, 1.0, "underfitting\n→ good fit", fontsize=6.5, ha="center", va="top")
    ax.text(8.7, 1.0, "overfitting", fontsize=6.5, ha="center", va="top")
    ax.annotate("", xy=(9.7, train[-1]), xytext=(9.7, val[-1]), arrowprops=dict(arrowstyle="<->", lw=0.7, color=G1))
    ax.text(9.5, (train[-1] + val[-1]) / 2, "generalisation\ngap", fontsize=6.3, ha="right", va="center", color=G1)
    ax.set_xlabel("Training time (epochs)", fontsize=7.6, labelpad=2)
    ax.set_ylabel("Error", fontsize=7.6, labelpad=2)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(0, 1.05)
    ax.set_xlim(0, 10)
    ax.legend(loc="center right", bbox_to_anchor=(1.0, 0.6), fontsize=6.6, handlelength=1.8)
    fig.text(0.0, 0.97, "(a)", fontsize=8.2, weight="bold", va="center")
    # (b) double descent over model size (schematic)
    bx = fig.add_axes([0.56, 0.13, 0.43, 0.76])
    x = np.linspace(0, 10, 1001)
    thr = 4.0
    tr = np.where(x < thr, 0.62 * np.clip(1 - x / thr, 0, 1) ** 1.5, 0.0)
    te = 0.13 + 0.75 * np.exp(-x / 1.1) + 0.62 * np.exp(-((x - thr) / 1.0) ** 2)
    left_min = te[x < thr].min()
    mid = (x > 3) & (x < 5)
    assert te[-1] < left_min and abs(x[mid][np.argmax(te[mid])] - thr) < 0.05
    bx.plot(x, tr, color=INK, label="Training error")
    bx.plot(x, te, color=INK, ls="--", label="Test error")
    bx.axvline(thr, color=G2, ls=":", lw=1)
    bx.text(thr + 0.15, 1.0, "interpolation\nthreshold", fontsize=6.5, color=G1, va="top")
    bx.text(1.9, 1.0, "classical\nregime", fontsize=6.5, ha="center", va="top")
    bx.text(7.6, 0.62, "modern, over-\nparameterised\nregime", fontsize=6.5, ha="center", va="top")
    bx.set_xlabel("Model size (parameters)", fontsize=7.6, labelpad=2)
    bx.set_ylabel("Error", fontsize=7.6, labelpad=2)
    bx.set_xticks([])
    bx.set_yticks([])
    bx.set_ylim(-0.02, 1.05)
    bx.set_xlim(0, 10)
    bx.legend(loc="upper right", bbox_to_anchor=(1.0, 0.86), fontsize=6.6, handlelength=1.8)
    fig.text(0.515, 0.97, "(b)", fontsize=8.2, weight="bold", va="center")
    F.save(fig, "fig-02-06")
