public class EspinoLeandroo {

    public static void main(String[] args) {
        String expression1 = "5 + 16 / 7 - 4";
        String expression2 = "5 a 6";

        System.out.println(validateMathExpression(expression1)); 
        System.out.println(validateMathExpression(expression2)); 
    }

    public static boolean validateMathExpression(String expression) {
        String[] tokens = expression.split("\\s+");
        
        if (tokens.length % 2 == 0) {
            return false;
        }

        for (int i = 0; i < tokens.length; i++) {
            if (i % 2 == 0) {
                if (!isNumber(tokens[i])) {
                    return false;
                }
            } else { 
                if (!isOperation(tokens[i])) {
                    return false;
                }
            }
        }

        return true;
    }

    private static boolean isNumber(String token) {
        try {
            Double.parseDouble(token);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    private static boolean isOperation(String token) {
        return token.matches("[+\\-*/%]");
    }
}
