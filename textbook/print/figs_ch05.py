"""Figures for chapter 5, drawn from figures/specs/ in the house style."""
import math

import numpy as np

import figstyle as F
from figstyle import G1, G2, G3, G4, INK, arrow, box, canvas, fig, label, node, save


@fig("fig-05-01")
def f0501():
    fig, ax = canvas(3.0, ylim=(0, 66))
    W, H = 18, 8
    pos = {"Perceive": (32, 47), "Plan": (66, 47), "Act": (66, 21), "Observe": (32, 21)}
    sub = {"Perceive": "read current state", "Plan": "model chooses step", "Act": "call a tool", "Observe": "read tool output"}
    for k, (x, y) in pos.items():
        box(ax, x - W / 2, y - H / 2, W, H, "", fill="white")
        label(ax, x, y + 1.3, k, fs=8.5, weight="bold")
        label(ax, x, y - 2.1, sub[k], fs=6.2, color=G1, italic=True)
    # the clockwise cycle
    e = W / 2 + 1.0
    arrow(ax, 32 + e, 47, 66 - e, 47)
    arrow(ax, 66, 47 - H / 2 - 0.9, 66, 21 + H / 2 + 0.9)
    arrow(ax, 66 - e, 21, 32 + e, 21)
    arrow(ax, 32, 21 + H / 2 + 0.9, 32, 47 - H / 2 - 0.9)
    # goal in
    box(ax, 2, 43, 13, 8, "Goal from\nuser", fill=G4, fs=7.5)
    arrow(ax, 15.6, 47, 32 - e, 47)
    # memory in the middle of the loop
    box(ax, 42, 31, 14, 6, "", fill=G4)
    label(ax, 49, 35.2, "Memory", fs=7.5, weight="bold")
    label(ax, 49, 32.4, "notes, transcript", fs=5.9, italic=True, color=G1)
    arrow(ax, 54.5, 37.6, 58.5, 42.2, style="<|-|>", ls="--", lw=0.7, ms=6)
    arrow(ax, 43.5, 30.4, 39.5, 25.8, style="<|-|>", ls="--", lw=0.7, ms=6)
    # tools to the right of Act
    box(ax, 82, 14.5, 16, 13, "", fill=G4)
    label(ax, 90, 24.5, "Tools", fs=8, weight="bold")
    label(ax, 90, 19.2, "web search\ncode runner\nemail · files", fs=6.2)
    arrow(ax, 66 + e, 21, 81.2, 21, style="<|-|>")
    # human check to the right of Plan
    box(ax, 83, 44, 14, 6, "Human check", fill="white", fs=7.2)
    arrow(ax, 83.5, 43.3, 73.5, 25.6, ls="--", lw=0.7, rad=-0.15)
    label(ax, 85.5, 36.3, "approve /\ninterrupt", fs=6.2, italic=True, color=G1, ha="left")
    # stop below Observe
    arrow(ax, 32, 21 - H / 2 - 0.9, 32, 9.8)
    label(ax, 33.5, 13.3, "done?", fs=6.5, italic=True, ha="left")
    box(ax, 20, 2.5, 24, 6.5, "Stop: goal met\nor limit reached", fill="white", fs=6.8)
    save(fig, "fig-05-01")


@fig("fig-05-02")
def f0502():
    fig, ax = canvas(3.2, ylim=(0, 78))
    lanes = [("User", 9), ("Application", 34), ("Language model", 64), ("Weather tool", 90)]
    for n, x in lanes:
        box(ax, x - 8.5, 70, 17, 6, n, fill=G4, fs=7.5)
        ax.plot([x, x], [69.5, 3], color=G2, lw=0.7, ls=(0, (3, 3)))
    X = dict(lanes)
    msgs = [
        ("User", "Application", "1  Weather in Leeds tomorrow?", False, 63),
        ("Application", "Language model", "2  question + tool list", False, 56),
        ("Language model", "Application", "3  get_weather(Leeds, tomorrow)", False, 47),
        ("Application", "Weather tool", "4  run get_weather", False, 40),
        ("Weather tool", "Application", "5  forecast data", True, 33),
        ("Application", "Language model", "6  tool result as text", False, 26),
        ("Language model", "Application", "7  final answer", True, 19),
        ("Application", "User", "8  answer shown", True, 12),
    ]
    for a, b, t, ret, y in msgs:
        xa, xb = X[a], X[b]
        arrow(ax, xa, y, xb, y, ls="--" if ret else "-", lw=0.8)
        if t.startswith("3"):
            # the structured request: a small framed label
            box(ax, (xa + xb) / 2 - 13.3, y + 1.4, 26.6, 3.6, "", fill="white", lw=0.5,
                style="round,pad=0.3,rounding_size=0.6")
            ax.text((xa + xb) / 2, y + 3.2, t, ha="center", va="center", fontsize=6.3)
            label(ax, X["Language model"] + 1.5, y + 3.2, "structured request", fs=6, ha="left", italic=True, color=G1)
        else:
            ax.text((xa + xb) / 2, y + 1.2, t, ha="center", va="bottom", fontsize=6.6)
    # activation bar on the Application lifeline, messages 3-5
    ax.add_patch(F.FancyBboxPatch((X["Application"] - 1.1, 31.5), 2.2, 16.5, boxstyle="square,pad=0",
                                  fc=G3, ec=INK, lw=0.5, zorder=3))
    label(ax, X["Application"] - 2.5, 39.5, "holds permissions;\ndecides whether\nto run", fs=6, ha="right",
          italic=True, color=G1)
    # shaded note beside message 6, between the model and tool lifelines
    box(ax, 66.8, 17.5, 20, 9.5, "tool output enters\nthe same context\nas the instructions", fill=G4,
        fs=6, italic=True, lw=0.5)
    save(fig, "fig-05-02")


@fig("fig-05-03")
def f0503():
    fig = F.figure(2.5)
    ax = fig.add_axes([0.1, 0.15, 0.72, 0.8])
    n = np.arange(1, 51)
    for p, ls, lab in ((0.99, "-", "99% per step"), (0.95, "--", "95% per step"), (0.90, ":", "90% per step")):
        y = 100 * p ** n
        ax.plot(n, y, color=INK, ls=ls, lw=1.3)
        ax.text(51, {0.99: y[-1], 0.95: 10.5, 0.90: 1.0}[p], lab, fontsize=7.5, va="center")
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
