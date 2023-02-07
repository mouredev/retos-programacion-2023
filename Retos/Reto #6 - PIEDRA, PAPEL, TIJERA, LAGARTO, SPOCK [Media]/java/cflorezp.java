package reto6PiedraPapelTijera;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

public class cflorezp {

    public static void main(String[] args) {



        HashMap<String, List<String>> rules = new HashMap<>();

        rules.put("tijera", new ArrayList<>(Arrays.asList("papel", "lagarto")));
        rules.put("papel", new ArrayList<>(Arrays.asList("piedra", "spock")));
        rules.put("piedra", new ArrayList<>(Arrays.asList("lagarto", "tijera")));
        rules.put("lagarto", new ArrayList<>(Arrays.asList("spock", "papel")));
        rules.put("spock", new ArrayList<>(Arrays.asList("tijera", "piedra")));

        System.out.println(rules);

        String jugada = "tijera";
        List<String> points = new ArrayList<>();
        points = rules.get(jugada);
        if(points.get(0).equals(jugada) || points.get(1).equals("lagarto")){
            int player1 = 1;
            int player2 = 0;
            System.out.println(player1);
            System.out.println(player2);
        }


    }
}
