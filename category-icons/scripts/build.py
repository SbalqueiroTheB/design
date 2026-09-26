#!/usr/bin/env python3
"""Gera os 8 ícones de categoria (SVG) + a grade de preview.

Grid interno de 100x100; pictograma branco dentro da área segura 14..86.
Estilo: flat, cantos retos (miter/butt), sem sombra, sem gradiente.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent
W = "#FFFFFF"
S = 5  # espessura de traço padrão

# Ordem e cores inspiradas na bandeira do orgulho (ajustadas p/ contraste)
ICONS = [
    ("bares",          "Bares",          "#E40303"),
    ("discoteca",      "Discoteca",      "#FF8C00"),
    ("sauna",          "Sauna",          "#004DFF"),
    ("cruising",       "Cruising",       "#008026"),
    ("comer-e-beber",  "Comer e beber",  "#D9A400"),
    ("ao-ar-livre",    "Ao ar livre",    "#750787"),
    ("estilo-de-vida", "Estilo de vida", "#B0105E"),
    ("alojamento",     "Alojamento",     "#C2410C"),
]

stroke = f'fill="none" stroke="{W}" stroke-width="{S}" stroke-linejoin="miter" stroke-linecap="butt"'


def bares(bg):
    return f'''
  <path d="M26 24 H74 L50 50 Z" {stroke}/>
  <path d="M34 31 H66 L50 48 Z" fill="{W}"/>
  <line x1="50" y1="50" x2="50" y2="74" {stroke}/>
  <rect x="35" y="72" width="30" height="5" fill="{W}"/>
  <line x1="57" y1="38" x2="71" y2="14" stroke="{W}" stroke-width="3.5"/>
  <circle cx="69" cy="17" r="4.5" fill="{W}"/>'''


def discoteca(bg):
    return f'''
  <defs><clipPath id="ball"><circle cx="50" cy="56" r="24"/></clipPath></defs>
  <line x1="50" y1="12" x2="50" y2="32" {stroke}/>
  <circle cx="50" cy="56" r="24" fill="{W}"/>
  <g clip-path="url(#ball)" stroke="{bg}" stroke-width="2.6">
    <line x1="20" y1="44" x2="80" y2="44"/><line x1="20" y1="56" x2="80" y2="56"/>
    <line x1="20" y1="68" x2="80" y2="68"/>
    <line x1="38" y1="28" x2="38" y2="84"/><line x1="50" y1="28" x2="50" y2="84"/>
    <line x1="62" y1="28" x2="62" y2="84"/>
  </g>
  <path d="M80 18 L82 24 L88 26 L82 28 L80 34 L78 28 L72 26 L78 24 Z" fill="{W}"/>
  <path d="M19 30 L20.3 34 L24 35.3 L20.3 36.6 L19 40.6 L17.7 36.6 L14 35.3 L17.7 34 Z" fill="{W}"/>'''


def sauna(bg):
    wave = lambda x: (f'<path d="M{x} 62 C{x-8} 55 {x+8} 49 {x} 42 C{x-8} 35 {x+8} 29 {x} 22" '
                      f'fill="none" stroke="{W}" stroke-width="{S}" stroke-linecap="butt"/>')
    return f'''
  {wave(36)}
  {wave(50)}
  {wave(64)}
  <rect x="20" y="68" width="60" height="6" fill="{W}"/>
  <rect x="26" y="74" width="6" height="12" fill="{W}"/>
  <rect x="68" y="74" width="6" height="12" fill="{W}"/>'''


def cruising(bg):
    return f'''
  <rect x="30" y="16" width="44" height="68" {stroke}/>
  <path d="M27.5 13.5 L46 20 V80 L27.5 86.5 Z" fill="{W}"/>
  <circle cx="41" cy="52" r="1.8" fill="{bg}"/>
  <circle cx="60" cy="37" r="8" fill="{W}"/>
  <path d="M49 84 V56 L53 50 H67.5 L71.5 56 V84 Z" fill="{W}"/>'''


def comer_e_beber(bg):
    return f'''
  <circle cx="50" cy="52" r="19" {stroke}/>
  <circle cx="50" cy="52" r="10" fill="none" stroke="{W}" stroke-width="3"/>
  <path d="M16 20 V36 H28 V20" fill="none" stroke="{W}" stroke-width="3.5"/>
  <line x1="22" y1="20" x2="22" y2="36" stroke="{W}" stroke-width="3.5"/>
  <rect x="19.5" y="34" width="5" height="50" fill="{W}"/>
  <path d="M75 18 L84 28 V52 H75 Z" fill="{W}"/>
  <rect x="75" y="50" width="5" height="34" fill="{W}"/>'''


def ao_ar_livre(bg):
    return f'''
  <circle cx="78" cy="30" r="8" fill="{W}"/>
  <path d="M34 74 Q36 54 46 36" fill="none" stroke="{W}" stroke-width="{S}"/>
  <path d="M46 36 Q34 24 16 32 Q32 30 46 36 Z" fill="{W}"/>
  <path d="M46 36 Q40 18 26 16 Q38 24 46 36 Z" fill="{W}"/>
  <path d="M46 36 Q54 20 66 18 Q56 26 46 36 Z" fill="{W}"/>
  <path d="M46 36 Q62 34 68 50 Q58 38 46 36 Z" fill="{W}"/>
  <path d="M46 36 Q30 38 24 52 Q34 40 46 36 Z" fill="{W}"/>
  <path d="M14 76 Q34 66 60 74 L60 76 Z" fill="{W}"/>
  <path d="M14 86 q6 -5 12 0 t12 0 t12 0 t12 0 t12 0 t12 0" fill="none" stroke="{W}" stroke-width="4"/>'''


def estilo_de_vida(bg):
    # Haltere em cima; sacola (esq.) e pente (dir.) embaixo
    teeth = "".join(f'<rect x="{x}" y="58" width="2.4" height="18" fill="{W}"/>'
                    for x in range(58, 86, 5))
    return f'''
  <rect x="30" y="19.5" width="40" height="5" fill="{W}"/>
  <rect x="24" y="11" width="7" height="22" fill="{W}"/>
  <rect x="69" y="11" width="7" height="22" fill="{W}"/>
  <rect x="18" y="15" width="6" height="14" fill="{W}"/>
  <rect x="76" y="15" width="6" height="14" fill="{W}"/>
  <path d="M26 56 V50 a8 8 0 0 1 16 0 V56" fill="none" stroke="{W}" stroke-width="4"/>
  <path d="M18 54 H50 L52 88 H16 Z" fill="{W}"/>
  <rect x="56" y="52" width="30" height="7" fill="{W}"/>
  {teeth}'''


def alojamento(bg):
    return f'''
  <rect x="10" y="40" width="6" height="42" fill="{W}"/>
  <rect x="10" y="64" width="50" height="7" fill="{W}"/>
  <rect x="54" y="71" width="6" height="11" fill="{W}"/>
  <rect x="19" y="52" width="12" height="9" fill="{W}"/>
  <rect x="33" y="50" width="27" height="11" fill="{W}"/>
  <path d="M71 40 V32 H83 V40" fill="none" stroke="{W}" stroke-width="4"/>
  <rect x="65" y="40" width="24" height="38" fill="{W}"/>
  <line x1="72" y1="46" x2="72" y2="72" stroke="{bg}" stroke-width="2.6"/>
  <line x1="82" y1="46" x2="82" y2="72" stroke="{bg}" stroke-width="2.6"/>
  <rect x="68" y="78" width="4" height="5" fill="{W}"/>
  <rect x="82" y="78" width="4" height="5" fill="{W}"/>'''


DRAW = {
    "bares": bares, "discoteca": discoteca, "sauna": sauna, "cruising": cruising,
    "comer-e-beber": comer_e_beber, "ao-ar-livre": ao_ar_livre,
    "estilo-de-vida": estilo_de_vida, "alojamento": alojamento,
}


def icon_svg(slug, bg, size=512):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" '
            f'viewBox="0 0 100 100" shape-rendering="geometricPrecision">\n'
            f'  <rect width="100" height="100" fill="{bg}"/>'
            f'{DRAW[slug](bg)}\n</svg>\n')


def grid_svg():
    cell, gap, pad, label_h = 100, 16, 32, 22
    cols, rows = 4, 2
    w = pad * 2 + cols * cell + (cols - 1) * gap
    h = pad * 2 + rows * (cell + label_h) + (rows - 1) * gap
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w*4}" height="{h*4}" viewBox="0 0 {w} {h}">',
             f'<rect width="{w}" height="{h}" fill="#EDEDED"/>']
    for i, (slug, label, bg) in enumerate(ICONS):
        c, r = i % cols, i // cols
        x = pad + c * (cell + gap)
        y = pad + r * (cell + label_h + gap)
        parts.append(f'<g transform="translate({x} {y})"><rect width="100" height="100" fill="{bg}"/>{DRAW[slug](bg)}</g>')
        parts.append(f'<text x="{x+50}" y="{y+cell+15}" text-anchor="middle" '
                     f'font-family="Helvetica, Arial, sans-serif" font-size="9" font-weight="600" '
                     f'fill="#333">{label}</text>')
    parts.append('</svg>')
    # clipPath ids repetidos na grade: só a discoteca usa, então tudo bem
    return "\n".join(parts)


if __name__ == "__main__":
    for i, (slug, _, bg) in enumerate(ICONS, 1):
        (OUT / "svg" / f"{i:02d}-{slug}.svg").write_text(icon_svg(slug, bg))
    (OUT / "grid.svg").write_text(grid_svg())
    print("ok")
