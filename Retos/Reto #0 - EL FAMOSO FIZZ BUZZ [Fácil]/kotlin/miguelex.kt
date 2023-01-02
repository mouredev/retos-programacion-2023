fun main() {
    FizzBuzz(100)
}

private fun FizzBuzz(n: Int){

    for (i in 1..n){
        when {
            i % 15 == 0 -> println("FizzBuzz")
            i % 3 == 0 -> println("Fizz")
            i % 5 == 0 -> println("Buzz")
            else -> println(i)
        }
    }
}