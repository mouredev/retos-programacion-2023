package reto_02;

/**
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo
 * ha ganado. El programa recibirá una secuencia formada por "P1" (Player 1) o
 * "P2" (Player 2), según quien gane cada punto del juego.
 *
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce"
 * (empate), ventaja. - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el
 * programa mostraría lo siguiente: 15 - Love 30 - Love 30 - 15 30 - 30 40 - 30
 * Deuce Ventaja P1 Ha ganado el P1 - Si quieres, puedes controlar errores en la
 * entrada de datos. - Consulta las reglas del juego si tienes dudas sobre el
 * sistema de puntos.
 *
 * @author jesus
 */

public class JesusWay69_2 {

    public static void main(String[] args) {

        String[] players = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"};
        String[] score = {"Love", "15", "30", "40", "Ventaja" , "Ganador"};
        
        int limit1 = 0;
        int limit2 = 0;
        String P1 = "Love";
        String P2 = "Love";
        System.out.printf("%6s %10s %10s\n", "PUNTO", "Player  1", "Player  2");
        System.out.printf("%6s %10s %10s\n", "------", "----------", "----------");
        System.out.printf("%6s %10s %10s\n", "Start", "     Love", "     Love");

        for (int i = 0; i < players.length; i++) {
        
            if ("P1".equals(players[i]) && !("30".equals(P1) && "40".equals(P2))) {
                limit1++;
                for (int j = 0; j <= limit1; j++) {
                    P1 = score[j];
                }

                System.out.printf("%6s %10s %10s\n", players[i], P1, P2);

            } else if ("P2".equals(players[i])&& !("40".equals(P1) && "30".equals(P2))) {
                limit2++;
                for (int k = 0; k <= limit2; k++) {
                    P2 = score[k];
                }
                System.out.printf("%6s %10s %10s\n", players[i], P1, P2);
            }
         
           
            else  {
                System.out.printf(" %-20s \n",  "  -----------Deuce----------");
                P1="";
                P2="";
                System.arraycopy(score, 3, score, 0 , 3);
                limit1=0;
                limit2=0;
            }
        }

    }

}
