const PLAYERS = { 'P1': 0, 'P2': 1, },
      POINTS = {
        0: 'Love',
        1: '15',
        2: '30',
        3: '40',
        4: 'Deuce',
        5: 'Add',
        6: 'Game',
      }

let playerGamers = [0, 0],
    sequence = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2', 'P1', 'P2', 'P2', 'P2'],
    sequence2 = ['P1', 'P1', 'P1', 'P1'];

/**
 * Puntuación de los jugadores
 * @param {number} winner Jugador ganador. Su índice: 0 | 1
 * @returns {Array<number|undefined, boolean>} Jugador ganador o undefined si no lo hay. Booleano true para indicar fin del juego
 */
const setScore = (winner) => {
    let looser = Boolean(winner) ? 0 : 1; //Jugador perdedor

    let scoreLooser = playerGamers[looser],
        scoreWinner = playerGamers[winner];

    //Cómo se puntúa: {0: 'Love, 1: '15', 2: '30', 3: '40', 4: 'Deuce', 5: 'Add', 6: 'Game'}

    if (scoreWinner + 1 === 6) {  //Si álguién llega a 6 ganador
        playerGamers[winner] = 6; //Game
        playerGamers[looser] = scoreLooser;
        return [winner, true];
    }

    if (scoreWinner + 1 === 4 && scoreLooser < 3) {  //Más de 40 y el perdedor menos de 40 Game
        playerGamers[winner] = 6; //Game
        playerGamers[looser] = scoreLooser;
        return [winner, true];
    }

    if (scoreWinner + 1 === 4 && scoreLooser === 5 || scoreWinner + 1 === 3 && scoreLooser === 3) { //Forzamos Deuce
        playerGamers[winner] = 4; //Deuce
        playerGamers[looser] = 4;
        return [undefined, false];
    }

    if (scoreWinner + 1 === 5 && scoreLooser === 4) { //Ventaja
        playerGamers[winner] = 5; //Add
        playerGamers[looser] = 3;
        return [undefined, false];
    }

    playerGamers[winner] = scoreWinner + 1;
    playerGamers[looser] = scoreLooser;
    return [undefined, false];
}

sequence.forEach(p => {
    let p1 = playerGamers[0],
        p2 = playerGamers[1];
    const [player, finish] = setScore(PLAYERS[p]);
    console.log(`${POINTS[p1]}-${POINTS[p2]}`);
    if (finish) {
        console.log(`Ha ganado el  P${player + 1}`);
    }

});


playerGamers = [0, 0];
console.log(`@@@@@@@@@@@@@@@@@@@@@@@@@`);
console.log(``);
console.log(`@@@@@@@@@@@@@@@@@@@@@@@@@`);
sequence2.forEach(p => {
    let p1 = playerGamers[0],
        p2 = playerGamers[1];
    const [player, finish] = setScore(PLAYERS[p]);
    console.log(`${POINTS[p1]}-${POINTS[p2]}`);
    if (finish) {
        console.log(`Ha ganado el  P${player + 1}`);
    }

});