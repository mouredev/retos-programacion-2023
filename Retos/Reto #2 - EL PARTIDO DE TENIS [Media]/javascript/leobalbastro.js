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
/* TODO: OPTIMIZAR*/
let points = {
  0: "love",
  1: "15",
  2: "30",
  3: "40",
};

let jugadores = {
  P1: 0,
  P2: 0,
};

let indice = 6;

function match(listPlayer) {
  let contador = 0;
  for (let elemento in listPlayer) {
    try {
      let key = listPlayer[elemento];
      let check = key in jugadores;
      if (check === true) {
        if (contador < 6) {
          jugadores[listPlayer[elemento]] += 1;
          if (jugadores["P1"] >= 3 && jugadores["P1"] - jugadores["P2"] === 2) {
            console.log("Victoria jugador 1");
            break;
          } else if (
            jugadores["P2"] >= 3 &&
            jugadores["P2"] - jugadores["P1"] === 2
          ) {
            console.log("Victoria jugador 2");
            break;
          } else if (
            jugadores["P1"] >= 3 &&
            jugadores["P2"] >= 3 &&
            jugadores["P1"] - jugadores["P2"] === 0
          ) {
            console.log("Deuce");
            deuce(listPlayer);
            break;
          }
        }
      } else {
        throw new Error(
          "Uno de los elementos es erroneo, por favor compruebe los elementos y vuelva a ejecutar el programa"
        );
      }
      contador += 1;
      console.log(`${points[jugadores["P1"]]} - ${points[jugadores["P2"]]}`);
    } catch (error) {
      console.log(error.message);
      break;
    }
  }
}

function deuce(listPlayer) {
  let punto1 = 0;
  let punto2 = 0;
  for (let i = indice; i < listPlayer.length && Math.abs(punto1-punto2)<2; i++) {
    if (listPlayer[i] === "P1") {
      punto1 += 1;
    } else if (listPlayer[i] === "P2") {
      punto2 += 1;
    }
    if (punto1 === punto2) {
      console.log("Deuce");
      indice += 2;
      punto1 = 0;
      punto2 = 0;
    } else if (punto2 - punto1 === 1) {
      console.log("Ventaja para P2");
    } else if (punto1 - punto2 === 1) {
      console.log("Ventaja para P1");
    } else if (punto1 - punto2 === 2) {
      console.log("Victoria para el P1");
      break
    } else if (punto2 - punto1 === 2) {
      console.log("victoria para el P2");
      break
    }
  }
}

match(["P1", "P1", "P2", "P2", "P1", "P2","P1", "P2","P1", "P2","P1", "P2","P1", "P2","P1", "P2","P1", "P2","P1", "P2","P1", "P2","P1", "P2", "P1", "P1"]);
