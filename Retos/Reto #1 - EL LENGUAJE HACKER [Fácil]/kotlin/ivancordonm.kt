private fun main() {
    val leetAlphabet = mapOf(
        'a' to "4",
        'b' to "13",
        'c' to "[",
        'd' to ")",
        'e' to "3",
        'f' to "|=",
        'g' to "&",
        'h' to "#",
        'i' to "1",
        'j' to ",_|",
        'k' to ">|",
        'l' to "1",
        'm' to "/\\/\\",
        'n' to "^/",
        'o' to "0",
        'p' to "|*",
        'q' to "(_,)",
        'r' to "12",
        's' to "5",
        't' to "7",
        'u' to "(_)",
        'v' to "\\/",
        'w' to "\\/\\/",
        'x' to "><",
        'y' to "j",
        'z' to "2"
    )

    fun String.toLeet() = map { leetAlphabet.getOrElse(it.lowercaseChar()) {it} }.joinToString("")

    println("Esto es una prueba".toLeet())
    println("hacker".toLeet())
    println("waka waka".toLeet())

}
