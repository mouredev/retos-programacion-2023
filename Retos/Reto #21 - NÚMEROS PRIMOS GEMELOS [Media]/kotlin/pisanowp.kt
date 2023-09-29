fun main() {

    /*
    * Reto #21 22/05/2023
    *
    * Crea un programa que encuentre y muestre todos los pares de números primos
    * gemelos en un rango concreto.
    * El programa recibirá el rango máximo como número entero positivo.
    *
    * - Un par de números primos se considera gemelo si la diferencia entre
    *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
    *
    * - Ejemplo: Rango 14
    *   (3, 5), (5, 7), (11, 13)
    */

    var rango: Int? = null
    var valido = false

    while (!valido) {
        print("Introduce el rango >")
        val input = readLine()

        try {
            rango = input?.toInt()
            valido = true
        } catch (e: NumberFormatException) {
            println("Entrada inválida. Debes ingresar un número entero.")
        }
    }

    buscarPrimosGemelos(rango!!)

}

fun esNumeroPrimo(numero:Int):Boolean {

    if (numero < 2)
        return false

    for (i in 2 until numero) {
        if (numero % i == 0)
            return false
    }

    return true
}

fun buscarPrimosGemelos(rango: Int) {
    for (numero in 1..rango) {
        if (esNumeroPrimo(numero)){
            // Busco cuales pueden ser los primeros hermanos
            for (hermano in numero..rango) {
                if (esNumeroPrimo(hermano)){
                    if ((hermano-numero)==2){
                        print("($numero, $hermano) ")
                    }
                }
            }
        }
    }
}
