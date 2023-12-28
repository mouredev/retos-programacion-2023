fun main(args: Array<String>) {

    println(translateNaturalToHacker("Esto es una demostracion"))
    println(translateNaturalToHacker("Resolviendo el reto de Mouredev"))
    println(translateNaturalToHacker("leet"))
}

fun translateNaturalToHacker(phrase: String): String {
    val leetMapCodes = mapOf(
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

    return phrase.map {
        leetMapCodes.getOrElse(it.lowercase()[0]) { it }
    }.joinToString("")
}