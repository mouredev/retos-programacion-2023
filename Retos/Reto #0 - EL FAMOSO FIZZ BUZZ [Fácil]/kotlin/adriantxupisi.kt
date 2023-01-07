/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

 fun main() {
    for (number in 1..100) {
        println(fizzbuzz(number))
    }
}

fun fizzbuzz(number: Int): String {
    return when {
        number % 3 == 0 && number % 5 == 0 -> "fizzbuzz"
        number % 3 == 0 -> "fizz"
        number % 5 == 0 -> "buzz"
        else -> number.toString()
    }
}