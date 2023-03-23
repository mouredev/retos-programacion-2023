import java.util.Map;
import java.util.HashMap;

public class josevalver {

    String[][] leet = {
        {"A", "4"},
        {"B", "I3"},
        {"C", "["},
        {"D", ")"},
        {"E", "3"},
        {"F", "|="},
        {"G", "6"},
        {"H", "#"},
        {"I", "1"},
        {"J", ",_|"},
        {"K", ">|"},
        {"L", "1"},
        {"M", "|\\/|"},
        {"N", "|\\|"},
        {"O", "0"},
        {"P", "|*"},
        {"Q", "(_,)"},
        {"R", "|2"},
        {"S", "5"},
        {"T", "7"},
        {"U", "(_)"},
        {"V", "\\/"},
        {"W", "\\/\\/"},
        {"X", "><"},
        {"Y", "j"},
        {"Z", "2"},
        {"1", "L"},
        {"2", "Z"},
        {"3", "E"},
        {"4", "A"},
        {"5", "S"},
        {"6", "b"},
        {"7", "T"},
        {"8", "B"},
        {"9", "g"},
        {"0", "o"}
    };

    public String convert(String text) {
        Map<String, String> map = new HashMap<String, String>();
        for (String[] pair : leet) {
            map.put(pair[0], pair[1]);
        }
        String result = "";
        for (int i = 0; i < text.length(); i++) {
            String letter = text.substring(i, i + 1);
            if (map.containsKey(letter)) {
                result += map.get(letter);
            } else {
                result += letter;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        josevalver jv = new josevalver();
        System.out.println("Enter text to convert: ");
        String text = System.console().readLine();
        System.out.println(jv.convert(text.toUpperCase()));
    }
}