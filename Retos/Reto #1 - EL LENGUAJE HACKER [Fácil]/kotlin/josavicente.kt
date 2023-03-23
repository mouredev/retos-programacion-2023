fun main(args: Array<String>) {

    println("Introduce una palabra o frase: ")
    val input : String = (readLine()?:"").uppercase()
    val hackerLanguage = mapOf<String, String>(
        "A" to "4",
        "B" to "13",
        "C" to "[",
        "D" to ")",
        "E" to "3",
        "F" to "|=",
        "G" to "&",
        "H" to "#",
        "I" to "1",
        "J" to ",_|",
        "K" to ">|",
        "L" to "1",
        "M" to "/\\/\\",
        "N" to "ˆ/",
        "O" to "0",
        "P" to "|*",
        "Q" to "(_,)",
        "R" to "12",
        "S" to "5",
        "T" to "7",
        "U" to "(_)",
        "V" to "\\/",
        "W" to "\\/\\/",
        "X" to "><",
        "Y" to "j",
        "Z" to "2",
        " " to " ",
        "1" to "L",
        "2" to "R",
        "3" to "E",
        "4" to "A",
        "5" to "S",
        "6" to "b",
        "7" to "T",
        "8" to "B",
        "9" to "g",
        "0" to "o",
    )
    var result = ""
    for (i:Int in 0..input.length - 1) {
        println("Key es:  ${input[i].toString()} el valor es ${hackerLanguage[input[i].toString()]}")
        if (!hackerLanguage[input[i].toString()].isNullOrBlank()) {
            result += hackerLanguage[input[i].toString()]
        }
    }
    if (result.isNullOrBlank()) println("La palabra o frase no tiene traducción hacker")
        else println("La traducción es: $result")
}