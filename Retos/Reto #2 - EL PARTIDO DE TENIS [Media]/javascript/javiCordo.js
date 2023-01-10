
//
// javiCordo.js
//
//
//  Created by Javier Alejandro Cordovés Almaguer on 10/01/23.


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

const score = [0,0]
const points = ['Love',15,30,40,'Deuce','Ventaja']

function TennisGame(result) {
  let isWinner = false;
  for (const element of result) {
    if(isWinner){
    console.log('Ya existe un ganador')
    break;
  }
  let currentPlayer = element.includes('P1') ? 0: 1
    try {
      if ( element !== 'P1' && element !== 'P2')  { 
        throw new Error ('No se admite ese valor solo se puede usar P1 y P2')
      }
      score[currentPlayer] ++
    } catch (error) {
       console.error(error);
       break;
    }
    isWinner = resultGame(currentPlayer)
  }
  
}

function resultGame(currentPlayer) {
  if(score[0] === 3 && score[1] === 3) {
    console.log('Deuce')
  }
  else if((score[0] === 4 && score[0] > score[1]) || (score[1] === 4 && score[0] < score[1])) console.log(`Ventaja P${currentPlayer + 1}` )
  else if((score[0] === 5 && score[0] - score[1] === 2) || (score[1] === 5 && score[1] - score[0] === 2)){
    console.log(`Ha Ganado el P${currentPlayer + 1}` )
    return true
  }
  else console.log(points[score[0]] + ' - ' + points[score[1]] )

  return false
}

TennisGame(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'])