/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

const FROM_NUMBER = 1;
const TO_NUMBER = 100;

const fizzbuzz = () => {
    for(let x=FROM_NUMBER; x<=TO_NUMBER; x++){
        x % 15 == 0  ? console.log('fizzbuzz')
                    : x % 5 == 0    ? console.log('buzz')
                                    : x % 3 == 0    ? console.log('fizz')
                                                    : console.log(x)
    }
}

fizzbuzz();