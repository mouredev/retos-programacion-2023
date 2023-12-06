import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Qv1ko {

    public static void main(String[] args) {
        System.out.println(isMathExpression("5 + 6 / 7 - 4"));
    }

    private static boolean isMathExpression(String expression) {

        boolean result = true;
        Pattern regex = Pattern.compile("-?\\d+|-?\\d+\\.\\d+|[+\\-*/%]");
        Matcher check;

        for (String element : expression.split(" ")) {
            check = regex.matcher(element);
            if (!check.find()) {
                result = false;
                break;
            }
        }

        return result;

    }

}
