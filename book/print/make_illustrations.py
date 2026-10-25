"""Chapter-opener illustrations for the book.

One continuous style: monochrome line art, one pen weight, round caps, a single
light-grey fill, and a horizon line that enters every drawing at the same height
on the left and leaves at the same height on the right, so that all twenty
drawings, laid side by side, form one unbroken landscape.
"""
import math
import os

W, H, Y = 1200, 300, 232  # canvas and horizon height
INK = "#1d1d1d"
GREY = "#e4e4e4"
MID = "#b9b9b9"
OUT = os.path.join(os.path.dirname(__file__), "illustrations")


def svg(body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}">'
        f'<g fill="none" stroke="{INK}" stroke-width="2.6" stroke-linecap="round" '
        f'stroke-linejoin="round">{body}</g></svg>'
    )


def horizon(gaps=()):
    """The continuous line, always unbroken from edge to edge."""
    return f'<line x1="0" y1="{Y}" x2="{W}" y2="{Y}"/>'


def thin(d, w=1.5, extra=""):
    return f'<path d="{d}" stroke-width="{w}" {extra}/>'


def path(d, fill="none", w=None):
    sw = f' stroke-width="{w}"' if w else ""
    return f'<path d="{d}" fill="{fill}"{sw}/>'


def text(x, y, s, size=20, anchor="middle", weight=400):
    return (
        f'<text x="{x}" y="{y}" font-family="EB Garamond, serif" font-size="{size}" '
        f'font-weight="{weight}" text-anchor="{anchor}" fill="{INK}" stroke="none">{s}</text>'
    )


def house(x, w=90, h=60, roof=40, windows=1, lit=False, door=True):
    b = Y
    s = path(f"M{x} {b} V{b-h} L{x+w/2} {b-h-roof} L{x+w} {b-h} V{b}")
    fill = GREY if lit else "none"
    ww = 18
    for i in range(windows):
        wx = x + (i + 1) * w / (windows + 1) - ww / 2
        s += f'<rect x="{wx}" y="{b-h+14}" width="{ww}" height="{ww}" fill="{fill}" stroke-width="2"/>'
    if door:
        s += f'<rect x="{x+w-26}" y="{b-30}" width="14" height="30" stroke-width="2"/>'
    return s


def pylon(x, h=150, arm=40):
    t = Y - h
    s = path(f"M{x-22} {Y} L{x-5} {t} L{x+5} {t} L{x+22} {Y}")
    # lattice
    n = 6
    for i in range(n):
        y0 = Y - i * h / n
        y1 = Y - (i + 1) * h / n
        xa0 = x - 22 + 17 * (i / n)
        xb0 = x + 22 - 17 * (i / n)
        xa1 = x - 22 + 17 * ((i + 1) / n)
        xb1 = x + 22 - 17 * ((i + 1) / n)
        s += thin(f"M{xa0} {y0} L{xb1} {y1} M{xb0} {y0} L{xa1} {y1}", 1.2)
    s += path(f"M{x-arm} {t+18} H{x+arm} M{x-arm*0.7} {t+42} H{x+arm*0.7}")
    s += path(f"M{x-6} {t} L{x} {t-14} L{x+6} {t}")
    return s


def wires(xs, h=150, arm=40, sag=26, drop=None):
    s = ""
    for a, b in zip(xs, xs[1:]):
        for off, yy in ((-arm, 18), (arm, 18), (-arm * 0.7, 42), (arm * 0.7, 42)):
            y = Y - h + yy
            sg = sag if drop is None or a < drop else sag * 3.2
            s += thin(f"M{a+off} {y} Q{(a+b)/2+off} {y+sg} {b+off} {y}", 1.3)
    return s


def snow(n=40, seed=3, x0=0, x1=W, y0=20, y1=200):
    import random

    r = random.Random(seed)
    return "".join(
        f'<circle cx="{r.uniform(x0, x1):.0f}" cy="{r.uniform(y0, y1):.0f}" r="{r.uniform(1.2, 2.4):.1f}" fill="{INK}" stroke="none"/>'
        for _ in range(n)
    )


