fun main() {
    val p1 = Player(name = "P1")
    val p2 = Player(name = "P2")

    println("P1 - P2\n---------")

    do {
        val pointWinner = getPlayerPointWinner(p1, p2)
        when (pointWinner.state) {
            ZERO -> {
                pointWinner.state = FIFTEEN
                printRegularTableResults(p1, p2)
            }

            FIFTEEN -> {
                pointWinner.state = THIRTEEN
                printRegularTableResults(p1, p2)
            }

            THIRTEEN -> {
                if (p1.state == FOURTEEN || p2.state == FOURTEEN) {
                    setPlayersDeuce(p1, p2)
                    println("Deuce")
                } else {
                    pointWinner.state = FOURTEEN
                    printRegularTableResults(p1, p2)
                }
            }

            DEUCE -> {
                if (p1.state == ADVANTAGE || p2.state == ADVANTAGE) {
                    setPlayersDeuce(p1, p2)
                    println("Deuce")
                } else {
                    pointWinner.state = ADVANTAGE
                    println("Ventaja ${pointWinner.name}")
                }
            }

            FOURTEEN, ADVANTAGE -> {
                println("Ha ganado el ${pointWinner.name}")
                break
            }
        }
    } while (true)
}

private fun getPlayerPointWinner(player1: Player, player2: Player) = listOf(player1, player2).random()

private fun setPlayersDeuce(p1: Player, p2: Player) {
    p1.state = DEUCE
    p2.state = DEUCE
}

private fun printRegularTableResults(p1: Player, p2: Player) {
    println("${p1.state.value} - ${p2.state.value}")
}

data class Player(val name: String, var state: PlayerState = ZERO)

enum class PlayerState(val value: String) {
    ZERO("Love"),
    FIFTEEN("15"),
    THIRTEEN("30"),
    FOURTEEN("40"),
    DEUCE("Deuce"),
    ADVANTAGE("Adv")
}
