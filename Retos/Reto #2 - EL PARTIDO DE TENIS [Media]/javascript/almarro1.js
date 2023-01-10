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

const readline = require('node:readline');
const util = require('node:util');

const States = {
  DEUCE: 'Deuce',
  LOVE: 'Love',
  _15: '15',
  _30: '30',
  _40: '40',
  ADVANTAGE: 'Ventaja',
  WIN: 'Ha ganado el ',
};

const score = [States.LOVE, States.LOVE];

/**
 * Incrementa el marcador añadiendo un punto para el jugador ```player```. 
 * @param {number} player toma valores 0 ó 1
 */
function incrementScoreFor(player) {
  switch (score[player]) {
    case States.LOVE:
      score[player] = States._15;
      break;
    case States._15:
      score[player] = States._30;
      break;
    case States._30:
      if (score[1 - player] === States._40) {
        score[player] = States.DEUCE;
        score[1 - player] = States.DEUCE;
      } else {
        score[player] = States._40;
      }
      break;
    case States._40:
    case States.ADVANTAGE:
      score[player] = States.WIN;
      break;
    case States.DEUCE:
      if (score[1 - player] === States.ADVANTAGE) {
        score[1 - player] = States.DEUCE;
      } else {
        score[player] = States.ADVANTAGE;
      }
      break;
  }
}

/**
 * Función que devuelve true/false si el marcador actual declara vencedor a un jugador y que dibuja el marcador actual
 * @returns 
 */
function assertScore(pointFor) {
  // comprobar si hay un ganador y salir del bucle
  if (score[0] === States.WIN || score[1] === States.WIN) {
    console.log(`${pointFor}: Ha ganado el P${(score[0] === States.WIN ? 1 : 2)}`);
    return true;
  }
  // Comprobar si hay ventaja para algún jugador
  if (score[0] === States.ADVANTAGE || score[1] === States.ADVANTAGE) {
    console.log(`${pointFor}: Ventaja P${(score[0] === States.ADVANTAGE ? 1 : 2)}`);
  } else
    // comprobar si hay deuce
    if (score[0] === States.DEUCE || score[1] === States.DEUCE) {
      console.log(`${pointFor}: Deuce`);
    }
    // resto de casos
    else {
      console.log(`${pointFor}: ${score[0]} - ${score[1]}`);
    }
  return false;
}


function main() {
  score[0] = States.LOVE;
  score[1] = States.LOVE;

  const playPoints = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2', 'P1', 'P1'];

  for (let pointFor of playPoints) {
    incrementScoreFor(pointFor === 'P1' ? 0 : 1);
    if (assertScore(pointFor)) {
      break;
    }
  }
}

// main();

async function interactive() {
  score[0] = States.LOVE;
  score[1] = States.LOVE;

  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  let finished = false;
  console.log('Empezando el juego...');
  const question = util.promisify(rl.question).bind(rl);
  do {
    const answer = await question('¿Quién gana el punto, 1 ó 2? ');
    if (answer === '1' || answer === '2') {
      incrementScoreFor(answer === '1' ? 0 : 1);
      finished = assertScore(`P${answer}`);
    } else {
      console.log('Respuesta incorrecta, responde "1" ó "2"...');
    }
  } while (!finished);
  rl.close();
}

interactive();
