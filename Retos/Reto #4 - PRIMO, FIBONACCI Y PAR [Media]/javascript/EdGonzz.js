// ```
// /*
//  * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
//  * Ejemplos:
//  * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
//  * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
//  */
// ```

function isNumeroPrimo(num) {
    let isPrimo = true
    let result

    if (num < 1) {
        isPrimo = false
    }

    for (let i = 2; i < num; i++) {
        if (num % i === 0) {
            isPrimo = false
        }
    }

    isPrimo == true ? result = 'es primo' : result = 'es compuesto';
    return result
}

function isFibonacci(num) {
    let result
    let prev1 = 0
    let prev2 = 1

    for (let i = 0; i < num; i++) {
        var suma = prev1 + prev2
        prev1 = prev2
        prev2 = suma
    }

    num == suma ? result = 'es Fibonacci' : result = 'no es Fibonacci'
    return result
}

function isNumeroPar(num) {
    let result
    num % 2 === 0 ? result = 'es par' : result = 'es impar'
    return result
}

function comprobar(num) {
    console.log(`${num} ${isNumeroPrimo(num)}, ${isFibonacci(num)} y ${isNumeroPar(num)}`);
}

comprobar(2)
comprobar(7)
comprobar(8)
comprobar(13)
comprobar(0)
comprobar(256)