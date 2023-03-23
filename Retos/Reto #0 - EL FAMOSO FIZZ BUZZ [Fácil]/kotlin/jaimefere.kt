fun main() {
    (1..100).forEach { num ->
        when {
            num % 5 == 0 -> {
                if(num % 3 == 0) {
                    print("fizz")
                }
                println("buzz")
            }
            num % 3 == 0 -> println("fizz")
            else -> println(num.toString())
        }
    }
}