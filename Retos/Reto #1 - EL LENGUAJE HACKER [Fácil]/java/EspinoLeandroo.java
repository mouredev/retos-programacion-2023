import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class EspinoLeandroo {

    Map<String, String> diccionary = new HashMap<>();

    public static void main(String[] args) {
        EspinoLeandroo espinoLeandroo = new EspinoLeandroo();

        espinoLeandroo.fillDiccionary();

        System.out.print(">> ");
        Scanner scanner = new Scanner(System.in);
        String message = scanner.nextLine();

        System.out.println( "<< " + espinoLeandroo.convert(message));

        scanner.close();
    }

    private String convert(String message) {
        message = message.toLowerCase();
        String newMessage = "";
        for (int i = 0; i < message.length(); i++) {
            char c = message.charAt(i);
            String ls = this.diccionary.get(c + "");
            if (ls != null) {
                newMessage += ls;
            } else {
                newMessage += c;
            }
        }
        return newMessage;
    }

    private void fillDiccionary() {
        diccionary.put("a", "4");
        diccionary.put("b", "I3");
        diccionary.put("c", "[");
        diccionary.put("d", ")");
        diccionary.put("e", "3");
        diccionary.put("f", "|=");
        diccionary.put("g", "&");
        diccionary.put("h", "#");
        diccionary.put("i", "1");
        diccionary.put("j", ",_|");
        diccionary.put("k", ">|");
        diccionary.put("l", "1");
        diccionary.put("m", "/\\/\\");
        diccionary.put("n", "^/");
        diccionary.put("o", "0");
        diccionary.put("p", "|*");
        diccionary.put("q", "(_,)");
        diccionary.put("r", "I2");
        diccionary.put("s", "5");
        diccionary.put("t", "7");
        diccionary.put("u", "(_)");
        diccionary.put("v", "\\/");
        diccionary.put("w", "\\/\\/");
        diccionary.put("x", "><");
        diccionary.put("y", "j");
        diccionary.put("z", "2");
        diccionary.put("1", "L");
        diccionary.put("2", "R");
        diccionary.put("3", "E");
        diccionary.put("4", "A");
        diccionary.put("5", "S");
        diccionary.put("6", "b");
        diccionary.put("7", "T");
        diccionary.put("8", "B");
        diccionary.put("9", "g");
        diccionary.put("0", "o");
    }

}