fun main() {

    /*
    * Reto #20 18/05/2023
    *
    * ¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible!
    *
    *  Crea un programa que dibuje una Trifuerza de "Zelda"
    *  formada por asteriscos.
    *  - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
    *  - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
    *
    *  Ejemplo: Trifuerza 2
    *
    *    *
    *   ***
    *  *   *
    * *** ***
    */


    var filas: Int? = null
    var valido = false

    while (!valido) {
        print("Introduce el número de filas >")
        val input = readLine()

        try {
            filas = input?.toInt()
            valido = true
        } catch (e: NumberFormatException) {
            println("Entrada inválida. Debes ingresar un número entero.")
        }
    }

    TriFuerza(filas!!).pintar()



}

class TriFuerza(var filas:Int = 1){
    private var triFuerza = mutableListOf("")

    init {

        this.triFuerza = mutableListOf("")

        (filas downTo 1).forEach{fila->

            var pico = ""
            var base = ""
            var relleno = "".padStart(2*(filas - fila), ' ')
            (1..fila).forEach {
                pico += relleno + " *  "
                base += relleno + "*** "
                relleno = ""
            }
            this.triFuerza.add(base)
            this.triFuerza.add(pico)


        }


    }

    fun pintar(){
        this.triFuerza.reversed().forEach {
            println(it)
        }
    }

}