fun main() {
    for (i in 1..100) {
        var result = "$i. "

        if (i % 3 == 0) {
            result += "fizz"
        }
        if (i % 5 == 0) {
            result += "buzz"
        }

        println(result)
    }
}