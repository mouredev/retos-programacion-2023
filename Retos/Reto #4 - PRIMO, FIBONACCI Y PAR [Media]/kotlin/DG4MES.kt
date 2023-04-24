fun isPrime(n:Int):String {
    return if(
        n%2 == 0 || n%3 == 0 ||
        n%3 == 0 || n%7 == 0
    ) "no es primo" else "es primo"

}

fun wIsPrime(n:Int):String{
    return when(n){
        2,3,5,7 -> "es primo"
        else -> isPrime(n)
    }
}

fun isPair(n:Int):String {
    return if(n%2 == 0) "es par" else "es impar"
}


fun listFibonnaci(n:Int):List<Int> {
    val fib = mutableListOf<Int>(0,1)
    for(i in 2..n+1){
        fib.add(fib[fib.size - 2] + fib[fib.size - 1])
    }
    return fib
}
    
fun isFibonnaci(n:Int):String {
    return if(n in listFibonnaci(n)) "es fibonacci" else "no es fibonacci"
}

fun comprobar(n:Int):String {
    return "$n ${wIsPrime(n)}, ${isFibonnaci(n)}, ${isPair(n)}"
}

fun main() {
    println(comprobar(2))
    println(comprobar(7))
}