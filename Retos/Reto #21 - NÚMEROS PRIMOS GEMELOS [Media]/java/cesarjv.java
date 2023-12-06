package org.example;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.IntStream;

/**
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
public class cesarjv {
    public static void main(String[] args) {
        Integer num=14;
        List<Integer> primeNumbers = IntStream.range(2, num).filter(App::isPrimeStream).boxed().toList();
        Map<Integer,Integer> res=new HashMap<>();
        int comparisonValue=primeNumbers.get(0);
        for(Integer x: primeNumbers){
            if(x-comparisonValue==2){
                res.put(comparisonValue,x);
            }
            comparisonValue=x;
        }
        res.forEach((k,v) -> System.out.println("("+k+", "+v+")"));
    }
    private static boolean isPrimeStream(int n) {
        return IntStream.range(2, n).noneMatch(i -> n % i == 0);
    }
}