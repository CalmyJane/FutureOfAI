"""Figures for chapter 13, drawn from figures/specs/ in the house style."""
import math

import numpy as np
from matplotlib.patches import Polygon, Wedge

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


@fig("fig-13-01")
def f1301():
    fig, ax = canvas(3.3, ylim=(0, 74))
    # pyramid: four trapezoid levels, top level darkest
    y0, xc = 3.0, 38.0
    hs = [12.0, 13.5, 13.0, 21.0]            # bottom .. top
    wb, wt = 60.0, 30.0                       # width at base and at apex
    ytop = y0 + sum(hs)

    def half(y):
        return (wb + (wt - wb) * (y - y0) / (ytop - y0)) / 2

    tiers = [  # bottom .. top: (title, examples, note, fill, text colour)
        ("Minimal risk: no new duties", "Spam filters · Video games", "", G4, INK),
        ("Transparency risk: disclosure", "Chatbots · Deepfakes ·\nAI-generated content", "Art. 50; from Aug 2026", G3, INK),
        ("High risk: strict requirements", "Hiring, credit, education ·\nProduct safety components",
         "Annex I and III; from Dec 2027 / Aug 2028", G2, INK),
        ("Unacceptable risk:\nbanned", "Social scoring ·\nUntargeted face scraping ·\nEmotion recognition\nat work or school",
         "Art. 5; since Feb 2025", G1, "white"),
    ]
    y = y0
    for (title, ex, note, fill, tc), h in zip(tiers, hs):
        a, b = half(y), half(y + h)
        ax.add_patch(Polygon([(xc - a, y), (xc + a, y), (xc + b, y + h), (xc - b, y + h)],
                             closed=True, fc=fill, ec=INK, lw=0.7))
        top = y + h - 1.2
        if title.startswith("Unacceptable"):
            ax.text(xc, top, title, ha="center", va="top", fontsize=6.8, weight="bold", color=tc, linespacing=1.05)
            ax.text(xc, top - 6.0, ex, ha="center", va="top", fontsize=5.9, color=tc, linespacing=1.05)
            ax.text(xc, y + 1.0, note, ha="center", va="bottom", fontsize=5.9, color=tc, style="italic")
        else:
            nl = ex.count("\n") + 1
            ax.text(xc, top, title, ha="center", va="top", fontsize=7.0, weight="bold", color=tc)
            ax.text(xc, top - 3.3, ex, ha="center", va="top", fontsize=6.2, color=tc, linespacing=1.05)
            if note:
                ax.text(xc, top - 3.6 - 2.9 * nl, note, ha="center", va="top", fontsize=5.9, color=tc, style="italic")
        y += h
    # obligations arrow on the far left
    arrow(ax, 4.0, y0 + 2, 4.0, ytop - 1, lw=0.9)
    label(ax, 1.6, (y0 + ytop) / 2, "Obligations increase", fs=6.8, rot=90, italic=True)
    # dashed bracket spanning all tiers
    bx = 71.0
    ax.plot([bx - 2, bx, bx, bx - 2], [y0, y0, ytop, ytop], color=INK, lw=0.7, ls=(0, (3, 2)))
    ax.plot([bx, 74.5], [(y0 + ytop) / 2] * 2, color=INK, lw=0.7, ls=(0, (3, 2)))
    # GPAI column
    cx, cw = 75.5, 24.0
    label(ax, cx + cw / 2, 69.5, "General-purpose\nAI models", fs=7.2, weight="bold")
    label(ax, cx + cw / 2, 64.0, "across all tiers", fs=6.0, italic=True, color=G1)
    # upper box
    box(ax, cx, 36.5, cw, 22.5, "", fill="white", lw=0.7, style="round,pad=0.3,rounding_size=1.0")
    ax.text(cx + cw / 2, 57.6, "GPAI models", ha="center", va="top", fontsize=7.0, weight="bold")
    ax.text(cx + cw / 2, 53.6, "Documentation\nCopyright policy\nTraining-data\nsummary",
            ha="center", va="top", fontsize=6.2, linespacing=1.1)
    ax.text(cx + cw / 2, 37.6, "Art. 53; since Aug 2025", ha="center", va="bottom", fontsize=5.9, style="italic")
    # lower box, heavier border
    box(ax, cx, 4.0, cw, 27.5, "", fill=G4, lw=1.5, style="round,pad=0.3,rounding_size=1.0")
    ax.text(cx + cw / 2, 30.0, "GPAI with\nsystemic risk", ha="center", va="top", fontsize=7.0, weight="bold",
            linespacing=1.05)
    ax.text(cx + cw / 2, 22.6, "> 10$^{25}$ FLOP\n(presumed)\nEvaluations,\nincident reports",
            ha="center", va="top", fontsize=6.2, linespacing=1.15)
    ax.text(cx + cw / 2, 5.2, "Art. 55", ha="center", va="bottom", fontsize=5.9, style="italic")
    arrow(ax, cx + cw / 2, 35.8, cx + cw / 2, 32.2, lw=0.7, ms=6)
    save(fig, "fig-13-01")


def _dot(ax, x, y, kind, r=0.85):
    if kind == "f":
        ax.add_patch(F.Circle((x, y), r, fc=INK, ec=INK, lw=0.7, zorder=4))
    elif kind == "h":
        ax.add_patch(F.Circle((x, y), r, fc="white", ec=INK, lw=0.7, zorder=4))
    else:  # half-filled: executive order
        ax.add_patch(F.Circle((x, y), r, fc="white", ec=INK, lw=0.7, zorder=4))
        ax.add_patch(Wedge((x, y), r, 90, 270, fc=INK, ec=INK, lw=0.7, zorder=5))


