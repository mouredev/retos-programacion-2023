/*
 Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 gane cada punto del juego.
 
 - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
   15 - Love
   30 - Love
   30 - 15
   30 - 30
   40 - 30
   Deuce
   Ventaja P1
   Ha ganado el P1
 - Si quieres, puedes controlar errores en la entrada de datos.   
 - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
 */

// SOLUTION:
const points = ["p1", "p1", "p2", "p2", "p1", "p2", "p1", "p1"];
const initialPoints = 15; 
let puntosDelJugador1 = 0; 
let puntosDelJugador2 = 0; 


const tennisGame = () => {
  puntosIniciales(0, "p1");
  console.log(`Jugador1: ${puntosDelJugador1} - Jugador2: ${puntosDelJugador2}`);
  puntosIniciales(1, "p1");
  console.log(`Jugador1: ${puntosDelJugador1} - Jugador2: ${puntosDelJugador2}`);
  puntosIniciales(2, "p2");
  console.log(`Jugador1: ${puntosDelJugador1} - Jugador2: ${puntosDelJugador2}`);
  puntosIniciales(2, "p2");
  console.log(`Jugador1: ${puntosDelJugador1} - Jugador2: ${puntosDelJugador2}`);

}

const puntosIniciales = (turno, jugador) => {
  if(points[turno] === "p1" && jugador === "p1") {
    puntosDelJugador1 = puntosDelJugador1 + initialPoints;
  } else if(points[turno] === "p2" &&  jugador === "p2") {
    puntosDelJugador2 = puntosDelJugador2 + initialPoints;
  }
}

tennisGame();
