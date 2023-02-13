"use strict";

function evalNumber(number) {
  let outSentence = `${number} `;
  outSentence += isPrime(number) ? "es primo, " : "no es primo, ";
  outSentence += isFibbonacci(number) ? "fibonacci " : "no es fibbonacci ";
  outSentence += isEven(number) ? "y es par" : "y es impar";
  return outSentence;
}

const isPrime = (number) => {
  if (number === 2) return true;
  for (let i = 2; i < number; i++) {
    if (number % i === 0) return false;
  }
  return true;
};

const isFibbonacci = (number, a = 0, b = 1) => {
  if (number === 0 || number === 1) return true;
  let nextNumber = a + b;
  if (nextNumber === number) return true;
  if (nextNumber > number) return false;
  return isFibbonacci(number, b, nextNumber);
};

const isEven = (number) => {
  return number % 2 === 0;
};

const start = () => {
  console.log(evalNumber(2));
  console.log(evalNumber(7));
  console.log(evalNumber(13));
  console.log(evalNumber(8));
  console.log(evalNumber(49));
};

start();
