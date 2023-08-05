fun main(){
    fizzBuzz()
}

fun fizzBuzz(){
    for (i in 1..100){
    	if (i%3==0 && i%5==0){
            println("fizzbuzz")
        } else if (i%3==0){
            println("fizz")
        } else if (i%5==0){
            println("buzz")
        } else{
            println(i)
        }
    }
}