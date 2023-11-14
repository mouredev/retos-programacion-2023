/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 *
 *
 * EJERCICIO REALIZADO POR LAURA ORTEGA 24/08/2023
 *
 */

const esPrimo = (numero) => {
  let primo = true;

  numero < 1 ? (primo = false) : (primo = true);
  for (let i = 2; i < numero; i++) if (numero % i === 0) primo = false;

  return primo;
};

const esPar = (numero) => {
  return numero % 2 === 0;
};

const esFibonacci = (numero) => {
  let aux1 = 0;
  let aux2 = 1;
  let fibo = 0;
  while (fibo < numero) {
    fibo = aux1 + aux2;
    aux1 = aux2;
    aux2 = fibo;
  }
  if (numero === fibo) {
    return true;
  } else {
    return false;
  }
};

const validarNumero = (numero) =>
  `${numero} ${esPrimo(numero) ? "es primo" : "no es primo"}, ${
    esFibonacci(numero) ? "es fibonacci" : "no es fibonacci"
  } y ${esPar(numero) ? "es par" : "es impar"}`;

console.log(validarNumero(7));
console.log(validarNumero(2));
console.log(validarNumero(3));
console.log(validarNumero(-4));
console.log(validarNumero(55));
