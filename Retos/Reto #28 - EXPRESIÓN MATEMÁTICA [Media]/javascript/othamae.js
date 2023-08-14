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

const checkExpression = (expression) => {
    const validOperators = ["+", "-", "*", "/", "%"]
    const expressionArray = expression.split(" ")
    if (expressionArray.length < 3)  return false
    for (const char of expressionArray) {
        if (!validOperators.includes(char) && (!/^([0-9])*$/.test(char))) {    
            return false
        }
    }
    return true
}


console.log(checkExpression("5 + 6 / 7 - 4")) //true
console.log(checkExpression("5 a 6")) //false
console.log(checkExpression("85 a 6")) //false
console.log(checkExpression("957 - 6")) //true
console.log(checkExpression("- 6 +5")) //false
console.log(checkExpression("83 -+ 6")) //false
console.log(checkExpression("597-6")) //false
console.log(checkExpression("95 - 66 + 7 / 2")) //true


