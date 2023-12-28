package reto1;

import java.util.HashMap;
import java.util.Map;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

public class jitos_dev {

    public static void main(String[] args) {
        String natural = "Hola Mundo!!";
        System.out.println(naturalToLeet(natural));
    }

    public static String naturalToLeet(String natural) {
        Map<String, String> dictionary = getDictionary();
        StringBuilder leet = new StringBuilder();

        for (char characterNatural : natural.toCharArray()) {
            //Lo paso a minúscula por si introduce algún caracter en mayúscula ya que el diccionario está en minúscula
            String character = String.valueOf(characterNatural).toLowerCase();

            //Comprobamos que contiene el caracter antes de obtenerlo y guardarlo para devolverlo
            if (dictionary.containsKey(character)) {
                leet.append(dictionary.get(character));
            }
        }
        return leet.toString();
    }

    public static Map<String, String> getDictionary() {
        Map<String, String> dictionary = new HashMap<>();
        dictionary.put("a", "4");
        dictionary.put("b", "I3");
        dictionary.put("c", "[");
        dictionary.put("d", ")");
        dictionary.put("e", "3");
        dictionary.put("f", "|=");
        dictionary.put("g", "&");
        dictionary.put("h", "#");
        dictionary.put("i", "1");
        dictionary.put("j", ",_|");
        dictionary.put("k", ">|");
        dictionary.put("l", "1");
        dictionary.put("m", "/\\/\\");
        dictionary.put("n", "^/");
        dictionary.put("o", "0");
        dictionary.put("p", "|*");
        dictionary.put("q", "(_,)");
        dictionary.put("r", "I2");
        dictionary.put("s", "5");
        dictionary.put("t", "7");
        dictionary.put("u", "(_)");
        dictionary.put("v", "\\/");
        dictionary.put("w", "\\/\\/");
        dictionary.put("x", "><");
        dictionary.put("y", "j");
        dictionary.put("z", "2");
        dictionary.put(" ", " ");

        dictionary.put("1", "L");
        dictionary.put("2", "R");
        dictionary.put("3", "E");
        dictionary.put("4", "A");
        dictionary.put("5", "S");
        dictionary.put("6", "b");
        dictionary.put("7", "T");
        dictionary.put("8", "B");
        dictionary.put("9", "g");
        dictionary.put("0", "o");

        return dictionary;
    }
}
