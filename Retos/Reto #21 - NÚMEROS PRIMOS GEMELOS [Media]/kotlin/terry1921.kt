fun main() {
    println("twin primes: ${getTwinPrimes(14)}")
}

fun getTwinPrimes(range: Int): List<Pair<Int, Int>> {
    val primes = mutableListOf<Int>()
    (1..range).forEach { i -> if (isPrime(i)) primes.add(i) }
    val twinPrimes = mutableListOf<Pair<Int, Int>>()
    (0 until primes.size - 1).forEach { i ->
        if (primes[i + 1] - primes[i] == 2) {
            twinPrimes.add(Pair(primes[i], primes[i + 1]))
        }
    }
    return twinPrimes
}

fun isPrime(number: Int): Boolean {
    if (number <= 1) return false
    if (number == 2) return true
    if (number % 2 == 0) return false
    var i = 3
    while (i * i <= number) {
        if (number % i == 0) return false
        i += 2
    }
    return true
}