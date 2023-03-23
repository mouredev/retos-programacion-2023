/*

 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

*/

function fizzBuzz() {
  let numba = 1;
  while (numba <= 100) {
    const multiples = { 3: 'fizz', 5: 'buzz' };
    let output = '';
    Object
      .entries(multiples)
      .forEach(([multiplier, word]) => {
        if (numba % multiplier === 0) output += word;
      });

    output = output === '' ? numba.toString() : output;
    console.log(`${output}`);
    numba++;
  }
}

fizzBuzz();