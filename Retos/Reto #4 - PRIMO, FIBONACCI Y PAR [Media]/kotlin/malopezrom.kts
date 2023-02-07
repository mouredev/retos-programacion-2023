/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

/**
 * Comprueba si un número es primo
 * @param number Número a comprobar
 * @return true si es primo, false si no lo es
 */
fun isPrime(num: Int): Boolean {
    if (num <= 1) {
        return false
    }

    for (i in 2..num / 2) {
        if (num % i == 0) {
            return false
        }
    }

    return true
}

/**
 * Comprueba si un numero es par
 * @param number Número a comprobar
 * @return true si es par, false si no lo es
 *
 */
fun isEven(num: Int): Boolean {
    return num % 2 == 0
}

/**
 * Comprueba si un número es fibonacci
 * @param number Número a comprobar
 * @return true si es fibonacci, false si no lo es
 */
fun isFibonacci(num: Int): Boolean {
    return if(num>0){
        isPerfectSquare(5 * num * num + 4) || isPerfectSquare(5 * num * num - 4)
    }else{
        false
    }
}

/**
 * Comprueba si un numero es un cuadrado perfecto
 * @param number Número a comprobar
 * @return true si es un cuadrado perfecto, false si no lo es
 */
fun isPerfectSquare(num: Int): Boolean {
    return Math.sqrt(num.toDouble()) % 1 == 0.0

}

/**
 * Comprueba si un número es primo, fibonacci y par
 * @param number Número a comprobar
 * @return String con el resultado
 */
fun checkNumber(num: Int): String {
    var result = "$num es "

    if (isPrime(num)) {
        result += "primo, "
    } else {
        result += "no primo, "
    }

    if (isFibonacci(num)) {
        result += "fibonacci, "
    } else {
        result += "no fibonacci, "
    }

    if (isEven(num)) {
        result += "par"
    } else {
        result += "impar"
    }

    return result
}

/**
 * Funcion Principal
 */
fun main(){
    println(checkNumber(2))
    println(checkNumber(7))
    println(checkNumber(8))
    println(checkNumber(13))
    println(checkNumber(21))
    println(checkNumber(34))
    println(checkNumber(55))
    println(checkNumber(0))
    println(checkNumber(-2))
}

main()