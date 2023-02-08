
fun main() {

    play("🗿", "🦎")
    play("📄", "🦎")
    play("✂️", "🗿")
    play("🖖", "📄")
    play("🗿", "🦎")
    play("📄", "🖖")
    play("🖖", "🦎")
    play("🖖", "🖖")
    play("✂️", "✂️")
}

private fun play(player1: String, player2: String) {

    val values = mapOf(
        "🗿" to 1,
        "📄" to 7,
        "✂️" to 12,
        "🦎" to 15,
        "🖖" to 23,
    )
    val result = values[player1]!! + values[player2]!!
    val winner = if(values[player2]!! == values[player1]!!) "tie!"
    else
        when(result) {
            8 -> if(values[player2]!! > values[player1]!!) "player2" else "player1"
            13 -> if(values[player2]!! < values[player1]!!) "player2" else "player1"
            16 -> if(values[player2]!! < values[player1]!!) "player2" else "player1"
            24 -> if(values[player2]!! > values[player1]!!) "player2" else "player1"
            19 -> if(values[player2]!! > values[player1]!!) "player2" else "player1"
            22 -> if(values[player2]!! > values[player1]!!) "player2" else "player1"
            30 -> if(values[player2]!! < values[player1]!!) "player2" else "player1"
            27 -> if(values[player2]!! < values[player1]!!) "player2" else "player1"
            35 -> if(values[player2]!! > values[player1]!!) "player2" else "player1"
            38 -> if(values[player2]!! < values[player1]!!) "player2" else "player1"
            else -> "wrong input"
        }
    println("player1: $player1 / player2: $player2")
    if (winner != "tie!") println("$winner wins!") else println(winner)
    println()

}