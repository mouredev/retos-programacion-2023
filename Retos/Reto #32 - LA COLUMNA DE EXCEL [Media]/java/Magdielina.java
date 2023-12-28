import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.OptionalInt;
import java.util.stream.IntStream;
import java.util.regex.*;
import java.lang.IllegalArgumentException;
public class Magdielina {
    public static void main(String[] args) {
        try {
            System.out.println("Column number: " + getColumnNumber("CA").orElseThrow(IllegalArgumentException::new));
        } catch (Exception e) {
            System.out.println("Error: Invalid column: " + e);
        }
    }

    public static void main(String[] args) {
        try {
            System.out.println("Column number: " + getColumnNumber("CA").orElseThrow(IllegalArgumentException::new));
        } catch (Exception e) {
            System.out.println("Error: Invalid column: " + e);
        }
    }

    public static OptionalInt getColumnNumber(String column){
        if (column != null && !Pattern.compile("[^A-Z]").matcher(column).find()) {
            List<String> list = Arrays.asList(column.split(""));
            Collections.reverse(list);
            int columnNumber = IntStream.range(0, list.size()).reduce(0, (acc, idx) -> (int)((list.get(idx).charAt(0) - 64) * Math.pow(26,idx)  + acc ));
            return OptionalInt.of(columnNumber);
        }
        return OptionalInt.empty();
    }

}