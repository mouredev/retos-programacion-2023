/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

import java.util.*

fun main() {
        val random = Random()
        val charPool: List<Char> = ('a'..'z') + ('A'..'Z') + ('0'..'9') + listOf('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '\\', '|', ';', ':', ',', '.', '<', '>', '/', '?')

        println("Ingrese la longitud de la contraseña entre 8 y 16")
        var length = readLine()!!.toInt()
        while(length < 8 || length > 16) {
            println("La longitud debe ser entre 8 y 16")
            length = readLine()!!.toInt()
        }

        println("Incluir letras mayúsculas en la contraseña? (S/N)")
        val uppercase = readLine()!!.toLowerCase() == "s"

        println("Incluir números en la contraseña? (S/N)")
        val numbers = readLine()!!.toLowerCase() == "s"

        println("Incluir símbolos en la contraseña? (S/N)")
        val symbols = readLine()!!.toLowerCase() == "s"

        var password = ""
        while (password.length < length) {
            val pool = if (uppercase) {
                if (numbers) {
                    if (symbols) {
                        charPool
                    } else {
                        charPool.filter { it.isLetterOrDigit() }
                    }
                } else {
                    if (symbols) {
                        charPool.filter { it.isLetter() }
                    } else {
                        charPool.filter { it.isLetter() }.filterNot { it.isUpperCase() }
                    }
                }
            } else {
                if (numbers) {
                    if (symbols) {
                        charPool.filterNot { it.isUpperCase() }
                    } else {
                        charPool.filterNot { it.isUpperCase() }.filter { it.isLetterOrDigit() }
                    }
                } else {
                    if (symbols) {
                        charPool.filterNot { it.isUpperCase() }.filterNot { it.isLetterOrDigit() }
                    } else {
                        charPool.filterNot { it.isUpperCase() }.filter { it.isLetter() }.filterNot { it.isDigit() }
                    }
                }
            }
            password += pool[random.nextInt(pool.size)]
        }
        println("La contraseña generada es: $password")
    }