/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

const isEven = (number) => {
  if (number % 2 === 0) {
    return true;
  } else {
    return false;
  }
};

const isFibonnaci = (number) => {
  let list_of_number = [0, 1];
  for (let i = 2; i <= 2500; i++) {
    list_of_number.push(list_of_number[i - 2] + list_of_number[i - 1]);
  }
  if (list_of_number.indexOf(number) !== -1) {
    return true;
  } else {
    return false;
  }
};

const isPrime = (number) => {
  let count = 0;
  if (number > 0) {
    for (let i = 0; i <= number; i++) {
      if (number % i === 0) {
        count += 1;
      } 
    }
    if (count === 2) {
        return true
    } else {
        return false
    }
  }
  return false;
};


