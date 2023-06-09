fun main() {

    /*
    * Reto #22 29/05/2023 LA ESPIRAL
    *
    * Crea una función que dibuje una espiral como la del ejemplo.
    * - Únicamente se indica de forma dinámica el tamaño del lado.
    * - Símbolos permitidos: ═ ║ ╗ ╔ ╝ ╚
    *
    * Ejemplo espiral de lado 5 (5 filas y 5 columnas):
    * ════╗
    * ╔══╗║
    * ║╔╗║║
    * ║╚═╝║
    * ╚═══╝
    *
    */

    val lado = pideNumero( "el tamaño del lado")

    dibujaEspiral(lado)

}

fun dibujaEspiral(lado:Int) {
    //println("A dibujar una espiral de lado $lado")
    var espiral = mutableListOf("")

    (1..lado).forEach {

        if (it==1){
            espiral.add(0, "╗")

        } else {

            var indice = 0
            var temp = mutableListOf("")
            if (it%2==0){
                // Si la fila es par, hay que continuar la espiral
                // por la izquierda y terminar abajo

                (0 until espiral.count()-1).forEach {
                    if (it==0) {
                        temp.add(indice, "╔" + espiral.get(it) )
                        indice++

                    } else  {
                        temp.add(indice, "║" + espiral.get(it))
                        indice++
                    }
                }
                temp.add(indice, "╚" + "═".padStart(it-1, '═') )
                indice++

            } else {
                // Si la fila es impar, hay que continuar la espiral
                // por la derecha y terminar arriba

                temp.add(indice, "═".padStart(it-1, '═') + "╗" )
                indice++

                (0 until espiral.count()-1).forEach {
                    //println ( "$it => ${espiral.get(it)}  ")
                    if (it == espiral.count()-2) {
                        temp.add(indice, espiral.get(it) + "╝"  )
                        indice++

                    } else  {
                        temp.add(indice, espiral.get(it) + "║" )
                        indice++
                    }
                }
            }
            espiral = temp

        }

        /*
        println("Interación nº $it")
        espiral.forEach { println("=>$it<=")}
        println("-----------------") */

    }

    espiral.forEach { println(it) }

}

/*
* lado = 1
* ╗
*

*
* lado = 2
* ╔╗
* ╚═
*

*
* lado = 3
* ══╗
* ╔╗║
* ╚═╝
*

*
* lado = 4
* ╔══╗
* ║╔╗║
* ║╚═╝
* ╚═══
*

*
* lado = 5
* ════╗
* ╔══╗║
* ║╔╗║║
* ║╚═╝║
* ╚═══╝
*
*/



fun pideNumero( etiqueta : String): Int {
    var numero: Int? = null
    var valido = false

    while (!valido) {
        print("Introduce $etiqueta >")
        val input = readLine()

        try {
            numero = input?.toInt()
            valido = true
        } catch (e: NumberFormatException) {
            println("Entrada inválida. Debes ingresar un número entero.")
        }
    }
    return numero!!
}