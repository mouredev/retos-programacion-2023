fun main() {
    (1 until 100 + 1).forEach{ index ->
        val multiple3 = index % 3 == 0
        val multiple5 = index % 5 == 0
        
        if (multiple3 && multiple5) {
        	println("fizzbuzz")
        }
        else if (multiple5) {
            println("buzz")
        }
        
        else if (multiple3) {
            println("fizz")
        }
        else {
           println(index)
        }
    }
}