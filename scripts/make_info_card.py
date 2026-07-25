"""
Modern GitHub Neofetch Info Card
Generates info-card.svg
"""

import html
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "info-card.svg")
STATIC = bool(os.environ.get("STATIC"))

# --------------------------
# Card
# --------------------------
W = 520
H = 390

PAD = 22
TITLEBAR_H = 34
KEY_X = PAD
VAL_X = PAD + 105
LINE_H = 22

# --------------------------
# Colors (GitHub Dark)
# --------------------------
BG = "#0d1117"
BG2 = "#161b22"
FRAME = "#30363d"

TEXT = "#c9d1d9"
MUTED = "#8b949e"

KEY = "#ffa657"
SECTION = "#58a6ff"

GREEN = "#3fb950"
CYAN = "#39d0ff"
PURPLE = "#d2a8ff"

# --------------------------
# Content
# --------------------------

ROWS = [
    ("host",),

    ("kv", "Name", "Moanish Chowdary"),
    ("kv", "Role", "B.Tech CSE (3rd Year) @ Sreenidhi University"),
    ("kv", "Focus", "Full-Stack Development • AI/ML"),
    ("kv", "Seeking", "Software Engineering Internships"),

    ("gap"),

    ("sec", "Tech Stack"),

    ("kv", "Languages", "Java • Python • C++ • JavaScript"),
    ("kv", "Frontend", "React • HTML • CSS"),
    ("kv", "Backend", "Spring Boot • FastAPI • Node.js"),
    ("kv", "Database", "MySQL • PostgreSQL"),
    ("kv", "AI/ML", "TensorFlow • OpenCV • Scikit-learn"),
    ("kv", "Tools", "Git • GitHub • Docker • Linux"),
]

# --------------------------

def esc(s):
    return html.escape(s)

def rise(inner, index):
    if STATIC:
        return f"<g>{inner}</g>"

    delay = 0.18 + index * 0.06

    return f"""
<g opacity="0" transform="translate(0,6)">
{inner}
<animate attributeName="opacity"
from="0" to="1"
begin="{delay:.2f}s"
dur="0.45s"
fill="freeze"/>

<animateTransform
attributeName="transform"
type="translate"
from="0 6"
to="0 0"
begin="{delay:.2f}s"
dur="0.45s"
fill="freeze"
calcMode="spline"
keySplines="0.2 0.8 0.2 1"/>
</g>
"""

parts = []

parts.append(f"""
<svg
xmlns="http://www.w3.org/2000/svg"
width="{W}"
height="{H}"
viewBox="0 0 {W} {H}"
font-family="JetBrains Mono, Cascadia Code, Consolas, monospace">

<defs>

<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
<stop offset="0%" stop-color="{BG2}"/>
<stop offset="100%" stop-color="{BG}"/>
</linearGradient>

<filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
<feDropShadow
dx="0"
dy="8"
stdDeviation="10"
flood-color="#000"
flood-opacity="0.35"/>
</filter>

</defs>

<rect
x="8"
y="8"
rx="14"
width="{W-16}"
height="{H-16}"
fill="url(#bg)"
stroke="{FRAME}"
filter="url(#shadow)"/>

<line
x1="8"
y1="{TITLEBAR_H+8}"
x2="{W-8}"
y2="{TITLEBAR_H+8}"
stroke="{FRAME}"/>
""")

# Window buttons

buttons = ["#ff5f56", "#ffbd2e", "#27c93f"]

for i, color in enumerate(buttons):
    cx = PAD + i * 18
    cy = TITLEBAR_H / 2 + 8
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="5" fill="{color}"/>')

parts.append(f"""
<text
x="{W/2}"
y="{TITLEBAR_H/2+13}"
fill="{MUTED}"
font-size="12"
text-anchor="middle">

moanishkoya@github: ~$ neofetch

</text>
""")

y = TITLEBAR_H + 40

for idx, row in enumerate(ROWS):

    kind = row[0]

    if kind == "gap":
        y += LINE_H * 0.6
        continue

    if kind == "host":

        inner = f"""
<text
x="{KEY_X}"
y="{y}"
font-size="15"
font-weight="700">

<tspan fill="{GREEN}">moanishkoya</tspan>
<tspan fill="{MUTED}">@</tspan>
<tspan fill="{CYAN}">github</tspan>

</text>

<line
x1="{KEY_X+120}"
y1="{y-5}"
x2="{W-PAD}"
y2="{y-5}"
stroke="{FRAME}"/>
"""

    elif kind == "sec":

        title = esc(row[1])

        inner = f"""
<text
x="{KEY_X}"
y="{y}"
fill="{SECTION}"
font-size="13"
font-weight="700">

❯ {title}

</text>

<line
x1="{KEY_X+95}"
y1="{y-5}"
x2="{W-PAD}"
y2="{y-5}"
stroke="{FRAME}"/>
"""

    elif kind == "kv":

        key = esc(row[1])
        val = esc(row[2])

        inner = f"""
<text
x="{KEY_X}"
y="{y}"
fill="{KEY}"
font-size="12.8"
font-weight="700">

{key}

</text>

<text
x="{VAL_X}"
y="{y}"
fill="{TEXT}"
font-size="12.8">

{val}

</text>
"""

    elif kind == "bul":

        txt = esc(row[1])

        inner = f"""
<circle
cx="{KEY_X+4}"
cy="{y-4}"
r="2.7"
fill="{GREEN}"/>

<text
x="{KEY_X+16}"
y="{y}"
fill="{TEXT}"
font-size="12.8">

{txt}

</text>
"""

    else:
        continue

    parts.append(rise(inner, idx))
    y += LINE_H

parts.append("</svg>")

svg = "".join(parts)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)

print(f"Generated {OUT}")