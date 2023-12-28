fun main() {
    TennisMatch(listOf("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"))
    TennisMatch(listOf("P1", "P1", "P1", "P2", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2"))
}

private fun TennisMatch(players: List<String>) {
    var p1Points = 0
    var p2Points = 0

    players.forEach { player ->
        when (player.uppercase()) {
            "P1" -> p1Points++
            "P2" -> p2Points++
            else -> {
                println("Error en el tanteo")
                return
            }
        }

        if ((p1Points == 4) && (p2Points == 4)) {
            p1Points = 3
            p2Points = 3
        }

        // Imprimir resultado
        PrintScore(p1Points, p2Points)
    }
}

private fun PrintScore(P1: Int, P2: Int) {

    val score: Map<Int, String> = mapOf(0 to "Love", 1 to "15", 2 to "30", 3 to "40")

    if ((P1 == P2) and (P1 == 3)) {
        println("\tDeuce")
    } else if ((P1 == 4) and (P2 == 3)) {
        println("\tVentaja P1")
    } else if ((P2 == 4) and (P1 == 3)) {
        println("\tVentaja P2")
    } else if ((P1 == 5) and (P1 - P2 == 2)) {
        println("\tGana P1")
    } else if ((P2 == 5) and (P2 - P1 == 2)) {
        println("\tGana P2")
    } else {
        println("P1:\t ${score[P1]} - ${score[P2]} \t:P2")
    }
}
