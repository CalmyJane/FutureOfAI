"""Figures for chapter 9, drawn from figures/specs/ in the house style."""
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


@fig("fig-09-01")
@own_glyph_ids
def f0901():
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
            transform=ax.get_yaxis_transform(), fontproperties=bold(7), ha="left", va="center")
    ax.text(-0.5, 6.85, "Lin et al. (2025), elections: gap between opposing AI advocates",
            transform=ax.get_yaxis_transform(), fontproperties=bold(7), ha="left", va="center")
    ax.text(18.6, 9.7, "Durability: 36\u201342% of the\nconversation effect remained\nafter one month (Hackenburg\net al.); slightly more than\none third after more than\na month (Lin et al., US).",
            fontsize=6.1, va="center", ha="left", linespacing=1.15,
            bbox=dict(boxstyle="round,pad=0.4,rounding_size=0.3", fc=G4, ec=G2, lw=0.5))
    fig.text(0.015, 0.012, "Dashed line at 0: average effect of campaign contact and ads in US general\nelections \u2248 0 (Kalla & Broockman 2018, 49 field experiments). Whiskers: 95% CIs.",
             fontsize=6.4, ha="left", va="bottom", color=G1, style="italic", linespacing=1.15)
    F.save(fig, "fig-09-01")


@fig("fig-09-02")
@own_glyph_ids
def f0902():
    fig, ax = canvas(2.45, ylim=(0, 56))
    names = [("Create", "Camera or\nAI tool"), ("Sign manifest", "Who, what tool,\nwhen"),
             ("Edit", "New signed\nentry added"), ("Publish and\ndisplay", "Platform shows\ncredentials"),
             ("Viewer checks", "Signature\nvalid?")]
    w, hgt, yb = 15, 13, 27
    xs = [1 + i * 19.75 for i in range(5)]
    for (t, s), x in zip(names, xs):
        box(ax, x, yb, w, hgt, "", fill="white")
        two = "\n" in t
        blabel(ax, x + w / 2, yb + hgt - (3.2 if two else 2.6), t, fs=7.4)
        label(ax, x + w / 2, yb + (2.9 if two else 3.6), s, fs=6.2, italic=True, color=G1)
    ym = yb + hgt / 2
    for a, b in zip(xs, xs[1:]):
        arrow(ax, a + w + 0.7, ym, b - 0.7, ym)
    # padlock between boxes 2 and 3, above the arrow
    px = (xs[1] + w + xs[2]) / 2
    ax.add_patch(F.FancyBboxPatch((px - 1.1, yb + hgt + 3.0), 2.2, 2.1, boxstyle="square,pad=0", fc=G2, ec=INK, lw=0.6))
    ax.add_patch(F.matplotlib.patches.Arc((px, yb + hgt + 5.1), 1.5, 2.6, theta1=0, theta2=180, color=INK, lw=0.8))
    label(ax, px, yb + hgt + 9.6, "Hash binds manifest to file", fs=6.4, italic=True)
    ax.plot([px, px], [yb + hgt + 2.8, ym + 1.0], color=G2, lw=0.5)
    # watermark tag under box 1
    ax.add_patch(F.FancyBboxPatch((xs[0] + 1.5, yb - 10), w - 3, 6, boxstyle="round,pad=0.3,rounding_size=1",
                                  fc="white", ec=INK, lw=0.7, ls=":"))
    label(ax, xs[0] + w / 2, yb - 7, "Invisible\nwatermark", fs=6.2)
    ax.plot([xs[0] + w / 2, xs[0] + w / 2], [yb - 3.6, yb - 0.4], color=G2, lw=0.5, ls=":")
    # recovery branch (dashed)
    bx = (xs[2] + w + xs[3]) / 2
    by = 3
    box(ax, xs[2] - 2, by, 16, 8, "Manifest\nstripped", fill=G4, fs=7, lw=0.7)
    arrow(ax, bx, ym - 0.4, xs[2] + 11, by + 8.8, ls="--", lw=0.8)
    box(ax, xs[3] + 0.5, by, 15, 8, "Watermark\nlookup", fill=G4, fs=7, lw=0.7)
    arrow(ax, xs[2] + 14.6, by + 4, xs[3] - 0.2, by + 4, ls="--", lw=0.8)
    arrow(ax, xs[3] + 16.2, by + 4, xs[4] + w / 2, yb - 0.6, ls="--", lw=0.8, rad=0.35)
    label(ax, xs[4] + w / 2 + 2.2, 10.5, "Recover from\ncloud", fs=6.2, italic=True, color=G1, ha="left")
    # callout
    cy = 47
    box(ax, xs[4] - 2.5, cy, w + 5, 6.2, "", fill=G4, lw=0.6, style="round,pad=0.4,rounding_size=2")
    blabel(ax, xs[4] + w / 2, cy + 4.3, "Provenance \u2260 truth", fs=7.4, italic=True)
    label(ax, xs[4] + w / 2, cy + 1.4, "Records origin, not accuracy", fs=5.9, italic=True, color=G1)
    ax.plot([xs[4] + w / 2, xs[4] + w / 2], [cy - 0.6, yb + hgt + 0.5], color=G2, lw=0.5)
    save(fig, "fig-09-02")


@fig("fig-09-03")
@own_glyph_ids
def f0903():
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
    F.save(fig, "fig-09-03")
