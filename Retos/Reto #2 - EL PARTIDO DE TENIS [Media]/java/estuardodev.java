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
    * - Consulta las reglas del juego si tienes dudas sobre el sistema de unidades.   
*/
import java.util.HashMap;

public class estuardodev {
    public static void main(String[] args) {
        String[] plays = { "P1", "P1", "P2", "P1", "P2", "P2", "P2" };
        gameTennis(plays);
    }

    public static void gameTennis(String[] plays) {
        HashMap<Integer, String> points = new HashMap<>();
        points.put(0, "Love");
        points.put(1, "Deuce");

        int pointsP1 = 0;
        int pointsP2 = 0;

        for (String p : plays) {
            switch (p) {
                case "P1":
                    if (pointsP1 < 30) {
                        pointsP1 = pointsP1 + 15;
                    } else {
                        pointsP1 = pointsP1 + 10;
                    }
                    break;
                case "P2":
                    if (pointsP2 < 30) {
                        pointsP2 = pointsP2 + 15;
                    } else {
                        pointsP2 = pointsP2 + 10;
                    }
                    break;
            }

            if (pointsP1 == 0) {
                System.out.println(points.get(0) + " - " + pointsP2 + " - (Ventaja P2)");
            } else if (pointsP2 == 0) {
                System.out.println(pointsP1 + " - " + points.get(0) + " - (Ventaja P1)");
            } else if (pointsP1 == pointsP2) {
                System.out.println(points.get(1));
            } else {
                if (pointsP1 < pointsP2) {
                    System.out.println(pointsP1 + " - " + pointsP2 + " - (Ventaja P2)");
                } else {
                    System.out.println(pointsP1 + " - " + pointsP2 + " - (Ventaja P1)");
                }
            }
        }

        if (pointsP1 > pointsP2) {
            System.out.println("Ganador P1");
        } else if (pointsP2 < pointsP1) {
            System.out.println("Ganador P2");
        } else {
            System.out.println(points.get(1));
        }
    }
}
