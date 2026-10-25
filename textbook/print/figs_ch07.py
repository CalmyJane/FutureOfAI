"""Figures for chapter 7, drawn from figures/specs/ in the house style."""
import math

import numpy as np

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


@fig("fig-07-01")
def f0701():
    fig, ax = canvas(3.75, ylim=(0, 86))
    x0, w = 10, 55
    h, gap, yb = 13.0, 2.2, 2.0
    bands = [
        ("Chip design", "Nvidia, AMD, Google (TPU), Huawei", False),
        ("Chip fabrication", "TSMC, Samsung", True),
        ("Memory & packaging", "SK Hynix, Samsung, Micron (HBM);\nTSMC (CoWoS), ASE, Amkor (packaging)", True),
        ("Cloud & data centres", "Hyperscalers (e.g. Google, Amazon,\nMicrosoft, Meta); neo-clouds", False),
        (None, None, False),
    ]

    def choke_mark(x, y):
        node(ax, x, y, 1.8, fill=INK)
        ax.text(x, y - 0.1, "!", ha="center", va="center", fontsize=6.8, color="white", weight="bold")

    ys = []
    for i, (name, ex, choke) in enumerate(bands):
        y = yb + i * (h + gap)
        ys.append(y)
        if name is None:
            continue
        box(ax, x0, y, w, h, fill=G4 if not choke else "white", lw=1.8 if choke else 0.7,
            style="round,pad=0,rounding_size=1")
        label(ax, x0 + 2, y + h - 3.0, name, fs=8, ha="left", weight="bold")
        label(ax, x0 + 2, y + h - 5.4, ex, fs=6.2, ha="left", color=G1, va="top")
        if choke:
            choke_mark(x0 + w - 3.2, y + h - 3.0)
    # top band: models & applications, split in two halves
    y = ys[4]
    box(ax, x0, y, w, h, fill=G4, lw=0.7, style="round,pad=0,rounding_size=1")
    label(ax, x0 + 2, y + h / 2, "Models &\napplications", fs=8, ha="left", weight="bold")
    for k, (t, s) in enumerate((("Closed-weight", "API access"), ("Open-weight", "downloadable"))):
        bx = x0 + 20 + k * 17.5
        box(ax, bx, y + 1.5, 16, h - 3.0, fill="white", lw=0.6, style="round,pad=0,rounding_size=0.8")
        label(ax, bx + 8, y + h / 2 + 1.4, t, fs=6.8)
        label(ax, bx + 8, y + h / 2 - 1.8, s, fs=6.0, color=G1, italic=True)
    # left arrow: each layer supplies the one above
    arrow(ax, 5.0, yb, 5.0, ys[4] + h, lw=0.8)
    label(ax, 2.4, (yb + ys[4] + h) / 2, "each layer supplies the one above", fs=6.4, color=G1, rot=90)
    # side inputs on the right
    sx, sw = 72, 26
    sides = [
        (0, "Design software (EDA)", "Synopsys, Cadence,\nSiemens EDA", True),
        (1, "Chip-making tools", "ASML (sole EUV maker);\nZeiss (ASML’s optics)", True),
        (3, "Energy & grid", "electricity + water", False),
    ]
    for i, name, ex, choke in sides:
        y = ys[i]
        box(ax, sx, y + 0.8, sw, h - 1.6, fill="white", lw=1.8 if choke else 0.7,
            style="round,pad=0,rounding_size=1")
        label(ax, sx + 1.6, y + h - 3.2, name, fs=6.8, ha="left", weight="bold")
        label(ax, sx + 1.6, y + h - 5.4, ex, fs=5.9, ha="left", color=G1, va="top")
        if choke:
            choke_mark(sx + sw - 2.6, y + 2.8)
        arrow(ax, sx - 0.2, y + h / 2, x0 + w + 0.3, y + h / 2, lw=0.8)
    # legend
    choke_mark(sx + 2.0, 82.0)
    label(ax, sx + 4.6, 82.0, "chokepoint: one or\nvery few suppliers", fs=6.2, ha="left", italic=True)
    save(fig, "fig-07-01")


def _yr(y, m, d=1):
    return y + (m - 1) / 12 + (d - 1) / 365


