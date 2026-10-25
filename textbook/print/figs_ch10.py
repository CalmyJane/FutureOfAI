"""Figures for chapter 10, drawn from figures/specs/ in the house style."""
import math

import numpy as np

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


@fig("fig-10-01")
def f1001():
    fig = F.figure(3.6)
    # Panel A: Turkey RCT, grouped bars
    ax = fig.add_axes([0.14, 0.57, 0.84, 0.36])
    groups = ["Assisted practice", "Unassisted exam"]
    base = [48, -17]
    tutor = [127, -1.2]
    x = np.arange(2)
    w = 0.32
    ax.bar(x - w / 2 - 0.01, base, w, color=G1, edgecolor=INK, lw=0.6, label="GPT Base")
    ax.bar(x + w / 2 + 0.01, tutor, w, color="white", edgecolor=INK, lw=0.6, hatch="////", label="GPT Tutor")
    ax.axhline(0, color=INK, lw=0.9)
    labs_b = ["+48%", "−17%"]
    labs_t = ["+127%", "≈0, n.s."]
    for i in range(2):
        yb = base[i]
        if yb > 0:
            ax.text(x[i] - w / 2 - 0.01, yb + 4, labs_b[i], ha="center", va="bottom", fontsize=7.5)
        else:
            ax.text(x[i] - w / 2 - 0.01, yb / 2, labs_b[i], ha="center", va="center", fontsize=7.5, color="white")
        yt = tutor[i]
        ax.text(x[i] + w / 2 + 0.01, yt + 4 if yt > 0 else 4, labs_t[i], ha="center", va="bottom", fontsize=7.5)
    ax.set_xlim(-0.6, 1.6)
    ax.set_ylim(-30, 145)
    ax.set_yticks([-20, 0, 20, 40, 60, 80, 100, 120, 140])
    ax.set_xticks(x)
    ax.set_xticklabels(groups, fontsize=8)
    ax.tick_params(axis="x", length=0, pad=4)
    ax.tick_params(axis="y", labelsize=7.5)
    ax.set_ylabel("Change vs control group (%)", fontsize=7.5)
    ax.legend(loc="upper right", fontsize=7.5, handlelength=1.4, handleheight=0.9)
    ax.set_title("A. Turkey, high-school mathematics (randomised trial)", fontsize=8.5, loc="left", x=-0.12, pad=6)
    fig.text(0.14, 0.485, "Nearly 1,000 students, grades 9–11, autumn 2023; classes assigned to arms, students randomly assigned to classes.",
             fontsize=6.8, style="italic", color=G1)

    # Panel B: effect sizes in two other RCTs
    bx = fig.add_axes([0.42, 0.15, 0.52, 0.25])
    rows = [("Nigeria: overall assessment\n(6 weeks, after school)", 0.31),
            ("Nigeria: English only", 0.23),
            ("Harvard physics: AI tutor\nvs active learning", 0.63)]
    y = np.arange(len(rows))[::-1]
    bx.barh(y, [v for _, v in rows], 0.55, color=G3, edgecolor=INK, lw=0.6)
    for yi, (_, v) in zip(y, rows):
        bx.text(v + 0.015, yi, f"{v:.2f}", va="center", fontsize=7.5)
    bx.set_yticks(y)
    bx.set_yticklabels([r for r, _ in rows], fontsize=7.2, linespacing=1.05)
    bx.tick_params(axis="y", length=0, pad=4)
    bx.tick_params(axis="x", labelsize=7.5)
    bx.set_xlim(0, 0.8)
    bx.set_xticks([0, 0.2, 0.4, 0.6, 0.8])
    bx.set_ylim(-0.6, 2.6)
    bx.set_xlabel("Effect size (standard deviations)", fontsize=7.5)
    fig.text(0.02, 0.425, "B. Effect sizes in two other trials (three estimates)", fontsize=8.5)
    fig.text(0.42, 0.0, "Different tests and settings: effect sizes are not directly comparable.",
             fontsize=6.8, style="italic", color=G1)
    F.save(fig, "fig-10-01")


