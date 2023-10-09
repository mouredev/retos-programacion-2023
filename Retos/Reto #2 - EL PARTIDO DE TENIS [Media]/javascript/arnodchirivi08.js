/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 * 
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.   
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */
const punctuation = { 0: 'Love', 1: 15, 2: 30, 3: 40, 4: 50, 5: 60 };
const players = { P1: 0, P2: 0 }


function game(sequence) {
    if (verifySequence(sequence)) {
        console.log('Existe un error en la secuencia ingresada');
    }

    for (let i = 0; i < sequence.length; i++) {
        const player = sequence[i];
       
        if (player === 'P1' || player === 'P2') {
            players[player]++;
        }
        if (players.P1 === players.P2 && (players.P1 >= 3 || players.P2 >= 3)) {
            imprimirResultados('Deuce');
        } else if (players.P1 >= 5 || players.P2 >= 5) {
            imprimirResultados(players.P1 > players.P2 ? 'Ha ganado P1' : 'Ha ganado P2')
        } else if (players.P1 >= 4 || players.P2 >= 4) {
            imprimirResultados(players.P1 > players.P2 ? 'Ventaja P1' : 'Ventaja P2');
        } else {
            imprimirResultados(`${punctuation[players.P1]} ${punctuation[players.P2]}`);
        }
    }
}

function verifySequence(sequence) {
    return sequence.some(item => item !== 'P1' && item !== 'P2')
}

function imprimirResultados(resultado) {
    console.log(resultado);
}

game(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'])