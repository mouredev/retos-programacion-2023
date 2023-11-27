package retos2023

import java.util.*

/*
 * ¿Conoces el calendario de aDEViento de la comunidad (https://adviento.dev)?
 * 24 días, 24 regalos sorpresa relacionados con desarrollo de software.
 * Desde el 1 al 24 de diciembre.
 *
 * Crea un programa que simule el mecanismo de participación:
 * - Mediante la terminal, el programa te preguntará si quieres añadir y borrar
 *   participantes, mostrarlos, lanzar el sorteo o salir.
 * - Si seleccionas añadir un participante, podrás escribir su nombre y pulsar enter.
 * - Si seleccionas añadir un participante, y este ya existe, avisarás de ello.
 *   (Y no lo duplicarás)
 * - Si seleccionas mostrar los participantes, se listarán todos.
 * - Si seleccionas eliminar un participante, podrás escribir su nombre y pulsar enter.
 *   (Avisando de si lo has eliminado o el nombre no existe)
 * - Si seleccionas realizar el sorteo, elegirás una persona al azar
 *   y se eliminará del listado.
 * - Si seleccionas salir, el programa finalizará.
 */

fun main(){

    val competitors = mutableListOf<String>()
    val scanner = Scanner(System.`in`)
    boardOptions()
    var userInput = scanner.nextLine().lowercase()
    while ((userInput != "5") && (userInput != "Salir".lowercase())){
        when(userInput){
            "1", "Agregar participante".lowercase() -> {
                val competitorName = competitorNameInput(scanner)
                if (!competitors.contains(competitorName)) competitors.add(competitorName)
                else println("El participante ya existe.")
            }
            "2", "Borrar participante".lowercase() -> {
                val competitorName = competitorNameInput(scanner)
                if (competitors.contains(competitorName)) competitors.remove(competitorName)
                else println("El participante no existe.")
            }
            "3", "Mostrar todos los participantes".lowercase() -> showAllCompetitors(competitors)
            "4", "Lanzar sorteo".lowercase() -> {
                if (competitors.isNotEmpty()) {
                    val randomlySelectCompetitor = launchLottery(competitors)
                    println("Ha salido sorteado $randomlySelectCompetitor")
                    competitors.remove(randomlySelectCompetitor)
                } else println("La lista de participantes está vacía")
            }
            else -> println("Opción incorrecta. Ingrésela otra vez.")
        }
        boardOptions()
        userInput = scanner.nextLine().lowercase()
    }
    println("Hasta pronto!")

}

private fun launchLottery(competitors: List<String>) = competitors.random()

private fun showAllCompetitors(competitors: List<String>) = competitors.forEach { println(it) }

private fun competitorNameInput(scanner: Scanner): String {
    println("Ingrese nombre: ")
    return scanner.nextLine()
}

private fun boardOptions() {
    println("Seleccione una opción:\n" +
            "1-Agregar participante\n" +
            "2-Borrar participante\n" +
            "3-Mostrar todos los participantes\n" +
            "4-Lanzar sorteo\n" +
            "5-Salir\n")
}
