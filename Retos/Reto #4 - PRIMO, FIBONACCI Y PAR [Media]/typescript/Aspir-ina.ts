/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const isEven = (num: number) => num % 2 === 0;

const isPrime = (num: number): boolean => {
  for (let i: number = 2; i < num; i++) {
    if (num % i === 0) return false;
  }

  return true;
}

const isFibonacci = (num: number, a: number = 0, b: number = 1): boolean => {
  const fx: number = a + b;
  if (fx === num) return true;
  if (fx > num) return false;
  return isFibonacci(num, b, fx);
}

const elPrimoElFibonacciYElPar = (num: number): string => {
  if (num < 0) return 'Positive number needed!';

  return `${num} ${isPrime(num) ? 'is' : 'is not'} prime, ${isFibonacci(num) ? 'is' : 'is not'} fibonacci and is ${isEven(num) ? 'even' : 'odd'}`;
}

console.log(elPrimoElFibonacciYElPar(2));
console.log(elPrimoElFibonacciYElPar(5));
console.log(elPrimoElFibonacciYElPar(7));
console.log(elPrimoElFibonacciYElPar(12));