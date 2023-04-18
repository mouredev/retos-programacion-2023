package neyser;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner sc1 = new Scanner(System.in);

        System.out.println("Introducir un numero");
        Integer numero = sc1.nextInt();

        dibujar(numero);
    }

    public static void dibujar(Integer numero){
        String gradasP = "_|";
        String gradasN = "|_";
        String espacio = " ";
        Integer num2 = numero;

        if(numero == 0){
            System.out.println("__");
        } else if (numero>0) {
            for (int i = 0; i <=numero; i++, num2--) {
                if (i == 0) {
                    System.out.println(espacio.repeat(2*num2)+"_");
                } else{
                    System.out.println(espacio.repeat(2*num2)+ gradasP );
                }
            }
        } else{
            num2 = 0;
            for (int i = 0; i >numero; i--, num2++) {
                if (i == 0) {
                    System.out.println("_");
                    num2 = 0;
                } else{
                    System.out.println((espacio.repeat(2*num2-1))+ gradasN);
                }
            }
        }

    }

}

    