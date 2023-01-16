package reto2;

import java.util.*;

import static reto2.jitos_dev.Player.*;
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
        Player[] gameSequence = new Player[]{P1, P1, P2, P2, P1, P2, P1, P1};
        Player[] gameSequence2 = new Player[]{P1, P1, P2, P2, P1, P2, P1, P2, P2, P2};
        List<Marker> finalMarker = match(gameSequence2);
        finalMarker.forEach(System.out::println);
    }

    private static List<Marker> match(Player[] secuence) {
        //Lista de "Marcadores" para devolver
        List<Marker> markers = new ArrayList<>();
        //Lista de posibles puntuaciones del juego
        List<Score> scores = Arrays.asList(scores());
        int positionInArray1 = 1;
        int positionInArray2 = 1;

        //Recorremos la secuencia de juego que nos pasan por parámetro
        for (Player player: secuence) {
            Marker marker = new Marker();

            //Si markers no está vacía le damos el valor del último marcador a "marker"
            if (!markers.isEmpty()) {
                Marker lastMarker = markers.get(markers.size() -1);
                marker.setScore1(lastMarker.getScore1());
                marker.setScore2(lastMarker.getScore2());
            }

            //Si ha ganado el jugador 1
            if (player == P1 && marker.getScore1().getValue().equals("Ventaja P1")) {
                Score winner = new Score("Ha ganado el P1");
                marker.setScore1(winner);
                marker.setScore2(winner);
                markers.add(marker);
                break;
            }

            //Si ha ganado el jugador 2
            if (player == P2 && marker.getScore2().getValue().equals("Ventaja P2")) {
                Score winner = new Score("Ha ganado el P2");
                marker.setScore1(winner);
                marker.setScore2(winner);
                markers.add(marker);
                break;
            }
            //Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
            //Le damos el nuevo valor al marcador
            if (player == P1) {
                //Le damos la nueva puntuación. Si es la última que es Ventaja le damos el valor de DEUCE
                if (marker.score1.getValue().contains("Ventaja P2")) {
                    marker.setScore1(new Score("Deuce"));
                    marker.setScore2(new Score("Deuce"));
                    //Retrocedemos una posición en el array para las dos puntuaciones
                    positionInArray2--;
                    positionInArray1--;
                } else {
                    marker.score1 = scores.get(positionInArray1);
                    positionInArray1++;
                }

                if (marker.score1.getValue().startsWith("Ventaja") || marker.score2.getValue().startsWith("Ventaja")) {
                    marker.setScore1(new Score("Ventaja P1"));
                    marker.setScore2(new Score("Ventaja P1"));
                    //Sumamos uno a la posición del player2 porque al player1 ya se la sumamos en el else
                    positionInArray2++;
                }

            } else {
                //Le damos la nueva puntuación
                if (marker.score2.getValue().contains("Ventaja P1")) {
                    marker.setScore1(new Score("Deuce"));
                    marker.setScore2(new Score("Deuce"));
                    //Retrocedemos una posición en el array para las dos puntuaciones
                    positionInArray1--;
                    positionInArray2--;
                } else {
                    marker.score2 = scores.get(positionInArray2);
                    positionInArray2++;
                }

                if (marker.score1.getValue().startsWith("Ventaja") || marker.score2.getValue().startsWith("Ventaja")) {
                    marker.setScore1(new Score("Ventaja P2"));
                    marker.setScore2(new Score("Ventaja P2"));
                    //Sumamos uno a la posición del player1 porque al player2 ya se la sumamos en el else
                    positionInArray1++;
                }

            }

            //Si la puntuación es 40 40 le damos el valor de DEUCE
            if (marker.getScore1().getValue().equals("40") && marker.getScore2().getValue().equals("40")) {
                marker.setScore1(new Score("Deuce"));
                marker.setScore2(new Score("Deuce"));
                positionInArray1++;
                positionInArray2++;
            }

            markers.add(marker);
        }

        return markers;
    }

    private static Score[] scores() {
        return new Score[]{new Score("Love"), new Score("15"), new Score("30"), new Score("40"), new Score("Deuce"), new Score("Ventaja")};
    }

    public enum Player {
        P1, P2
    }

    static class Score {
        private String value;

        public Score(String value) {
            this.value = value;
        }

        public String getValue() {
            return value;
        }

        public void setValue(String value) {
            this.value = value;
        }
    }

    static class Marker {
        private Score score1;
        private Score score2;

        public Marker() {
            this.score1 = new Score("Love");
            this.score2 = new Score("Love");
        }

        public Score getScore1() {
            return score1;
        }

        public void setScore1(Score score1) {
            this.score1 = score1;
        }

        public Score getScore2() {
            return score2;
        }

        public void setScore2(Score score2) {
            this.score2 = score2;
        }

        @Override
        public String toString() {
            if (score1.getValue().equals("Deuce") && score2.getValue().equals("Deuce"))
                return score1.getValue();
            else if (score1.getValue().startsWith("Ventaja") && score2.getValue().startsWith("Ventaja"))
                return score1.getValue();
            else if (score1.getValue().startsWith("Ha ganado") && score2.getValue().startsWith("Ha ganado"))
                return score1.getValue();
            else
                return score1.getValue().concat(" - ").concat(score2.getValue());
        }
    }
}