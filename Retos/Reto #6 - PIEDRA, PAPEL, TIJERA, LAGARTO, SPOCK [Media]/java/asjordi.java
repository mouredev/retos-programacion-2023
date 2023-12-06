import java.util.*;

public class RockPaperScissorsLizardSpock {

    public static void main(String[] args) {

        RockPaperScissorsLizardSpock r = new RockPaperScissorsLizardSpock();

        String[][] games = new String[][]{{"piedra", "tijera"}, {"tijera", "piedra"}, {"papel", "tijera"}};
//        String[][] games = new String[][]{{"piedra", "piedra"}};
//        String[][] games = new String[][]{{"piedra", "piedra"}, {"piedra", "piedra"}, {"piedra", "piedra"}, {"piedra", "piedra"}};
//        String[][] games = new String[][]{{"spock", "piedra"}, {"tijeras", "papel"}, {"piedra", "piedra"}, {"lagarto", "spock"}};

    }

    public String playGame(String[][] games) {

        int winsPlayerOne = 0;
        int winsPlayerTwo = 0;

        Map<String, String[]> rules = new HashMap<>();
        rules.put("piedra", new String[] {"tijera", "lagarto"});
        rules.put("papel", new String[] {"piedra", "spock"});
        rules.put("tijera", new String[] {"papel", "lagarto"});
        rules.put("lagarto", new String[] {"spock", "papel"});
        rules.put("spock", new String[] {"piedra", "tijera"});

        for (String[] g : games){

            String p1 = g[0];
            String p2 = g[1];

            if (!Objects.equals(p1, p2)) {

                String res = Arrays.toString(rules.get(p1));

                if (res != null && res.contains(p2)) {
                    winsPlayerOne ++;
                } else {
                    winsPlayerTwo ++;
                }
            }

        }

        return winsPlayerOne == winsPlayerTwo ? "Tie": winsPlayerOne > winsPlayerTwo ? "Player 1" : "Player 2";

    }

}
