
fun toLeet(words: String){
    
    println("Convirtiendo $words a leet")

    val alfabeto = "abcdefghijklmnñopqrstuvwxyz1234567890 "
    val leet = listOf("4", "I3", "[", ")", "3", "|=", "&", "#", "1", ",_|",
        ">|", "1", "/\\/\\", "^/", "^/", "0", "|*", "(_,)",  "I2", "5", "7", "(_)",
        "\\/", "\\/\\/", "><", "j", "2", "L", "R", "E", "A", "S", "b", "T", "B", "g", "o", " ")

    println(words.lowercase().map { c ->
        leet[alfabeto.indexOf(c)] }.joinToString (""))
}