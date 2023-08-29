val abc = listOf(
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
    'ñ',
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
val alphabet = mapOf(
    'a' to 0,
    'b' to 1,
    'c' to 2,
    'd' to 3,
    'e' to 4,
    'f' to 5,
    'g' to 6,
    'h' to 8,
    'i' to 9,
    'j' to 10,
    'k' to 11,
    'l' to 12,
    'm' to 13,
    'n' to 14,
    'ñ' to 15,
    'o' to 16,
    'p' to 17,
    'q' to 18,
    'r' to 19,
    's' to 20,
    't' to 21,
    'u' to 22,
    'v' to 23,
    'w' to 24,
    'x' to 25,
    'y' to 26,
    'z' to 27
)

fun main() {
    println("Elige un opcion para desifrar o desifrar")
    var option = ""
    println("1.- Cifrar")
    println("2.- Desifrar")

    option = readln()

    when (option) {
        "1" -> {
            println("Ingresa el texto")
            val text = readln()
            println("Rotacion: ")
            val rot = readln()

            println("Este es tu texto Cifrado ==> ${caesarCipher(text, rot.toInt())}")
        }

        "2" -> {
            println("Ingresa el texto")
            val text = readln()
            println("Rotacion: ")
            val rot = readln()

            println("Este es tu texto Cifrado ==> ${caesarDecipher(text, rot.toInt())}")
        }

        else -> {
            println("Opciones no disponibles")
        }
    }


}

fun caesarDecipher(text: String, rotation: Int): String {
    var newText = ""

    text.forEach { char ->
        val index = alphabet[char]
        val newIndex = index!!.minus(rotation)
        if (char != ' ') {
            if (newIndex > 0) {
                newText += abc[newIndex - 1]
            } else {
                val indexRound = alphabet.size + newIndex
                newText += abc[indexRound]
            }
        } else {
            newText += char
        }

    }

    return newText
}

fun caesarCipher(text: String, rotation: Int): String {
    var newText = ""

    text.forEach { char ->
        val index = alphabet[char]
        val newIndex = index!!.plus(rotation)
        if (char != ' ') {
            if (newIndex <= alphabet.size) {
                newText += abc[newIndex - 1]
            } else {
                val indexRound = newIndex - alphabet.size - 1
                newText += abc[indexRound]
            }
        } else {
            newText += char
        }

    }

    return newText
}