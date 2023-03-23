//
// javiCordo.js
//
//
//  Created by Javier Alejandro Cordovés Almaguer on 27/12/22.

/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

function fizzbuzz() {
  let min = 1;
  let max = 100;
  for (let i = min; i <= max; i++) {
    let multipleOfThree = isMultiple(i, 3);
    let multipleOfTFive = isMultiple(i, 5);
    if (multipleOfTFive && multipleOfThree) console.log("fizzbuzz");
    else if (multipleOfThree) console.log("fizz");
    else if (multipleOfTFive) console.log("buzz");
    else console.log(i);
  }
}

/**
 *
 * @param value value to compare
 * @param multiple multiple number
 * @returns true if the value is a multiple of and false if it is not.
 */
function isMultiple(value, multiple) {
  switch (multiple) {
    case 3:
      return value % multiple === 0 ? true : false;
    case 5:
      return value % multiple === 0 || value % multiple === 5 ? true : false;
  }
}

fizzbuzz();
