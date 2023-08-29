import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Main {

    public static void main(String[] args) {
        String[] sequence = { "P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1" };
        TennisGame game1 = new TennisGame(sequence);

        String[] sequence2 = { "P1", "P1", "P2", "P2", "P1", "P2", "P3" };
        TennisGame game2 = new TennisGame(sequence2);
    }
}

class TennisGame {
    private final String[] sequence;
    private final String[] scoreValues = { "Love", "15", "30", "40" };
    private final Map<String, Integer> playerScores = new HashMap<>();
    private final StringBuilder gameOutput = new StringBuilder();
    private String errorMessage = "\nEntrada de datos no válida.";

    public TennisGame(String[] sequence) {
        this.sequence = sequence;

        if (isValidSequence()) {
            initializePlayerScores();
            gameOutput.append("P1       P2\n");
            startGame();
            System.out.println(getGameResult());
        } else {
            System.out.println(errorMessage);
        }
    }

    private void initializePlayerScores() {
        playerScores.put("P1", 0);
        playerScores.put("P2", 0);
    }

    private boolean isValidSequence() {
        long player1Count = Arrays.stream(sequence).filter("P1"::equals).count();
        long player2Count = Arrays.stream(sequence).filter("P2"::equals).count();

        if (sequence.length != player1Count + player2Count) {
            errorMessage += " La secuencia solo debe contener 'P1' o 'P2'.";
            return false;
        }

        if (Math.abs(player1Count - player2Count) < 2) {
            errorMessage += " La secuencia no tiene un ganador.";
            return false;
        }

        return true;
    }

    public void startGame() {
        for (String player : sequence) {
            playerScores.merge(player, 1, Integer::sum);

            if (playerScores.get("P1").equals(playerScores.get("P2"))) {
                gameOutput.append("Deuce\n");
            } else if (playerScores.get("P1") >= 4 || playerScores.get("P2") >= 4) {
                int scoreDifference = Math.abs(playerScores.get("P1") - playerScores.get("P2"));

                if (scoreDifference == 1) {
                    gameOutput.append("Ventaja ").append(getHighestScorePlayer()).append("\n");
                } else {
                    gameOutput.append("Ha ganado el ").append(getHighestScorePlayer()).append("\n");
                    return;
                }
            } else {
                gameOutput.append(scoreValues[playerScores.get("P1")])
                        .append("   -   ").append(scoreValues[playerScores.get("P2")])
                        .append("\n");
            }
        }
    }

    public String getGameResult() {
        return gameOutput.toString();
    }

    private String getHighestScorePlayer() {
        int highestScore = playerScores.entrySet()
                .stream()
                .max(Map.Entry.comparingByValue())
                .map(entry -> entry.getValue())
                .orElse(0);

        return playerScores.entrySet()
                .stream()
                .filter(entry -> entry.getValue() == highestScore)
                .map(Map.Entry::getKey)
                .findFirst()
                .orElse("");
    }
}
