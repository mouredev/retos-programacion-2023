fun main() {
    val p1 = Player.P1
    val p2 = Player.P2
    tennisGame(points = listOf(p1, p1, p2, p2, p1, p2, p1, p1))
    println()
    tennisGame(points = listOf(p1, p2, p2, p1, p1, p1, p2, p2))
    println()
    tennisGame(points = listOf(p1, p1, p2, p2, p1, p2, p1, p2, p2, p2))
}

enum class Player {
    P1, P2
}

fun tennisGame(points: List<Player>) {
    val game = listOf("Love", "15", "30", "40")
    var p1Points = 0
    var p2Points = 0
    for (winner in points) {
        when (winner) {
            Player.P1 -> p1Points += 1
            Player.P2 -> p2Points += 1
        }

        if (p1Points == 4 && p2Points == 4) {
            p1Points -= 1
            p2Points -= 1
        }

        when {
            p1Points == 3 && p2Points == 3 -> println("Deuce")
            p1Points == 4 && p2Points == 3 -> println("Ventaja P1")
            p1Points == 3 && p2Points == 4 -> println("Ventaja P2")
            p1Points == 5 || (p1Points == 4 && p2Points < 4) -> {
                println("Ha ganado el P1")
                return
            }
            p2Points == 5 || (p2Points == 4 && p1Points < 4) -> {
                println("Ha ganado el P2")
                return
            }
            else -> println("${game[p1Points]} - ${game[p2Points]}")
        }
    }
    println("Faltan puntos para definir un ganador")
}