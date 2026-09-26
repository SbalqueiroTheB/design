#!/usr/bin/env python3
"""Avatares padrão bear2me para quem ainda não tem foto.

Mesma linguagem dos ícones de categoria (gradiente vertical, chamas translúcidas,
duotone branco), mas com a paleta quente da logo, para não confundir com categoria.

Regras:
  - card sempre com cantos retos
  - mesmo busto em todos; variam só barba, cabelo, boné/gorro e óculos
  - figura em branco, sem tom de pele (ninguém é "rotulado" pelo sorteio)
  - detalhes (barba, cabelo, óculos) na cor escura do próprio fundo
"""
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent
W = "#FFFFFF"

# slug, nome, cor topo, cor base (tons tirados do gradiente do urso e do logotipo)
AVATARS = [
    ("brasa",     "Brasa",     "#EE5A45", "#9A1E1E"),
    ("laranja",   "Laranja",   "#F79545", "#B84A17"),
    ("ambar",     "Âmbar",     "#F4B846", "#B26A0C"),
    ("mel",       "Mel",       "#D8A150", "#87521A"),
    ("urso",      "Urso",      "#A86A3E", "#4E2C16"),
    ("terracota", "Terracota", "#CF6444", "#6E2A1C"),
    ("vinho",     "Vinho",     "#B8475A", "#5A1A29"),
    ("grafite",   "Grafite",   "#7A6A60", "#2E2724"),
]


def st(w, color, op=None):
    o = f' stroke-opacity="{op}"' if op else ""
    return (f'fill="none" stroke="{color}" stroke-width="{w}"{o} '
            f'stroke-linecap="round" stroke-linejoin="round"')


# ---------- peças ----------
def body(d):
    """Busto comum a todos: ombros translúcidos, pescoço, orelhas e cabeça sólidos."""
    return f'''
  <path d="M12 100 V91 Q12 72 36 68 Q50 76 64 68 Q88 72 88 91 V100 Z" fill="{W}" fill-opacity=".5"/>
  <path d="M40 69 Q50 79 60 69" {st(2, d, ".35")}/>
  <rect x="43" y="56" width="14" height="15" rx="4" fill="{W}"/>
  <path d="M43 60 Q50 67 57 60 V65.5 Q50 70 43 65.5 Z" fill="{d}" fill-opacity=".22"/>
  <circle cx="34.5" cy="48" r="4" fill="{W}"/><circle cx="65.5" cy="48" r="4" fill="{W}"/>
  <ellipse cx="50" cy="45" rx="15.5" ry="18" fill="{W}"/>'''


def eyes(d):
    return f'<circle cx="44" cy="45" r="1.7" fill="{d}"/><circle cx="56" cy="45" r="1.7" fill="{d}"/>'


def brows(d):
    return f'<path d="M40.5 40.5 Q44 39 47 40.3 M53 40.3 Q56 39 59.5 40.5" {st(1.6, d, ".8")}/>'


MUSTACHE = "M42.5 55.5 Q46 52.5 50 54 Q54 52.5 57.5 55.5 Q54 57 50 55.6 Q46 57 42.5 55.5 Z"


def beard_full(d, op="1", chin=70):
    return (f'<path d="M34.8 44 C34.5 60 41 {chin} 50 {chin+1} C59 {chin} 65.5 60 65.2 44 '
            f'C63 52 60.5 56.5 56 57.5 Q50 60.5 44 57.5 C39.5 56.5 37 52 34.8 44 Z" fill="{d}" fill-opacity="{op}"/>'
            f'<path d="{MUSTACHE}" fill="{d}" fill-opacity="{op}"/>')


def beard_long(d):
    return (f'<path d="M34.8 44 C34.5 64 41 82 50 86 C59 82 65.5 64 65.2 44 '
            f'C63 52 60.5 56.5 56 57.5 Q50 60.5 44 57.5 C39.5 56.5 37 52 34.8 44 Z" fill="{d}"/>'
            f'<path d="{MUSTACHE}" fill="{d}"/>'
            f'<path d="M46 70 Q50 76 54 70 M44 64 Q50 71 56 64" {st(1.2, W, ".25")}/>')


def goatee(d):
    return (f'<path d="M45 58.5 Q50 57 55 58.5 L54 66 Q50 70 46 66 Z" fill="{d}"/>'
            f'<path d="{MUSTACHE}" fill="{d}"/>')


def mustache_big(d):
    return f'<path d="M40.5 56 Q45 51 50 53.5 Q55 51 59.5 56 Q57 60 54 57.5 Q50 56 46 57.5 Q43 60 40.5 56 Z" fill="{d}"/>'


def hair_short(d):
    return f'<path d="M34.6 44 C33.5 30 41 26.5 50 26.5 C59 26.5 66.5 30 65.4 44 C63 37 57 34 50 34 C43 34 37 37 34.6 44 Z" fill="{d}"/>'


def hair_quiff(d):
    return (f'<path d="M34.6 43 C33.5 30 41 27 50 27 C59 27 66.5 30 65.4 43 C63 36.5 57 34 50 34 C43 34 37 36.5 34.6 43 Z" fill="{d}"/>'
            f'<path d="M40 31 C43 20 58 17 64 25 C60 23 55 24 52 28 Z" fill="{d}"/>')


