fun main() {

    /*
     * Reto #14 03/04/2023
     * Crea una función que reciba un número decimal y lo trasforme a Octal
    * y Hexadecimal.
    * - No está permitido usar funciones propias del lenguaje de programación que
    * realicen esas operaciones directamente.
    */


    val listaNumeros = listOf(0, 3, 8, 12, 16, 57, 200, 800, 1332, 8149)

    listaNumeros.forEach { numero ->
        println("El numero $numero es ${numero.toOctal()} en OCTAL y ${numero.toHexadecimal()} en HEXADECIMAL")
    }

}

fun Int.toOctal(): String {
    var octal = ""
    var numero = this
    var resto: Int

    if (this == 0)
        octal = "0"

    while (numero > 0) {
        resto = numero % 8
        octal = resto.toString() + octal
        numero /= 8

    }
    return octal
}

fun Int.toHexadecimal(): String {
    val letras = listOf('A', 'B', 'C', 'D', 'E', 'F')
    var digitoChar : String
    var hexadecimal = ""
    var numero = this
    var resto: Int

    if (this == 0)
        hexadecimal = "0"

    while (numero > 0) {
        resto = numero % 16
        if (resto < 10) {
            digitoChar = resto.toString()
        }
        else {
            digitoChar = letras[resto-10].toString()
        }

        hexadecimal = digitoChar + hexadecimal
        numero /= 16

    }
    return hexadecimal

}