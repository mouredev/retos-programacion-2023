/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
// TODO: [X] Detect if the number given is Fibonacci
// TODO: [X] Detect if the number given is prime
// TODO: [X] Detect if the number given is par
// TODO: [ ] Return message

function numberProperties(number: number) {
    // Check if the number given is par
    const isPar = number % 2 === 0;
    console.log(isPar)

    // Check if the number given is prime
    let isPrime = false;
    let primeCounter = 0;
    for (let i = 1; i <= number; i++) {
        console.log(`The rest of ${number} by ${i} is equal to: ${number % i}`)
        if (number % i === 0) ++primeCounter;
    }
    if (primeCounter === 2) isPrime = true;
    console.log(isPrime)

    // Check if the number given is fibonacci
    let f1 = 0;
    let f2 = 1;
    let f3 = 0;
    let fibonacci: number[] = [];
    while (f3 < number) {
        f3 = f1 + f2;
        f2 = f1;
        f1 = f3;
        fibonacci.push(f3)
        console.log(fibonacci)
    }
    const isFibonacci = fibonacci.some(n => n === number);
    return isFibonacci;
}

console.log(numberProperties(144))