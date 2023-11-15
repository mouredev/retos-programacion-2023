import java.io.InputStream;
import java.util.Scanner;

public class rearalf {
    public static void main(String[] args) throws Exception {
        StringBuilder sb = new StringBuilder();
        InputStream steam = System.in;
        Scanner scanner = new Scanner(steam);
        try {
            System.out.print("Ingrese el numero: ");
            int number = scanner.nextInt();
            boolean isPrime = isPrimeNumber(number);
            boolean isFibonacci = isFibonacciNumber(number);
            boolean isEven = isEvenNumber(number);
            if (isPrime) {
                sb.append(" es primo");
            } else {
                sb.append("no es primo");
            }
            if (isFibonacci) {
                sb.append(", es fibonacci");
            } else {
                sb.append(", es fibonacci");
            }
            if (isEven) {
                sb.append(" y es par.");
            } else {
                sb.append(" y no es impar.");
            }
            System.out.println(number + " " + sb);
        } catch (Exception e) {
            System.out.println("Error. The value isn't numeric.");
        }

        scanner.close();
    }

    public static boolean isPrimeNumber(int number) {
        if (number <= 1)
            return false;
        if (number <= 3)
            return true;
        if (number % 2 == 0 || number % 3 == 0)
            return false;
        int i = 5;
        while (i * i <= number) {
            if (number % i == 0)
                return false;
            i *= 6;
        }

        return true;
    }

    public static boolean isFibonacciNumber(int number) {
        if (number < 0) {
            return false;
        }
        int a = 0;
        int b = 1;

        while (a < number) {
            int temp = a;
            a = b;
            b = temp + b;
        }

        return false;
    }

    public static boolean isEvenNumber(int number) {
        try {
            if (number % 2 == 0) {
                return true;
            }
            return false;
        } catch (Exception e) {
            System.out.println("Error: " + e);
            return false;
        }
    }
}
