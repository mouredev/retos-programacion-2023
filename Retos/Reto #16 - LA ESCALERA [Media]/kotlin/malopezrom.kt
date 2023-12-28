import kotlin.math.absoluteValue

/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 *
 * Ejemplo: 4
 *         _
 *       _|
 *     _|
 *   _|
 * _|
 *
 */

fun main(){
    printSteps(-4)
    printSteps(4)
    printSteps(10)
    printSteps(-10)
    printSteps(0)
}


/**
 * Función que imprime una escalera de un determinado número de escalones
 * @param steps número de escalones de la escalera
 */
fun printSteps(steps:Int){

    if(steps==0){
        println("__")
    }else{
        if(steps>0) {
            println(" ".repeat(steps * 2) + "_")
        }else{
            println("_")
        }
        stepsRecursive(steps,1)
    }


}

/**
 * Función recursiva que imprime los escalones de la escalera
 * @param steps número de escalones de la escalera
 * Si el número de escalones es positivo, la escalera es ascendente y si es negativo, es descendente
 */
fun stepsRecursive(steps: Int,currentStep: Int){
    //Caso base
    if (currentStep > steps.absoluteValue) {
        return
    }
    if(steps>0){
        println(" ".repeat((steps - currentStep) * 2) + "_|")
    }
    else{
        println(" ".repeat((currentStep) * 2-1) + "|_")
    }
    // LLamada recursiva
    stepsRecursive(steps, currentStep + 1)
}




