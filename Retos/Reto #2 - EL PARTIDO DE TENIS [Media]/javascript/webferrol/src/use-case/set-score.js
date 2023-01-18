/**
 * Puntuación de los jugadores
 * @param {Array<number>} players [0,0] - Puntuación de jugador 1 (key 0) y jugador 2 (key 1)
 * @param {number} winner Jugador ganador. Su índice: 0 | 1
 * @returns {Array<number|undefined, boolean>} Jugador ganador o undefined si no lo hay. Booleano true para indicar fin del juego
 */

export const setScore = (players, winner) => {
    let looser = Boolean(winner) ? 0 : 1; //Jugador perdedor

    let scoreLooser = players[looser],
    scoreWinner = players[winner];

    //Cómo se puntúa: {0: 'Love, 1: '15', 2: '30', 3: '40', 4: 'Deuce', 5: 'Add', 6: 'Game'}
    
    if (scoreWinner + 1 === 6) {  //Si álguién llega a 6 ganador
        players[winner] = 6; //Game
        players[looser] = scoreLooser;
        return [winner, true];
    }

    if (scoreWinner + 1 === 4 && scoreLooser < 3) {  //Más de 40 y el perdedor menos de 40 Game
        players[winner] = 6; //Game
        players[looser] = scoreLooser;
        return [winner, true];
    }

    if (scoreWinner + 1 === 4 && scoreLooser === 5 || scoreWinner + 1 === 3 && scoreLooser === 3) { //Forzamos Deuce
        players[winner] = 4; //Deuce
        players[looser] = 4; 
        return [undefined, false];
    }

    if (scoreWinner + 1  === 5 && scoreLooser === 4) { //Ventaja
        players[winner] = 5; //Add
        players[looser] = 3;
        return [undefined, false];
    }

    players[winner] = scoreWinner + 1;
    players[looser] = scoreLooser;
    return [undefined, false];
}