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

const game = ['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P2','P2','P1','P2','P2','P2'];

const POINTS = {
  0: 'love',
  1: '15',
  2: '30',
  3: '40'
}

game.reduce( (score, player, i, arr) => {
  score = {...score, [player]: score[player] + 1 };
  if(score['P1'] < 3 || score['P2'] < 3){
    console.log(`${POINTS[score['P1']]} - ${POINTS[score['P2']]}`);
  }else if( score['P1'] === score['P2']){
    console.log('Deuce');
  }else if(score['P1'] - score['P2'] > 1 || score['P1'] - score['P2'] < -1){
    console.log(`Winner ${player}`);
    arr.splice(i+1);
  }else {
    console.log(`Advance ${player}`);
  }

  return score;
}, {['P1']: 0, ['P2']: 0});