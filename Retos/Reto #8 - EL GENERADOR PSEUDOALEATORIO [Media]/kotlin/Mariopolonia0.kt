fun main() {
    ramdow1_100()
}

/*
 * Crea un generador de números pseudoaleatorios entre 0 y 100.
 * - No puedes usar ninguna función "random" (o semejante) del 
 *   lenguaje de programación seleccionado.
 *
 * Es más complicado de lo que parece...
 */

//video de referencia : https://youtu.be/wClRtNl60cw

fun ramdow1_100() {

    val time = System.currentTimeMillis().toString()
    var semilla = time.substring(time.length - 3, time.length).toInt()
    
    var hasta = 0
    var numero = 0.0
    var numeroDos = 0.0
    var contador = 0

    print("Cuanto número aleatorio se imprimirán:")
    hasta = readLine()!!.toInt()


    while (contador < hasta) {
        numero = ((5 * semilla + 7) % 8).toDouble()
        numeroDos = numero * 8.toDouble()
        
        if (numeroDos > 0 && numeroDos <= 100){
            println("$numeroDos")
            contador ++
        }
        
        semilla = numero.toInt()
    }
}
