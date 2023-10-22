import java.util.Scanner;

public class ycanas {

    public static void tableOf(int number) {
        System.out.println();

        for (int i = 1; i < 11; i++) {
            int value = i * number;
            System.out.println(i + " X " + number + " = " + value);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("¿Que tabla desea consulta? : ");
        int number = sc.nextInt();
        tableOf(number);
    }
}
