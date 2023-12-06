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

function corectaExprecion(expresion) {
  let comprobador1 = /(\s[+-/\*%]\s)/g;
  let comprobador2 = /-?\d+\.?\d*/g;
  let reduccion1 = expresion.replace(comprobador1, '');
  let reduccion2 = reduccion1.replace(comprobador2, '');
  if(!reduccion2) {
    console.log(true);
  } else {
    console.log(false);
  }
}

corectaExprecion('2 + 254 - -5.2 * 6 / 2 % 3'); /* true */
corectaExprecion('2 + 254 - -5.2 * 6 / 2 %3');  /* false */
corectaExprecion('2 + 254 - -5.2 a 6 / 2 % 3'); /* false */
