package com.retos;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

import java.util.HashMap;
import java.util.Scanner;

public class Reto1LenguajeHacker {

    public static void main(String[] args) {

        HashMap<Character, String> diccionario = new HashMap<>();

        diccionario.put('A', "4");
        diccionario.put('B', "I3");
        diccionario.put('C', "[");
        diccionario.put('D', ")");
        diccionario.put('E', "3");
        diccionario.put('F', "|=");
        diccionario.put('G', "&");
        diccionario.put('H', "#");
        diccionario.put('I', "1");
        diccionario.put('J', ",_|");
        diccionario.put('K', ">|");
        diccionario.put('L', "1");
        diccionario.put('M', "/|/|");
        diccionario.put('N', "^/");
        diccionario.put('O', "0");
        diccionario.put('P', "|*");
        diccionario.put('Q', "(_,)");
        diccionario.put('R', "I2");
        diccionario.put('S', "5");
        diccionario.put('T', "7");
        diccionario.put('U', "(_)");
        diccionario.put('V', "|/");
        diccionario.put('W', "|/|/");
        diccionario.put('X', "><");
        diccionario.put('Y', "j");
        diccionario.put('Z', "2");
        diccionario.put('1', "L");
        diccionario.put('2', "R");
        diccionario.put('3', "E");
        diccionario.put('4', "A");
        diccionario.put('5', "S");
        diccionario.put('6', "b");
        diccionario.put('7', "T");
        diccionario.put('8', "B");
        diccionario.put('9', "g");
        diccionario.put('0', "o");
        diccionario.put(' ', " ");

        String frase;
        boolean fin = false;
        System.out.println("(Para salir introduzca: Fin)");
        System.out.println("Introduce una frase: ");

        while (!fin) {
            Scanner entrada = new Scanner(System.in);
            frase = entrada.nextLine().toUpperCase();
            fin = frase.equals("FIN");

            for (int i = 0; i < frase.toCharArray().length; i++) {
                String traduccion = diccionario.get(frase.toCharArray()[i]);

                if (!fin) {
                    System.out.print(traduccion);
                }
            }
            System.out.println();
        }
    }
}
