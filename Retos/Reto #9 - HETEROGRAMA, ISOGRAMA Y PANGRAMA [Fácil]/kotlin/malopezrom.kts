import java.util.*
/*
 * Crea 3 funciones, cada una encargada de detectar si una cadena de
 * texto es un heterograma, un isograma o un pangrama.
 * - Debes buscar la definición de cada uno de estos términos.
 */

/**
 * Función principal
 */

fun main(){
    checkWord("Ecuador, cada quince de noviembre")
    checkWord("esdrújula")
    checkWord("aliento")
    checkWord("mama")
    checkWord("El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja")
    checkWord("Jovencillo emponzoñado de whisky, ¡qué figurota exhibe!")

}

/**
 * Funcione que comprueba si una palabra es un isograma, pangrama o heterograma
 */
fun checkWord(word: String) {
    var message = "La frase $word es: "
    val conditions = mutableListOf<String>()

    if(word.isHetereogram()) conditions.add("heterograma")
    if(word.isIsogram()) conditions.add("isograma")
    if(word.isPangram("abcdefghijklmnopqrstuvwxyz")) conditions.add("pangrama")


    message += if (conditions.isEmpty()) {
        "ni un isograma, ni un pangrama, ni un heterograma"
    } else {
        conditions.joinToString(", ") + "."
    }

    println(message)
}
/**
 * Funcion de extension de un string que limpia los acentos de una cadena de texto y
 * los sustituye por su equivalente sin acento
 */
fun String.cleanText(): String {
    val regExp = Regex("[áéíóúÁÉÍÓÚ]")
    val accents = mapOf(
            "á" to "a",
            "é" to "e",
            "í" to "i",
            "ó" to "o",
            "ú" to "u",
            "Á" to "A",
            "É" to "E",
            "Í" to "I",
            "Ó" to "O",
            "Ú" to "U"
    )

    return regExp.replace(this) {
        accents[it.value] ?: it.value
    }
}
/**
 * Funcion que detecta si una palabra es un heterograma con una expresion regular
 * Un Heterograma es una palabra que no tiene letras repetidas
 */
fun String.isHetereogram(): Boolean {
    val textLower = this.lowercase(Locale.getDefault()).cleanText().replace(Regex("[^a-z]"), "")
    val regExp = Regex("^(?!.*(.).*\\1)[a-zA-Z]+\$")
    return regExp.matches(textLower)
}
/**
 * Funcion que detecta si una palabra es un isograma.
 * Un isograma es una palabra en la que cada letra se repite exactamente el mismo numero de veces
 * Una palabra en la que cada letra se repite una sola vez es a su vez un heterograma.
 * Un palabra en la que cada letra se repite dos veces es un isograma de grado 2 y asi sucesivamente.
 */
fun String.isIsogram(): Boolean {
    val countLetters = mutableMapOf<Char, Int>()
    val textLower = this.toLowerCase().cleanText().replace(Regex("[^a-z]"), "")
    textLower.forEach { letter ->
        countLetters[letter] = countLetters.getOrDefault(letter, 0) + 1
    }
    return countLetters.values.toSet().size == 1
}

/**
 * Funcion que detecta si una palabra es un pangrama
 * Un Pangrama es una frase que contiene todas las letras del alfabeto
 */
fun String.isPangram(alphabet:String): Boolean {
    val textLower = this.lowercase(Locale.getDefault()).cleanText().replace(Regex("[^a-z]"), "")
    val regExp = Regex("[a-z]")
    val numberOfLetters = regExp.findAll(alphabet).count()
    val letters = regExp.findAll(textLower).map { it.value }.toSet()
    return letters.size == numberOfLetters
}

main()
