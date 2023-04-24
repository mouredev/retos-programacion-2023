import java.util.*

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */


/**
 * Translates a string to leet speak intermediate using a map
 */
fun leetSpeakTranslator(text: String):String {

    val leetDictionary = mapOf(
            "a" to "4",
            "b" to "I3",
            "c" to "[",
            "d" to ")",
            "e" to "3",
            "f" to "|=",
            "g" to "&",
            "h" to "#",
            "i" to "1",
            "j" to ",_|",
            "k" to ">|",
            "l" to "1",
            "m" to "/\\/\\",
            "n" to "^/",
            "o" to "0",
            "p" to "|*",
            "q" to "(_,)",
            "r" to "I2",
            "s" to "5",
            "t" to "7",
            "u" to "(_)",
            "v" to "\\/",
            "w" to "\\/\\/",
            "x" to "><",
            "y" to "j",
            "z" to "2",
            "0" to "o",
            "1" to "L",
            "2" to "R",
            "3" to "E",
            "4" to "A",
            "5" to "S",
            "6" to "b",
            "7" to "T",
            "8" to "B",
            "9" to "g"
    )

    var hackerText = ""
    text.forEach { char ->
        val replaceChar = leetDictionary.getOrDefault(char.toString().lowercase(Locale.getDefault()), char.toString()).let {
            hackerText += it
        }
    }
    return hackerText
}

/**
 * Test Cases
 */
println(leetSpeakTranslator("Feliz 2023!"))
println(leetSpeakTranslator("Yo soy la primavera que ha llegado\n" +
        "con un ramillete de violetas,\n" +
        "y soy el sol que ha salido hoy\n" +
        "para iluminar tus ojos de gitana.\n" +
        "\n" +
        "Soy el aire que te envuelve\n" +
        "y el agua que te baña,\n" +
        "y soy el fuego que te quema\n" +
        "en la hoguera del querer."))
