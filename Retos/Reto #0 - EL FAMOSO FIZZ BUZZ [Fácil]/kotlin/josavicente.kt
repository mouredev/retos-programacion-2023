fun main(args: Array<String>) {
    for(index: Int in 1..50){
        println(fizzbuzzGenerator(index))
    }
}

fun fizzbuzzGenerator(number: Int): String {
    if ((number % 3 == 0) && (number % 5 == 0)) return "fizzbuzz"
    if (number % 3 == 0) return "fizz"
    if (number % 5 == 0) return "buzz"
    return number.toString()
}