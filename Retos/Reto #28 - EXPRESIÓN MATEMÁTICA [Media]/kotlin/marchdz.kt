fun validateMathExpression(mathExpression: String) {
    val regex = """^-?\d+(\.\d+)?\s[+\-*/%]\s-?\d+(\.\d+)?(\s[+\-*/%]\s-?\d+(\.\d+)?)*$""".toRegex()
    println("$mathExpression -> ${regex.matches(mathExpression)}")
}

fun main() {
    validateMathExpression("5 + 6 / 7 - 4")         // true
    validateMathExpression("5 a 6")                 // false
    validateMathExpression("5 + 600.06 / 70 - 4.4") // true
    validateMathExpression("5 + 6 /7 - 4")          // false
    validateMathExpression("5 +")                   // false
    validateMathExpression("5 + 600.06 / 70 - ")    // false
}