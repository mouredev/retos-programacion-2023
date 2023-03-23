/**
"""
RETO #0
Escribe un programa que muestre por consola (con un print) los
números de 1 a 100 (ambos incluidos y con un salto de línea entre
cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

(1..100).forEach {
    when {
        (it % 3) == 0 && (it % 5) == 0 -> "fizzbuzz"
        (it % 5) == 0 -> "buzz"
        (it % 3) == 0 -> "fizz"
        else -> it
    }.let {
        println(it)
    }
}