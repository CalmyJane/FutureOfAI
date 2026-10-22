"""Figures for chapter 12, drawn from figures/specs/ in the house style."""
import functools
import math
import urllib.parse

import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib.textpath import TextToPath

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


def own_glyph_ids(fn):
    """The bundled EB Garamond weights share one PostScript name, so matplotlib's SVG glyph ids for
    bold and regular collide (bold glyphs leak into regular text). While this figure is drawn, key
    glyph ids by font file instead. Restored afterwards, so other modules are unaffected."""
    @functools.wraps(fn)
    def run(*a, **k):
        orig = TextToPath._get_glyph_repr

        def rep(self, font, glyph):
            name = F.os.path.splitext(F.os.path.basename(font.fname))[0]
            return urllib.parse.quote(f"{name}-{glyph:x}").replace("%", "_")
        TextToPath._get_glyph_repr = rep
        try:
            return fn(*a, **k)
        finally:
            TextToPath._get_glyph_repr = orig
    return run


def bold(size, italic=False):
    """Bold face loaded from its own file, so its SVG glyph ids do not collide with the regular face."""
    f = "EBGaramond-BoldItalic.ttf" if italic else "EBGaramond-Bold.ttf"
    return FontProperties(fname=F.os.path.join(F.FONTS, f), size=size)


def blabel(ax, x, y, text, fs=8, italic=False, **kw):
    kw.setdefault("ha", "center")
    kw.setdefault("va", "center")
    ax.text(x, y, text, fontproperties=bold(fs, italic), color=INK, linespacing=1.15, **kw)


# canvas scale: inches per data unit (x 0..100 over WIDTH)
def _sx():
    return F.WIDTH / 100


@fig("fig-12-01")
@own_glyph_ids
def f1201():
    H, YT = 2.7, 60
    fig, ax = canvas(H, ylim=(0, YT))
    k = (H / YT) / _sx()          # x units per y unit, so holes are drawn round-ish
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
        ax.add_patch(F.matplotlib.patches.Polygon(poly, closed=True, fc=G3, ec=INK, lw=0.6, joinstyle="round", zorder=2))
        holes = [(yp, 2.3)] + extra[i] + ([(ys, 2.0)] if i == 0 else [])
        for hy, r in holes:
            ax.add_patch(F.matplotlib.patches.Ellipse((cx(x, hy), hy), r * 2 * k, r * 2,
                                                       fc="white", ec=G1, lw=0.4, zorder=3))
    labels = ["Alignment\ntraining", "Pre-release\nevaluations", "Interpretability\naudits",
              "Reasoning\nmonitoring", "Deployment\nsafeguards", "Governance\nframeworks"]
    tags = ["12.1: RLHF,\nconstitutions", "12.5: red-teaming,\ncapability tests", "12.3",
            "12.4: chain-of-\nthought monitors", "filters, access\ncontrols", "12.6: thresholds,\nexternal testing"]
    for x, l, t in zip(xs, labels, tags):
        label(ax, x, 17, l, fs=6.6)
        label(ax, x, 9.6, t, fs=5.8, color=G1, italic=True)
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
    label(ax, 50, 1.6, "No single layer is complete; layering reduces the chance that all fail together.",
          fs=6.4, italic=True)
    save(fig, "fig-12-01")


@fig("fig-12-02")
@own_glyph_ids
def f1202():
    H, YT = 3.3, 70
    fig, ax = canvas(H, ylim=(0, YT))
    uy = H / YT                   # inches per y unit
    ux = _sx()                    # inches per x unit

    def dot(x, y, d_in, fill):
        ax.add_patch(F.matplotlib.patches.Ellipse((x, y), d_in / ux, d_in / uy, fc=fill, ec=INK, lw=0.6, zorder=3))

    # stage 1: input text
    box(ax, 1.5, 35, 15.5, 11, "", fill="white", lw=0.7)
    label(ax, 9.25, 49.5, "Input text", fs=7.2, weight="normal")
    label(ax, 9.25, 40.5, "“Driving over\nthe Golden\nGate Bridge”", fs=6.6, italic=True)
    # stage 2 and 4: neuron columns
    shades = [G1, G3, G2, "white", G2, G3]
    ncy = [52 - i * 5.6 for i in range(6)]     # 52 .. 24
    for xc in (31, 91):
        for y, c in zip(ncy, shades):
            dot(xc, y, 0.17, c)
    blabel(ax, 31, 61, "Model neurons\n(one layer)", fs=6.8)
    blabel(ax, 91, 61, "Reconstructed\nactivations", fs=6.8)
    label(ax, 31, 17.5, "Concepts overlap\n(superposition)", fs=6.2, italic=True, color=G1)
    # stage 3: candidate features
    fx, n = 55, 20
    fy = [62 - i * 2.75 for i in range(n)]     # 62 .. 9.75
    s_in = 0.095
    on = {2: "Golden Gate Bridge", 7: "Driving / cars", 15: "San Francisco"}
    for i, y in enumerate(fy):
        ax.add_patch(F.FancyBboxPatch((fx - s_in / ux / 2, y - s_in / uy / 2), s_in / ux, s_in / uy,
                                      boxstyle="square,pad=0", fc=INK if i in on else "white", ec=INK, lw=0.5, zorder=3))
        if i in on:
            label(ax, fx + 2.6, y, on[i], fs=6.2, italic=True, ha="left")
    blabel(ax, fx, 68, "Candidate features (many more)", fs=6.8)
    label(ax, fx - 3.2, 44, "Sparse:\nfew active", fs=6.2, italic=True, color=G1, ha="right")
    # arrows
    arrow(ax, 17.5, 40.5, 27.5, 40.5, lw=0.8)
    arrow(ax, 34.5, 38, 51, 38, lw=0.8)
    label(ax, 42.5, 35.6, "Encoder", fs=6.6, italic=True)
    arrow(ax, 77, 38, 87.5, 38, lw=0.8)
    label(ax, 82.2, 35.6, "Decoder", fs=6.6, italic=True)
    # bracket under stage 3
    bl, br, by = fx - 3.5, fx + 3.5, 7.2
    ax.plot([bl, bl, br, br], [by + 1.2, by, by, by + 1.2], color=INK, lw=0.6)
    ax.plot([fx, fx], [by, by - 1.0], color=INK, lw=0.6)
    label(ax, fx, 3.2, "Labelled by inspecting top-activating examples", fs=6.2, italic=True)
    # reconstruction error: dashed comparison between stage 2 and stage 4
    ye = 12
    ax.plot([31, 31, 91, 91], [20.5 - 6.2, ye, ye, 20.5], color=G1, lw=0.6, ls=(0, (3, 2)))
    label(ax, 76, ye + 2.2, "Reconstruction error\n= unexplained part", fs=6.2, italic=True, color=G1)
    save(fig, "fig-12-02")
