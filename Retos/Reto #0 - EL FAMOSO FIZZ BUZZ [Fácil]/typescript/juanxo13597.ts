/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

export function fizzBuzz(limit: number) {
    const result: string[] = [];
    for (let i: number = 1; i <= limit; i++) {
        result.push(
            i % 3 === 0 && i % 5 === 0 ? 'fizzbuzz' : i % 3 === 0 ? 'fizz' : i % 5 === 0 ? 'buzz' : i.toString()
        );
    }

    return result;
}

console.log(fizzBuzz(100));
