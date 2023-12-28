import kotlin.math.sqrt

fun main() {

    fun isFibonacci(n: Int) = sqrt(5.0 * n * n + 4) % 1 == 0.0 || sqrt(5.0 * n * n - 4) % 1 == 0.0
    fun isPrime(n: Int): Boolean {
        if(n <= 1) return false
        (2..sqrt(n.toDouble()).toInt()).forEach{
            if(n % it == 0) return false
        }
        return true
    }
    fun isPair(n: Int) = n % 2 == 0

    fun getInfo(n: Int) = buildString {
        append("$n")
        if(isPair(n)) append(" is even")
        else append(" is odd")
        if(isFibonacci(n)) append(" and is fibonacci")
        if(isPrime(n)) append(" and is prime")
        append(".")
    }

    println(getInfo(2))
    println(getInfo(7))
    println(getInfo(100))
    println(getInfo(233))
}
