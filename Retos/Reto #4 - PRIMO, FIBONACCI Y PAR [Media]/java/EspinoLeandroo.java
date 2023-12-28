import java.util.Scanner;

public class EspinoLeandroo {

    public static void main(String[] args) {
        EspinoLeandroo espinoLeandroo = new EspinoLeandroo();

        Scanner sc = new Scanner(System.in);

        System.out.print("Ingresa Número: ");
        int n = sc.nextInt();

        System.out.print("El número " + n);
        if (espinoLeandroo.primo(n)) {
            System.out.print(" es primo, ");
        } else {
            System.out.print(" no es primo, ");
        }
        if (espinoLeandroo.esFibonacci(n)) {
            System.out.print("es fibonacci, ");
        } else {
            System.out.print("no es fibonacci, ");
        }
        if (espinoLeandroo.esPar(n)) {
            System.out.print("es par.");
        } else {
            System.out.print("es impar.");
        }

    }

    private boolean esPar(int n) {
        return n % 2 == 0;
    }

    private boolean esFibonacci(int n) {
        int num1 = 0, num2 = 1;
        int counter = 0;

        while (num1 <= n) {
            if (num1 == n) {
                return true;
            }

            int num3 = num2 + num1;
            num1 = num2;
            num2 = num3;
            counter = counter + 1;
        }
        return false;
    }

    private boolean primo(int n) {
        if (n <= 1)
            return false;

        for (int i = 2; i < n; i++)
            if (n % i == 0)
                return false;

        return true;
    }

}
