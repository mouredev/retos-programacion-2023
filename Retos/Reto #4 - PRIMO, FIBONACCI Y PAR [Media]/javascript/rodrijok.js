/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

function primoFibonacciPar(number){
    let isPrime = true;
    let isFibonacci = false;
    let isEven = false;

    if(number % 2 == 0) isEven = true;

    for(let i = 2; i < number; i++){
        if(number % i == 0){
            isPrime = false;
            break;
        }
    }

    let fibonacci = [0, 1];
    for(let i = 2; i < number; i++){
        fibonacci[i] = fibonacci[i - 1] + fibonacci[i - 2];
    }

    if(fibonacci.includes(number)) isFibonacci = true;
    else isFibonacci = false;

    let message = `
                   ---------------------
                   | Numero       -> ${number} |
                   ---------------------
                   | Es primo     | ${isPrime ? "✅" : "❌" } |
                   | Es fibonacci | ${isFibonacci ? "✅" : "❌" } |
                   | Es par       | ${isEven ? "✅" : "❌" } |
                   ---------------------`;  
    return message; 
}

console.log(primoFibonacciPar(2));
console.log(primoFibonacciPar(8));
console.log(primoFibonacciPar(16));
console.log(primoFibonacciPar(34));
