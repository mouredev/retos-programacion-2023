import kotlin.system.exitProcess

val playersPoints = listOf<String>("Love", "15", "30", "40")
var player1Points = 0
var player2Points = 0
var deucePoints1 = 0
var deucePoints2 = 0

fun main() {
    println("Para ingresar los puntos de cada jugador ingrese P1 o P2 según corresponda:")
    game()
}

private fun game() {
    when (readln()) {

        "P1" -> {
            player1Points++
            if (player1Points > 3) {
                println("Ha ganado el P1")
                exitProcess(0)
            }
            if (player1Points == 3 && player2Points == 3) {
                println("Deuce")
                deuce()
                return
            }
            println("${playersPoints[player1Points]} - ${playersPoints[player2Points]}")
            game()
        }

        "P2" -> {
            player2Points++
            if (player2Points > 3) {
                println("Ha ganado el P2")
                exitProcess(0)
            }
            if (player1Points == 3 && player2Points == 3) {
                println("Deuce")
                deuce()
                return
            }
            println("${playersPoints[player1Points]} - ${playersPoints[player2Points]}")
            game()
        }
        else -> {
            println("Ingresa P1 o P2")
            game()
        }
    }
}

fun deuce() {
    when (readln()) {
        "P1" -> {
            deucePoints1++
            if (deucePoints1 > deucePoints2 && deucePoints1 - deucePoints2 == 1) {
                println("Ventaja P1")
                deuce()
            } else if (deucePoints1 == deucePoints2) {
                println("Deuce")
                deuce()
            } else {
                println("Ha ganado el P1")
                exitProcess(0)
            }
        }
        "P2" -> {
            deucePoints2++
            if (deucePoints2 > deucePoints1 && deucePoints2 - deucePoints1 == 1) {
                println("Ventaja P2")
                deuce()
            } else if (deucePoints1 == deucePoints2) {
                println("Deuce")
                deuce()
            } else {
                println("Ha ganado el P2")
                exitProcess(0)
            }
        }
    }
}
