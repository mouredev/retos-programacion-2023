class BasesNumber(
    var decimal: Int,
    var octa: String = "",
    var hexa: String = ""
) {
    override fun toString(): String {
        return "decimal: $decimal - octadecimal: $octa - hexadecimal: $hexa"
    }
}

fun Int.toOctadecimal(): String {
    var result = ""
    var rest = this.mod(8)
    var quotient: Int = this / 8
    while(quotient > 8) {
        result = "$rest$result"
        rest = quotient.mod(8)
        quotient /= 8
    }
    result = "$quotient$rest$result"
    return result
}

fun Int.toHexadecimal(): String {
    var result = ""
    var rest = this.mod(16)
    var quotient: Int = this / 16
    while(quotient > 16) {
        result = "${rest.toHex()}$result"
        rest = quotient.mod(16)
        quotient /= 16
    }
    result = "${quotient.toHex()}${rest.toHex()}$result"
    return result
}

fun Int.toHex(): String {
    return when(this) {
        10 -> "A"
        11 -> "B"
        12 -> "C"
        13 -> "D"
        14 -> "E"
        15 -> "F"
        else -> "$this"
    }
}

fun calculateBases(number: Int): BasesNumber {
    val result = BasesNumber(number)
    result.octa = number.toOctadecimal()
    result.hexa = number.toHexadecimal()
    return result
}

fun main() {
    println(calculateBases(768))
    println(calculateBases(460))
}