fun main() {

    /*
    * Reto #31 31/07/2023 EL ÁBACO
    *
    * Crea una función que sea capaz de leer el número representado por el ábaco.
    * - El ábaco se representa por un array con 7 elementos.
    * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
    *   para las cuentas y una secuencia de "---" para el alambre.
    * - El primer elemento del array representa los millones, y el último las unidades.
    * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
    *
    * Ejemplo de array y resultado:
    * ["O---OOOOOOOO",
    *  "OOO---OOOOOO",
    *  "---OOOOOOOOO",
    *  "OO---OOOOOOO",
    *  "OOOOOOO---OO",
    *  "OOOOOOOOO---",
    *  "---OOOOOOOOO"]
    *
    *  Resultado: 1.302.790
    *
    */

    // Creo un ábaco pasando un array
    val aux = listOf(
        "O---OOOOOOOO",
        "OOO---OOOOOO",
        "---OOOOOOOOO",
        "OO---OOOOOOO",
        "OOOOOOO---OO",
        "OOOOOOOOO---",
        "---OOOOOOOOO"
    ).toMutableList()

    val abaco = Abaco(aux)
    println(abaco.toInt())

    // Sobre el ábaco que ya tengo, lo reseteo a otro número
    abaco.init(2023)
    abaco.pintar()

}


class Abaco(
    var abaco: MutableList<String> = mutableListOf(
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO",
        "---OOOOOOOOO"
    )
) {

    fun init(numero: Int = 0) {
        (0..6).forEach { abaco[it] = "---000000000" }
        if (numero > 0) {
            numero.toString().padStart(7, '0').forEachIndexed { fila, digito ->
                setCuentas(fila, digito.digitToInt())
            }
        }
    }

    fun setCuentas(fila: Int, cuentas: Int) {
        val dummy = "".padStart(cuentas, '0') + "---" + "".padStart(9 - cuentas, '0')
        abaco[fila] = dummy


    }

    fun pintar() {
        abaco.forEach {
            println(it)
        }
    }

    fun toInt(): Int {
        var numero = ""
        abaco.forEach { fila ->
            val partes = fila.split("---")
            numero += partes[0].length
        }
        return numero.toInt()
    }

}