def tree(x, h=70):
    return path(f"M{x} {Y} V{Y-h*0.35}") + path(
        f"M{x} {Y-h} L{x-h*0.28} {Y-h*0.35} H{x+h*0.28} Z", fill=GREY, w=2.2
    )


def figure(x, s=1.0, filled=False):
    f = GREY if filled else "none"
    return (
        f'<circle cx="{x}" cy="{Y-40*s}" r="{8*s}" fill="{f}" stroke-width="{2*s:.1f}"/>'
        + path(f"M{x-13*s} {Y} Q{x-13*s} {Y-28*s} {x} {Y-28*s} Q{x+13*s} {Y-28*s} {x+13*s} {Y}", fill=f, w=2 * s)
    )


# ---------------------------------------------------------------- scenes
def ch00():
    s = horizon()
    s += house(150, 120, 70, 50, windows=2, lit=True)
    s += f'<rect x="272" y="{Y-34}" width="30" height="34" stroke-width="2"/>'  # heat pump
    s += f'<circle cx="287" cy="{Y-17}" r="10" stroke-width="1.6"/>'
    s += tree(80, 80) + tree(380, 60)
    s += pylon(620) + pylon(860) + pylon(1100)
    s += wires([620, 860, 1100])
    # the frequency trace, falling
    s += thin("M420 60 H700 C730 60 740 70 760 90 S800 150 840 170", 2.2, 'stroke-dasharray="1 0"')
    s += text(430, 52, "50.0 Hz", 18, "start")
    s += text(800, 200, "19:42", 18, "end", 600)
    s += snow(55, 7)
    return s


def ch01():
    s = horizon()
    for i in range(11):
        x = 40 + i * 70
        s += house(x, 46, 30, 22, windows=1, lit=False, door=False)
        s += thin(f"M{x+23} {Y-60} V{Y-78} M{x+17} {Y-72} L{x+23} {Y-80} L{x+29} {Y-72}", 1.6)
    s += pylon(900, 140) + pylon(1110, 140)
    s += wires([900, 1110], 140)
    return s


def ch02():
    s = horizon()
    # inputs: many small marks at top left flowing into a funnel
    import random

    r = random.Random(2)
    for _ in range(60):
        x, y = r.uniform(60, 420), r.uniform(20, 90)
        s += thin(f"M{x:.0f} {y:.0f} q6 -6 12 0", 1.4)
    s += path("M90 105 H400 L280 175 V205 H210 V175 Z", fill=GREY)
    s += thin("M245 205 C 300 230 500 140 620 120", 1.6)
    s += thin("M245 205 C 320 240 520 190 760 150", 1.6)
    s += thin("M245 205 C 340 250 560 230 900 170", 1.6)
    for x, y in ((620, 120), (760, 150), (900, 170)):
        s += f'<rect x="{x}" y="{y}" width="110" height="70" rx="6" stroke-width="2.2"/>'
        s += thin(f"M{x+16} {y+28} q10 -12 20 0 t20 0 t20 0 t20 0 M{x+16} {y+46} H{x+80}", 1.5)
        s += path(f"M{x+55} {y+70} V{Y}")
    return s


def ch03():
    s = horizon()
    nodes = [(80, 120), (190, 70), (300, 140), (420, 90), (520, 170), (640, 110), (760, 60),
             (860, 150), (980, 100), (1100, 160), (360, 40), (700, 190)]
    family = {1, 2, 3, 5, 6, 8, 9}
    edges = [(0, 1), (1, 2), (2, 3), (3, 4), (3, 5), (5, 6), (5, 7), (7, 8), (8, 9), (1, 10), (10, 3), (4, 11), (11, 7), (6, 8), (0, 2)]
    for a, b in edges:
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        s += thin(f"M{x1} {y1} L{x2} {y2}", 1.4)
    for i, (x, y) in enumerate(nodes):
        s += f'<circle cx="{x}" cy="{y}" r="{15 if i in family else 11}" fill="{MID if i in family else "white"}" stroke-width="2.2"/>'
    for x in (300, 860):
        s += thin(f"M{x} {nodes[2][1] if x == 300 else nodes[7][1]} V{Y}", 1.2, 'stroke-dasharray="3 6"')
    return s


