const input = [
  ['🗿', '✂️'],
  ['✂️', '🗿'],
  ['📄', '✂️'],
];

function getResult(input) {
  const map = new Map();

  // Assigning who wins to whom.
  map.set('🖖', new Set(['🗿', '✂️']));
  map.set('🗿', new Set(['🦎', '✂️']));
  map.set('🦎', new Set(['📄', '🖖']));
  map.set('📄', new Set(['🗿', '🖖']));
  map.set('✂️', new Set(['📄', '🦎']));

  let player1 = 0,
    player2 = 0;

  for (const [p1, p2] of input) {
    if (map.get(p1).has(p2)) player1++;
    else if (map.get(p2).has(p1)) player2++;
  }

  if (player1 == player2) return 'Tie';

  return player1 > player2 ? 'Player 1' : 'Player 2';
}

/////////////////////////////////////////////// tests
// Caso 00: Prueba de Funcionamiento.
// Desc: Se busca comprobar le correcto funcionamiento del algoritmo con el ejemplo provisto.
console.log(getResult(input));

// Caso 01: Empate
// Des: Se busca que ambos jugadores obtengan la misma cantidad de puntos.
console.log(
  getResult([
    ['🗿', '✂️'],
    ['✂️', '🗿'],
  ])
);

// Caso 02: Player 1 gana
// Des: Se busca que Player 1 obtengan la victoria.
console.log(
  getResult([
    ['🗿', '✂️'],
    ['✂️', '🗿'],
    ['🗿', '✂️'],
  ])
);

// Caso 03: Player 2 gana
// Des: Se busca que Player 2 obtengan la victoria.
console.log(
  getResult([
    ['🗿', '✂️'],
    ['✂️', '🗿'],
    ['🦎', '✂️'],
  ])
);
