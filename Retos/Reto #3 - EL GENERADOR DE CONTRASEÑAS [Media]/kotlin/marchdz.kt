import kotlin.random.Random

fun passwordGenerator(
    passwordLength: Int,
    addUpperCase: Boolean = false,
    addNumbers: Boolean = false,
    addSymbols: Boolean = false,
) {
    var charsToUse = "abcdefghijklmnopqrstuvwxyz"
    val upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val numbers = "0123456789"
    val symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    var password = ""

    if (addUpperCase) charsToUse += upperCase
    if (addNumbers) charsToUse += numbers
    if (addSymbols) charsToUse += symbols

    val passwordLengthWithinRange = when {
        passwordLength < 8 -> 8
        passwordLength > 16 -> 16
        else -> passwordLength
    }

    for (position in 1..passwordLengthWithinRange) {
        password += charsToUse[Random.nextInt(0, charsToUse.length)]
    }

    println(password)
}

fun main() {
    passwordGenerator(12, true, true, true)
    passwordGenerator(18, false, true, false)
    passwordGenerator(6)
}