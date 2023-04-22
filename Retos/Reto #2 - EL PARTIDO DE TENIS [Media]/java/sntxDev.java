import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Map;

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

public class sntxDev {
    public static char l = 'a';
    public static String a = "P1", b = "P2";
    public static ArrayList<String> secuencia = new ArrayList<String>();
    public static Map<Integer, String> puntos = Map.of(
            0, "Love",
            1, "15",
            2, "30",
            3, "40");

    public static void main(String[] args) {
        BufferedReader entrada = new BufferedReader(new InputStreamReader(System.in));
        try {
            while ((l == 'a') || (l == 'b')) {
                System.out.print("a: Player 1, b: Player 2, (Cualquier otro caracter finaliza el programa): ");
                l = entrada.readLine().charAt(0);

                cargarArr(secuencia, b, a);
            }
            imprimirArr(secuencia);
            llamarSecuencia(secuencia);
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    static void cargarArr(ArrayList<String> list, String opcion1, String opcion2) {
        if (l == 'a') {
            secuencia.add(a);
        } else if (l == 'b') {
            secuencia.add(b);
        }
    }

    static void imprimirArr(ArrayList<String> list) {
        System.out.print("| ");
        for (int i = 0; i < list.size(); i++) {
            System.out.print(list.get(i) + " | ");
        }
        System.out.println("");
    }

    static void llamarSecuencia(ArrayList<String> puntos) {
        int puntosP1 = 0;
        int puntosP2 = 0;

        for (String punto : puntos) {
            if ("P1".equals(punto.trim())) {
                puntosP1++;
            }
            if ("P2".equals(punto.trim())) {
                puntosP2++;
            }
            System.out.println(ganador(puntosP1, puntosP2));
        }
        System.out.println("Juego terminado");
    }

    public static String ganador(int puntosP1, int puntosP2) {
        int max = Math.max(puntosP1, puntosP2);
        int min = Math.min(puntosP1, puntosP2);

        if ((min < 3) && (max < 4)) {
            return puntos.get(puntosP1) + " - " + puntos.get(puntosP2);
        }

        if (max == min) {
            return "Deuce";
        } else {
            String ganador = (max == puntosP1 ? "P1" : "P2");
            if ((max - min) >= 2) {
                return ganador + " ha ganado";
            } else {
                return "Ventaja " + ganador;
            }
        }
    }
}