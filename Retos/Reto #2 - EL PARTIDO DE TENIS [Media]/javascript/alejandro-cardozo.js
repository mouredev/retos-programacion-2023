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

/**
 *  Retrieves an array representing the sequences of a tennis game.
 *  @param {Array} arr Array containing player points.
 *  @returns {Array} Array of game sequences. Array with string "Entrada Inválida" if the input is invalid.
 */

function tennisGame(arr) {
  // Check valid input
  if (
    arr.some((el) => el !== 'P1' && el !== 'P2') ||
    (arr.filter((el) => el === 'P1').length < 4 &&
      arr.filter((el) => el === 'P2').length < 4) ||
    Math.abs(
      arr.filter((el) => el === 'P1').length -
        arr.filter((el) => el === 'P2').length
    ) > 4 ||
    Math.abs(
      arr.filter((el) => el === 'P1').length -
        arr.filter((el) => el === 'P2').length
    ) < 2
  )
    return ['Entrada Inválida'];

  const points = {
    0: 'Love',
    1: '15',
    2: '30',
    3: '40',
  };
  let p1Counter = 0;
  let p2Counter = 0;
  const score = [];
  let currentScore = 'Love - Love';
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === 'P1') {
      p1Counter++;
    } else {
      p2Counter++;
    }
    if (
      !points[p1Counter] ||
      !points[p2Counter] ||
      (p1Counter === 3 && p2Counter === 3)
    ) {
      if (p1Counter === p2Counter) {
        currentScore = 'Deuce';
      } else if (Math.abs(p1Counter - p2Counter) === 1) {
        currentScore = `Ventaja ${p1Counter > p2Counter ? 'P1' : 'P2'}`;
      } else if (Math.abs(p1Counter - p2Counter) === 2) {
        currentScore = `Ha ganado el ${p1Counter > p2Counter ? 'P1' : 'P2'}`;
      } else {
        currentScore = 'Game Over';
        break;
      }
    } else {
      currentScore = `${points[p1Counter]} - ${points[p2Counter]}`;
    }
    score.push(currentScore);
  }

  // if 'currentScore' is 'Game Over' it means that the game continued after one of the players won.
  // So the input is invalid.
  if (currentScore === 'Game Over') return ['Entrada Inválida'];
  return score;
}

// Test

// tennisGame([
//   'P1',
//   'P1',
//   'P1',
//   'P2',
//   'P2',
//   'P2',
//   'P2',
//   'P1',
//   'P1',
//   'P1',
// ]).forEach((s) => console.log(s));
