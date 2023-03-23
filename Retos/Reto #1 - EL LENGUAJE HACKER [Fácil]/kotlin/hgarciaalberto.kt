
/**
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

object Reto1 {

    @JvmStatic
    fun main(args: Array<String>) {
        val text = "Esto es un mensaje de prueba en 2023"
        println(text)
        println(text.hackerText())
    }

    private fun String.hackerText(): String =
        this.lowercase().toCharArray().map {
            if (mapper.contains(it)) mapper[it] else it
        }.joinToString("")

    private val mapper = buildMap {
        put('a', "4")
        put('b', "I3")
        put('c', "[")
        put('d', ")")
        put('e', "3")
        put('f', "|=")
        put('g', "&")
        put('h', "#")
        put('i', "1")
        put('j', ",_|")
        put('k', ">|")
        put('l', "1")
        put('m', "/\\/\\")
        put('n', "^/")
        put('o', "0")
        put('p', "|*")
        put('q', "(_,)")
        put('r', "I2")
        put('s', "5")
        put('t', "7")
        put('u', "(_)")
        put('v', "\\/")
        put('w', "\\/\\/")
        put('x', "><")
        put('y', "j")
        put('z', "2")
        put('1', "L")
        put('2', "R")
        put('3', "E")
        put('4', "A")
        put('5', "S")
        put('6', "b")
        put('7', "T")
        put('8', "B")
        put('9', "g")
        put('0', "o")
    }
}
