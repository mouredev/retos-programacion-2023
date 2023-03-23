import java.text.Normalizer

fun main() {
    testCase(word = "4", expected = "A")
    testCase(word = "hola", expected = "#014")
    testCase(word = "Algo más complejo", expected = "41&0 /\\/\\45 [0/\\/\\|*13,_|0")
}

fun testCase(word: String, expected: String) {
    val wordHack = hack(word = word)

    if (wordHack != expected) {
        throw Exception(
            "Case with the word: '$word', returns $wordHack but it should be $expected"
        )
    }

    println("Word: '${word}', word hacked '${wordHack}'")
}

fun hack(word: String): String {
    return word.clean()
        .replace("0", "o")
        .replace("1", "L")
        .replace("2", "R")
        .replace("3", "E")
        .replace("4", "A")
        .replace("5", "S")
        .replace("6", "b")
        .replace("7", "T")
        .replace("8", "B")
        .replace("9", "g")
        .replace("a", "4")
        .replace("b", "I3")
        .replace("c", "[")
        .replace("d", ")")
        .replace("e", "3")
        .replace("f", "|=")
        .replace("g", "&")
        .replace("h", "#")
        .replace("i", "1")
        .replace("j", ",_|")
        .replace("k", ">|")
        .replace("l", "1")
        .replace("m", "/\\/\\")
        .replace("n", "^/")
        .replace("o", "0")
        .replace("p", "|*")
        .replace("q", "(_,)")
        .replace("r", "I2")
        .replace("s", "5")
        .replace("t", "7")
        .replace("u", "(_)")
        .replace("v", "\\/")
        .replace("w", "\\/\\/")
        .replace("x", "><")
        .replace("y", "j")
        .replace("z", "2")
}

fun CharSequence.clean(): String {
    val regexUnAccent = "\\p{InCombiningDiacriticalMarks}+".toRegex()

    val temp = Normalizer.normalize(this, Normalizer.Form.NFD)
    return regexUnAccent.replace(temp.lowercase(), "")
}
