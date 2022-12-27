
fun main(args: Array<String>) {
    println((1..100).map { when {
        it % 15 ==0 -> "fizzbuzz"
        it % 3 == 0 -> "fizz"
        it % 5 == 0 -> "buzz"
        else -> it
    } }.joinToString ("\n"))
}