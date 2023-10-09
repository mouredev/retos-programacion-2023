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
const puntuacionNumerico = { 0: 'Love', 1: 15, 2: 30, 3: 40, 4: 50, 5: 60 }
const jugadores = { p1: 'P1', p2: 'P2' }


function puntuacionJuegodos(secuencia) {
    let player1 = 0;
    let player2 = 0;

    if(verificarValoresCorrectos(secuencia)) return console.log('Existe un error en la secuencia ingresada')
    for (let i = 0; i < secuencia.length; i++) {
        secuencia[i] === jugadores.p1 ? player1++ : player2++;
        if (player1 === player2 && (player1 >= 3 || player2 >= 3)) {
            console.log('Deuce');
        }
        else if (player1 >= 5 || player2 >= 5) {
            player1 > player2 ? console.log('Ha ganado P1') : console.log('Ha ganado P2');
        }
        else if (player1 >= 4 || player2 >= 4) {
            player1 > player2 ? console.log('Ventaja P1') : console.log('Ventaja P2');
        }
        else if (player1 <= 3 || player2 <= 3) {
            console.log(`${puntuacionNumerico[player1]} ${puntuacionNumerico[player2]}`)
        }
    }
}

function verificarValoresCorrectos(secuencia) {
    return secuencia.some(item => item !== jugadores.p1 && item !== jugadores.p2)
}

puntuacionJuegodos(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);

