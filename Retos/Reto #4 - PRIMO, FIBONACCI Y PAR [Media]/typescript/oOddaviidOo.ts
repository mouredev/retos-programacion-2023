/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
const getRandomNumber = (min: number, max: number): number => {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  };
  
  const isEven = (n: number): boolean => {
    return n % 2 === 0;
  };
  
  const isPrime = (n: number): boolean => {
    if (n > 1 && n % n === 0 && n % 1 === 0) {
      for (let index = n - 1; index > 2; index--) {
        if (n % index === 0) {
          return false;
        }
      }
      return true;
    }
    return false;
  };
  
  const isFibonacci = (n: number): boolean => {
    let fibonacciNumbers: number[] = [0, 1];
    while (fibonacciNumbers[1] <= n) {
      if (n === fibonacciNumbers[1]) {
        return true;
      }
      fibonacciNumbers.push(fibonacciNumbers[0] + fibonacciNumbers[1]);
      fibonacciNumbers.shift();
    }
    return false;
  };
  
  const checkNumber = (n: number) => {
    console.log(`${n} ${isPrime(n) ? 'es' : 'no es'} primo, ${isFibonacci(n) ? 'es': 'no es'} Fibonacci y ${isEven(n) ? 'es par' : 'es impar'}`)
  };
  // checkNumber(0);
  checkNumber(getRandomNumber(-1, 55));
  