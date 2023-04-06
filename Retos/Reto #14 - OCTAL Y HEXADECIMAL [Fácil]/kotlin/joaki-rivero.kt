fun main() {
    octalAndHexadecimal(500)
    octalAndHexadecimal(95)
}

fun octalAndHexadecimal(num: Int) {

    var octal = ""
    var hexadecimal = ""
    var resultOctal = num
    var resultHexadecimal = num

    do {
        octal += "${resultOctal % 8}"
        resultOctal /= 8

        if (resultOctal < 8) octal += "$resultOctal"

    } while (resultOctal > 8)

    do {
        hexadecimal += when (resultHexadecimal % 16) {
            10 -> "A"
            11 -> "B"
            12 -> "C"
            13 -> "D"
            14 -> "E"
            15 -> "F"
            else -> "${resultHexadecimal % 16}"
        }

        resultHexadecimal /= 16
        if (resultHexadecimal < 16) hexadecimal += "$resultHexadecimal"

    } while (resultHexadecimal > 16)

    println("Decimal: $num")
    println("Octal: ${octal.reversed()}")
    println("Hexadecimal: ${hexadecimal.reversed()}\n")
}