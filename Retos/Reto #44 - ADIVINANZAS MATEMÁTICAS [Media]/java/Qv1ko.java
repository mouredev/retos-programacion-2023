import java.util.Scanner;
import java.util.Timer;
import java.util.TimerTask;

public class Qv1ko {

    static boolean end = false;

    public static void main(String[] args) {
        riddle();   
    }

    private static void riddle() {

        int x = 1, y = 1, ope1 = 0, ope2 = 0, operation = 0, correct = 0;
        String[] operators = new String[] {"+", "-", "*", "/"};
        double result = 0;
        String answer = "";
        
        while (!end) {

            ope1 =  (int)(Math.random() * (int)Math.pow(10, x));
            ope2 = (int)(Math.random() * (int)Math.pow(10, y));

            operation = (int)(Math.random() * 4);

            if (operation == 0) {
                result = ope1 + ope2;
            } else if (operation == 1) {
                result = ope1 - ope2;
            } else if (operation == 2) {
                result = ope1 * ope2;
            } else if (operation == 3) {

                while (ope2 == 0) {
                    ope2 = (int)(Math.random() * (int)Math.pow(10, y));
                }

                result = ope1 / ope2;

            }

            answer = question(ope1, ope2, operators[operation]);

            if (end) {
                break;
            } else if (Double.parseDouble(answer) == result) {

                correct++;

                if (correct % 5 == 0) {
                    if (x > y) {
                        y++;
                    } else {
                        x++;
                    }
                }

            } else {
                end = true;
            }

            System.out.println(ope1 + " " + operators[operation] + " " + ope2 + " = " + result);

        }

        System.out.println("You got " + correct +  " questions correct");

    }

    private static String question(int num1, int num2, String operation) {

        Scanner sc = new Scanner(System.in);
        String answer = "";

        Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            public void run() {
                System.out.println("\nThe time is over");
                end = true;
            }
        }, 3000);

        try {
            System.out.print(num1 + " " + operation + " " + num2 + " = ");
            answer = sc.nextLine();
        } finally {
            timer.cancel();
        }

        return answer;

    }

}
