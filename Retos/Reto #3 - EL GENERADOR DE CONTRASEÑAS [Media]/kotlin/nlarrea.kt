/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

fun main() {
    println(passwordGenerator(16, true, true, true))
    println(passwordGenerator(8, false, false, false))
    println(passwordGenerator(10, true, true, false))
}


fun passwordGenerator(
    n:Int = 8,
    hasUpper:Boolean = false,
    hasNum:Boolean = false,
    hasSymbols:Boolean
) : String {
    var choices = (97..122).toMutableList()     // ASCII a-z

    if (hasUpper) choices += (65..90).toMutableList()   // ASCII A-Z
    if (hasNum) choices += (48..57).toMutableList()     // ASCII 0-9
    if (hasSymbols) choices += (33..47).toMutableList() + (58..64).toMutableList() + (91..96).toMutableList()

    var length = if (n < 8) 8 else if (n > 16) 16 else n
    var password = ""
    for (i in 0..length) {
        password += choices.random().toChar()
    }

    return password
}