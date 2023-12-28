import java.util.*;
public class santiw01 {

    HashMap <String, String> alphabet = new HashMap<String, String>();
    public static void main(String[] args) {
        String message = new String("santiw01").toLowerCase();
        santiw01 santiw01 = new santiw01();
        santiw01.fillAlphabet();
        System.out.println(santiw01.TransformString(message));
    }
        private String TransformString(String message) {
            String transformedMessage = new String("");
            for(int i = 0; i < message.length(); i++) {
                char character = message.charAt(i);
                transformedMessage += this.alphabet.get(character + "");
            }
            return transformedMessage;
        }

        private void fillAlphabet() {
            alphabet.put("a", "4");
            alphabet.put("b", "I3");
            alphabet.put("c", "[");
            alphabet.put("d", ")");
            alphabet.put("e", "3");
            alphabet.put("f", "|=");
            alphabet.put("g", "&");
            alphabet.put("h", "#");
            alphabet.put("i", "1");
            alphabet.put("j", ",_|");
            alphabet.put("k", ">|");
            alphabet.put("l", "1");
            alphabet.put("m", "/\\/\\");
            alphabet.put("n", "^/");
            alphabet.put("o", "0");
            alphabet.put("p", "|*");
            alphabet.put("q", "(_,)");
            alphabet.put("r", "I2");
            alphabet.put("s", "5");
            alphabet.put("t", "7");
            alphabet.put("u", "(_)");
            alphabet.put("v", "\\/");
            alphabet.put("w", "\\/\\/");
            alphabet.put("x", "><");
            alphabet.put("y", "j");
            alphabet.put("z", "2");
            alphabet.put("1", "L");
            alphabet.put("2", "R");
            alphabet.put("3", "E");
            alphabet.put("4", "A");
            alphabet.put("5", "S");
            alphabet.put("6", "b");
            alphabet.put("7", "T");
            alphabet.put("8", "B");
            alphabet.put("9", "g");
            alphabet.put("0", "o");
        }
}