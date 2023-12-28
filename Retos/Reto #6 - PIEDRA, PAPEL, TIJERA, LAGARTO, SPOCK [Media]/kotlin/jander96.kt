package com.example.retosdeprogramacion2023
/*
* Fuente de reglas:
* https://bigbangtheory.fandom.com/es/wiki/Piedra,_Papel,_Tijera,_Lagarto_o_Spock#:
* ~:text=Piedra%2C%20Papel%2C%20Tijera%2C%20Lagarto%20o%20Spock%20es%20una,
* %28formado%20por%20la%20mano%20Vulcana%20de%20Star%20Trek%29.*/

fun main() {
val log= listOf((Power.Tijera to Power.Papel),(Power.Papel to Power.Piedra),
(Power.Tijera to Power.Lagarto))
    println(simulateGame(log))
}

fun simulateGame(gameLog: List<Pair<Power, Power>>): String {

    var pointsPlayer1 = 0
    var pointsPlayer2 = 0
    for (register in gameLog) {
        when (register) {
            (Power.Tijera to Power.Papel) -> pointsPlayer1++
            (Power.Papel to Power.Piedra) -> pointsPlayer1++
            (Power.Piedra to Power.Tijera) -> pointsPlayer1++
            (Power.Piedra to Power.Lagarto) -> pointsPlayer1++
            (Power.Lagarto to Power.Spock) -> pointsPlayer1++
            (Power.Spock to Power.Tijera) -> pointsPlayer1++
            (Power.Tijera to Power.Lagarto) -> pointsPlayer1++
            (Power.Lagarto to Power.Papel) -> pointsPlayer1++
            (Power.Papel to Power.Spock) -> pointsPlayer1++
            (Power.Spock to Power.Piedra) -> pointsPlayer1++
            else -> pointsPlayer2++


        }
    }
    return if (pointsPlayer1 > pointsPlayer2) "Payer1"
    else if (pointsPlayer2 > pointsPlayer1) "Player2"
    else "Empate"
}

sealed class Power {
    object Piedra : Power()
    object Papel : Power()
    object Tijera : Power()
    object Lagarto : Power()
    object Spock : Power()
}
