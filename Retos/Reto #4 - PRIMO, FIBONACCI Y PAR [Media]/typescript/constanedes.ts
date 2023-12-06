/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

function isFibonacci(num: number): boolean {
    let a = 0, b = 1;
    while (b < num) [a, b] = [b, a + b];
    return b === num;
}

function isPrime(num: number): boolean {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}

function isEven(num: number): boolean {
    return num % 2 === 0;
}

function checkEvenFibonacciPrime(num: number): string {
    let result = `${num} `;
    result += `${isPrime(num) ? 'es primo, ' : 'no es primo, '}`;
    result += `${isFibonacci(num) ? 'fibonacci' : 'no es fibonacci'}`;
    result += `${isEven(num) ? ' y es par' : ' y es impar'}`;
    return result;
}

console.log(checkEvenFibonacciPrime(7));
