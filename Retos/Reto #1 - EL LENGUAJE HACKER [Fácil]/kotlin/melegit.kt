/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

fun main() {
    println("leet")
    println(hackerLanguage("leet"))
}

private fun hackerLanguage(text: String): String {
    return text.map {
        when (it) {
            'a', 'A' -> "4"
            'b', 'B' -> "I3"
            'c', 'C' -> "["
            'd', 'D' -> ")"
            'e', 'E' -> "3"
            'f', 'F' -> "|="
            'g', 'G' -> "&"
            'h', 'H' -> "#"
            'i', 'I' -> "1"
            'j', 'J' -> ",_|"
            'k', 'K' -> ">|"
            'l', 'L' -> "1"
            'm', 'M' -> "/\\/\\"
            'n', 'N' -> "^/"
            'o', 'O' -> "0"
            'p', 'P' -> "|*"
            'q', 'Q' -> "(_,)"
            'r', 'R' -> "I2"
            's', 'S' -> "5"
            't', 'T' -> "7"
            'u', 'U' -> "(_)"
            'v', 'V' -> "\\/"
            'w', 'W' -> "\\/\\/"
            'x', 'X' -> "><"
            'y', 'Y' -> "j"
            'z', 'Z' -> "2"
            '0' -> "o"
            '1' -> "L"
            '2' -> "R"
            '3' -> "E"
            '4' -> "A"
            '5' -> "S"
            '6' -> "b"
            '7' -> "T"
            '8' -> "B"
            '9' -> "g"
            else -> it
        }
    }.joinToString("")
}