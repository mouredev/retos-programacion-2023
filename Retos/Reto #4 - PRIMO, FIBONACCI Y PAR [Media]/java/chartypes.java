import java.util.ArrayList;
import java.util.List;

public class chartypes {

  public static void main(String[] args) {
    exercise(2);
    exercise(7);

  }

  public static void exercise(int number) {

    if (isPrime(number))
      System.out.print(number + " is prime, ");
    else
      System.out.print(number + " is not prime, ");
    if (isFibonacci(number))
      System.out.print("is fibonacci and ");
    else
      System.out.print("is not fibonacci and ");
    if (isPar(number))
      System.out.print("is par");
    else
      System.out.print("is odd ");

  }

  public static boolean isPar(int number) {
    return number % 2 == 0;
  }

  public static boolean isPrime(int number) {
    if (number < 1)
      return false;

    for (int i = 2; i < number; i++)
      if (number % i == 0)
        return false;

    return true;
  }

  public static boolean isFibonacci(int number) {

    List<Integer> fibonacci = new ArrayList<>();
    fibonacci.add(1);
    fibonacci.add(1);
    int current;
    int len;

    for (int i = 0; i < number + 1; i++) {
      len = fibonacci.size();
      current = fibonacci.get(len - 1) + fibonacci.get(len - 2);
      if (current == number)
        return true;
      fibonacci.add(current);
    }
    return false;
  }

}
