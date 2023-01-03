
fun main(){
    val range = 1..100

    range.forEach { number ->
        val multipleOfThree = number%3 == 0
        val multipleOfFive = number%5 == 0
        
        if (multipleOfThree && multipleOfFive) {
            println("fizbuzz")
        } else if(!multipleOfThree && !multipleOfFive){
            println(number)
        } else if(multipleOfThree){
            println("fizz")
        } else println("buzz")


    }
}