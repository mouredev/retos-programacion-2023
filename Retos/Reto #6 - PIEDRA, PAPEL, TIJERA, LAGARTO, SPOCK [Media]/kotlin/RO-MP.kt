

val ganadores = mutableMapOf<String, List<String>>()

fun main(){
    setWinners()
    val juego = play(10)


    val winner = getWinner(juego)
    if (winner != "Tie") println("The winner was: $winner")
    else println("It was a Tie")

}


fun play(times: Int): List<List<String>> {
    val juego = mutableListOf<List<String>>()
    repeat(times){
        juego.add(listOf(OPCIONES.values().random().toString(), OPCIONES.values().random().toString()))
    }
    println(juego)
    return juego
}


fun getWinner(game: List<List<String>>): String{
    val score = mutableListOf(0, 0)

    game.forEach { match ->
        ganadores[match[0]]?.contains(match[1])?.apply {
            if (this) score[0] = score[0] + 1
            else score[1] = score[1] + 1
        }
    }
    println(score)
    return when{
        score[0]>score[1] ->  "Player 1"
        score[1]>score[0] ->  "Player 2"
        else -> "Tie"
    }

}

fun setWinners(){
    ganadores[OPCIONES.PIEDRA.toString()] =
        listOf(OPCIONES.LAGARTO.toString(), OPCIONES.TIJERA.toString())

    ganadores[OPCIONES.PAPEL.toString()] =
        listOf(OPCIONES.PIEDRA.toString(), OPCIONES.SPOCK.toString())

    ganadores[OPCIONES.TIJERA.toString()] =
        listOf(OPCIONES.LAGARTO.toString(), OPCIONES.PAPEL.toString())

    ganadores[OPCIONES.LAGARTO.toString()] =
        listOf(OPCIONES.PAPEL.toString(), OPCIONES.SPOCK.toString())

    ganadores[OPCIONES.SPOCK.toString()] =
        listOf(OPCIONES.PIEDRA.toString(), OPCIONES.TIJERA.toString())
}

enum class OPCIONES{
    PIEDRA,
    PAPEL,
    TIJERA,
    LAGARTO,
    SPOCK
}

