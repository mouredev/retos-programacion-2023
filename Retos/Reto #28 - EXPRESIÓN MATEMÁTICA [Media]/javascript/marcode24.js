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

const isMathExpresion = (str) => {
  str = str.replace(/\s+/g, ' ').split(' ').join('');
  const regex = /^(\d+[\\+\-\\*\\/%]?)+\d+$/;
  return regex.test(str);
};

// Visita mi repo en GitHub para ver y correr los tests de este código --> https://github.com/marcode24/weekly-challenges
