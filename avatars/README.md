# Avatares padrão bear2me

8 avatares para quem ainda **não cadastrou foto**. Ninguém é punido por não ter
foto: em vez do quadrado cinza, cada pessoa ganha um personagem com a cara do app.

Mesma linguagem dos ícones de categoria (gradiente vertical, chamas translúcidas,
duotone branco, **cantos retos**), mas com a **paleta quente da logo**, para não
confundir avatar com categoria.

| # | Personagem | Topo | Base |
|---|------------|------|------|
| 1 | Careca + barba cheia | `#EE5A45` | `#9A1E1E` |
| 2 | Boné + barba curta | `#F79545` | `#B84A17` |
| 3 | Cabelo curto + óculos + barba cheia | `#F4B846` | `#B26A0C` |
| 4 | Topete + bigodão | `#D8A150` | `#87521A` |
| 5 | Gorro + barba longa | `#A86A3E` | `#4E2C16` |
| 6 | Entradas + cavanhaque + óculos redondos | `#CF6444` | `#6E2A1C` |
| 7 | Cabelo cacheado + barba curta | `#B8475A` | `#5A1A29` |
| 8 | Boné pra trás + barba cheia | `#7A6A60` | `#2E2724` |

## Decisões de inclusão

- **Mesmo corpo em todos.** Variam só barba, cabelo, boné/gorro e óculos. Um sorteio
  nunca vai "dizer" que alguém é gordo, magro ou forte.
- **Sem tom de pele.** A figura é branca (duotone), então o sorteio também não
  atribui etnia a ninguém.
- **Claramente ilustração.** Ninguém confunde com a foto real da pessoa.
- **Base livre para o nome.** O personagem fica acima da faixa do nome que o app
  sobrepõe no card.

## Como o app escolhe o avatar (fixo pelo ID)

Cada usuário recebe **sempre o mesmo** avatar, calculado a partir do ID. Assim a
pessoa fica reconhecível na grade mesmo sem foto, e o avatar não muda a cada abertura.

```ts
// FNV-1a 32 bits: rápido, estável e com boa distribuição entre os 8 avatares
export function avatarIndex(userId: string, total = 8): number {
  let h = 0x811c9dc5;
  for (let i = 0; i < userId.length; i++) {
    h ^= userId.charCodeAt(i);
    h = Math.imul(h, 0x01000193);
  }
  return (h >>> 0) % total;
}

const AVATARS = [
  "01-brasa", "02-laranja", "03-ambar", "04-mel",
  "05-urso", "06-terracota", "07-vinho", "08-grafite",
];

export const defaultAvatar = (userId: string) =>
  `/avatars/${AVATARS[avatarIndex(userId)]}.png`;
```

Quando a pessoa sobe uma foto, a foto substitui o avatar. Para adicionar mais
personagens no futuro, basta aumentar a lista: a distribuição continua uniforme
(mas os usuários existentes podem trocar de avatar, então faça isso antes do lançamento).

## Arquivos

- `svg/`: fonte vetorial (viewBox 100×100)
- `png/`: 512×512
- `grid.png`: preview com a faixa do nome, como no app
- `sizes.png`: teste de legibilidade em 96/64/48/32 px

Regerar:

```sh
python3 scripts/build.py
export PW=/opt/node22/lib/node_modules/playwright   # ou: npm i playwright
node scripts/render.js && node scripts/sizes.js
```
