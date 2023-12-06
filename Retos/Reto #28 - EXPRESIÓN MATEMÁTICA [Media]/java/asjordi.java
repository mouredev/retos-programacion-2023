public class MathematicalExpression {

    public static boolean check(String expression){

        String[] components = expression.split(" ");

        if (components.length < 3 || components.length % 2 == 0) return false;

        boolean check = true;

        for (int i = 0; i < components.length; i++) {
            if (i % 2 == 0) check = isNumber(components[i]);
            else check = isOperation(components[i]);

            if (!check) return false;
        }

        return check;

    }

    private static boolean isNumber(String str) {
        try {
            Double.parseDouble(str);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }

    private static boolean isOperation(String str) {
        return str.matches("[+\\-*/%]");
    }

}
