/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

//Generamos una modularización de funciones para aplicarlas a la función principal que es testNumber(n).

function cuadrado(valor) {  
  const raiz = Math.sqrt(valor); // Aplicamos la raiz cuadrada al argumento
  return raiz === Math.floor(raiz); // Comprobamos si la raiz cuadrada entrega un número entero
}

function esFibo(n) {
  let test1 = cuadrado(5 * n * n + 4); // Llamamos a la funcion cuadrado perfecto
  let test2 = cuadrado(5 * n * n - 4);
  return test1 || test2; // Comprobamos y devolvemos cual es true
}

function esPar(n) {
  return n % 2 === 0; // Comprobamos y devolvemos si es true o false
}

function esPrimo(n) {
  if (n <= 1) { // El número 1 se descarta por regla
    return false;
  }
  for (let i = 2; i <= Math.sqrt(n); i++) { // Generamos una iteración para probar el número con todos los valores
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

function testNumber(n) { // Función principal, llamamos a todas las funciones anteriores para aplicar el valor
  let par = esPar(n)
    ? console.log(`El número ${n} es par`)
    : console.log(`El número ${n} no es par`);
  let fibo = esFibo(n)
    ? console.log(`El número ${n} es fibonacci`)
    : console.log(`El número ${n} no es fibonacci`);
  let primo = esPrimo(n)
    ? console.log(`El número ${n} es primo`)
    : console.log(`El número ${n} no es primo`);
}

const nuevotest = testNumber(3);