def ch04():
    s = horizon([(560, 700)])
    # insulators and an open disconnector blade
    for x in (180, 330):
        s += path(f"M{x} {Y} V{Y-70}")
        for k in range(5):
            s += f'<ellipse cx="{x}" cy="{Y-80-k*12}" rx="14" ry="5" stroke-width="2"/>'
    s += path(f"M180 {Y-140} L300 {Y-200}")
    s += f'<circle cx="330" cy="{Y-140}" r="5" fill="{INK}" stroke="none"/>'
    # desk with binder and pencil
    s += path(f"M520 {Y-60} H740 M540 {Y-60} V{Y} M720 {Y-60} V{Y}")
    s += path(f"M560 {Y-60} L548 {Y-120} L630 {Y-128} L632 {Y-62}", fill=GREY)
    s += path(f"M632 {Y-62} L640 {Y-128} L718 {Y-120} L704 {Y-60}", fill="white")
    for k in range(4):
        s += thin(f"M650 {Y-110+k*12} L700 {Y-106+k*12}", 1.2)
    s += thin(f"M598 {Y-108} q12 -8 22 0", 1.2)
    s += path(f"M760 {Y-70} L860 {Y-90} L868 {Y-84} L768 {Y-64} Z")
    s += pylon(1030, 160) + thin(f"M1070 {Y-142} Q1150 {Y-120} 1200 {Y-128}", 1.3)
    return s


def ch05():
    s = horizon([(380, 820)])
    s += path(f"M380 {Y} V{Y-90} H820 V{Y} M380 {Y-45} H820 M600 {Y-90} V{Y}", w=2.4)
    for x in (480, 710):
        s += f'<circle cx="{x}" cy="{Y-22}" r="4" fill="{INK}" stroke="none"/><circle cx="{x}" cy="{Y-67}" r="4" fill="{INK}" stroke="none"/>'
    # photograph frame
    s += f'<rect x="420" y="{Y-190}" width="90" height="100" stroke-width="2.4"/>'
    s += f'<circle cx="452" cy="{Y-158}" r="9" stroke-width="1.6"/><circle cx="478" cy="{Y-154}" r="9" stroke-width="1.6"/>'
    s += thin(f"M436 {Y-108} Q452 {Y-140} 466 {Y-112} Q478 {Y-138} 494 {Y-108}", 1.6)
    # speaker
    s += f'<rect x="560" y="{Y-160}" width="70" height="70" rx="12" fill="{GREY}" stroke-width="2.4"/>'
    for r in (8, 16, 24):
        s += f'<circle cx="595" cy="{Y-125}" r="{r}" stroke-width="1.4"/>'
    # key dish
    s += path(f"M680 {Y-98} Q740 {Y-78} 790 {Y-98}")
    s += thin(f"M720 {Y-100} l10 -8 m0 0 h22 m-4 0 v5 m-6 -5 v4", 1.6)
    return s


def ch06():
    s = horizon([(300, 900)])
    s += path(f"M300 {Y-40} H900 M330 {Y-40} V{Y} M870 {Y-40} V{Y}")
    for k in range(9):
        off = (k % 3) * 3
        s += path(f"M{430+off} {Y-40-k*11} H{640+off}", w=2)
    s += f'<rect x="440" y="{Y-170}" width="200" height="70" fill="white" stroke-width="2.4"/>'
    s += thin(f"M458 {Y-150} H600 M458 {Y-136} H580", 1.3)
    s += f'<rect x="458" y="{Y-124}" width="12" height="12" stroke-width="1.6"/>'
    s += thin(f"M460 {Y-118} l4 4 l8 -10", 2)
    s += thin(f"M490 {Y-114} c10 -14 18 6 26 -4 s14 -10 24 2", 1.8)
    s += path(f"M660 {Y-140} L760 {Y-176} L766 {Y-170} L666 {Y-134} Z")
    s += text(800, Y-60, "899 / 900", 22, "middle", 600)
    return s


