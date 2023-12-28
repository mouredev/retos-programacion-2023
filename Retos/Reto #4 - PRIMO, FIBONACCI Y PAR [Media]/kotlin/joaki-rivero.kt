/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

fun main() {
    checkTypeOfNumber(2)    // sí, sí, sí
    checkTypeOfNumber(13)   // sí, sí, no
    checkTypeOfNumber(7)    // sí, no, no
    checkTypeOfNumber(1)    // no, sí, no
    checkTypeOfNumber(8)    // no, sí, sí
    checkTypeOfNumber(14)   // no, no, sí
    checkTypeOfNumber(65)   // no, no, no
}

fun checkTypeOfNumber(number: Int) {
    var result = "$number "
    result += if (isPrimo(number)) "es primo, " else "no es primo, "
    result += if (isFibonacci(number)) "fibonacci " else "no es fibonacci "
    result += if (isPar(number)) "y es par" else "y es impar"

    println(result)
}

private fun isPrimo(number: Int): Boolean {
    var isPrimo = true

    if (number == 1) return false
    for (i in 2 until number) {
        if (number % i == 0) {
            isPrimo = false
            break
        }
    }
    return isPrimo
}

private fun isFibonacci(number: Int): Boolean {
    var isFibonacci = false
    var a = 1
    var b = 1
    var c = 0

    if (number == 1) return true
    while (c <= number) {
        c = a + b
        a = b
        b = c

        if (c == number) {
            isFibonacci = true
            break
        }
    }
    return isFibonacci
}

private fun isPar(number: Int): Boolean {
    return number % 2 == 0
}
