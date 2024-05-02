import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 * se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
 * con el alfabeto y los números en "leet".
 * (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 * 
 * @author anmac
 */

public class anmac {

  private static final Map<String, String> LEET_DICTIONARY = new HashMap<>() {
    {
      // Alphabet
      put("A", "4");
      put("B", "I3");
      put("C", "[");
      put("D", ")");
      put("E", "3");
      put("F", "|=");
      put("G", "&");
      put("H", "#");
      put("I", "1");
      put("J", ",_|");
      put("K", ">|");
      put("L", "1");
      put("M", "/\\/\\");
      put("N", "^/");
      put("O", "0");
      put("P", "|*");
      put("Q", "(_,)");
      put("R", "I2");
      put("S", "5");
      put("T", "7");
      put("U", "(_)");
      put("V", "\\/");
      put("W", "\\/\\/");
      put("X", "><");
      put("Y", "j");
      put("Z", "2");
      // Numbers
      put("L", "1");
      put("R", "2");
      put("E", "3");
      put("A", "4");
      put("S", "5");
      put("b", "6");
      put("T", "7");
      put("B", "8");
      put("g", "9");
      put("o", "0");
    }
  };

  public static void main(String[] args) {
    String text;
    if (args.length == 0) {
      System.out.print("Enter a text to translate: ");
      try (Scanner sc = new Scanner(System.in)) {
        text = sc.nextLine();
      }
    } else {
      text = String.join(" ", args);
    }
    System.out.println(translateToLeet(text.trim()));
  }

  private static String translateToLeet(String text) {
    if (text == null || text.length() == 0) {
      throw new IllegalArgumentException("Input text cannot be null nor empty");
    }
    StringBuilder result = new StringBuilder();
    for (char c : text.toCharArray()) {
      result.append(LEET_DICTIONARY.getOrDefault(String.valueOf(c).toUpperCase(), String.valueOf(c)));
    }
    return result.toString();
  }
}
