fun main() {
    fizzbuzz()
}

fun fizzbuzz(start: Int = 1, end: Int = 100) {

    for (i in start..end) {
        if (i % 3 == 0 && i % 5 == 0) println("fizzbuzz")
        else if (i % 3 == 0) println("fizz")
        else if (i % 5 == 0) println("buzz")
        else println(i)
    }

}
