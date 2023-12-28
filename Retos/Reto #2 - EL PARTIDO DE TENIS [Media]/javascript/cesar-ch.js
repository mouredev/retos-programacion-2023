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

const points = ["Love", 15, 30, 40, "Deuce", "Ventaja"];

const tennisGame = (arr) => {
  let p1 = 0;
  let p2 = 0;
  let respuesta = "";

  arr.map((e) => {
    e === "P1" ? p1++ : p2++;

    if (p1 >= 3 && p2 >= 3 && p1 == p2) {
      respuesta += "Deuce\n";
    } else if (p1 < 4 && p2 < 4) {
      respuesta += `${points[p1]} - ${points[p2]}\n`;
    } else if (p1 == 4 || p2 == 4) {
      p1 == 4 ? (respuesta += "Vantaja P1\n") : (respuesta += "Ventaja P2\n");
    } else if (p1 == 5 || p2 == 5) {
      p1 == 5
        ? (respuesta += "Ha ganado el P1")
        : (respuesta += "Ha ganado P2");
    }
  });

  return respuesta;
};

// console.log(tennisGame(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]));
