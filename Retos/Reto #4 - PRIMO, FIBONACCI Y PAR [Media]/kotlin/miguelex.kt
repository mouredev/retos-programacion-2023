fun main() {
    CheckNumber(1)
    CheckNumber(2)
    CheckNumber(3)
    CheckNumber(4)
    CheckNumber(5)
    CheckNumber(6)
    CheckNumber(7)
    CheckNumber(8)
    CheckNumber(9)
    CheckNumber(10)
    CheckNumber(1024)
    CheckNumber(1358742586)
}

private fun CheckNumber(number: Int) {
    val isPrime = if (isPrimeNumber(number)) "es primo, " else "no es primo, "
    val isEven = if (isEvenNumber(number)) "es par, " else "es impar "
    val isFibonacci =
            if (isFibonacciNumber(number)) "y esta en la serie de Fibonacci"
            else "y no esta en la serie de Fibonacci"

    println(" EL numero $number $isPrime $isEven $isFibonacci")
}

private fun isPrimeNumber(number: Int): Boolean {
    var isPrime = true
    for (i in 2..number / 2) {
        if (number % i == 0) {
            isPrime = false
            break
        }
    }
    return isPrime
}

private fun isEvenNumber(number: Int): Boolean {
    return number % 2 == 0
}

private fun isFibonacciNumber(number: Int): Boolean {
    var a = 0
    var b = 1
    var c = 0
    while (c < number) {
        c = a + b
        a = b
        b = c
    }
    return c == number
}