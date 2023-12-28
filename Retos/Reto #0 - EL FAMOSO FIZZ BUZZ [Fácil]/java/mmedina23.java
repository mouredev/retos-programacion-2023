import java.util.stream.IntStream;

public class FizzBuzz {

    public static void main(String[] args) {
        IntStream.rangeClosed(1, 100).forEach(it -> {
            switch (Integer.valueOf(it)) {
                case Integer i && (i % 3) == 0 && (i % 5) == 0 -> System.out.println("fizzbuzz");
                case Integer i && (i % 3) == 0 -> System.out.println("fizz");
                case Integer i && (i % 5) == 0 -> System.out.println("buzz");
                default -> System.out.println(it);
            }
        });
    }
}