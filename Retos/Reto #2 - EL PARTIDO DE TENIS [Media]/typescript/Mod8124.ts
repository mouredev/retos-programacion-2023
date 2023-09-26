/* Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
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
 * - tanto importante en el tenis se gana despues de 4 puntos con 2 de ventaja  */

const play = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'];
const rules = {
  love: ['love', 15, 30, 40],
  deuce: 'Deuce',
  ventaja: 'Ventaja',
  win: 'Ha ganado el',
};
let scoreP1 = 0;
let scoreP2 = 0;

const checkScore = (play: string) => {
  if (play === 'P1') scoreP1++;
  if (play === 'P2') scoreP2++;

  printResult();
};

const printResult = () => {
  if (scoreP1 >= 3 && scoreP2 >= 3 && scoreP1 === scoreP2) {
    console.log(rules.deuce);
  } else if (scoreP1 < 4 && scoreP2 < 4) {
    console.log(`${rules.love[scoreP1]} - ${rules.love[scoreP2]}`);
  } else if ((scoreP1 | scoreP1) !== 5 && 5 && scoreP1 > scoreP2) {
    console.log(rules.ventaja + ' P1');
  } else if ((scoreP1 | scoreP1) !== 5 && scoreP2 > scoreP1) {
    console.log(rules.ventaja + 'P2');
  } else if ((scoreP1 || scoreP2) === 5) {
    console.log(rules.win, scoreP1 === 5 ? 'P1' : 'P2');
  }
};

const who_win = (play: string[]): void => {
  play.forEach(checkScore);
};

who_win(play);
