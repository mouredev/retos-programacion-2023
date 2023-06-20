import kotlin.math.roundToInt

fun main() {

    /*
    * Reto #13 27/03/2023
    *
    * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
    * - El juego comienza proponiendo una palabra aleatoria incompleta
    *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
    * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
    *   la palabra a adivinar)
    *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
    *     uno al número de intentos
    *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
    *     al número de intentos
    *   - Si el contador de intentos llega a 0, el jugador pierde
    * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
    * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
    *
    */

    val juego = Ahorcado()
    juego.inicio()


}

class Ahorcado(
    var intentos: Int = 3
) {

    fun inicio() {

        val palabraClaro = getPalabra()
        var palabraOfuscada = ofuscarPalabra(palabraClaro)

        //var palabraClaro = palabra.toCharArray()
        val workingPalabraOfuscada = palabraOfuscada.toCharArray()


        while (intentos > 0) {
            println(palabraOfuscada)
            println("Tienes ${intentos} intentos. Puedes intentar averiguar una letra o poner la palabra ")

            print(">")
            val texto = readLine()!!
            if (texto.length == 1) {
                palabraClaro.forEachIndexed() { i, letra ->
                    if ((texto == letra.toString())
                        && (workingPalabraOfuscada[i] == '_')
                    ) {
                        workingPalabraOfuscada[i] = letra
                        palabraOfuscada = String(workingPalabraOfuscada)
                        intentos++
                    }
                }
                intentos--

            } else if (texto.length == palabraClaro.length) {
                if (palabraClaro == texto) {
                    palabraOfuscada = palabraClaro

                } else {
                    intentos--

                }


            } else {
                println("Entrada erronea")

            }

            if (palabraOfuscada == palabraClaro) {
                intentos = 0
            }
        }

        if (palabraClaro == palabraOfuscada) {
            println("¡¡¡ ENHORABUENA !!! has hacertado la palabra ${palabraClaro} ")
        } else {
            println("HAS FALLADO :(, la palabra era ${palabraClaro}")
        }

    }

    fun getPalabra(): String {
        val listaPalabras = listOf<String>(
            "volumen", "estallido", "alterar", "signos", "abollar", "muebles",
            "orilla", "ejemplo", "empatar", "claustrofobia", "tinto", "paella",
            "acercar", "diamante", "cuchara", "cucaracha", "fiscal", "trigal",
            "azulejo"
        )
        return listaPalabras[(0 until listaPalabras.count()).random()]

    }

    fun ofuscarPalabra(palabra: String): String {
        val palabraOfosucada = palabra.toCharArray()
        var numLetrasOfosucar = (palabra.length * .60).roundToInt() - 1
        while (numLetrasOfosucar > 0) {
            val pos = (0 until palabra.length).random()
            if (palabraOfosucada[pos] != '_') {
                palabraOfosucada[pos] = '_'
                numLetrasOfosucar--
            }
        }
        return String(palabraOfosucada)
    }

}