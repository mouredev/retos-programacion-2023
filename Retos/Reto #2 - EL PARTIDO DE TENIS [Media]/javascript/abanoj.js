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

const reto2 = partido => {
  let p1 = 0, p2= 0;
  const POINTS = ['Love', 15, 30, 40];

  if (partido.some( e => e !== 'P1' & e !== 'P2'))
    throw TypeError("This method only accepts 'P1' and 'P2' as inputs.");

  for(e of partido){
    if(e === 'P1'){
      p1++;
    } else if (e === 'P2') {
      p2++;
    }
    if(p1 >= 3 & p1 === p2) console.log('Deuce');
    if(p1 >= 4 & p1 === p2 + 1){console.log('Ventaja P1'); continue}
    if(p1 >= 4 & p1 >= p2 + 2){console.log('Ha ganado el P1'); return}
    if(p2 >= 4 & p2 === p1 + 1){console.log('Ventaja P2'); continue};
    if(p2 >= 4 & p2 >= p1 + 2){console.log('Ha ganado el P2'); return}
    
    if (p1 < 3 || ((p1 === 3 || p2 === 3) & p1 !== p2)){
      console.log(`${POINTS[p1]} - ${POINTS[p2]}`)
    }
  }
}

// reto2(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1']);
// console.log('================')
// reto2(['P2', 'P2', 'P1', 'P1', 'P2', 'P1', 'P2', 'P2']);
// console.log('================')
// reto2(['P2','P2','P2','P1','P2','P1']);
// console.log('================')
// reto2(['P1','P1','P1','P2','P1','P2']);