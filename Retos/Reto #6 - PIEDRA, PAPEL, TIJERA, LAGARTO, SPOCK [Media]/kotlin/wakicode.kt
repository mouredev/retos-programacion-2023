fun main(args: Array<String>) {

    val jugada0 = listOf(Pair("🗿", "✂️"), Pair("✂️", "🗿"), Pair("📄", "✂️"))
    val jugada1 = listOf(Pair("🦎", "🦎"), Pair("🦎", "🗿"), Pair("🖖", "✂️"), Pair("📄", "🗿"))
    val jugada2 = listOf(Pair("✂️", "🖖"), Pair("🗿", "📄"), Pair("🦎", "🗿"), Pair("🖖", "🦎"))
    val jugada3 = listOf(Pair("🖖", "✂️"), Pair("🗿", "🗿"), Pair("✂️", "✂️"), Pair("🖖", "📄"))

    println(play(jugada0))
    println(play(jugada1))
    println(play(jugada2))
    println(play(jugada3))
}


fun play(moves: List<Pair<String, String>>): String {

    var player1 = 0
    var player2 = 0

    val values = arrayOf(
        intArrayOf(1, 0, 1, 0, 1),
        intArrayOf(1, 1, 0, 1, 0),
        intArrayOf(0, 1, 1, 0, 1),
        intArrayOf(1, 0, 1, 1, 0),
        intArrayOf(0, 1, 0, 1, 1)
    )

    val items = listOf("🗿", "📄", "✂️", "🦎", "🖖")

    moves.forEach {
        player1 += values[items.indexOf(it.first)][items.indexOf(it.second)]
        player2 += values[items.indexOf(it.second)][items.indexOf(it.first)]
    }
    return if (player1 > player2) "Player 1" else if (player2 == player1) "Tie" else "Player 2"
}

