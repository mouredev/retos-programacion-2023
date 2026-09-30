'use strict';

function isPrime(number) {
  if (number < 2 || !Number.isInteger(number)) return false;
  for (let divisor = 2; divisor * divisor <= number; divisor++) {
    if (number % divisor === 0) return false;
  }
  return true;
}

function twinPrimes(limit) {
  if (!Number.isInteger(limit) || limit < 1) throw new Error('El rango debe ser un entero positivo');
  const pairs = [];
  for (let number = 3; number + 2 <= limit; number++) {
    if (isPrime(number) && isPrime(number + 2)) pairs.push([number, number + 2]);
  }
  return pairs;
}

module.exports = { twinPrimes };

if (require.main === module) console.log(twinPrimes(Number(process.argv[2] ?? 14)));
