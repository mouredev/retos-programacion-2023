fun main() {

    /*
    * Reto #46 27/11/2023  LA CARRERA DE COCHES
    *
    * Crea un programa que simule la competición de dos coches en una pista.
    * - Los dos coches estarán representados por 🚙 y 🚗. Y la meta por 🏁.
    * - Cada pista tendrá entre 1 y 3 árboles 🌲 colocados de forma aleatoria.
    * - Las dos pistas tendrán una longitud configurable de guiones bajos "_".
    * - Los coches comenzarán en la parte derecha de las pistas. Ejemplo:
    *   🏁____🌲_____🚙
    *   🏁_🌲____🌲___🚗
    *
    * El juego se desarrolla por turnos de forma automática, y cada segundo
    * se realiza una acción sobre los coches (moviéndose a la vez), hasta que
    * uno de ellos (o los dos a la vez) llega a la meta.
    * - Acciones:
    *   - Avanzar entre 1 a 3 posiciones hacia la meta.
    *   - Si al avanzar, el coche finaliza en la posición de un árbol,
    *     se muestra 💥 y no avanza durante un turno.
    *   - Cada turno se imprimen las pistas y sus elementos.
    *   - Cuando la carrera finalice, se muestra el coche ganador o el empate.
    *
    */

    CarreraDeCoches(30)

}

class CarreraDeCoches(longitud: Int = 10) {

    private val circuito1 : Carretera
    private val circuito2 : Carretera

    init {
        circuito1 = Carretera(longitud = longitud, "🚙" )
        circuito2 = Carretera(longitud = longitud, "🚗" )
        loopGame()

        println("------------------")
        if (circuito1.enMeta && circuito2.enMeta){
            println("¡¡¡ EMPATE !!!")
        } else if (circuito1.enMeta){
            println("¡¡¡ GANADOR 🚙 !!!")
        } else if (circuito2.enMeta){
            println("¡¡¡ GANADOR 🚗 !!!")
        }
        println("------------------")
    }


    private fun loopGame() {

        // Inicio carrera
        circuito1.pintar()
        circuito2.pintar()
        retardo()

        var finCarrera = false
        while ( !finCarrera ) {

            val posiciones = (1..3).random()
            circuito1.avanzar(posiciones)
            circuito2.avanzar(posiciones)
            circuito1.pintar()
            circuito2.pintar()
            retardo()
            if (circuito1.enMeta || circuito2.enMeta){
                finCarrera = true
            }

        }

    }


    private fun retardo(segundos:Long = 1){

        Thread.sleep(segundos *1000)
    }







}

class Carretera(val longitud: Int, cocheInicial: String){

    private val carretera: MutableList<String> = mutableListOf()
    private val meta = "🏁"
    private val arbol = "🌲"
    private val accidente = "💥"

    var enMeta = false

    init{
        carretera.add(meta)
        (1..longitud).forEach(){
            carretera.add("_")
        }

        // Ponemos los árboles
        var numArboles : Int = (1..3).random()
        while (numArboles>0) {
            val posicion = (1..longitud).random()
            if (carretera[posicion] != arbol) {
                carretera[posicion] = arbol
                numArboles--
            }

        }

        // Finalmente, ponemos el coche en la salida
        carretera.add(cocheInicial)

    }

    fun avanzar(movimiento:Int){

        var mov = movimiento
        var posicion = carretera.lastIndex //Posicion actual del coche


        while (mov>0){

            when (carretera[posicion-1]) {
                meta -> {
                    enMeta = true
                    mov = 0
                }

                arbol -> {
                    carretera[posicion-1] = accidente
                    mov = 0
                }

                else -> {
                    carretera[posicion-1] = carretera[posicion]
                    carretera.removeLast()

                    posicion--
                    mov--

                }

            }

        }

    }

    fun pintar(){
        carretera.forEach(){
            print(it)
        }
        println()
    }

}