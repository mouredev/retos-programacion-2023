// # Reto #2: EL PARTIDO DE TENIS
// #### Dificultad: Media | Publicación: 09/01/23 | Corrección: 16/01/23

// ## Enunciado

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

const game1 = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"];

const darPuntaje = (secuencia) => {
  const marcador = {
    0: "Love",
    1: "15",
    2: "30",
    3: "40",
  };
  let p1 = 0;
  let p2 = 0;

  for (let i of secuencia) {
    if (i == "P1") {
      p1++;
    } else {
      p2++;
    }

    if (p1 > 3 && p2 <= 2) {
      console.log("ha ganado el juego el", i);
      break;
    } else if (p2 > 3 && p1 <= 2) {
      console.log("ha ganado el juego el", i);
      break;
    }

    if (p1 < 3 || p2 < 3) {
      console.log("Marcador: ", marcador[p1], "-", marcador[p2]);
    } else if (p1 === 3 && p2 === 3) {
      console.log("Deuce");
    } else if (p1 === 3 && p2 === 4) {
      console.log("Ventaja P2");
    } else if (p1 === 4 && p2 === 3) {
      console.log("Ventaja P1");
    } else if (p1 === 4 && p2 === 4) {
      p1 = 3;
      p2 = 3;
      console.log("Deuce");

    }else{
      console.log("Ha ganado el juego el", i);

    }
  }
};

darPuntaje(game1);
