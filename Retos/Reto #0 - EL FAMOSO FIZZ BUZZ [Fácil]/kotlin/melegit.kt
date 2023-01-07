fun main() {
    (1..100).forEach { num ->
        when {
            num % 3 == 0 && num % 5 == 0 -> println("FizzBuzz")
            num % 3 == 0 -> println("Fizz")
            num % 5 == 0 -> println("Buzz")
            else -> println(num)
        }
        println()
    }
}