import java.util.Arrays;
import java.util.Scanner;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

class HackerLang {
  public static final String[] leet = {"o", "L", "R", "E", "A", "S", "b", "T", "B", "g", "4", "I3",
    "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", "/\\/\\", "^/", "0", "|*", "(_,)", "I2",
    "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2"};
  public static final char[] decode = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b',
    'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};

  public static String encodeString (String message) {
    message = message.toLowerCase();
    String encoded = "";
    for (int i = 0; i < message.length(); i++) {
      char currentChar = message.charAt(i);
      int pos = Arrays.binarySearch(decode, currentChar); 
      if (pos >= 0) {
        encoded += leet[pos];
      } else {
        encoded += currentChar;
      }
    }
    return encoded;
  }

  public static void main(String... args) {
    Scanner input = new Scanner(System.in);

    System.out.println("Escribe un mensaje para codificar a \"1337\":");

    String decodedMessage = input.nextLine();

    String encodedMessage = encodeString(decodedMessage);

    System.out.println(encodedMessage);

  }
}
