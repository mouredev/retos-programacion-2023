fun main() {

    /*
    * Reto #4 23/01/2023
    *
    * PRIMO, FIBONACCI Y PAR
    *
    * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
    * Ejemplos:
    * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
    * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
    */

    (0 until 10).forEach {numero ->
        primoFibonacciPar(numero)
    }


}



fun primoFibonacciPar(numero:Int){
    print( "${numero}" )

    if (esPrimo(numero))
        print( " es primo," )
    else
        print( " no es primo," )

    if (esFibonacci(numero))
        print( " fibonacci" )
    else
        print( " no es fibonacci" )

    if (esPar(numero))
        println( " y es par" )
    else
        println( " y es impar" )
}

fun esPrimo(numero:Int):Boolean {

    if (numero < 2)
        return false

    for (i in 2 until numero) {
        if (numero % i == 0)
            return false
    }

    return true
}

fun esFibonacci(numero: Int):Boolean{
    var esFibonacci = false
    var num1 : Int = 0
    var num2 : Int = 1

    for (i in 1..numero+1){
        // Nivel pro, usando la función de extension also
        num1 = num2.also {
            num2 += num1
        }

        if (num2==numero)
            esFibonacci = true

    }

    return esFibonacci

}

fun esPar(numero:Int):Boolean{
    return numero%2==0
}
