package EjercicioKotlin
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
    reto2()
}

private fun reto2() {
    var puntoPlayerUno = 0
    var puntoPlayerDos = 0

    do {
        if (rand(1, 2) == 1) {
            puntoPlayerUno++
        } else {
            puntoPlayerDos++
        }
        println("jugador uno : " + octenerPunto(puntoPlayerUno) + " Jugador Dos : " + octenerPunto(puntoPlayerDos))

        Thread.sleep(2000)
    } while (puntoPlayerDos < 3 && puntoPlayerUno < 3)

    if (puntoPlayerUno == puntoPlayerDos){
        println("\n Empate")
        return
    }

    if (puntoPlayerUno > puntoPlayerDos) {
        println("\nJugador uno a ganado")
    } else {
        println("\nJugador dos a ganado")
    }
}

fun octenerPunto(punto: Int): String {
    return when (punto) {

        1 -> {
            " 15"
        }

        2 -> {
            "30"
        }

        3 -> {
            "40"
        }

        else -> {
            "Love"
        }
    }
}

fun rand(start: Int, end: Int): Int {
    require(start <= end) { "Illegal Argument" }
    return (start..end).random()
}
