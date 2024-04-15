/*# Reto #4: PRIMO, FIBONACCI Y PAR
#### Dificultad: Media | Publicación: 23/01/23 | Corrección: 30/01/23

## Enunciado

 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"

*/

function esPrimo(numero) {
    for (let i = 2; i < numero; i++) {
        if (numero % i === 0) {
            return false;
        }
    }
    return numero > 1;
}

function esPar(numero) {
    return numero % 2 === 0;
}

function esFibonacci(numero) {
    const sqrt5 = Math.sqrt(5);
    const phi = (1 + sqrt5) / 2;

    const a = phi * numero;
    return Number.isInteger(a) && a > 0;
}

function analizarNumero(numero) {
    const esPrimoResultado = esPrimo(numero) ? "es primo" : "no es primo";
    const esParResultado = esPar(numero) ? "es par" : "es impar";
    const esFibonacciResultado = esFibonacci(numero) ? "es fibonacci" : "no es fibonacci";

    console.log(`${numero} ${esPrimoResultado}, ${esFibonacciResultado} y ${esParResultado}`);
}

// Ejemplos de uso:
analizarNumero(2);
analizarNumero(7);

