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



function mathCheck(expression) {
  if (typeof expression !== "string") {
    return false;
  }

  const expressionElements = expression.trim().split(" ");
  const numbers = expressionElements.filter((_, index) => index % 2 === 0);
  const symbols = expressionElements.filter((_, index) => index % 2 !== 0);
  const allSymbols = ["+", "-", "*", "/", "%"];

  const areNumbers = numbers.every((e) => !isNaN(e));
  const areSymbols = symbols.every((e) => allSymbols.includes(e));

  const endsWithSymbol = symbols.includes(
    expressionElements[expressionElements.length - 1]
  );

  return areNumbers && areSymbols && !endsWithSymbol;
}




console.log(mathCheck("2 + 4 - 3 - 2 / 2 * 7")); // true
console.log(mathCheck("2 + 4 - 3 - 2 / 2 7")); // false
console.log(mathCheck("5.25 + 10 / 3")); // true
console.log(mathCheck("8 - 2 / 2 * 4 +")); // false
