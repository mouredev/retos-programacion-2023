package reto_40;
import java.util.Scanner;
/*
 * Crea un programa que sea capaz de solicitarte un número y se
 * encargue de imprimir su tabla de multiplicar entre el 1 y el 10.
 * - Debe visualizarse qué operación se realiza y su resultado.
 *   Ej: 1 x 1 = 1
 *       1 x 2 = 2
 *       1 x 3 = 3
 *       ... 
 */
public class JesusWay69 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese el número de la tabla de multiplicar: "); 
        int n = sc.nextInt();
        for (int i = 1; i <= 10; i++) 
            System.out.println(n + " X " + i + " = " + n * i);
    }
}
