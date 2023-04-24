import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

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

/**
 * The type Sebastian 01973.
 */
public class Sebastian01973 {

    /**
     * The constant players.
     */
    public static final String[] players = {"P1", "P2"};
    /**
     * The constant scores.
     */
    public static final String[] scores = {"Love", "15", "30", "40"};

    private ArrayList<String> sequence;
    private HashMap<Integer, String> pointsDictionary;
    private int countP1;
    private int countP2;

    /**
     * Instantiates a new Sebastian 01973.
     *
     * @param sequence the sequence
     */
    public Sebastian01973(ArrayList<String> sequence) {
        this.sequence = sequence;
        this.countP1 = 0;
        this.countP2 = 0;
        pointsDictionary = new HashMap<>();
        for (int i = 0; i < scores.length; i++) {
            pointsDictionary.put(i, scores[i]);
        }
    }

    /**
     * Este metodo va contando los puntos de los jugadores
     * en cada set del juego
     */
    public void countPoints() {
        for (String seq : this.sequence) {
            if (seq.equals(players[0])) {
                countP1++;
            } else if (seq.equals(players[1])) {
                countP2++;
            }
            System.out.println(gameTenis());
        }
    }

    /**
     * La logica del juego
     *
     * @return the string
     */
    public String gameTenis() {
        if (countP1 == 3 && countP2 == 3) { // Si ambos jugadores van empatados en el set 40 - 40
            return "Deuce";
        }
        if (countP1 > 3 || countP2 > 3) {
            if (countP1 == countP2) {
                return "Deuce";
            }
            if (countP1 > countP2 + 1) { // Si el jugador P1 lleva ventaja y anota otro set, pasa a ganar el set
                return "Ha ganado " + players[0];
            } else if (countP1 > countP2) { // Si estan en empate y el jugador P1 hace set, posa a ventaja
                return "Ventaja " + players[0];
            }
            if (countP2 > countP1 + 1) { // Si el jugador P2 lleva ventaja y anota otro set, pasa a ganar el set
                return "Ha ganado " + players[1];
            } else {
                return "Ventaja " + players[1]; // Si estan en empate y el jugador P1 hace set, posa a ventaja
            }
        } else {
            return (pointsDictionary.get(countP1) + " - " + pointsDictionary.get(countP2));
        }
    }

    /**
     * The entry point of application.
     *
     * @param args the input arguments
     */
    public static void main(String[] args) {
        String[] test = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"};
        String[] test1 = {"P1", "P1", "P2", "P2", "P1", "P2", "P2", "P2"};
        String[] test2 = {"P1", "P1", "P1", "P1", "P1"};
        String[] test3 = {"P1", "P1", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2"};
        ArrayList<String> sequence = new ArrayList<>(List.of(test));
        //sequence.forEach(System.out::println);
        Sebastian01973 sebastian01973 = new Sebastian01973(sequence);
        sebastian01973.countPoints();
    }
}
