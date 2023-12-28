const primeFibonacciEven = (input) => {
  if (parseInt(input) != input) return `${input} no es un número válido`;

  return `${input}${isPrime(input) ? " " : " no "}es primo,${
    isFibonacci(input) ? " es " : " no es "
  }fibonacci y es ${input % 2 == 0 ? "par" : "impar"}`;
};

const isPrime = (input) => {
  if (input < 2) return false;

  let limit = parseInt(Math.sqrt(input));
  if (limit <= 2) limit = input - 1;

  for (let i = 2; i <= limit; i++) {
    if (input % i == 0) return false;
  }
  return true;
};

const isFibonacci = (input) => {
  if (input < 0) return false;

  return (
    perfectSquare(5 * input * input + 4) || perfectSquare(5 * input * input - 4)
  );
};

const perfectSquare = (input) => {
  let squareRoot = parseInt(Math.sqrt(input));
  return squareRoot * squareRoot == input;
};

// A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers.
// Solución número primo: https://en.wikipedia.org/wiki/Prime_number#Trial_division

// The Fibonacci sequence, in which each number is the sum of the two preceding ones.
// The sequence commonly starts from 0 and 1, although some authors start the sequence from 1 and 1 or sometimes (as did Fibonacci) from 1 and 2.
// Solución número fibonacci: https://www.geeksforgeeks.org/check-number-fibonacci-number/

const tests = {
  input: [1, 2, 3, 0, -10, 12.28, 999_999_999],
  output: [
    "1 no es primo, es fibonacci y es impar",
    "2 es primo, es fibonacci y es par",
    "3 es primo, es fibonacci y es impar",
    "0 no es primo, es fibonacci y es par",
    "-10 no es primo, no es fibonacci y es par",
    "12.28 no es un número válido",
    "999999999 no es primo, no es fibonacci y es impar",
  ],
};
let errors = 0;
tests["input"].forEach((test, index) => {
  const resp = primeFibonacciEven(test);
  const expected = tests["output"][index];
  if (resp == expected) return;

  errors += 1;
  console.log(`\n\noriginal: ${test}`);
  console.log(resp);
  console.log(`expected: ${expected}`);
});

console.log(`\nTests${errors != 0 ? " not " : " "}passed, ${errors} errors\n`);
