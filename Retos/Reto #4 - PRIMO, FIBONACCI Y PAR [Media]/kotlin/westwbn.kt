import kotlin.math.sqrt

fun main() {
    print("Ingresa un numero : ")
    val n = readln().toInt()

    evaluateNumber(n)
}

fun evaluateNumber(number:Int){
    if (number < 0){
        println("Ingresa un numero entero")
    } else {
        println("$number ${isPrime(number)}, ${isFibonacci(number)} y ${isPar(number)}")
    }
}

fun isPrime(n: Int): String {
    if (n == 2) {
        return "es primo"
    } else if (n < 2 || n % 2 == 0) {
        return "no es primo"
    }

    for (i in 3..sqrt(n.toDouble()).toInt() step 2) {
        if (n % i == 0) return "no es primo"
    }
    return "es primo"
}

fun isFibonacci(n:Int):String{
    var a = 0
    var b = 1
    var c = a + b

    while (c <= n){
        if (c == n){
            return "es fibonacci"
        } else {
            a = b
            b = c
            c = a + b
        }
    }
    return "no es fibonacci"
}

fun isPar(n:Int):String{
    if (n % 2 == 0){
        return "es par"
    }
    return "es impar"
}
