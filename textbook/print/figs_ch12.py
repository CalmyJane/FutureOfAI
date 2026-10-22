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
    H, YT = 2.75, 60
    fig, ax = canvas(H, ylim=(0, YT))
    k = (H / YT) / _sx()          # x units per y unit, for true-proportion holes
    y0, y1 = 20, 50               # slice bottom / top
    ym = (y0 + y1) / 2
    sw, shear = 4.2, 2.4          # slice width and top offset (tilt)
    xs = [21 + i * 12.6 for i in range(6)]
    yp, ys = 39, 28               # dashed (harm) path; solid (stopped) path

    def cx(x, y):                 # centre line of tilted slice at height y
        return x + shear * (y - ym) / (y1 - y0)

    extra = [[(46, 1.5), (24, 1.1)], [(44, 1.3), (33, 1.0), (23, 1.2)], [(25, 1.4), (46, 1.0)],
             [(32, 1.2), (24, 1.0)], [(46, 1.3), (29, 1.1), (23, 0.9)], [(31, 1.4), (45, 1.0)]]
    for i, x in enumerate(xs):
        poly = [(x - sw / 2 - shear / 2, y0), (x + sw / 2 - shear / 2, y0), (x + sw / 2 + shear / 2, y1), (x - sw / 2 + shear / 2, y1)]
        ax.add_patch(F.matplotlib.patches.Polygon(poly, closed=True, fc=G3, ec=INK, lw=0.6, joinstyle="round", zorder=2))
        holes = [(yp, 1.8)] + extra[i] + ([(ys, 1.6)] if i == 0 else [])
        for hy, r in holes:
            ax.add_patch(F.matplotlib.patches.Ellipse((cx(x, hy), hy), r * 2 * k * 0.95, r * 2, angle=0,
                                                       fc="white", ec=G1, lw=0.4, zorder=3))
    labels = ["Alignment\ntraining", "Pre-release\nevaluations", "Interpretability\naudits",
              "Reasoning\nmonitoring", "Deployment\nsafeguards", "Governance\nframeworks"]
    tags = ["12.1: RLHF,\nconstitutions", "12.5: red-teaming,\ncapability tests", "12.3",
            "12.4: chain-of-\nthought monitors", "filters, access\ncontrols", "12.6: thresholds,\nexternal testing"]
    for x, l, t in zip(xs, labels, tags):
        label(ax, x, 14.5, l, fs=6.6, va="center")
        label(ax, x, 6.5, t, fs=5.8, color=G1, italic=True, va="center")
    # hazard and harm
    box(ax, 1.5, 30.5, 9.5, 7, "Hazard", fill=G4, fs=7.5)
    box(ax, 89, 35.5, 9.5, 7, "Harm", fill=G1, fs=7.5, color=INK)
    ax.texts[-1].set_color("white")
    # dashed path through aligned holes
    ax.annotate("", xy=(88.6, yp), xytext=(11.4, 36.5), zorder=4,
                arrowprops=dict(arrowstyle="-|>", mutation_scale=8, lw=0.9, ls="--", color=INK,
                                shrinkA=0, shrinkB=0, connectionstyle="arc3,rad=0"))
    # solid path: through slice 1, stopped at slice 2
    xstop = cx(xs[1], ys) - sw / 2 - 0.15
    ax.plot([11.4, xstop], [31.5, ys], color=INK, lw=0.9, zorder=4, solid_capstyle="butt")
    ax.plot([xstop, xstop], [ys - 1.8, ys + 1.8], color=INK, lw=1.4, zorder=4)
    label(ax, xstop + 0.6, ys - 4.6, "Stopped", fs=6.4, italic=True, ha="left")
    label(ax, 50, 56.5, "Harm gets through only when the holes in every layer line up", fs=6.6, italic=True, color=G1)
    label(ax, 50, 1.2, "No single layer is complete; layering reduces the chance that all fail together.",
          fs=6.4, italic=True)
    save(fig, "fig-12-01")
