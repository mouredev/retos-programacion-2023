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

const POINTS = ['Love', '15', '30', '40'];

function tennisMatch(sequence: string[]): void {
  const scores = {
    P1: 0,
    P2: 0,
  };

  sequence.forEach(winner => {
    scores[winner]++;
    if (scores.P1 <= 3 && scores.P2 <= 3 && scores.P1 + scores.P2 !== 6) {
      console.log(`${POINTS[scores.P1]} - ${POINTS[scores.P2]}`);
      return;
    }
    if (scores.P1 === scores.P2) {
      console.log('Deuce');
      return;
    }
    if (Math.abs(scores.P1 - scores.P2) === 1) {
      console.log(`Ventaja ${winner}`);
      return;
    }
    console.log(`Ha ganado el ${winner}`);
  });
}

function test() {
  // Arrange
  let received = '';
  const log = console.log;
  console.log = arg => {
    log(arg);
    received += `${arg}\n`;
  };

  // Act
  tennisMatch(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);

  // Assert
  console.log = log;
  const expected =
    [
      '15 - Love',
      '30 - Love',
      '30 - 15',
      '30 - 30',
      '40 - 30',
      'Deuce',
      'Ventaja P1',
      'Ha ganado el P1',
    ].join('\n') + '\n';
  if (received === expected) {
    console.log('✅ PASS');
  } else {
    console.log('❌ FAIL', { expected, received });
  }
}

test();
