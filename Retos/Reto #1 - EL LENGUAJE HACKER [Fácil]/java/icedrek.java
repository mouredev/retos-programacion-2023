import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        String input = "Hola mundo";
        System.out.println("salida: " + toLeet(input));
    }

    public static String toLeet(String input) {
        Map<Character, String> leetMap = new HashMap<>();
        leetMap.put('a', "4");
        leetMap.put('b', "13");
        leetMap.put('c', "[");
        leetMap.put('d', ")");
        leetMap.put('e', "3");
        leetMap.put('f', "|=");
        leetMap.put('g', "&");
        leetMap.put('h', "#");
        leetMap.put('i', "!");
        leetMap.put('j', ",_|");
        leetMap.put('k', ">|");
        leetMap.put('l', "1");
        leetMap.put('m', "/\\/\\");
        leetMap.put('n', "^/");
        leetMap.put('o', "0");
        leetMap.put('p', "|*");
        leetMap.put('q', "(_,)");
        leetMap.put('r', "I2");
        leetMap.put('s', "5");
        leetMap.put('t', "7");
        leetMap.put('u', "(_)");
        leetMap.put('v', "\\/");
        leetMap.put('w', "\\/\\/");
        leetMap.put('x', "><");
        leetMap.put('y', "j");
        leetMap.put('z', "2");
        leetMap.put('1', "L");
        leetMap.put('2', "R");
        leetMap.put('3', "E");
        leetMap.put('4', "A");
        leetMap.put('5', "S");
        leetMap.put('6', "b");
        leetMap.put('7', "T");
        leetMap.put('8', "B");
        leetMap.put('9', "g");
        leetMap.put('0', "o");

        input = input.toLowerCase();
        StringBuilder output = new StringBuilder();

        for (int i = 0; i < input.length(); i++) {
            char letter = input.charAt(i);

            if (leetMap.containsKey(letter)) {
                output.append(leetMap.get(letter));
            } else {
                output.append(letter);
            }
        }

        return output.toString();
    }
}
