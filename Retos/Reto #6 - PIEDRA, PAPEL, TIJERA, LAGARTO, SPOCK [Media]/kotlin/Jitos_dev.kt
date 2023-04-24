package reto6.kotlin

import java.util.concurrent.atomic.AtomicInteger

fun main() {
    val main = Jitos_dev()
    val PIEDRA = Jitos_dev.value.PIEDRA
    val TIJERA = Jitos_dev.value.TIJERA
    val PAPEL = Jitos_dev.value.PAPEL
    val LAGARTO = Jitos_dev.value.LAGARTO
    val SPOCK = Jitos_dev.value.SPOCK

    val game1winner1 = arrayOf(arrayOf(PIEDRA, TIJERA), arrayOf(TIJERA, PIEDRA), arrayOf(TIJERA, PAPEL))
    val game2winner1 = arrayOf(arrayOf(PIEDRA, LAGARTO), arrayOf(PAPEL, SPOCK), arrayOf(PAPEL, TIJERA), arrayOf(SPOCK, LAGARTO), arrayOf(PAPEL, PIEDRA))
    val game1winner2 = arrayOf(arrayOf(PIEDRA, LAGARTO), arrayOf(PAPEL, SPOCK), arrayOf(PAPEL, TIJERA), arrayOf(SPOCK, LAGARTO), arrayOf(PIEDRA, PAPEL))
    val game2winner2 = arrayOf(arrayOf(PIEDRA, TIJERA), arrayOf(TIJERA, PIEDRA), arrayOf(PAPEL, TIJERA))
    val gameTie1 = arrayOf(arrayOf(PIEDRA, TIJERA), arrayOf(TIJERA, PIEDRA), arrayOf(TIJERA, PAPEL), arrayOf(PAPEL, TIJERA))
    val gameTie2 = arrayOf(arrayOf(PIEDRA, LAGARTO), arrayOf(PAPEL, SPOCK), arrayOf(PAPEL, TIJERA), arrayOf(SPOCK, LAGARTO), arrayOf(PAPEL, PIEDRA), arrayOf(PIEDRA, PAPEL))

    println(main.startGame(game1winner1));
    println(main.startGame(game2winner1));
    println(main.startGame(game1winner2));
    println(main.startGame(game2winner2));
    println(main.startGame(gameTie1));
    println(main.startGame(gameTie2));
}

class Jitos_dev {

    fun startGame(values: Array<Array<value>>): String {
        val pointsPlayer1 = AtomicInteger(0)
        val pointsPlayer2 = AtomicInteger(0)

        values.forEach { arrValues ->

            val playerWinner: Int = winnerPlayer(arrValues);

            if (playerWinner == 1) {
                pointsPlayer1.getAndIncrement()

            } else if (playerWinner == 2) {
                pointsPlayer2.getAndIncrement()
            }
        }

        if (pointsPlayer1.get() == pointsPlayer2.get())
            return "The game ends in a tie";

        return if (pointsPlayer1.get() > pointsPlayer2.get()) "The winner is Player1" else "The winner is Player2";
    }

    /**
     * This method return one if the winner is the zero value of the array position. If the winner is the
     * one value of the array position return two
     * @param game array of two value
     * @return one or two
     */
    private fun winnerPlayer(game: Array<value>): Int {
        val PLAYER_1: value = game[0];
        val PLAYER_2: value = game[1];

        if (PLAYER_1 == value.PIEDRA) {
            return playerAgainstStone(PLAYER_2);

        } else if (PLAYER_1 == value.PAPEL) {
            return playerAgainstPaper(PLAYER_2);

        } else if (PLAYER_1 == value.TIJERA) {
            return playerAgainstScissors(PLAYER_2);

        } else if (PLAYER_1 == value.LAGARTO) {
            return playerAgainstLizard(PLAYER_2);

        } else if (PLAYER_1 == value.SPOCK){ //It´s spock because it´s last one
            return playerAgainstSpock(PLAYER_2);
        }

        return 0;
    }

    private fun playerAgainstSpock(PLAYER_2: value): Int {
        if (PLAYER_2 == value.PIEDRA)
            return 1;

        else if (PLAYER_2 == value.LAGARTO)
            return 2;

        else if (PLAYER_2 == value.PAPEL)
            return 2;

        else if (PLAYER_2 == value.TIJERA) {
            return 1;
        }
        //if equals value PLAYER_1 and PLAYER_2 return zero
        return 0;
    }

    private fun playerAgainstLizard(PLAYER_2: value): Int {
        if (PLAYER_2 == value.PIEDRA)
            return 2;

        else if (PLAYER_2 == value.TIJERA)
            return 2;

        else if (PLAYER_2 == value.PAPEL)
            return 1;

        else if (PLAYER_2 == value.SPOCK)
            return 1;

        return 0;
    }

    private fun playerAgainstScissors(PLAYER_2: value): Int{
        if (PLAYER_2 == value.PIEDRA)
            return 2;

        else if (PLAYER_2 == value.LAGARTO)
            return 1;

        else if (PLAYER_2 == value.PAPEL)
            return 1;

        else if (PLAYER_2 == value.SPOCK) {
            return 2;
        }
        return 0;
    }

    private fun playerAgainstPaper(PLAYER_2: value): Int {
        if (PLAYER_2 == value.PIEDRA)
            return 1;

        else if (PLAYER_2 == value.LAGARTO)
            return 2;

        else if (PLAYER_2 == value.TIJERA)
            return 2;

        else if (PLAYER_2 == value.SPOCK)
            return 1;

        return 0;
    }

    private fun playerAgainstStone(PLAYER_2: value): Int {
        if (PLAYER_2 == value.LAGARTO)
            return 1;

        else if (PLAYER_2 == value.TIJERA)
            return 1;

        else if (PLAYER_2 == value.SPOCK)
            return 2;

        else if (PLAYER_2 == value.PAPEL)
            return 2;

        return 0;
    }

    enum class value {
        PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK
    }
}