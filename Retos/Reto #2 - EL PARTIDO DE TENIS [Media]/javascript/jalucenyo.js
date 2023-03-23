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

export default function tennisGame (sequence) {
  const puntuaciones = ['Love', 15, 30, 40]

  let scoreP1 = 0
  let scoreP2 = 0
  const result = []

  for (const game of sequence) {
    (game === 'P1' ? scoreP1++ : scoreP2++)

    if (scoreP1 >= 3 || scoreP2 >= 3) {
      if (scoreP1 === scoreP2) {
        result.push('Deuce')
      } else if (scoreP1 >= 4 || scoreP2 >= 4) {
        if (Math.abs(scoreP1 - scoreP2) >= 2) {
          result.push(`Ha ganado el ${scoreP1 > scoreP2 ? 'P1' : 'P2'}`)
        } else {
          result.push(`Ventaja ${scoreP1 > scoreP2 ? 'P1' : 'P2'}`)
        }
      } else {
        result.push(`${puntuaciones[scoreP1]} - ${puntuaciones[scoreP2]}`)
      }
    } else {
      result.push(`${puntuaciones[scoreP1]} - ${puntuaciones[scoreP2]}`)
    }
  }

  return result
}
