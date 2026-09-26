#!/usr/bin/env python3
"""Avatares padrão bear2me para quem ainda não tem foto: parentes da logo.

O urso é o da logo (silhueta cabeça+corpo, gradiente marrom -> cinza, focinho
claro, nariz escuro, chamas escuras atrás). Para PROTEGER a logo, o avatar
nunca é idêntico a ela:
  - formato quadrado com cantos retos (o círculo com borda é exclusivo da logo)
  - 8 gradientes de fundo quentes, nenhum igual ao vermelho -> amarelo oficial
  - só os olhos variam, de leve
Assim um perfil sem foto nunca se passa pela conta oficial da marca.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent
W = "#FFFFFF"

# slug, expressão, 3 paradas do gradiente (topo, meio, base)
AVATARS = [
    ("por-do-sol", "Olhar da logo", ("#D93A4A", "#EE6A3C", "#F4A340")),
    ("ambar",      "Piscando",      ("#F07A2E", "#F5A23A", "#F8CB4A")),
    ("brasa",      "Feliz",         ("#C2303A", "#DC4E32", "#EE7E38")),
    ("mel",        "Olhando à esquerda", ("#E39440", "#EDB34E", "#F3D06E")),
    ("vinho",      "Dormindo",      ("#B23A5A", "#CF4E55", "#EA7C5C")),
    ("terracota",  "Olhando à direita", ("#C25A3E", "#D8804C", "#E8AA68")),
    ("rosa",       "Curioso",       ("#DE4A72", "#EF716A", "#F5A26C")),
    ("crepusculo", "Sereno",        ("#8C4A74", "#B9505A", "#E88E52")),
]

# Cores do urso, tiradas da logo
BEAR_TOP, BEAR_MID, BEAR_BOT = "#B24A1C", "#7E4A2C", "#4A4745"
MUZZLE_TOP, MUZZLE_BOT = "#FFFFFF", "#CFCFD1"
NOSE = "#2E2B2A"
FLAME = "#3A2217"


def st(w, color, op=None):
    o = f' stroke-opacity="{op}"' if op else ""
    return (f'fill="none" stroke="{color}" stroke-width="{w}"{o} '
            f'stroke-linecap="round" stroke-linejoin="round"')


def eyes(kind):
    l, r, y = 43, 57, 47.5
    if kind == "open":
        return (f'<ellipse cx="{l}" cy="{y}" rx="1.35" ry="2.1" fill="{W}"/>'
                f'<ellipse cx="{r}" cy="{y}" rx="1.35" ry="2.1" fill="{W}"/>')
    if kind == "left":
        return (f'<ellipse cx="{l-1.2}" cy="{y}" rx="1.35" ry="2.1" fill="{W}"/>'
                f'<ellipse cx="{r-1.2}" cy="{y}" rx="1.35" ry="2.1" fill="{W}"/>')
    if kind == "right":
        return (f'<ellipse cx="{l+1.2}" cy="{y}" rx="1.35" ry="2.1" fill="{W}"/>'
                f'<ellipse cx="{r+1.2}" cy="{y}" rx="1.35" ry="2.1" fill="{W}"/>')
    if kind == "wink":
        return (f'<ellipse cx="{l}" cy="{y}" rx="1.35" ry="2.1" fill="{W}"/>'
                f'<path d="M{r-2.4} {y+.4} Q{r} {y-2} {r+2.4} {y+.4}" {st(1.4, W)}/>')
    if kind == "happy":
        return (f'<path d="M{l-2.4} {y+.8} Q{l} {y-2.2} {l+2.4} {y+.8}" {st(1.4, W)}/>'
                f'<path d="M{r-2.4} {y+.8} Q{r} {y-2.2} {r+2.4} {y+.8}" {st(1.4, W)}/>')
    if kind == "closed":
        return (f'<path d="M{l-2.4} {y-.4} Q{l} {y+1.8} {l+2.4} {y-.4}" {st(1.4, W)}/>'
                f'<path d="M{r-2.4} {y-.4} Q{r} {y+1.8} {r+2.4} {y-.4}" {st(1.4, W)}/>')
    if kind == "calm":   # olhos semicerrados, tranquilo
        return (f'<path d="M{l-2} {y} H{l+2}" {st(1.5, W)}/>'
                f'<path d="M{r-2} {y} H{r+2}" {st(1.5, W)}/>')
    if kind == "big":
        return (f'<ellipse cx="{l}" cy="{y-.3}" rx="1.8" ry="2.6" fill="{W}"/>'
                f'<ellipse cx="{r}" cy="{y-.3}" rx="1.8" ry="2.6" fill="{W}"/>')
    raise ValueError(kind)


EYES = {"por-do-sol": "open", "ambar": "wink", "brasa": "happy", "mel": "left",
        "vinho": "closed", "terracota": "right", "rosa": "big", "crepusculo": "calm"}


def bear(slug):
    b = f"av-{slug}"
    return f'''
  <defs>
    <linearGradient id="{b}-bear" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{BEAR_TOP}"/><stop offset=".45" stop-color="{BEAR_MID}"/>
      <stop offset="1" stop-color="{BEAR_BOT}"/>
    </linearGradient>
    <linearGradient id="{b}-muz" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{MUZZLE_TOP}"/><stop offset="1" stop-color="{MUZZLE_BOT}"/>
    </linearGradient>
  </defs>
  <g fill="{FLAME}" fill-opacity=".34">
    <path d="M28 90 C8 66 8 32 28 8 C26 22 31 30 35 38 C32 50 30 70 29 90 Z"/>
    <path d="M47 34 C47 20 56 8 70 0 C66 12 69 20 67 34 Z"/>
    <path d="M73 84 C70 58 80 36 97 26 C90 38 85 56 77 86 Z"/>
  </g>
  <circle cx="30.5" cy="35" r="7.5" fill="{BEAR_TOP}"/>
  <circle cx="69.5" cy="35" r="7.5" fill="{BEAR_TOP}"/>
  <path d="M24 100 C25.5 82 27.5 66 28.5 53 C29 41 32 35 40 33.5 H60 C68 35 71 41 71.5 53 C72.5 66 74.5 82 76 100 Z"
        fill="url(#{b}-bear)"/>
  {eyes(EYES[slug])}
  <path d="M41.5 58 C41.5 52.5 45 50.5 50 50.5 C55 50.5 58.5 52.5 58.5 58 V63.5 C58.5 67.5 55.5 70 50 70 C44.5 70 41.5 67.5 41.5 63.5 Z"
        fill="url(#{b}-muz)"/>
  <path d="M45.6 56.2 Q50 54.3 54.4 56.2 Q54.6 59.4 50 62 Q45.4 59.4 45.6 56.2 Z" fill="{NOSE}"/>'''


def tile(slug, stops):
    t, m, b = stops
    return f'''
  <defs>
    <linearGradient id="av-{slug}-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{t}"/><stop offset=".5" stop-color="{m}"/><stop offset="1" stop-color="{b}"/>
    </linearGradient>
    <clipPath id="av-{slug}-card"><rect width="100" height="100"/></clipPath>
  </defs>
  <g clip-path="url(#av-{slug}-card)">
    <rect width="100" height="100" fill="url(#av-{slug}-bg)"/>
    {bear(slug)}
  </g>'''


def avatar_svg(slug, stops, size=512):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">'
            f'{tile(slug, stops)}\n</svg>\n')


def grid_svg():
    """Prévia 4x2 com a faixa do nome como no app."""
    cell, gap, pad = 100, 10, 24
    cols, rows = 4, 2
    names = ["Marcos", "Rafa", "Tiago", "Beto", "Urso_SP", "Caio", "Léo", "Dudu"]
    w = pad * 2 + cols * cell + (cols - 1) * gap
    h = pad * 2 + rows * cell + (rows - 1) * gap
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w*4}" height="{h*4}" viewBox="0 0 {w} {h}">',
             f'<rect width="{w}" height="{h}" fill="#F5F2ED"/>']
    for i, (slug, _, stops) in enumerate(AVATARS):
        x = pad + (i % cols) * (cell + gap)
        y = pad + (i // cols) * (cell + gap)
        parts.append(f'<g transform="translate({x} {y})">{tile(slug, stops)}'
                     f'<rect x="4" y="83" width="92" height="13" fill="#3A3634" fill-opacity=".82"/>'
                     f'<text x="8" y="92.3" font-family="Quicksand, Helvetica, Arial, sans-serif" '
                     f'font-size="7.5" font-weight="700" fill="#FFFFFF">{names[i]}</text></g>')
    parts.append('</svg>')
    return "\n".join(parts)


if __name__ == "__main__":
    for f in (OUT / "svg").glob("*.svg"):
        f.unlink()
    for f in (OUT / "png").glob("*.png"):
        f.unlink()
    for i, (slug, _, stops) in enumerate(AVATARS, 1):
        (OUT / "svg" / f"{i:02d}-{slug}.svg").write_text(avatar_svg(slug, stops))
    (OUT / "grid.svg").write_text(grid_svg())
    print("ok")
