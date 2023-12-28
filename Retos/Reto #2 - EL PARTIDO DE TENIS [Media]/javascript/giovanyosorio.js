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

const players = {
    p1: 1,
    p2: 2,
  };
function tennis(points){

    let game = ["love", "15", "30", "40"];
    let PuntosP1 = 0;
    let PuntosP2 = 0;
      console.log(points);
      for (const iterator of points) {
        console.log(iterator);
        if (iterator== players.p1) {
            PuntosP1=PuntosP1+1
        }
        if (iterator== players.p2) {
            PuntosP2=PuntosP2+1
        }
      //  console.log(`${game[PuntosP1]} - ${game[PuntosP2]} `);
        
        if (PuntosP1>=3 &&PuntosP2>=3) {
            if (PuntosP1==PuntosP2) {
                console.log("Deuce");
            }else if(PuntosP1>PuntosP2 ){
                console.log("ventaja"+ players.p1)
            }else{
                console.log("ventaja"+ players.p2)
            }
        }
        else {
            console.log(`${game[PuntosP1]} - ${game[PuntosP2]} `);
          }
      }
      if (PuntosP1 >PuntosP2 ) {
        console.log("ha ganado P1");
      }
      else{
        console.log("ha ganado P2");
      }

}
tennis([
    players.p1,
    players.p1,
    players.p2,
    players.p2,
    players.p1,
    players.p2,
    players.p1,
    players.p1,
  ]);
  