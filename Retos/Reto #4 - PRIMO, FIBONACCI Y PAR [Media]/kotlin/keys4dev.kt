/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

fun main() {
    println(esFibonacciEsParEsPrimo(21))
}

fun esFibonacci(numero:Int):String{
    if (numero == 0){
        return "es fibonacci";
    }
        
    var secuencia = mutableListOf(0,1)
    while (secuencia[secuencia.lastIndex]<numero){
        secuencia.add(secuencia[secuencia.lastIndex]+secuencia[secuencia.lastIndex-1])
    }
  
    return if (secuencia[secuencia.lastIndex] == numero) "es fibonacci" else "no es fibonacci"
}

fun esPrimo(numero:Int):String{
    if(numero < 2){
        return "no es primo";
    }
    for (i in 2..<numero){
        if (numero % i  == 0){
            return "no es primo"
        }
    }
    return "es primo"
}

fun esPar(numero:Int):String{
    return if(numero%2==0 ) "es par" else "es impar";
}

fun esFibonacciEsParEsPrimo(numero:Int):String{
    return numero.toString() + " " + esPrimo(numero) + ", " + esFibonacci(numero) + " y " + esPar(numero);

}