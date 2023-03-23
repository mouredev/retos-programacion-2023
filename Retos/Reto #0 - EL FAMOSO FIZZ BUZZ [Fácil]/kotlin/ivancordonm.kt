fun main() {
    (1..100).forEach {
        when (true) {
            (it % 15 == 0) -> println("fizzbuzz")
            (it % 3 == 0) -> println("fizz")
            (it % 5 == 0) -> println("buzz")
            else -> println(it)
        }
    }
}
