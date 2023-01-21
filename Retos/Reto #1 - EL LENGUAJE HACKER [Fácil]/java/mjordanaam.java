/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
import java.util.*;

public class mjordanaam {
    public static Map<String, String> leetAlphabet = new HashMap<String, String>();

    static {
        leetAlphabet.put("A","4");
        leetAlphabet.put("B","I3");
        leetAlphabet.put("C","[]");
        leetAlphabet.put("D",")");
        leetAlphabet.put("E","3");
        leetAlphabet.put("F","|=");
        leetAlphabet.put("G","&");
        leetAlphabet.put("H","#");
        leetAlphabet.put("I","1");
        leetAlphabet.put("J",",_|");
        leetAlphabet.put("K",">|");
        leetAlphabet.put("L","1");
        leetAlphabet.put("M","/\\/\\");
        leetAlphabet.put("N","^/");
        leetAlphabet.put("O","0");
        leetAlphabet.put("P","|*");
        leetAlphabet.put("Q","(_,)");
        leetAlphabet.put("R","I2");
        leetAlphabet.put("S","5");
        leetAlphabet.put("T","7");
        leetAlphabet.put("U","(_)");
        leetAlphabet.put("V","\\/");
        leetAlphabet.put("W","\\/\\/");
        leetAlphabet.put("X","><");
        leetAlphabet.put("Y","j");
        leetAlphabet.put("Z","2");
        leetAlphabet.put("1","L");
        leetAlphabet.put("2","R");
        leetAlphabet.put("3","E");
        leetAlphabet.put("4","A");
        leetAlphabet.put("5","S");
        leetAlphabet.put("6","b");
        leetAlphabet.put("7","T");
        leetAlphabet.put("8","B");
        leetAlphabet.put("9","g");
        leetAlphabet.put("0","o");
    }

    public static String convertToHackerCode(String text){

        String convertedText = "";

        for (int i = 0; i < text.length(); i++) {
            String character = (text.charAt(i) + "").toUpperCase();

            if (leetAlphabet.get(character) != null){
                convertedText += leetAlphabet.get(character);
            }
            else{
                convertedText += text.charAt(i) + "";
            }
        }
        return convertedText;
    }

    public static void main(String[] args) {
        String result = convertToHackerCode("Hello World!");

        System.out.println(result);

        result = convertToHackerCode("mouredev");

        System.out.println(result);
    }
}
