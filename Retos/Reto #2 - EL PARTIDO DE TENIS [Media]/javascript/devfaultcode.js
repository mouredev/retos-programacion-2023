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

const prompt = require('prompt-sync')();

let P1 = 'Love'
let P2 = 'Love'

function score(player) {
    switch (player) {
        case 'Love':
            return player = 15
        case 15:
            return player = 30
        case 30:
            return player = 40
        case 40:
            return player = 'adventage'
        case 'adventage':
            return player = 'winner'
        default:
            return player
    }
}

function Tennis(P1, P2) {

    if (P1 === 'Love' && P2 === 'Love') console.log('\n' + P1 + ' - ' + P2 + '\n');

    answer = prompt ('Select a player (P1 or P2) :')

    if(answer === 'P1') {
        P1 = score(P1)
    } else if (answer === 'P2') {
        P2 = score(P2)
    } else {
        console.log('\nSelect a valid Player (P1 or P2)');
    }

    if (P1 === 'adventage' && P2 === 'adventage') {
        P1 = 40
        P2 = 40
    }
    
    if (P1 === 'adventage' && P2 !== 40) {
        console.log('\nThe winner is P1\n');
        return
    } else if (P2 === 'adventage' && P1 !== 40) {
        console.log('\nThe winner is P2\n');
        return
    }
    
    if (P1 === 40 && P2 === 40) {
        console.log('\nDeuce\n')
    } else if (P1 === 'adventage' && P2) {
        console.log('\nP1 adventage\n');
    } else if (P2 === 'adventage' && P1) {
        console.log('\nP2 adventage\n');
    } else if ((P1 !== 'winner' && P2 !== 'winner') && (P1 !== 'Love' || P2 !== 'Love')) {
        console.log('\n' + P1 + ' - ' + P2 + '\n');
    }
    
    if (P1 === 'winner') {
        console.log('\nThe winner is P1\n');
        return
    } else if (P2 === 'winner') {
        console.log('\nThe winner is P2\n');
        return
    } else {
        Tennis(P1, P2)
    }
}

Tennis(P1, P2)