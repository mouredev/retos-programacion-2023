fun main() {
    calculateWinner(winnerList = listOf("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"))
}

fun calculateWinner(winnerList: List<String>) {
    val scores = listOf("Love", "15", "30", "40")

    val player1 = "p1"
    val player2 = "p2"

    var player1Points = 0
    var player2Points = 0

    println("P1 - P2")

    winnerList.forEach { winner ->

        when (winner.lowercase()) {
            player1 -> player1Points += 1
            player2 -> player2Points += 1
            else -> return@forEach
        }

        if (player1Points == player2Points && player1Points == 3) println("Deuce")
        else if (player1Points == 4) println("ventaja P1")
        else if (player2Points == 4) println("ventaja P2")
        else if (player1Points == 5) {
            println("Ha ganado el P1")
            return
        } else if (player2Points == 5) {
            println("Ha ganado el P2")
            return
        } else if (player1Points > 5 || player2Points > 5) return
        else println("${scores[player1Points]} - ${scores[player2Points]}")
    }
}