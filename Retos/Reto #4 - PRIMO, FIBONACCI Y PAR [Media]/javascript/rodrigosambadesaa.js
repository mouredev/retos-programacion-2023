'use strict';

function isPrime(number) {
  if (!Number.isInteger(number) || number < 2) return false;
  if (number === 2) return true;
  if (number % 2 === 0) return false;
  for (let divisor = 3; divisor * divisor <= number; divisor += 2) {
    if (number % divisor === 0) return false;
  }
  return true;
}

function isFibonacci(number) {
  if (!Number.isInteger(number) || number < 0) return false;
  const isSquare = value => Number.isInteger(Math.sqrt(value));
  return isSquare(5 * number * number + 4) || isSquare(5 * number * number - 4);
}

function describeNumber(number) {
  if (!Number.isInteger(number)) throw new TypeError('Se esperaba un número entero');
  return `${number} ${isPrime(number) ? 'es primo' : 'no es primo'}, ` +
    `${isFibonacci(number) ? 'fibonacci' : 'no es fibonacci'} y ` +
    `${number % 2 === 0 ? 'es par' : 'es impar'}`;
}

module.exports = { isPrime, isFibonacci, describeNumber };

if (require.main === module) console.log(describeNumber(Number(process.argv[2] ?? 2)));
