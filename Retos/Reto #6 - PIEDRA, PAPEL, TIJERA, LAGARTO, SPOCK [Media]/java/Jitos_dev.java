package reto6.java;

import java.util.Arrays;
import java.util.concurrent.atomic.AtomicInteger;

import static reto6.java.Jitos_dev.value.*;

public class Jitos_dev {
    /*Reto de piedra, papel, tiejera, lagarto, spock
    * Las tijeras cortan el papel, el papel cubre a la piedra, la piedra aplasta al lagarto, el lagarto envenena
    * a Spock, Spock destroza las tijeras, las tijeras decapitan al lagarto, el lagarto se come el papel,
    * el papel refuta a Spock, Spock vaporiza la piedra, y, como es habitual, la piedra aplasta las tijeras.*/

    /*
     * Crea un programa que calcule quien gana más partidas al piedra,
     * papel, tijera, lagarto, spock.
     * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
     * - La función recibe un listado que contiene pares, representando cada jugada.
     * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
     *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
     * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
     * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
     */

    public static void main(String[] args) {
        Jitos_dev main = new Jitos_dev();

        value[][] game1winner1 = {{PIEDRA, TIJERA}, {TIJERA, PIEDRA}, {TIJERA, PAPEL}};
        value[][] game2winner1 = {{PIEDRA, LAGARTO}, {PAPEL, SPOCK}, {PAPEL, TIJERA}, {SPOCK, LAGARTO}, {PAPEL, PIEDRA}};
        value[][] game1winner2 = {{PIEDRA, LAGARTO}, {PAPEL, SPOCK}, {PAPEL, TIJERA}, {SPOCK, LAGARTO}, {PIEDRA, PAPEL}};
        value[][] game2winner2 = {{PIEDRA, TIJERA}, {TIJERA, PIEDRA}, {PAPEL, TIJERA}};
        value[][] gameTie1 = {{PIEDRA, TIJERA}, {TIJERA, PIEDRA}, {TIJERA, PAPEL}, {PAPEL, TIJERA}};
        value[][] gameTie2 = {{PIEDRA, LAGARTO}, {PAPEL, SPOCK}, {PAPEL, TIJERA}, {SPOCK, LAGARTO}, {PAPEL, PIEDRA}, {PIEDRA, PAPEL}};

        System.out.println(main.startGame(game1winner1));
        System.out.println(main.startGame(game2winner1));
        System.out.println(main.startGame(game1winner2));
        System.out.println(main.startGame(game2winner2));
        System.out.println(main.startGame(gameTie1));
        System.out.println(main.startGame(gameTie2));
    }



    public String startGame(value[][] values) {
        AtomicInteger pointsPlayer1 = new AtomicInteger();
        AtomicInteger pointsPlayer2 = new AtomicInteger();

        Arrays.asList(values).forEach(arrValues -> {
            int playerWinner = winnerPlayer(arrValues);

            if (playerWinner == 1) {
                pointsPlayer1.getAndIncrement();

            } else if (playerWinner == 2){
                pointsPlayer2.getAndIncrement();
            }
        });

        if (pointsPlayer1.get() == pointsPlayer2.get())
            return "The game ends in a tie";

        return pointsPlayer1.get() > pointsPlayer2.get() ? "The winner is Player1" : "The winner is Player2";
    }

    /**
     * This method return one if the winner is the zero value of the array position. If the winner is the
     * one value of the array position return two
     * @param game array of two value
     * @return one or two
     */
    public int winnerPlayer(value[] game) {
        final value PLAYER_1 = game[0];
        final value PLAYER_2 = game[1];

        if (PLAYER_1 == PIEDRA) {
            return playerAgainstStone(PLAYER_2);

        } else if (PLAYER_1 == PAPEL) {
            return playerAgainstPaper(PLAYER_2);

        } else if (PLAYER_1 == TIJERA) {
            return playerAgainstScissors(PLAYER_2);

        } else if (PLAYER_1 == LAGARTO) {
            return playerAgainstLizard(PLAYER_2);

        } else if (PLAYER_1 == SPOCK){ //It´s spock because it´s last one
            return playerAgainstSpock(PLAYER_2);
        }

        return 0;
    }

    private int playerAgainstSpock(value PLAYER_2) {
        if (PLAYER_2 == PIEDRA)
            return 1;

        else if (PLAYER_2 == LAGARTO)
            return 2;

        else if (PLAYER_2 == PAPEL)
            return 2;

        else if (PLAYER_2 == TIJERA) {
            return 1;
        }
        //if equals value PLAYER_1 and PLAYER_2 return zero
            return 0;
    }

    private int playerAgainstLizard(value PLAYER_2) {
        if (PLAYER_2 == PIEDRA)
            return 2;

        else if (PLAYER_2 == TIJERA)
            return 2;

        else if (PLAYER_2 == PAPEL)
            return 1;

        else if (PLAYER_2 == SPOCK)
            return 1;

        return 0;
    }

    private int playerAgainstScissors(value PLAYER_2) {
        if (PLAYER_2 == PIEDRA)
            return 2;

        else if (PLAYER_2 == LAGARTO)
            return 1;

        else if (PLAYER_2 == PAPEL)
            return 1;

        else if (PLAYER_2 == SPOCK) {
            return 2;
        }
        return 0;
    }

    private int playerAgainstPaper(value PLAYER_2) {
        if (PLAYER_2 == PIEDRA)
            return 1;

        else if (PLAYER_2 == LAGARTO)
            return 2;

        else if (PLAYER_2 == TIJERA)
            return 2;

        else if (PLAYER_2 == SPOCK)
            return 1;

        return 0;
    }

    private int playerAgainstStone(value PLAYER_2) {
        if (PLAYER_2 == LAGARTO)
            return 1;

        else if (PLAYER_2 == TIJERA)
            return 1;

        else if (PLAYER_2 == SPOCK)
            return 2;

        else if (PLAYER_2 == PAPEL)
            return 2;

        return 0;
    }

    public enum value {
        PIEDRA, PAPEL, TIJERA, LAGARTO, SPOCK
    }
}
