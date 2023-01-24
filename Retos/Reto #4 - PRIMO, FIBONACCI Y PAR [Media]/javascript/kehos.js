/*
 * Reto #4 - Primo, Fibonacci y Par
 * Propuesta de solución realizada por Kehos
 * https://github.com/Kehos
 * 24/01/2023
 */

let isPrime = false;
let isFibonacci = false;
let isEven = false;

function checkPrime() {}

function checkFibonacci() {}

function checkEven() {}

function checkNumber(number) {
  if (!isNaN(number) && typeof number === 'number') {
    checkPrime(number);
    checkFibonacci(number);
    checkEven(number);
    console.log(`- ${number} ${isPrime ? '' : 'no '}es primo, ${isFibonacci ? '' : 'no es '}fibonacci y es ${isEven ? 'par' : 'impar'}.`);
  } else {
    console.log('- El valor introducido no es un número correcto');
  }
}

console.log('\n');
checkNumber(2);
checkNumber(100);
checkNumber('hello');
checkNumber(false);
