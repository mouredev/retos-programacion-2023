/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

class Number {

  public static boolean isPrime(int number) {
    if (number > 2 && isEven(number)) return false;
    for (int i = 2; i < number; i++) {
      if (number % i == 0) return false;
    }
    return true;
  }

  public static boolean isFib(int number) {
    if (number == 0 || number == 1) return true;
    int x = 0;
    int y = 1;
    int z = x + y;
    do {
      if (number == z) return true;
      x = y;
      y = z;
      z = x + y;
    } while (z <= number);
    return false;
  }

  public static boolean isEven(int number) {
    return (number % 2 == 0);
  }

  public static void check(int number) {
    System.out.printf("%d ", number);
    if (!isPrime(number))
      System.out.printf("no es primo, ");
    else
      System.out.printf("es primo, ");

    if (!isFib(number))
      System.out.printf("no es fibonacci ");
    else
      System.out.printf("es fibonacci ");

    if (!isEven(number))
      System.out.printf("y es impar%n");
    else
      System.out.printf("y es par%n");
  }

  public static void main(String... args) {
    check(2);
    check(7);
  }
}
