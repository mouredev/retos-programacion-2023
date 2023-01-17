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

const scores = ['Love', '15', '30', '40'];
const P1 = 'P1';
const P2 = 'P2';
let scoreP1 = 0;
let scoreP2 = 0;
let goesToAdvantage = false;
let gameHasEnded = false;

function getWinner(points) {
  console.log('Secuencia del Game:');
  points.forEach(point => {
    if (gameHasEnded) { return; }
    const isP1Point = point.toUpperCase() === 'P1';
    if (isP1Point) {
      scoreP1++;
    }
    else {
      scoreP2++;
    }

    console.log(scoreP1, scoreP2);
    const isDeuce = scoreP1 === 3 && scoreP2 === 3;
    if (!isDeuce && !goesToAdvantage) {
      console.log(`${scores[scoreP1]} - ${scores[scoreP2]}`);
      if (scoreP1 >= 3 || scoreP2 >= 3) {
        const hasP1Won = scoreP1 > scoreP2;
        hasP1Won ? console.log('P1 Wins') : console.log('P2 Wins');
        gameHasEnded = true;
      }
    }
    else if (isDeuce) {
      goesToAdvantage = true;
      console.log('Deuce');
    }
    else if (goesToAdvantage) {
      const playerAdvantage = isP1Point ? 1 : 2;
      console.log(`Advantage P${playerAdvantage}`);
      const hasP1Won = (scoreP1 - scoreP2) === 2;
      const hasP2Won = (scoreP2 - scoreP1) === 2;
      if (hasP1Won) { console.log('P1 Wins'); }
      else if (hasP2Won) { console.log('P2 Wins'); }
      gameHasEnded = hasP1Won || hasP2Won;
    }
    else {
      console.log(`${scores[scoreP1]} - ${scores[scoreP2]}`);
      if (scoreP1 >= 3 || scoreP2 >= 3) {
        const hasP1Won = scoreP1 > scoreP2;
        hasP1Won ? console.log('P1 Wins') : console.log('P2 Wins');
        gameHasEnded = true;
      }
    }
  });
}

// let gamePoints = [P1, P1, P2, P2, P1, P2, P1, P1];
// getWinner(gamePoints);

// let gamePoints = [P1, P1, P2, P2, P1, P2, P1, P1, P2, P1];
// getWinner(gamePoints);

// let gamePoints = [P1, P1, P1, P1, P1, P1];
// getWinner(gamePoints);

// let gamePoints = [P1, P1];
// getWinner(gamePoints);