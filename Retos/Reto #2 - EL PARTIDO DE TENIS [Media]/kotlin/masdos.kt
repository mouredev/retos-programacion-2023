import kotlin.math.abs

fun main() {
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

  val matchResult: MutableList<String> = mutableListOf()

  println("PARTIDO DE TENIS")
  var finish = false
  while (!finish) {
    println(
      "Introduce quien ha ganado el punto. P1 (Player 1), P2 (Player 2) o X (Fin del partido):"
    )
    when (val point = readln()) {
      "P1",
      "P2" -> matchResult.add(point)
      "X" -> finish = true
      else -> println("El parámetro '$point' no es correcto. Aceptados: P1, P2 o X")
    }
  }
  calculateScoreGame(matchResult).forEach { println(it) }
}

private fun calculateScoreGame(matchResult: MutableList<String>): List<String> {
  val pointSystem = mapOf(0 to "Love", 1 to "15", 2 to "30", 3 to "40")

  var scoreP1 = 0
  var scoreP2 = 0

  return matchResult.map {
    if (it == "P1") scoreP1++ else scoreP2++
    when {
      isDeuce(scoreP1, scoreP2) -> "Deuce"
      isAdvantage(scoreP1, scoreP2) -> "Ventaja $it"
      isWin(scoreP1, scoreP2) -> "Ha ganado el $it"
      else -> "${pointSystem[scoreP1]} - ${pointSystem[scoreP2]}"
    }
  }
}

private fun isWin(scoreP1: Int, scoreP2: Int) =
  (scoreP1 >= 4 || scoreP2 >= 4) && abs(scoreP1 - scoreP2) >= 2

private fun isAdvantage(scoreP1: Int, scoreP2: Int) =
  (scoreP1 > 3 || scoreP2 > 3) && abs(scoreP1 - scoreP2) == 1

private fun isDeuce(scoreP1: Int, scoreP2: Int) = scoreP1 >= 3 && scoreP2 >= 3 && scoreP1 == scoreP2
