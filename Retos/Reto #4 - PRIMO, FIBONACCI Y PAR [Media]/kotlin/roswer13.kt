fun main() {
    (0..10).forEach { x ->
        evaluateNumber(number = x)
    }
}

fun evaluateNumber(number: Int) {
    if (number < 0) {
        println("Debes ingresar un numero entero")
        return
    }
    println("$number ${isPrimo(number = number)}, ${isFibonacci(number = number)} y ${isPar(number = number)}")
}

fun isPrimo(number: Int): String {
    if (number == 0 || number == 1 || number == 4) return "no es primo"

    (2..number / 2).forEach { x ->
        if (number % x == 0) {
            return "no es primo"
        }
    }
    return "es primo"
}

fun isFibonacci(number: Int): String {
    var a = 0
    var b = 1

    if (number == a || number == b) return "fibonacci"

    var c = a + b
    while (c <= number) {
        if (c == number) return "fibonacci"

        a = b
        b = c
        c = a + b
    }
    return "no es fibonacci"
}

fun isPar(number: Int): String {
    return if (number % 2 == 0) "es par." else "es impar."
}
