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


function getPairsOfPrimes(range) {
    let pairsOfPrimes = [];
    let pair = [];

    for (let i=2; i<=range; i++) {
        if (isPrime(i)) {
            pair.push(i);
            if (pair.length === 2) {
                if (pair[1] - pair[0] === 2) {
                    pairsOfPrimes.push(pair.slice());
                }
            
                pair.shift();
            }
        }
    }

    return pairsOfPrimes;
}


const isPrime = (number) => {
    if (number < 2) return false;
    
    for (let i=2; i<number; i++) {
        if (number % i === 0) return false;
    }

    return true;
}


function printPairs(pairs) {
    console.log('\nPairs of prime numbers:');
    for (let pair of pairs) {
        console.log(pair);
    }
}


printPairs(getPairsOfPrimes(14));