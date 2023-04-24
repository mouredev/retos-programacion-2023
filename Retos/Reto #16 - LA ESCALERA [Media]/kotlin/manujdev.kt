package reto16

import kotlin.math.abs

fun main() {
    drawAStaircase(readDataForStandardInput("Introduce el número de escalones: "))
}

// Función para obtener los datos del usuario por la consola.
fun readDataForStandardInput(info: String): Int {
    print(info)
    return readln().toInt()
}

// Función que detectará si el número es positivo, negativo o en su defecto es cero.
fun drawAStaircase(number: Int) {
    
    try {
        when {
            number == 0 -> {
                println("__")
            }

            number > 0 -> {
                drawStaircaseIfPositiveNumb(number)
            }

            number <= -1 -> {
                drawStaircaseIfNegativeNumb(number)
            }
        }
    } catch (e: NumberFormatException) {
        println("""
            Por favor introduzca un número:
            - Positivo para una escalera ascendente.
            - Negativo para una escalera descendente.
        """.trimIndent())
    }
}

fun drawStaircaseIfPositiveNumb(num: Int) {
    var steps: Int = num

    for (i in 0..num) { // Creará cada una de las filas.
        for (j in 0..num) {      // Creará cada una de las columnas.
            // Casuísticas o condiciones
            if (i == 0 && j == num) {
                print("_")
            } else if (i != 0 && j == steps - 1) {
                print("_|")
                steps -= 1
            }else print("  ")
        }
        println()  // Salto de línea al terminar cada fila.
    }
}

fun drawStaircaseIfNegativeNumb(num: Int) {
    val steps = abs(num) // transforma el valor a positivo

    for (i in 0..steps) { // Creará cada una de las filas.
        for (j in 0..steps) {      // Creará cada una de las columnas.
            // Casuísticas o condiciones
            if (i == 0 && j == 0) print(" _") else if (j == i) print("|_") else print("  ")
        }
        println()  // Salto de línea al terminar cada fila.
    }
}











