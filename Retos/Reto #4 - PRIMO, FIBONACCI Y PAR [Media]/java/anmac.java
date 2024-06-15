/*
 * Escribe un programa que, dado un número, compruebe y muestre si es primo, fibonacci y par.
 * Ejemplos:
 * - Con el número 2, nos dirá: "2 es primo, fibonacci y es par"
 * - Con el número 7, nos dirá: "7 es primo, no es fibonacci y es impar"
 */

import java.util.concurrent.ExecutionException;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.Future;

public class anmac {

  private final boolean isPrime;
  private final boolean isFibonacci;
  private final boolean isEven;

  public anmac(boolean isPrime, boolean isFibonacci, boolean isEven) {
    this.isPrime = isPrime;
    this.isFibonacci = isFibonacci;
    this.isEven = isEven;
  }

  public static void main(String[] args) {
    int number = 53;
    try {
      anmac properties = computeNumberProperties(number);
      printResult(number, properties);
    } catch (InterruptedException | ExecutionException e) {
      System.err.println(
          "Error trying to compute and print number properties for "
              + number
              + ": "
              + e.getMessage());
    }
  }

  private static anmac computeNumberProperties(int number)
      throws InterruptedException, ExecutionException {
    ExecutorService executor = Executors.newFixedThreadPool(2);

    Future<Boolean> primeFuture = executor.submit(() -> isPrime(number));
    Future<Boolean> fibonacciFuture = executor.submit(() -> isFibonacci(number));
    Future<Boolean> evenFuture = executor.submit(() -> isEven(number));

    boolean isPrime = primeFuture.get();
    boolean isFibonacci = fibonacciFuture.get();
    boolean isEven = evenFuture.get();

    executor.shutdown();
    return new anmac(isPrime, isFibonacci, isEven);
  }

  private static void printResult(int number, anmac properties) {
    StringBuilder sb = new StringBuilder();
    sb.append(number);
    sb.append(properties.isPrime ? " es primo" : " no es primo");
    sb.append(", ");
    sb.append(properties.isFibonacci ? "fibonacci" : "no es fibonacci");
    sb.append(" y ");
    sb.append(properties.isEven ? "es par" : "es impar");
    System.out.println(sb.toString());
  }

  /**
   * This method returns true if the number is prime, false otherwise. Uses the Trial Division
   * method.
   *
   * @param number the number to check
   * @return true if the number is prime, false otherwise
   */
  private static boolean isPrime(int number) {
    if (number < 2) {
      return false;
    }
    for (int divisor = 2; divisor <= (int) Math.sqrt(number); divisor++) {
      if (number % divisor == 0) return false;
    }
    return true;
  }

  /**
   * This method returns true if the number is fibonacci, false otherwise. Uses the Binet's Formula
   * to check if one or both (5*n^2 + 4) (5*n^2 - 4) of the numbers is a perfect square.
   *
   * @param number the number to check
   * @return true if the number is fibonacci, false otherwise
   */
  private static boolean isFibonacci(int number) {
    if (number == 0 || number == 1) return true;

    int n1 = ((5 * number * number) + 4);
    int n2 = ((5 * number * number) - 4);

    return isPerfectSquare(n1) || isPerfectSquare(n2);
  }

  /**
   * This method returns check if the number is a perfect square.
   *
   * @param number the number to check
   * @return true if the number is a perfect square, false otherwise
   */
  private static boolean isPerfectSquare(int number) {
    int sqrt = (int) Math.sqrt(number);
    return ((sqrt * sqrt) == number);
  }

  /**
   * This method returns true if the number is even, false otherwise.
   *
   * @param number the number to check
   * @return true if the number is even, false otherwise
   */
  private static boolean isEven(int number) {
    return (number % 2 == 0);
  }
}
