"use strict";

function isItEvent(number) {
  return number % 2 == 0;
}

function isItPrimeNumber(number) {
  if (number <= 0 || number == 1) return false;

  let counter = 0;
  for (let i = 1; i <= number; i++) {
    if (number % i == 0) {
      counter++;
    }
  }

  return counter == 2;
}

function isItFibonacci(number) {
  if (number == 0) return false;
  if (number == 1) return true;

  let serie = [0, 1];

  //number+1: to iterate 1 more time and thus obtain a series where the value may or may not be contained
  for (let i = 2; i <= number + 1; i++) {
    serie.push(serie[i - 1] + serie[i - 2]);
  }

  return serie.some((element) => element == number);
}

function checkNumber(number) {
  if (typeof number != "number") return "Please enter a numeric value";

  if (!Number.isInteger(number)) return "Please enter a whole number";

  
  let isPar = isItEvent(number) ? "is event" : "is odd";
  let isPrimeNumber = isItPrimeNumber(number)
    ? "is prime"
    : "is not prime";
  let isFibonacci = isItFibonacci(number)
    ? "is fibonacci"
    : "is not fibonacci";

  return `${number} ${isPrimeNumber}, ${isFibonacci} and ${isPar}`;
}

console.log(checkNumber(2));
console.log(checkNumber(7));
