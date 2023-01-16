fun main() {
    val scores = listOf("Love", "15", "30", "40")
    var p1Score = 0
    var p2Score = 0
    var point: String

    while (true) {
        println("Ingrese el punto del jugador 1 (P1) o el jugador 2 (P2):")
        point = readln()

        if (point != "P1" && point != "P2") {
            println("Entrada inválida. Por favor, ingrese P1 o P2.")
            continue
        }

        when (point) {
            "P1" -> p1Score++
            "P2" -> p2Score++
        }

        val scoreString = if (p1Score == p2Score) "Deuce"
            else if (p1Score > 3) "ventaja P1"
            else if (p2Score > 3) "ventaja P2"
            else "${scores[p1Score]} - ${scores[p2Score]}"

        println(scoreString)

        if ((p1Score >= 4 || p2Score >= 4) && Math.abs(p1Score - p2Score) >= 2) {
            val winnerPlayer = if (p1Score > p2Score) "P1" else "P2"
            println("Ha ganado el $winnerPlayer")
            break
        }
    }
}