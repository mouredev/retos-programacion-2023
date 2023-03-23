import java.text.Normalizer

private val REGEX_UNACCENTED = "\\p{InCombiningDiacriticalMarks}+".toRegex()

fun CharSequence.unaccented(): String {
    val temp = Normalizer.normalize(this, Normalizer.Form.NFD)
    return REGEX_UNACCENTED.replace(temp, "")
}

fun transleet(text: String): String {
    val leetAlphabet = mapOf('A' to "4", 'B' to "I3", 'C' to "[", 'D' to ")", 'E' to "3", 'F' to "|=", 'G' to "6", 'H' to "#", 'I' to "1", 'J' to ",_|", 'K' to ">|", 'L' to "1",
        'M' to "/\\/\\", 'N' to "^/", 'O' to "0", 'P' to "|*", 'Q' to "(_,)", 'R' to "I2", 'S' to "5", 'T' to "7", 'U' to "(_)", 'V' to "\\/", 'W' to "\\/\\/", 'X' to "><", 'Y' to "j", 'Z' to "2",
        '1' to "L", '2' to "R", '3' to "E", '4' to "A", '5' to "S", '6' to "b", '7' to "T", '8' to "B", '9' to "g", '0' to "o")
    val cleanedText = text.unaccented().uppercase()
    var result = ""

    cleanedText.forEach { char ->
        result += if(leetAlphabet.keys.contains(char)) {
            leetAlphabet[char]
        } else {
            char
        }
    }

    return result
}

fun main() {
    println(transleet("¿Estás mirándolo?"))   // ¿357á5 /\/\1I2á|\||)010?
    println(transleet("Mira cómo escribo leet, ¿tú lo puedes hacer así de bien?"))   // /\/\1I24 [ó/\/\0 35[I21I30 1337, ¿7ú 10 |>(_)3|)35 #4[3I2 45í |)3 I313|\|?
    println(transleet("Esto es la Wikipedia, la enciclopedia libre"))   // 3570 35 14 \/\/1|<1|>3|)14, 14 3|\|[1[10|>3|)14 11I3I23
    println(transleet("Esto es Leet Speak, ¿sabes hacerlo?"))   // 3570 35 1337 5|>34|<, ¿54I335 #4[3I210?
    println(transleet("Puedes usar algunas letras si te resulta demasiado difícil"))    // |>(_)3|)35 (_)54I2 416(_)|\|45 137I245 51 73 I235(_)174 |)3/\/\4514|)0 |)1phí[11
}