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
    tennisMatch(listOf("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"))
    tennisMatch(listOf("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1", "P2"))
    tennisMatch(listOf("P2", "P3", "P1", "P1", "P2", "P1", "P2", "P2"))
    tennisMatch(listOf("P2", "P2", "P1", "P1", "P2", "P1", "P2", "P2"))
}


class Player() {
    val scores : List<String> = listOf("Love", "15", "30", "40")

    var score : String = "Love"
    var value : Int = 0

    fun updateScore() {
        if (this.value < 4) {
            this.score = scores[this.value]
        } else {
            this.score = scores[3]
        }
    }
}


fun tennisMatch(points:List<String>) {
    val player1 = Player()
    val player2 = Player()
    var endMatch:Boolean = false

    println("\nRESULTADO DEL PARTIDO:\n")
    for (point in points) {
        if (endMatch) {
            println("\nYA HAY GANADOR!\nNo se tendrán en cuenta los puntos restantes!\n")
            break
        }

        if (point == "P1") {
            player1.value++
            player1.updateScore()
        } else if (point == "P2") {
            player2.value++
            player2.updateScore()
        } else {
            println("El dato no es correcto.")
            return
        }

        endMatch = checkWinner(player1, player2)
    }
}


fun checkWinner(p1:Player, p2:Player) : Boolean {
    if (p1.value == 3 && p2.value == 3) {
        println("Deuce")
    } else if (p1.value >= 4 || p2.value >= 4) {
        val pointsDifference : Int = p1.value - p2.value

        if (pointsDifference == 0) println("Deuce")
        else if (pointsDifference == 1) println("Ventaja P1")
        else if (pointsDifference == -1) println("Ventaja P2")

        else if (pointsDifference >= 2) {
            println("Ha ganado el P1")
            return true
        } else {
            println("Ha ganado el P2")
            return true
        }
    } else {
        println(p1.score + " - " + p2.score)
    }

    return false
}