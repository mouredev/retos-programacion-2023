fun main() {
    PasswordGenerator()
    PasswordGenerator(8, true)
    PasswordGenerator(16, false, true, true)
    PasswordGenerator(3)
    PasswordGenerator(21)
}

private fun PasswordGenerator(
        size: Int = 8,
        uppercase: Boolean = false,
        digit: Boolean = false,
        special: Boolean = false
) {
    var chars = "abcdefghijklmnopqrstuvwxyz"
    val upper = chars.uppercase()
    val numbers = "0123456789"
    val specialChars = "!@#$%^&*()_+"

    var password = ""

    if ((size < 8) or (size > 16)) {
        println("El tamaño de la clave tiene que estar entre 8 y 16 caracteres")
        return
    }

    if (uppercase) chars += upper

    if (digit) chars += numbers

    if (special) chars += specialChars

    for (i in 1..size) {
        password += chars.random()
    }

    println(password)
}