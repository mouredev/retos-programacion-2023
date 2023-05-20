/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */


fun main() {
    fizzBuzz(100)
}


private fun fizzBuzz(number: Int) {
    for (n in 0..number) {
        if (n % 5 == 0 && n % 3 == 0) {
            println("fizzbuzz")
        } else if (n % 3 == 0) {
            println("fizz")
        } else if (n % 5 == 0) {
            println("buzz")
        } else {
            println(n)
        }
    }
}