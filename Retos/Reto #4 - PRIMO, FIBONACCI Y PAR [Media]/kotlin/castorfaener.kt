package com.cursosant.android.retosprogramacion2223

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */


fun main() {

    println("Introduce un numero")
    val input = readlnOrNull()?.toInt()?:0

    val even = if(isEven(input)){
        "es par"
    }else{
        "es impar"
    }

    val prime = if(isPrime(input)){
        "es primo"
    }else{
        "no es primo"
    }

    val fibonacci = if(isFibonacci(input)){
        "es fibonacci"
    }else{
        "no es fibonacci"
    }

    println("$input $prime, $fibonacci y $even")

}

fun isEven(number: Int): Boolean {
    return number % 2 == 0
}

fun isPrime(number: Int): Boolean {
    var result = true
    for(num in 2 until number){
        if (number % num == 0) {
            result = false
        }
    }
    return result
}

fun isFibonacci(number: Int): Boolean {
    var fiboEnd = false
    var isFibo = false
    val fiboList = mutableListOf(1,1)
    while(!fiboEnd){
        for(index in 0 .. number){
            fiboList.add(fiboList[index] + fiboList[index + 1])
            if(fiboList.lastIndexOf(index) >= number) fiboEnd = true
        }
    }
    fiboList.forEach {
        if(it == number) isFibo = true
    }
    return isFibo
}