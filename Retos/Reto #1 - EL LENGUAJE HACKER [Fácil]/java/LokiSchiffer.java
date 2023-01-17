*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */

import java.util.HashMap;
import java.util.Map;
import java.lang.StringBuffer;

class Main {
  static Map<String, String> leetTable = new HashMap<>();
  static void populateTable(){
    leetTable.put("a", "4");
    leetTable.put("b", "I3");
    leetTable.put("c", "[");
    leetTable.put("d", ")");
    leetTable.put("e", "3");
    leetTable.put("f", "|=");
    leetTable.put("g", "&");
    leetTable.put("h", "#");
    leetTable.put("i", "1");
    leetTable.put("j", ",_|");
    leetTable.put("k", ">|");
    leetTable.put("l", "1");
    leetTable.put("m", "/\\/\\");
    leetTable.put("n", "^/");
    leetTable.put("o", "0");
    leetTable.put("p", "|*");
    leetTable.put("q", "(_,)");
    leetTable.put("r", "I2");
    leetTable.put("s", "5");
    leetTable.put("t", "7");
    leetTable.put("u", "(_)");
    leetTable.put("v", "\\/");
    leetTable.put("w", "\\/\\/");
    leetTable.put("x", "><");
    leetTable.put("y", "j");
    leetTable.put("z", "2");
    leetTable.put("1", "L");
    leetTable.put("2", "R");
    leetTable.put("3", "E");
    leetTable.put("4", "A");
    leetTable.put("5", "S");
    leetTable.put("6", "b");
    leetTable.put("7", "T");
    leetTable.put("8", "B");
    leetTable.put("9", "g");
    leetTable.put("0", "o");
  }

  static String leetTranslate(String frase) {
    String[] phraseArray =frase.split("");
    for (int i = 0; i < phraseArray.length; i++) {
      if (leetTable.containsKey(phraseArray[i].toLowerCase())) {
        phraseArray[i] = leetTable.get(phraseArray[i].toLowerCase());
      }
    }
    return String.join("", phraseArray);
}

  public static void main(String[] args) {
    populateTable();
    System.out.println(leetTranslate("La mera prueba"));
    System.out.println(leetTranslate("2da comprobación del reto 1"));
    System.out.println(leetTranslate("numeros 1234567890"));
    System.out.println(leetTranslate("Ángel se fue a la tierra, del olvido!"));
  }
}