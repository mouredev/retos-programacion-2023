fun analyzeText(text: String) {
    val sentenceCount = text.split(".", ":", ";", "!", "?")
        .filter { it.isNotBlank() }.size
    val words = text.split(" ").filter { it.isNotBlank() }.toMutableList()
    val wordsCount = words.size

    for ((index, word) in words.withIndex()) {
        words[index] = word.replace(Regex("[,.:;!¡¿?]"), "")
    }

    val wordsAverageLength = if (wordsCount > 0) words.sumOf(String::length) / wordsCount else 0
    val longestWord = if (words.isNotEmpty()) words.maxBy(String::length) else ""

    println("""
        =======================================
        Número total de palabras: $wordsCount
        Longitud media de las palabras: $wordsAverageLength
        Número de oraciones del texto: $sentenceCount
        Palabra más larga: $longestWord
        =======================================
        """.trimIndent())
}

fun main() {
    analyzeText("Esto es una prueba; siempre hay que probar. ¿Ha funcionado? ¡Seguro!")
    analyzeText("t")
    analyzeText("")
}