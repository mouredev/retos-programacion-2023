import java.util.InputMismatchException;
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
public class willbipo{
    public static void main(String[] args){
        try {
            Scanner scanner = new Scanner(System.in);
            System.out.print("Ingrese el numero de la tabla deseada: ");
            int number = scanner.nextInt();
            imprimeTabla(number);
        } catch (InputMismatchException e) {
            System.out.println("Inserte un numero entero valido");
        }
        
    }

    public static void imprimeTabla(int number){
            for (int i = 1; i <= 10; i++) {
                System.out.println(number + " x " + i + " = " + number * i );
            }
    }

    
}