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
fun main(args: Array<String>) {
    val score = mutableListOf<Pair<Int, String>>()
    score.add(15 to "love")
    score.add(30 to "love")
    score.add(30 to "15")
    score.add(30 to "30")
    score.add(40 to "30")

    val result: String = playTenis(score)
    println("You win $result")
}

private fun playTenis(pointGame: List<Pair<Int, String>>): String {
    var p1: Int = 0
    var p2: Int = 0

    pointGame.forEach { (points, _) ->
        p1 += points
        var p2: String? = pointGame.lastOrNull() { it.first == points }?.second
        if (p2 != null) {
            p2 += whilePoints(p2)
        }
    }
    return when {
        p1 > p2 -> "Player 1"
        p2 > p1 -> "Player 2"
        else -> "equals"
    }
}

private fun whilePoints(point: String): Int {
    return when (point) {
        "Love" -> 0
        "15" -> 15
        "30" -> 30
        "40" -> 40
        else -> 0
    }
}
