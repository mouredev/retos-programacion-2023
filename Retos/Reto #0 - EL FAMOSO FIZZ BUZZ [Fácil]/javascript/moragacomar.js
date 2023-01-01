/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

/* FUNCIÓN PRINT */

const print = (texto) => console.log(texto);


/* FUNCIÓN FIZZBUZZ V2 */

const fizzbuzz = (numMax) => {
    for (let i = 1; i <= numMax; i++) {
        i % 15 === 0 ? print("fizzbuzz") : i % 5 === 0 ? print("buzz") : i % 3 === 0 ? print("fizz") : print(i);
    }
}

/* LLAMADA A LA FUNCIÓN FIZZBUZZ V2 */

fizzbuzz(100);


/* FUNCIÓN FIZZBUZZ V1 */

// const fizzbuzz = (numMax) => {
//     for (let i = 1; i <= numMax; i++) {
//         if (i % 15 === 0) {
//             console.log("fizzbuzz");
//         } else if (i % 3 === 0) {
//             console.log("fizz");
//         } else if (i % 5 === 0) {
//             console.log("buzz");
//         } else {
//             console.log(i);
//         }
//     }
// }

