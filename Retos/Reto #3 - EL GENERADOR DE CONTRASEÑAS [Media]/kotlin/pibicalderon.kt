
import kotlin.random.Random

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

private fun generarConstrasena(longitud: Int, conMayusculas: Boolean, conNumeros: Boolean, conSimbolos: Boolean) {

    if (longitud in 8..16) {
        val numeros = ('0'..'9').toList()
        val minusculas = ('a'..'z').toList()
        val mayusculas = ('A'..'Z').toList()
        val simbolos = listOf('~','!','@','#','$','%','^','&','*','(',')','-','_','+','=','[',']','{','}','|','<','>','?','/')

        val elementosConstrasena = mutableListOf(minusculas)

        if (conNumeros) {
            elementosConstrasena.add(numeros)
        }
        if (conSimbolos) {
            elementosConstrasena.add(simbolos)
        }
        if (conMayusculas) {
            elementosConstrasena.add(mayusculas)
        }
        val elementosAgregados = IntArray(elementosConstrasena.size)
        var password = ""
        for (i in 0 until longitud) {
            val indiceAleaotrio = Random.nextInt(elementosConstrasena.size)
            elementosAgregados[indiceAleaotrio] = 1
            password += elementosConstrasena[indiceAleaotrio].random()
        }

        if (elementosAgregados.sum() == elementosConstrasena.size) {
            println("Longitud: $longitud, con Mayusculas: $conMayusculas, con Numeros: $conNumeros, Con Simbolos: $conSimbolos:")
            println("Contrasena: $password")
        } else {
            // La contrasena no cumple todas las condiciones
            generarConstrasena(longitud, conMayusculas, conNumeros, conSimbolos)
        }
    } else {
        println("La contrasena tiene que ser entre 8 y 16 caracteres")
    }

}

fun main() {
    generarConstrasena(longitud = 8, conMayusculas = true, conNumeros = true, conSimbolos = true)
    generarConstrasena(longitud = 8, conMayusculas = false, conNumeros = true, conSimbolos = true)
    generarConstrasena(longitud = 8, conMayusculas = false, conNumeros = false, conSimbolos = true)
    generarConstrasena(longitud = 8, conMayusculas = false, conNumeros = false, conSimbolos = false)

    generarConstrasena(longitud = 10, conMayusculas = true, conNumeros = true, conSimbolos = true)
    generarConstrasena(longitud = 10, conMayusculas = false, conNumeros = true, conSimbolos = true)
    generarConstrasena(longitud = 10, conMayusculas = false, conNumeros = false, conSimbolos = true)
    generarConstrasena(longitud = 10, conMayusculas = false, conNumeros = false, conSimbolos = false)

    generarConstrasena(longitud = 7, conMayusculas = true, conNumeros = true, conSimbolos = true)
    generarConstrasena(longitud = 17, conMayusculas = true, conNumeros = true, conSimbolos = true)
}