def hair_receding(d):
    return (f'<path d="M34.6 46 C34 38 36 33 40 31 L40.5 42 Q38 43 34.6 46 Z" fill="{d}"/>'
            f'<path d="M65.4 46 C66 38 64 33 60 31 L59.5 42 Q62 43 65.4 46 Z" fill="{d}"/>')


def hair_curly(d):
    c = [(37, 36, 5), (41, 30, 5.5), (47, 26.5, 5.5), (53, 26.5, 5.5), (59, 30, 5.5), (63, 36, 5),
         (35, 42, 3.8), (65, 42, 3.8), (50, 31, 5)]
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{d}"/>' for x, y, r in c)


def cap_front(d):
    return (f'<path d="M34 41 C33 27 41 23.5 50 23.5 C59 23.5 67 27 66 41 Z" fill="{d}"/>'
            f'<path d="M50 24 V40" {st(1.2, W, ".3")}/>'
            f'<circle cx="50" cy="24.5" r="1.8" fill="{d}"/>'
            f'<path d="M30 42.5 Q50 35 70 42.5 Q50 47.5 30 42.5 Z" fill="{d}"/>'
            f'<path d="M34 42 Q50 37.8 66 42" {st(1, W, ".3")}/>')


def cap_back(d):
    return (f'<path d="M34 42 C33 27 41 23.5 50 23.5 C59 23.5 67 27 66 42 Z" fill="{d}"/>'
            f'<path d="M44 42 Q44 35.5 50 35.5 Q56 35.5 56 42 Z" fill="{W}" fill-opacity=".45"/>'
            f'<path d="M43.5 37.5 H56.5" {st(1.8, d)}/><circle cx="50" cy="37.5" r="1.2" fill="{W}" fill-opacity=".6"/>'
            f'<path d="M34 41.5 Q50 39 66 41.5" {st(1.2, W, ".3")}/>')


def beanie(d):
    ribs = "".join(f'<line x1="{x}" y1="36.5" x2="{x}" y2="42" stroke="#FFFFFF" stroke-opacity=".28" stroke-width="1"/>'
                   for x in range(37, 64, 4))
    return (f'<circle cx="50" cy="18.5" r="4.5" fill="{d}"/>'
            f'<path d="M33.5 42 C33 26 41 21.5 50 21.5 C59 21.5 67 26 66.5 42 Z" fill="{d}"/>'
            f'<rect x="33" y="36" width="34" height="7" rx="2" fill="{d}"/>{ribs}')


def glasses_square(d):
    return (f'<rect x="38.5" y="41" width="10" height="8" rx="2" {st(1.8, d)}/>'
            f'<rect x="51.5" y="41" width="10" height="8" rx="2" {st(1.8, d)}/>'
            f'<path d="M48.5 44 Q50 42.8 51.5 44 M38.5 43.5 L35 42.5 M61.5 43.5 L65 42.5" {st(1.6, d)}/>')


def glasses_round(d):
    return (f'<circle cx="44" cy="45" r="4.8" {st(1.7, d)}/><circle cx="56" cy="45" r="4.8" {st(1.7, d)}/>'
            f'<path d="M48.8 44.5 Q50 43.3 51.2 44.5 M39.2 44 L35 43 M60.8 44 L65 43" {st(1.5, d)}/>')


# ---------- os 8 personagens ----------
def a_brasa(d):      # careca + barba cheia
    return body(d) + eyes(d) + brows(d) + beard_full(d) + \
        f'<path d="M40 31 Q45 28.5 49 29" {st(1.6, d, ".2")}/>'


def a_laranja(d):    # boné + barba curta
    return body(d) + eyes(d) + beard_full(d, "1", 63.5) + cap_front(d)


def a_ambar(d):      # cabelo curto + óculos + barba cheia
    return body(d) + hair_short(d) + eyes(d) + beard_full(d) + glasses_square(d)


def a_mel(d):        # topete + bigodão
    return body(d) + hair_quiff(d) + eyes(d) + brows(d) + mustache_big(d)


def a_urso(d):       # gorro + barba longa
    return body(d) + beard_long(d) + eyes(d) + beanie(d)


def a_terracota(d):  # entradas + cavanhaque + óculos redondos
    return body(d) + hair_receding(d) + eyes(d) + goatee(d) + glasses_round(d)


def a_vinho(d):      # cabelo cacheado + barba curta
    return body(d) + hair_curly(d) + eyes(d) + brows(d) + beard_full(d, "1", 63.5)


def a_grafite(d):    # boné pra trás + barba cheia
    return body(d) + eyes(d) + brows(d) + beard_full(d) + cap_back(d)


DRAW = {"brasa": a_brasa, "laranja": a_laranja, "ambar": a_ambar, "mel": a_mel,
        "urso": a_urso, "terracota": a_terracota, "vinho": a_vinho, "grafite": a_grafite}


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
          fill="#000" fill-opacity=".09"/>
    <g transform="translate(50 100) scale(1.1) translate(-50 -100)">{DRAW[slug](bottom)}</g>
  </g>'''


def avatar_svg(slug, top, bottom, size=512):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 100 100">'
            f'{tile(slug, top, bottom)}\n</svg>\n')


def grid_svg():
    """Prévia 4x2 com o rótulo do nome como no app (faixa escura sobre a base do card)."""
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
