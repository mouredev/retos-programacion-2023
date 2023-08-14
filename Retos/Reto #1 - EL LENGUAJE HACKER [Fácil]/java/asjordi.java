import java.util.HashMap;

public class asjordi {

  public String leetConverter(String str) {

        String[] strArray = str.toUpperCase().split("");
        StringBuilder msg = new StringBuilder();

        HashMap<String, String> alphabet = new HashMap<>();
        alphabet.put("A", "4");
        alphabet.put("B", "I3");
        alphabet.put("C", "[");
        alphabet.put("D", ")");
        alphabet.put("E", "3");
        alphabet.put("F", "|=");
        alphabet.put("G", "&");
        alphabet.put("H", "#");
        alphabet.put("I", "1");
        alphabet.put("J", ",_|");
        alphabet.put("K", ">|");
        alphabet.put("L", "1");
        alphabet.put("M", "/\\/\\");
        alphabet.put("N", "^/");
        alphabet.put("O", "0");
        alphabet.put("P", "|*");
        alphabet.put("Q", "(_,)");
        alphabet.put("R", "I2");
        alphabet.put("S", "5");
        alphabet.put("T", "7");
        alphabet.put("U", "(_)");
        alphabet.put("V", "\\/");
        alphabet.put("W", "\\/\\/");
        alphabet.put("X", "><");
        alphabet.put("Y", "j");
        alphabet.put("Z", "2");
        alphabet.put(" ", " ");
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

        for (String s : strArray) {
            msg.append(alphabet.get(s));
        }

        return msg.toString();

    }

}