@fig("fig-10-02")
def f1002():
    fig = F.figure(2.6)
    ax = fig.add_axes([0.12, 0.16, 0.86, 0.8])
    years = list(range(2015, 2026))
    n = [6, 18, 27, 65, 80, 114, 129, 162, 226, 235, 335]
    ax.bar(years, n, 0.65, color=G2, edgecolor=INK, lw=0.5)
    for yr, v in zip(years, n):
        ax.text(yr, v + 5, str(v), ha="center", va="bottom", fontsize=6.8)
    ax.set_xlim(2014.4, 2025.6)
    ax.set_ylim(0, 362)
    ax.set_xticks(years)
    ax.set_xticklabels([str(y) for y in years], fontsize=7.2)
    ax.tick_params(axis="x", length=0)
    ax.tick_params(axis="y", labelsize=7.5)
    ax.set_yticks(range(0, 351, 50))
    ax.set_xlabel("Year of FDA decision", fontsize=8)
    ax.set_ylabel("Devices authorised (number)", fontsize=8)
    ax.text(2014.9, 345, "Total listed (1995–June 2026): 1,614\n510(k) clearances: 1,553 (96%)\nradiology 1,230 (76%)\ncardiovascular 154; neurology 73",
            fontsize=7, va="top", ha="left", linespacing=1.3,
            bbox=dict(boxstyle="square,pad=0.5", fc="white", ec=G2, lw=0.5))
    F.save(fig, "fig-10-02")


@fig("fig-10-03")
def f1003():
    fig, ax = canvas(2.7, ylim=(0, 60))
    stages = ["Intake and\nhistory", "Tests and\nimaging", "Diagnosis", "Treatment\ndecision", "Documen-\ntation", "Follow-up"]
    tools = ["Patient-facing\nchatbot", "Image triage,\nscreening", "Diagnostic\nsuggestions", "Risk alerts", "Ambient\nscribe", "Reminders,\nmonitoring"]
    evid = ["Conversation\nsafety study", "Screening\nRCT", "Clinician-\nwith-AI trial", "External valid-\nation + impact\ntrial", "Time, accuracy\nand safety\naudit", "Outcome\nstudy"]
    x0, step, w = 14.0, 14.7, 11.2
    ys, yt, ye = 38, 20, 6
    hs, ht = 9, 8
    for i in range(6):
        cx = x0 + i * step + w / 2
        box(ax, x0 + i * step, ys, w, hs, stages[i], fill=G4, fs=6.8)
        box(ax, x0 + i * step - 0.2, yt, w + 0.4, ht, tools[i], fill="white", fs=6.4,
            style="square,pad=0.3")
        ax.plot([cx, cx], [ys - 0.6, yt + ht + 0.5], color=G1, lw=0.6, ls=(0, (2, 1.6)))
        label(ax, cx, ye, evid[i], fs=6.2, italic=True, color=G1)
        if i < 5:
            a = arrow(ax, x0 + i * step + w + 0.45, ys + hs / 2, x0 + (i + 1) * step - 0.45, ys + hs / 2, lw=0.8, ms=6)
            a.shrinkA = a.shrinkB = 0
    for y, t in ((ys + hs / 2, "Care stage"), (yt + ht / 2, "AI tool"), (ye, "Evidence\nneeded")):
        label(ax, 0.5, y, t, fs=7, ha="left", weight="bold")
    # bracket over row 1
    xa, xb = x0 - 0.4, x0 + 5 * step + w + 0.4
    yb = ys + hs + 2.6
    ax.plot([xa, xa, xb, xb], [yb - 1.4, yb, yb, yb - 1.4], color=INK, lw=0.6)
    label(ax, (xa + xb) / 2, yb + 2.4, "Clinician remains accountable", fs=7, italic=True)
    save(fig, "fig-10-03")
