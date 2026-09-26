# Avatares padrão bear2me

8 avatares para quem ainda **não cadastrou foto**. Ninguém é punido por não ter
foto: em vez do quadrado cinza, cada pessoa ganha o urso do bear2me.

O urso é o **da logo**: silhueta cabeça+corpo, gradiente marrom → cinza,
focinho claro, nariz escuro e chamas escuras atrás. Variam só a cor do fundo e,
de leve, os olhos.

| # | Fundo | Olhos | Gradiente (topo → meio → base) |
|---|-------|-------|--------------------------------|
| 1 | Pôr do sol | Olhar da logo | `#D93A4A` → `#EE6A3C` → `#F4A340` |
| 2 | Âmbar | Piscando | `#F07A2E` → `#F5A23A` → `#F8CB4A` |
| 3 | Brasa | Feliz | `#C2303A` → `#DC4E32` → `#EE7E38` |
| 4 | Mel | Olhando à esquerda | `#E39440` → `#EDB34E` → `#F3D06E` |
| 5 | Vinho | Dormindo | `#B23A5A` → `#CF4E55` → `#EA7C5C` |
| 6 | Terracota | Olhando à direita | `#C25A3E` → `#D8804C` → `#E8AA68` |
| 7 | Rosa | Curioso | `#DE4A72` → `#EF716A` → `#F5A26C` |
| 8 | Crepúsculo | Sereno | `#8C4A74` → `#B9505A` → `#E88E52` |

## Proteção da logo

O avatar é **parente** da logo, nunca a logo. Se fosse idêntico, todo perfil sem
foto pareceria a conta oficial da bear2me, o que confunde o usuário, abre espaço
para perfis falsos e dilui a marca. Por isso:

- **Formato:** quadrado com cantos retos. O círculo com borda é exclusivo da logo.
- **Fundo:** nenhum dos 8 gradientes é o vermelho → amarelo oficial.
- **Olhos:** variam de leve em 7 dos 8.
- **Regra para o app:** a logo oficial nunca é usada como avatar de usuário.

## Por que ursos e não pessoas

- **Neutro.** O avatar representa a comunidade, não a pessoa. Ninguém recebe
  corpo, rosto, idade ou etnia por sorteio.
- **Claramente um mascote.** Ninguém confunde com a foto real do usuário.
- **Base livre para o nome.** O rosto fica acima da faixa do nome que o app
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
  "01-por-do-sol", "02-ambar", "03-brasa", "04-mel",
  "05-vinho", "06-terracota", "07-rosa", "08-crepusculo",
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
