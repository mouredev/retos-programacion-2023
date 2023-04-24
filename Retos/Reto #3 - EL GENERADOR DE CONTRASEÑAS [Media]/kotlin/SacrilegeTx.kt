import java.util.*

fun main() {
    val passwordLength = 8
    val includeUpperCase = false
    val includeNumbers = true
    val includeSymbols = true

    val password = generateRandomPassword(passwordLength, includeUpperCase, includeNumbers, includeSymbols)
    println("Generated password: $password")
}

fun generateRandomPassword(length: Int, upperCase: Boolean, numbers: Boolean, symbols: Boolean): String {
    val charList = mutableListOf<Char>()
    val random = Random()

    if (upperCase) {
        charList.addAll('A'..'Z')
    }
    if (numbers) {
        charList.addAll('0'..'9')
    }
    if (symbols) {
        charList.addAll(listOf('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', '"', '\'', '<', '>', ',', '.', '?', '/'))
    }
    if (charList.isEmpty()) {
        charList.addAll('a'..'z')
    }

    return (1..length)
        .map { charList[random.nextInt(charList.size)] }
        .joinToString("")
}
