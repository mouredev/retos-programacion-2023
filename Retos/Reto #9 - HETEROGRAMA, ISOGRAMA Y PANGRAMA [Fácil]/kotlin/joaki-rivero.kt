fun main() {
    println(evaluateText("quiere la boca exhausta vid, kiwi, piña y fugaz jamón"))
    println(evaluateText("salero"))
    println(evaluateText("aaabbb"))
    println(evaluateText("marmota"))
}

fun evaluateText(text: String): String {
    val textFormatted = text.filterNot { it.isWhitespace() }.trim().lowercase()

    val isHeterogram = isHeterogram(textFormatted)
    val isIsogram = isIsogram(textFormatted)
    val isPangram = isPangram(textFormatted)

    if (!isHeterogram && !isIsogram && !isPangram) {
        return "No es ni heterograma, isograma ni pangrama."
    }

    var result = ""

    if (isHeterogram) result += "Es heterograma. "
    if (isIsogram) result += "Es isograma. "
    if (isPangram) result += "Es pangrama."

    return result
}

fun isHeterogram(text: String): Boolean {
    return text.length == text.toSet().size
}

fun isIsogram(text: String): Boolean {
    var isIsogram = true
    val characters = mutableMapOf<Char, Int>()

    text.forEach { char ->
        if (!characters.containsKey(char)) {
            characters[char] = 1
        } else {
            characters[char] = characters[char]!! + 1
        }
    }

    val numberOfChars = characters.entries.first().value

    characters.forEach { (char, _) ->
        if (characters[char] != numberOfChars) {
            isIsogram = false
            return@forEach
        }
    }

    return isIsogram
}

fun isPangram(text: String): Boolean {
    val characters = mutableSetOf<Char>()

    text.forEach { char ->
        characters.add(char)
    }

    return characters.size > 14
}