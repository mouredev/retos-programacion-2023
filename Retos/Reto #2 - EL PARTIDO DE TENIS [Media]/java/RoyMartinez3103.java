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

public class RoyMartinez3103 {

    public static void main(String[] args) {
        String[] secuencia = {"P1", "P2", "P1", "P1", "P1", "P2", "P1", "P1"};
        jugar(secuencia);
    }

    public static void jugar(String[] secuencia) {
        Integer pointsP1 = 0, pointsP2 = 0;

        for (String punto : secuencia) {
            if (punto.equals("P1")) {
                if (pointsP1.equals(30)) {
                    pointsP1 += 10;
                } else {
                    pointsP1 += 15;
                }
            } else {
                if (pointsP2.equals(30)) {
                    pointsP2 += 10;
                } else {
                    pointsP2 += 15;
                }
            }

            imprimeMarcador(pointsP1, pointsP2);

            if (pointsP1.equals(70) || pointsP2.equals(70)) {
                break;
            }
        }
    }

    public static void imprimeMarcador(Integer pointsP1, Integer pointsP2) {
        String marcadorP1 = pointsP1.equals(0) ? "Love" : pointsP1.toString();
        String marcadorP2 = pointsP2.equals(0) ? "Love" : pointsP2.toString();
        String resultado;

        if (pointsP1.equals(40) && pointsP2.equals(40)) {
            resultado = "Deuce";
        } else if (pointsP1.equals(55)) {
            resultado = "Ventaja P1";
        } else if (pointsP2.equals(55)) {
            resultado = "Ventaja P2";
        } else if (pointsP1.equals(70)) {
            resultado = "Ha ganado el P1";
        } else if (pointsP2.equals(70)) {
            resultado = "Ha ganado el P2";
        } else {
            resultado = marcadorP1 + " - " + marcadorP2;
        }
        System.out.println(resultado);

    }
}
