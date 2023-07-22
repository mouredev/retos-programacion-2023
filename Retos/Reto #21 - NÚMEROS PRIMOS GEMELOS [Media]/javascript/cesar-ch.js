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

function twinNumbers(max) {
    let primeNumbers = []
    for (let i = 2; i <= max; i++) {
        let isPrime = 0
        for (let j = 1; j <= i; j++) {
            if (i % j === 0) {
                isPrime++
            }
        }
        if (isPrime === 2) {
            primeNumbers.push(i)
        }
    }
    let twinNumbers = []
    for (let i = 0; i < primeNumbers.length; i++) {
        if (primeNumbers[i + 1] - primeNumbers[i] === 2) {
            twinNumbers.push(`(${primeNumbers[i]}, ${primeNumbers[i + 1]})`)
        }
    }
    return twinNumbers
}

console.log(twinNumbers(100))