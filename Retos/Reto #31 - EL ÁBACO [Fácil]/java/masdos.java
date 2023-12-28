/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *
 *  Resultado: 1.302.790
 */
public class masdos {

  public static final int MILLION = 0;
  public static final int THOUSAND = 3;

  public static void main(String[] args) {
    String[] resultAbacus = {
      "O---OOOOOOOO",
      "OOO---OOOOOO",
      "---OOOOOOOOO",
      "OO---OOOOOOO",
      "OOOOOOO---OO",
      "OOOOOOOOO---",
      "---OOOOOOOOO"
    };
    System.out.println(calculate(resultAbacus));

    String[] resultAbacusWithInitialZeros = {
      "---OOOOOOOOO",
      "---OOOOOOOOO",
      "OO---OOOOOOO",
      "OO---OOOOOOO",
      "OOOOOOO---OO",
      "OOOOOOOOO---",
      "---OOOOOOOOO"
    };
    System.out.println(calculate(resultAbacusWithInitialZeros));
  }

  public static String calculate(String[] resultAbacus) {
    StringBuilder result = new StringBuilder();
    for (int i = 0; i < resultAbacus.length; i++) {
      int indiceStart = resultAbacus[i].indexOf("O");
      int indiceEnd = resultAbacus[i].indexOf("-");
      String beads =
          indiceStart < indiceEnd ? resultAbacus[i].substring(indiceStart, indiceEnd) : "";
      result.append(beads.length());
      if (i == MILLION || i == THOUSAND) {
        result.append(".");
      }
    }
    String resultWithoutInitialZero = result.toString().replaceAll("^(0{0,3}\\.?){0,3}", "");
    return resultWithoutInitialZero.isEmpty() ? "0" : resultWithoutInitialZero;
  }
}
