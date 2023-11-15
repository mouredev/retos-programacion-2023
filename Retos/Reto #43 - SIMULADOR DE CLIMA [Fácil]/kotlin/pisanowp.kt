import kotlin.math.roundToInt

fun main() {

    /*
    * Reto #43 30/10/2023 SIMLULADOR DE CLIMA
    *
    * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
    * de un lugar ficticio al pasar un número concreto de días según estas reglas:
    * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
    * - Cada día que pasa:
    *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
    *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día
    *     siguiente aumenta en un 20%.
    *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día
    *     siguiente disminuya en un 20%.
    *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
    * - La función recibe el número de días de la predicción y muestra la temperatura
    *   y si llueve durante todos esos días.
    * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
    */

    val temperature = pideNumeroPositivo("Set initial temperature")
    val rainPercentage = pideNumeroPositivo("Set initial rain percentaje")
    val numDays = pideNumeroPositivo("Set number days of simulation")

    val simmulate = Weather(temperature, rainPercentage.toFloat())
    simmulate.simulate(numDays)

}

class Weather(
    private var temperature: Int = 34,
    private var rainPercentage: Float = 10f
) {
    private var maxTemp = 0
    private var minTemp = 0
    private var daysWithRain = 0

    fun simulate(numDays: Int = 7) {

        println("Start simulation")

        maxTemp = temperature
        minTemp = temperature

        (1..numDays).forEach { day ->
            if (temperature > maxTemp)
                maxTemp = temperature

            if (temperature < minTemp)
                minTemp = temperature

            println(" - Day number $day Temperature: ${temperature}º Rain percentaje: ${rainPercentage.roundToInt()} %")

            if ((1..100).random() <= 10) {

                when (listOf("up", "down").random()) {
                    "up" -> {
                        temperature += 2
                    }

                    "down" -> {
                        temperature -= 2
                    }
                }

            }

            if (temperature > 25) {
                rainPercentage *= 1.20f

            }

            if (temperature < 5) {
                rainPercentage -= ((rainPercentage * 20) / 100)
            }

            if (rainPercentage >= 100) {

                rainPercentage = 100f
                temperature -= 1
            }

            if (rainPercentage < 1) {
                rainPercentage = 1f

            }

            if ((1..100).random() <= rainPercentage) {
                println("¡¡¡¡¡LLUEVE !!!")
                daysWithRain++

            }


        }

        println("End simulation for $numDays days")
        println()
        println("Maximum temperature ${maxTemp}º")
        println("Minimum temperature ${minTemp}º")
        println("Days with rain ${daysWithRain}")

    }

}