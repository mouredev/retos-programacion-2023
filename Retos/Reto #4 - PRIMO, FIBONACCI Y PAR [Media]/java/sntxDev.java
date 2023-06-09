import java.io.BufferedReader;
import java.io.InputStreamReader;
/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

public class sntxDev {
    public static void main(String[] args) {
        BufferedReader entrada = new BufferedReader(new InputStreamReader(System.in));
        int n;
        try {
            System.out.print("Ingrese un número: ");
            n = Integer.valueOf(entrada.readLine());

            String res = n + isPrime(n) + "," + isFibonacci(n) + "," + isEven(n);
            System.out.println(res);
        } catch (Exception e) {
            System.out.println(e);
        }
    }

    public static boolean sequencePrime(int n) {
        for (int i = 2; i < n; i++) {
            if ((i == n) && (i % 2 == 0)) {
                return false;
            }
        }
        return true;
    }

    public static String isPrime(int n) {
        if (sequencePrime(n) || (n == 1) || (n == 2)) {
            return " is prime";
        }
        return " not prime";
    }

    public static int sequenceFibonacci(int n) {
        if (n == 0) {
            return 0;
        } else if (n == 1) {
            return 1;
        } else {
            return sequenceFibonacci(n - 1) + sequenceFibonacci(n - 2);
        }
    }

    public static String isFibonacci(int n) {
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sequenceFibonacci(i);
        }
        for (int num : arr) {
            if (num == n) {
                return " is fibonnaci";
            }
        }
        return " not fibonacci";
    }

    public static String isEven(int n) {
        if (n % 2 == 0) {
            return " is even";
        }
        return " not even";
    }
}
