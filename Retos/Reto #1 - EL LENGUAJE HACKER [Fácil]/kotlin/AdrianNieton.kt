import java.util.*

/**
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

object Translation {

    val pattern = Regex("[a-zA-Z0-9 ]+")

    val leetDictionary = mapOf(
        " " to " ",     "A" to "4",
        "B" to "I3",    "C" to "[",
        "D" to ")",     "E" to "3",
        "F" to "|=",    "G" to "&",
        "H" to "#",     "I" to "1",
        "J" to ",_|",   "K" to ">|",
        "L" to "1",     "M" to "/\\/\\",
        "N" to "^/",    "O" to "0",
        "P" to "|*",    "Q" to "(_,)",
        "R" to "I2",    "S" to "5",
        "T" to "7",     "U" to "(_)",
        "V" to "\\/",   "W" to "\\/\\/",
        "X" to "><",    "Y" to "j",
        "Z" to "2",     "0" to "A",
        "1" to "B",     "2" to "C",
        "3" to "D",     "4" to "E",
        "5" to "F",     "6" to "G",
        "7" to "H",     "8" to "I",
        "9" to "J")
}

fun main() {
    val scanner = Scanner(System.`in`)

    print("Introduce una cadena de texto alfanumérica: ")
    val input = scanner.nextLine()
    println(input.toLeet())
}

fun String.toLeet(): String {

    var result = ""

    if (this.matches(Translation.pattern)) {
        this.uppercase().forEach { result += Translation.leetDictionary[it.toString()] }
    }
    else {
        result = "String inválido"
    }

    return result
}