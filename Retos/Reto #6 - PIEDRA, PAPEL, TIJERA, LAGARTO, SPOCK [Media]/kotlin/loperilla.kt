fun main() {
    print(
        match(
            PLAY(MOVEMENTS.PIEDRA,MOVEMENTS.TIJERA),
            PLAY(MOVEMENTS.PIEDRA,MOVEMENTS.PAPEL),
            PLAY(MOVEMENTS.LAGARTO,MOVEMENTS.PIEDRA),
            PLAY(MOVEMENTS.PIEDRA,MOVEMENTS.SPOCK),
            PLAY(MOVEMENTS.PIEDRA,MOVEMENTS.LAGARTO),
            PLAY(MOVEMENTS.SPOCK,MOVEMENTS.PIEDRA),
            PLAY(MOVEMENTS.PIEDRA,MOVEMENTS.PIEDRA),
            PLAY(MOVEMENTS.PAPEL,MOVEMENTS.TIJERA)
        )
    )
}

enum class MOVEMENTS {
    PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK
}

// "🗿": ["✂️", "🦎"],
// "📄": ["🗿", "🖖"],
// "✂️" : ["📄","🦎"],
// "🦎": ["📄","🖖"],
// "🖖": ["✂️","🗿"]  
private val MOVEMENT_COUNTERS = mapOf(
    MOVEMENTS.PIEDRA to listOf<MOVEMENTS>(MOVEMENTS.TIJERA, MOVEMENTS.LAGARTO),
    MOVEMENTS.PAPEL to listOf<MOVEMENTS>(MOVEMENTS.PIEDRA, MOVEMENTS.SPOCK),
    MOVEMENTS.TIJERA to listOf<MOVEMENTS>(MOVEMENTS.PAPEL, MOVEMENTS.LAGARTO),
    MOVEMENTS.LAGARTO to listOf<MOVEMENTS>(MOVEMENTS.PAPEL, MOVEMENTS.SPOCK),
    MOVEMENTS.SPOCK to listOf<MOVEMENTS>(MOVEMENTS.TIJERA, MOVEMENTS.PIEDRA)
)

data class PLAY(val player1Move: MOVEMENTS, val player2Movie: MOVEMENTS) {
    fun checkEquals() = player1Move == player2Movie
}

private fun match(vararg plays:PLAY) {
    var player1CountWins = 0
    var player2CountWins = 0
    var tiesCount = 0
    plays.forEach {
        if(it.checkEquals()) 
            tiesCount++
        else 
            if(checkPlayer1Win(it)) {
                player1CountWins++
            } else {
                player2CountWins++
            }
    }

    println(calculateWinnerMessage(player1CountWins, player2CountWins, tiesCount))
}

/*
    Al comprobar previamente si ambos jugadores sacan el mismo movimiento,
    aquí devuelve true si la jugada del 1 vence a la del 2
*/
private fun checkPlayer1Win(play: PLAY): Boolean {
    val counters: List<MOVEMENTS> = MOVEMENT_COUNTERS.getValue(play.player1Move)
    return counters.contains(play.player2Movie)
}

private fun calculateWinnerMessage(player1Wins: Int, player2Wins: Int, tieCount: Int): String {
    println(player1Wins)
    println(player2Wins)
    println(tieCount)
    return when {
        player1Wins > player2Wins -> {
            "Gana player 1"
        }
        player2Wins > player1Wins -> {
            "Gana player 2"
        }
        else -> {
            "Empate"
        }
    }
} 