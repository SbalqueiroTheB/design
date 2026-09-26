# Ícones de categoria

8 ícones flat, quadrados (1:1), cantos retos, pictograma branco sobre cor sólida.
Paleta na ordem da bandeira do orgulho, ajustada para contraste.

| # | Categoria | Cor | Arquivo |
|---|-----------|-----|---------|
| 1 | Bares | `#E40303` | `svg/01-bares.svg` |
| 2 | Discoteca | `#FF8C00` | `svg/02-discoteca.svg` |
| 3 | Sauna | `#004DFF` | `svg/03-sauna.svg` |
| 4 | Cruising | `#008026` | `svg/04-cruising.svg` |
| 5 | Comer e beber | `#D9A400` | `svg/05-comer-e-beber.svg` |
| 6 | Ao ar livre | `#750787` | `svg/06-ao-ar-livre.svg` |
| 7 | Estilo de vida | `#B0105E` | `svg/07-estilo-de-vida.svg` |
| 8 | Alojamento | `#C2410C` | `svg/08-alojamento.svg` |

- `svg/` — fonte vetorial (viewBox 100×100, exporta em 512px)
- `png/` — 512×512
- `grid.svg` / `grid.png` — preview da grade 4×2 sobre cinza claro

Regerar:

```sh
python3 scripts/build.py
PW=/opt/node22/lib/node_modules/playwright node scripts/render.js   # ou: npm i playwright
```
