// Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
// Ejemplos:
//          - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
//          - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar" 

const isEven = (number: number): boolean => number % 2 === 0;

const isPrime = (number: number): boolean => {
  let index = 1;
  let isDivideBy = 0;

  while (index <= number) {
    if (number % index === 0) isDivideBy++;
    index++;
  }

  return isDivideBy === 2;
};

const isFibo = (number: number, count = 1, last = 0): boolean => {
  if (count < number) {
    return isFibo(number, count + last, count);
  }
  if (count === number) {
    return true;
  }
  return false;
};

const printNumber = (number: number) => {
  let numberIsPrime = isPrime(number) ? 'es primo' : 'no es primo';
  let numberIsFibo = isFibo(number) ? 'fibonacci' : 'no es fibonacci';
  let numberIsEven = isEven(number) ? 'es par' : 'es impar';

  let message = `${number} ${numberIsPrime}, ${numberIsFibo} y ${numberIsEven}`;

  console.log(message);
};

printNumber(8);
