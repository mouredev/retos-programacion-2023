package EjercicioKotlin.Mouredev

class Reto45_ElCalendarioDeAdeviento {

    var listaParticipantes: MutableList<String> = mutableListOf("mario", "eskerni", "jaziel", "polonia")

    init {
        var stop = false

        while (stop == false) {
            when (menu()) {
                1 -> {
                    agregarParticipante()
                }

                2 -> {
                    borrarParticipante()
                }

                3 -> {
                    listarParticipante()
                }

                4 -> {
                    realizarSorteo()
                }

                5 -> {
                    stop = true
                }

                else -> {
                    println("Opcion no existe")
                }

            }
        }
    }

    private fun agregarParticipante() {
        println("\n\n")
        println("---------Agrega Participante---------")
        print("Digite el nombre:")

        val nombre = readln()

        //el contains busca si hay un nombre igual en la lista
        if (listaParticipantes.contains(nombre)) {
            println("Participante ya esta en la lista")
        } else {
            listaParticipantes.add(nombre)
            println("Participante agregado")
        }
    }

    private fun realizarSorteo() {
        println("\n\nEl ganador es :${listaParticipantes.random()}")
        listaParticipantes = mutableListOf()
        println("\n\nSe limpio la lista")
    }

    private fun borrarParticipante() {
        println("\n\n")
        println("---------Borrar Participante---------")
        print("Digite el nombre:")

        val nombre = readln()

        //el contains busca si hay un nombre igual en la lista
        if (listaParticipantes.contains(nombre)) {
            listaParticipantes.remove(nombre)
            println("Participante borrado de la lista")
        } else {
            println("Participante no esta en la lista")
        }
    }

    private fun listarParticipante() {
        var item = 1
      
        println("\n\n----Lista de participante----")
        
        listaParticipantes.map {
            println("${item}.${it}")
            item++
        }
    }

    private fun menu(): Int {
        var select = 0
      
        println("\n\n")
        println("---------Menu---------")
        println("1.Agregar participante")
        println("2.Borrar participante")
        println("3.Mostrar")
        println("4.Realizar Sorteo")
        println("5.Salir")
        print("Seleccione una opcion:")
        select = readLine()!!.toInt()

        return select
    }
}

fun main() {
    Reto45_ElCalendarioDeAdeviento()
}
