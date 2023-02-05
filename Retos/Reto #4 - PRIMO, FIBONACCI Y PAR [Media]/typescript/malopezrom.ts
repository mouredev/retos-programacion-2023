/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */


/**
 * Comprueba si un número es primo
 * @param num Número a comprobar
 * @returns true si es primo, false en caso contrario
 */
function isPrime(num: number): boolean {
    if (num <= 1) {
        return false;
    }

    for (let i = 2; i < num; i++) {
        if (num % i === 0) {
            return false;
        }
    }

    return true;
}

/**
 * Comprueba si un número es par
 * @param num Número a comprobar
 * @returns true si es par, false en caso contrario
 */
function isPar(num: number): boolean {
    return num % 2 === 0;
}

/**
 * Comprueba si un número es fibonacci
 * @param num Número a comprobar
 * @returns true si es fibonacci, false en caso contrario
 */
function isFibonacci(num: number): boolean {
    if(num>0) {
    return  isSquare(5 * num * num + 4) || isSquare(5 * num * num - 4)
    } else {
        return false;
    }
}

/**
 * Comprueba si un número es cuadrado perfecto
 * @param num Número a comprobar
 * @returns true si es cuadrado perfecto, false en caso contrario
 */
function isSquare(num: number): boolean {
    return Math.sqrt(num) % 1 === 0;
}

/**
 * Comprueba si un número es primo, fibonacci y par
 * @param num Número a comprobar
 * @returns Cadena con el resultado de la comprobación
 */
function isPrimeFibonacciPar(num: number): string {
    let result = num + " es "

    if (isPrime(num)) {
        result += "primo, ";
    } else {
        result += "no primo, ";
    }

    if (isFibonacci(num)) {
        result += "fibonacci, ";
    } else {
        result += "no fibonacci, ";
    }

    if (isPar(num)) {
        result += "par";
    } else {
        result += "impar";
    }

    return result;
}

/**
 * Casos de prueba
 */

console.log(isPrimeFibonacciPar(2));
console.log(isPrimeFibonacciPar(7));
console.log(isPrimeFibonacciPar(8));
console.log(isPrimeFibonacciPar(13));
console.log(isPrimeFibonacciPar(21));
console.log(isPrimeFibonacciPar(0));
console.log(isPrimeFibonacciPar(-2));

