import kotlin.math.abs

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

fun main(){
    tenisGame(arrayOf(Player.P1, Player.P1, Player.P1, Player.P1))
    tenisGame(arrayOf(Player.P1, Player.P1, Player.P1, Player.P1, Player.P1, Player.P1))
}

enum class Player {
    P1,
    P2
}

private fun tenisGame(game: Array<Player>) {

    val scores = arrayOf("Love", "15", "30", "40")
    var pointsP1 = 0
    var pointsP2 = 0
    var finished = false
    var error = false
    game.forEach { player ->
        error = finished
        if (player == Player.P1) pointsP1 += 1
        if (player == Player.P2) pointsP2 += 1
        if (pointsP1 >= 3 && pointsP2 >= 3){
            if (!finished && abs(pointsP1 - pointsP2) <= 1){
                if (pointsP1 == pointsP2) println("Deuce")
                else if ( pointsP1 > pointsP2) println("Ventaja P1") else println("Ventaja P2")
            } else {
                finished = true
            }
        }else{
            if(pointsP1 < 4 && pointsP2 < 4){
                println("${scores[pointsP1]} - ${scores[pointsP2]}")
            }else{
                finished = true
            }
        }
    }

    if ( error || !finished){
        println("Error en los puntos")
    }else if (pointsP1 > pointsP2){
        println("Gana P1")
    }else{
        println("Gana P2")
    }
}