import java.time.Instant
import kotlin.math.absoluteValue
import kotlin.math.pow

fun main() {

    /*
    * Reto #8 20/02/2023
    *
    * El generador pseudoaleatorio
    *
    * Crea un generador de números pseudoaleatorios entre 0 y 100.
    * No puedes usar ninguna función "random" (o semejante) del lenguaje de programación seleccionado.
    *
    */


    //
    // Usando los algoritmos encontrados en esta web para generar números pseudoalearios
    // https://svijaykoushik.github.io/blog/2019/10/04/three-awesome-ways-to-generate-random-number-in-javascript/
    //
    println("Usando MSM => ${GeneradorPseudoaleatorio().generate()}")
    println("Usando LCG => ${GeneradorPseudoaleatorio("LCG").generate()}")
    println("Usando XOR => ${GeneradorPseudoaleatorio("XOR").generate()}")


}


class GeneradorPseudoaleatorio(var method: String = "MSM", var seed: Int = 0) {


    fun generate(): Int {

        val numero: Int = when (method) {
            "MSM" -> {
                middleSquareMethod()
            }

            "LCG" -> {
                linearCongruentialGenerator()
            }


            "XOR" -> {
                xorShift()
            }

            else -> {
                99
            }
        }
        return numero

    }

    private fun setSeed() {
        seed = Instant.now().nano

    }

    // Middle Square Method (MSM)
    private fun middleSquareMethod(): Int {
        /*
        Middle Square Method (MSM)
        For an n-digit random number sequence:
        1.- Start with an n-digit number as the seed. Let’s say it’s a 2-digit number 42.
        2.- Square it. Here, the square of 42 is 1764.
        3.- Extract the middle n-digits of the squared number to get the next number in our sequence.
             In our case, the next number would be 76.

        4.- Use the result as the seed and repeat steps 1-4 for the next cycle.
         */
        setSeed()
        seed = seed.toString().substring(0..2).toInt()
        //println("Mi semillas es ${this.seed}")

        var iteraciones = 0
        seed.toString().forEach { it -> iteraciones += it.digitToInt() }
        //println("Iteraciones ${iteraciones}")

        var random = seed

        (0 until iteraciones).forEach {
            random = random * random
            //println(random)
            //random = random.toString().padStart(6, '0').substring(1..3).toInt()
            random = random.toString().padEnd(6, '0').substring(1..3).toInt()
            //println(random)
        }

        return (random % 101)
    }


    // The Linear Congruential Generator (LCG) algorithm
    private fun linearCongruentialGenerator(): Int {
        // The LCG uses a linear equation that involves congruence operation for the generation of a random sequence of numbers.
        // Linear means an algebraic equation that has no variables raised to the power greater than one.
        // Congruential means an equation that uses modulus division operation.

        // Where X is the seed. Akin to the MSM the result is used as the seed for the next cycle.

        // a – is the multiplier
        // c – is the increment and
        // m – is the modulus

        // It has the following conditions
        // m > 0, duh! divide by zero is impossible
        // 0 < a < m
        // 0 ≤ c < m and
        // 0 ≤ X < m
        setSeed()
        val a = 1664525.toDouble()
        val m = 2.toDouble().pow(32.toDouble())
        val c = 1013904223.toDouble()

        val random = (a * seed.toDouble() + c) % m

        return (random % 101).toInt()
    }

    private fun xorShift(): Int {
        setSeed()

        seed = seed xor (seed shl 13)
        seed = seed xor (seed shr 17)
        seed = seed xor (seed shl 5)

        return (seed % 101).absoluteValue


    }
}