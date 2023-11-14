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

function evaluate(expression) {
    if (typeof expression !== 'string') {
        return false;
    }

    const chars = expression.split(' ');
    const firstChar = chars[0];
    const lastChar = chars[chars.length - 1];
    if (!isValidNumber(firstChar) || !isValidNumber(lastChar)) {
        return false;
    }

    let prevIsOperator = false;
    for (const char of chars) {
        if (isValidNumber(char)) {
          prevIsOperator = false;
        } else if (isValidOperator(char)) {
            if (prevIsOperator) {
                return false;
            }
            prevIsOperator = true;
        } else {
            return false;
        }
    }
    return true;
}
  
function isValidNumber(input){
    const numberRegex = /^-?\d+(\.\d+)?$/;
    return numberRegex.test(input);
}

function isValidOperator(input){
    const operatorRegex = /^[+\-*\/%]$/;
    return operatorRegex.test(input);
}

// Test cases

console.log(evaluate("5 + 6 / 7 - 4"));                         // true
console.log(evaluate("5 a 6"));                                 // false
console.log(evaluate("10 * -2"));                               // true
console.log(evaluate("5.5 + 6.6 - 6.6 * 6.6 / 1.1 % 13.3"));    // true
console.log(evaluate("3.3 + 3.3.3"));                           // false (Invalid number with multiple decimal points)
console.log(evaluate("33.3 + 34.7 /"));                         // false (Incomplete expression)
console.log(evaluate("/ 3.3 + 4.4"));                           // false (Incomplete expression)
console.log(evaluate("5 * (6 - 4)"));                           // false (Unsupported characters)
console.log(evaluate("5 * + / 9"));                             // false (Multiple consecutive operators)
console.log(evaluate(""));                                      // false (Empty expression)
console.log(evaluate(123));                                     // false (Invalid input type)
console.log(evaluate(null));                                    // false (Invalid input type)