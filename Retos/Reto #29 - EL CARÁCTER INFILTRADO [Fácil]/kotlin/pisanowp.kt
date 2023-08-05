fun main() {

    /*
    * Reto #29 17/07/2023 EL CARÁCTER INFILTRADO
    *
    * Crea una función que reciba dos cadenas de texto casi iguales,
    * a excepción de uno o varios caracteres.
    * La función debe encontrarlos y retornarlos en formato lista/array.
    * - Ambas cadenas de texto deben ser iguales en longitud.
    * - Las cadenas de texto son iguales elemento a elemento.
    * - No se pueden utilizar operaciones propias del lenguaje
    *   que lo resuelvan directamente.
    *
    * Ejemplos:
    * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
    * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
    */


    //val cadena1 = "Me llamo mouredev"
    //val cadena2 = "Me llemo mouredov"

    val cadena1 = "Me llamo.Brais Moure"
    val cadena2 = "Me llamo brais moure"

    val infiltrados = buscaCaracteresInfiltrados(cadena1, cadena2)
    println(infiltrados)

}

fun buscaCaracteresInfiltrados(cadena1: String, cadena2: String): List<Char> {
    val infiltrados = mutableListOf<Char>()

    if (cadena1.length != cadena2.length) {
        println("¡¡¡ LAS CADENAS NO TIENEN LA MISMA LONGITUD !!!")

    } else {

        cadena1.forEachIndexed { index, c1 ->

            val c2 = cadena2[index]
            //println("[${index}] => $c1 $c2")
            if (c1 != c2) {
                infiltrados.add(c2)
            }

        }

    }

    return infiltrados

}