import java.text.Normalizer

private val REGEX_UNACCENTED = "\\p{InCombiningDiacriticalMarks}+".toRegex()

fun CharSequence.unaccented(): String {
    val temp = Normalizer.normalize(this, Normalizer.Form.NFD)
    return REGEX_UNACCENTED.replace(temp, "")
}
private fun isHeterogram(text: String): Boolean {
    val occurrencesMap = mutableMapOf<Char, Int>()
    for(character in text) {
        occurrencesMap.putIfAbsent(character, 0)
        occurrencesMap[character] = occurrencesMap[character]!! + 1
    }
    return occurrencesMap.values.minOf { it } == occurrencesMap.values.maxOf { it } && occurrencesMap.values.first() == 1
}

private fun isIsogram(text: String): Boolean {
    val occurrencesMap = mutableMapOf<Char, Int>()
    for(character in text) {
        occurrencesMap.putIfAbsent(character, 0)
        occurrencesMap[character] = occurrencesMap[character]!! + 1
    }
    return occurrencesMap.values.minOf { it } == occurrencesMap.values.maxOf { it } && occurrencesMap.values.first() > 1
}

private fun isPangram(text: String): Boolean {
    val alphabet = "abcdefghijklmnopqrstuvwxyz"
    val occurrencesMap = mutableMapOf<Char, Int>()
    alphabet.forEach { letter ->
        occurrencesMap[letter] = 0
    }
    for(character in text) {
        occurrencesMap[character] = occurrencesMap[character]!! + 1
    }
    return occurrencesMap.values.minOf { it } > 0
}

private fun isHeterogramIsogramOrPangram(text: String) {
    val cleanedText = text.lowercase().unaccented().replace("[^a-z]".toRegex(), "")
    println("'$text' ${if(isHeterogram(cleanedText)) "" else "no "}es histograma, ${if(isIsogram(cleanedText)) "" else "no "}es isograma y ${if(isPangram(cleanedText)) "" else "no "}es pangrama.")
}

fun main() {
    isHeterogramIsogramOrPangram("ventrilocuas")
    isHeterogramIsogramOrPangram("hiperblanduzcos")
    isHeterogramIsogramOrPangram("bilabial")
    isHeterogramIsogramOrPangram("Caucasus")
    isHeterogramIsogramOrPangram("Jovencillo emponzoñado de whisky, ¡qué figurota exhibe!")
    isHeterogramIsogramOrPangram("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú.")
}