@fig("fig-07-02")
def f0702():
    fig, ax = canvas(3.55, ylim=(-6, 74))
    t0, t1, xa, xb = 2022.62, 2026.72, 3.0, 88.0

    def X(t):
        return xa + (t - t0) / (t1 - t0) * (xb - xa)

    ay = 37
    ax.plot([X(t0), X(t1)], [ay, ay], color=INK, lw=0.8)
    for yr in (2023, 2024, 2025, 2026):
        ax.plot([X(yr)] * 2, [ay - 0.8, ay + 0.8], color=INK, lw=0.6)
        label(ax, X(min(yr + 0.5, 2026.38)), ay + 1.9, str(yr), fs=6.3, color=G2)
    # (date, label, note, kind, side(+1 above/-1 below), level, align)
    ev = [
        (_yr(2022, 10, 7), "7 Oct 2022", "Advanced chip controls", "licences for advanced AI\nchips and tools to China", "t", 1, 1, "l"),
        (_yr(2023, 10, 17), "17 Oct 2023", "Thresholds revised", "adds performance density;\nA800/H800 covered", "t", -1, 1, "r"),
        (_yr(2024, 12, 2), "2 Dec 2024", "HBM and tools", "controls on high-bandwidth\nmemory, more equipment", "t", 1, 1, "r"),
        (_yr(2025, 1, 13), "13 Jan 2025", "AI Diffusion Framework", "global tiered licensing; closed-\nweight model controls", "t", -1, 1, "r"),
        (_yr(2025, 4, 9), "9 Apr 2025", "H20 licence required", "Nvidia told licence\nneeded for China", "t", 1, 2, "r"),
        (_yr(2025, 5, 13), "13 May 2025", "Rescission announced", "diffusion rule not enforced;\nreplacement promised", "o", -1, 2, "r"),
        (_yr(2025, 9, 29), "29 Sep / 10 Nov 2025", "Affiliates rule, then stayed", "50%-owned affiliates of listed\nentities covered; stayed for a year", "t", 1, 2, "l"),
        (_yr(2026, 1, 15), "15 Jan 2026", "H200 case-by-case", "China review moved from\ndenial to case-by-case", "o", 1, 1, "l"),
        (_yr(2026, 7, 10), "10 Jul 2026", "UAE licence-free access", "partner access to advanced\ncomputing items", "d", -1, 1, "r"),
    ]
    lev = {1: 6.0, 2: 21.5}

    def mark(x, kind):
        if kind == "t":
            ax.plot([x], [ay], marker="s", ms=4.6, mfc=INK, mec=INK, zorder=3)
        elif kind == "o":
            ax.plot([x], [ay], marker="o", ms=5, mfc="white", mec=INK, mew=0.9, zorder=3)
        else:
            ax.plot([x], [ay], marker="D", ms=4.4, mfc=G2, mec=INK, mew=0.8, zorder=3)

    for t, date, lab, note, kind, side, level, al in ev:
        x = X(t)
        d = lev[level]
        top = ay + side * (d + 13.5)
        ax.plot([x, x], [ay + side * 1.6, top], color=G2, lw=0.5, zorder=1)
        tx = x + 1.0 if al == "l" else x - 1.0
        ha = "left" if al == "l" else "right"
        ybase = ay + side * d if side > 0 else ay - d - 13.5
        label(ax, tx, ybase + 11.6, date, fs=6.3, ha=ha, va="center", color=G1)
        label(ax, tx, ybase + 8.2, lab, fs=7.4, ha=ha, va="center", weight="bold")
        label(ax, tx, ybase + 3.0, note, fs=6.1, ha=ha, va="center", italic=True, color=G1)
        mark(x, kind)
    # suspension of the Affiliates rule (10 Nov 2025): own marker, joined to the 29 Sep stem
    xs_, xa_ = X(_yr(2025, 11, 10)), X(_yr(2025, 9, 29))
    ax.plot([xs_, xs_, xa_], [ay + 1.6, ay + 4.0, ay + 4.0], color=G2, lw=0.5, zorder=1)
    mark(xs_, "o")
    from matplotlib.lines import Line2D
    hs = [Line2D([], [], ls="", marker="s", ms=4.6, mfc=INK, mec=INK, label="tightening"),
          Line2D([], [], ls="", marker="o", ms=5, mfc="white", mec=INK, label="loosening / withdrawal"),
          Line2D([], [], ls="", marker="D", ms=4.4, mfc=G2, mec=INK, label="partner access")]
    ax.legend(handles=hs, loc="lower center", bbox_to_anchor=(0.5, 0.03), ncol=3, fontsize=7,
              handletextpad=0.3, columnspacing=1.6)
    label(ax, 50, -4.0, "Effective dates, except 17 Oct 2023 and 13 May 2025 (announcements) and 9 Apr 2025 (notice to Nvidia).",
          fs=6.0, color=G1, italic=True)
    save(fig, "fig-07-02")


