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

  public static void main(String[] args) {
    System.out.println(translateT9Code("6-666-88-777-33-3-33-888"));
    System.out.println(translateT9Code("6-667-88-777-33-3-33-888"));
  }

  private static final HashMap<Integer, String> T9_KEY_MAP = createT9KeyMap();

  public static String translateT9Code(String t9Code) {
    validateT9CodeFormat(t9Code);
    return Arrays.stream(t9Code.split("-"))
        .map(
            splitCode -> {
              int key = Integer.parseInt(splitCode.substring(0, 1));
              int value = splitCode.length() - 1;
              return T9_KEY_MAP.get(key).substring(value, value + 1);
            })
        .collect(Collectors.joining());
  }

  private static void validateT9CodeFormat(String t9Code) {
    if (!t9Code.matches(
        "^(0|([2-58])\\2{0,2}|([679])\\3{0,3})(-(0|([2-58])\\6{0,2}|([679])\\7{0,3}))*$")) {
      throw new IllegalArgumentException(
          "The T9Code has invalid format, T9Code: " + t9Code + ". Example: '555-44-22'");
    }
  }

  private static HashMap<Integer, String> createT9KeyMap() {
    HashMap<Integer, String> t9KeyMap = new HashMap<>();
    t9KeyMap.put(0, " ");
    t9KeyMap.put(2, "ABC");
    t9KeyMap.put(3, "DEF");
    t9KeyMap.put(4, "GHI");
    t9KeyMap.put(5, "JKL");
    t9KeyMap.put(6, "MNOÑ");
    t9KeyMap.put(7, "PQRS");
    t9KeyMap.put(8, "TUV");
    t9KeyMap.put(9, "WXYZ");
    return t9KeyMap;
  }
}
