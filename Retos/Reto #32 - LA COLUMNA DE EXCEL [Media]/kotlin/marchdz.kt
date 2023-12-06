fun calculateColumnNumber(columnsAsString: String) {
    if (columnsAsString.isEmpty()) {
        println("La entrada está vacía.")
    } else if (!columnsAsString.all { character -> character.code in 65..90 }) {
        println("La entrada \"$columnsAsString\" es incorrecta. Solamente se admiten letras mayúsculas.")
    } else {
        val charsAsNumbers = columnsAsString.map { character -> character.code - 64 }
        val columnNumber = charsAsNumbers.reduce { accumulated, number -> accumulated * 26 + number }
        println("$columnsAsString = $columnNumber")
    }
}

fun main() {
    calculateColumnNumber("A")  // A = 1
    calculateColumnNumber("Z")  // Z = 26
    calculateColumnNumber("AA") // AA = 27
    calculateColumnNumber("CA") // CA = 79
    calculateColumnNumber("")   // La entrada está vacía.
    calculateColumnNumber("cA") // La entrada "cA" es incorrecta. Solamente se admiten letras mayúsculas.
    calculateColumnNumber("C4") // La entrada "C4" es incorrecta. Solamente se admiten letras mayúsculas.
}