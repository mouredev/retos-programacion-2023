/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
// TODO: [X] Detect if the number given is Fibonacci
// TODO: [X] Detect if the number given is prime
// TODO: [X] Detect if the number given is par
// TODO: [X] Return message
function numberProperties(number) {
    // Check if the number given is par
    const isPar = number % 2 === 0;
    const parMsg = isPar ? 'es par' : 'es impar';
    // Check if the number given is prime
    let isPrime = false;
    let primeCounter = 0;
    for (let i = 1; i <= number; i++) {
        if (number % i === 0)
            ++primeCounter;
    }
    if (primeCounter === 2)
        isPrime = true;
    const primeMsg = isPrime ? 'es primo' : 'no es primo';
    // Check if the number given is fibonacci
    let f1 = 0;
    let f2 = 1;
    let f3 = 0;
    let fibonacci = [];
    while (f3 < number) {
        f3 = f1 + f2;
        f2 = f1;
        f1 = f3;
        fibonacci.push(f3);
    }
    const isFibonacci = fibonacci.some(n => n === number);
    const fibonacciMsg = isFibonacci ? 'es fibonacci' : 'no es fibonacci';
    // Message
    let message = `${number} ${primeMsg}, ${fibonacciMsg} y ${parMsg}`;
    return message;
}
numberProperties(1); // 1 no es primo, es fibonacci y es impar
numberProperties(7); // 7 es primo, no es fibonacci y es impar
numberProperties(8); // 8 no es primo, es fibonacci y es par
numberProperties(144); // 144 no es primo, es fibonacci y es par
