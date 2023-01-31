package EjercicioKotlin.Mouredev

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

fun main() {
    Comprobar(8)
    Comprobar(12)
    Comprobar(103)
}

fun Comprobar(_numero: Int) {

    if (fibonacci(numeroCombrobar = _numero))
        println("El numero $_numero es un fibonacci")
    else
        println("El numero $_numero no es un fibonacci")

    if (EsPrimo(numero = _numero))
        println("El numero $_numero es un Primo")
    else
        println("El numero $_numero no es un Primo")

    if (esPar(numero = _numero))
        println("El numero $_numero es un Par")
    else
        println("El numero $_numero no es un Par")

    println("-----------------------------")
}

fun EsPrimo(numero: Int): Boolean {
    var contado = 2

    if (numero == 2) return true
    if (numero % 2 == 0) return false

    while (contado * contado <= numero) {
        contado++
        if (numero % contado == 0)
            return false
    }
    return true
}

fun esPar(numero: Int): Boolean {
    if (numero % 2 == 0)
        return true

    return false
}

fun fibonacci(numeroCombrobar: Int): Boolean {
    var fibonacciUno = 1
    var fibonacciDos = 1
    var esFibonacci = false

    while (numeroCombrobar > fibonacciUno) {
        val fibonacciDos_auxiliar = fibonacciUno
        fibonacciUno += fibonacciDos
        fibonacciDos = fibonacciDos_auxiliar
        esFibonacci = (fibonacciUno == numeroCombrobar)
    }

    return esFibonacci
}
