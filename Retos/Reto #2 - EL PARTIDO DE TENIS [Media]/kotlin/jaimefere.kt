private enum class Player {
    P1, P2
}

private enum class Score {
    LOVE_LOVE, LOVE_FIFTEEN, LOVE_THIRTY, LOVE_FORTY,
    FIFTEEN_LOVE, FIFTEEN_FIFTEEN, FIFTEEN_THIRTY, FIFTEEN_FORTY,
    THIRTY_LOVE, THIRTY_FIFTEEN, THIRTY_THIRTY, THIRTY_FORTY,
    FORTY_LOVE, FORTY_FIFTEEN, FORTY_THIRTY, FORTY_FORTY,
    DEUCE,
    P1_ADVANTAGE, P2_ADVANTAGE,
    P1_WIN, P2_WIN,
    ERROR;


    companion object {
        fun playPoint(obj: Score, pointWinner: Player): Score {
            return when(obj) {
                LOVE_LOVE -> if(pointWinner == Player.P1) FIFTEEN_LOVE else LOVE_FIFTEEN
                LOVE_FIFTEEN -> if(pointWinner == Player.P1) FIFTEEN_FIFTEEN else LOVE_THIRTY
                LOVE_THIRTY -> if(pointWinner == Player.P1) FIFTEEN_THIRTY else LOVE_FORTY
                LOVE_FORTY -> if(pointWinner == Player.P1) FIFTEEN_FORTY else P2_WIN
                FIFTEEN_LOVE -> if(pointWinner == Player.P1) THIRTY_LOVE else FIFTEEN_FIFTEEN
                FIFTEEN_FIFTEEN -> if(pointWinner == Player.P1) THIRTY_FIFTEEN else LOVE_FIFTEEN
                FIFTEEN_THIRTY -> if(pointWinner == Player.P1) FIFTEEN_LOVE else FIFTEEN_THIRTY
                FIFTEEN_FORTY -> if(pointWinner == Player.P1) FORTY_FORTY else P2_WIN
                THIRTY_LOVE -> if(pointWinner == Player.P1) FORTY_LOVE else THIRTY_FIFTEEN
                THIRTY_FIFTEEN -> if(pointWinner == Player.P1) P1_WIN else LOVE_FIFTEEN
                THIRTY_THIRTY -> if(pointWinner == Player.P1) FIFTEEN_LOVE else THIRTY_THIRTY
                THIRTY_FORTY -> if(pointWinner == Player.P1) FORTY_FORTY else P2_WIN
                FORTY_LOVE -> if(pointWinner == Player.P1) P1_WIN else FORTY_FIFTEEN
                FORTY_FIFTEEN -> if(pointWinner == Player.P1) P1_WIN else FORTY_THIRTY
                FORTY_THIRTY -> if(pointWinner == Player.P1) P1_WIN else FORTY_FORTY
                FORTY_FORTY, DEUCE -> if(pointWinner == Player.P1) P1_ADVANTAGE else P2_ADVANTAGE
                P1_ADVANTAGE -> if(pointWinner == Player.P1) P1_WIN else DEUCE
                P2_ADVANTAGE -> if(pointWinner == Player.P1) P2_WIN else DEUCE
                else -> ERROR
            }
        }
        fun getName(obj: Score): String {
            return when(obj) {
                LOVE_LOVE -> "Nada - Nada"
                LOVE_FIFTEEN -> "Nada - 15"
                LOVE_THIRTY -> "Nada - 30"
                LOVE_FORTY -> "Nada - 40"
                FIFTEEN_LOVE -> "15 - Nada"
                FIFTEEN_FIFTEEN -> "15 - 15"
                FIFTEEN_THIRTY -> "15 - 30"
                FIFTEEN_FORTY -> "15 - 40"
                THIRTY_LOVE -> "30 - Nada"
                THIRTY_FIFTEEN -> "30 - 15"
                THIRTY_THIRTY -> "30 - Nada"
                THIRTY_FORTY -> "30 - 40"
                FORTY_LOVE -> "40 - Nada"
                FORTY_FIFTEEN -> "40 - 15"
                FORTY_THIRTY -> "40 - 30"
                FORTY_FORTY -> "40 - 40"
                DEUCE -> "Empate"
                P1_ADVANTAGE -> "Ventaja P1"
                P2_ADVANTAGE -> "Ventaja P2"
                P1_WIN -> "Ha ganado P1"
                P2_WIN -> "Ha ganado P2"
                ERROR -> "Puntuación de entrada errónea"
            }
        }
    }
}

private fun playGame(points: Array<Player>) {
    var score = Score.LOVE_LOVE

    points.forEach { pointWinner ->
        println(Score.getName(score))
        score = Score.playPoint(score, pointWinner)
    }
    println(Score.getName(score))
}

fun main() {
    playGame(arrayOf(Player.P1, Player.P1, Player.P1, Player.P2, Player.P2, Player.P2, Player.P1, Player.P2, Player.P1, Player.P1))
}