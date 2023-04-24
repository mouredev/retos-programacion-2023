/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */



import kotlinx.coroutines.delay
import kotlinx.coroutines.runBlocking
import kotlin.math.abs
import kotlin.math.pow

/**
 * Función principal
 */
fun main(){
    for(i in 1..10)
       println(CustomRandom.random(1, 100))
}
/**
 * Clase que genera números pseudoaleatorios utilizando el algoritmo de congruencia lineal
 * Contiene un metodo estático que devuelve un número pseudoaleatorio entre un rango de valores
 *
 */
class CustomRandom {
    /**
     * Genera una semilla para el algoritmo de congruencia lineal
     */
    fun getSeed(): Int {
        val multiplier: Int = 1103515245;
        val increment: Int = 12345;
        val bits = 2.0.pow(32.0).toInt()
        runBlocking {
            delay(1000)
        }
        val nanoSeconds = Math.abs(System.nanoTime())
        return (multiplier * nanoSeconds + increment).toInt() % bits
    }


        companion object {
            /**
             * Devuelve un número pseudoaleatorio entre un rango de valores
             * @param min
             * @param max
             */
            fun random(min: Int, max: Int): Int {
                val rand = CustomRandom()
                val seed = rand.getSeed()
                return abs(min + (seed % max))
            }
        }
}


main()
