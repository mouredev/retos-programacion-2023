import kotlin.math.absoluteValue

fun tennisMatch(vararg points: String) {
    var player1Score = 0
    var player2Score = 0
    var finished = false
    val pointsStrings = arrayOf("Love", "15", "30", "40")

    for (point in points) {
        if (!finished) {
            when (point) {
                "P1" -> player1Score += 1
                "P2" -> player2Score += 1
                else -> println("Ignorando un valor incorrecto en la posición ${points.indexOf(point) + 1}...")
            }

            when {
                player1Score >= 3 && player2Score >= 3 -> {
                    when {
                        player1Score == player2Score -> println("Deuce")
                        player1Score - player2Score == 1 -> println("Ventaja P1")
                        player2Score - player1Score == 1 -> println("Ventaja P2")
                        (player1Score - player2Score).absoluteValue == 2 -> finished = true
                    }
                }

                player1Score == 4 || player2Score == 4 -> finished = true
                else -> println("${pointsStrings[player1Score]} - ${pointsStrings[player2Score]}")
            }
        }
    }

    when {
        finished -> println(if (player1Score > player2Score) "Ha ganado el P1" else "Ha ganado el P2")
        else -> println("Puntos insuficientes para determinar un resultado")
    }
}

fun main() {
    tennisMatch("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1")
}