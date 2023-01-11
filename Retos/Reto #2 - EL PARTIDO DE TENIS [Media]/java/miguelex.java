import java.util.*;

public class miguelex {

    public static void main(String[] args) {
        TennisMatch(Arrays.asList("P1", "P1", "P2", "P2", "P1", "P2", "P1", "P1"));
        TennisMatch(Arrays.asList("P1", "P1", "P1", "P2", "P2", "P2", "P1", "P2", "P1", "P2", "P2", "P2"));
    }

    private static void TennisMatch(List<String> players) {
        int p1Points = 0;
        int p2Points = 0;

        for (String player : players) {
            if (player.equals("P1")) {
                p1Points++;
            } else if (player.equals("P2")) {
                p2Points++;
            } else {
                System.out.println("Error en el tanteo");
                return;
            }

            if (p1Points == 4 && p2Points == 4) {
                p1Points = 3;
                p2Points = 3;
            }

            PrintScore(p1Points, p2Points);
        }
    }

    private static void PrintScore(int P1, int P2) {
        List<String> score = Arrays.asList("Love", "15", "30", "40");

        if ((P1 == P2) && (P1 == 3)) {
            System.out.println("\tDeuce");
        } else if ((P1 == 4) && (P2 == 3)) {
            System.out.println("\tVentaja P1");
        } else if ((P2 == 4) && (P1 == 3)) {
            System.out.println("\tVentaja P2");
        } else if ((P1 == 5) && (P1 - P2 == 2)) {
            System.out.println("\tGana P1");
        } else if ((P2 == 5) && (P2 - P1 == 2)) {
            System.out.println("\tGana P2");
        } else {
            System.out.println(String.format("P1:\t %s - %s \t:P2", score.get(P1), score.get(P2)));
        }
    }

}
