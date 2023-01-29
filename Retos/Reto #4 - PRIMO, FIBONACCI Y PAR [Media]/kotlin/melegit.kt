fun main() {
    println(buildStringResult(144))
    println(buildStringResult(2))
    println(buildStringResult(11))
    println(buildStringResult(13))
    println(buildStringResult(7))
}

private fun buildStringResult(number: Int): String {
    var stringResult = ""

    stringResult += if (isPrimeNumber(number)) "es primo," else "no es primo,"
    stringResult += if (isFibonacciNumber(number)) " es fibonacci" else " no es fibonacci"
    stringResult += if (isEvenNumber(number)) " y es par" else " y es impar"
    return stringResult
}

fun isFibonacciNumber(number: Int): Boolean {
    val result: Boolean = when (number) {
        0 -> true
        1 -> true
        else -> generateFibonacciSequence(number)
    }
    return result
}

fun generateFibonacciSequence(number: Int): Boolean {
    val firstValue = 0
    val secondValue = 1
    var auxValue = firstValue
    var auxValue2 = secondValue
    var nextValue = 0

    do {
        nextValue = auxValue + auxValue2
        auxValue = auxValue2
        auxValue2 = nextValue
        if (number == nextValue) return true
    } while (nextValue < number)
    return false
}

fun isEvenNumber(number: Int): Boolean {
    return when {
        number % 2 == 0 -> true
        else -> false
    }
}

fun isPrimeNumber(number: Int): Boolean {
    (2 until number).forEach {
        if (number % it == 0) return false
    }
    return true
}
