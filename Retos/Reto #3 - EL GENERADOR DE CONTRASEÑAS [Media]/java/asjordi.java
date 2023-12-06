import java.util.List;
import java.util.Random;

public class GeneratePassword {

    private final int length;
    private final boolean withUppercase;
    private final boolean withNumbers;
    private final boolean withSymbols;
    private final Random random;

    public GeneratePassword(int length, boolean withUppercase, boolean withNumbers, boolean withSymbols) {

        this.length = length < 8 ? 8 : Math.min(length, 16);
        this.withUppercase = withUppercase;
        this.withNumbers = withNumbers;
        this.withSymbols = withSymbols;
        this.random = new Random();

    }

    public String generate() {

        StringBuilder password = new StringBuilder();

        while (password.length() < length) {

            password.append(getLowercaseLetter());
            if (this.withUppercase) password.append(getUppercaseLetter());
            if (this.withNumbers) password.append(getNumber());
            if (this.withSymbols) password.append(getSymbol());

        }

        return password.toString();

    }

    public String getUppercaseLetter() {

        List<String> uppercaseLetter = List.of(
                "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
        );

        return uppercaseLetter.get(random.nextInt(uppercaseLetter.size()));

    }

    public String getLowercaseLetter() {

        List<String> lowercaseLetter = List.of(
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        );

        return lowercaseLetter.get(random.nextInt(lowercaseLetter.size()));

    }

    public String getNumber() {

        List<String> numbers = List.of("0", "1", "2", "3", "4", "5", "6", "7", "8", "9");

        return numbers.get(random.nextInt(numbers.size()));

    }

    public String getSymbol() {

        List<String> symbols = List.of("!", "@", "#", "$", "%", "&", "*", "+", "-", "=", "^");

        return symbols.get(random.nextInt(symbols.size()));

    }

}
