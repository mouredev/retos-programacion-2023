import java.util.stream.IntStream;

public class idevcm {
    public static void main(String[] args) {
        IntStream
                .range(1, 101)
                .mapToObj(number ->
                        number % 3 == 0 ? number % 5 == 0 ? "FizzBuzz" : "Fizz" : number % 5 == 0 ? "Buzz" : number)
                .forEach(System.out::println);
    }
}
