fun main() {
    println(passwordGenerator(length = 4))
    println(passwordGenerator(length = 8, capital = true))
    println(passwordGenerator(length = 16, capital = true, number = true))
    println(passwordGenerator(length = 32, capital = true, number = true, symbol = true))
}

fun passwordGenerator(length: Int = 8, capital: Boolean = false, number: Boolean = false, symbol: Boolean = false): String {
    var password = ""
    val asciiCodes = (97..122).toMutableList()

    if (capital) asciiCodes += (65..90)
    if (number) asciiCodes += (48..57)
    if (symbol) asciiCodes += (33..47)

    val finalLength = when {
        length < 8 -> 8
        length > 16 -> 16
        else -> length.toByte()
    }

    for (i in 0..< finalLength) {
        password += asciiCodes.random().toChar()
    }

    return password
}