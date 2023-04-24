
import kotlin.math.sqrt

fun main() {
    checkPrimeFibonacciEven(2)
    checkPrimeFibonacciEven(7)
    checkPrimeFibonacciEven(0)
    checkPrimeFibonacciEven(1)
    checkPrimeFibonacciEven(-2)
}

private fun checkPrimeFibonacciEven(number: Int) {

    var result = "$number "

    // Primo
    if (number > 1) {
        var prime = true
        for (index in 2 until number) {
            if (number % index == 0) {
                result += "no es primo, "
                prime = false
                break
            }
        }
        if (prime) {
            result += "es primo, "
        }
    } else {
        result += "no es primo, "
    }

    // Fibonacci
    result += if (number > 0 && (isPerfectSquare(5 * number * number + 4) || isPerfectSquare(
    5 * number * number - 4))) "es fibonacci " else "no es fibonacci "

    // Par
    result += if (number % 2 == 0) "y es par" else "y es impar"

    println(result)
}


private fun isPerfectSquare(number: Int): Boolean {
    val sqrt = sqrt(number.toDouble()).toInt()
    return sqrt * sqrt == number
}