package Reto_09

private val allLetters = listOf<Char>(
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
)

fun main(args: Array<String>) {
    print("Introduzca una cadena de texto para saber si se trata de un heterograma, un isograma o un pangrama: ")
    val cadena = readln().toList()
    isHeterograma(cadena)
    isIsograma(cadena)
    isPangrama(cadena)
}

fun isHeterograma(cadena: List<Char>) {
    if (cadena.size != cadena.distinct().size) println("La cadena ${String(cadena.toCharArray())} no es un heterograma.")
    else println("¡La cadena ${String(cadena.toCharArray())} es un heterograma!")
}

fun isIsograma(cadena: List<Char>) {
    var isIsograma: Boolean

    // Get a key-value map where each key it's a character at the input chain and the value is the number of appearances of that character.
    val aparicionesCaracter =
        cadena
            .groupingBy { it }
            .eachCount()

    /* We get a list of all the values (number of appearances) and we compare how distinct they are.
     * It should be only 1 type of value for be an isograma.
     */
    isIsograma = aparicionesCaracter.values.distinct().count() == 1
    if (isIsograma) println("¡La cadena ${String(cadena.toCharArray())} es un isograma de grado ${aparicionesCaracter.values.distinct()}!")
    else println("La cadena ${String(cadena.toCharArray())} no es un isograma")

}

fun isPangrama(cadena: List<Char>) {
    if(cadena.containsAll(allLetters)) println("¡La cadena ${String(cadena.toCharArray())} es un pangrama!")
    else println("La cadena ${String(cadena.toCharArray())} no es un pangrama")
}