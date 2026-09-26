#!/usr/bin/env python3
"""Avatares padrão bear2me para quem ainda não tem foto: o urso da logo.

Composição da própria logo: urso escuro, focinho branco, chamas escuras atrás,
gradiente quente. O urso é sempre o mesmo; variam só pose e expressão.
Nada de acessório humano: o avatar representa a comunidade, não a pessoa.

Regras herdadas dos ícones de categoria: cantos retos, gradiente vertical,
chamas translúcidas no topo, detalhes em branco translúcido.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent
W = "#FFFFFF"

# slug, pose, cor topo, cor base (tons tirados do gradiente do urso e do logotipo)
AVATARS = [
    ("brasa",     "De frente",   "#EE5A45", "#9A1E1E"),
    ("laranja",   "Acenando",    "#F79545", "#B84A17"),
    ("ambar",     "Piscando",    "#F4B846", "#B26A0C"),
    ("mel",       "Curioso",     "#D8A150", "#87521A"),
    ("urso",      "Dormindo",    "#A86A3E", "#4E2C16"),
    ("terracota", "Olhando",     "#CF6444", "#6E2A1C"),
    ("vinho",     "Feliz",       "#B8475A", "#5A1A29"),
    ("grafite",   "Surpreso",    "#7A6A60", "#2E2724"),
]


def darken(hex_, k=0.38):
    r, g, b = (int(hex_[i:i + 2], 16) for i in (1, 3, 5))
    return "#%02X%02X%02X" % tuple(round(c * (1 - k)) for c in (r, g, b))


def st(w, color, op=None):
    o = f' stroke-opacity="{op}"' if op else ""
    return (f'fill="none" stroke="{color}" stroke-width="{w}"{o} '
            f'stroke-linecap="round" stroke-linejoin="round"')


def eyes(kind, dx=0):
    l, r, y = 41.5 + dx, 58.5 + dx, 47
    if kind == "open":
        return (f'<ellipse cx="{l}" cy="{y}" rx="1.6" ry="2.3" fill="{W}"/>'
                f'<ellipse cx="{r}" cy="{y}" rx="1.6" ry="2.3" fill="{W}"/>')
    if kind == "big":
        return (f'<ellipse cx="{l}" cy="{y-.5}" rx="2.3" ry="3" fill="{W}"/>'
                f'<ellipse cx="{r}" cy="{y-.5}" rx="2.3" ry="3" fill="{W}"/>')
    if kind == "wink":
        return (f'<ellipse cx="{l}" cy="{y}" rx="1.6" ry="2.3" fill="{W}"/>'
                f'<path d="M{r-3} {y+.5} Q{r} {y-2.5} {r+3} {y+.5}" {st(1.8, W)}/>')
    if kind == "closed":
        return (f'<path d="M{l-3} {y-.5} Q{l} {y+2.5} {l+3} {y-.5}" {st(1.8, W)}/>'
                f'<path d="M{r-3} {y-.5} Q{r} {y+2.5} {r+3} {y-.5}" {st(1.8, W)}/>')
    if kind == "happy":
        return (f'<path d="M{l-3} {y+1} Q{l} {y-3} {l+3} {y+1}" {st(1.8, W)}/>'
                f'<path d="M{r-3} {y+1} Q{r} {y-3} {r+3} {y+1}" {st(1.8, W)}/>')
    raise ValueError(kind)


def mouth(kind, dark, dx=0):
    x = 50 + dx
    if kind == "smile":
        return f'<path d="M{x} 59.5 V61 M{x-3.5} 61.5 Q{x} 64.5 {x+3.5} 61.5" {st(1.3, dark)}/>'
    if kind == "open":
        return (f'<path d="M{x} 59.5 V61" {st(1.3, dark)}/>'
                f'<path d="M{x-4} 61.2 Q{x} 68 {x+4} 61.2 Z" fill="{dark}"/>')
    if kind == "o":
        return f'<path d="M{x} 59.5 V61" {st(1.3, dark)}/><ellipse cx="{x}" cy="63.2" rx="1.8" ry="2.2" fill="{dark}"/>'
    if kind == "flat":
        return f'<path d="M{x} 59.5 V61 M{x-2.5} 62 H{x+2.5}" {st(1.3, dark)}/>'
    raise ValueError(kind)


def bear(bottom, eye="open", mth="smile", tilt=0, look=0, extra=""):
    b = darken(bottom)           # urso um tom abaixo da base do fundo
    dx = look
    head = f'''
    <circle cx="{31+dx*.4}" cy="33" r="8.5" fill="{b}"/><circle cx="{69+dx*.4}" cy="33" r="8.5" fill="{b}"/>
    <circle cx="{31+dx*.4}" cy="33" r="4.3" fill="{W}" fill-opacity=".3"/><circle cx="{69+dx*.4}" cy="33" r="4.3" fill="{W}" fill-opacity=".3"/>
    <ellipse cx="50" cy="50" rx="22.5" ry="20.5" fill="{b}"/>
    {eyes(eye, dx*.6)}
    <path d="M{40+dx} 56 C{40+dx} 50 {60+dx} 50 {60+dx} 56 C{60+dx} 63 {55+dx} 67.5 {50+dx} 67.5 C{45+dx} 67.5 {40+dx} 63 {40+dx} 56 Z" fill="{W}"/>
    <path d="M{45.5+dx} 54 Q{50+dx} 52.3 {54.5+dx} 54 Q{54+dx} 57.6 {50+dx} 59.6 Q{46+dx} 57.6 {45.5+dx} 54 Z" fill="{b}"/>
    {mouth(mth, b, dx)}'''
    return f'''
  <path d="M14 100 V89 Q14 71 50 69 Q86 71 86 89 V100 Z" fill="{b}"/>
  {extra}
  <g transform="rotate({tilt} 50 62)">{head}</g>'''


def wave_paw(bottom):
    b = darken(bottom)
    return f'''
  <path d="M72 84 Q78 70 77 56" {st(10, b)}/>
  <circle cx="77" cy="52" r="7.5" fill="{b}"/>
  <ellipse cx="77" cy="54" rx="3.3" ry="2.7" fill="{W}" fill-opacity=".45"/>
  <circle cx="73" cy="48.5" r="1.5" fill="{W}" fill-opacity=".45"/><circle cx="77" cy="47" r="1.5" fill="{W}" fill-opacity=".45"/>
  <circle cx="81" cy="48.5" r="1.5" fill="{W}" fill-opacity=".45"/>
  <path d="M86 44 Q89.5 50 86 56 M89.5 40 Q95 50 89.5 60" {st(1.8, W, ".55")}/>'''


ZZ = (f'<path d="M77 16 H85 L77 24 H85" {st(2.5, W, ".65")}/>'
      f'<path d="M88 7 H93 L88 12 H93" {st(2, W, ".55")}/>')

SPARK = f'<path d="M86 14 L87.4 18.6 L92 20 L87.4 21.4 L86 26 L84.6 21.4 L80 20 L84.6 18.6 Z" fill="{W}" fill-opacity=".7"/>'
HEART = f'<path transform="translate(5 -6)" d="M78 30 C74 26 74 21 78 21 C80 21 80.5 23 80.5 23 C80.5 23 81 21 83 21 C87 21 87 26 83 30 L80.5 32.5 Z" fill="{W}" fill-opacity=".7"/>'

POSE = {
    "brasa":     lambda d: bear(d),
    "laranja":   lambda d: bear(d, mth="open", tilt=-6, extra=wave_paw(d)),
    "ambar":     lambda d: bear(d, eye="wink", tilt=5),
    "mel":       lambda d: bear(d, eye="big", mth="flat", tilt=-14),
    "urso":      lambda d: bear(d, eye="closed", mth="flat", tilt=8) + ZZ,
    "terracota": lambda d: bear(d, look=5),
    "vinho":     lambda d: bear(d, eye="happy", mth="open") + HEART,
    "grafite":   lambda d: bear(d, eye="big", mth="o", tilt=4) + SPARK,
}


def tile(slug, top, bottom):
    return f'''
  <defs>
    <linearGradient id="av-{slug}-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/>
    </linearGradient>
    <clipPath id="av-{slug}-card"><rect width="100" height="100"/></clipPath>
  </defs>
  <g clip-path="url(#av-{slug}-card)">
    <rect width="100" height="100" fill="url(#av-{slug}-bg)"/>
    <path d="M6 0 C4 12 10 20 20 26 C14 16 18 8 26 0 Z M66 0 C62 10 68 18 80 24 C74 14 78 6 86 0 Z"
          fill="#000" fill-opacity=".1"/>
    {POSE[slug](bottom)}
  </g>'''


def avatar_svg(slug, top, bottom, size=512):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">'
            f'{tile(slug, top, bottom)}\n</svg>\n')


def grid_svg():
    """Prévia 4x2 com a faixa do nome como no app."""
    cell, gap, pad = 100, 10, 24
    cols, rows = 4, 2
    names = ["Marcos", "Rafa", "Tiago", "Beto", "Urso_SP", "Caio", "Léo", "Dudu"]
    w = pad * 2 + cols * cell + (cols - 1) * gap
    h = pad * 2 + rows * cell + (rows - 1) * gap
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w*4}" height="{h*4}" viewBox="0 0 {w} {h}">',
             f'<rect width="{w}" height="{h}" fill="#F5F2ED"/>']
    for i, (slug, _, top, bottom) in enumerate(AVATARS):
        x = pad + (i % cols) * (cell + gap)
        y = pad + (i // cols) * (cell + gap)
        parts.append(f'<g transform="translate({x} {y})">{tile(slug, top, bottom)}'
                     f'<rect x="4" y="83" width="92" height="13" fill="#3A3634" fill-opacity=".82"/>'
                     f'<text x="8" y="92.3" font-family="Quicksand, Helvetica, Arial, sans-serif" '
                     f'font-size="7.5" font-weight="700" fill="#FFFFFF">{names[i]}</text></g>')
    parts.append('</svg>')
    return "\n".join(parts)


if __name__ == "__main__":
    for i, (slug, _, top, bottom) in enumerate(AVATARS, 1):
        (OUT / "svg" / f"{i:02d}-{slug}.svg").write_text(avatar_svg(slug, top, bottom))
    (OUT / "grid.svg").write_text(grid_svg())
    print("ok")
