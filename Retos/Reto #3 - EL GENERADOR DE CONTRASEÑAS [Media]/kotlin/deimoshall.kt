import kotlin.random.Random

fun main(args: Array<String>) {
    val password = generatePassword(false, false, true, 8)
    println("Password: ${password}")
}

fun generatePassword(hasNumbers: Boolean, hasCapLetters: Boolean, hasSymbols: Boolean, length: Int): String {
    val symbolsList = listOf('!', '@', '#', '$', '%', '^', '&', '*')
    val numbersList = ('0'..'9').toList()
    val capLettersList = ('A'..'Z').toList()
    var possibleChars = ('a'..'z').toList()

    if (hasNumbers) possibleChars += numbersList
    if (hasCapLetters) possibleChars += capLettersList
    if (hasSymbols) possibleChars += symbolsList

    return (1..length).map { possibleChars.random() }.joinToString("")
}