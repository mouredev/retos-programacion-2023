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
 */

const secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];
let puntosGame = ["Love", 15, 30, 40, "Deuce"];
let player1 = 0;
let player2 = 0;

function juego(secuencia) {
  for (let i = 0; i < secuencia.length; i++) {
    let element = secuencia[i];

    element == "P1" ? (player1 += 1) : element == "P2" ? (player2 += 1) : "";

    if (puntosGame[player1] == 40 && puntosGame[player2] == 40) console.log(puntosGame[4]);
    else if (player1 > 3) {
      console.log("Ventaja P1");
    } else if (p2 > 3) {
      console.log("Ventaja P2");
    } else console.log(`${puntosGame[p1]} - ${puntosGame[p2]}`);
  }

  player1 > player2 ? console.log("Ha ganado el P1") : console.log("Ha ganado el P2");
}

juego(secuencia);
