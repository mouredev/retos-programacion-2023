const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let userInput = 0;
rl.question("Ingresa un número: ", (answer) => {
  userInput = Number(answer);

  console.log(
    `El número ${userInput} ${isPrime(userInput).msg},` +
      ` ${isFibonacci(userInput).msg} y ` +
      ` ${esPar(userInput).msg}`
  );

  rl.close();
});

/**
 * Check if a number is a Pair or not
 * @param {Number} num number to check if its pair or not
 * @returns {Object} the result object {is, msg}
 */
function esPar(num) {
  if (num % 2 == 0) {
    return {
      is: true,
      msg: "es Par",
    };
  } else {
    return {
      is: false,
      msg: "es Impar",
    };
  }
}

/**
 * Regresa si es un número primo. Los números primos son aquellos que solo tienen 2 factores: 1 y ellos mismos.
 * @param {*} num
 * @returns {Object} the result object {is, msg}
 */
function isPrime(num) {
  let output = {};
  const isPrimeOrNot = () => {
    if (num <= 1) {
      return false;
    }
    if (num <= 3) {
      return true;
    }
    if (num % 2 === 0 || num % 3 === 0) {
      return false;
    }

    for (let i = 5; i * i <= num; i += 6) {
      if (num % i === 0 || num % (i + 2) === 0) {
        return false;
      }
    }

    return true;
  };

  output["is"] = isPrimeOrNot();
  output["msg"] = isPrimeOrNot() == true ? "es primo" : "no es Primo";
  return output;
}

function fibonacci(n) {
  // The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. It starts with 0 and 1.

  if (n <= 1) {
    return n;
  } else {
    return fibonacci(n - 1) + fibonacci(n - 2);
  }
}

/**
 * Check if a number is part of the fibonacci sequence
 * @param {Number} n Number that if going to be screen to check if its a fibonacci or not
 * @returns {Object} the result object {is, msg}
 */
function isFibonacci(n) {
  let fibonacciSeq = [];

  for (let num = 0; num <= n + 1; num++) {
    fibonacciSeq.push(fibonacci(num));
  }

  let output = {};
  output.seq = fibonacciSeq;
  output.number = n;

  if (fibonacciSeq.includes(n)) {
    output["is"] = true;
    output["msg"] = "fibonacci";
  } else {
    output["is"] = false;
    output["msg"] = "no es fibonacci";
  }

  return output;
}
