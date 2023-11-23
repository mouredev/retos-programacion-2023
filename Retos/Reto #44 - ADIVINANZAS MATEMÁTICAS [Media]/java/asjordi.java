import java.util.Random;
import java.util.Scanner;
import java.util.Timer;
import java.util.TimerTask;

public class MathRiddle {

    static boolean gameOn = true;
    static int correctAnswers = 0;
    static int num1Digits = 1;
    static int num2Digits = 1;
    static Random random = new Random();

    public static void main(String[] args) {
        while (gameOn) {
            int num1 = randomInt(num1Digits);
            int num2 = randomInt(num2Digits);
            char operation = randomOperation();

            int result;
            if (operation == '+') result = num1 + num2;
            else if (operation == '-') result = num1 - num2;
            else if (operation == '*') result = num1 * num2;
            else {
                while (num2 == 0) num2 = randomInt(num2Digits);
                result = num1 / num2;
            }

            String answer = inputWithTimeout(num1, num2, operation);

            if (!gameOn) break;
            else if (answer.equals(Integer.toString(result))) {
                System.out.println("Respuesta correcta!");
                correctAnswers++;

                if (correctAnswers % 5 == 0) {
                    if (correctAnswers % 2 == 0) num2Digits++;
                    else num1Digits++;
                }

            } else {
                System.out.println("Respuesta incorrecta!");
                gameOn = false;
            }
        }

        System.out.println("Juego finalizado. Has acertado " + correctAnswers + " cálculos.");
    }

    private static int randomInt(int digits) {
        return random.nextInt((int) Math.pow(10, digits));
    }

    private static char randomOperation() {
        char[] operations = {'+', '-', '*', '/'};
        return operations[random.nextInt(operations.length)];
    }

    private static String inputWithTimeout(int num1, int num2, char operation) {
        Timer timer = new Timer();
        timer.schedule(new TimerTask() {
            @Override
            public void run() {
                System.out.println("\n¡El tiempo ha finalizado! Pulsa enter.");
                gameOn = false;
            }
        }, 3000);

        String answer;
        try {
            System.out.print("¿Cuál es el resultado de " + num1 + " " + operation + " " + num2 + "? ");
            answer = new Scanner(System.in).nextLine();
        } finally {
            timer.cancel();
        }

        return answer;
    }

}
