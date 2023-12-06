import kotlin.math.absoluteValue

fun main() {

    /*
    * Reto #16 17/04/2023
    * Crea una función que dibuje una escalera según su número de escalones.
    * - Si el número es positivo, será ascendente de izquierda a derecha.
    * - Si el número es negativo, será descendente de izquierda a derecha.
    * - Si el número es cero, se dibujarán dos guiones bajos (__).
    *
    * Ejemplo: 4
    *         _
    *       _|
    *     _|
    *   _|
    * _|
    *
    */

    println("ESCALERA ARRIBA")
    printEscalera(3)

    println("NO ESCALERA")
    printEscalera()

    println("ESCALERA ABAJO")
    printEscalera(-5)



}

fun printEscalera(steps:Int = 0){

    if (steps ==0){
        println("__")

    } else if ( steps > 0) {
        // Escalera Arriba
        println("_".padStart(steps*2+1, ' '))
        (steps downTo 1).forEach(){
            println("_|".padStart(it*2, ' '))
        }

    } else {
        // Escalera Abajo
        (1 .. steps.absoluteValue).forEach(){
            println("_".padStart((it-1)*2, ' '))
            println("|".padStart(((it)*2)-1, ' '))

        }

    }

}

