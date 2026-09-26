#!/usr/bin/env python3
"""Ícones de categoria bear2me — v2 (duotone + gradiente da marca).

Grid 100x100, pictograma dentro da área segura ~12..88.
DNA da marca aplicado:
  - fundo em gradiente vertical (claro em cima -> profundo embaixo), como o círculo do urso
  - chamas escuras translúcidas no topo, como atrás do urso
  - duotone: branco sólido + branco translúcido sobrepostos, como as letras do logo
  - traços com pontas/cantos arredondados, como a tipografia

Cards SEMPRE com cantos retos (90°) — regra da marca.
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent
W = "#FFFFFF"
H = 'fill="#FFFFFF" fill-opacity=".5"'  # branco translúcido (camada de trás)

# slug, rótulo, cor topo, cor base (ordem do arco-íris do pedido original)
ICONS = [
    ("bares",          "Bares",          "#F2493F", "#B5121B"),
    ("discoteca",      "Discoteca",      "#FFA23D", "#E3561A"),
    ("sauna",          "Sauna",          "#4C8DFF", "#1B45C9"),
    ("cruising",       "Cruising",       "#2FBF6B", "#0C6B34"),
    ("comer-e-beber",  "Comer e beber",  "#FFC23A", "#D98200"),
    ("ao-ar-livre",    "Ao ar livre",    "#A259D9", "#5A1784"),
    ("estilo-de-vida", "Estilo de vida", "#EC4F86", "#A0104E"),
    ("alojamento",     "Alojamento",     "#9A5A2A", "#4A2A12"),
]


def st(w=4.5, color=W, op=None):
    o = f' stroke-opacity="{op}"' if op else ""
    return (f'fill="none" stroke="{color}" stroke-width="{w}"{o} '
            f'stroke-linecap="round" stroke-linejoin="round"')


def sparkle(cx, cy, r, extra=f'fill="{W}"'):
    k = r * 0.22
    return (f'<path d="M{cx} {cy-r} Q{cx+k} {cy-k} {cx+r} {cy} Q{cx+k} {cy+k} {cx} {cy+r} '
            f'Q{cx-k} {cy+k} {cx-r} {cy} Q{cx-k} {cy-k} {cx} {cy-r} Z" {extra}/>')


def bares(c):
    return f'''
  <line x1="55" y1="40" x2="68" y2="12" {st(3)}/>
  <path d="M33 33 H67 L50 51 Z" {H}/>
  <circle cx="44" cy="37" r="1.6" fill="{W}"/><circle cx="52" cy="42" r="1.2" fill="{W}"/>
  <circle cx="48" cy="46" r="1" fill="{W}"/>
  <path d="M24 27 H76 L50 55 Z" {st()}/>
  <line x1="50" y1="55" x2="50" y2="76" {st()}/>
  <path d="M36 79 Q50 73 64 79" {st()}/>
  <circle cx="74" cy="27" r="9.5" fill="{W}"/>
  <circle cx="74" cy="27" r="6.5" {st(1.3, c)}/>
  <path d="M74 20.5 V33.5 M68.4 23.8 L79.6 30.2 M68.4 30.2 L79.6 23.8" {st(1.3, c)}/>'''


def discoteca(c):
    s = "discoteca"
    lat = "".join(f'<line x1="20" y1="{y}" x2="80" y2="{y}"/>'
                  for y in (38, 47, 56, 65, 74))
    lon = "".join(f'<ellipse cx="50" cy="56" rx="{rx}" ry="24"/>' for rx in (12, 21))
    return f'''
  <defs><clipPath id="{s}-ball"><circle cx="50" cy="56" r="24"/></clipPath></defs>
  <line x1="50" y1="8" x2="50" y2="28" {st(2.5)}/>
  <rect x="45.5" y="27" width="9" height="5" rx="1.5" fill="{W}"/>
  <circle cx="50" cy="56" r="24" {H}/>
  <g clip-path="url(#{s}-ball)">
    <circle cx="40" cy="46" r="21" fill="{W}"/>
    <g fill="none" stroke="{c}" stroke-opacity=".75" stroke-width="1.1">{lat}{lon}<line x1="50" y1="30" x2="50" y2="82"/></g>
  </g>
  {sparkle(80, 22, 8)}
  {sparkle(20, 32, 5.5)}
  {sparkle(81, 80, 4.5, H)}
  {sparkle(18, 76, 3.5, H)}'''


def sauna(c):
    def curl(x, extra):
        return (f'<path d="M{x} 50 C{x-7} 44 {x+7} 38 {x} 32 C{x-7} 26 {x+7} 20 {x} 14" {extra}/>')
    return f'''
  {curl(32, st(4, op=".5"))}
  {curl(44, st(4))}
  {curl(56, st(4, op=".5"))}
  <path d="M28 58 Q44 44 60 58" {st(2.5, op=".6")}/>
  <path d="M25 58 H63 L59 84 H29 Z" fill="{W}" stroke="{W}" stroke-width="3" stroke-linejoin="round"/>
  <line x1="27" y1="65" x2="61" y2="65" stroke="{c}" stroke-width="2.2"/>
  <line x1="29" y1="77.5" x2="59" y2="77.5" stroke="{c}" stroke-width="2.2"/>
  <rect x="72" y="18" width="9" height="36" rx="4.5" {st(3)}/>
  <line x1="76.5" y1="54" x2="76.5" y2="32" {st(3)}/>
  <circle cx="76.5" cy="59" r="7" fill="{W}"/>
  <path d="M66 26 H69 M66 33 H69 M66 40 H69 M66 47 H69" {st(2, op=".6")}/>'''


def cruising(c):
    s = "cruising"
    return f'''
  <defs>
    <mask id="{s}-moon"><rect width="100" height="100" fill="#fff"/>
      <circle cx="28" cy="17" r="7" fill="#000"/></mask>
    <clipPath id="{s}-gap"><rect x="42" y="24" width="34" height="60"/></clipPath>
  </defs>
  <circle cx="23" cy="21" r="8" fill="{W}" mask="url(#{s}-moon)"/>
  {sparkle(14, 38, 3, H)}{sparkle(30, 34, 2.2, H)}
  <path d="M42 84 H76 L92 100 H30 Z" fill="#FFFFFF" fill-opacity=".18"/>
  <rect x="42" y="24" width="34" height="60" fill="#000" fill-opacity=".28"/>
  <g clip-path="url(#{s}-gap)" fill="{W}">
    <path d="M75 34 C66 34 62 40 62 47 C62 50 60 52 58.5 54 L62 55 C62 58 63 60 66 60 L75 60 Z"/>
    <path d="M58 84 V74 Q58 63 70 62 H80 V84 Z"/>
  </g>
  <path d="M42 24 L29 17 V92 L42 84 Z" {H} stroke="#FFFFFF" stroke-opacity=".6" stroke-width="2" stroke-linejoin="round"/>
  <circle cx="33" cy="55" r="1.8" fill="{W}"/>
  <rect x="42" y="24" width="34" height="60" {st(4)}/>'''


def comer_e_beber(c):
    return f'''
  <circle cx="50" cy="54" r="23" {H}/>
  <circle cx="50" cy="54" r="15" fill="{W}"/>
  <path d="M34 42 A20 20 0 0 1 44 35.5" {st(2.5)}/>
  <path d="M12 16 V29 Q12 36 18 36 Q24 36 24 29 V16" {st(3)}/>
  <line x1="18" y1="16" x2="18" y2="31" {st(3)}/>
  <line x1="18" y1="36" x2="18" y2="84" {st(5)}/>
  <path d="M79 14 C86 18 89 30 88 46 H79 Z" fill="{W}" stroke="{W}" stroke-width="2" stroke-linejoin="round"/>
  <line x1="83.5" y1="46" x2="83.5" y2="84" {st(5)}/>'''


def ao_ar_livre(c):
    return f'''
  <circle cx="79" cy="22" r="13" fill="#FFFFFF" fill-opacity=".25"/>
  <circle cx="79" cy="22" r="8" fill="{W}"/>
  <path d="M16 76 Q42 60 74 76 Z" {H}/>
  <path d="M36 74 Q37 52 48 35 L52 37 Q42 53 42 74 Z" fill="{W}"/>
  <path d="M50 36 C40 30 28 32 20 42 C30 36 40 36 50 36 Z" {H}/>
  <path d="M50 36 C58 30 70 32 76 42 C68 36 58 36 50 36 Z" {H}/>
  <path d="M50 36 C42 24 30 20 18 26 C30 26 40 28 50 36 Z" fill="{W}"/>
  <path d="M50 36 C46 22 38 14 28 12 C38 18 44 26 50 36 Z" fill="{W}"/>
  <path d="M50 36 C54 24 60 18 66 16 C60 22 55 28 50 36 Z" fill="{W}"/>
  <circle cx="47.5" cy="39.5" r="2.6" fill="{W}"/><circle cx="53" cy="40" r="2.6" {H}/>
  <path d="M12 82 q5 -4 10 0 t10 0 t10 0 t10 0 t10 0 t10 0 t10 0 t10 0" {st(3.5)}/>
  <path d="M18 90 q5 -4 10 0 t10 0 t10 0 t10 0 t10 0 t10 0 t10 0" {st(3, op=".5")}/>'''


def estilo_de_vida(c):
    teeth = "".join(f'<rect x="{x:.1f}" y="19" width="1.9" height="12" rx=".95" fill="{W}"/>'
                    for x in [59 + i * 3.5 for i in range(7)])
    return f'''
  <g opacity=".5">
    <path d="M32 42 V36 a10 10 0 0 1 20 0 V42" {st(3.5)}/>
    <path d="M22 42 H62 L65 86 H19 Z" fill="{W}" stroke="{W}" stroke-width="3" stroke-linejoin="round"/>
  </g>
  <g transform="rotate(28 71 22)">
    <rect x="57" y="13" width="28" height="7" rx="2.5" fill="{W}"/>
    {teeth}
  </g>
  <g transform="rotate(-25 56 66)">
    <rect x="36" y="64" width="40" height="4.5" rx="2.2" fill="{W}"/>
    <rect x="38" y="55" width="7" height="22" rx="2.5" fill="{W}"/>
    <rect x="67" y="55" width="7" height="22" rx="2.5" fill="{W}"/>
    <rect x="32.5" y="58.5" width="5" height="15" rx="2" fill="{W}"/>
    <rect x="74.5" y="58.5" width="5" height="15" rx="2" fill="{W}"/>
  </g>'''


def alojamento(c):
    return f'''
  <path d="M20 16 H28 L20 24 H28" {st(2.5, op=".6")}/>
  <path d="M31 9 H36 L31 14 H36" {st(2, op=".6")}/>
  <rect x="11" y="38" width="7" height="46" rx="3" fill="{W}"/>
  <rect x="11" y="64" width="52" height="7" rx="2.5" fill="{W}"/>
  <rect x="56" y="69" width="6" height="15" rx="2.5" fill="{W}"/>
  <rect x="21" y="47" width="13" height="10" rx="4" fill="{W}"/>
  <path d="M36 50 H59 Q63 50 63 54 V62 H36 Z" fill="{W}"/>
  <path d="M40 55 H58" {st(1.6, c, ".5")}/>
  <path d="M71 40 V33 Q71 31 73 31 H81 Q83 31 83 33 V40" {st(3.5)}/>
  <rect x="66" y="40" width="22" height="40" rx="4" fill="{W}"/>
  <path d="M72.5 46 V74 M81.5 46 V74" {st(2.2, c)}/>
  <circle cx="70.5" cy="84" r="2.6" fill="{W}"/><circle cx="83.5" cy="84" r="2.6" fill="{W}"/>'''


DRAW = {
    "bares": bares, "discoteca": discoteca, "sauna": sauna, "cruising": cruising,
    "comer-e-beber": comer_e_beber, "ao-ar-livre": ao_ar_livre,
    "estilo-de-vida": estilo_de_vida, "alojamento": alojamento,
}


def tile(slug, top, bottom):
    """Fundo (gradiente + chamas da marca) + pictograma, dentro de um clip com o raio do card."""
    return f'''
  <defs>
    <linearGradient id="{slug}-bg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/>
    </linearGradient>
    <clipPath id="{slug}-card"><rect width="100" height="100"/></clipPath>
  </defs>
  <g clip-path="url(#{slug}-card)">
    <rect width="100" height="100" fill="url(#{slug}-bg)"/>
    <path d="M6 0 C4 12 10 20 20 26 C14 16 18 8 26 0 Z M66 0 C62 10 68 18 80 24 C74 14 78 6 86 0 Z"
          fill="#000" fill-opacity=".09"/>
    {DRAW[slug](bottom)}
  </g>'''


def icon_svg(slug, top, bottom, size=512):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">'
            f'{tile(slug, top, bottom)}\n</svg>\n')


def grid_svg():
    cell, gap, pad, label_h = 100, 14, 28, 20
    cols, rows = 4, 2
    w = pad * 2 + cols * cell + (cols - 1) * gap
    h = pad * 2 + rows * (cell + label_h) + (rows - 1) * gap
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w*4}" height="{h*4}" viewBox="0 0 {w} {h}">',
             f'<rect width="{w}" height="{h}" fill="#F5F2ED"/>']  # off-white do app
    for i, (slug, label, top, bottom) in enumerate(ICONS):
        x = pad + (i % cols) * (cell + gap)
        y = pad + (i // cols) * (cell + label_h + gap)
        parts.append(f'<g transform="translate({x} {y})">{tile(slug, top, bottom)}</g>')
        parts.append(f'<text x="{x+50}" y="{y+cell+14}" text-anchor="middle" '
                     f'font-family="Quicksand, Comfortaa, Helvetica, Arial, sans-serif" '
                     f'font-size="9" font-weight="700" fill="#4A4A4A">{label}</text>')
    parts.append('</svg>')
    return "\n".join(parts)


if __name__ == "__main__":
    for i, (slug, _, top, bottom) in enumerate(ICONS, 1):
        (OUT / "svg" / f"{i:02d}-{slug}.svg").write_text(icon_svg(slug, top, bottom))
    (OUT / "grid.svg").write_text(grid_svg())
    print("ok")
