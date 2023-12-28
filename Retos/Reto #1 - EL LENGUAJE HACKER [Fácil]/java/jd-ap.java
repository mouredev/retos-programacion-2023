import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class LenguajeHacker {


    private static final Map<String, String> equivalents;
    static {
        equivalents = new HashMap<>();
        equivalents.put("a", "4");
        equivalents.put("b", "I3");
        equivalents.put("c", "[");
        equivalents.put("d", ")");
        equivalents.put("e", "3");
        equivalents.put("f", "|=");
        equivalents.put("g", "&");
        equivalents.put("h", "#");
        equivalents.put("i", "1");
        equivalents.put("j", ",_|");
        equivalents.put("k", ">|");
        equivalents.put("l", "1");
        equivalents.put("m", "^^");
        equivalents.put("n", "^/");
        equivalents.put("o", "0");
        equivalents.put("p", "|*");
        equivalents.put("q", "(_,)");
        equivalents.put("r", "I2");
        equivalents.put("s", "5");
        equivalents.put("t", "7");
        equivalents.put("u", "(_)");
        equivalents.put("v", "|/");
        equivalents.put("w", "2u");
        equivalents.put("x", "><");
        equivalents.put("y", "j");
        equivalents.put("z", "2");
        equivalents.put("1", "L");
        equivalents.put("2", "R");
        equivalents.put("3", "E");
        equivalents.put("4", "A");
        equivalents.put("5", "S");
        equivalents.put("6", "b");
        equivalents.put("7", "T");
        equivalents.put("8", "B");
        equivalents.put("9", "g");
        equivalents.put("0", "o");
    }
    
    private static void to1337(String input) {
        Arrays.stream(input.toLowerCase().split(""))
                .map(it -> equivalents.getOrDefault(it, it))
                .forEach(System.out::print);
    }

    public static void main(String[] args) {
        to1337("Leet");
    }
}