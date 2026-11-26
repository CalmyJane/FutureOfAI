"""House style for all figures: greyscale, EB Garamond, thin lines, consistent boxes and arrows."""
import os

import matplotlib

matplotlib.use("svg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch, Circle

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
OUT = os.path.join(os.path.dirname(HERE), "figures", "svg")
for f in os.listdir(FONTS):
    if f.endswith(".ttf"):
        font_manager.fontManager.addfont(os.path.join(FONTS, f))

INK = "#1a1a1a"
G1 = "#4d4d4d"   # dark grey
G2 = "#8c8c8c"   # mid grey
G3 = "#c8c8c8"   # light grey
G4 = "#ececec"   # fill
SERIES = [INK, G2, "#5f5f5f", G3]

plt.rcParams.update({
    "font.family": "EB Garamond",
    "font.size": 9,
    "axes.edgecolor": INK,
    "axes.linewidth": 0.6,
    "axes.labelcolor": INK,
    "axes.titlesize": 9.5,
    "xtick.color": INK,
    "ytick.color": INK,
    "xtick.major.width": 0.6,
    "ytick.major.width": 0.6,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "legend.frameon": False,
    "svg.fonttype": "path",
    "lines.linewidth": 1.4,
    "axes.prop_cycle": matplotlib.cycler(color=SERIES),  # no stray RGB defaults in a greyscale book
    "mathtext.fontset": "custom",
    "mathtext.rm": "EB Garamond",
    "mathtext.it": "EB Garamond:italic",
    "mathtext.bf": "EB Garamond:bold",
})

# A5 text width is about 113 mm = 4.45 in
WIDTH = 4.45


def figure(height=2.4, width=WIDTH):
    fig = plt.figure(figsize=(width, height))
    return fig


def canvas(height=2.4, width=WIDTH, xlim=(0, 100), ylim=(0, 50)):
    """A blank diagram canvas in arbitrary units (x 0..100)."""
    fig = plt.figure(figsize=(width, height))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.axis("off")
    return fig, ax


def box(ax, x, y, w, h, text="", fill=G4, lw=0.8, fs=8.5, weight="normal", style="round,pad=0.4,rounding_size=1.2", color=INK, italic=False):
    p = FancyBboxPatch((x, y), w, h, boxstyle=style, linewidth=lw, edgecolor=color, facecolor=fill)
    ax.add_patch(p)
    if text:
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, weight=weight,
                color=INK, style="italic" if italic else "normal", linespacing=1.15)
    return p


def arrow(ax, x0, y0, x1, y1, lw=0.9, color=INK, style="-|>", rad=0.0, ls="-", ms=8):
    a = FancyArrowPatch((x0, y0), (x1, y1), arrowstyle=style, mutation_scale=ms, linewidth=lw,
                        color=color, connectionstyle=f"arc3,rad={rad}", linestyle=ls, shrinkA=2, shrinkB=2)
    ax.add_patch(a)
    return a


def label(ax, x, y, text, fs=8, ha="center", va="center", color=INK, italic=False, weight="normal", rot=0):
    ax.text(x, y, text, fontsize=fs, ha=ha, va=va, color=color, style="italic" if italic else "normal",
            weight=weight, rotation=rot, linespacing=1.15)


def node(ax, x, y, r=2.2, fill="white", lw=0.9, text="", fs=7):
    c = Circle((x, y), r, facecolor=fill, edgecolor=INK, linewidth=lw)
    ax.add_patch(c)
    if text:
        ax.text(x, y, text, ha="center", va="center", fontsize=fs)
    return c


def save(fig, name):
    os.makedirs(OUT, exist_ok=True)
    fig.savefig(os.path.join(OUT, name + ".svg"), bbox_inches="tight", pad_inches=0.04, transparent=True)
    plt.close(fig)


FIGS = {}


def fig(name):
    """Register a figure-drawing function under its figure id."""
    def deco(fn):
        FIGS[name] = fn
        return fn
    return deco
