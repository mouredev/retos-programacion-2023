/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

let inicio = 1

while (inicio <= 100) {
    let multiplo3 = inicio % 3
    let multiplo5 = inicio % 5

    
    if (multiplo3 == 0 && multiplo5 == 5) {
        console.log("fizzbuzz")
    } else if (multiplo3 == 0) {
        console.log("fizz")
    } else if (multiplo5 == 0) {
        console.log("buzz")
    } else {
        console.log(inicio)
    }
    inicio++
}