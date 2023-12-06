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


function checkExpression(expression) {
    const operators = ['+', '-', '*', '/', '%'];
    const expressionArray = expression.trim().split(/\s+/);


    // if no 3 elements -> NOK

    if (expressionArray.length < 3) {
        console.log('There must be at least 3 elements in the expression.');
        return false;
    }


    // if no operators at all -> NOK

    if (!operators.some(operator => expression.includes(operator))) {
        console.log('There are no operators in this expression.');
        return false;
    }


    // if expression starts or ends with operator -> NOK
    // * expression can start with '-' or '+'

    if (
        operators.includes(expressionArray[0]) && expressionArray[0] !== '-' && expressionArray[0] !== '+' ||
        operators.includes(expressionArray[expressionArray.length - 1])
    ) {
        console.log(
            'Expressions can not start with operators (except "-" or "+").\nExpressions can not end with operators.'
        );
        return false;
    }


    // check operators between numbers
    
    let lastElement;
    
    for (let element of expressionArray) {
        // if two operators together (no space between them) -> NOK
        if (element.length > 1 && !/^\d+$/.test(element)) {
            console.log('This expression has more than one operator without spacing.');
            return false;
        }

        // if no operators between numbers -> NOK
        if (/^\d+$/.test(lastElement) && /^\d+$/.test(element)) {
            console.log('Missing operator between numbers.');
            return false;
        }

        // if two operators between numbers -> NOK
        if (
            operators.includes(lastElement) && operators.includes(element) &&
            element !== '-'    // allowed for the number sign
        ) {
            console.log('Missing number between operators.');
            return false;
        }

        // if not allowed operator -> NOK
        if (/(?!-|\+|\/|%|\*)[\W]/.test(element)) {
            console.log('There is a not allowed operator in this expression.');
            return false;
        }

        lastElement = element;
    }


    // if no errors -> OK

    return true;
}


console.log(checkExpression('5 + 6 / 7 - 4'));      // true
console.log(checkExpression('a + b / c - d'));      // true -> letters can be considered numbers
console.log(checkExpression('5 / - 6'));            // true -> '-' operator allowed after another operator (number sign)

console.log(checkExpression('5 a 6'));              // false -> no operators
console.log(checkExpression('+ 5 - 6 8'));          // false -> missing operator between numbers
console.log(checkExpression('+ 5 - 6 / % 8'));      // false -> missing number between operators
console.log(checkExpression('5 & - 6'));            // false -> not allowed operator