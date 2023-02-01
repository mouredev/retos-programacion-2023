import kotlin.math.pow
import kotlin.math.sqrt

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

fun main(args: Array<String>) {
    println( isPrimeOrFibOrEven(2))
    println( isPrimeOrFibOrEven(7))
}
fun isPrimeOrFibOrEven(number: Int): String {

    val f1 = (1 + sqrt(5.0))/2
    val f2 = (1 - sqrt(5.0))/2

    val isPrime = number > 1 && (3..sqrt(number.toDouble()).toInt()).map{it}.all { number % it > 0 }
    val isFibbonacci = (0 until number).any { ((f1.pow(it) - f2.pow(it)) / (f1-f2)).toInt() == it }
    val isEven = number % 2 == 0

    val prime = "$number ${if (isPrime) "es" else "no es"} primo"
    val fibonnaci = "${if (isFibbonacci) "es" else "no es"} fibonnaci"
    val even = if (isEven) "es par" else "es impar"

    return "$prime, $fibonnaci y $even"
}




