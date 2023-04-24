import java.util.Map;
import java.util.Scanner;

public class Amartellram {

    public static Map<Integer, String> POINTS_MAPPER = Map.of(
            0, "Love",
            1, "15",
            2, "30",
            3, "40");

    public static void main(String[] args) {

        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Ingrese secuencia de juego: ");
            String sequence = scanner.nextLine();
            callSequence(sequence);
        }

        //Additional Sample 1
        System.out.println("\nTest Sample 1");
        String test = "P1, P1 ,P2, P2, P1, P2, P2, P2";
        System.out.println(test);
        callSequence(test);

        //Additional Sample 2
        System.out.println("\nTest Sample 2");
        String test2 = "P1, P1, P1, P1";
        System.out.println(test2);
        callSequence(test2);

        // Additional Sample 3
        System.out.println("\nTest Sample 3");
        String test3 = "P1, P1, P2, P2, P1, P2, P1, P2, P2, P2";
        System.out.println(test3);
        callSequence(test3);


    }

    static void callSequence(String sequence) {
        String[] points = sequence.trim().split(",");

        int pointsP1 = 0;
        int pointsP2 = 0;

        for (String point : points) {
            if ("P1".equals(point.trim())) pointsP1++;
            if ("P2".equals(point.trim())) pointsP2++;
            System.out.println(getPointName(pointsP1, pointsP2));
        }

        System.out.println("========= End of Game =========");
    }

    public static String getPointName(int pointsP1, int pointsP2) {
        int max = Math.max(pointsP1, pointsP2);
        int min = Math.min(pointsP1, pointsP2);


        if (min < 3 && max <= 3) {
            return POINTS_MAPPER.get(pointsP1) + " - " + POINTS_MAPPER.get(pointsP2);
        }

        if (max == min) {
            return "Deuce";
        } else {
            String playerMax = max == pointsP1 ? "P1" : "P2";
            if (max - min >= 2)
                return playerMax + " ha ganado";
            else
                return "Ventaja " + playerMax;
        }
    }
}
