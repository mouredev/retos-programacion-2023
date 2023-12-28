fun main() {
    val rounds = listOf(
        Pair("🗿", "✂️"),
        Pair("✂️", "🗿"),
        Pair("📄", "✂️")
    )

    val result = calculateWinner(rounds)

    println("El ganador es $result")
}

fun calculateWinner(rounds: List<Pair<String, String>>): String {
    var player1Score = 0
    var player2Score = 0

    rounds.forEach { round ->
        val player1Choice = round.first
        val player2Choice = round.second

        when {
            player1Choice == player2Choice -> {
                // Empate
            }
            player1Choice == "🗿" && (player2Choice == "✂️" || player2Choice == "🦎") -> {
                // Gana jugador 1
                player1Score++
            }
            player1Choice == "✂️" && (player2Choice == "📄" || player2Choice == "🦎") -> {
                // Gana jugador 1
                player1Score++
            }
            player1Choice == "📄" && (player2Choice == "🗿" || player2Choice == "🖖") -> {
                // Gana jugador 1
                player1Score++
            }
            player1Choice == "🦎" && (player2Choice == "📄" || player2Choice == "🖖") -> {
                // Gana jugador 1
                player1Score++
            }
            player1Choice == "🖖" && (player2Choice == "🗿" || player2Choice == "✂️") -> {
                // Gana jugador 1
                player1Score++
            }
            else -> {
                // Gana jugador 2
                player2Score++
            }
        }
    }

    return when {
        player1Score > player2Score -> "Player 1"
        player2Score > player1Score -> "Player 2"
        else -> "Tie"
    }
}
