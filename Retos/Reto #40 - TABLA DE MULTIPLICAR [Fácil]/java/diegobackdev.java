import java.util.Scanner;

/* RETO 40: TABLA DE MULTIPLICAR
 * Crea un programa que sea capaz de solicitarte un número y se encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */

class diegobackdev {
    public static void main(String[] args) {
        Scanner read = new Scanner(System.in);
        System.out.print("Input a number: ");
        int number = read.nextInt();

        for (int i = 1; i<=10; i++) {
            System.out.println(number + " x " + i + " = " + number*i);
        }
    }

}