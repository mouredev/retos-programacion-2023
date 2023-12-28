/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

// Función que comprueba si un número es primo

function esParoImpar(number) {
  if (number % 2 == 0) {
    return "es par";
  } else {
    return "es impar";
  }
}

function esFinonacci(number) {
  let a = 0;
  let b = 1;
  let c = 1;
  while (c < number) {
    c = a + b;
    a = b;
    b = c;
  }
  if (c == number) {
    return "es fibonacci";
  }
  return "no es fibonacci";
}

function esPrimo(number) {
  for (let i = 2; i < number; i++) {
    if (number % i == 0) {
      return "no es primo";
    }
  }
  return "es primo";
}
