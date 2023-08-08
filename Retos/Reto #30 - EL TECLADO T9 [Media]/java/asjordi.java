import java.util.HashMap;

public class Keyboard {

    public static String t9ToText(String str){
        if (str == null || str.isBlank()) throw new IllegalArgumentException("Invalid input");
        HashMap<Integer, String[]> keyboard = getKeyboard();
        String[] strArr = str.split("-");
        StringBuilder res = new StringBuilder();

        for (String s : strArr){
            int key = Integer.parseInt(Character.toString(s.charAt(0)));
            if (keyboard.containsKey(key)){
                int len = s.length() - 1;
                int lenKey = keyboard.get(key).length;
                if (len < lenKey) res.append(keyboard.get(key)[len]);
                else res.append(keyboard.get(key)[len % lenKey]);
            }
        }

        return res.toString().toUpperCase();
    }

    private static HashMap<Integer, String[]> getKeyboard(){
        HashMap<Integer, String[]> keyboard = new HashMap<>();
        keyboard.put(0, new String[]{" "});
        keyboard.put(1, new String[]{".", ",", "?", "!"});
        keyboard.put(2, new String[]{"a", "b", "c"});
        keyboard.put(3, new String[]{"d", "e", "f"});
        keyboard.put(4, new String[]{"g", "h", "i"});
        keyboard.put(5, new String[]{"j", "k", "l"});
        keyboard.put(6, new String[]{"m", "n", "o"});
        keyboard.put(7, new String[]{"p", "q", "r", "s"});
        keyboard.put(8, new String[]{"t", "u", "v"});
        keyboard.put(9, new String[]{"w", "x", "y", "z"});
        return keyboard;
    }
}
