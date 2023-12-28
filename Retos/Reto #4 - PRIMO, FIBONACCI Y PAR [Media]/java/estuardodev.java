/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

import java.util.Scanner;

public class estuardodev {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Ingresa un número para verificar si es primo, fibonacci y par: ");
        try {
            int valor = scanner.nextInt();
            verificar(valor);
        } catch (Exception ex) {
            System.out.println("Ingresa valores válidos.");
        }

        scanner.close();
    }

    public static void verificar(int dato) {
        System.out.println(dato + " " + esPrimo(dato) + ", " + esFibonacci(dato) + " y " + parImpar(dato));
    }

    public static String parImpar(int dato) {
        return dato % 2 == 0 ? "es par" : "es impar";
    }

    public static String esPrimo(int numero) {
        if (numero <= 1)
            return "no es primo";

        for (int i = 2; i <= Math.sqrt(numero); i++) {
            if (numero % i == 0)
                return "no es primo";
        }

        return "es primo";
    }

    public static String esFibonacci(int dato) {
        int a = 0;
        int b = 1;
        int contador = 0;

        while (contador < 1000) {
            int temp = a + b;
            a = b;
            b = temp;

            if (a == dato) {
                return "fibonacci";
            }
            contador++;
        }

        return "no es fibonacci";
    }
}
