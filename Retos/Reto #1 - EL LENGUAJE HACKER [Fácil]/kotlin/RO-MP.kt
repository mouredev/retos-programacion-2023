

fun main(){
    val text = "Hola mundo. Con cariño: Rodrigo (RO-MP)"

    println("\nTu texto: $text \n" +
            "Tu texto en leet: ${naturalToLeet(text)}")
}

fun naturalToLeet(text: String): String {
    var leet = ""
    for (letter in text){
        leet = leet.plus(leetMap.get(letter.toUpperCase().toString())?:letter)
    }

    return leet
}

val leetMap: Map<String, String> = mapOf(
    "A" to "4",
    "B" to "I3",
    "C" to "[",
    "D" to ")",
    "E" to "3",
    "F" to "|=",
    "G" to "&",
    "H" to "#",
    "I" to "1",
    "J" to ",_|",
    "K" to ">|",
    "L" to "7",
    "M" to "/\\/\\",
    "N" to "^/",
    "O" to "0",
    "P" to "|*",
    "Q" to "(_,)",
    "R" to "|2",
    "S" to "5",
    "T" to "7",
    "U" to "(_)",
    "V" to "\\/",
    "W" to "\\/\\/",
    "X" to "><",
    "Y" to "`/",
    "Z" to "2",
    " " to " ",
    "\n" to " \n"
)