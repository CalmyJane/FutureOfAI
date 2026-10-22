"""Figures for chapter 5, drawn from figures/specs/ in the house style."""
import math

import numpy as np

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


@fig("fig-05-01")
def f0501():
    fig, ax = canvas(2.9, ylim=(0, 64))
    cx, cy = 50, 30
    pos = {"Perceive": (cx - 16, cy + 10), "Plan": (cx + 16, cy + 10), "Act": (cx + 16, cy - 10), "Observe": (cx - 16, cy - 10)}
    sub = {"Perceive": "read current state", "Plan": "model chooses step", "Act": "call a tool", "Observe": "read tool output"}
    for k, (x, y) in pos.items():
        box(ax, x - 9, y - 4, 18, 8, "", fill="white")
        label(ax, x, y + 1.2, k, fs=8.5, weight="bold")
        label(ax, x, y - 2, sub[k], fs=6, color=G1, italic=True)
    arrow(ax, cx - 6.5, cy + 10, cx + 6.5, cy + 10)
    arrow(ax, cx + 16, cy + 5.6, cx + 16, cy - 5.6)
    arrow(ax, cx + 6.5, cy - 10, cx - 6.5, cy - 10)
    arrow(ax, cx - 16, cy - 5.6, cx - 16, cy + 5.6)
    box(ax, cx - 7, cy - 2.6, 14, 5.2, "Language\nmodel", fill=G4, fs=6.8)
    ax.plot([cx + 7.5, cx + 9], [cy + 2, cy + 6], color=G2, lw=0.6)
    box(ax, 4, cy + 6, 16, 8, "Goal from\nuser", fill=G4, fs=7.5)
    arrow(ax, 20.5, cy + 10, cx - 25.5, cy + 10)
    box(ax, cx + 2, 51, 34, 10, "", fill=G4)
    label(ax, cx + 19, 58.5, "Tools", fs=8, weight="bold")
    label(ax, cx + 19, 54, "web search · code runner\nemail · files", fs=6.3)
    arrow(ax, cx + 16, cy - 5.4 + 8.8, cx + 16, 50.5, style="<|-|>")
    box(ax, cx - 10, 1.5, 20, 7, "Memory\n(notes, transcript)", fill="white", fs=6.8)
    arrow(ax, cx - 4, 9, cx + 12, cy + 5.4, style="<|-|>", ls="--", lw=0.7, rad=0.25)
    arrow(ax, cx - 6, 9, cx - 16, cy - 14.4, style="<|-|>", ls="--", lw=0.7)
    box(ax, 80, 6, 17, 9, "Stop: goal met\nor limit reached", fill="white", fs=6.5)
    arrow(ax, cx - 16, cy - 14.4, 79.5, 10.5, rad=0.25, lw=0.8)
    label(ax, 62, 10.5, "done?", fs=6.5, italic=True)
    box(ax, 83, 44, 14, 7, "Human\ncheck", fill="white", fs=6.8)
    arrow(ax, 85, 43.5, cx + 25.5, cy - 9, ls="--", lw=0.7, rad=-0.2)
    label(ax, 92, 33, "approve /\ninterrupt", fs=6, italic=True, color=G1)
    save(fig, "fig-05-01")


@fig("fig-05-02")
def f0502():
    fig, ax = canvas(3.1, ylim=(0, 74))
    lanes = [("User", 10), ("Application", 37), ("Language model", 64), ("Weather tool", 90)]
    for n, x in lanes:
        box(ax, x - 9, 66, 18, 6, n, fill=G4, fs=7.5)
        ax.plot([x, x], [65.5, 3], color=G2, lw=0.7, ls=(0, (3, 3)))
    X = dict(lanes)
    msgs = [
        ("User", "Application", "1  Weather in Leeds tomorrow?", False),
        ("Application", "Language model", "2  question + tool list", False),
        ("Language model", "Application", "3  get_weather(Leeds, tomorrow)", False),
        ("Application", "Weather tool", "4  run get_weather", False),
        ("Weather tool", "Application", "5  forecast data", True),
        ("Application", "Language model", "6  tool result as text", False),
        ("Language model", "Application", "7  final answer", True),
        ("Application", "User", "8  answer shown", True),
    ]
    y = 59
    for a, b, t, ret in msgs:
        xa, xb = X[a], X[b]
        arrow(ax, xa, y, xb, y, ls="--" if ret else "-", lw=0.8)
        mono = t.startswith("3")
        ax.text((xa + xb) / 2, y + 1.3, t, ha="center", va="bottom", fontsize=6.6,
                family="DejaVu Sans Mono" if mono else "EB Garamond")
        y -= 7
    ax.add_patch(F.FancyBboxPatch((35.8, 30), 2.4, 16, boxstyle="square,pad=0", fc=G3, ec=INK, lw=0.5))
    label(ax, 30, 38, "holds permissions;\ndecides whether to run", fs=6, ha="right", italic=True, color=G1)
    box(ax, 66, 21, 30, 6.5, "tool output enters the same\ncontext as the instructions", fill=G4, fs=6.2, italic=True)
    save(fig, "fig-05-02")


@fig("fig-05-03")
def f0503():
    fig = F.figure(2.5)
    ax = fig.add_axes([0.1, 0.15, 0.72, 0.8])
    n = np.arange(1, 51)
    for p, ls, lab in ((0.99, "-", "99% per step"), (0.95, "--", "95% per step"), (0.90, ":", "90% per step")):
        y = 100 * p ** n
        ax.plot(n, y, color=INK, ls=ls, lw=1.3)
        ax.text(51, y[-1], lab, fontsize=7.5, va="center")
    ax.plot([20], [100 * 0.95 ** 20], "o", mfc="white", mec=INK, ms=4)
    ax.annotate("20 steps at 95% ≈ 36%", xy=(20, 35.8), xytext=(24, 52), fontsize=7.5,
                arrowprops=dict(arrowstyle="-", color=G2, lw=0.6))
    ax.set_xlim(0, 50)
    ax.set_ylim(0, 100)
    ax.set_xticks(range(0, 51, 10))
    ax.set_yticks(range(0, 101, 20))
    ax.set_xlabel("Number of steps in task")
    ax.set_ylabel("Probability whole task succeeds (%)")
    F.save(fig, "fig-05-03")
