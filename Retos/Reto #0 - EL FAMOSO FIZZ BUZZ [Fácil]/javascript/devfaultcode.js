/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

let numero = 1
let printNumero

while (numero <= 100) {
    numero % 3 == 0 && numero % 5 == 0 ? printNumero = 'fizzbuzz' :
    numero % 3 == 0 ? printNumero = 'fizz' :
    numero % 5 == 0 ? printNumero = 'buzz' :
    printNumero = numero
    console.log(printNumero)
    numero++
}

