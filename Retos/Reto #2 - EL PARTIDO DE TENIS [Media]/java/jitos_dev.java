package java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static java.jitos_dev.Player.P1;
import static .jitos_dev.Player.P2;

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
public class jitos_dev {

    public static void main(String[] args) {
        Player[] gameSequence = new Player[] { P1, P1, P2, P2, P1, P2, P1, P1 };
        Player[] gameSequence2 = new Player[] { P1, P1, P2, P2, P1, P2, P1, P2, P2, P2 };
        List<Marker> finalMarker = match(gameSequence2);
        finalMarker.forEach(System.out::println);
    }

    private static List<Marker> match(Player[] secuence) {
        // Lista de "Marcadores" para guardar los resultados
        List<Marker> markers = new ArrayList<>();
        // Lista de posibles puntuaciones del juego
        List<String> scores = Arrays.asList(scores());

        // Recorremos la secuencia de juego que nos pasan por parámetro
        for (Player player : secuence) {
            // Creamos un nuevo marcador para este juego
            Marker marker = new Marker();

            // Si "markers" no está vacía le damos el valor del último marcador a "marker"
            // Declaramos lastMarker para que no apunte al mismo objeto
            Marker lastMarker = markers.isEmpty() ? marker : markers.get(markers.size() - 1);
            marker.setScoreP1(lastMarker.getScoreP1());
            marker.setScoreP2(lastMarker.getScoreP2());

            // Le damos el nuevo valor al marcador
            if (player == P1) {
                String lastScore = lastMarker.getScoreP1();

                // Si tiene ventaja y ha ganado el punto gana el partido
                if (lastScore.equals("Ventaja P1")) {
                    marker.setScoreP1("Ha ganado el P1");
                    marker.setScoreP2("Ha ganado el P1");
                    markers.add(marker);
                    break;
                }

                // Si tiene Ventaja y ha perdido el punto le damos el valor de DEUCE a los dos
                if (lastScore.equals("Ventaja P2")) {
                    marker.setScoreP1("Deuce");
                    marker.setScoreP2("Deuce");
                    markers.add(marker);
                    continue;
                }

                // Almacenamos la nueva puntuación que es el valor que tiene la puntuación
                // actual más uno en el array
                String newScore = scores.get(scores.indexOf(lastScore) + 1);

                marker.setScoreP1(newScore);

                // Si es ventaja se lo modificamos a los dos
                if (marker.getScoreP1().startsWith("Ventaja")) {
                    marker.setScoreP1("Ventaja P1");
                    marker.setScoreP2("Ventaja P1");
                }

            } else {
                String lastScore = lastMarker.getScoreP2();

                // Si tiene ventaja y ha ganado el punto gana el partido
                if (lastScore.equals("Ventaja P2")) {
                    marker.setScoreP1("Ha ganado el P2");
                    marker.setScoreP2("Ha ganado el P2");
                    markers.add(marker);
                    break;
                }

                // Si tiene Ventaja y ha perdido el punto le damos el valor de DEUCE a los dos
                if (lastScore.equals("Ventaja P1")) {
                    marker.setScoreP1("Deuce");
                    marker.setScoreP2("Deuce");
                    markers.add(marker);
                    continue;
                }

                // Almacenamos la nueva puntuación que es el valor que tiene la puntuación
                // actual más uno en el array
                String newScore = scores.get(scores.indexOf(lastScore) + 1);

                marker.setScoreP2(newScore);

                // Si es ventaja se lo modificamos a los dos
                if (marker.getScoreP2().startsWith("Ventaja")) {
                    marker.setScoreP1("Ventaja P2");
                    marker.setScoreP2("Ventaja P2");
                }

            }

            // Si la puntuación es 40 40 le damos el valor de DEUCE
            if (marker.getScoreP1().equals("40") && marker.getScoreP2().equals("40")) {
                marker.setScoreP1("Deuce");
                marker.setScoreP2("Deuce");
            }

            // añadimos el marcador de este punto a la lista
            markers.add(marker);
        }

        return markers;
    }

    private static String[] scores() {
        return new String[] { "Love", "15", "30", "40", "Deuce", "Ventaja" };
    }

    public enum Player {
        P1, P2
    }

    static class Marker {
        private String scoreP1;
        private String scoreP2;

        public Marker() {
            this.scoreP1 = "Love";
            this.scoreP2 = "Love";
        }

        public String getScoreP1() {
            return scoreP1;
        }

        public void setScoreP1(String scoreP1) {
            this.scoreP1 = scoreP1;
        }

        public String getScoreP2() {
            return scoreP2;
        }

        public void setScoreP2(String scoreP2) {
            this.scoreP2 = scoreP2;
        }

        @Override
        public String toString() {
            if (scoreP1.equals("Deuce") && scoreP2.equals("Deuce"))
                return scoreP1;
            else if (scoreP1.startsWith("Ventaja") && scoreP2.startsWith("Ventaja"))
                return scoreP1;
            else if (scoreP1.startsWith("Ha ganado") && scoreP2.startsWith("Ha ganado"))
                return scoreP1;
            else
                return scoreP1.concat(" - ").concat(scoreP2);
        }
    }
}