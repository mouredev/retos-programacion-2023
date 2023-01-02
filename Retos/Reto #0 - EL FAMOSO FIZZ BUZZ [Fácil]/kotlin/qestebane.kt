fun main(){
    fizzbuzz()
}

private fun fizzbuzz() {
    (1..100).forEach{ num ->
        when {
            num % 3 == 0 && num % 5 == 0 -> println("fizzbuzz")
            num % 3 == 0 -> println("fizz")
            num % 5 == 0 -> println("buzz")
            else         -> println(num)
        }
    }
}