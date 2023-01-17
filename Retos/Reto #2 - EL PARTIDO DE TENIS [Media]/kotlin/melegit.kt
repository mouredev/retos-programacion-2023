package reto2

/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 *
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
 */
fun main() {
    runGameSequence(
        listOf(
            PlayerType.PLAYER1.playerName,
            PlayerType.PLAYER1.playerName,
            PlayerType.PLAYER2.playerName,
            PlayerType.PLAYER2.playerName,
            PlayerType.PLAYER1.playerName,
            PlayerType.PLAYER2.playerName,
            PlayerType.PLAYER1.playerName,
            PlayerType.PLAYER1.playerName,
        )
    )
}

fun runGameSequence(sequence: List<String>) {
    sequence.forEach { pointPlayer ->
        println(updateScorePanel(pointPlayer))
    }
}

fun updateScorePanel(Player: String): String {
    return when (Player) {
        PlayerType.PLAYER1.playerName -> {
            if (!isPlayOver) player1IndexPoints += 1
            getCurrentResult()
        }
        PlayerType.PLAYER2.playerName -> {
            if (!isPlayOver) player2IndexPoints += 1
            getCurrentResult()
        }
        else -> resultStatusList[9]
    }
}

private fun getCurrentResult(): String =
    when {
        isPlayOver && player1IndexPoints > player2IndexPoints -> resultStatusList[10] + " " + resultStatusList[7]
        isPlayOver && player1IndexPoints > player2IndexPoints -> resultStatusList[10] + " " + resultStatusList[8]
        (player1IndexPoints >= 3 && player2IndexPoints >= 3) && (player1IndexPoints == player2IndexPoints) -> resultStatusList[4]
        (player1IndexPoints >= 3 && player2IndexPoints >= 3) && (player1IndexPoints - player2IndexPoints == 1) -> resultStatusList[5]
        (player1IndexPoints >= 3 && player2IndexPoints >= 3) && (player2IndexPoints - player1IndexPoints == 1) -> resultStatusList[6]
        (player1IndexPoints >= 3) && (player1IndexPoints - player2IndexPoints == 2) -> {
            isPlayOver = true
            resultStatusList[7]
        }
        (player2IndexPoints >= 3) && (player2IndexPoints - player1IndexPoints == 2) -> {
            isPlayOver = true
            resultStatusList[8]
        }
        else -> resultStatusList[player1IndexPoints] + " - " + resultStatusList[player2IndexPoints]
    }

enum class PlayerType(val playerName: String) {
    PLAYER1(playerName = "P1"),
    PLAYER2(playerName = "P2"),
}

var player1IndexPoints = 0
var player2IndexPoints = 0
var isPlayOver: Boolean = false

val resultStatusList = arrayListOf(
    "Love",
    "15",
    "30",
    "40",
    "Deuce",
    "Ventaja P1",
    "Ventaja P2",
    "Ha ganado el P1",
    "Ha ganado el P2",
    "Info incorrecta",
    "Partido finalizado"
)