@fig("fig-13-02")
def f1302():
    H = 3.6
    fig, ax = canvas(H, ylim=(0, 22.47 * H))
    x0, x1 = 15.5, 98.5          # Jan 2023 .. Dec 2026 (end)

    def X(y, m):
        return x0 + ((y - 2023) * 12 + (m - 1) + 0.5) * (x1 - x0) / 48

    lanes = ["EU", "United\nStates", "China", "UK", "Inter-\nnational"]
    LH, ybase = 14.6, 8.5
    ly = {n: ybase + (len(lanes) - 1 - i) * LH + LH / 2 for i, n in enumerate(lanes)}
    for i, n in enumerate(lanes):
        yc = ly[n]
        if i % 2 == 0:
            ax.add_patch(F.FancyBboxPatch((0.5, yc - LH / 2), x1 - 0.5, LH, boxstyle="square,pad=0",
                                          fc=G4, ec="none", zorder=0))
        ax.plot([x0, x1], [yc, yc], color=G2, lw=0.5, zorder=1)
        label(ax, 1.5, yc, n, fs=7.0, weight="bold", ha="left")
    # time axis
    ya = ybase
    ax.plot([x0, x1], [ya, ya], color=INK, lw=0.6)
    for k in range(9):
        xt = x0 + k * 6 * (x1 - x0) / 48
        ax.plot([xt, xt], [ya, ya - (1.0 if k % 2 == 0 else 0.6)], color=INK, lw=0.6)
        if k % 2 == 0:
            ax.plot([xt, xt], [ya, ya + 5 * LH], color=G3, lw=0.4, ls=(0, (2, 2)), zorder=0.5)
    for k, yr in enumerate(range(2023, 2027)):
        label(ax, x0 + (k * 12 + 6) * (x1 - x0) / 48, ya - 2.4, str(yr), fs=7.0)

    # (lane, year, month, text, kind, side, ha)   kind: f filled, h hollow, e half (executive order)
    ev = [
        ("EU", 2024, 8, "AI Act\nin force", "f", "u", "center"),
        ("EU", 2025, 2, "Prohibitions\napply", "f", "d", "right"),
        ("EU", 2025, 7, "GPAI Code\npublished", "h", "u", "center"),
        ("EU", 2025, 8, "GPAI duties\napply", "f", "d", "left"),
        ("EU", 2026, 7, "Digital Omnibus\nin force", "f", "u", "center"),
        ("United\nStates", 2023, 10, "EO 14110\nsigned", "e", "u", "center"),
        ("United\nStates", 2025, 1, "EO 14110\nrevoked", "e", "u", "center"),
        ("United\nStates", 2025, 9, "California\nSB 53 signed", "f", "u", "center"),
        ("United\nStates", 2025, 12, "EO on\nstate laws", "e", "d", "center"),
        ("United\nStates", 2026, 5, "Colorado re-\nplaces AI Act", "f", "u", "center"),
        ("China", 2023, 8, "Generative\nAI measures", "f", "u", "center"),
        ("China", 2025, 9, "Labelling\nrules apply", "f", "u", "center"),
        ("China", 2026, 7, "Anthropomorphic\nAI rules", "f", "u", "center"),
        ("UK", 2023, 3, "Pro-innovation\nwhite paper", "h", "u", "left"),
        ("UK", 2025, 2, "AI Security\nInstitute", "h", "u", "center"),
        ("UK", 2026, 3, "Copyright\nreport", "h", "u", "center"),
        ("Inter-\nnational", 2023, 10, "G7 Hiroshima\nCode", "h", "u", "right"),
        ("Inter-\nnational", 2023, 11, "Bletchley\nDeclaration", "h", "d", "left"),
        ("Inter-\nnational", 2024, 5, "Seoul\ncommitments", "h", "u", "center"),
        ("Inter-\nnational", 2024, 9, "CoE treaty\nopens", "f", "d", "center"),
        ("Inter-\nnational", 2025, 2, "Paris\nstatement", "h", "u", "center"),
        ("Inter-\nnational", 2025, 8, "UN Panel and\nDialogue", "h", "d", "center"),
        ("Inter-\nnational", 2026, 2, "India Impact\nSummit", "h", "u", "center"),
    ]
    MON = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()
    for lane, yr, m, t, kind, side, ha in ev:
        x, yc = X(yr, m), ly[lane]
        _dot(ax, x, yc, kind)
        tx = {"left": x - 1.0, "right": x + 1.0}.get(ha, x)
        txt = f"{t}\n{MON[m - 1]} {yr}"
        n = t.count("\n") + 1
        if side == "u":
            ax.text(tx, yc + 1.3, f"{MON[m - 1]} {yr}", ha=ha, va="bottom", fontsize=5.9, color=G1,
                    style="italic", zorder=6)
            ax.text(tx, yc + 3.6, t, ha=ha, va="bottom", fontsize=5.9, linespacing=1.0, zorder=6)
        else:
            ax.text(tx, yc - 1.3, t, ha=ha, va="top", fontsize=5.9, linespacing=1.0, zorder=6)
            ax.text(tx, yc - 1.3 - 2.3 * n - 0.2, f"{MON[m - 1]} {yr}", ha=ha, va="top", fontsize=5.9,
                    color=G1, style="italic", zorder=6)
    # legend
    lyg = 1.6
    items = [("f", "binding law or regulation"), ("e", "executive order"), ("h", "non-binding")]
    lx = 18
    for kind, t in items:
        _dot(ax, lx, lyg, kind)
        label(ax, lx + 1.8, lyg, t, fs=6.4, ha="left")
        lx += 27
    save(fig, "fig-13-02")
