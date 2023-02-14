fun main() {
    val game01 = listOf(Pair("🗿","✂️"), Pair("✂️","🗿"), Pair("📄","✂️"));
    val game02 = listOf(Pair("✂️","✂️"), Pair("🗿","🗿"), Pair("📄","📄"));
    val game03 = listOf(Pair("🖖","✂️"), Pair("🖖","🗿"), Pair("📄","✂️"));
    println(whoWins(game01))
    println(whoWins(game02))
    println(whoWins(game03))
}

fun whoWins(games: List<Pair<String, String>>): String {
    var player1Score = 0
    var player2Score = 0
    val ruleMap = mapOf(
        "🗿" to setOf("✂️", "🦎"),
        "✂️" to setOf("📄", "🦎"),
        "📄" to setOf("🗿", "🖖"),
        "🦎" to setOf("📄", "🖖"),
        "🖖" to setOf("✂️", "🗿")
    )

    for (game in games) {
        if (ruleMap[game.second]?.contains(game.first) == true) {
            player2Score++
        } else if (ruleMap[game.first]?.contains(game.second) == true) {
            player1Score++
        }
    }

    return when {
        player1Score > player2Score -> "Player 1"
        player2Score > player1Score -> "Player 2"
        else -> "Tie"
    }
}