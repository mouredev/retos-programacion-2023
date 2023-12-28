function excellColumnToNumber(column: string): number {
    if (!column.match(/^[A-Z]+$/)) throw new Error('Invalid column format');
    return column.split('').reduce((acc, cur) => acc * 26 + cur.charCodeAt(0) - 64, 0);
}

console.log('A', excellColumnToNumber('A')); // 1
console.log('Z', excellColumnToNumber('Z')); // 26
console.log('AA', excellColumnToNumber('AA')); // 27
console.log('CA', excellColumnToNumber('CA')); // 79

// Explicacion
/**
 * .split('') divide el string en un array de caracteres
 * .reduce(fn, init) recorre el array y va acumulando el valor de cada iteracion (el parametro fn es una lambda que ejecutara en cada iteracion);
 * el segundo parametro de .reduce(fn init) es el valor inicial (0)
 * acc * 26 para que el valor anterior cambie de unidades a decenas, etc, antes de introducir el nuevo valor de unidades
 * .charCodeAt(0) devuelve el codigo ASCII del caracter
 * - 64 para que A sea 1, B sea 2, etc
 */

// Tests, descomenta solo el que necesites

/**
 * Node tests
 * por si usas node lts
 * requiere de `npm i -D typescript @types/node`
 * y de `npx tsc path/to/eliyya.ts && node path/to/eliyya.js`
 */
// import assert from 'node:assert';
// import test from "node:test"

// test('Correct tests', (t) => {
//     assert.strictEqual(excellColumnToNumber('A'), 1);
//     assert.strictEqual(excellColumnToNumber('Z'), 26);
//     assert.strictEqual(excellColumnToNumber('AA'), 27);
//     assert.strictEqual(excellColumnToNumber('AZ'), 52);
//     assert.strictEqual(excellColumnToNumber('BA'), 53);
//     assert.strictEqual(excellColumnToNumber('CA'), 79);
//     assert.strictEqual(excellColumnToNumber('ZA'), 677);
//     assert.strictEqual(excellColumnToNumber('ZZ'), 702);
//     assert.strictEqual(excellColumnToNumber('AAA'), 703);
// });
// test('Incorrect tests', (t) => {
//     assert.throws(() => { excellColumnToNumber(''); }, Error);
//     assert.throws(() => { excellColumnToNumber('1'); }, Error);
//     assert.throws(() => { excellColumnToNumber('a'); }, Error);
//     assert.throws(() => { excellColumnToNumber('A1'); }, Error);
// });

/**
 * Deno tests
 * requiere de `deno test path/to/eliyya.ts`
 */
// import { assertStrictEquals, assertThrows } from "https://deno.land/std@0.197.0/assert/mod.ts";

// Deno.test('Correct tests', () => {
//     assertStrictEquals(excellColumnToNumber('A'), 1);
//     assertStrictEquals(excellColumnToNumber('Z'), 26);
//     assertStrictEquals(excellColumnToNumber('AA'), 27);
//     assertStrictEquals(excellColumnToNumber('AZ'), 52);
//     assertStrictEquals(excellColumnToNumber('BA'), 53);
//     assertStrictEquals(excellColumnToNumber('CA'), 79);
//     assertStrictEquals(excellColumnToNumber('ZA'), 677);
//     assertStrictEquals(excellColumnToNumber('ZZ'), 702);
//     assertStrictEquals(excellColumnToNumber('AAA'), 703);
// });

// Deno.test('Incorrect tests', () => {
//     assertThrows(() => { excellColumnToNumber(''); }, Error);
//     assertThrows(() => { excellColumnToNumber('1'); }, Error);
//     assertThrows(() => { excellColumnToNumber('a'); }, Error);
//     assertThrows(() => { excellColumnToNumber('A1'); }, Error);
// });
