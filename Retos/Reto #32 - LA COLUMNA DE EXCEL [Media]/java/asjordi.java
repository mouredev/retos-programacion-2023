public class Excel {

    public static int calculateColumnNumber(String column){

        int result = 0;

        for (char c : column.toCharArray()) result = result * 26 + (c - 'A' + 1);

        return result;
    }

}
