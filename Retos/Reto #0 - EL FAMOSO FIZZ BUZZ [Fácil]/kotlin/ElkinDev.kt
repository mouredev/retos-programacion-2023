/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
fun main(args: Array<String>) {
    fizzbuzz4()
}

fun fizzbuzz1() {
    println("Solucion con if")
    for (i in 1..100) {
        if (i % 3 == 0 && i % 5 == 0) {
            println("$i fizzbuzz")
        } else if (i % 3 == 0) {
            println("$i fizz")
        } else if (i % 5 == 0) {
            println("$i fizz")
        } else (println("$i"))
    }
}

fun fizzbuzz2() {
    println("Solucion con when")
    for (i in 1..100) {
        when {
            i % 3 == 0 && i % 5 == 0 -> println("$i fizzbuzz")
            i % 3 == 0 -> println("$i fizz")
            i % 5 == 0 -> println("$i buzz")
            else -> println(i)
        }
    }
}

fun fizzbuzz3() {
    println("Solucion con while")
    var i = 1
    while (i <= 100) {
        if (i % 3 == 0 && i % 5 == 0) {
            println("$i fizzbuzz")
        } else if (i % 3 == 0) {
            println("$i fizz")
        } else if (i % 5 == 0) {
            println("$i buzz")
        } else {
            println(i)
        }
        i++
    }

}

fun fizzbuzz4() {
    println("Solucion con Do While")
    var i = 1
    do {
        if (i % 3 == 0 && i % 5 == 0) {
            println("$i fizzbuzz")
        } else if (i % 3 == 0) {
            println("$i fizz")
        } else if (i % 5 == 0) {
            println("$i buzz")
        } else {
            println(i)
        }
        i++
    } while (i <= 100)
}
