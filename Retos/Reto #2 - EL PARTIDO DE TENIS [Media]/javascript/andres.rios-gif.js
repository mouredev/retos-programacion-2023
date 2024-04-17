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

const player1 = "P1";
const player2 = "P2";
let p1 = 0;
let p2 = 0;

const data = [
  player1,
  player1,
  player2,
  player2,
  player1,
  player2,
  player1,
  player1,
];

const dataMap = data.map((x) => {
  if (x === "P1") {
    p1 += 15;
  } else if (x === "P2") {
    p2 += 15;
  }
  console.log(`${p1} - ${p2}`);
});
