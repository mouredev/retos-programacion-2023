/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

/**
 * 
 * @param {Number} startNum 
 * @param {Number} endNum 
 */
const printNumbers = (startNum = 1, endNum = 100) => {
    while (startNum <= endNum) {
        let result = fizzBuzzValue(startNum)
        console.log(result);
        startNum++
    }

}

/**
 * 
 * @param {Number} num 
 * @returns {String|Number}
 */
const fizzBuzzValue = (num) => {
    let validation = (num % 3 === 0 && num % 5 === 0)
        ? 'fizzbuzz'
        : (num % 3 === 0)
            ? 'fizz'
            : (num % 5 === 0)
                ? 'buzz'
                : num;
    return validation

}

printNumbers();


