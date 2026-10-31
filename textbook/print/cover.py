"""Build the paperback cover for BoD (back + spine + front, one PDF, 5 mm bleed on all four sides).

BoD's cover calculator (bod.de/hilfe/coverberechnung) gives, for a 14.8 x 21 cm paperback:
    spine_width = pages / 2 * paper thickness per leaf
    cover spine = spine_width + 0.6 mm (the two cover boards)
    cover sheet = 5 mm + 148 mm + cover spine + 148 mm + 5 mm  by  5 mm + 210 mm + 5 mm
The final spine comes from myBoD once the book project is set up; pass it with --spine-mm.

Run:  python3 textbook/print/cover.py [--pages 590] [--paper weiss] [--spine-mm 36.0] [--isbn 978-3-...]
Writes delivery/understanding-ai_cover_A5_PB.pdf (upload this) and
delivery/understanding-ai_cover_A5_PB_guides.pdf (same with trim, fold and safe-zone lines; do not upload).
"""
import argparse
import math
import os
import random

PRINT = os.path.dirname(os.path.abspath(__file__))
TB = os.path.dirname(PRINT)

# thickness per leaf in cm, from the BoD cover calculator
PAPER = {"weiss": 0.012, "chamois": 0.0135, "weiss80": 0.0105, "chamois80": 0.0105}
TRIM_W, TRIM_H, BLEED = 148.0, 210.0, 5.0
SAFE = 10.0          # keep text this far inside the trim and the spine folds
SPINE_SAFE = 2.5     # keep spine text this far inside each fold (the spine can shift by about 1 mm)

BG = (10, 16, 32)
DIM = (24, 35, 59)
MID = (42, 59, 94)
CYAN = (46, 230, 214)
VIOLET = (124, 108, 255)
AMBER = (255, 176, 32)
INK = "#F2F4F8"
SOFT = "#9AA7C0"


def mix(a, b, t):
    t = max(0.0, min(1.0, t))
    return tuple(round(a[i] + (b[i] - a[i]) * t) for i in range(3))


def hexc(c):
    return "#%02X%02X%02X" % c


