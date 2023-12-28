package EjercicioKotlin.Mouredev

/*
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
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
 *   ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */

class reto13 {
    private var word = listOf("evening", "friend", "because", "waiting", "please", "tomorrow", "time").random()
    //el posiento de las palabra que estaran oculta
    private var attempts = (word.length * 0.6).toInt()
    private var wordDisguise = word

    init {
        disguiseWord()
        begin()
    }

    private fun begin() {
        var stop = false

        while (!stop) {
            print()
            val char = readln()[0]

            if (word.contains(char)) {
                val replace = wordDisguise.toCharArray()

                for (item in replace.indices) {
                    if (word[item] == char)
                        replace[item] = char
                }
                wordDisguise = String(replace)

            } else {
                println("\n========================")
                println("it is not in the word")
                println("========================")
                attempts--
                
                if (attempts == 0) {
                    stop = true
                    println("\n==============")
                    println("you have lost")
                    println("==============")
                }
            }

            if (!wordDisguise.contains('_')) {
                stop = true
                println("\n==============")
                println("to cattle")
                println("==============")
            }
        }
    }

    private fun print() {
        println("==================================")
        println("the word is : $wordDisguise")
        println("have $attempts available")
        print("select letter:")
    }

    private fun disguiseWord() {
        val position = Array(attempts, { 0 })
        
        for (item in 0..attempts - 1) {
            var positionToHide = 0
            var stop = false
            
            do {
                positionToHide = (0..word.length - 1).random()

                if (!position.contains(positionToHide))
                    stop = true

            } while (!stop)

            position[item] = positionToHide

            val replace = wordDisguise.toCharArray()
            replace[positionToHide] = '_'
            wordDisguise = String(replace)
        }
    }
}

fun main() {
    reto13()
}
