fun main() {
    testCase(length = 6)
    testCase(length = 7)
    testCase(length = 8)
    testCase(length = 5)
    testCase(length = 9)
}

fun testCase(length: Int) {
    val password = generatePassword(length = length)

    if (password.length != length) {
        println(
            "Case with the length: '$length', returns ${password.length} but it should be $length"
        )
        return
    }

    println("Password: '$password', the length '${password.length}'")
}

fun generatePassword(length: Int): String {
    if (length in 6..8) {

        val chars = ('0'..'9') + ('a'..'z') + ('A'..'Z') + '*' + ',' + '.' + '$' + '&' + '/'

        return List(length) { chars.random() }.joinToString("")
    }

    return String()
}