package Reto4.Java;

import java.util.InputMismatchException;
import java.util.Scanner;

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */
public class vandresca {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int input;
        try{
            input = scanner.nextInt();
            System.out.println(makeMessage(input));
        }catch(InputMismatchException ime){

        }finally{
            scanner.close();
        }
    }

    private static String makeMessage(int input){
        StringBuilder message = new StringBuilder();
        message.append(String.valueOf(input));
        message.append(isPrime(input));
        message.append(isFibonacci(input));
        message.append(isEven(input));
        return message.toString();
    }


    private static String isPrime(int number){
        for(int i=2; i<number; i++){
            if(number%i==0) return " no es primo,";
        }     
        return " es primo,";
    }

    private static String isFibonacci(int number){
        int fibonnaci=1;
        int number1 = 0;
        int number2 = 1;
        while(fibonacci < number){
            fibonnaci =number1 + number2;
            number1= number2;
            number2= fibonacci;
        }
        return (fibonnaci == number)?" es fibonnaci,": " no es fibonnaci,";
    }

    private static String isEven(int number){
        return (number%2==0)?" es par.":" no es par.";
    }
}
