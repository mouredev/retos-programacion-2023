/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

fun main() {
    generatePassword()
    generatePassword(length = 10, withCapitalLetters = false)
    generatePassword(length = 13, withNumbers = false, withSymbols = false)
    generatePassword(16, withCapitalLetters = true, withNumbers = false, withSymbols = true)
    generatePassword(length = 25)
}

fun generatePassword(
    length: Int = 8,
    withCapitalLetters: Boolean = true,
    withNumbers: Boolean = true,
    withSymbols: Boolean = true
) {

    val symbols = "!@#$%&*"
    val types = mutableListOf(Type.Letters)
    var result = ""

    if (withCapitalLetters) types.add(Type.CapitalLetters)
    if (withNumbers) types.add(Type.Numbers)
    if (withSymbols) types.add(Type.Symbols)

    if (length < 8 || length > 16) {
        println("Longitud incorrecta.")
        return
    }

    for (i in 1..length) {
        when (types.random()) {
            Type.Letters -> result += ('a'..'z').random()
            Type.CapitalLetters -> result += ('A'..'Z').random()
            Type.Numbers -> result += (0..9).random()
            Type.Symbols -> result += symbols.random()
        }
    }

    println("Contraseña: $result")
}

enum class Type {
    Letters, CapitalLetters, Numbers, Symbols
}