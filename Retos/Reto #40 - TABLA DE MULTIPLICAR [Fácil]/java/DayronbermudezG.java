/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */

import java.util.Scanner;

public class DayronbermudezG {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        do {

            System.out.print("Ingrese un numero: ");
            int n = scanner.nextInt();
            System.out.println();

            for(int i=0;i<=10;i++) {

                System.out.println(n + " x " + i + " = " + n*i);
            }
            System.out.println();
        }while(true);   
    }
}
