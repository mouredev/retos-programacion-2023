/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / % 
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */

const regex = new RegExp('([-]?\\d+(,\\d+)?)(([ ][+|\\-|*|\\/|%][ ])([-]?\\d+(,\\d+)?))+', 'g');

const ejemploA = "5 + 6 / 7 - 4";
const ejemploB = "5 a 6";
const ejemploC = "-5 + 3,25 * -23,12 / 12 % 2 - 1 + 23";

const isExpresionMatematica = expresion => regex.test(expresion);

console.log(isExpresionMatematica(ejemploA));  //true
console.log(isExpresionMatematica(ejemploB));  //false
console.log(isExpresionMatematica(ejemploC));  //true

