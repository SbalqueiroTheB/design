# Ícones de categoria — bear2me (v2)

8 ícones quadrados (1:1), **sempre com cantos retos**, pictograma em duotone branco
sobre gradiente vertical. Linguagem tirada da identidade bear2me:

- **Gradiente vertical** (claro → profundo), como o círculo do urso
- **Chamas escuras translúcidas** no topo, como atrás do urso
- **Duotone**: branco sólido + branco translúcido sobrepostos, como as letras do logo
- **Pontas e cantos arredondados** no pictograma, como a tipografia (só no desenho; o card é reto)

| # | Categoria | Topo | Base | Arquivo |
|---|-----------|------|------|---------|
| 0 | **Todos** (sem filtro) | arco-íris | `#E4312B` → `#F07A26` → `#E9A800` → `#1FA055` → `#2F6FE0` → `#7B2FB0` | `svg/00-todos.svg` |
| 1 | Bares | `#F2493F` | `#B5121B` | `svg/01-bares.svg` |
| 2 | Discoteca | `#FFA23D` | `#E3561A` | `svg/02-discoteca.svg` |
| 3 | Sauna | `#4C8DFF` | `#1B45C9` | `svg/03-sauna.svg` |
| 4 | Cruising | `#2FBF6B` | `#0C6B34` | `svg/04-cruising.svg` |
| 5 | Comer e beber | `#FFC23A` | `#D98200` | `svg/05-comer-e-beber.svg` |
| 6 | Ao ar livre | `#A259D9` | `#5A1784` | `svg/06-ao-ar-livre.svg` |
| 7 | Estilo de vida | `#EC4F86` | `#A0104E` | `svg/07-estilo-de-vida.svg` |
| 8 | Alojamento | `#9A5A2A` | `#4A2A12` | `svg/08-alojamento.svg` |

## Ícone "Todos" e regra do filtro

O "Todos" representa o estado **sem filtro**. Fundo com o arco-íris do orgulho
(contém as cores de todas as categorias) e grade 2×2, o símbolo universal de "ver tudo".

Comportamento no filtro:

1. Ao abrir, **Todos** vem marcado (nenhum filtro aplicado).
2. Marcar qualquer categoria **desmarca Todos**.
3. Desmarcar a última categoria marcada **volta para Todos** (a lista nunca fica vazia).
4. Tocar em **Todos** limpa todas as categorias.
5. "Limpar filtros" equivale a tocar em Todos.

Na grade do filtro, use 3 colunas (Todos + 8 = 3×3).

- `svg/`: fonte vetorial (viewBox 100×100, exporta em 512px)
- `png/`: 512×512
- `grid.png`: preview 4×2 sobre o off-white do app (`#F5F2ED`)
- `sizes.png`: teste de legibilidade em 96/64/48/32 px

Tamanho mínimo recomendado: **48px**. Em 32px os ícones mais detalhados (sauna,
estilo de vida) começam a embolar.

Regerar:

```sh
python3 scripts/build.py
export PW=/opt/node22/lib/node_modules/playwright   # ou: npm i playwright
node scripts/render.js && node scripts/sizes.js
```
