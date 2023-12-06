fun main() {

    /*
    * Reto #28 10/07/2023 EXPRESIÓN MATEMÁTICA
    *
    * Crea una función que reciba una expresión matemática (String)
    * y compruebe si es correcta. Retornará true o false.
    * - Para que una expresión matemática sea correcta debe poseer
    *   un número, una operación y otro número separados por espacios.
    *   Tantos números y operaciones como queramos.
    * - Números positivos, negativos, enteros o decimales.
    * - Operaciones soportadas: + - * / %
    *
    * Ejemplos:
    * "5 + 6 / 7 - 4" -> true
    * "5 a 6" -> false
    */

    print("Introduce expresión matemática a validar >")
    val  expresionMatematica =  readLine()
    if (expresionMatematica != null){
        if (validaExpresionMatematica(expresionMatematica)){
            println("LA EXPRESIÓN ${expresionMatematica} ES VÁLIDA")
        } else {
            println("LA EXPRESIÓN ${expresionMatematica} NO ES VÁLIDA")
        }

    }

    /*
    Descomentar para prebas
    val expresiones = listOf(
        "5 + 6 / 7 - 4",
        "1 + 2", "4 - 3", "5 * 6", "8 / 4",
        "1 +2", "4 -3", "5 *6", "8 /4",
        "5 a 6", "3 + 4 r 8",
        "22 + 34 / 33",
        "2+3", "25 + 3",
        "5 a ",
        "5 + ", "+ 3"
    )
    expresiones.forEach {
        if (validaExpresionMatematica(it)){
            println("${it} => VÁLIDA")
        } else {
            println("${it} => NO VÁLIDA")
        }
    }
    */







}

fun validaExpresionMatematica(expresionMatematica: String): Boolean {
    // Expresion regular,
    // ^[0-9]+  Debe empezar por número
    // y luego se debe repetir 1 o más veces la siguiente cadena
    // espacio (\s), operador (+|-|*|/), otro espacio (\s) y un número
    // (\\s(\\+|-|\\*|/)\\s[0-9]+)+$"
    val pattern = "^[0-9]+(\\s(\\+|-|\\*|/)\\s[0-9]+)+$"

    return Regex(pattern).matches(expresionMatematica)

}

