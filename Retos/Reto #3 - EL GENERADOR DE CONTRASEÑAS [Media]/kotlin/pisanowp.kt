import kotlin.random.Random


fun main() {

    /*
    * Reto #3 06/01/2023
    *
    * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
    * Podrás configurar generar contraseñas con los siguientes parámetros:
    * - Longitud: Entre 8 y 16.
    * - Con o sin letras mayúsculas.
    * - Con o sin números.
    * - Con o sin símbolos.
    * (Pudiendo combinar todos estos parámetros entre ellos)
    */

    println(GeneradorClaves(longitud = 2, withUpperCase = true, withNumber = true, withSimbols = false).generarClave())
    println(GeneradorClaves(withNumber = true).generarClave())
    println(GeneradorClaves(longitud = 10, withSimbols = true, withUpperCase = true).generarClave())

}


class GeneradorClaves(
    var longitud: Int = 8,
    var withUpperCase: Boolean = false,
    var withNumber: Boolean = false,
    var withSimbols: Boolean = false
) {


    private fun dameLetra(): Char {
        return Random.nextInt(97, 123).toChar()
    }

    private fun dameNumero(): Char {
        return Random.nextInt(48, 58).toChar()
    }

    private fun dameSimbolo(): Char {
        return (when (Random.nextInt(0, 4)) {
            0 -> Random.nextInt(33, 48).toChar()
            1 -> Random.nextInt(58, 65).toChar()
            2 -> Random.nextInt(91, 97).toChar()
            else -> Random.nextInt(123, 127).toChar()
        })

    }

    fun generarClave(): String {
        var clave = ""
        var charType = 0
        var letra = 'x'
        if (longitud < 8)
            longitud = 8
        if (longitud > 16)
            longitud = 16

        (0 until longitud).forEach {
            charType = Random.nextInt(0, 4)

            if (charType == 0 && withUpperCase)
                letra = dameLetra().uppercaseChar()
            else if (charType == 1 && withNumber)
                letra = dameNumero()
            else if (charType == 2 && withSimbols)
                letra = dameSimbolo()
            else
                letra = dameLetra()

            clave += letra

        }

        return clave

    }

}