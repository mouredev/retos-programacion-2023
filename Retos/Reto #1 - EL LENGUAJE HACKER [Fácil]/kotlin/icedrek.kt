/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

fun main() {
    val inputList = listOf(
        "Hola Mundo",
        "MoureDev",
        "El cielo esta enladrillado"
    )

    inputList.forEach { input -> println("$input - ${input.toLeet()}") }
}

fun String.toLeet(): String {
    val leetMap = mapOf(
        'a' to "4",
        'b' to "13",
        'c' to "[",
        'd' to ")",
        'e' to "3",
        'f' to "|=",
        'g' to "&",
        'h' to "#",
        'i' to "!",
        'j' to ",_|",
        'k' to ">|",
        'l' to "1",
        'm' to "/\\/\\",
        'n' to "^/",
        'o' to "0",
        'p' to "|*",
        'q' to "(_,)",
        'r' to "I2",
        's' to "5",
        't' to "7",
        'u' to "(_)",
        'v' to "\\/",
        'w' to "\\/\\/",
        'x' to "><",
        'y' to "j",
        'z' to "2",
        '1' to "L",
        '2' to "R",
        '3' to "E",
        '4' to "A",
        '5' to "S",
        '6' to "b",
        '7' to "T",
        '8' to "B",
        '9' to "g",
        '0' to "o"
    )

    val input = this.lowercase()
    var output = ""

    for (letter in input) {
        if (leetMap[letter].isNullOrEmpty()) output += letter
        else output += leetMap[letter]
    }

    return output
}
