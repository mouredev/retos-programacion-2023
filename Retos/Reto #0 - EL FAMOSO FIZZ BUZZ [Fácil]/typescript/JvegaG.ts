/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

export const fizzBuzzFunction = (value: number): string => {
    if( value % 3 === 0 && value % 5 === 0)
        return `fizzbuzz`;
    else if (value % 3 === 0)
        return `fizz`;
    else if (value % 5 === 0)
        return `buzz`;
    else
        return `${value}`;
}

for (let i = 1; i <= 100; i++) {
    console.log(`${fizzBuzzFunction(i)}`)
}
