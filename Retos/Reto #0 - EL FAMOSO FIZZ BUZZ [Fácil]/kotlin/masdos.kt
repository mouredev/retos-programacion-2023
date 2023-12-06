/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

fun main() {
  fizzbuzz()
}

private fun fizzbuzz() {
  for (i in 1..100) {
    when {
      i % 3 == 0 && i % 5 == 0 -> println("fizzbuzz")
      i % 3 == 0 -> println("fizz")
      i % 5 == 0 -> println("buzz")
      else -> println(i)
    }
  }
}
