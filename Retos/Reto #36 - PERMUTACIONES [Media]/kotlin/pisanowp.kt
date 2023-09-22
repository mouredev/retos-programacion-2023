fun main() {

    /*
    * Reto #36 04/09/2023  PERMUTACIONES
    *
    * Crea un programa que sea capaz de generar e imprimir todas las
    * permutaciones disponibles formadas por las letras de una palabra.
    * - Las palabras generadas no tienen por qué existir.
    * - Deben usarse todas las letras en cada permutación.
    * - Ejemplo: sol, slo, ols, osl, los, lso
    *
    */

    val palabra = "sol"
    //val palabra = "hola"

    permutaciones("", palabra)

}

fun permutaciones(palabra: String, resto: String = "") {
    if (resto.length == 1) {
        println(palabra + resto)

    } else {
        resto.forEachIndexed { index, c ->
            permutaciones(palabra + c, resto.removeRange(index, index + 1))

        }

    }

}