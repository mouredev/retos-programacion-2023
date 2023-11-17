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

function jugarTenis(secuencia) {
  let puntuacionP1 = 0
  let puntuacionP2 = 0

  const puntuaciones = ["Love", 15, 30, 40]

  for (let punto of secuencia) {
    if (punto === "P1") {
      puntuacionP1++
    } else if (punto === "P2") {
      puntuacionP2++
    }

    // Mostrar puntuación actual
    if (puntuacionP1 >= 3 && puntuacionP2 >= 3) {
      if (puntuacionP1 === puntuacionP2) {
        console.log("Deuce")
      } else if (puntuacionP1 > puntuacionP2) {
        console.log("Ventaja P1")
      } else {
        console.log("Ventaja P2")
      }
    } else {
      console.log(
        `${puntuaciones[puntuacionP1]} - ${puntuaciones[puntuacionP2]}`
      )
    }

    // Verificar si hay un ganador
    if (puntuacionP1 >= 4 && puntuacionP1 - puntuacionP2 >= 2) {
      console.log("Ha ganado el P1")
      return
    } else if (puntuacionP2 >= 4 && puntuacionP2 - puntuacionP1 >= 2) {
      console.log("Ha ganado el P2")
      return
    }
  }
}

// Ejemplo de uso
const secuenciaJuego = ["P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"]
jugarTenis(secuenciaJuego)

