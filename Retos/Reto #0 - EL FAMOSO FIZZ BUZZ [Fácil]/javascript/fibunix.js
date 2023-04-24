/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
const fizzBuzz = (init, end) => {
  for (let i = init; i <= end; i++) {
    let multipleOfThree = i % 3 == 0;
    let multipleOfFive = i % 5 == 0;
    let result = "";

    if (!multipleOfThree && !multipleOfFive) {
      console.log(i);
      continue;
    }

    if (multipleOfThree) {
      result += "fizz";
    }

    if (multipleOfFive) {
      result += "buzz";
    }

    console.log(result);
  }
};

/**
 * Test
 */
fizzBuzz(1, 100);
