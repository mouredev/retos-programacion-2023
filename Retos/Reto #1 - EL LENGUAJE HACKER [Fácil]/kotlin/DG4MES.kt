val ltrs = mapOf(
        "A" to "4",
        "B" to "|3",
        "C" to "(",
        "D" to "|)",
        "E" to "3",
        "F" to "|=",
        "G" to "6",
        "H" to "#",
        "I" to "1",
        "J" to "_|",
        "K" to "|<",
        "L" to "|",
        "M" to "/\\/\\",
        "N" to "^/",
        "O" to "0",
        "P" to "|*",
        "Q" to "(_,)",
        "R" to "/2",
        "S" to "5",
        "T" to "7",
        "U" to "(_)",
        "V" to "\\/",
        "W" to "\\N",
        "X" to "><",
        "Y" to "`/",
        "Z" to "2",
        "0" to "o",
        "1" to "l",
        "2" to "Z",
        "3" to "E",
        "4" to "A",
        "5" to "S",
        "6" to "G",
        "7" to "T",
        "8" to "B",
        "9" to "g",
        " " to " "
)
fun textToHacker(text:String):String {
    var hacker = ""
    for(ltr in text.toUpperCase()){
        hacker += ltrs["$ltr"]
    }
    return hacker 
}
    
fun main(){
    val texto = "holanda"
    println(textToHacker(texto))
}