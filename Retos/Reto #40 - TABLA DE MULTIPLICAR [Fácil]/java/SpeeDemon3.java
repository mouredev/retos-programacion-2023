import java.util.Scanner;

/**
 * @author -> Antonio Ruiz Benito = speeDemon
 */
public class SpeeDemon3 {
    public static void main(String[] args) {

        /*
         * Crea un programa que sea capaz de solicitarte un número y se
         * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
         * - Debe visualizarse qué operación se realiza y su resultado.
         *   Ej: 1 x 1 = 1
         *       1 x 2 = 2
         *       1 x 3 = 3
         *       ...
         */

        System.out.println("Enter a number");

        Scanner sc = new Scanner(System.in);

        int num = sc.nextInt();

        for (int i = 1; i < 11; i++) {

            int result = num * i;

            System.out.println(num + " X " + i + " = " + result);

        }

    }
}