def ch07():
    s = horizon()
    s += path(f"M0 {Y-22} L120 120 L190 170 L300 70 L420 190 L520 130 L700 {Y}", w=1.6)
    for i in range(14):
        x = 120 + i * 48
        s += figure(x, 0.85, filled=(i % 5 != 2))
    s += path(f"M900 {Y} V{Y-80} H1040 V{Y}")
    s += path(f"M940 {Y-80} V{Y-86} H1000 V{Y-80}")
    s += path(f"M955 {Y-100} H990 V{Y-130} H955 Z", fill="white")
    return s


def ch08():
    s = horizon([(820, 1080)])
    # ledger page with magnifier
    s += path(f"M120 40 H420 V200 H120 Z", fill="white")
    for k in range(9):
        y = 62 + k * 15
        s += thin(f"M138 {y} H300 M320 {y} H400", 1.2)
    s += f'<rect x="132" y="{62+5*15-9}" width="276" height="16" fill="{GREY}" stroke="none"/>'
    s += thin(f"M138 {62+5*15} H300 M320 {62+5*15} H400", 1.6)
    s += f'<circle cx="330" cy="{62+5*15}" r="46" stroke-width="3"/>'
    s += path(f"M362 {62+5*15+34} L420 {62+5*15+92}", w=6)
    # clinic and an empty plot
    s += path(f"M820 {Y} V{Y-80} H960 V{Y}")
    s += path(f"M880 {Y-62} h20 M890 {Y-72} v20", w=3)
    s += f'<rect x="842" y="{Y-38}" width="22" height="38" stroke-width="2"/>'
    s += thin(f"M960 {Y-80} H1080 V{Y}", 2, 'stroke-dasharray="8 8"')
    return s


def ch09():
    s = horizon([(470, 640)])
    for k in range(19):
        sh = 8 * math.sin(k * 0.7)
        s += path(f"M{480+sh} {Y-k*11} H{630+sh} V{Y-11-k*11} H{480+sh} Z", fill=("white" if k % 4 else GREY), w=1.8)
    s += figure(700, 1.0)
    # chess queen
    q = 960
    s += path(f"M{q-40} {Y} H{q+40} L{q+30} {Y-20} H{q-30} Z M{q-22} {Y-20} L{q-30} {Y-100} L{q-12} {Y-80} L{q} {Y-110} L{q+12} {Y-80} L{q+30} {Y-100} L{q+22} {Y-20}", fill=GREY)
    s += f'<circle cx="{q}" cy="{Y-118}" r="7" stroke-width="2"/>'
    return s


def ch10():
    s = horizon()
    for x in (150, 1050):
        s += path(f"M{x} {Y} V{Y-120}")
        s += f'<rect x="{x-24}" y="{Y-170}" width="48" height="56" rx="8" fill="{GREY}" stroke-width="2.4"/>'
    import random

    r = random.Random(10)
    for i in range(70):
        t = i / 69
        x = 200 + t * 800
        y = Y - 150 - 70 * math.sin(math.pi * t) + r.uniform(-14, 14)
        if r.random() < 0.5:
            s += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="2.6" fill="{INK}" stroke="none"/>'
        else:
            s += thin(f"M{x-5:.0f} {y:.0f} h10", 2.2)
    s += text(600, Y - 20, "?", 34, "middle", 600)
    return s


