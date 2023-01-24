import kotlin.math.abs

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

fun validateNumber(number: Int) {
    val absNumber = abs(number)

    println("$number" +
            if (isPrime(absNumber)) {" es primo,"} else { " no es primo,"} +
            if (isFibonacci(absNumber)) {" es fibonacci"} else {" no es fibonacci"} +
            " y es " +
            if (isEven(absNumber)) {"par"} else {"impar"}
    )
}

fun isPrime(number: Int): Boolean {

    if (number == 0 || number == 1) return false
    for(i in 2 .. (number/2)) {
        if (number % i == 0) {
            return false
        }
    }
    return true
}

fun isFibonacci(number: Int): Boolean {
    var a = 0
    var b = 1
    var result = 0

    while (result <= number) {
        if (result == number) {
            return true
        }
        result = a + b
        a = b
        b = result
    }
    return false
}

fun isEven(number: Int): Boolean {
    return number % 2 == 0
}

fun main() {
    validateNumber(0)
    validateNumber(1)
    validateNumber(2)
    validateNumber(3)
    validateNumber(4)
    validateNumber(5)
    validateNumber(6)
    validateNumber(7)
    validateNumber(8)
    validateNumber(9)
    validateNumber(10)
    validateNumber(11)
    validateNumber(13)
}