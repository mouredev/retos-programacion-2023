/*
 * Crea una función que reciba una expresión matemática (String)
 * y compruebe si es correcta. Retornará true o false.
 * - Para que una expresión matemática sea correcta debe poseer
 *   un número, una operación y otro número separados por espacios.
 *   Tantos números y operaciones como queramos.
 * - Números positivos, negativos, enteros o decimales.
 * - Operaciones soportadas: + - * / %
 *
 * Ejemplos:
 * "5 + 6 / 7 - 4" -> true
 * "5 a 6" -> false
 */
public class masdos {

  public static void main(String[] args) {
    System.out.println(isValidMathOperation("5 + 6 / 7 - 4"));
    System.out.println(isValidMathOperation("5 a 6"));
    System.out.println(isValidMathOperation("-5.45 + 6.5 / 7 - 4.5"));
  }

  public static boolean isValidMathOperation(String operation) {
    return operation.matches("^(-?\\d(.\\d)?)+(\\s[-+*/%]\\s(-?\\d(.\\d)?)+)+$");
  }
}