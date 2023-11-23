fun main() {
    println("-------Partido de Tenis------- \n")
    play()
}

fun points(point: Int): String {
    return when(point) {
        1 -> "15"
        2 -> "30"
        3 -> "40"
        else -> "Love"
    }
}

fun random(start: Int, end: Int): Int {
    require(start <= end) {"No válido"}
    return (start..end).random()
}

fun play()  {
    var playerOne = 0
    var playerTwo= 0

    while (playerTwo < 3 && playerOne < 3) {
        if (random(1, 2) == 1) playerOne++
        else playerTwo++

        println("Player 1: ${points(playerOne)} -- Player 2: ${points(playerTwo)}")

        Thread.sleep(1000)
    }

    if (playerOne == playerTwo) {
        println("Empate")
        return
    }
    if (playerOne > playerTwo) println("\n-----¡¡Ganador Player 1!!-----")
    else println("\n-----¡¡Ganador Player 2!!-----")
}

