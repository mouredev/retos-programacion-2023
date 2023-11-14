public class ycanas {
    public static void drawStaircase(int steps) {
        if (steps > 0) {
            for (int i = 0; i < steps + 1; i++) {
                String draw = (i == 0) ? "_" : "_|";
                int spaces = (steps * 2) - (2 * i);
                System.out.println(" ".repeat(spaces) + draw);
            }
        }

        else if (steps < 0) {
            for (int i = 0; i < (steps * (- 1)) + 1; i++) {
                String draw = (i == 0) ? " _" : "|_";
                System.out.println(" ".repeat((2 * i)) + draw);
            }
        }

        else {
            System.out.println("__");
        }
    }

    public static void main(String[] args) {
        System.out.println("\nAscendente:");
        drawStaircase(4);

        System.out.println("\nDescendente:");
        drawStaircase(-4);

        System.out.println("\n0:");
        drawStaircase(0);
    }
}
