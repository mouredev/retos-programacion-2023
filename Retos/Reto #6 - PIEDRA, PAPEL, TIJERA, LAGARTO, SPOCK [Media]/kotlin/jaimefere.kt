private enum class Move(var symbol: String) {
    ROCK("🗿"), PAPER("📄"), SCISSORS("✂️"), ALLIGATOR("🦎"),  SPOCK("🖖")
}

private fun playRockPaperScissorsAlligatorSpock(games: Array<Pair<String, String>>): String {
    var playerOneWins = 0
    var playerTwoWins = 0

    games.forEach { game ->
        val playerOneMove = Move.values().first { it.symbol == game.first }
        val playerTwoMove = Move.values().first { it.symbol == game.second }
        if(playerOneMove != playerTwoMove) {
            if ((playerOneMove == Move.SCISSORS && playerTwoMove == Move.PAPER) ||
                (playerOneMove == Move.PAPER && playerTwoMove == Move.ROCK) ||
                (playerOneMove == Move.ROCK && playerTwoMove == Move.ALLIGATOR) ||
                (playerOneMove == Move.ALLIGATOR && playerTwoMove == Move.SPOCK) ||
                (playerOneMove == Move.SPOCK && playerTwoMove == Move.SCISSORS) ||
                (playerOneMove == Move.SCISSORS && playerTwoMove == Move.ALLIGATOR) ||
                (playerOneMove == Move.ALLIGATOR && playerTwoMove == Move.PAPER) ||
                (playerOneMove == Move.PAPER && playerTwoMove == Move.SPOCK) ||
                (playerOneMove == Move.SPOCK && playerTwoMove == Move.ROCK) ||
                (playerOneMove == Move.ROCK && playerTwoMove == Move.SCISSORS)) {
                playerOneWins++
            } else {
                playerTwoWins++
            }
        }
    }

    return if(playerOneWins == playerTwoWins) "Tie" else if(playerOneWins > playerTwoWins) "Player 1" else "Player 2"
}

fun main() {
    println(playRockPaperScissorsAlligatorSpock(arrayOf(Pair("🗿","✂️"), Pair("✂️","🗿"), Pair("📄","✂️"))))
}