import kotlin.random.Random

fun generatePassword(longLength: Boolean = true, withUpperLetters: Boolean = true, withNumbers: Boolean = true, withSymbols: Boolean = true): String {
    val letters = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    val numbers = "0123456789"
    val symbols = "~`!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/"
    var eligibleCharacters = "${if(withUpperLetters) letters else ""}${if(withNumbers) numbers else ""}${if(withSymbols) symbols else ""}"
    var result = ""
    if(eligibleCharacters.isNotEmpty()) {
        for(i in 1..(if(longLength) 16 else 8)) {
            result = "$result${eligibleCharacters[Random.nextInt(0, eligibleCharacters.length - 1)]}"
        }
    }
    return result
}

fun main() {
    println(generatePassword())
    println(generatePassword(longLength = false, withNumbers = false, withSymbols = false))
    println(generatePassword(longLength = false, withUpperLetters = false, withSymbols = false))
    println(generatePassword(longLength = false, withUpperLetters = false, withNumbers = false))
    println(generatePassword(withUpperLetters = false, withNumbers = false, withSymbols = false))
}