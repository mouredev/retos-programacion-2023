package EjercicioKotlin.Mouredev

// link del video
// https://youtube.com/shorts/vZlfaU3WbJk

class Cordenada {

    private var oneVertical = 1
    private var oneHorizontal = 1

    private var TwoVertical = 2
    private var twoHorizontal = 1

    private var threeVertical = 2
    private var threeHorizontal = 2

    private var FourVertical = 2
    private var fourHorizontal = 3

    fun moverDerecha() {

        if (fourHorizontal == 10) {
            println("\n===========================")
            println("No se puede mover asi la derecha")
            println("===========================")
        } else {
            oneHorizontal += 1
            twoHorizontal += 1
            threeHorizontal += 1
            fourHorizontal += 1

            println("\n===========================")
            println("se movio asi la derecha")
            println("===========================")
        }
    }

    fun moverIzquierda() {

        if (twoHorizontal == 1) {
            println("\n===========================")
            println("No se puede mover asi la izquierda")
            println("===========================")
        } else {
            oneHorizontal -= 1
            twoHorizontal -= 1
            threeHorizontal -= 1
            fourHorizontal -= 1

            println("\n===========================")
            println("se movio asi la izquierda")
            println("===========================")
        }
    }

    fun moverArriba() {

        if (oneVertical == 1) {
            println("\n===========================")
            println("No se puede mover asi arriba")
            println("===========================")
        } else {
            oneVertical -= 1
            TwoVertical -= 1
            threeVertical -= 1
            FourVertical -= 1

            println("\n===========================")
            println("se movio asi arriba")
            println("===========================")
        }
    }

    fun moverAbajo() {

        if (FourVertical == 10) {
            println("\n===========================")
            println("No se puede mover asi abajo")
            println("===========================")
        } else {
            oneVertical += 1
            TwoVertical += 1
            threeVertical += 1
            FourVertical += 1

            println("\n===========================")
            println("se movio asi abajo")
            println("===========================")

        }
    }

    fun comprobar(One: Int, Two: Int): Boolean {

        return if (oneVertical == One && oneHorizontal == Two)
            true
        else if (TwoVertical == One && twoHorizontal == Two)
            true
        else if (threeVertical == One && threeHorizontal == Two)
            true
        else if (FourVertical == One && fourHorizontal == Two)
            true
        else
            false
    }
}

/**
 * cuadro negro
 * println("\uD83D\uDD33")
 *
 * cuadro blanco
 * println("\uD83D\uDD32")
 * */

fun main() {
    val cordenada = Cordenada()
    var stop = true
    var read = ""

    do {
        for (itOne in 1..10) {

            for (itTwo in 1..10) {

                if (cordenada.comprobar(itOne, itTwo)) {
                    print("\uD83D\uDD33")
                } else {
                    print("\uD83D\uDD32")
                }

            }
            println()
        }

        println("\n\nopciones del mover el tetris:\narriba: w\nabajo: s\nderecha: a\nizquierda: d\n")
        print("Seleccione una opcion:")
        read = readLine()!!

        when (read) {
            "w" -> {
                cordenada.moverArriba()
            }

            "a" -> {
                cordenada.moverIzquierda()
            }

            "s" -> {
                cordenada.moverAbajo()
            }

            "d" -> {
                cordenada.moverDerecha()
            }

            "x" -> {
                stop = false
            }

            else -> {
                println("\n===========================")
                println("opcion no esta en la lista")
                println("===========================")
            }
        }

    } while (stop)

}
