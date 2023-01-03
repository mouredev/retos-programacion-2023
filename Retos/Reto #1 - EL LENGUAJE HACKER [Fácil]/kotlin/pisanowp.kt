fun main(){

    /*
     * Reto #1 02/01/2023
     *  Escribe un programa que reciba un texto y transforme lenguaje natural a
     *  "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
     *  se caracteriza por sustituir caracteres alfanuméricos.
     *  Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
     *  con el alfabeto y los números en "leet".
     *  (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
     */

    val texto = "Esta va a ser mi Oración"
    println(texto)
    println(texto.leetCode())
}

fun String.leetCode(): String{

    val leet = mapOf(
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
        "ñ" to "^/",
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
        "z" to "2"
    )

    var dummy = ""
    (0..this.length-1 ).forEach { i ->
        dummy +=  leet.get(this[i].lowercase()) ?: this[i]
    }
    return dummy

}