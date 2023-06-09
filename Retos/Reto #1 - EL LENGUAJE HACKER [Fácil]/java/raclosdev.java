
/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

import java.util.HashMap;
import java.util.Map;

public class raclosdev {
    static Map<Character, String> replacements = new HashMap<>();


    public static String hackText(String text) {

        StringBuilder hacked = new StringBuilder();
        for (Character c : text.toCharArray()) {
            if (replacements.containsKey(c)) hacked.append(replacements.get(c));
            else hacked.append(c);
        }

        return text;
    }

    public static void main(String[] args) {
        String texto = "Reto solucionado por RaclosDev";
        System.out.println(hackText(texto));
    }

    public void fillMap() {
        replacements.put('a', "4");
        replacements.put('b', "6");
        replacements.put('c', "(");
        replacements.put('d', "|)");
        replacements.put('e', "3");
        replacements.put('f', "|=");
        replacements.put('g', "6");
        replacements.put('h', "|-|");
        replacements.put('i', "1");
        replacements.put('j', "_|");
        replacements.put('k', "|<");
        replacements.put('l', "1_");
        replacements.put('m', "|V|");
        replacements.put('n', "|\\|");
        replacements.put('o', "0");
        replacements.put('p', "|*");
        replacements.put('q', "0_");
        replacements.put('r', "|2");
        replacements.put('s', "5");
        replacements.put('t', "7");
        replacements.put('u', "|_|");
        replacements.put('v', "\\/");
        replacements.put('w', "\\/\\/");
        replacements.put('x', "><");
        replacements.put('y', "`/");
        replacements.put('z', "2");
        replacements.put('0', "O");
        replacements.put('1', "I");
        replacements.put('2', "Z");
        replacements.put('3', "E");
        replacements.put('4', "A");
        replacements.put('5', "S");
        replacements.put('6', "G");
        replacements.put('7', "T");
        replacements.put('8', "B");
        replacements.put('9', "P");
    }
}
