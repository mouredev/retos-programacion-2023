package com.retos;

/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo,
 * fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

import java.util.Scanner;

public class Reto4ComprobarNumeros {

    public static void main(String[] args) {

        boolean fin = false;
        System.out.println("Para salir, introduzca: 0");

        while (!fin) {
            System.out.println("Introduce un número entero: ");
            Scanner entrada = new Scanner(System.in);
            int num = entrada.nextInt();
            String fibonacci;
            String primo;
            String par;

            if (fibonacci(num)) {
                fibonacci = "es fibonacci";
            } else {
                fibonacci = "no es fibonacci";
            }

            if (primo(num)) {
                primo = "Es primo";
            } else {
                primo = "No es primo";
            }

            if (par(num)) {
                par = "es par";
            } else {
                par = "no es par";
            }

            if (num == 0) {
                fin = true;
            } else {
                System.out.println(num + ": " + primo + ", " + fibonacci + " y " + par);
            }
        }
    }

    public static boolean fibonacci(int numFibonacci) {
        boolean fibonacci = false;

        double cuadrado1 = (5*(numFibonacci^2) + 4);
        double raizCuadrada1 = Math.sqrt(cuadrado1);

        double cuadrado2 = (5*(numFibonacci^2) - 4);
        double raizCuadrada2 = Math.sqrt(cuadrado2);

        if (raizCuadrada1 % 1 == 0) {
            fibonacci = true;
        } else if (raizCuadrada2 % 1 == 0) {
            fibonacci = true;
        }
        return fibonacci;
    }

    public static boolean primo(int numPrimo) {
        boolean primo = true;

        for (int i = 2; i <= numPrimo / 2; i++) {

            if (numPrimo % i == 0) {
                primo = false;
                break;
            }
        }
        return primo;
    }

    public static boolean par(int numPar) {
        return numPar % 2 == 0;
    }
}
