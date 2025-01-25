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

// Crear jugadores
class Player {
  constructor() {
    this.puntos = 0;
  }

  puntuacion() {
    let pts = "";
    if (this.puntos === 0) {
      pts = "Love";
    } else if (this.puntos === 1) {
      pts = "15";
    } else if (this.puntos === 2) {
      pts = "30";
    } else if (this.puntos === 3) {
      pts = "40";
    } else {
      pts = "Ventaja";
    }

    return pts;
  }
}

const p1 = new Player();
const p2 = new Player();

const partidoDeTenis = (puntuaciones) => {
  for (let i = 0; i < puntuaciones.length; i++) {
    // Sumar puntos al ganador
    if (puntuaciones[i] == "P1") {
      p1.puntos += 1;
    } else if (puntuaciones[i] == "P2") {
      p2.puntos += 1;
    }

    // Imprimir en pantalla los resultados
    if (p1.puntos >= 3 && p2.puntos >= 3) {
      // Deuce
      if (p1.puntos == p2.puntos) {
        console.log("Deuce");
      } else if (p1.puntos - 1 == p2.puntos) {
        console.log("Ventaja P1");
      } else if (p2.puntos - 1 == p1.puntos) {
        console.log("Ventaja P2");
      } else if (p1.puntos - 2 == p2.puntos) {
        console.log("Ha ganado el P1");
      } else if (p2.puntos - 2 == p1.puntos) {
        console.log("Ha ganado el P2");
      }
    } else {
      console.log(`${p1.puntuacion()} - ${p2.puntuacion()}`);
    }
  }
};

let secuencia = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];

partidoDeTenis(secuencia);
