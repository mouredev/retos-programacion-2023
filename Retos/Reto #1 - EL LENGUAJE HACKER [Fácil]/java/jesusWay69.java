package reto_01;

import java.util.*;

/**
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje se
 * caracteriza por sustituir caracteres alfanuméricos. - Utiliza esta tabla
 * (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) con el alfabeto y
 * los números en "leet". (Usa la primera opción de cada transformación. Por
 * ejemplo "4" para la "a")
 *
 * @author jesus
 */
public class jesusWay69 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        System.out.println("Escriba un texto para tracucir a leguaje hack: ");
        String text = sc.nextLine().toUpperCase();
        letters_hm(text);

    }

    private static void letters_hm(String text) {

        Map T124N5L4T012 = new HashMap<>();
        String texthack = "";
        T124N5L4T012.put('A', "4");
        T124N5L4T012.put('B', "I3");
        T124N5L4T012.put('C', "{");
        T124N5L4T012.put('D', ")");
        T124N5L4T012.put('E', "3");
        T124N5L4T012.put('F', "|=");
        T124N5L4T012.put('G', "&");
        T124N5L4T012.put('H', "#");
        T124N5L4T012.put('I', "1");
        T124N5L4T012.put('J', ",_|");
        T124N5L4T012.put('K', "|<");
        T124N5L4T012.put('L', "1");
        T124N5L4T012.put('M', "/\\/\\");
        T124N5L4T012.put('N', "^/");
        T124N5L4T012.put('O', "0");
        T124N5L4T012.put('P', "|*");
        T124N5L4T012.put('Q', "(_,)");
        T124N5L4T012.put('R', "I2");
        T124N5L4T012.put('S', "5");
        T124N5L4T012.put('T', "7");
        T124N5L4T012.put('U', "(_)");
        T124N5L4T012.put('V', "\\/");
        T124N5L4T012.put('W', "\\/\\/");
        T124N5L4T012.put('X', "><");
        T124N5L4T012.put('Y', " j");
        T124N5L4T012.put('Z', "2");
        T124N5L4T012.put(' ', " ");
        for (int i = 0; i < text.length(); i++) {
            char keys = text.charAt(i);
            if (T124N5L4T012.containsKey(keys)) 
                texthack = texthack + T124N5L4T012.get(keys);
        }

        System.out.println(texthack);
    }

}
