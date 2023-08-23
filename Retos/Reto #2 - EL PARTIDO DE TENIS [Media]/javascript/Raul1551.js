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

function tennisGame(sequence) {
    let points_P1 = 0;
    let points_P2 = 0;
  
    const POINTS = ["Love", 15, 30, 40];
  
    for (let game of sequence) {
      if (game === "P1") {
        points_P1++;
      } else if (game === "P2") {
        points_P2++;
      } else {
        console.log("Error: Invalid play");
        return;
      }
  
      if (points_P1 >= 3 && points_P2 >= 3) {
        if (points_P1 === points_P2) {
          console.log("Deuce");
        } else if (points_P1 - points_P2 === 1) {
          console.log("Ventaja P1");
        } else if (points_P2 - points_P1 === 1) {
          console.log("Ventaja P2");
        } else if (points_P1 - points_P2 >= 2) {
          console.log("Ha ganado el P1");
          return;
        } else if (points_P2 - points_P1 >= 2) {
          console.log("Ha ganado el P2");
          return;
        }
      } else {
        console.log(POINTS[points_P1] + " - " + POINTS[points_P2]);
      }
    }
  
    console.log("Fin del juego");
  }
  
  const sequence = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];
  tennisGame(sequence);
  
  
  


