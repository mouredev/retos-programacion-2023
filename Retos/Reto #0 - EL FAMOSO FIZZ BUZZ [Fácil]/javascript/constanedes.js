/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

function fizzbuzzTest(){
    for (i = 1; i <= 100; i++) {
        switch (true) {
            case i % 15 === 0:
                console.log('fizzbuzz')
                break;
            case i % 5 === 0:
                console.log('buzz');
                break;
            case i % 3 === 0:
                console.log('fizz');
                break;  
            default:
                console.log(i);
        }
    }
}

function fizzbuzzCompressed(){
    for (i = 1; i <= 100; i++) console.log((i%3?'':'fizz')+(i%5?'':'buzz') || i)
}