def ch11():
    s = horizon([(700, 1020)])
    # lattice
    cx, cy, r = 300, 120, 30
    for i in range(-2, 3):
        for j in range(-1, 2):
            x = cx + i * r * 1.5
            y = cy + j * r * math.sqrt(3) + (r * math.sqrt(3) / 2 if i % 2 else 0)
            pts = " ".join(f"{x+r*math.cos(math.pi/3*k):.1f},{y+r*math.sin(math.pi/3*k):.1f}" for k in range(6))
            s += f'<polygon points="{pts}" stroke-width="1.6"/>'
            s += f'<circle cx="{x:.0f}" cy="{y:.0f}" r="4" fill="{INK}" stroke="none"/>'
    # storage containers
    for k in range(2):
        x = 710 + k * 160
        s += path(f"M{x} {Y} V{Y-70} H{x+150} V{Y}", fill=GREY)
        for m in range(1, 6):
            s += thin(f"M{x+m*25} {Y-64} V{Y-6}", 1.2)
    # thermometer and snowflake
    s += path(f"M1100 {Y-40} V{Y-160} a10 10 0 0 1 20 0 V{Y-40}")
    s += f'<circle cx="1110" cy="{Y-30}" r="16" fill="{MID}" stroke-width="2.4"/>'
    s += text(1140, Y - 140, "−30°", 20, "start")
    for k in range(3):
        a = k * math.pi / 3
        s += thin(f"M{560+26*math.cos(a):.0f} {80+26*math.sin(a):.0f} L{560-26*math.cos(a):.0f} {80-26*math.sin(a):.0f}", 2)
    return s


def ch12():
    s = horizon([(80, 330)])
    # plant building with vents and steam
    s += path(f"M80 {Y} V{Y-90} H330 V{Y}", fill="white")
    for x in (120, 200, 280):
        s += f'<rect x="{x-14}" y="{Y-120}" width="28" height="30" stroke-width="2"/>'
        s += thin(f"M{x} {Y-128} c-16 -14 14 -24 0 -40 c-14 -14 14 -24 0 -42", 1.6)
    # pipes on stilts
    s += path(f"M330 {Y-50} H860 M330 {Y-62} H860", w=2.2)
    for x in range(360, 860, 60):
        s += thin(f"M{x} {Y-50} V{Y}", 1.6)
    # giraffe
    g = 980
    s += path(f"M{g-55} {Y-118} Q{g-60} {Y-150} {g-20} {Y-150} H{g+30} Q{g+52} {Y-150} {g+50} {Y-122} Q{g+46} {Y-104} {g+20} {Y-104} H{g-30} Q{g-52} {Y-104} {g-55} {Y-118} Z", fill=GREY)
    for lx in (g - 40, g - 26, g + 22, g + 36):
        s += path(f"M{lx} {Y-106} V{Y}", w=2.4)
    s += path(f"M{g+36} {Y-146} L{g+68} {Y-204}", w=3) + path(f"M{g+48} {Y-140} L{g+78} {Y-194}", w=3)
    s += path(f"M{g+64} {Y-206} Q{g+74} {Y-218} {g+100} {Y-204} Q{g+94} {Y-192} {g+78} {Y-194}", fill=GREY, w=2.2)
    s += path(f"M{g+70} {Y-210} l-2 -12 M{g+80} {Y-212} l2 -12", w=2)
    s += path(f"M{g-56} {Y-130} q-14 10 -12 40", w=1.6)
    for (sx, sy) in ((g-30, Y-132), (g-5, Y-124), (g+22, Y-134)):
        s += f'<circle cx="{sx}" cy="{sy}" r="6" fill="{MID}" stroke="none"/>'
    return s


def ch13():
    s = horizon([(820, 1040)])
    # slow clock
    s += f'<circle cx="300" cy="120" r="80" stroke-width="2.6"/>'
    for k in range(12):
        a = k * math.pi / 6
        s += thin(f"M{300+70*math.cos(a):.0f} {120+70*math.sin(a):.0f} L{300+78*math.cos(a):.0f} {120+78*math.sin(a):.0f}", 2)
    s += path("M300 120 L300 66", w=3) + path("M300 120 L336 138", w=3)
    s += path(f"M300 200 V{Y}")
    # fast clock with blurred hand
    s += f'<circle cx="600" cy="140" r="40" stroke-width="2.2"/>'
    for k in range(10):
        a = k * math.pi / 5
        s += thin(f"M600 140 L{600+34*math.cos(a):.0f} {140+34*math.sin(a):.0f}", 1, 'stroke-opacity="0.6"')
    s += path(f"M600 180 V{Y}")
    # register book on a table
    s += path(f"M820 {Y-50} H1040 M840 {Y-50} V{Y} M1020 {Y-50} V{Y}")
    s += path(f"M860 {Y-50} L870 {Y-80} H930 L930 {Y-50} M930 {Y-50} L930 {Y-80} H990 L1000 {Y-50}", fill=GREY)
    return s


