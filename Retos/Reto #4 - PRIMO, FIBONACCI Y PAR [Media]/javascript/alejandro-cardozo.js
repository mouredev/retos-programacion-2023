/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

/**
 *  Retrieves a string that explains whether the passed argument is a prime number, 
 *  whether it belongs to the Fibonacci sequence, and whether it is even.
 *  @param {number} num Integer number
 *  @returns {string} String describing the details of the number passed
 */

function isPrimeFibonacciEven(num) {
  let prime = true;
  let fibo = true;
  let even = true;

  // Checking if num is prime
  for (let i = 2, s = Math.sqrt(num); i <= s; i++) {
    if (num % i === 0) {
      prime = false;
      break;
    }
  }
  prime = prime && num > 1;

  // Checking if num belongs to the Fibonacci sequence
  // Formula's source: https://en.wikipedia.org/wiki/Fibonacci_number#Identification
  fibo =
    Math.sqrt(5 * Math.pow(num, 2) + 4) % 1 === 0 ||
    Math.sqrt(5 * Math.pow(num, 2) - 4) % 1 === 0;

  // Checking if num is even
  even = num % 2 === 0;

  return `${num}${prime ? '' : ' no'} es primo,${
    fibo ? '' : ' no'
  } es fibonacci y es ${even ? 'par' : 'impar'} `;
}

// Tests
// console.log(isPrimeFibonacciEven(1));
// console.log(isPrimeFibonacciEven(2));
// console.log(isPrimeFibonacciEven(3));
// console.log(isPrimeFibonacciEven(4));
// console.log(isPrimeFibonacciEven(5));
// console.log(isPrimeFibonacciEven(6));
// console.log(isPrimeFibonacciEven(7));
// console.log(isPrimeFibonacciEven(8));
// console.log(isPrimeFibonacciEven(9));
// console.log(isPrimeFibonacciEven(10));
