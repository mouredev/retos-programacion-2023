package reto3

fun main() {
    println(passwordGenerator(PasswordParams()))
    println(passwordGenerator(PasswordParams(length = 10, capital = true,)))
    println(passwordGenerator(PasswordParams(length = 12, numbers = true,)))
    println(passwordGenerator(PasswordParams(length = 14, symbols = true)))
    println(passwordGenerator(PasswordParams(length = 16, capital = true, numbers = true, symbols = true)))
}

fun passwordGenerator(config: PasswordParams): String {
    //letras por defecto el abcedario
    val characters = ArrayList((97..122).map {
        Char(it)
    })

    if (config.capital) {
        addCapitalLetters(characters)
    }

    if (config.numbers) {
        addNumbersLetters(characters)
    }

    if (config.symbols) {
        addSymbolsLetters(characters)
    }

    var password = ""
    val final_length = when {
        config.length < 8 -> 8
        config.length > 16 -> 16
        else -> config.length
    }

    while (password.length < final_length) {
        password += characters.random()
    }

    return password
}

private fun addSymbolsLetters(characters: ArrayList<Char>) {
    characters.addAll((33..48).map {
        Char(it)
    })
    characters.addAll((58..65).map {
        Char(it)
    })
    characters.addAll((91..97).map {
        Char(it)
    })
}

private fun addNumbersLetters(characters: ArrayList<Char>) {
    characters.addAll((49..58).map {
        Char(it)
    })
}

private fun addCapitalLetters(characters: ArrayList<Char>) {
    characters.addAll((65..91).map {
        Char(it)
    })
}

data class PasswordParams(
    val length: Int = 8,
    val capital: Boolean = false,
    val numbers: Boolean = false,
    val symbols: Boolean = false
)
