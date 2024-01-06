import java.util.HashMap;
import java.util.Scanner;

/**
 * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo
 * ha ganado.
 *
 * @author abel
 */
public class PartidoTennis {

    private int player1, player2;

    private HashMap<Integer, String> score;

    public int getPlayer1() {
        return player1;
    }

    public void setPlayer1(int player1) {
        this.player1 = player1;
    }

    public int getPlayer2() {
        return player2;
    }

    public void setPlayer2(int player2) {
        this.player2 = player2;
    }

    public HashMap<Integer, String> getScore() {
        return score;
    }

    public void setScore(HashMap<Integer, String> score) {
        this.score = score;
    }

    public PartidoTennis() {
        player1 = 0;
        player2 = 0;
        score = new HashMap<>();
        score.put(0, "Love");
        score.put(1, "15");
        score.put(2, "30");
        score.put(3, "40");
    }

    public boolean validInput(String input) {
        return "P1".equals(input) || "P2".equals(input);
    }

    public void calculateScore(String input) {
        if ("P1".equals(input)) {
            player1++;
        } else {
            player2++;
        }
    }

    public String playerMostScore() {
        String mayor;

        if (player1 > player2) {
            mayor = "P1";
        } else {
            mayor = "P2";
        }

        return mayor;
    }

    public void showScore() {
        if (player1 == player2 && player1>=3) {
            System.out.println("Deuce");
        } else if (Math.abs(player1 - player2) == 1 && player1 >= 3 && player2 >= 3) {
            System.out.println("Ventaja " + playerMostScore());
        } else if (winGame()) {
            System.out.println("Ha ganado el " + playerMostScore());
        } else {
            System.out.println(score.get(player1) + "-" + score.get(player2));
        }
    }

    public boolean winGame() {
        return Math.abs(player1 - player2) >= 2 && player1 >= 4 || player2 >= 4;
    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        PartidoTennis partidoTennis = new PartidoTennis();

        String input;
        do {
            
            do {
                System.out.println("¿Quién ganó el punto? - (P1/P2)");
                input = scan.nextLine();
                if (!partidoTennis.validInput(input)) {
                    System.err.println("Introduce un jugador válido");
                }
            } while (!partidoTennis.validInput(input));

            partidoTennis.calculateScore(input);

            partidoTennis.showScore();

        } while (!partidoTennis.winGame());
    }
}
