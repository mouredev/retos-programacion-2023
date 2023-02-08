/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
var num = 89

var result = "$num "

result += if (checkPrime(num)) "es primo," else "no es primo,"
result += if (checkFibonacci(num)) " fibonacci y " else "no es fibonacci y "
result += if (checkEvenNum(num)) "es par" else "es impar"


println(result)


fun checkPrime(numToBeChecked: Int): Boolean {
    if(numToBeChecked <= 0) {
        println("Ingrese un numero valido")
        return false
    }

    var primo: Boolean =  true

    for (i in 2..numToBeChecked){
        if(i == numToBeChecked) continue
        if (numToBeChecked % i == 0) {
            primo = false
            break
        }
    }

    return primo
}

fun checkFibonacci(numToBeChecked: Int): Boolean{

    var fibonacci: Boolean = true
    var pastFibonacci = 1
    var tempFibonacci = 0
    var currentFibonacci = 1

    while ( currentFibonacci <= numToBeChecked){
        if (currentFibonacci == numToBeChecked){
            fibonacci = true
            break
        }else{
            fibonacci = false
        }
        tempFibonacci = currentFibonacci
        currentFibonacci =  pastFibonacci + currentFibonacci
        pastFibonacci = tempFibonacci
    }

    return fibonacci
}

fun checkEvenNum(numToBeChecked: Int): Boolean{
    return if (numToBeChecked % 2 == 0) true else false
}
