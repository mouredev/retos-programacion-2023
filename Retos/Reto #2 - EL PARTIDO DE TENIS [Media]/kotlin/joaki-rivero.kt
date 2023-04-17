const val PLAYER_ONE = "P1"
const val PLAYER_TWO = "P2"

fun main() {
    playTennis()
}

fun playTennis() {
    val score = mapOf(0 to "Love", 1 to "15", 2 to "30", 3 to "40")
    var playing = true
    var p1Score = 0
    var p2Score = 0

    println("----- Tennis Match -----\n")

    do {
        print("¿Qué jugador ha anotado, $PLAYER_ONE o $PLAYER_TWO?: ")
        val player = readln().uppercase()

        if (player != PLAYER_ONE && player != PLAYER_TWO) {
            println("Jugador $player no reconocido. Introduzca  $PLAYER_ONE o $PLAYER_TWO.\n")
            continue
        }

        if (player == PLAYER_ONE) p1Score += 1 else p2Score += 1

        if (p1Score == 3 && p2Score == 3) {
            println("Deuce\n")
            continue
        }

        if (p1Score > 3 || p2Score > 3) {
            when {
                p1Score - p2Score >= 2 -> {
                    println("Ha ganado el $PLAYER_ONE")
                    playing = false
                }

                p2Score - p1Score >= 2 -> {
                    println("Ha ganado el $PLAYER_TWO")
                    playing = false
                }

                p1Score == p2Score -> println("Deuce\n")
                p1Score > p2Score -> println("Ventaja $PLAYER_ONE\n")
                else -> println("Ventaja $PLAYER_TWO\n")
            }
        } else {
            println("${score[p1Score]} - ${score[p2Score]}\n")
        }
    } while (playing)

    println("\n----- ------- -----")
}
