fun esPrimo(n: Int): Boolean {
    if (n < 2) return false
    for (i in 2 until n) {
        if (n % i == 0) return false
    }
    return true
}

fun esFibonacci(n: Int): Boolean {
    if (n == 0 || n == 1) return true
    var a = 0
    var b = 1
    var c = a + b
    while (c < n) {
        if (c == n) return true
        a = b
        b = c
        c = a + b
    }
    return false
}

fun esPar(n: Int): Boolean {
    return n % 2 == 0
}

fun main() {
    print("Ingrese un número: ")
    val number = readln().toInt()
    var message = "$number es "
    if (esPrimo(number)) message += "primo, "
    else message += "no es primo, "
    if (esFibonacci(number)) message += "fibonacci y tambien"
    else message += "no es fibonacci y tampoco "
    if (esPar(number)) message += "par"
    else message += "impar"
    println(message)
}
