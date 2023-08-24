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
 *
 *
 *
 * EJERCICIO DESARROLLADO POR LAURA ORTEGA - PANCRATZIA (24/08/2023)
 *
 */

const game = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];

const points = ["Love", 15, 30, 40];

const startGame = (game) => {

  const rank = {
    P1: 0,
    P2: 0,
  };


  game.forEach((round) => {
    round === "P1" ? rank.P1++ : rank.P2++;

    (rank.P1 < 3 && rank.P2 < 3) ||
    (rank.P1 === 3 && rank.P2 < rank.P1) ||
    (rank.P2 === 3 && rank.P1 < rank.P2)
      ? console.log(`${points[rank.P1]} - ${points[rank.P2]}`)
      : rank.P1 === rank.P2
        ? console.log("Deuce")
        : (rank.P1 > rank.P2 && rank.P1 < 5) || (rank.P2 > rank.P1 && rank.P2 < 5)
          ? console.log(`Ventaja ${rank.P1 > rank.P2 ? "P1" : "P2"}`)
          : console.log(`Ha ganado el ${rank.P1 > rank.P2 ? "P1" : "P2"}`);
  });

};

startGame(game);
