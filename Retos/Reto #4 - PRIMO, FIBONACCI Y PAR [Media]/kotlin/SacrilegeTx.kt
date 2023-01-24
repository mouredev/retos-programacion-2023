import kotlin.math.pow
import kotlin.math.sqrt

fun main() {
    val number: Int = 7
    val messageEvenOdd: String = if (isEvenNumber(number)) "es par" else "es impar"
    val messagePrime: String = if (isPrimeNumber(number)) "es primo" else "no es primo"
    val messageFibonacci: String = if (isFibonacci(number)) "es fibonacci" else "no es fibonacci"
    println("Con el numero $number el resultado es: $messagePrime, $messageFibonacci y $messageEvenOdd")
}

fun isEvenNumber(number: Int) : Boolean {
    return number % 2 == 0
}

fun isPrimeNumber(number: Int) : Boolean {
    //if (number == 2 || number == 3) return true
    var flag: Boolean = true
    for (i in 2 until number) {
        if (number % i == 0) {
            flag = false
            break
        }
    }
    return flag
}

fun isFibonacci(number: Int): Boolean {
    // numberToCheck is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both
    // is a perferct square
    return isPerfectSquare(5 * number.toDouble().pow(2.0) + 4) || isPerfectSquare(5 * number.toDouble().pow(2.0) - 4)
}

fun isPerfectSquare(number: Double) : Boolean {
    return if (number > 0 && sqrt(number) % 1 == 0.toDouble()) return true else false
}