def _bars_base(ax, ymax, step):
    ax.set_ylim(0, ymax)
    ax.set_yticks(range(0, ymax + 1, step))
    ax.set_yticklabels([f"{v:,}" for v in range(0, ymax + 1, step)], fontsize=7.5)
    ax.yaxis.grid(True, color=G3, lw=0.5)
    ax.set_axisbelow(True)
    ax.tick_params(axis="x", length=0)
    ax.set_ylabel("Electricity consumption (TWh)", fontsize=8)


@fig("fig-07-03")
def f0703():
    fig = F.figure(2.9)
    ax = fig.add_axes([0.12, 0.215, 0.86, 0.75])
    cats = ["2023", "2024", "2025", "Headwinds", "High\nEfficiency", "Base\nCase", "Lift-Off"]
    vals = [360, 416, 485, 833, 868, 945, 1008]
    xs = [0, 1, 2, 3.8, 4.8, 5.8, 6.8]
    for i, (x, v) in enumerate(zip(xs, vals)):
        if i < 3:
            ax.bar(x, v, 0.66, color=G1, edgecolor=G1, lw=0.6)
        else:
            base = i == 5
            ax.bar(x, v, 0.66, color=G4, edgecolor=INK, lw=1.4 if base else 0.6, hatch="////")
        ax.text(x, v + 18, f"{v:,}", ha="center", va="bottom", fontsize=7.2, weight="bold" if i == 5 else "normal")
    ax.axvline(2.9, color=G2, lw=0.7, ls=(0, (3, 2)))
    ax.text(3.0, 1150, "Projections", fontsize=7, ha="left", va="center", style="italic", color=G1)
    ax.text(2.8, 1150, "Estimates", fontsize=7, ha="right", va="center", style="italic", color=G1)
    ax.set_xticks(xs)
    ax.set_xticklabels(cats, fontsize=7.3, linespacing=1.0)
    ax.text(5.3, -228, "2030 (four IEA cases)", ha="center", va="center", fontsize=7.3, color=G1)
    ax.plot([3.45, 7.15], [-183, -183], color=G2, lw=0.6, clip_on=False)
    _bars_base(ax, 1200, 200)
    ax.set_xlim(-0.6, 7.4)
    fig.text(0.12, 0.008, "The IEA text rounds the 2030 Base Case to ‘about 950 TWh’. 2023–2025 are estimates.",
             fontsize=6.4, color=G1, ha="left", style="italic")
    F.save(fig, "fig-07-03")


@fig("fig-07-04")
def f0704():
    fig = F.figure(2.7)
    ax = fig.add_axes([0.12, 0.17, 0.86, 0.79])
    regs = ["United States", "China", "Europe", "Rest of world"]
    v24 = [183, 102, 68, 63]
    v30 = [426, 277, 114, 128]
    xs = np.arange(4)
    bw = 0.36
    for x, a, b in zip(xs, v24, v30):
        ax.bar(x - bw / 2 - 0.01, a, bw, color=G1, edgecolor=G1, lw=0.6)
        ax.bar(x + bw / 2 + 0.01, b, bw, color=G4, edgecolor=INK, lw=0.6, hatch="////")
        ax.text(x - bw / 2 - 0.01, a + 8, str(a), ha="center", va="bottom", fontsize=7.2)
        ax.text(x + bw / 2 + 0.01, b + 8, str(b), ha="center", va="bottom", fontsize=7.2)
    ax.set_xticks(xs)
    ax.set_xticklabels(regs, fontsize=7.8)
    _bars_base(ax, 500, 100)
    ax.set_xlim(-0.55, 3.55)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(fc=G1, ec=G1, lw=0.6, label="2024"),
                       Patch(fc=G4, ec=INK, lw=0.6, hatch="////", label="2030 (Base Case)")],
              loc="upper right", bbox_to_anchor=(1.0, 1.0), fontsize=7.3, handlelength=1.6)
    ax.text(3.5, 392, "World total:\n416 TWh (2024)\n945 TWh (2030)", ha="right", va="top", fontsize=6.8,
            color=G1, style="italic")
    fig.text(0.12, 0.012, "Rest of world = world minus the three named regions; IEA totals may not sum exactly because of rounding.",
             fontsize=6.0, color=G1, ha="left", style="italic")
    F.save(fig, "fig-07-04")
