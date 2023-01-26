/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

import java.util.ArrayList;

public class mjordanaam {
    public static boolean isPrime(int number){
        if(number > 1){
            for(int i = 2; i < number; i++){
                if (number % i == 0){
                    return false;
                }
            }
            return true;
        }
        else return false;
    }

    public static int fibonacci(int number){
        if (number == 0){
            return 0;
        }
        else if (number == 1){
            return 1;
        }
        else{
            return fibonacci(number-1) + fibonacci(number-2);
        }
    }

    public static boolean isFibonacci(int number){
        ArrayList<Integer> sequence = new ArrayList<Integer>();
        sequence.add(fibonacci(0));
        int counter = 0;

        while(sequence.get(counter) < number){
            counter++;
            sequence.add(fibonacci(counter));
        }

        return sequence.get(counter) == number;
    }

    public static boolean isEven(int number){
        return number % 2 == 0;
    }


    public static String checkNumber(int number){
        String text;
        if(number > -1){
            text = number + " is ";

            if(!isPrime(number)){
                text += "not ";
            }
            text += "prime, ";

            if(!isFibonacci(number)){
                text += "is not ";
            }
            text += "fibonacci and is ";

            if(isEven(number)){
                text += "even";
            }
            else{
                text += "odd";
            }
        }
        else{
            text = "Negative number";
        }
        return text;
    }

    public static void main(String[] args) {
        System.out.println(checkNumber(2));
        System.out.println(checkNumber(7));
        System.out.println(checkNumber(8));
        System.out.println(checkNumber(16));
        System.out.println(checkNumber(17));
        System.out.println(checkNumber(0));
        System.out.println(checkNumber(89));
        System.out.println(checkNumber(97));
        System.out.println(checkNumber(100));
        System.out.println(checkNumber(1));
        System.out.println(checkNumber(-1));
    }
}
 