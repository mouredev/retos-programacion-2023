fun main() {
    checkNumber(3)
    checkNumber(7)
}

fun isPrime(n: Int): Boolean {
    if (n < 2) return false
    for (i in 2 ..< n) {
        if (n % i == 0) return false
    }
    return true
}

fun isFibonacci(n: Int): Boolean {
    var a = 0
    var b = 1
    while (a < n) {
        val temp = a
        a = b
        b += temp
    }
    return a == n
}

fun isEven(n: Int): Boolean {
    return n % 2 == 0
}

fun checkNumber(n: Int) {
    val prime = if (isPrime(n)) "primo" else "no es primo"
    val fibonacci = if (isFibonacci(n)) "fibonacci" else "no es fibonacci"
    val even = if (isEven(n)) "par" else "impar"
    println("$n es $prime, $fibonacci y es $even")
}