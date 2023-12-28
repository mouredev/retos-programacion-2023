package com.example.retosdeprogramacion2023

fun main(){
    println(numClassifier(2))
}

fun numClassifier(num: Int): String{
    var result = "El numero $num es: "
    if (isPair(num)) result += "<Par> "
    if (isPrime(num)) result += "<Primo> "
    if (isFibonacci(num)) result += "<Fibonacci>"
    else result = "no cumple los requisitos"
    return result

}
fun isPrime(num: Int):Boolean{
    if (num <2 ) return true
    for(numTested in 2 until num ) {
        if(num % numTested  == 0) return false
    }
    return  true
}
fun isPair(num: Int): Boolean = num % 2 == 0

fun isFibonacci(num: Int): Boolean{
    var first = 0
    var second = 1
    var fibo = 1
    var isFibo = false


    for(i in 0 .. num){
        fibo = first + second
        if (num == fibo) isFibo = true

        first = second
        second = fibo
        if(isFibo) break
    }
    return isFibo
}