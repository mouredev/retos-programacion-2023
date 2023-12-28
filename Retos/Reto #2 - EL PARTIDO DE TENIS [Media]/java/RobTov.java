import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;

class RobTov {

    public static void main(String[] args) {
        String[] sequence = { "P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1" };
        TennisGame game1 = new TennisGame(sequence);

        String[] sequence2 = { "P1", "P1", "P2", "P2", "P1", "P2", "P3" };
        TennisGame game2 = new TennisGame(sequence2);
    }
}

class TennisGame {
    private final String[] sequece;

    private final String[] scoreValues = { "Love", "15", "30", "40" };
    private final HashMap<String, Integer> playerScores = new HashMap<>();
    private final StringBuilder gameOutput = new StringBuilder();
    private String errorMessage = "\nEntrada de datos no valida.";

    public TennisGame(String[] sequence) {
        this.sequece = sequence;

        if (this.isValidSequence()) {
            this.playerScores.put("P1", 0);
            this.playerScores.put("P2", 0);

            this.gameOutput.append("P1       P2\n");
            this.startGame();
            System.out.println(this.getGameResult());
        } else {
            System.out.println(errorMessage);
        }

    }
    private boolean isValidSequence() {
        List<String> seqToList = Arrays.asList(this.sequece);
        int player1Count = seqToList.stream().filter(s -> s.equals("P1")).toArray().length;
        int player2Count = seqToList.stream().filter(s -> s.equals("P2")).toArray().length;
        boolean isValid = true;

        if (this.sequece.length != player1Count + player2Count) {
            this.errorMessage += "La secuencia solo debe contener 'P1' o 'P2.";
            isValid = false;
        }
        if (!(player1Count >= player2Count + 2 || player2Count >= player1Count + 2)) {
            this.errorMessage += "La secuencia no tiene un ganador.";
            isValid = false;
        }
        return isValid;
    }

    public void startGame() {

        for (String player : this.sequece) {
            this.playerScores.merge(player, 1, Integer::sum);

            if (this.playerScores.get("P1") >= 3 && this.playerScores.get("P1").equals(this.playerScores.get("P2"))) {
                this.gameOutput.append("Deuce\n");
            } else if (this.playerScores.get("P1") >= 4 || this.playerScores.get("P2") >= 4) {
                if (
                        this.playerScores.get("P1") == this.playerScores.get("P2") + 1
                        || this.playerScores.get("P2") == this.playerScores.get("P1") + 1
                ) {
                    this.gameOutput.append("Ventaja ").append(this.getHighestScorePlayer()).append("\n");
                } else {
                    this.gameOutput.append("Ha ganado el ")
                            .append(this.getHighestScorePlayer()).append("\n");
                    return;
                }
            }  else if (this.playerScores.get("P1") <= 3 && this.playerScores.get("P2") <= 3) {
                this.gameOutput.append(this.scoreValues[this.playerScores.get("P1")])
                        .append("   -   ").append(this.scoreValues[this.playerScores.get("P2")])
                        .append("\n");
            }
         }

        System.out.println(this.playerScores);
    }

    public String getGameResult() {
        return this.gameOutput.toString();
    }

    private String getHighestScorePlayer() {
        int hiValue =  Collections.max(this.playerScores.values());
        return this.playerScores.get("P1") == hiValue ? "P1" : "P2";
    }
}