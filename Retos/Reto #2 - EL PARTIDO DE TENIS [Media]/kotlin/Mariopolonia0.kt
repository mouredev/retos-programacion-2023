package EjercicioKotlin

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
