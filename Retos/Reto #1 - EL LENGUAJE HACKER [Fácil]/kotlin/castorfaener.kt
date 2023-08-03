/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *
 */

fun main(){

    val alphabet: List<Char> = listOf(' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9')
    val hackerAlphabet = listOf(" ","4","I3","[",")","3","|=","&", "#", "1", ",_|", ">|", "1", "[V]","^/", "0", "|*", "(_,)", "12", "5", "7", "(_)", "|/", "'//", "><", "j", "2", "o", "L", "R", "E", "A", "S", "b", "T", "B", "g")

    println("Introduce un texto:")
    val textToTranslate = readLine()?.lowercase()
    var translatedText = ""

    textToTranslate?.map {
        val index = alphabet.indexOf(it)
        translatedText += hackerAlphabet[index]
    }
    println(translatedText)
}