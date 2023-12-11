import java.util.HashMap;
import java.util.Map;

public class rearalf {

    public static String rockPaperScissorsLizardSpock(String[][] games) {
        int playerOne = 0;
        int playerTwo = 0;

        Map<String, String[]> rules = new HashMap<>();
        rules.put("rock", new String[] { "scissors", "lizard" });
        rules.put("paper", new String[] { "rock", "spock" });
        rules.put("scissors", new String[] { "paper", "lizard" });
        rules.put("lizard", new String[] { "spock", "paper" });
        rules.put("spock", new String[] { "rock", "scissors" });

        for (String[] game : games) {
            String playerOneGame = game[0];
            String playerTwoGame = game[1];

            if (!playerOneGame.equals(playerTwoGame)) {
                if (contains(rules.get(playerOneGame), playerTwoGame)) {
                    playerOne += 1;
                } else {
                    playerTwo += 1;
                }
            }
        }

        if (playerOne == playerTwo) {
            return "Tie";
        } else if (playerOne < playerTwo) {
            return "Player 1";
        } else {
            return "Player 2";
        }
    }

    private static boolean contains(String[] array, String value) {
        for (String element : array) {
            if (element.equals(value)) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        System.out.println(rockPaperScissorsLizardSpock(new String[][] { { "rock", "rock" } }));
        System.out.println(rockPaperScissorsLizardSpock(new String[][] { { "rock", "scissors" } }));
        System.out.println(rockPaperScissorsLizardSpock(new String[][] { { "scissors", "rock" } }));
        System.out.println(rockPaperScissorsLizardSpock(new String[][] {
                { "rock", "rock" }, { "rock", "rock" }, { "rock", "rock" }, { "rock", "rock" } }));
        System.out.println(rockPaperScissorsLizardSpock(new String[][] {
                { "spock", "rock" }, { "scissors", "paper" }, { "rock", "rock" }, { "lizard", "spock" } }));
    }

}