def ch14():
    s = horizon([(300, 520)])
    # chair
    s += path(f"M330 {Y-84} H480 M340 {Y-84} V{Y} M470 {Y-84} V{Y} M480 {Y-84} V{Y-210} M472 {Y-84} L486 {Y-84}") + thin(f"M480 {Y-170} H470 M480 {Y-130} H470", 2)
    # violin leaning
    vx, vy = 580, Y
    s += f'<g transform="rotate(-12 {vx} {vy})">'
    s += path(f"M{vx} {vy-4} c-34 0 -44 -30 -30 -52 c10 -14 10 -22 0 -32 c-14 -22 -4 -50 30 -50 c34 0 44 28 30 50 c-10 10 -10 18 0 32 c14 22 4 52 -30 52 Z", fill=GREY)
    s += path(f"M{vx} {vy-138} V{vy-210}", w=4)
    s += f'<circle cx="{vx}" cy="{vy-218}" r="8" stroke-width="2.2"/>'
    s += thin(f"M{vx-12} {vy-82} c-6 -10 6 -20 0 -30 M{vx+12} {vy-82} c-6 -10 6 -20 0 -30", 1.6)
    s += "</g>"
    # sealed envelope
    s += path(f"M820 {Y-30} H1040 V{Y-130} H820 Z", fill="white")
    s += thin(f"M820 {Y-130} L930 {Y-70} L1040 {Y-130}", 1.8)
    s += f'<circle cx="930" cy="{Y-70}" r="14" fill="{MID}" stroke-width="2"/>'
    s += path(f"M840 {Y-30} V{Y} M1020 {Y-30} V{Y}", w=1.4)
    return s


def ch15():
    s = horizon([(1020, 1150)])
    import random

    r = random.Random(15)
    for i in range(26):
        for j in range(8):
            x = 200 + i * 30 + (j % 2) * 15
            y = 40 + j * 22
            op = r.choice((1, 1, 0.6, 0.35, 0.15))
            s += f'<circle cx="{x}" cy="{y}" r="4" fill="{INK}" fill-opacity="{op}" stroke="none"/>'
    # plant in pot
    s += path(f"M80 {Y} L70 {Y-40} H150 L140 {Y} Z", fill=GREY)
    for a in (-60, -30, 0, 30, 60):
        rad = math.radians(a - 90)
        s += thin(f"M110 {Y-40} Q{110+40*math.cos(rad)} {Y-80+30*math.sin(rad)/3} {110+70*math.cos(rad):.0f} {Y-40+60*math.sin(rad):.0f}", 1.8)
    # server rack
    s += path(f"M1020 {Y} V{Y-190} H1150 V{Y}")
    for k in range(8):
        s += thin(f"M1034 {Y-176+k*22} H1136", 1.3)
        s += f'<circle cx="1126" cy="{Y-182+k*22}" r="2.4" fill="{INK}" stroke="none"/>'
    return s


