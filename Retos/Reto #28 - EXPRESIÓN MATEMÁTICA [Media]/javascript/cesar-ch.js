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


function isMathExpression(str) {
    const operations = ['+', '-', '*', '/', '%']
    const mathExpression = str.split(' ')
    if (mathExpression.length < 3 || mathExpression.length % 2 == 0) {
        return false
    }

    let isMathExpression = true
    mathExpression.map((e, i) => {
        if (!Number(e) && i % 2 == 0) {
            isMathExpression = false
        }
        
        if (!operations.includes(e) && i % 2 != 0) {
            isMathExpression = false
        }
    }
    )
    return isMathExpression

}

console.log(isMathExpression("3 + 5"))
console.log(isMathExpression("3 a 5"))
console.log(isMathExpression("-3 + 5"))
console.log(isMathExpression("- 3 + 5"))
console.log(isMathExpression("-3 a 5"))
console.log(isMathExpression("-3+5"))
console.log(isMathExpression("3 + 5 - 1 / 4 % 8"))