def lattice(svg, x0, x1, y0, y1, rows, cols, strength, seed, highlight=None, start=0):
    """A layered network: rows of jittered nodes, each linked to its nearest nodes in the next row.
    strength 0..1 sets how far the colours rise above the background (no transparency is used)."""
    rnd = random.Random(seed)
    layers = []
    for r in range(rows):
        y = y0 + (y1 - y0) * r / (rows - 1)
        row = []
        for c in range(cols):
            x = x0 + (x1 - x0) * (c + 0.5) / cols + rnd.uniform(-0.32, 0.32) * (x1 - x0) / cols
            row.append((x, y + rnd.uniform(-1.6, 1.6)))
        layers.append(row)
    edges = []
    for r in range(rows - 1):
        for i, a in enumerate(layers[r]):
            near = sorted(range(cols), key=lambda j: abs(layers[r + 1][j][0] - a[0]))[: 3]
            for j in near:
                if rnd.random() < 0.8:
                    edges.append((r, i, j))
    hot = set()
    if highlight:
        # one path of activation from the bottom row up to the highlighted node in the top row
        target = highlight
        j = target
        for r in range(start, rows - 1):
            # walk downwards from the active node and record the edges
            below = sorted(range(cols), key=lambda k: abs(layers[r + 1][k][0] - layers[r][j][0]))[:2]
            k = rnd.choice(below)
            hot.add((r, j, k))
            j = k
        # a few side branches
        for (r, i, k) in list(hot):
            for kk in sorted(range(cols), key=lambda q: abs(layers[r + 1][q][0] - layers[r][i][0]))[1:3]:
                if rnd.random() < 0.55:
                    hot.add((r, i, kk))
    for (r, i, j) in edges:
        if (r, i, j) in hot:
            continue
        a, b = layers[r][i], layers[r + 1][j]
        col = mix(BG, MID, strength * (0.55 + 0.45 * rnd.random()))
        svg.append(f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="{hexc(col)}" stroke-width="0.22"/>')
    hot_nodes = set()
    for (r, i, j) in sorted(hot, key=lambda e: -e[0]):
        a, b = layers[r][i], layers[r + 1][j]
        t = (r - start) / max(1, rows - 2 - start)
        col = mix(mix(CYAN, VIOLET, t), BG, 1 - strength)
        glow = mix(col, BG, 0.72)
        svg.append(f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="{hexc(glow)}" stroke-width="1.5" stroke-linecap="round"/>')
        svg.append(f'<line x1="{a[0]:.2f}" y1="{a[1]:.2f}" x2="{b[0]:.2f}" y2="{b[1]:.2f}" stroke="{hexc(col)}" stroke-width="0.45" stroke-linecap="round"/>')
        hot_nodes.add((r, i))
        hot_nodes.add((r + 1, j))
    for r, row in enumerate(layers):
        for i, (x, y) in enumerate(row):
            if (r, i) in hot_nodes:
                continue
            col = mix(BG, MID, strength * 1.15)
            svg.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="0.55" fill="{hexc(col)}"/>')
    for (r, i) in hot_nodes:
        x, y = layers[r][i]
        t = (r - start) / max(1, rows - 1 - start)
        col = mix(mix(CYAN, VIOLET, t), BG, 1 - strength)
        for rad, k in ((2.6, 0.86), (1.7, 0.66), (1.05, 0.0)):
            svg.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{rad}" fill="{hexc(mix(col, BG, k))}"/>')
    if highlight is not None:
        x, y = layers[start][highlight]
        for rad, k in ((5.2, 0.9), (3.6, 0.76), (2.5, 0.5), (1.6, 0.0)):
            svg.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="{rad}" fill="{hexc(mix(AMBER, BG, k))}"/>')
        return (x, y)
    return None


def ean13(svg, isbn, x, y, w, h):
    """EAN-13 bars for an ISBN-13, drawn as solid black rectangles on white."""
    d = [int(c) for c in isbn if c.isdigit()]
    if len(d) == 12:
        d.append((10 - sum(v * (3 if i % 2 else 1) for i, v in enumerate(d)) % 10) % 10)
    assert len(d) == 13, "ISBN must have 13 digits"
    L = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
    G = ["0100111", "0110011", "0011011", "0100001", "0011101", "0111001", "0000101", "0010001", "0001001", "0010111"]
    R = ["1110010", "1100110", "1101100", "1000010", "1011100", "1001110", "1010000", "1000100", "1001000", "1110100"]
    parity = ["LLLLLL", "LLGLGG", "LLGGLG", "LLGGGL", "LGLLGG", "LGGLLG", "LGGGLL", "LGLGLG", "LGLGGL", "LGGLGL"][d[0]]
    bits = "101" + "".join((L if p == "L" else G)[v] for p, v in zip(parity, d[1:7])) + "01010" + "".join(R[v] for v in d[7:]) + "101"
    m = w / (len(bits) + 11)  # 11 modules of quiet zone on the left
    guard = {0, 1, 2, 45, 46, 47, 48, 49, 92, 93, 94}
    for i, b in enumerate(bits):
        if b == "1":
            bh = h if i in guard else h - 3.2
            svg.append(f'<rect x="{x + (11 + i) * m:.3f}" y="{y:.2f}" width="{m + 0.01:.3f}" height="{bh:.2f}" fill="#000"/>')
    s = "".join(map(str, d))
    fs = 2.9
    svg.append(f'<text x="{x + 4 * m:.2f}" y="{y + h:.2f}" font-family="JBM" font-size="{fs}" fill="#000">{s[0]}</text>')
    svg.append(f'<text x="{x + (11 + 24) * m:.2f}" y="{y + h:.2f}" font-family="JBM" font-size="{fs}" fill="#000" text-anchor="middle" letter-spacing="0.9">{s[1:7]}</text>')
    svg.append(f'<text x="{x + (11 + 71) * m:.2f}" y="{y + h:.2f}" font-family="JBM" font-size="{fs}" fill="#000" text-anchor="middle" letter-spacing="0.9">{s[7:]}</text>')
    hy = f"{s[:3]}-{s[3]}-{s[4:8]}-{s[8:12]}-{s[12]}"
    svg.append(f'<text x="{x + w / 2:.2f}" y="{y - 1.4:.2f}" font-family="JBM" font-size="2.6" fill="#000" text-anchor="middle">ISBN {hy}</text>')


def build(pages, paper, spine_mm, isbn, guides):
    if spine_mm is None:
        spine_mm = round(pages / 2 * PAPER[paper] * 10 + 0.6, 2)
    S = spine_mm
    W = BLEED + TRIM_W + S + TRIM_W + BLEED
    H = BLEED + TRIM_H + BLEED
    back_x = BLEED
    spine_x = BLEED + TRIM_W
    front_x = spine_x + S
    top = BLEED
    svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}mm" height="{H}mm" viewBox="0 0 {W} {H}">',
           f'<rect x="0" y="0" width="{W}" height="{H}" fill="{hexc(BG)}"/>']

    # the network runs across the whole wrap: faint on the back, brighter on the spine, full on the front
    lattice(svg, -4, front_x - 8, top - 6, top + 74, 7, 26, 0.38, 7)
    lattice(svg, front_x - 10, W + 4, top - 6, top + 110, 10, 15, 1.0, 11, highlight=10, start=2)

    # fine baseline grid on the lower front, like an embedding space seen edge-on
    for k in range(9):
        yy = top + 150 + k * 3.1
        col = mix(BG, DIM, 0.5 + 0.06 * k)
        svg.append(f'<line x1="{front_x + SAFE}" y1="{yy:.2f}" x2="{front_x + TRIM_W - SAFE}" y2="{yy:.2f}" stroke="{hexc(col)}" stroke-width="0.18"/>')

    fx = front_x + 15
    # front: title block
    svg.append(f'<text x="{fx - 0.8}" y="{top + 136}" font-family="InterD" font-weight="300" font-size="15.2" letter-spacing="-0.3" fill="{INK}">Understanding</text>')
    svg.append(f'<text x="{fx - 2.2}" y="{top + 176}" font-family="InterD" font-weight="700" font-size="42" letter-spacing="-0.6" fill="{INK}">AI</text>')
    svg.append(f'<text x="{fx}" y="{top + 186}" font-family="EBG" font-style="italic" font-size="6.0" fill="{INK}">Technology, Trends and the Decade Ahead</text>')
    svg.append(f'<text x="{fx}" y="{top + 196.5}" font-family="Inter" font-weight="500" font-size="3.6" letter-spacing="0.45" fill="{INK}">JAN GÖBEL</text>')

    # spine: title and author, reading top to bottom (English convention)
    cx = spine_x + S / 2
    svg.append(f'<g transform="translate({cx:.2f} {top + 18}) rotate(90)">'
               f'<text x="0" y="{2.95:.2f}" font-family="InterD" font-weight="300" font-size="8.2" fill="{INK}">Understanding <tspan font-weight="700">AI</tspan></text>'
               f'<text x="62" y="{1.6:.2f}" font-family="EBG" font-style="italic" font-size="4.6" fill="{SOFT}">Technology, Trends and the Decade Ahead</text>'
               f'<text x="{TRIM_H - 36 - 22}" y="{1.4:.2f}" font-family="Inter" font-weight="500" font-size="3.6" letter-spacing="0.4" fill="{INK}">JAN GÖBEL</text>'
               f'</g>')
    for rad, k in ((2.4, 0.8), (1.5, 0.45), (0.95, 0.0)):
        svg.append(f'<circle cx="{cx:.2f}" cy="{top + 10}" r="{rad}" fill="{hexc(mix(AMBER, BG, k))}"/>')

    # back: headline and blurb
    bx = back_x + 15
    svg.append(f'<text x="{bx}" y="{top + 24}" font-family="JBM" font-size="2.7" letter-spacing="0.3" fill="{hexc(CYAN)}">HOW IT WORKS · WHAT IT CHANGES · WHAT COMES NEXT</text>')
    head = ["What AI is, how it works,", "and what the evidence says", "about where it is going."]
    for i, ln in enumerate(head):
        svg.append(f'<text x="{bx}" y="{top + 52 + i * 8.6:.1f}" font-family="InterD" font-weight="600" font-size="7.4" letter-spacing="-0.1" fill="{INK}">{ln}</text>')
    blurb = [
        ('Artificial intelligence is discussed everywhere and explained almost', 0),
        ('nowhere. This book starts with the mechanisms: how a neural network', 0),
        ('learns, how a large language model turns text into predictions, why', 0),
        ('scale has driven progress and where it may stop. It then follows', 0),
        ('the technology into the world: agents, science, chips and energy,', 0),
        ('work and the economy, media and democracy, education and health,', 0),
        ('risk, safety and law.', 1),
        ('Worked examples take the reader through backpropagation and', 0),
        ('convolution, tokenisation, embeddings, attention and the transformer,', 0),
        ('and the training stages that turn a text predictor into an assistant', 0),
        ('or a reasoning model. Later chapters weigh the evidence on productivity', 0),
        ('and jobs, elections, classrooms and clinics, explain alignment,', 0),
        ('interpretability and evaluation, compare the law in the EU, the US,', 0),
        ('China and the UK, and close with scenarios for the next ten years.', 0),
    ]
    y = top + 88
    for ln, gap in blurb:
        svg.append(f'<text x="{bx}" y="{y:.1f}" font-family="EBG" font-size="3.95" fill="{INK}">{ln}</text>')
        y += 5.05 + (2.6 if gap else 0)
    # barcode field: white box, bottom right of the back, inside the safe zone
    bw, bh = 46.0, 27.0
    bxx = spine_x - SAFE - bw
    byy = top + TRIM_H - SAFE - bh
    svg.append(f'<rect x="{bxx}" y="{byy}" width="{bw}" height="{bh}" fill="#FFFFFF"/>')
    if isbn:
        ean13(svg, isbn, bxx + 3, byy + 6.5, bw - 6, bh - 10)
    else:
        svg.append(f'<text x="{bxx + bw / 2}" y="{byy + bh / 2 - 1}" font-family="Inter" font-size="2.6" fill="#666" text-anchor="middle">ISBN barcode</text>')
        svg.append(f'<text x="{bxx + bw / 2}" y="{byy + bh / 2 + 3}" font-family="Inter" font-size="2.2" fill="#999" text-anchor="middle">place BoD EAN-13 here</text>')

    if guides:
        g = 'stroke-width="0.25" fill="none"'
        svg.append(f'<rect x="{BLEED}" y="{BLEED}" width="{W - 2 * BLEED}" height="{TRIM_H}" stroke="#FF2A6D" {g}/>')
        for xx in (spine_x, front_x):
            svg.append(f'<line x1="{xx}" y1="0" x2="{xx}" y2="{H}" stroke="#FF2A6D" stroke-width="0.25" stroke-dasharray="2 1"/>')
        for x0 in (back_x, front_x):
            svg.append(f'<rect x="{x0 + SAFE}" y="{top + SAFE}" width="{TRIM_W - 2 * SAFE}" height="{TRIM_H - 2 * SAFE}" stroke="#00E5FF" {g} stroke-dasharray="1 1"/>')
        svg.append(f'<rect x="{spine_x + SPINE_SAFE}" y="{top + SAFE}" width="{S - 2 * SPINE_SAFE}" height="{TRIM_H - 2 * SAFE}" stroke="#00E5FF" {g} stroke-dasharray="1 1"/>')
        svg.append(f'<text x="{W / 2}" y="3.2" font-family="JBM" font-size="2.4" fill="#FF2A6D" text-anchor="middle">'
                   f'sheet {W:.1f} x {H:.1f} mm · spine {S:.2f} mm · bleed {BLEED:.0f} mm · red = trim/folds · cyan = safe zone</text>')
    svg.append("</svg>")

    fonts = os.path.join(PRINT, "fonts")
    css = f"""
@font-face {{ font-family: InterD; src: url({fonts}/InterDisplay-Light.otf); font-weight: 300; }}
@font-face {{ font-family: InterD; src: url({fonts}/InterDisplay-SemiBold.otf); font-weight: 600; }}
@font-face {{ font-family: InterD; src: url({fonts}/InterDisplay-Bold.otf); font-weight: 700; }}
@font-face {{ font-family: Inter; src: url({fonts}/Inter-Regular.otf); font-weight: 400; }}
@font-face {{ font-family: Inter; src: url({fonts}/Inter-Medium.otf); font-weight: 500; }}
@font-face {{ font-family: JBM; src: url({fonts}/JetBrainsMono-Regular.ttf); }}
@font-face {{ font-family: EBG; src: url({fonts}/EBGaramond-Regular.ttf); font-style: normal; }}
@font-face {{ font-family: EBG; src: url({fonts}/EBGaramond-RegularItalic.ttf); font-style: italic; }}
@page {{ size: {W}mm {H}mm; margin: 0; }}
html, body {{ margin: 0; padding: 0; }}
svg {{ display: block; }}
"""
    doc = f"<!doctype html><html><head><meta charset='utf-8'><title>Understanding AI – cover</title><style>{css}</style></head><body>{''.join(svg)}</body></html>"
    from weasyprint import HTML
    name = "understanding-ai_cover_A5_PB" + ("_guides" if guides else "")
    out = os.path.join(TB, "delivery", name + ".pdf")
    HTML(string=doc, base_url=PRINT).write_pdf(out, pdf_variant="pdf/x-4", output_intent="srgb")
    # mark the trim inside the 5 mm bleed so preflight tools see the finished size
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject
    pt = 72 / 25.4
    w = PdfWriter(clone_from=PdfReader(out))
    pg = w.pages[0]
    pg.bleedbox = RectangleObject([0, 0, W * pt, H * pt])
    pg.trimbox = RectangleObject([BLEED * pt, BLEED * pt, (W - BLEED) * pt, (H - BLEED) * pt])
    pg.artbox = pg.trimbox
    w.pdf_header = b"%PDF-1.6"
    with open(out, "wb") as f:
        w.write(f)
    print(f"{out}: {W:.1f} x {H:.1f} mm (spine {S:.2f} mm, {pages} pages, paper {paper})")
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--pages", type=int, default=590)
    ap.add_argument("--paper", default="weiss", choices=sorted(PAPER))
    ap.add_argument("--spine-mm", type=float, help="cover spine width from myBoD (overrides the calculation)")
    ap.add_argument("--isbn", default=os.environ.get("BOOK_ISBN"), help="ISBN-13; draws the EAN-13 barcode")
    a = ap.parse_args()
    for guides in (False, True):
        build(a.pages, a.paper, a.spine_mm, a.isbn, guides)
