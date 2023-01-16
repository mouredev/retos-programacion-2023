import kotlin.math.abs

fun main() {
    tenisGame(
            arrayOf(
                    Player.P1,
                    Player.P1,
                    Player.P2,
                    Player.P2,
                    Player.P1,
                    Player.P2,
                    Player.P1,
                    Player.P1
            )
    )

    tenisGame(
            arrayOf(
                    Player.P1,
                    Player.P1,
                    Player.P2,
                    Player.P2,
                    Player.P1,
                    Player.P2,
                    Player.P1,
                    Player.P1,
                    Player.P2,
                    Player.P1
            )
    )

    tenisGame(arrayOf(Player.P1, Player.P1, Player.P1, Player.P1, Player.P1, Player.P1))

    tenisGame(arrayOf(Player.P1, Player.P1))
}

enum class Player {
    P1,
    P2
}

private fun tenisGame(points: Array<Player>) {

    val game = arrayOf("Love", "15", "30", "40")
    var p1Points = 0
    var p2Points = 0
    var finished = false
    var error = false

    points.forEach { player ->
        error = finished

        p1Points += if (player == Player.P1) 1 else 0
        p2Points += if (player == Player.P2) 1 else 0

        if (p1Points >= 3 && p2Points >= 3) {
            if (!finished && abs(p1Points - p2Points) <= 1) {
                println(
                        if (p1Points == p2Points) "Deuce"
                        else if (p1Points > p2Points) "Ventaja P1" else "Ventaja P2"
                )
            } else {
                finished = true
            }
        } else {
            if (p1Points < 4 && p2Points < 4) {
                println("${game[p1Points]} - ${game[p2Points]}")
            } else {
                finished = true
            }
        }
    }

    println(
            if (error || !finished) "Los puntos jugados no son correctos"
            else if (p1Points > p2Points) "Ha ganado el P1" else "Ha ganado el P2"
    )
}
