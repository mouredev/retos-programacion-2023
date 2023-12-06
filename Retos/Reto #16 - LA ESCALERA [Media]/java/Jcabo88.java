import java.util.Scanner;

import static java.lang.Math.abs;

public class Jcabo88 {

    private static String createStep(int steps, String step) {
        return " ".repeat(steps).concat(step);
    }

    private static String downstairs(int steps) {
        String stair = "_\n";
        if (steps != 1) {
             stair = downstairs(steps - 1);
        }
        return stair.concat(createStep(steps, "|_")).concat("\n");
    }

    private static String upstairs(int steps, String res) {
        res = res.concat(createStep(steps, "_|")).concat("\n");
        if (steps != 0) {
            res = upstairs(steps - 1, res);
        }
        return res;
    }

    private static String upstairs(int steps) {
        return upstairs(steps - 1, createStep(steps, "_\n"));
    }

    public static void printStairs(int steps) {
        String result = "__";
        if (steps != 0) {
            result = steps > 0 ? upstairs(steps) : downstairs(abs(steps));
        }
        System.out.println(result);
    }


    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter number of stairs: ");
            printStairs(sc.nextInt());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }

    }
}