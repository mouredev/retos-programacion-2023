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

package com.malopezrom.reto2

/**
 * Enum Score
 * Representa el score de un jugador
 */
enum class Score {
    LOVE,
    FIFTEEN,
    THIRTY,
    FORTY,
    ADVANTAGE,
}

/**
 * Enumerado de los jugadores
 * @type {{P1: string; P2: string}}
 */
enum class Players{
    P1,
    P2
}



fun matchPoint(gameSequence: List<Players>){

    val p1 = Player(Players.P1)
    val p2 = Player(Players.P2)

    gameSequence.forEach { point ->
        when (point) {
            Players.P1 -> {
                p1.point(p2)
                if(p1.hasWinner()){
                    println("Ganador: ${p1.name}")
                    return
                }
            }
            Players.P2 -> {
                p2.point(p1)
                if(p2.hasWinner()){
                    println("Ganador: ${p2.name}")
                    return
                }
            }
        }


        println("${p1.score} - ${p2.score}")

    }

    if(!p1.hasWinner() && !p2.hasWinner()){
         println("No hay ganador")
    }

}

/**
 * Clase Player.
 * Representa un jugador con su nombre y su puntacion
 */
data class Player(val name: Players, var score: Score = Score.LOVE){
        private var winnner = false

        /**
         * Lógica de puntuaación del juego.
         * Suma un punto al jugador que ha ganado el punto.
         * Si ambos jugadores tienen 40 puntos, se produce un empate (Deuce).
         * Si un jugador tiene ventaja, gana el juego.(Winner)
         * @param player Player que ha perdido el punto
         */
        fun point(player:Player){

            when(score){
                Score.LOVE -> score = Score.FIFTEEN
                Score.FIFTEEN -> score = Score.THIRTY
                Score.THIRTY -> score = Score.FORTY
                Score.FORTY -> {

                    when (player.score) {
                        Score.FORTY ->{ score = Score.ADVANTAGE  }
                        Score.ADVANTAGE ->{ score = Score.FORTY
                                            player.score = Score.FORTY
                        }
                        else -> winnner = true
                    }
                }
                Score.ADVANTAGE -> winnner = true
            }


        }
        /**
         * Comprueba si alguno de los jugadores ha ganado
         * @return Boolean
         */
        fun hasWinner():Boolean {
            return winnner
        }

}

// Ejemplo de uso
matchPoint(listOf(Players.P1, Players.P1, Players.P1,Players.P1,Players.P1,Players.P1))
matchPoint(listOf(Players.P1, Players.P1, Players.P2, Players.P2, Players.P1, Players.P2, Players.P1, Players.P1))
matchPoint(listOf(Players.P1,Players.P1,Players.P1,Players.P2,Players.P2,Players.P2,Players.P2,Players.P1,Players.P1,Players.P2,Players.P2,Players.P2))
matchPoint(listOf(Players.P1, Players.P1, Players.P2))
