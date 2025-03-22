
import java.util.Scanner;

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
public class RoyMartinez3103 {

    public static void main(String args[]) {
        Integer num, resFibo = 0;
        Scanner scan = new Scanner(System.in);

        System.out.println("Ingresa un número: ");
        num = scan.nextInt();
        esPrimo(num);
        esPar(num);
        resFibo = esFibonacci(num);
        if (resFibo != null) {
            System.out.println("ES Fibonacci");
        } else {
            System.out.println("NO es Fibonacci");
        }

    }

    static void esPrimo(Integer num) {
        boolean esPrimo = true;
        for (int i = 2; i < num; i++) {
            if (num % i == 0) {
                esPrimo = false;
            }
        }
        if (esPrimo) {
            System.out.println("SI es primo");
        } else {
            System.out.println("NO es primo");
        }
    }

    static void esPar(Integer num) {
        if (num % 2 == 0) {
            System.out.println("Es par");
        } else {
            System.out.println("NO es par");
        }
    }

    static Integer esFibonacci(Integer num) {
        //0, 1, 1, 2, 3, 5, 8, 13, ...
        Integer n0 = 0, n1 = 1, fibo;

        if (num.equals(n0) || num.equals(n1)) {
            return num; // Si el número es 0 o 1, es Fibonacci
        }

        while (true) {
            fibo = n0 + n1;

            if (fibo.equals(num)) {
                return num; // Si se encuentra el número, se retorna
            }

            if (fibo > num) {
                return null; // Si se pasa del número, se retorna null
            }

            n0 = n1;
            n1 = fibo;
        }
    }

}
