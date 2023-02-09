function PiedraPapelTijerasLagartoSpock(juegos) {
    let p1Points = 0;
    let p2Points = 0;

    const ganador = {
        piedra: ['tijeras', 'lagarto'],
        papel: ['piedra', 'Spock'],
        tijeras: ['papel', 'lagarto'],
        lagarto: ['papel', 'Spock'],
        Spock: ['tijeras', 'piedra']
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

const juegos = [
    ['piedra', 'tijeras'],
    ['piedra', 'papel'],
    ['lagarto', 'Spock']
];

console.log(PiedraPapelTijerasLagartoSpock(juegos));

const juegos2 = [
    ['tijeras', 'tijeras'],
    ['piedra', 'papel'],
    ['lagarto', 'Spock'],
    ['piedra', 'papel'],
    ['Spock', 'papel'],
    ['lagarto', 'lagarto'],
    ['Spock', 'lagarto'],

];

console.log(PiedraPapelTijerasLagartoSpock(juegos2));