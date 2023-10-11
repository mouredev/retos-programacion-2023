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

public class vandresca{
    public static void main(String[] args) {
        Scanner scanner =new Scanner(System.in);
        System.out.println("¿Qué tabla de multiplicar quieres?. Escribe un número: ");
        int number = scanner.nextInt();
        scanner.close();
        for(int i=1; i<=10; i++){
            System.out.printf("%d x %d = %d \n", number, i, number*i);
        }     
    }    
 }
