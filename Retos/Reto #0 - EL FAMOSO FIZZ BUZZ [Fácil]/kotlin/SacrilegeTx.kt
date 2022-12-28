fun multiplo(number: Int): String {
    
    if (number % 3 == 0 && number % 5 == 0) return "fizzbuzz"
    if (number % 3 == 0) return "fizz"
    if (number % 5 == 0) return "buzz"
    return ""
}

fun main() {
    for (i in 1..101) {
        if (multiplo(i) != "") println(multiplo(i))
        else println(i)
    }
    
}