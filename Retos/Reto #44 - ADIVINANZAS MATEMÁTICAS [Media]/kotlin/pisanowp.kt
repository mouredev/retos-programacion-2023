import java.time.Duration
import java.time.LocalDateTime

fun main() {

    /*
    * Reto #44 13/11/2023 ADIVINANZAS MATEMÁTICAS
    *
    * Crea un juego interactivo por terminal en el que tendrás que adivinar
    * el resultado de diferentes
    * operaciones matemáticas aleatorias (suma, resta, multiplicación
    * o división de dos números enteros).
    * - Tendrás 3 segundos para responder correctamente.
    * - El juego finaliza si no se logra responder en ese tiempo.
    * - Al finalizar el juego debes mostrar cuántos cálculos has acertado.
    * - Cada 5 aciertos debes aumentar en uno el posible número de cifras
    *   de la operación (cada vez en un operando):
    *   - Preguntas 1 a 5: X (entre 0 y 9) operación Y (entre 0 y 9)
    *   - Preguntas 6 a 10: XX (entre 0 y 99) operación Y (entre 0 y 9)
    *   - Preguntas 11 a 15: XX operación YY
    *   - Preguntas 16 a 20: XXX (entre 0 y 999) operación YY
    *   ...
    */

    adivinanzasMatematicas()

}

fun adivinanzasMatematicas(tiempoParaResponder:Long = 3){

    var ronda = 0
    var finJuego = false

    while (!finJuego){
        ronda++
        val operacion = dameOperacion()
        var num1 = 0
        var num2 = 0
        var limiteInferior = 0

        if (operacion == '/') {
            limiteInferior = 1
        }

        if (ronda in (1..5)) {
            num1 = dameNumero(0, 9)
            num2 = dameNumero(limiteInferior, 9)

        } else if (ronda in (6..10) ) {
            num1 = dameNumero(0, 99)
            num2 = dameNumero(limiteInferior, 9)

        } else if (ronda in (11..15) ) {
            num1 = dameNumero(0, 99)
            num2 = dameNumero(limiteInferior, 99)

        } else if (ronda in (16..20) ) {
            num1 = dameNumero(0, 999)
            num2 = dameNumero(limiteInferior, 99)

        } else if (ronda in (11..25) ) {
            num1 = dameNumero(0, 999)
            num2 = dameNumero(limiteInferior, 999)

        }


        print("Ronda nº$ronda. ")
        val resultado = dameResultado(num1, num2, operacion)


        val resultadoUsuario = pideResultado("$num1 ${operacion} $num2", tiempoParaResponder)
        if (resultadoUsuario==-1) {
            println("Has tardado más de $tiempoParaResponder segundos en responder :(")
            finJuego = true

        } else if (resultadoUsuario!=resultado)  {
            println("Error, el resutaldo era $resultado :(")
            finJuego = true
        } else {
            println("¡¡¡ Enhorabuena !!! :D, vamos a por otra ...")
        }

    }

}


fun dameNumero( limiteInferior : Int = 0, limiteSuperior : Int = 9) : Int {
    return (limiteInferior..limiteSuperior).random()
}

fun dameOperacion() : Char {
    val operaciones = listOf('+', '-', '*', '/')
    return operaciones.random()
}

fun dameResultado(num1:Int, num2:Int, operacion:Char): Int{
    val resultado : Int
    when (operacion) {
        '+' -> {
            resultado = num1 + num2
        }
        '-' -> {
            resultado = num1 - num2
        }
        '*' -> {
            resultado = num1 * num2
        }
        '/' -> {
            resultado = num1 / num2
        }
        else -> {
            resultado = 0
        }
    }
    return resultado

}

fun pideResultado( etiqueta : String, tiempoParaResponder: Long = 3): Int {
    var numero: Int? = null
    var valido = false


    val tiempoInicial = LocalDateTime.now()

    while (!valido) {
        print("Introduce $etiqueta = ")
        val input = readLine()

        try {
            numero = input?.toInt()
            if (numero != null) {
                valido = true
            } else {
                println("Entrada inválida. Debes ingresar un número entero positivo.")
            }

        } catch (e: NumberFormatException) {
            println("Entrada inválida. Debes ingresar un número entero positivo.")
        }
    }

    val tiempoFinal = LocalDateTime.now()
    val duracion: Duration = Duration.between(tiempoInicial, tiempoFinal)

    // Obtener la diferencia en segundos
    val segundos = duracion.seconds
    if (segundos> tiempoParaResponder){
        numero=-1
    }

    return numero!!

}