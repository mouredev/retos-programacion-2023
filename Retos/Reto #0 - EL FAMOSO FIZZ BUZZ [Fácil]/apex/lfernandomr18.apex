/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */
Integer i = 0;
do {
    if(Math.mod(i, 3) == 0 && Math.mod(i, 5) == 0){
        System.debug('fizzbuzz');
    }
    else if(Math.mod(i, 3) == 0){
        System.debug('fizz');
    }
    else if(Math.mod(i, 5) == 0){
        System.debug('buzz');
    }
    else {
        System.debug(i);
    }
    i++;
} while ( i<=100);