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

const points: string[] = ["Love", "15", "30", "40"];

const tennisGame = (arr: string[]): string => {
  let p1 = 0;
  let p2 = 0;
  let answer = "";
  let winner = false;
  const final = arr.length;
  arr.map((e, i) => {
    if (winner == false) {
      e === "P1" ? p1++ : p2++;
      if (p1 >= 3 && p2 >= 3 && p1 == p2) {
        answer += "Deuce\n";
      } else if (p1 < 4 && p2 < 4) {
        answer += `${points[p1]} - ${points[p2]}\n`;
      } else if (p1 == 5 || p2 == 5) {
        winner = true;
        p1 == 5 ? (answer += "Ha ganado el P1") : (answer += "Ha ganado el P2");
      } else if (p1 == 4 || p2 == 4) {
        p1 == 4 ? (answer += "Vantaja P1\n") : (answer += "Ventaja P2\n");
      }
      if (winner == false && final == i + 1) {
        answer += "\nLos puntos jugados no son correctos";
      }
      if (winner == true && final != i + 1) {
        answer += "\nLos puntos jugados no son correctos";
      }
    }
  });
  return answer;
};

// console.log(tennisGame(["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]));
