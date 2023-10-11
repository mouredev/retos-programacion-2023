fun main() {

    /*
    * Reto #40 10/10/2023  TABLA DE MULTIPICAR
    *
    * Crea un programa que sea capaz de solicitarte un número y se
    * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
    * - Debe visualizarse qué operación se realiza y su resultado.
    *   Ej: 1 x 1 = 1
    *       1 x 2 = 2
    *       1 x 3 = 3
    *       ...
    */

    val numero = pideNumeroPositivo("Tabla de Multipicar")
    pintarTablaMultiplicar(numero)

}

fun pintarTablaMultiplicar(numero: Int) {
    (1..10).forEach(){
        println("$numero x $it = ${numero * it}")
    }
}

fun pideNumeroPositivo( etiqueta : String): Int {
    var numero: Int? = null
    var valido = false

    while (!valido) {
        print("Introduce $etiqueta >")
        val input = readLine()

        try {
            numero = input?.toInt()
            if (numero != null) {
                if (numero > 0){
                    valido = true
                } else {
                    println("Entrada inválida. Debes ingresar un número entero positivo.")
                }
            }

        } catch (e: NumberFormatException) {
            println("Entrada inválida. Debes ingresar un número entero positivo.")
        }
    }
    return numero!!
}