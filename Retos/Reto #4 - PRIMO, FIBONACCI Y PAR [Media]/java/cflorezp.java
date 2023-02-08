package reto4PrimoFibonacciPar;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class cflorezp {

    public static void main(String[] args) {

        System.out.println("***************** VALIDADOR DE PRIMO, FIBONACCI Y PAR *****************");
        int flag = 1;
        Scanner input = new Scanner(System.in);
        do{
            System.out.println("Por favor ingrese un número: ");
            int number = input.nextInt();
            input.nextLine();

            System.out.println("El numero " + number + isPrime(number) + isFibonacci(number) + isPar(number) + "\n");

            System.out.println("¿Desea verificar otro numero? (Y/N): ");
            String continua = input.nextLine();
            flag = continua.equals("Y") || continua.equals("y") ? 1 : 0;

        }while(flag == 1);

        System.out.println("\nHemos finalizado, ¡¡Gracias por usar esta aplicación!!");


    }

    public static String isPrime(int number) {
        if (number == 1 || number <= 0 || number == 4) return " no es primo,";
        if(number != 2){
            for (int i = 2; i < number / 2; i++) {
                if (number % i == 0) return " no es primo,";
            }
        }
        return " es primo,";
    }

    public static String isFibonacci(int number){
        if(number == 1) return " es fibonacci,";
        if(number >= 2){
            List<Integer> fibonnaci = new ArrayList<>();
            fibonnaci.add(1);
            fibonnaci.add(1);
            for(int i = 2; i <= number; i++){
                fibonnaci.add(fibonnaci.get(i-1) + fibonnaci.get(i-2));
                if(fibonnaci.contains(number)){
                    return " es fibonacci,";
                }
                if (!fibonnaci.contains(number) && fibonnaci.get(i) > number) {
                    break;
                }
            }
        }
        return " no es fibonacci,";
    }

    public static String isPar(int number){
        return (number % 2 == 0) ? " y es par." : " y no es par.";
    }
}
