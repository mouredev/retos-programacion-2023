fun main() {
    println("Introduce un número:")
    val input = readLine()
    try {
        val n = input!!.toInt()
        val result = isPrimeAndFibonacciAndParity(n)
        println(result)
    } catch (e: NumberFormatException) {
        println("La entrada no es un número válido.")
    }
}

fun isPrimeAndFibonacciAndParity(n: Int): String {
    val par = if (n % 2 == 0) "par" else "impar"
    val primo = if (isPrime(n)) "es primo" else "no es primo"
    val fibonacci = if (fibonnacci(n)) "es parte de la serie de Fibonacci" else "no es parte de la serie de Fibonacci"
    return "El número $n es $par, $primo y $fibonacci"
}

fun isPrime(n: Int): Boolean {
    if (n <= 1) return false
    if (n <= 3) return true
    if (n % 2 == 0 || n % 3 == 0) return false
    var i = 5
    while (i * i <= n) {
        if (n % i == 0 || n % (i + 2) == 0) return false
        i += 6
    }
    return true
}

fun fibonnacci(n: Int): Boolean {
    var a = 0
    var b = 1
    while (b < n) {
        val c = a + b
        a = b
        b = c
        if (b == n) return true
    }
    return false
}
