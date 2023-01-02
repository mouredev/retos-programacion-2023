fun main(args: Array<String>) {
    for (i in 1..100){
        if (i % 3 == 0 && i % 5 == 0){
            println("FIZZBUZZ")
        }else if (i % 3 == 0){
            println("FIZZ")
        }else if (i % 5 == 0 ){
            println("BUZZ")
        }else{
            println(i)
        }
    }
}