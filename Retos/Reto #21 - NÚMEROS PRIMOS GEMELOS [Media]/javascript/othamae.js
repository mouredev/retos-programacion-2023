/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 * 
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */

function twinPrimes(max) {
    twinPrimesNumbers = []
    for (let i = 0; i < max - 2; i++) {
        if (isPrime(i) && isPrime(i + 2)) {
            twinPrimesNumbers.push([i, i + 2])
        }
    }
    return twinPrimesNumbers;
}

function isPrime(n) {
    if (n <= 2) return false
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) return false
    }
    return true
}

console.log(twinPrimes(14))