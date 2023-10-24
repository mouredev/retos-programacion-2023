import java.util.InputMismatchException
import java.util.Scanner

/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ...
 */

fun main(args: Array<String>) {
    var scan = Scanner(System.`in`)
    var number: Int = 0
    var loopFirstTime: Boolean = true

    println("Inserte un número del 1 al 10:")

    do {
        if (!loopFirstTime){
            println("El valor insertado no es correcto.\nInserte un número del 1 al 10:")
        }

        try {
            number = scan.nextInt()
        } catch (e: InputMismatchException){
            scan = Scanner(System.`in`)
        }

        loopFirstTime = false
    } while (number < 1 || number > 11)

    for (i in 1..10){
        println("$number x $i = ${number * i}")
    }
}