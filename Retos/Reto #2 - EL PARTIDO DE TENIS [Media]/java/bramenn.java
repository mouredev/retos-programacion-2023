
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

class Bramenn {

    public static void main(String[] args) {

        List<String> tennisSets = Arrays.asList("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1");
        // List<String> tennisSets = Arrays.asList("P1", "P2", "P2", "P2", "P1", "P2", "P1", "P1");
        // List<String> tennisSets = Arrays.asList("P1", "P2", "P2", "P2", "P1", "P2", "P1", "P2");

        Player player_1 = new Player("P1");
        Player player_2 = new Player("P2");

        TennisMatch theGame = new TennisMatch(player_1, player_2, tennisSets);

        theGame.runGame();
    }

}

class Player {

    private String name;
    private int score;

    public Player(String name) {
        this.name = name;
        this.score = 0;
    }

    public String getName() {
        return name;
    }

    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score += score;
    }

}

class TennisMatch {

    private Player player_1;
    private Player player_2;
    private Player winner;
    private List<String> tennisSets;

    static HashMap<Integer, String> tennisPoints;
    static {
        tennisPoints = new HashMap<>();
        tennisPoints.put(0, "Love");
        tennisPoints.put(1, "15");
        tennisPoints.put(2, "30");
        tennisPoints.put(3, "40");
    };

    public TennisMatch(Player player_1, Player player_2, List<String> tennisSets) {
        this.player_1 = player_1;
        this.player_2 = player_2;
        this.tennisSets = tennisSets;
    }

    public Player getPlayer_1() {
        return player_1;
    }

    public Player getPlayer_2() {
        return player_2;
    }

    public Player getWinner() {
        return winner;
    }

    public void setWinner(Player winner) {
        this.winner = winner;
    }

    public void runGame() {
        this.tennisNarrator();

    }

    public void tennisNarrator() {

        String advantageText = "Ventaja %s";
        String scoreText = "%s - %s";

        for (int tennisSet = 0; tennisSet < this.tennisSets.size(); tennisSet++) {

            Player player = this.getPlayerByName(this.tennisSets.get(tennisSet));

            String text = "";

            player.setScore(1);

            switch (tennisSet) {
                case 5:
                case 6:
                    player = this.getPlayerWithHighestScore();

                    if (player == null) {
                        text = "Deuce";
                    } else {
                        text = String.format(advantageText, player.getName());
                    }

                    break;

                case 7:
                    this.setWinner(this.getPlayerWithHighestScore());
                    break;
                default:
                    text = String.format(scoreText, tennisPoints.get(player_1.getScore()),
                            tennisPoints.get(player_2.getScore()));
                    break;
            }

            if (!text.isEmpty()) {
                System.out.println(text);
            }
        }

        try {
            System.out.println("Ha ganado el " + this.getWinner().getName());
        } catch (Exception e) {
            System.out.println("Deuce");
        }
    }

    public Player getPlayerWithHighestScore() {
        Player winner = null;
        if (this.player_1.getScore() > this.player_2.getScore()) {
            winner = player_1;
        } else if (this.player_1.getScore() < this.player_2.getScore()) {
            winner = player_2;
        }
        return winner;
    }

    public Player getPlayerByName(String name) {

        if (name == this.getPlayer_1().getName()) {
            return this.getPlayer_1();
        } else {
            return this.getPlayer_2();
        }
    }
}
