fun isPrime(number: Int): Boolean {
    if(number < 2) {
        return false
    } else {
        (2 until number).forEach { partialNumber ->
            if(number % partialNumber == 0) {
                return false
            }
        }
        return true
    }
}

fun isFibonacci(number: Int): Boolean {
    var penultimate = 0
    var ultimate = 1
    while(ultimate < number) {
        ultimate += penultimate
        penultimate = ultimate - penultimate
    }
    return (number == penultimate) || (number == ultimate)
}

fun isEven(number: Int): Boolean {
    return number % 2 == 0
}

fun getKindOf(number: Int): String {
    return "$number ${if(isPrime(number)) "es" else "no es"} primo, ${if(isFibonacci(number)) "es" else "no es"} fibonacci y ${if(isEven(number)) "es par" else "es impar"}"
}

fun main() {
    println(getKindOf(0))
    println(getKindOf(1))
    println(getKindOf(2))
    println(getKindOf(7))
}