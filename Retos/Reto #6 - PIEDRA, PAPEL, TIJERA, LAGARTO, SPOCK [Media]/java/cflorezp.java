package reto6PiedraPapelTijera;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

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
public class cflorezp {

    public static void main(String[] args) {

        String[][] play = {{"piedra","papel"}, {"tijera","papel"}, {"papel","piedra"}};

        System.out.println(theGame(play));

    }

    public static String theGame(String[][] intro){
        HashMap<String, List<String>> rules = new HashMap<>();
        rules.put("tijera", new ArrayList<>(Arrays.asList("papel", "lagarto")));
        rules.put("papel", new ArrayList<>(Arrays.asList("piedra", "spock")));
        rules.put("piedra", new ArrayList<>(Arrays.asList("lagarto", "tijera")));
        rules.put("lagarto", new ArrayList<>(Arrays.asList("spock", "papel")));
        rules.put("spock", new ArrayList<>(Arrays.asList("tijera", "piedra")));

        int scorePlayer1 = 0;
        int scorePlayer2 = 0;
        for(int i = 0; i < intro.length; i++){
            for(int j = 0; j < 1; j++) {
                List<String> values = rules.get(intro[i][j]);
                String valuePlayer2 = intro[i][1];
                if (intro[i][j].equals(valuePlayer2)) {
                    continue;
                }
                if (values.contains(valuePlayer2)) {
                    scorePlayer1 += 1;
                } else {
                    scorePlayer2 += 1;
                }
            }
        }
        if(scorePlayer1 > scorePlayer2){
            return "¡¡¡¡Player 1 Wins!!!!";
        } else if (scorePlayer2 > scorePlayer1) {
            return "¡¡¡¡Player 2 Wins!!!!";
        }
        return "¡¡Tie!!";
    }
}
