fun main() {
    findPrimeAndTwinNumbers(100)
}

fun findPrimeAndTwinNumbers(endOfRange: Int) {
    val primeNumbers = findPrimeNumbers(endOfRange)
    primeNumbers.windowed(2, 1).forEach { (first, second) ->
        if (second - first == 2) print("($first, $second), ")
    }
    print("\b".repeat(2))
}

fun findPrimeNumbers(endOfRange: Int): List<Int> {
    return (2..endOfRange).filter { numberToCheck ->
        (2 until numberToCheck).none { numberToCheck % it == 0 }
    }
}
