import java.util.*

/*
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

fun main(args: Array<String>) {
    println("Inserte el numero de dias de la predicción: ")
    val dia: String = readln()
    simularClima(dia.toInt())
}

fun simularClima(dia: Int){
    println("Inserte la temperatura inicial: ")
    var temperatura: Int = readln().toInt()
    println("Inserte la probabilidad de lluvia: ")
    var probabilidadLluvia: Int = readln().toInt()
    var contadorDiasLluvia: Int = 0
    var aumentarDisminuirTemperatura: Int
    val listaTiempo: MutableList<Tiempo> = mutableListOf()
    val rnd: Random = Random()

    for (i in 1..dia){
        aumentarDisminuirTemperatura = rnd.nextInt(11) + 1

        if (aumentarDisminuirTemperatura == 1){
            temperatura += 2
        }

        if (aumentarDisminuirTemperatura == 2){
            temperatura -= 2
        }

        if (temperatura > 25){
            if ((probabilidadLluvia + 20) > 100)
                probabilidadLluvia = 100
            else
                probabilidadLluvia += 20
        }

        if (temperatura < 5){
            if ((probabilidadLluvia - 20) < 0)
                probabilidadLluvia = 0
            else
                probabilidadLluvia -= 20
        }

        listaTiempo.add(Tiempo(temperatura, probabilidadLluvia))

        if (probabilidadLluvia == 100){
            temperatura -= 1
            contadorDiasLluvia += 1
        }
    }

    //Mostrar datos por consola
    for (tiempo in listaTiempo){
        println(tiempo.toString())
    }

    listaTiempo.sortBy { it.temperatura }
    println("Temperatura mínima: ${listaTiempo[0].temperatura}")
    println("Temperatura máxima: ${listaTiempo[listaTiempo.lastIndex].temperatura}")
    println("Número de dias que ha llovido: " + contadorDiasLluvia)
}

data class Tiempo(val temperatura: Int, val probabilidadLluvia: Int){
    override fun toString(): String {
        return "Temperatura: " + temperatura.toString() + ", ProbabilidadLluvia: " + probabilidadLluvia.toString()
    }
}