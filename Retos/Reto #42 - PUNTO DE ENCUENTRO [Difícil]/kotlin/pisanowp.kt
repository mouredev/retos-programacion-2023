
import kotlin.math.sqrt

fun main() {

    /*
    * Reto #42 23/10/2023 PUNTO DE ENCUENTRO
    *
    * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
    * en dos dimensiones.
    * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
    *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
    * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
    * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
    * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.
    *
    */

    // Se cruzan en t5, (5, 5)
    var obj1 = Objeto(0, 0, 1, 1)
    var obj2 = Objeto(5, 0, 0, 1)

    puntoDeEncuentro(obj1, obj2)

    obj1 = Objeto(3, 2, 1, 4)
    obj2 = Objeto(2, 1, 1, 2)
    puntoDeEncuentro(obj1, obj2)

    // Rectas paralelas verticales, no se cruzan nunca
    obj1 = Objeto(1, 0, 0, 1)
    obj2 = Objeto(2, 0, 0, 3)
    puntoDeEncuentro(obj1, obj2)

    // Rectas que tampoco se cruzan
    obj1 = Objeto(2, 1, 4, 2)
    obj2 = Objeto(1, 0, 0, 1)
    puntoDeEncuentro(obj1, obj2)

    // Se ecuentran en el origen del eje
    obj1 = Objeto(-1, -1, 1, 1)
    obj2 = Objeto(2, -2, -2, 2)
    puntoDeEncuentro(obj1, obj2)

    // Rectas paralelas verticales misma velocidad, no se cruzan nunca
    obj1 = Objeto(1, 0, 0, 1)
    obj2 = Objeto(2, 0, 0, 1)
    puntoDeEncuentro(obj1, obj2)



}

fun puntoDeEncuentro(obj1: Objeto, obj2: Objeto) {

    obj1.mostrarPosicion("Objeto1")
    obj2.mostrarPosicion("Objeto2")

    val distancia = obj1.distanciaAObjeto(obj2)
    var nuevaDistancia = distancia
    println("Distancia entre los puntos $distancia")

    var acercandose = true
    var tiempo = 1
    while (acercandose){
        obj1.nuevaPosicion()
        obj2.nuevaPosicion()

        obj1.mostrarPosicion("Objeto1")
        obj2.mostrarPosicion("Objeto2")
        nuevaDistancia = obj1.distanciaAObjeto(obj2)

        println("Nueva distancia entre los puntos $nuevaDistancia")

        if (nuevaDistancia < distancia){
            tiempo++

        } else {
            // Se alejan, ya no van a coincidir en el tiempo
            acercandose = false
        }

        if (nuevaDistancia < 1){
            // Se han encontrado
            acercandose = false
        }

    }

    if ( nuevaDistancia < 1 ) {
        println("Se cruzan en el tiempo: $tiempo  en el punto ( ${obj1.posX}, ${obj1.posY} )")
    } else {
        println("Los puntos no se cruzan nunca")
    }

}

class Objeto(var posX: Int, var posY: Int, val velX: Int, val velY: Int){

    fun mostrarPosicion(nombre:String){
        println( "$nombre => ($posX, $posY)")
    }

    fun nuevaPosicion(){
        posX += velX
        posY += velY
    }

    fun distanciaAObjeto(obj2: Objeto):Double{

        val posX2 = (( obj2.posX - this.posX) * (obj2.posX - this.posX)).toDouble()
        val posY2 = (( obj2.posY - this.posY) * (obj2.posY - this.posY)).toDouble()

        return sqrt( posX2 + posY2 )

    }
}

