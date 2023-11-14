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
 *
 * Algunos casos testeados:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 * "-10.2.1 * 10" -> false
 * "20.0 * -1.01" -> true
 * "1.000001 * / 1000" -> false
 * "*10 + 29" -> false
 * "/ 10" -> false
 * "-20 * 32 *" -> false
 * "30 *" -> false
 * "20 20" -> false
 */

private val operators = listOf("+", "-", "*", "/", "%")
private val separator = " "

fun main() {
    val expression = "5 + 6 / 7 - 4"
    val isValidExpression = mathExpression(expression)
    println("Expresion valida? $expression -> $isValidExpression")
}

fun mathExpression(input: String): Boolean {
    val splitExpression = input.split(separator)
    return if (splitExpression.count() > 2 &&
        !startsOrEndsWithOperator(splitExpression.first(), splitExpression.last())) {
        var previousOperator = ""
        var previousNumber = ""
        var isValidExpression = true
        splitExpression.forEach { expression ->
            if(expression.isNumber() && previousNumber.isEmpty()) {
                previousNumber = expression
                previousOperator = ""
                return@forEach
            }
            if (expression.isOperator() && previousOperator.isEmpty()) {
                previousOperator = expression
                previousNumber = ""
                return@forEach
            }
            isValidExpression = false
        }
        isValidExpression
    } else {
        false
    }
}

private fun startsOrEndsWithOperator(first: String, last: String): Boolean {
    return operators.contains(first) || operators.contains(last)
}

private fun String.isNumber(): Boolean {
    return try {
        this.toDouble()
        true
    } catch (e: NumberFormatException) {
        false
    }
}

private fun String.isOperator(): Boolean {
    return operators.contains(this)
}
