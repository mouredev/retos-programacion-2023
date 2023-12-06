/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 * 
 * 
 * 
 * EJERCICIO DESARROLLADO POR LAURA ORTEGA - PANCRATZIA (23/08/2023)
 * 
 */


const MultipleOFNumber = (n, number) => n % number == 0 ?  true : false;

for(let i = 1; i <=100; i++){

    let msg ="";

    MultipleOFNumber(i, 3) ? msg += "fizz" : "";
    MultipleOFNumber(i, 5) ? msg += "buzz" : "";
    console.log(msg || i);
    
}


