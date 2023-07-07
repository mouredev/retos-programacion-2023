import java.util.ArrayList;
import java.util.Arrays;

public class asjordi {

    enum Player {
        P1,
        P2
    }

    public void generateScore(ArrayList<Player> points) {
        ArrayList<String> game = new ArrayList<>(Arrays.asList("Love", "15", "30", "40"));
        int playerOnePoints = 0;
        int playerTwoPoints = 0;
        boolean isFinished = false;
        boolean error = false;


        for (Player point : points) {

            error = isFinished;
            playerOnePoints += point == Player.P1 ? 1 : 0;
            playerTwoPoints += point == Player.P2 ? 1 : 0;

            if (playerOnePoints >= 3 && playerTwoPoints >= 3) {
                if (!isFinished && Math.abs(playerOnePoints - playerTwoPoints) <= 1){
                    if (playerOnePoints == playerTwoPoints) {
                        System.out.println("Deuce");
                    } else {
                        if (playerOnePoints > playerTwoPoints) {
                            System.out.println("Ventaja " + Player.P1);
                        } else {
                            System.out.println("Ventaja " + Player.P2);
                        }
                    }
                } else {
                    isFinished = true;
                }
            } else {
                if (playerOnePoints < 4 || playerTwoPoints < 4) {
                    System.out.println(game.get(playerOnePoints) + " - " + game.get(playerTwoPoints));
                } else {
                    isFinished = true;
                }

            }
        }

        if (error) {
            System.out.println("There was an error in the game!");
        } else {
            if (playerOnePoints > playerTwoPoints) {
                System.out.println(Player.P1 + " has won");
            } else {
                System.out.println(Player.P2 + " has won");
            }
        }
    }
}
