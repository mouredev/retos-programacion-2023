package EjercicioKotlin.Mouredev

fun main() {
    cuenta_atras(5,1000)
    cuenta_atras(3,5000)
}

/*
 * Crea una función que reciba dos parámetros para crear una cuenta atrás.
 * - El primero, representa el número en el que comienza la cuenta.
 * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
 * - Sólo se aceptan números enteros positivos.
 * - El programa finaliza al llegar a cero.
 * - Debes imprimir cada número de la cuenta atrás.
 */

fun cuenta_atras(desde:Int , tiempo:Long){
    println("\nStart\n")

    for (it in desde.downTo(0)){
        println("$it")
        Thread.sleep(tiempo)
    }

    println("\nEnd\n")
}
