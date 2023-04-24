/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

export function isPrime(num: number): boolean {
    if (num < 2) {
        return false;
    }
    for (let i = 2; i < num; i++) {
        if (num % i == 0) {
            return false;
        }
    }
    return true;
}

export function isFibonacci(num: number): boolean {
    let a = 0;
    let b = 1;
    let c = 1;
    while (c < num) {
        c = a + b;
        a = b;
        b = c;
    }
    return c == num;
}

export function isEven(num: number): boolean {
    return num % 2 == 0;
}

export function isPrimeFibonacciEven(num: number): string {
    let result = '';
    if (isPrime(num)) {
        result += 'primo, ';
    } else {
        result += 'no primo, ';
    }
    if (isFibonacci(num)) {
        result += 'fibonacci y';
    } else {
        result += 'no fibonacci y ';
    }
    if (isEven(num)) {
        result += 'par';
    } else {
        result += 'impar';
    }
    return result;
}
