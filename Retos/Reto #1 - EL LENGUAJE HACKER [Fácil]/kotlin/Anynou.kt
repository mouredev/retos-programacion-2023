fun main() {
    print("Enter text: ")

    val stringInput = readLine()!!
    translation(stringInput.lowercase())

}

fun translation(cadena: String) {

    val dictionary = mapOf(" " to " ", "a" to "4", "b" to "I3", "c" to "[", "d" to ")", "e" to "3",
                            "f" to "|=", "g" to "&", "h" to "#", "i" to "1", "j" to ",_|",
                            "k" to ">|", "l" to "1", "m" to "/\\/\\", "n" to "^/", "o" to "0",
                            "p" to "|*", "q" to "(_,)", "r" to "I2", "s" to "5", "t" to "7",
                            "u" to "(_)", "v" to "\\/", "w" to "\\/\\/", "x" to "><", "y" to "j",
                            "z" to "2", "1" to "L", "2" to "R", "3" to "E", "4" to "A", "5" to "S",
                            "6" to "b", "7" to "T", "8" to "B", "9" to "g", "0" to "o")

    var texto = ""

    for (c in cadena) {
        texto = texto + dictionary["$c"]

    }
    println(texto)
}
