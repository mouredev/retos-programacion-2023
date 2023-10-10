package reto21PrimosGemelos;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

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
public class Cflorezp {

    public static void main(String[] args) {

        System.out.println("\n************************************");
        System.out.println("Calculador de numeros primos Gemelos");
        System.out.println("************************************\n");
        System.out.println("Por favor ingrese el rango de numeros que desea: ");
        Scanner init = new Scanner(System.in);
        String value = init.nextLine();

        if(validationOfNumber(value)){
            int number = Integer.valueOf(value);
            if(number < 5){
                System.out.println("El rango es muy pequeño por lo que no hay primos gemelos");
            }else{
                printTwins(twinsPrimes(primes(number)));
            }
        }

        init.close();
    }

    public static List<Integer> primes(int number){
        List<Integer> primes = new ArrayList<>();
        for(int i = 3; i <= number; i++ ){
            if(isPrime(i)){
                primes.add(i);
            }
        }
        return primes;
    }

    public static boolean isPrime(int number){
        int count = 0;
        for(int i = 2; i < number; i++){
            int result = 0;
            result = number % i;
            if(result == 0){
                count++;
            }
            if(count == 1){
                return false;
            }
        }
        return true;
    }
    public static List<Integer> twinsPrimes(List<Integer> numbers){
        List<Integer> twins = new ArrayList<>();
        int first = 0, second = 0;
        for(int i = 0; i < numbers.size(); i++){
            first = numbers.get(i);
            if((i + 1) < numbers.size()){
                second = numbers.get(i + 1);
                if((first + 2) == second){
                    twins.add(first);
                    twins.add(second);
                }
            }
        }
        return twins;
    }
    public static void printTwins(List<Integer> numbers){
        for (int i = 0; i < numbers.size(); i += 2) {
            int element1 = numbers.get(i);
            int element2 = numbers.get(i + 1);
            System.out.print("(" + element1 + ", " + element2 + "), ");
        }
    }

    public static boolean validationOfNumber(String number){
        if(!number.matches("[0-9]+")){
            System.out.println("El valor ingresado no es valido!!");
            return false;
        }
        return true;
    }
}
