fun main() {
    passwordGenerator(12)
    passwordGenerator(24)
    passwordGenerator(4)
}
fun passwordGenerator(length: Int) {
    var password = ""
    val character:List<Char> = ('a'..'z') + ('A'..'Z') + ('0'..'9') + ('!'..'?')
    val finalLength = if (length < 8) 8 else if (length > 16) 16 else length

    while (password.length < finalLength){
        password += character.random().toChar()
    }
    println(password)
}