
fun main() {
    fizzbuzz()
}

private fun fizzbuzz() {

    for(number in 1..100) {

        if (number % 3 == 0 && number % 5 == 0) {
            println("fizzbuzz")
        } else if (number % 3 == 0) {
            println("fizz")
        } else if (number % 5 == 0) {
            println("buzz")
        } else {
            println(number)
        }
    }
}