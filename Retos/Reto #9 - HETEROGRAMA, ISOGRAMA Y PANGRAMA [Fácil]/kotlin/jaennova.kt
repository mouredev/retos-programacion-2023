fun esHeterograma(texto: String): Boolean {
    val letras = texto.filter { it.isLetter() }.toLowerCase().toSet()
    return letras.size == texto.length
}

fun esIsograma(texto: String): Boolean {
    val letras = texto.filter { it.isLetter() }.toLowerCase()
    return letras.length == letras.toSet().size
}

fun esPangrama(texto: String): Boolean {
    val letras = texto.filter { it.isLetter() }.toLowerCase().toSet()
    return letras.size == 26
}

fun main() {
    val texto = "El veloz murciélago hindú comía feliz cardillo y kiwi"
    println("¿Es '$texto' un heterograma? ${esHeterograma(texto)}")
    println("¿Es '$texto' un isograma? ${esIsograma(texto)}")
    println("¿Es '$texto' un pangrama? ${esPangrama(texto)}")
}
