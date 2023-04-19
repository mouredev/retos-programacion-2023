import com.google.gson.Gson
import java.net.HttpURLConnection
import java.net.URL
import kotlinx.serialization.*
import kotlin.coroutines.coroutineContext
import kotlin.math.floor
import kotlin.random.Random

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
 * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar ocultando más del 60%
 * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
 */






/**
 * Funcion de extension para obtener todos los indices de una ocurrrencia de un string
 */
fun String.indexOfAll(search:String):List<Int>{
    val indexes = mutableListOf<Int>()
    var i = -1

    while((this.indexOf(search, i+1).also { i = it }) != -1){
        indexes.add(i)
    }
    return indexes

}
/**
 * Interfaz para representar una letra y su posicion dentro de una palabra
 */
data class Letter(val letter:String, val position:Int)


/**
 * Clase para manejar la logica de las palabras
 */
/**
 * Constructor de la clase
 * @param word Palabra original a adivinarl
 * @param handicap Porcentaje de letras a ocultarlllll
 */

class GuessWord(val word:String, val handicap:Double){
    /**
     * API para obtener palabras aleatorias
     */
    companion object {
        private const val API_WORDS = "https://clientes.api.greenborn.com.ar/public-random-word?c=9&l=8"
        /**
         * Metodo estatico para obtener una palabra aleatoria de la API
         */
        val randomWord: String by lazy {
            val wordAPIURL = URL(API_WORDS)
            val wordConnection = wordAPIURL.openConnection() as HttpURLConnection
            try {
                val responseText = wordConnection.inputStream.bufferedReader().readText()
                Gson().fromJson(responseText, Array<String>::class.java).let { result ->
                    result[0]
                }
            } catch (e: Exception) {
                throw e
            } finally {
                wordConnection.disconnect()
            }
        }
    }


    val originalWord:String = word
    val letterUsed:MutableList<String> = mutableListOf()
    val letters:MutableList<Letter> = charsToHide()
    /**
     * Devuelve la palabra ofuscada
     */
    var secreword:String = this.offuscate()
    /**
     * Metodo para ocultar las letras de la palabra
     * @private
     */
    private fun charsToHide():MutableList<Letter>{
        val numChars = floor(originalWord.length * handicap).toInt()
        var offuscated = originalWord
        var _letters:MutableList<Letter> = mutableListOf()
        repeat(numChars) {
            val position = (0 until originalWord.length).random()
            offuscated = offuscated.substring(0, position) + '_' + offuscated.substring(position + 1)
        }

        _letters = offuscated.foldIndexed(mutableListOf()) { index, acc, current ->
            if (current == '_') acc
            else (acc + Letter(current.toString(), index)).toMutableList()
        }
        return _letters
    }
    private fun offuscate(): String {
        val palabra =
      originalWord.mapIndexed { i, c ->
        if (letters.any { it.position == i }) c else '_'
    }.joinToString("")

    return palabra
    }
    /**
     * Metodo para agregar una letra usada a la lista de letras que ya se han usado y no estan en la palabra
     * @param letter
     */
    fun addUserLetter(letter:String){
        if(!letterUsed.contains(letter)){
            letterUsed.add(letter)
        }
    }
    /**
     * Metodo para obtener las letras usadas que no estan en la palabra
     */
    fun letterUsed():String{
        return this.letterUsed.joinToString(",")
    }
    /**
     * Metodo para agregar una letra que si esta en la palabra
     * @param letter
     */
    fun addLetter(letter:Letter):Boolean{
        return if(this.letters.any {
                    it.position == letter.position && it.letter=="_"
                }){
            false
        }else{
            this.letters.add(letter)
            this.secreword = this.offuscate()
            true
        }


    }

}
/**
 * Clase para manejar la logica del juego
 */
/**
 * Constructor de la clase
 * @param word Palabra a adivinar
 */
class HangedGame(val word:String) {
    var attempts = 1
    var isFinish = false
    val maxAttemps = 5
    val guessWordClass = GuessWord(word, 0.6)
    val userInterface:UserInterface = UserInterface()
    /**
     * Metodo que devuelve la palabra que se debe adivinar ofuscada
     */

    val guessWord: String
        get() {
            return this.guessWordClass.secreword
        }

    /**
     * Metodo para adivinar una letra de la palabra
     * Si es una sola letra se agrega a la lista de letras usadas
     * Si es mas de una letra se intenta adivinar la palabra
     * @param letter Letra a adivinar o palabra a adivinar
     */
    fun guessLetter(letter: String): Boolean {

        if (letter.length > 1) {
            return if (letter == this.word) {
                println("¡¡¡Has ganado!!! La palabra que buscamos es $word")
                this.isFinish = true
                true
            } else {
                this.attempts++
                println("ERROR : La palabra no es correcta")
                if (this.attempts >= this.maxAttemps) {
                    println("¡¡¡Has perdido!!! La palabra que buscamos es $word")
                    println(userInterface.HangedInput[this.attempts-1])
                    this.isFinish = true
                }
                false
            }

        } else {
            if (this.word.contains(letter)) {
                this.word.indexOfAll(letter).forEach { index ->
                    if (this.guessWordClass.addLetter(Letter(letter, index))) {
                        if(this.guessWordClass.secreword==this.word){
                            println("¡¡¡Has ganado!!! La palabra que buscamos es $word")
                            this.isFinish = true
                            return true
                        }

                    }
                }
            } else {
                attempts++
                guessWordClass.addUserLetter(letter)
                println("\"ERROR : La letra no está en la palabra\"")
                if (this.attempts > this.maxAttemps) {
                    println(userInterface.HangedInput[this.attempts-1])
                    println("¡¡¡Has perdido!!! La palabra que buscamos es $word")
                    this.isFinish = true

                }
                return false

            }

        }
        return false
    }
    /**
     * Metodo asincrono para iniciar el juego
     */
    fun play(){
        println("Bienvenido al juego del ahorcado")
        println("=================================")
        while(!this.isFinish){
            println(userInterface.HangedInput[this.attempts-1])
            println("La palabra a adivinar: ${this.guessWord}")
            println("Intentos restantes : ${this.maxAttemps-this.attempts+1}")
            println("Letras usadas: ${this.guessWordClass.letterUsed()}")
            val letter = userInterface.prompt("Introduce una letra o una palabra")
            this.guessLetter(letter)

        }
    }



}
/**
 * Clase para manejar la interfaz de usuario
 *
 */
class UserInterface{

    val HangedInput:List<String> = listOf("""
    +---+
    |   |
        |
        |
        |
        |
=========""","""
    +---+
    |   |
    O   |
    |   |
        |
        |
=========""","""
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========""","""
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========""","""
    +---+
    |   |
    O   |
   /|\  |
   /    |
        |
=========""","""
    +---+
    |   |
    O   |
   /|\  |
   / \  |
        |
=========""")

    /**
     * Metodo para leer una entrada de texto
     * @param message Mensaje a mostrar al usuario
     */
    fun prompt(message: String): String {
        return readln()
    }

}
/**
 * Inicio del juego
 */

fun main(){

    val game = HangedGame(GuessWord.randomWord)
    game.play()

}

main()




