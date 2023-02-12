const JUGADA = {
  PIEDRA: '🗿',
  PAPEL: '📄',
  TIJERAS: '✂️',
  LAGARTO: '🦎',
  SPOCK: '🖖'
};

function PiedraPapelTijerasLagartoSpock(juegos) {
  let p1Points = 0;
  let p2Points = 0;

  const ganador = {
    [JUGADA.PIEDRA]: [JUGADA.TIJERAS, JUGADA.LAGARTO],
    [JUGADA.PAPEL]: [JUGADA.PIEDRA, JUGADA.SPOCK],
    [JUGADA.TIJERAS]: [JUGADA.PAPEL, JUGADA.LAGARTO],
    [JUGADA.LAGARTO]: [JUGADA.PAPEL, JUGADA.SPOCK],
    [JUGADA.SPOCK]: [JUGADA.TIJERAS, JUGADA.PIEDRA]
  };

  juegos.forEach(juego => {
    const [jugador1, jugador2] = juego;
    if (jugador1 === jugador2) {
      p1Points++;
      p2Points++;
    } else if (ganador[jugador1].includes(jugador2)) {
      p1Points++;
    } else {
      p2Points++;
    }
  });

  if (p1Points === p2Points)
    return `Empate a ${tiePoints} puntos`;
  else if (p1Points > p2Points)
    return `Gana el jugador 1 por ${p1Points} a ${p2Points} puntos`;
  else
    return `Gana el jugador 2 por ${p2Points} a ${p1Points} puntos`;
}

console.log(PiedraPapelTijerasLagartoSpock([
  [JUGADA.PIEDRA, JUGADA.TIJERAS],
  [JUGADA.PIEDRA, JUGADA.PAPEL],
  [JUGADA.LAGARTO, JUGADA.SPOCK]
]));

console.log(PiedraPapelTijerasLagartoSpock([
  [JUGADA.TIJERAS, JUGADA.TIJERAS],
  [JUGADA.PIEDRA, JUGADA.PAPEL],
  [JUGADA.LAGARTO, JUGADA.SPOCK],
  [JUGADA.PIEDRA, JUGADA.PAPEL],
  [JUGADA.SPOCK, JUGADA.PAPEL],
  [JUGADA.LAGARTO, JUGADA.LAGARTO],
  [JUGADA.SPOCK, JUGADA.LAGARTO],
]));
