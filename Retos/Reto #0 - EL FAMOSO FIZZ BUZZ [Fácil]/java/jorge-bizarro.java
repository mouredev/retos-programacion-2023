// Escribe un programa que muestre por consola (con un print) los
// números de 1 a 100 (ambos incluidos y con un salto de línea entre
// cada impresión), sustituyendo los siguientes:
// - Múltiplos de 3 por la palabra "fizz".
// - Múltiplos de 5 por la palabra "buzz".
// - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

public class Main {
  public static void main(String[] args) {
    for (int valueNumber = 1; valueNumber <= 100; valueNumber++)
    {
      String valueString = "";

      if (valueNumber % 3 == 0)
        valueString += "Fizz";

      if (valueNumber % 5 == 0)
        valueString += "Buzz";

      System.out.println(valueString.isEmpty() ? valueNumber : valueString);
    }
  }
}
