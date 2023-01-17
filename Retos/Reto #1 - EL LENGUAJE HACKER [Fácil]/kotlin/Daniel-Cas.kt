fun main() {
    val word: String = readln().lowercase()
    val dictionaryMap: Map<Char, String> = mapOf(
        'a' to "4",
        'b' to "|3",
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
        'r' to "|2",
        's' to "5",
        't' to "7",
        'u' to "(_)",
        'v' to "\\/",
        'w' to "\\/\\/",
        'x' to "><",
        'y' to "j",
        'z' to "2",
        ' ' to " "
    )
    var hackerWord = ""
    word.forEach { letter -> hackerWord += dictionaryMap[letter] }
    println(hackerWord)
}