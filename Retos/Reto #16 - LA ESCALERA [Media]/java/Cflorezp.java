package reto16Escalera;

import java.util.InputMismatchException;
import java.util.Scanner;

/*
 * Crea una función que dibuje una escalera según su número de escalones.
 * - Si el número es positivo, será ascendente de izquiera a derecha.
 * - Si el número es negativo, será descendente de izquiera a derecha.
 * - Si el número es cero, se dibujarán dos guiones bajos (__).
 *
 * Ejemplo: 4
 *         _
 *       _|
 *     _|
 *   _|
 * _|
 */
public class Cflorezp {

    public static void main(String[] args) {

        System.out.println("****** Pintor de Escaleras ******\n");
        System.out.print("¿Cuantos escalones desea que le dibuje? ");
        Scanner input = new Scanner(System.in);

        try {
            int numeroDeEscalones = input.nextInt();
            if (numeroDeEscalones > 0) {
                escaleraPositiva(numeroDeEscalones);
            } else if (numeroDeEscalones < 0) {
                escaleraNegativa(numeroDeEscalones);
            } else {
                System.out.println("__");
            }
        } catch (InputMismatchException e) {
            System.out.println("El valor ingresado no es un número válido, por lo tanto no se dibujará nada");
        }finally {
            input.close();
        }
    }

    public static void escaleraPositiva(int escalones) {
        for (int i = escalones; i >= 0; i--) {
            for (int j = 0; j < i; j++) {
                System.out.print("  ");
            }
            if (i == escalones) {
                System.out.println("_");
            } else {
                System.out.println("_|");
            }
        }
    }

    public static void escaleraNegativa(int escalones) {
        escalones = escalones * -1;
        for (int i = 0; i <= escalones; i++) {
            for (int j = 0; j < i; j++) {
                System.out.print("  ");
            }
            if (i == 0) {
                System.out.println(" _");
            } else {
                System.out.println("|_");
            }
        }
    }
}
