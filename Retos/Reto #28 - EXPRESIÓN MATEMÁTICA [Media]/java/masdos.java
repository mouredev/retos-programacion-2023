import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class masdos {

  public static void main(String[] args) {
    System.out.println(isValidMathOperation("5 + 6 / 7 - 4"));
    System.out.println(isValidMathOperation("5 a 6"));
    System.out.println(isValidMathOperation("-5.45 + 6.5 / 7 - 4.5"));
  }

  public static boolean isValidMathOperation(String operation) {
    Pattern pattern =
            Pattern.compile("^(\\-?\\d(\\.\\d)?)+(\\s[\\+\\-\\*\\/%]\\s(\\-?\\d(\\.\\d)?)+)+$");
    Matcher matcher = pattern.matcher(operation);
    return matcher.matches();
  }
}