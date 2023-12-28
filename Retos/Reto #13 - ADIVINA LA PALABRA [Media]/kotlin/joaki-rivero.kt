fun main() {
    wordGame()
}

const val MAX_INTENTS = 5
val words = listOf("alameda", "alabarda", "balada", "billar", "cacharro", "cocinero")

private fun wordGame() {
    var intents = MAX_INTENTS
    val wordResult = words.random()
    val charactersResult = wordResult.toCharArray()
    val characters = charactersResult.toMutableList()
    var isWinner = false

    val percent = (characters.size * 0.6).toInt()
    var charactersToHide = percent

    do {
        val index = (characters.indices).random()

        if (characters[index] != '_') {
            characters[index] = '_'
            charactersToHide--
        }
    } while (charactersToHide > 0)

    println("--- Adivina la palabra ---\n")

    while (intents > 0) {
        println("Intentos restantes: $intents")
        println(characters)
        print("Respuesta: ")

        val word = readln().lowercase()

        if (word.length > characters.size) {
            println("Palabra demasiado larga")
            intents--

        } else if (word.length < characters.size && word.length != 1) {
            println("Palabra demasiado corta")
            intents--

        } else if (word.length == 1) {
            if (charactersResult.contains(word.toCharArray()[0])) {
                charactersResult.forEachIndexed { index, resultChar ->
                    if (word.toCharArray()[0] == resultChar && characters[index] == '_') {
                        characters[index] = resultChar
                    }
                }

            } else {
                intents--
            }

        } else {
            if (word == wordResult) {
                isWinner = true
                break

            } else {
                intents--
            }
        }
        println()

        isWinner = !characters.contains('_')
        if (!characters.contains('_')) break
    }

    if (isWinner) {
        println("\nSolución: $wordResult")
        println("\n--- ¡Has ganado! ---")

    } else {
        println("Solución: $wordResult")
        println("\n--- Has perdido ---")
    }
}