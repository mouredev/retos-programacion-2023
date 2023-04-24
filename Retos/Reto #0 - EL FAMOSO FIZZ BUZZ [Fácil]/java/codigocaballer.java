import java.util.ArrayList;
import java.util.List;

final class FizzBuzzConstants {
    private FizzBuzzConstants() {
    }

    public static final String FIZZ = "fizz";
    public static final String BUZZ = "buzz";
    public static final String FIZZBUZZ = "fizzbuzz";
}

class FizzBuzzContext {
    FizzBuzzStrategy gameStrategy;

    public FizzBuzzContext(FizzBuzzStrategy gameStrategy) {
        this.gameStrategy = gameStrategy;
    }

    public void setGameStrategy(FizzBuzzStrategy gameStrategy) {
        this.gameStrategy = gameStrategy;
    }

    public List<Object> game() {
        return this.gameStrategy.execute();
    }
}

interface FizzBuzzStrategy {
    List<Object> execute();
}

class FizzBuzzStrategyMod implements FizzBuzzStrategy {
    @Override
    public List<Object> execute() {
        int N = 100;
        List<Object> result = new ArrayList<>(N);
        for (int num = 1; num <= N; num++) {
            if (num % 3 == 0 && num % 5 == 0) {
                result.add("fizzbuzz");
                System.out.printf("%s%n", FizzBuzzConstants.FIZZBUZZ);
            } else if (num % 5 == 0) {
                result.add("buzz");
                System.out.printf("%s%n", FizzBuzzConstants.BUZZ);
            } else if (num % 3 == 0) {
                result.add("fizz");
                System.out.printf("%s%n", FizzBuzzConstants.FIZZ);
            } else {
                result.add(num);
                System.out.printf("%s%n", num);
            }
        }
        return result;
    }
}

class FizzBuzzStrategySum implements FizzBuzzStrategy {
    @Override
    public List<Object> execute() {
        String word = "";
        int multi3 = 0, multi5 = 0, num = 1, N = 100;
        List<Object> result = new ArrayList<>(N);

        while (num <= N) {
            multi3 += 1;
            multi5 += 1;
            if (multi3 == 3) {
                word += FizzBuzzConstants.FIZZ;
                multi3 = 0;
            }
            if (multi5 == 5) {
                word += FizzBuzzConstants.BUZZ;
                multi5 = 0;
            }
            if (word.length() == 0) {
                result.add(num);
                System.out.printf("%s%n", num);
            } else {
                result.add(word);
                System.out.printf("%s%n", word);
            }
            word = "";
            num += 1;
        }
        return result;
    }
}

public class codigocaballer {
    public static void main(String[] args) {
        FizzBuzzStrategy modStrategy = new FizzBuzzStrategyMod();
        FizzBuzzContext fizzBuzzContext = new FizzBuzzContext(modStrategy);
        fizzBuzzContext.setGameStrategy(modStrategy);
        fizzBuzzContext.game();
    }
}
