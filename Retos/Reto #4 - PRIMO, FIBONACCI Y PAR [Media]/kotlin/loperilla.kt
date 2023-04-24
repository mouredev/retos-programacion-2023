fun main() {
    (2..10).forEach { it ->
        checkPrimePairFibonacci(it)
    }
}

private fun checkPrimePairFibonacci(number: Int) {
    print("${number} ${checkPair(number)} ${checkFibonacci(number)} ${checkPrime(number)} \n\n")
} 


private fun checkPair(number: Int): String {
    return if (number % 2 == 0) {
        "es par,"   
    } else {
        "no es par,"
    } 
}

private fun checkFibonacci(number: Int): String {
    var fib1 = 0
    var fib2 = 1
    do {
        var saveFib1 = fib1
        fib1 = fib2
        fib2 = saveFib1 + fib2
        }
    while (fib2 < number)

    return if (fib2 == number)
        "fibonacci"
    else
        "no fibonacci"
}

private fun checkPrime(number: Int): String {
    var flag = false
    for (i in 2..number / 2) {
        if (number % i == 0) {
            flag = true
            break
        }
    }

    return if (!flag)
        "y es primo."
    else
        "y no es primo."
}
