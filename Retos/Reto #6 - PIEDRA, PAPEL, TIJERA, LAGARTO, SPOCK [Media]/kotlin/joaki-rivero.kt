fun main() {
    rockPaperScissorsLizardSpock(listOf(Pair("🗿", "✂️"), Pair("✂️", "🗿"), Pair("📄", "✂️")))
}

fun rockPaperScissorsLizardSpock(gameSet: List<Pair<String, String>>) {
    var player1 = 0
    var player2 = 0

    gameSet.forEach { set ->
        val winner = getWinner(Pair(set.first, set.second))
        if (winner == 1) player1 += 1 else if (winner == 2) player2 += 1
    }

    if (player1 == player2) println("Tie")
    else if (player1 > player2) println("Player 1")
    else println("Player 2")
}

fun getWinner(set: Pair<String, String>): Int {
    val options = listOf("🗿", "📄", "✂️", "🦎", "🖖")
    if (set.first == set.second || !options.contains(set.first) || !options.contains(set.second)) return 0

    var winner = 0
    when (set.first) {
        "🗿" -> winner = if (set.second == "🦎" || set.second == "✂️") 1 else 2
        "📄" -> winner = if (set.second == "🗿" || set.second == "🖖") 1 else 2
        "✂️" -> winner = if (set.second == "📄" || set.second == "🦎") 1 else 2
        "🦎" -> winner = if (set.second == "🖖" || set.second == "📄") 1 else 2
        "🖖" -> winner = if (set.second == "🗿" || set.second == "✂️") 1 else 2
    }
    return winner
}
