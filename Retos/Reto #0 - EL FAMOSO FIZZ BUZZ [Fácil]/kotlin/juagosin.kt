fun main(){
    fizzbuzz()
}

fun fizzbuzz(){

    for (n in 1..100){
        if (n % 3 == 0 && n % 5 == 0) {
            println("FizzBuzz")
        }

        else if(n % 3 == 0 ){
            println("Fizz")
        }else if(n % 5 == 0) {
            println("Buzz")
        }else{
            println(n)
        }

    }
}