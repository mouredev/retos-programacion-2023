/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const isEven = (num) => {

  return num % 2 === 0;
};

const isFibonacci = (num) => {

  const checkPlus = Math.sqrt(5 * num * num + 4) % 1 === 0;
  const checkMinus = Math.sqrt(5 * num * num - 4) % 1 === 0;

  return checkPlus || checkMinus;
};

const isPrime = (num) => {

  if (num < 2) return false;
  if (num === 2) return true;
  if (isEven(num)) return false;

  for (let i = 3; i * i <= num; i += 2) {
    if (num % i === 0) return false;
  }

  return true;
};

const checkNumber = (num) => {

  return `${num} ${isPrime(num) ? '' : 'no '}es primo, ${isFibonacci(num) ? '' : 'no '} es fibonacci y es ${isEven(num) ? 'par' : 'impar'}`;
};

console.log(checkNumber(2));
console.log(checkNumber(4));
console.log(checkNumber(7));
console.log(checkNumber(13));
console.log(checkNumber(27644437));
console.log(checkNumber(27644439));
console.log(checkNumber(479001599));