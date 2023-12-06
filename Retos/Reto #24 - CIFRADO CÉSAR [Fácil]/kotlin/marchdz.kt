fun caesarCipher(positionsToShift: Int, text: String) {
    val lowerCase = "abcdefghijklmnopqrstuvwxyz"
    val upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    var textToPrint = ""

    for (character in text) {
        textToPrint += when {
            character.isLowerCase() -> lowerCase[(lowerCase.indexOf(character) + (positionsToShift % 26) + 26) % 26]
            character.isUpperCase() -> upperCase[(upperCase.indexOf(character) + (positionsToShift % 26) + 26) % 26]
            else -> character
        }
    }
    println(textToPrint)
}

fun caesarDecipher(positionsToShift: Int, text: String) {
    caesarCipher(-positionsToShift, text)
}

fun main() {
    caesarCipher(35, "Probando el programa")
    caesarDecipher(35, "Yaxkjwmx nu yaxpajvj")
}