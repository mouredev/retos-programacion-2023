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
    var player1Wins = 0
    var playsToCheck = plays.asList().filter { !it.checkEquals() }
    playsToCheck.forEach {
        if(checkPlayer1Win(it)) {
            player1Wins++
        } else {
            player1Wins--
        }
        println(player1Wins)
    }

    println(calculateWinnerMessage(player1Wins))
}

/*
    Al comprobar previamente si ambos jugadores sacan el mismo movimiento,
    aquí devuelve true si la jugada del 1 vence a la del 2
*/
private fun checkPlayer1Win(play: PLAY): Boolean {
    val counters: List<MOVEMENTS> = MOVEMENT_COUNTERS.getValue(play.player1Move)
    return counters.contains(play.player2Movie)
}

private fun calculateWinnerMessage(player1CountWins: Int): String {
    if(player1CountWins == 0) {
        return "Empate"
    }
    return "Gana el jugador ${if(player1CountWins > 0) 1 else { 2 }}"
} 