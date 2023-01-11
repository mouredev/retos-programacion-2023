/*
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
 * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
 * gane cada punto del juego.
 *
 * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
 * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
 *   15 - Love
 *   30 - Love
 *   30 - 15
 *   30 - 30
 *   40 - 30
 *   Deuce
 *   Ventaja P1
 *   Ha ganado el P1
 * - Si quieres, puedes controlar errores en la entrada de datos.
 * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.
 */
import java.util.Scanner;
public class reto02_ElPartidoDeTenis {
    static boolean dimeMarcador(int intP1, int intP2) {
        final String[] STR_ARR_PUNTUACIONES = {"Love", "15", "30", "40"};
        int intDiferenciaPuntuacion;
        String strPuntuacion;

        if (intP1 == 3 && intP2 == 3) {
            System.out.println("Deuce"); //Para el primer 40 - 40
        } else if (intP1 >= 4 || intP2 >= 4) {
            intDiferenciaPuntuacion = intP1 - intP2;

            if (intDiferenciaPuntuacion == 0) {
                System.out.println("Deuce");
            } else if (intDiferenciaPuntuacion == 1) {
                System.out.println("Ventaja P1");
            } else if (intDiferenciaPuntuacion == -1) {
                System.out.println("Ventaja P2");
            } else if (intDiferenciaPuntuacion >= 2) {
                System.out.println("Ha ganado el P1");
                return true;
            } else {
                System.out.println("Ha ganado el P2");
                return true;
            }
        } else {
            strPuntuacion = STR_ARR_PUNTUACIONES[intP1] + " - "
                    + STR_ARR_PUNTUACIONES[intP2];
            System.out.println(strPuntuacion);
        }
        return false;
    }
    static String dimeJugador(Scanner scEntrada) {
        String strJugadorCheck;
        String strJugadorReturn;

        System.out.println("¿Quién ha ganado el punto? (P1 o P2)");
        strJugadorCheck = scEntrada.nextLine().toUpperCase();
        while (!strJugadorCheck.equals("P1") && !strJugadorCheck.equals("P2")) {
            System.out.println("Has introducido un jugador no válido (Introduce P1 o P2).");
            System.out.println("¿Quién ha ganado el punto? (P1 o P2)");
            strJugadorCheck = scEntrada.nextLine().toUpperCase();
        }
        strJugadorReturn = strJugadorCheck;

        return strJugadorReturn;
    }
    static void inicio() {
        Scanner scEntrada = new Scanner(System.in);
        int intPuntuacionP1 = 0;
        int intPuntuacionP2 = 0;
        boolean blnJuegoFinalizado = false;
        String strJugadorPunto;

        while(!blnJuegoFinalizado) {
            strJugadorPunto = dimeJugador(scEntrada);
            switch (strJugadorPunto) {
                case "P1" -> intPuntuacionP1++;
                case "P2" -> intPuntuacionP2++;
            }
            blnJuegoFinalizado = dimeMarcador(intPuntuacionP1, intPuntuacionP2);
        }
        scEntrada.close();
    }
    public static void main(String[] args) {
        inicio();
    }
}
