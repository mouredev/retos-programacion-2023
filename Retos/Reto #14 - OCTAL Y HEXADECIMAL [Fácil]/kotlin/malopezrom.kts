import kotlin.Number

/*
 * Crea una función que reciba un número decimal y lo trasforme a Octal
 * y Hexadecimal.
 * - No está permitido usar funciones propias del lenguaje de programación que
 * realicen esas operaciones directamente.
 */



/**
 * Funcion principal
 */
fun main() {
    val valor = 255255255
    println("Decimal: $valor")
    println("Octal: ${valor.toOctal()}")
    println("Hexadecimal: ${valor.toHexadecimal()}")

}

/**
 * Funcion de extension que convierte un numero decimal a octal
 */
fun Number.toOctal(): Int {
    var octal = 0
    var decimal = this.toInt()
    var i = 1
    while (decimal != 0) {
        octal += (decimal % 8) * i
        decimal /= 8
        i *= 10
    }
    return octal

}

/**
 * Funcion de extension que convierte un numero decimal a hexadecimal
 */
fun Number.toHexadecimal(): String {
    var hexadecimal = ""
    var decimal = this.toInt()
    while (decimal != 0) {
        val value = decimal % 16
        hexadecimal = if (value < 10) {
            value.toString() + hexadecimal
        } else {
            (value + 55).toChar() + hexadecimal
        }
        decimal /= 16
    }
    return hexadecimal
}

main()