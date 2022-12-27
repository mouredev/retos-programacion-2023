

/*
 * Reto#0
 * @author Joaquin Martinez Rus
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
fun main(args: Array<String>) {
    println((1..100).map { when {
        it % 15 ==0 -> "fizzbuzz"
        it % 3 == 0 -> "fizz"
        it % 5 == 0 -> "buzz"
        else -> it
    } }.joinToString ("\n"))
}