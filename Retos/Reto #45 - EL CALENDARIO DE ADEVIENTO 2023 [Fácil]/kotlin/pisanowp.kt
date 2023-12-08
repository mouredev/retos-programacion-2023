package retos2023

fun main() {

    /*
    * Reto #45 20/11/2023 EL CALENDARIO DE ADEVIENTO 2023
    *
    * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
    * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
    * Desde el 1 al 24 de diciembre.
    *
    * Crea un programa que simule el mecanismo de participación:
    * - [X] Mediante la terminal, el programa te preguntará si quieres añadir y borrar
    *   participantes, mostrarlos, lanzar el sorteo o salir.
    * - [X] Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
    * - [X] Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
    *   (Y no lo duplicarás)
    * - [X] Si seleccionas mostrar los participantes, se listarán todos.
    * - [X] Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
    *   (Avisando de si lo has eliminado o el nombre no existe)
    * - [X] Si seleccionas realizar el sorteo, elegirás una persona al azar
    *   y se eliminará del listado.
    * - [X] Si seleccionas salir, el programa finalizará.
    *
    */

    val cal = CalendarioADeviento()
    cal.menu()


}

class CalendarioADeviento() {

    private val participantes: MutableList<String> = mutableListOf()

    fun menu() {

        var opcion = 0
        while (opcion != 5) {
            println()
            println("1 - Añadir participante")
            println("2 - Borrar participante")
            println("3 - Listar participantes")
            println("4 - Realizar sorteo")
            println("5 - Salir")
            opcion = pideNumeroPositivo("Elige una opción")

            when (opcion) {
                1 -> addParticipante()
                2 -> borrarParticipante()
                3 -> listarParticipantes()
                4 -> realizarSorteo()
                5 -> println("Fin")
                else -> println("Opción no válida")
            }

        }

    }

    fun realizarSorteo() {
        if (participantes.isEmpty()) {
            println("Aún no hay participantes en la lista. Añade alguno antes de realizar el sorteo")

        } else {
            println("El ganador es ${participantes.random()} ¡¡ENHORABUENA!!")
        }

    }

    fun listarParticipantes() {
        if (participantes.isEmpty()) {
            println("Aún no hay participantes en la lista.")

        } else {
            println("Lista de participantes")
            participantes.forEach() {
                println(it)

            }

        }
    }

    fun borrarParticipante() {
        val participante = pedirNombreParticipante("Introduce el participante a añadir")
        if (participantes.contains(participante)) {
            participantes.remove(participante)
            println("$participante eliminado a la lista de participantes.")

        } else {
            println("$participante NO ESTA en la lista de participantes.")

        }


    }

    fun addParticipante() {
        val participante = pedirNombreParticipante("Introduce el participante a añadir")
        if (participantes.contains(participante)) {
            println("$participante YA ESTA en la lista de participantes.")
        } else {
            participantes.add(participante)
            println("$participante añadido a la lista de participantes.")
        }
    }


    fun pedirNombreParticipante(pregunta: String): String {

        var valido = false
        var input: String? = null

        while (!valido) {
            print("$pregunta >")
            input = readLine()
            if (input != null) {
                valido = true
            }
        }

        return input!!

    }

    fun pideNumeroPositivo( etiqueta : String): Int {
        var numero: Int? = null
        var valido = false

        while (!valido) {
            print("Introduce $etiqueta >")
            val input = readLine()

            try {
                numero = input?.toInt()
                if (numero != null) {
                    if (numero > 0){
                        valido = true
                    } else {
                        println("Entrada inválida. Debes ingresar un número entero positivo.")
                    }
                }

            } catch (e: NumberFormatException) {
                println("Entrada inválida. Debes ingresar un número entero positivo.")
            }
        }
        return numero!!
    }

}