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


        int scorePlayer1 = 0;
        int scorePlayer2 = 0;
        String[][] intro = {{"piedra","tijera"}, {"tijera","tijera"}, {"papel","papel"}};
        for(int i = 0; i < intro.length; i++){
            for(int j = 0; j < 1; j++){
                List<String> values = rules.get(intro[i][j]);
                String valuePlayer2 = intro[i][1];
                if(intro[i][j].equals(valuePlayer2)){
                    continue;
                }
                if(values.contains(valuePlayer2)){
                    scorePlayer1 += 1;
                }else{
                    scorePlayer2 += 1;
                }
            }
        }

        System.out.println("Player 1: " + scorePlayer1);
        System.out.println("Player 2: " + scorePlayer2);







    }
}
