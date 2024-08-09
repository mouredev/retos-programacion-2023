fun main() {
    for (index in 1..100) {
        val divisiblePorTres = index % 3 == 0
        val divisiblePorCinco = index % 5 == 0
        if (divisiblePorTres && divisiblePorCinco) {
            println("FizzBuzz")
        } else if (divisiblePorTres) {
            println("Fizz")
        } else if (divisiblePorCinco) {
            println("Buzz")
        } else {
            println(index)

        }
    }
}

/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
