"""Figures for chapter 12, drawn from figures/specs/ in the house style."""
import math

import numpy as np

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


# canvas scale: inches per data unit (x 0..100 over WIDTH)
def _sx():
    return F.WIDTH / 100


@fig("fig-12-01")
def f1201():
    H, YT = 2.85, 60
    fig, ax = canvas(H, ylim=(-3.5, YT))
    k = ((H * YT / (YT + 3.5)) / YT) / _sx()          # x units per y unit, so holes are drawn round-ish
    y0, y1 = 22, 55               # slice bottom / top
    ym = (y0 + y1) / 2
    sw, shear = 5.6, 2.6          # slice width and top offset (tilt)
    xs = [22 + i * 12.4 for i in range(6)]
    ys, yp = 47, 35               # solid (stopped) path; dashed (harm) path

    def cx(x, y):                 # centre line of the tilted slice at height y
        return x + shear * (y - ym) / (y1 - y0)

    extra = [[(28, 1.6)], [(52, 1.3), (27, 1.9)], [(46, 2.0), (26, 1.3)],
             [(51, 1.5), (27, 1.8)], [(47, 1.4), (26, 1.6)], [(51, 1.6), (27, 1.4)]]
    for i, x in enumerate(xs):
        poly = [(x - sw / 2 - shear / 2, y0), (x + sw / 2 - shear / 2, y0),
                (x + sw / 2 + shear / 2, y1), (x - sw / 2 + shear / 2, y1)]
        sl = F.matplotlib.patches.Polygon(poly, closed=True, fc=G3, ec=INK, lw=0.6, joinstyle="round", zorder=2)
        if i == 2:                # interpretability: research stage, not yet a deployable layer
            sl.set_linestyle((0, (3, 2)))
            sl.set_facecolor(G4)
        ax.add_patch(sl)
        holes = [(yp, 2.3)] + extra[i] + ([(ys, 2.0)] if i == 0 else [])
        for hy, r in holes:
            ax.add_patch(F.matplotlib.patches.Ellipse((cx(x, hy), hy), r * 2 * k, r * 2,
                                                       fc="white", ec=G1, lw=0.4, zorder=3))
    labels = ["Alignment\ntraining", "Pre-release\nevaluations", "Interpretability\naudits",
              "Reasoning\nmonitoring", "Deployment\nsafeguards", "Governance\nframeworks"]
    tags = ["12.1: RLHF,\nconstitutions", "12.3: red-teaming,\ncapability tests", "12.4: research\nstage",
            "12.5: chain-of-\nthought monitors", "12.6: control\nprotocols,\ncontainment",
            "12.7: thresholds,\nexternal testing"]
    for x, l, t in zip(xs, labels, tags):
        label(ax, x, 20.6, l, fs=6.6, va="top")
        label(ax, x, 13.4, t, fs=5.8, color=G1, italic=True, va="top")
    # hazard and harm
    box(ax, 1.2, 37.5, 9, 6, "Hazard", fill=G4, fs=7.5)
    box(ax, 89.6, yp - 3, 9, 6, "Harm", fill=G1, fs=7.5)
    ax.texts[-1].set_color("white")
    # dashed path through the aligned holes, all the way to Harm
    ax.plot([10.9, 14, 89.2 - 1.8], [40.5, yp, yp], color=INK, lw=0.9, ls=(0, (3.5, 2)), zorder=4)
    arrow(ax, 85, yp, 89.4, yp, lw=0.9)
    # solid path: through a hole in slice 1, stopped by slice 2
    xstop = cx(xs[1], ys) - sw / 2 - 0.2
    ax.plot([10.9, 14, xstop], [40.5, ys, ys], color=INK, lw=0.9, zorder=4)
    ax.plot([xstop, xstop], [ys - 2.2, ys + 2.2], color=INK, lw=1.5, zorder=4, solid_capstyle="butt")
    gx = (cx(xs[0], y1) + cx(xs[1], y1)) / 2
    label(ax, gx, y1 + 2.6, "Stopped", fs=6.4, italic=True)
    ax.plot([gx, xstop - 0.3], [y1 + 0.9, ys + 2.6], color=G2, lw=0.5, zorder=4)
    label(ax, 50, 0.6, "No single layer is complete; layering helps most when layers fail independently.\n"
          "A model that recognises tests, or monitors from the same model family, can line up the holes (11.5, 12.3).",
          fs=6.2, italic=True)
    save(fig, "fig-12-01")


