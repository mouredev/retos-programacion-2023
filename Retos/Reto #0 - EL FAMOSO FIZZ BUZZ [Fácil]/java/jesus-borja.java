/*
 * Escribe un programa que muestre por consola (con un print) los
 * números de 1 a 100 (ambos incluidos y con un salto de línea entre
 * cada impresión), sustituyendo los siguientes:
 * - Múltiplos de 3 por la palabra "fizz".
 * - Múltiplos de 5 por la palabra "buzz".
 * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
 */

class FizzBuzz {

  public static void FizzBuzz(int n) {
    for (int i = 1; i <= n; i++) {

      boolean fizz = (i % 3 == 0);
      boolean buzz = (i % 5 == 0);
      boolean fizzbuzz = (i % 15 == 0);

      if (fizzbuzz) System.out.printf("fizzbuzz\n");
      else if (fizz) System.out.printf("fizz\n");
      else if (buzz) System.out.printf("buzz\n");
      else System.out.println(i);
    }
  }

  public static void main(String... args) {
    FizzBuzz(100);
  }
}
