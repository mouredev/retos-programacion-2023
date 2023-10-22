import java.util.Scanner;

public class rearalf {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);

        int shifts = 0;
        int p1 = 0;
        int p2 = 0;

        do {
            System.out.print("The point is (P1 or P2): ");
            String input = scanner.next();

            if (input.equals("P1")) {
                p1++;
                shifts++;
            } else if (input.equals("P2")) {
                p2++;
                shifts++;
            } else if (input != "P1" || input != "P2") {
                System.out.println("Invalid input");
            }

            System.out.println(GetPoint(p1) + " - " + GetPoint(p2));

        } while (shifts < 6);

        System.out.println("");
        if (p1 == 3 && p2 == 3) {
            System.out.println(GetPoint(p1) + " - " + GetPoint(p2));
            System.out.println("Deuce");
        } else if (p1 > p2) {
            System.out.println(GetPoint(p1) + " - " + GetPoint(p2));
            System.out.println("Ventaja P1");
            System.out.println("Ha ganado el P1");
        } else if (p1 < p2) {
            System.out.println(GetPoint(p1) + " - " + GetPoint(p2));
            System.out.println("Ventaja P2");
            System.out.println("Ha ganado el P2 ");
        }
        System.out.println("");

        scanner.close();
    }

    public static String GetPoint(int point) {
        String textPoint = "";
        switch (point) {
            case 0:
                textPoint = "Love";
                break;
            case 1:
                textPoint = "15";
                break;
            case 2:
                textPoint = "30";
                break;
            case 3:
                textPoint = "40";
                break;
            default:
                break;
        }
        return textPoint;
    }
}
