public class Ladder {
    private static String drawStep(int num) {
        if (num > 0) {
            return "_|";
        } else {
            return "|_";
        }
    }

    private static String drawSpace() {
        return "  ";
    }

    public static void drawLadder(int num) {
        if (num == 0) {
            System.out.println("__");
        }
        if (num > 0) {
            int absNum = Math.abs(num);
            for (int i = 0; i <= num; i++) {
                if (num == absNum) {
                    System.out.println(drawSpace().repeat(absNum) + "_");
                    absNum--;
                } else {
                    String line = drawSpace().repeat(absNum) + drawStep(num);
                    System.out.println(line);
                    absNum--;
                }
            }
        }
        if (num < 0) {
            int aux = 0;
            for (int i = 0; i <= Math.abs(num); i++) {
                if (num == aux) {
                    System.out.println("_");
                } else {
                    String line = drawSpace().repeat(aux) + drawStep(num);
                    System.out.println(line);
                }
                aux++;
            }
        }
    }
}