/*
 * Crea un programa que encuentre y muestre todos los pares de números primos
 * gemelos en un rango concreto.
 * El programa recibirá el rango máximo como número entero positivo.
 *
 * - Un par de números primos se considera gemelo si la diferencia entre
 *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
 *
 * - Ejemplo: Rango 14
 *   (3, 5), (5, 7), (11, 13)
 */

import java.util.ArrayList;
import java.util.List;

public class LilyMilano {

    public static void main(String[] args) {

        int max = 33;

        List<List<Integer>> twins = getPrimeTwins(max);

        System.out.println(twins);  // [[3, 5], [5, 7], [11, 13], [17, 19], [29, 31]]

    }

    public static List<List<Integer>> getPrimeTwins(int max) {

        List<List<Integer>> twins = new ArrayList<>();

        for (int i = 2; i <= max; i++) {
            if (isPrime(i) && isPrime(i + 2)) {
                twins.add(List.of(i, i + 2));
            }
        }

        return twins;

    }

    public static boolean isPrime(int num) {
        if (num <= 1) return false;
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) return false;
        }
        return true;
    }

}
