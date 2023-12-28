fun main() {
    val gamePoints = listOf("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1")

    var player1Points = 0
    var player2Points = 0
    var gameOver = false
    var winner = ""

    gamePoints.forEach { point ->
        when (point) {
            "P1" -> player1Points += 1
            "P2" -> player2Points += 1
        }

        var player1Score = when (player1Points) {
            0 -> "Love"
            1 -> "15"
            2 -> "30"
            3 -> "40"
            else -> ""
        }
        var player2Score = when (player2Points) {
            0 -> "Love"
            1 -> "15"
            2 -> "30"
            3 -> "40"
            else -> ""
        }

        if (player1Points >= 4 && player1Points - player2Points >= 2) {
            gameOver = true
            winner = "P1"
        } else if (player2Points >= 4 && player2Points - player1Points >= 2) {
            gameOver = true
            winner = "P2"
        } else if (player1Points == 4 && player2Points == 4) {
            player1Score = "Deuce"
            player2Score = "Deuce"
        } else if (player1Points == 5 && player2Points == 4) {
            player1Score = "Ventaja P1"
            player2Score = "Deuce"
        } else if (player1Points == 4 && player2Points == 5) {
            player1Score = "Deuce"
            player2Score = "Ventaja P2"
        }

        println("$player1Score - $player2Score")

        if (gameOver) {
            println("Ha ganado el $winner")
            return
        }
    }
}