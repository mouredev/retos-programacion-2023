/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const checkNumber = (number) => {
  let prime = "no es primo",
    fibonacci = "no es fibonacci",
    par = "es impar";

  const primeNumber = () => {
    if (number === 0 || number === 1 || number === 4) return;
    if (number === 2 || number === 3) prime = "es primo";

    for (let i = 2; i < number / 2; i++) {
      if (number % i === 1) {
        return (prime = "es primo");
      }
    }
  };

  let fibonacciSecuence = () => {
    if (number === 0 || number === 1) fibonacci = "es fibonacci";

    let secuence = [0, 1];
    for (let f = 2; f <= number * 2; f++) {
      secuence.push(secuence[f - 1] + secuence[f - 2]);
      if (secuence.includes(number)) {
        fibonacci = "es fibonacci";
      } else if (secuence[secuence.length - 1] > number) {
        return;
      }
    }
    return fibonacci;
  };

  const parImpar = () => {
    if (number % 2) {
      return;
    } else {
      par = "es par";
    }
  };

  primeNumber();
  fibonacciSecuence();
  parImpar();
  console.log(`${number}: ${prime}, ${fibonacci} y ${par}`);
  // console.log(`${prime}`);
  // console.log(`${fibonacci}`);
  // console.log(`${par}`);
};

checkNumber(1);
checkNumber(2);
checkNumber(3);
checkNumber(4);
checkNumber(5);
checkNumber(8);
checkNumber(11);
checkNumber(12);
checkNumber(13);
// checkNumber(61);
// checkNumber(62);

let FIBONACCI = 5;

let fibonacciNumber = (num) => {
  let secuence = [0, 1];
  for (let f = 2; f <= num; f++) {
    secuence.push(secuence[f - 1] + secuence[f - 2]);
    // console.log(secuence);
    // console.log(secuence.includes(num));
    if (secuence.includes(num)) {
      return `${num} es fibonacci`;
    } else if (secuence[secuence.length - 1] > num) {
      return `${num} no es fibonacci`;
    }
  }
};

// console.log(fibonacciNumber(FIBONACCI));
