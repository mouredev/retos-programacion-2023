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
function match() {
  let [p1, p2, round, scoreboardOutput] = [0, 0, 0, ""];

  function addSetWinner(player) {
    if (player == "P1") {
      p1++;
    } else if (player == "P2") {
      p2++;
    }

    round++;
    // Build the ScoreBoard
    if (round < 8) {
      displayScoreBoard();
    }
  }

  function displayScoreBoard() {
    if (round < 6) {
      scoreboardOutput += `${toTenisPoints(p1)} - ${toTenisPoints(p2)} \n`;
    } else if (round >= 6 && toTenisPoints(p1) == toTenisPoints(p2)) {
      scoreboardOutput += `Deuce \n`;
    } else if (round == 7) {
      scoreboardOutput += p1 > p2 ? `Ventaja P1 \n` : `Ventaja P2 \n`;
    } else {
      scoreboardOutput += p1 > p2 ? `Ha ganado P1` : `Ha ganado P2`;
    }
    return scoreboardOutput;
  }

  function toTenisPoints(num) {
    if (num == 0) {
      num = "Love";
    } else if (num == 1) {
      num = 15;
    } else if (num == 2) {
      num = 30;
    } else if (num == 3) {
      num = 40;
    }
    return num;
  }

  return {
    addSetWinner,
    displayScoreBoard,
  };
}
const theMatch = match();
theMatch.addSetWinner("P1");
theMatch.addSetWinner("P1");
theMatch.addSetWinner("P2");
theMatch.addSetWinner("P2");
theMatch.addSetWinner("P1");
theMatch.addSetWinner("P2");
theMatch.addSetWinner("P1");
theMatch.addSetWinner("P1");
console.log(theMatch.displayScoreBoard());
