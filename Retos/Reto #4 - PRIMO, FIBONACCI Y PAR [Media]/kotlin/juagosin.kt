package com.cursosant.android.retosprogramacion2223

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

fun main()
{

    Comprobacion(2)
    Comprobacion(5)
    Comprobacion(7)
    Comprobacion(12)
    Comprobacion(13)
    Comprobacion(55)
    Comprobacion(64)

}

fun Comprobacion (valor: Int){
    print(valor)
    print(Primo((valor)))
    print(isInFibonacci((valor)))
    print(Par((valor)))
    println("")
}

fun Fibonacci(valor: Int):Int{
    if(valor <= 1){
        return  valor
    }

    return Fibonacci(valor-1) + Fibonacci(valor-2)

}

fun Primo(valor: Int):String{
    var checkPrimo = true

    for (i in 1..valor){

        if(valor%i==0 && (i!=valor && i!=1)){
            checkPrimo = false
            return " no es primo"
        }
    }
    return " es primo"
}

fun Par(valor: Int):String{

    if(valor % 2 == 0){
        return " y es par"
    }else return " y es impar"

}

fun isInFibonacci(valor: Int):String{
    var n = 0
    do {
        var x = Fibonacci(n)
        if(valor == x){
            return ", fibonacci"
        }
        n++
    }while(x<=valor)
    return ", no es fibonacci"
}