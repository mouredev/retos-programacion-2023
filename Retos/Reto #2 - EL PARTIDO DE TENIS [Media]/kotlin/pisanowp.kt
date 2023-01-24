fun main() {

    /*
    * Reto #2 09/01/2023
    *
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

    //val juego = arrayOf("P1", "P1", "P2", "P1", "P2")
    //val juego = arrayOf("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1")
    //val juego = arrayOf("P1", "p2", "P1", "P2", "P2", "P1", "P3", "P2", "P1", "P1", "P1", "P2", "P2", "P2")
    //val juego = arrayOf("P1", "p1", "P1", "x1", "P1", "x1", "P1")
    //val juego = arrayOf("P2", "p2", "P2", "x2", "P2", "x2", "P2")
    //val juego = arrayOf("p1","P2", "p1", "P2", "p2", "p1", "p2", "p1", "p1", "p2", "P2", "P2")
    val juego = arrayOf("p1","P2", "p1", "P1", "p1")

    partido(puntos = juego)

}

fun partido(vararg puntos: String) {
    val puntacion = mapOf(
        0 to "love",
        1 to "15",
        2 to "30",
        3 to "40"
    )

    var jugador1 = 0
    var jugador2 = 0

    run secuenciaJuego@{
        puntos.forEach nuevoPunto@{ punto ->
            if (punto.uppercase() == "P1") {
                jugador1++

            } else if (punto.uppercase() == "P2") {
                jugador2++
            } else {
                // Punto no válido, miramos el siguiente
                return@nuevoPunto
            }

            if (((jugador1 >= 3) || (jugador2 >= 3))
                && (jugador1 == jugador2)
            )
                println("Deuce")

            else if ((jugador1 >= 4) && (jugador1 - jugador2) >= 2) {
                println("Ha ganado el P1")
                return@secuenciaJuego

            } else if ((jugador2 >= 4) && (jugador2 - jugador1) >= 2) {
                println("Ha ganado el P2")
                return@secuenciaJuego

            } else
                if ((jugador1 >= 4) || (jugador2 >= 4)) {
                    if (jugador1 > jugador2)
                        println("Ventaja P1")

                    else
                        println("Ventaja P2")

                } else {
                    println("${puntacion.get(jugador1)} - ${puntacion.get(jugador2)}")

                }
        }
    }

}