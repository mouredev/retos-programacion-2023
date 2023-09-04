/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

fun main(args: Array<String>) {
    menu()
}

fun menu() {
    println("Ingresa el texto a transformar en lenguaje hacker")
    while (true) {
        val entrada: String? = readLine()
        if (entrada.isNullOrBlank()) {
            println("No has insertado valor")
        } else {

            val cadena = remplazaValores(entrada)
            println("Lenguaje natural: \n $entrada")
            println("Leet Speak cheat sheet: \n  $cadena")
            break
        }
    }
}

fun remplazaValores(cadena: String): String {
    var valores = ""
    for (caracter in cadena) {
        val caracterRemplazado = when (caracter) {
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
            'a' -> '4'
            'b' -> '8'
            'c' -> '('
            'd' -> "|)"
            'e' -> '3'
            'f' -> "|="
            'g' -> '6'
            'h' -> '#'
            'i' -> '1'
            'j' -> "_|"
            'k' -> "|<"
            'l' -> "|_"
            'm' -> "/\\/\\"
            'n' -> "|\\|"
            'o' -> '0'
            'p' -> "|D"
            'q' -> "(,)"
            'r' -> "|2"
            's' -> '5'
            't' -> '7'
            'u' -> "|_|"
            'v' -> "\\/"
            'w' -> "\\/\\/"
            'x' -> '×'
            'y' -> '%'
            'z' -> '2'
            else -> caracter
        }
        valores += caracterRemplazado
    }
    return valores
}