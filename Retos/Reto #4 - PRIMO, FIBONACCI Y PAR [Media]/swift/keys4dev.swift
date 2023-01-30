import UIKit

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

func esFibonacci(numero:Int)->(String){
    if (numero == 0){
        return "es fibonacci";
    }
        
    var secuencia = [0,1]
    while (secuencia[secuencia.count-1]<numero){
        secuencia.append(secuencia[secuencia.count-1]+secuencia[secuencia.count-2])
    }
    
    var resultado = secuencia[secuencia.count-1] == numero ? "es fibonacci" : "no es fibonacci"
    return resultado
}

func esPrimo(numero:Int)->(String){
    if(numero < 2){
        return "no es primo";
    }
    for i in 2..<numero{
        if (numero % i  == 0){
            return "no es primo"
        }
    }
    return "es primo"
}

func esPar(numero:Int)->(String){
    return numero%2==0 ? "es par" : "es impar";
}

func esFibonacciEsParEsPrimo(numero:Int)->(String){
    
    //return String(numero) + " " + esPrimo(numero: numero) + ", " + esFibonacci(numero: numero) + " y " + esPar(numero: numero);
    return String(numero) + " " + esPrimo(numero: numero) + ", " + esFibonacci(numero: numero) + " y " + esPar(numero: numero);
}



print(esFibonacciEsParEsPrimo(numero:11))