fun t9ToText(input: String) {

    val t9Map = mapOf(
        "2" to 'A', "22" to 'B', "222" to 'C', "3" to 'D', "33" to 'E', "333" to 'F', "4" to 'G', "44" to 'H',
        "444" to 'I', "5" to 'J', "55" to 'K', "555" to 'L', "6" to 'M', "66" to 'N', "666" to 'O', "7" to 'P',
        "77" to 'Q', "777" to 'R', "7777" to 'S', "8" to 'T', "88" to 'U', "888" to 'V', "9" to 'W', "99" to 'X',
        "999" to 'Y', "9999" to 'Z', "0" to " "
    )

    val output = input.split("-").mapNotNull { t9Map[it] }.joinToString("")

    println(output)
}

fun main() {
    t9ToText("6-666-88-777-33-3-33-888")                        // MOUREDEV
    t9ToText("333-88-66-222-444-666-66-2-0-666-55")             // FUNCIONA OK
    t9ToText("H2O-333-88-66-222-88888-444-666-66-2-0-666-55-1") // FUNCIONA OK
}