def ch16():
    s = horizon()
    import random

    r = random.Random(16)
    for _ in range(70):
        x, y = r.uniform(0, W), r.uniform(10, 200)
        s += thin(f"M{x:.0f} {y:.0f} l-6 16", 1.1, 'stroke-opacity="0.7"')
    s += f'<circle cx="640" cy="120" r="58" stroke-width="5" stroke="{MID}"/>'
    s += f'<circle cx="540" cy="120" r="58" stroke-width="5"/>'
    def arc(cx, cy, r, a0, a1):
        x0, y0 = cx + r * math.cos(math.radians(a0)), cy + r * math.sin(math.radians(a0))
        x1, y1 = cx + r * math.cos(math.radians(a1)), cy + r * math.sin(math.radians(a1))
        return f"M{x0:.1f} {y0:.1f} A{r} {r} 0 0 1 {x1:.1f} {y1:.1f}"
    s += f'<path d="{arc(640, 120, 58, 135, 165)}" stroke="white" stroke-width="11"/>'
    s += f'<path d="{arc(640, 120, 58, 128, 172)}" stroke="{MID}" stroke-width="5"/>'
    s += text(540, 228, "7", 26, "middle", 600) + text(640, 228, "8", 26, "middle", 600)
    s += thin("M560 220 H620 l-8 -6 m8 6 l-8 6", 1.8)
    return s


def ch17():
    s = horizon()
    s += house(130, 120, 70, 50, windows=2, lit=True)
    s += f'<rect x="252" y="{Y-34}" width="30" height="34" stroke-width="2"/>'
    s += f'<circle cx="267" cy="{Y-17}" r="10" stroke-width="1.6"/>'
    for i, x in enumerate((340, 430, 520)):
        s += house(x, 70, 44, 30, windows=1, lit=True, door=False)
    # church
    s += path(f"M640 {Y} V{Y-80} H720 V{Y} M640 {Y-80} L680 {Y-110} L720 {Y-80} M680 {Y-110} V{Y-190} M670 {Y-174} H690")
    s += f'<rect x="668" y="{Y-60}" width="24" height="34" rx="12" fill="{GREY}" stroke-width="2"/>'
    s += pylon(880) + pylon(1110)
    s += wires([880, 1110])
    s += thin("M330 60 H820", 2.2)
    s += text(330, 52, "50.0 Hz", 18, "start")
    s += snow(35, 17)
    return s


def ch18():
    s = horizon([(660, 1040)])
    # window with snow
    s += f'<rect x="150" y="40" width="200" height="150" stroke-width="2.4"/>'
    s += thin("M250 40 V190 M150 115 H350", 1.6)
    s += snow(18, 18, 160, 340, 50, 180)
    # music stand
    s += path(f"M480 {Y} L510 {Y-110} L540 {Y} M510 {Y-110} V{Y-130}")
    s += path(f"M470 {Y-130} H550 L540 {Y-180} H480 Z", fill="white")
    s += thin(f"M488 {Y-166} H532 M486 {Y-156} H534 M484 {Y-146} H536", 1.1)
    # shelf with binder and pencil
    s += path(f"M660 {Y-70} H1040 M680 {Y-70} V{Y} M1020 {Y-70} V{Y}")
    s += path(f"M720 {Y-70} V{Y-180} H770 V{Y-70}", fill=GREY)
    s += f'<rect x="732" y="{Y-160}" width="26" height="20" fill="white" stroke-width="1.6"/>'
    s += path(f"M770 {Y-70} V{Y-160} H800 V{Y-70}")
    s += path(f"M840 {Y-72} L980 {Y-82} L982 {Y-76} L842 {Y-70}", w=2)
    return s


def ch19():
    s = f'<line x1="0" y1="{Y}" x2="1080" y2="{Y}"/>'
    for i in range(29):
        x = 60 + i * 35
        s += thin(f"M{x} {Y} V{Y-(18 if i % 5 == 0 else 10)}", 1.6)
    s += f'<circle cx="1094" cy="{Y}" r="12" fill="{GREY}" stroke-width="2.6"/>'
    return s


SCENES = [ch00, ch01, ch02, ch03, ch04, ch05, ch06, ch07, ch08, ch09,
          ch10, ch11, ch12, ch13, ch14, ch15, ch16, ch17, ch18, ch19]

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for i, fn in enumerate(SCENES):
        with open(os.path.join(OUT, f"ill-{i:02d}.svg"), "w") as f:
            f.write(svg(fn()))
    print(f"wrote {len(SCENES)} illustrations to {OUT}")
