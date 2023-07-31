import java.util.Arrays;
import java.util.HashMap;
import java.util.stream.Collectors;

/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */
public class masdos {

  public static String translateT9Code(String t9Code) {
    if (!t9Code.matches(
        "^(0|([2-58])\\2{0,2}|([679])\\3{0,3})(-(0|([2-58])\\6{0,2}|([679])\\7{0,3}))*$")) {
      throw new IllegalArgumentException(
          "The T9Code has invalid format, T9Code: " + t9Code + ". Example: '555-44-22'");
    }
    HashMap<String, String[]> t9KeyMap = createT9KeyMap();
    return Arrays.stream(t9Code.split("-"))
        .map(
            splitCode -> {
              String key = String.valueOf(splitCode.charAt(0));
              int value = splitCode.length() - 1;
              return t9KeyMap.get(key)[value];
            })
        .collect(Collectors.joining());
  }

  private static HashMap<String, String[]> createT9KeyMap() {
    HashMap<String, String[]> t9KeyMap = new HashMap<>();
    t9KeyMap.put("0", new String[] {" "});
    t9KeyMap.put("2", new String[] {"A", "B", "C"});
    t9KeyMap.put("3", new String[] {"D", "E", "F"});
    t9KeyMap.put("4", new String[] {"G", "H", "I"});
    t9KeyMap.put("5", new String[] {"J", "K", "L"});
    t9KeyMap.put("6", new String[] {"M", "N", "O", "Ñ"});
    t9KeyMap.put("7", new String[] {"P", "Q", "R", "S"});
    t9KeyMap.put("8", new String[] {"T", "U", "V"});
    t9KeyMap.put("9", new String[] {"W", "X", "Y", "Z"});
    return t9KeyMap;
  }
}
