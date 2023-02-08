/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

for (let i = 1; i <= 100; i++) {
    let output = '';
    Object.entries({
        3: 'fizz',
        5: 'buzz',
    }).forEach(([multiplier, word]) => {
        if (i % +multiplier === 0) output += word
    });
    console.log(output === '' ?  i : output)
}
