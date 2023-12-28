import java.util.*;

public class miguelex {

    private static String HackerEncode(String plainText) {

        Map<String, String> leetCode = new HashMap<String, String>();
        leetCode.put("a", "4");
        leetCode.put("b", "I3");
        leetCode.put("c", "[");
        leetCode.put("d", ")");
        leetCode.put("e", "3");
        leetCode.put("f", "|=");
        leetCode.put("g", "&");
        leetCode.put("h", "#");
        leetCode.put("i", "1");
        leetCode.put("j", ",_|");
        leetCode.put("k", ">|");
        leetCode.put("l", "1");
        leetCode.put("m", "/\\/\\");
        leetCode.put("n", "^/");
        leetCode.put("o", "0");
        leetCode.put("p", "|*");
        leetCode.put("q", "(_,)");
        leetCode.put("r", "I2");
        leetCode.put("s", "5");
        leetCode.put("t", "7");
        leetCode.put("u", "(_)");
        leetCode.put("v", "\\/");
        leetCode.put("w", "\\/\\/");
        leetCode.put("x", "><");
        leetCode.put("y", "j");
        leetCode.put("z", "2");
        leetCode.put("0", "o");
        leetCode.put("1", "L");
        leetCode.put("2", "R");
        leetCode.put("3", "E");
        leetCode.put("4", "A");
        leetCode.put("5", "S");
        leetCode.put("6", "b");
        leetCode.put("7", "T");
        leetCode.put("8", "B");
        leetCode.put("9", "g");

        String encryptedText = "";

        for (int i = 0; i < plainText.length(); i++) {
            String letter = plainText.substring(i, i + 1);
            if (leetCode.containsKey(letter.toLowerCase())) {
                encryptedText += leetCode.get(letter.toLowerCase());
            } else {
                encryptedText += letter;
            }
        }

        return encryptedText;
    }

    public static void main(String[] args) {
        System.out.println(HackerEncode("leet"));
        System.out.println(HackerEncode("Mi nombre es Miguelex"));
        System.out.println(HackerEncode("1234567890"));
        System.out.println(HackerEncode("Hola Mundo!! Esto es una_prueba con caracteres extrañ@s"));
    }
}