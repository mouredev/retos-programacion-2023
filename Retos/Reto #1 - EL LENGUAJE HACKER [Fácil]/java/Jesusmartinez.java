import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https=//www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

public class Jesusmartinez {

    public static void main(String[] args) {
        System.out.println(convertTexttoHacker("Mario"));
    }

    public static String convertTexttoHacker(String text) {
        Map<String, String> lettersMap = new HashMap<>();
        lettersMap.put("A", "4");
        lettersMap.put("B", "8");
        lettersMap.put("C", "(");
        lettersMap.put("D", ")");
        lettersMap.put("E", "3");
        lettersMap.put("F", "|=");
        lettersMap.put("G", "6");
        lettersMap.put("H", "#");
        lettersMap.put("I", "1");
        lettersMap.put("J", "]");
        lettersMap.put("K", ">|");
        lettersMap.put("L", "1");
        lettersMap.put("M", "/\\/\\//\\");
        lettersMap.put("N", "/\\/\\");
        lettersMap.put("O", "0");
        lettersMap.put("P", "|>");
        lettersMap.put("Q", "9");
        lettersMap.put("R", "|2");
        lettersMap.put("S", "5");
        lettersMap.put("T", "7");
        lettersMap.put("U", "(_)");
        lettersMap.put("V", "\\/");
        lettersMap.put("W", "\\/\\/");
        lettersMap.put("X", "><");
        lettersMap.put("Y", "`/");
        lettersMap.put("Z", "2");

        StringBuilder finalText = new StringBuilder();
        Arrays.asList(text.toUpperCase().split("")).stream().forEach(val -> {
            finalText.append(lettersMap.get(val));
        });
        return finalText.toString();
    }

}
