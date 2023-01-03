import java.util.stream.IntStream;

public class amartellram {

  public static void fizzbuzz() {
    IntStream.range(1, 101)
        .forEach(number -> {
          StringBuilder text = new StringBuilder();
          if (number % 3 == 0) {
            text.append("fizz");
          }
          if (number % 5 == 0) {
            text.append("buzz");
          }
          System.out.println(text.isEmpty() ? number : text);
        });
  }

  public static void main(String[] args) {
    fizzbuzz();
  }
}