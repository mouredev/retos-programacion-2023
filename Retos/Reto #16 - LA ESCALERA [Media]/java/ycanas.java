public class ycanas {
    public static void drawStaircase(int steps) {
        if (steps > 0) {
            for (int i = 0; i < steps + 1; i++) {
                String draw = (i == 0) ? "_" : "_|";
                int decrement = ((steps * 2) + 1) - (2 * i);

                for (int j = 0; j < decrement - 1; j++){
                    System.out.print(" ");
                }

                System.out.println(draw);
            }
        }

        else if (steps < 0) {
            for (int i = 0; i < (steps * (- 1)) + 1; i++) {
                String draw = (i == 0) ? " _" : "|_";

                for (int j = 0; j < 2 * i; j++){
                    System.out.print(" ");
                }

                System.out.println(draw);
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
