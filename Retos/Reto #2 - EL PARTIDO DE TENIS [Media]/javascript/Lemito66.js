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

const juegoDelTenis = (arregloDePunto) => {
  jugadores = {
    P1: 0,
    P2: 0,
  };
  marcador = ["Love", "15", "30", "40"];
  try {
    if (marcador.length > 0) {
      for (let puntos of arregloDePunto) {
        jugadores[puntos.toUpperCase()] += 1;
        imprimirResultados(jugadores, marcador);
      }
    }
    else{
        console.log('La lista esta vacia');
    }
  } catch (error) {
    console.log(error);
  }

};

const imprimirResultados = (jugadores, marcador) => {
    let diferenciaDePuntos = 0;
    if (jugadores["P1"] === 3 && jugadores["P2"] === 3) {
      console.log("Deuce");
    } else if (jugadores["P1"] >= 4 || jugadores["P1"] >= 4) {
      diferenciaDePuntos = jugadores["P1"] - jugadores["P2"];
      if (diferenciaDePuntos === 0) {
        console.log("Deuce");
      } else if (diferenciaDePuntos === 1) {
        console.log("Ventaja P1");
      } else if (diferenciaDePuntos === -1) {
        console.log("Ventaja P2");
      } else if (diferenciaDePuntos >= 2) {
        console.log("Game P1");
      } else {
        console.log("Game P2");
      }
    } else {
        console.log(`${marcador[jugadores["P1"]]}-${marcador[jugadores["P2"]]}`);
    }
  }


juegoDelTenis(['P1', 'P1', 'P1','P1'])
juegoDelTenis(['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'])