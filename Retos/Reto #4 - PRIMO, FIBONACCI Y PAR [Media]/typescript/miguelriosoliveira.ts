/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

function isPrime(num: number): boolean {
  if (num <= 1) {
    return false;
  }

  for (let i = 2; i <= num / i; i++) {
    if (num % i === 0) {
      return false;
    }
  }

  return true;
}

function isPerfectSquare(num: number): boolean {
  const sqrt = Math.floor(Math.sqrt(num));
  return sqrt * sqrt === num;
}

function isFibonacci(num: number): boolean {
  return isPerfectSquare(5 * num * num + 4) || isPerfectSquare(5 * num * num - 4);
}

function isEven(num: number): boolean {
  return num % 2 === 0;
}

function isPrimeFibonacciAndEven(num: number): string {
  let message = `${num} `;

  if (!isPrime(num)) {
    message += 'no ';
  }
  message += 'es primo, ';

  if (!isFibonacci(num)) {
    message += 'no es ';
  }
  message += 'fibonacci y es ';

  if (!isEven(num)) {
    message += 'im';
  }
  message += 'par';

  return message;
}

function test() {
  [
    { input: 2, expected: '2 es primo, fibonacci y es par' },
    { input: 7, expected: '7 es primo, no es fibonacci y es impar' },
    { input: 8, expected: '8 no es primo, fibonacci y es par' },
    { input: 9, expected: '9 no es primo, no es fibonacci y es impar' },
  ].every(({ input, expected }) => {
    const received = isPrimeFibonacciAndEven(input);
    const hasPassed = received === expected;
    if (received === expected) {
      console.log('✅ PASSED');
    } else {
      console.log('❌ FAILED', { expected, received });
    }
    return hasPassed;
  });
}

test();
