package reto4PrimoFibonacciPar;

import java.net.StandardSocketOptions;
import java.util.ArrayList;
import java.util.List;

public class cflorezp {

    public static void main(String[] args) {

        System.out.println(isFibonacci(-250));

    }

    public static String isPrime(int number) {
        if (number == 1 || number <= 0 || number == 4) return " no es primo";
        if(number != 2){
            for (int i = 2; i < number / 2; i++) {
                if (number % i == 0) return "no es primo";
            }
        }
        return "es primo";
    }

    public static String isFibonacci(int number){
        if(number == 1) return " es fibonacci";
        if(number >= 2){
            List<Integer> fibonnaci = new ArrayList<>();
            fibonnaci.add(1);
            fibonnaci.add(1);
            for(int i = 2; i <= number; i++){
                fibonnaci.add(fibonnaci.get(i-1) + fibonnaci.get(i-2));
                if(fibonnaci.contains(number)){
                    return " es fibonacci";
                } else if (!fibonnaci.contains(number) && fibonnaci.get(i) > number) {
                    break;
                }
            }
        }
        return " no es fibonacci";
    }
}
