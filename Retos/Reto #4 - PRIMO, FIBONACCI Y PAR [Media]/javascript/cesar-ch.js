/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const checkNumber = (e) => {
    
  let answer = `${e} `;
  const primeNumber = (e) => {
    let prime = true;
    for (let i = 2; i < e; i++) {
      e % i === 0 ? (prime = false) : prime;
    }
    prime ? (answer += "es primo, ") : (answer += "no es primo, ");
  };

  const fibonacciNumber = (e) => {
    let fibonacci = false;
    let numOne = 1;
    let numTwo = 1;
    for (let i = 2; i <= e; i++) {
      [numOne, numTwo] = [numOne + numTwo, numOne];
      e === numOne
        ? (fibonacci = fibonacci || true)
        : (fibonacci = fibonacci || false);
    }
    fibonacci ? (answer += "fibonacci ") : (answer += "no es fibonacci ");
  };

  const parNumber = (e) => {
    e % 2 === 0 ? (answer += "y es par") : (answer += "y es impar");
  };

  primeNumber(e);
  fibonacciNumber(e);
  parNumber(e);

  return answer;
};

//   console.log(checkNumber(2)); //2 es primo, fibonacci y es par
//   console.log(checkNumber(7)); //7 es primo, no es fibonacci y es impar
