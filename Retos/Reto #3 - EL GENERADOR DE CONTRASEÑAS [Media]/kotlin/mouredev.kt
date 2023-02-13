fun main() {
    println(passwordGenerator())
    println(passwordGenerator(length = 16))
    println(passwordGenerator(length = 1))
    println(passwordGenerator(length = 22))
    println(passwordGenerator(length = 12, capital = true))
    println(passwordGenerator(length = 12, capital = true, numbers = true))
    println(passwordGenerator(length = 12, capital = true, numbers = true, symbols = true))
    println(passwordGenerator(length = 12, capital = true, symbols = true))
}

private fun passwordGenerator(
        length: Int = 8,
        capital: Boolean = false,
        numbers: Boolean = false,
        symbols: Boolean = false
): String {

    // Fuente: https://www.ascii-code.com

    val characters = (97..122).toMutableList()

    if (capital) {
        characters += (65..90).toList()
    }

    if (numbers) {
        characters += (48..57).toList()
    }

    if (symbols) {
        characters += (33..47).toList() + (58..64).toList() + (91..96).toList()
    }

    var password = ""

    val finalLength = if (length < 8) 8 else if (length > 16) 16 else length

    while (password.length < finalLength) {
        password += characters.random().toChar()
    }

    return password
}
