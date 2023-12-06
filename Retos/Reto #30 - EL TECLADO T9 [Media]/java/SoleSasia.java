import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        System.out.println(T9toText("44-666-555-2-0-3-33-888-7777-1111")); //HOLA DEVS!
    }

    public static String T9toText(String inputT9) {

        String[] inputT9Blocks = inputT9.split("-");

        if(!isCorrectFormat(inputT9Blocks)){
            return "Existen campos diferentes en un mismo bloque";
        };

        Map<String, String> T9Map = getT9Map();

        String text = "";
        for (String block : inputT9Blocks) {
            text += T9Map.get(block).toUpperCase();
        }

        return text;
    };

    private static boolean isCorrectFormat(String[] inputT9Blocks) {
        for (String block : inputT9Blocks) {
            if (block.length() > 1 && block.length() < 5) {
                char character = block.charAt(0);
                for (int i = 0; i < block.length(); i++) {
                    if (character != block.charAt(i)) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    private static Map<String, String> getT9Map() {
        Map<String, String> T9Map = new HashMap<>();

        T9Map.put("1", ",");
        T9Map.put("11", ".");
        T9Map.put("111", "?");
        T9Map.put("1111", "!");
        T9Map.put("2", "a");
        T9Map.put("22", "b");
        T9Map.put("222", "c");
        T9Map.put("3", "d");
        T9Map.put("33", "e");
        T9Map.put("333", "f");
        T9Map.put("4", "g");
        T9Map.put("44", "h");
        T9Map.put("444", "i");
        T9Map.put("5", "j");
        T9Map.put("55", "k");
        T9Map.put("555", "l");
        T9Map.put("6", "m");
        T9Map.put("66", "n");
        T9Map.put("666", "o");
        T9Map.put("7", "p");
        T9Map.put("77", "q");
        T9Map.put("777", "r");
        T9Map.put("7777", "s");
        T9Map.put("8", "t");
        T9Map.put("88", "u");
        T9Map.put("888", "v");
        T9Map.put("9", "w");
        T9Map.put("99", "x");
        T9Map.put("999", "y");
        T9Map.put("9999", "z");
        T9Map.put("0", " ");

        return T9Map;
    }
}
