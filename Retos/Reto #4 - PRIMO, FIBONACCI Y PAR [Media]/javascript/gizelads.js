/* Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
Ejemplos:
- Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
- Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar" */

function esPar(num) {
    if (num % 2 === 0) {
        return true
    } else {
        return false
    }
}

function esFibonacci(num) {
    let aux1 = 0
    let aux2 = 1
    let fibo = 0
    while (fibo < num) {
        fibo = aux1 + aux2
        aux1 = aux2
        aux2 = fibo
    }
        
    if (num === fibo) {
        return true
    } else {
        return false
    }
}

function esPrimo(num) {
    let cont = 0
    for (let i = 1; i <= num; i++) {
        if (num % i == 0) {
            cont++
        }
    }

    if (cont == 2) {
        return true
    } else {
        return false
    }
}

function primoFibonacciPar(num) {
    let respuesta = ""

    if (esPrimo(num)) {
        respuesta = num + " es primo, "
    } else {
        respuesta = num + " no es primo, "
    }

    if (esFibonacci(num)) {
        respuesta += "fibonacci y "
    } else {
        respuesta += "no es fibonacci y "
    }

    if (esPar(num)) {
        respuesta += "es par."
    } else {
        respuesta += "es impar."
    }
    console.log(respuesta)
}

// primoFibonacciPar(2)
// 2 es primo, fibonacci y es par.

// primoFibonacciPar(7)
// 7 es primo, no es fibonacci y es impar.

// primoFibonacciPar(8)
// 8 no es primo, fibonacci y es par.

// primoFibonacciPar(95)
// 95 no es primo, no es fibonacci y es impar.

// primoFibonacciPar(1)
// 1 no es primo, fibonacci y es impar.