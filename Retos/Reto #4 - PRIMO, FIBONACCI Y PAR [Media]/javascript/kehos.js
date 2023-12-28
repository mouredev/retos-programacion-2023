/*
 * Reto #4 - Primo, Fibonacci y Par
 * Propuesta de solución realizada por Kehos
 * https://github.com/Kehos
 * 24/01/2023
 */

let isPrime = true;
let isFibonacci = false;
let isEven = false;

function checkPrime(number) {
  isPrime = true;
  
  if (number === 0 || number === 1) {
    isPrime = false;
  }

  for (let i = 2; i < number; i++) {
    if (number % i === 0) {
      isPrime = false;
      break;
    }
  }
}

function checkFibonacci(number) {
  isFibonacci = (isPerfectSquare(5 * number * number + 4) || isPerfectSquare(5 * number * number - 4));
}

function isPerfectSquare(number) {
  const square = parseInt(Math.sqrt(number));
  return number === square * square;
}

function checkEven(number) {
  isEven = number % 2 === 0;
}

function checkNumber(value) {
  if (!isNaN(value) && typeof value === 'number') {
    checkPrime(value);
    checkFibonacci(value);
    checkEven(value);
    console.log(`- ${value} ${isPrime ? '' : 'no '}es primo, ${isFibonacci ? '' : 'no '}es fibonacci y es ${isEven ? 'par' : 'impar'}.`);
  } else {
    console.log(`- El valor introducido ("${value}") no es un número válido`);
  }
}

const valueArray = [ 1, 0, 2, 100, true, 8, 'Hello', 7, {}, 93, 13 ];
console.log('\nValores a evaluar: ', valueArray, '\n');
valueArray.forEach( value => checkNumber(value) );
