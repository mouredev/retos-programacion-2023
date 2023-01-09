
fun main() {
    println(leetTranslator("Leet"))
    println(leetTranslator("Aquí está un texto de prueba para ver si funciona el reto!"))
}

private fun leetTranslator(text: String): String {

    val leet = mapOf("A" to "4", "B" to "I3", "C" to "[", "D" to ")", "E" to "3", "F" to "|=",
        "G" to "&", "H" to "#", "I" to "1", "J" to ",_|", "K" to ">|", "L" to "1", "M" to "/\\/\\",
        "N" to "^/", "O" to "0", "P" to "|*", "Q" to "(_,)", "R" to "I2", "S" to "5", "T" to "7",
        "U" to "(_)", "V" to "\\/", "W" to "\\/\\/", "X" to "><", "Y" to "j", "Z" to "2",
        "1" to "L", "2" to "R", "3" to "E", "4" to "A", "5" to "S", "6" to "b", "7" to "T",
        "8" to "B", "9" to "g", "0" to "o")

    var leetText = ""

    for (word in text) {
        val character = word.toString().uppercase()
        leetText += if (leet.containsKey(character)) {
            leet[character]
        } else {
            word.toString()
        }
    }

    return leetText
}