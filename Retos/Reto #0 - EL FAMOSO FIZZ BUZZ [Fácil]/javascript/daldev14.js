/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

function FizzBuzz() {
  for (let i = 1; i <= 100; i++) {
    let output = `${i % 3 == 0 ? "fizz" : ""}${i % 5 == 0 ? "buzz" : ""}`;
    console.log(output ? output : i);
  }
}

FizzBuzz();

/* utilizando array */

function FizzBuzzv2() {
  const FizzBuzzArray = new Array(100).fill(0).map((_value, index) => {
    if ((index + 1) % 5 == 0 && (index + 1) % 3 == 0) return "fizzbuzz";
    if ((index + 1) % 3 == 0) return "fizz";
    if ((index + 1) % 5 == 0) return "buzz";

    return index + 1;
  });

  FizzBuzzArray.forEach((el) => console.log(el));
}

FizzBuzzv2();