@fig("fig-12-02")
def f1202():
    H, YT = 3.1, 66
    fig, ax = canvas(H, ylim=(0, YT))
    uy = H / YT                   # inches per y unit
    ux = _sx()                    # inches per x unit

    def dot(x, y, d_in, fill):
        ax.add_patch(F.matplotlib.patches.Ellipse((x, y), d_in / ux, d_in / uy, fc=fill, ec=INK, lw=0.6, zorder=3))

    # stage 1: input text
    box(ax, 1.5, 32.5, 15.5, 11, "", fill="white", lw=0.7)
    label(ax, 9.25, 47, "Input text", fs=6.8, weight="bold")
    label(ax, 9.25, 38, "“Driving over\nthe Golden\nGate Bridge”", fs=6.6, italic=True)
    # stage 2 and 4: neuron columns
    shades = [G1, G3, G2, "white", G2, G3]
    ncy = [52 - i * 5.6 for i in range(6)]     # 52 .. 24
    # reconstruction is close but not exact: two units differ slightly in shade
    recon = [G1, G3, G2, G4, G2, G2]
    for xc, sh in ((31, shades), (91, recon)):
        for y, c in zip(ncy, sh):
            dot(xc, y, 0.17, c)
    label(ax, 31, 60, "Model activations\n(one layer)", fs=6.8, weight="bold")
    label(ax, 91, 60, "Reconstructed\nactivations", fs=6.8, weight="bold")
    label(ax, 31, 17, "Concepts overlap\n(superposition)", fs=6.2, italic=True, color=G1)
    # stage 3: candidate features
    fx, n = 55, 20
    fy = [58 - i * 2.1 for i in range(n)]      # 58 .. 18.1
    s_in = 0.074
    on = {2: "Golden Gate Bridge", 7: "Driving / cars", 15: "San Francisco"}
    for i, y in enumerate(fy):
        ax.add_patch(F.FancyBboxPatch((fx - s_in / ux / 2, y - s_in / uy / 2), s_in / ux, s_in / uy,
                                      boxstyle="square,pad=0", fc=INK if i in on else "white", ec=INK, lw=0.5, zorder=3))
        if i in on:
            label(ax, fx + 2.6, y, on[i], fs=6.2, italic=True, ha="left")
    label(ax, fx, 63, "Candidate features (many more)", fs=6.8, weight="bold")
    label(ax, fx - 3.2, 44, "Sparse:\nfew active", fs=6.2, italic=True, color=G1, ha="right")
    # arrows
    arrow(ax, 17.5, 38, 27.5, 38, lw=0.8)
    arrow(ax, 34.5, 38, 51, 38, lw=0.8)
    label(ax, 42.5, 35.6, "Encoder", fs=6.6, italic=True)
    arrow(ax, 77, 38, 87.5, 38, lw=0.8)
    label(ax, 82.2, 35.6, "Decoder", fs=6.6, italic=True)
    # bracket under stage 3
    bl, br, by = fx - 3.5, fx + 3.5, 15.6
    ax.plot([bl, bl, br, br], [by + 1.2, by, by, by + 1.2], color=INK, lw=0.6)
    ax.plot([fx, fx], [by, by - 1.0], color=INK, lw=0.6)
    label(ax, fx, 11.4, "Labelled by inspecting\ntop-activating examples", fs=6.2, italic=True)
    # reconstruction error: dashed comparison between stage 2 and stage 4
    ye = 5.6
    ax.plot([31, 31, 91, 91], [13.6, ye, ye, 22.2], color=G1, lw=0.6, ls=(0, (3, 2)))
    label(ax, 61, ye - 3.2, "Reconstruction error = unexplained part", fs=6.2, italic=True, color=G1)
    save(fig, "fig-12-02")


@fig("fig-12-03")
def f1203():
    with F.plt.rc_context({"hatch.linewidth": 0.4, "hatch.color": G2}):
        _f1203()


def _f1203():
    # Baker et al. (2025), Table 1: recall against a regex detector over all of training
    groups = ["exit(0) hack", "SkipTest hack", "Both hacks"]
    act, cot = [40, 80, 60], [93, 97, 95]
    fig = F.figure(2.7)
    ax = fig.add_axes([0.11, 0.2, 0.87, 0.74])
    x = np.arange(len(groups))
    bw = 0.34
    xa, xc = x - bw / 2 - 0.01, x + bw / 2 + 0.01
    ax.bar(xa, act, bw, color=G3, edgecolor=INK, lw=0.5, label="Actions only")
    ax.bar(xc, cot, bw, color=G1, edgecolor=INK, lw=0.5, label="Chain of thought + actions")
    for xs_, vs in ((xa, act), (xc, cot)):
        for xi, v in zip(xs_, vs):
            ax.text(xi, v + 1.5, f"{v}%", ha="center", va="bottom", fontsize=7.3,
                    bbox=dict(fc="white", ec="none", pad=0.6))
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    ax.tick_params(axis="x", length=0)
    ax.set_xlim(-0.6, 2.6)
    ax.set_ylim(0, 118)
    ax.set_yticks(range(0, 101, 20))
    ax.spines["left"].set_bounds(0, 100)
    ax.yaxis.grid(True, color=G3, lw=0.4)
    ax.set_axisbelow(True)
    ax.set_ylabel("Recall (% of hacks detected)")
    ax.legend(loc="upper left", ncol=2, fontsize=7.3, handlelength=1.4, handleheight=1.0,
              bbox_to_anchor=(0.0, 1.04))
    fig.text(0.11, 0.015, "Approximate precision (joint): actions only 81%, chain of thought 77%.",
             fontsize=6.3, color=G1, style="italic")
    F.save(fig, "fig-12-03")
