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


const tenis = (partido) => {
    const puntuacion = ["Love", 15, 30, 40, "Deuce"];
    let playerOne = 0;
    let playerTwo = 0;

    for (let puntos of partido) {
        if ('P1' === puntos) {
            playerOne++;
        } else if ('P2' === puntos) {
            playerTwo++;
        }

        if (playerOne >= 3 && playerTwo >= 3 && playerOne === playerTwo) {
            console.log(puntuacion[4]);
        } else if (playerOne >= 4 && playerTwo === playerOne - 1) {
            console.log("Ventaja P1");
        } else if (playerTwo >= 4 && playerOne === playerTwo - 1) {
            console.log('Ventaja P2');
        } else if (playerOne >= 4 && playerTwo >= playerOne - 2) {
            console.log('Ha ganado el P1');
            break; // Termina el juego
        } else if (playerTwo >= 4 && playerOne >= playerTwo - 2) {
            console.log('Ha ganado el P2');
            break; // Termina el juego
        } else {
            console.log(`Puntuación actual: ${puntuacion[playerOne]} - ${puntuacion[playerTwo]}`);
        }
    }
}

tenis(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);


