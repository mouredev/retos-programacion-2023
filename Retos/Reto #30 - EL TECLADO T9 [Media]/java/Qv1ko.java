import java.util.HashMap;
import java.util.Map;

public class Qv1ko {

    public static void main(String[] args) {
        System.out.println(t9Translator("66-666-55-444-2"));
    }

    private static String t9Translator(String numbers) {

        String result = "";
        Map<String, String> t9Keyboard = new HashMap<String, String>();
        t9Keyboard.put("2", "A");
        t9Keyboard.put("3", "D");
        t9Keyboard.put("4", "G");
        t9Keyboard.put("5", "J");
        t9Keyboard.put("6", "M");
        t9Keyboard.put("7", "P");
        t9Keyboard.put("8", "T");
        t9Keyboard.put("9", "W");
        t9Keyboard.put("0", " ");
        t9Keyboard.put("22", "B");
        t9Keyboard.put("33", "E");
        t9Keyboard.put("44", "H");
        t9Keyboard.put("55", "K");
        t9Keyboard.put("66", "N");
        t9Keyboard.put("77", "Q");
        t9Keyboard.put("88", "U");
        t9Keyboard.put("99", "X");
        t9Keyboard.put("222", "C");
        t9Keyboard.put("333", "F");
        t9Keyboard.put("444", "I");
        t9Keyboard.put("555", "L");
        t9Keyboard.put("666", "O");
        t9Keyboard.put("777", "R");
        t9Keyboard.put("888", "V");
        t9Keyboard.put("999", "Y");
        t9Keyboard.put("7777", "S");
        t9Keyboard.put("9999", "Z");

        for(String str : numbers.split("-")) {
            result += (t9Keyboard.containsKey(str)) ? t9Keyboard.get(str) : "";
        }

        return result;

    }

}
