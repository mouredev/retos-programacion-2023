
import java.util.Map;
import java.util.HashMap;

public class chartypes {
    static Map<Character, String> dictionary = new HashMap<>();

    static void insertLetters(Map<Character, String> dictionary) {
        dictionary.put('a', "4");
        dictionary.put('b', "I3");
        dictionary.put('c', "[");
        dictionary.put('d', ")");
        dictionary.put('e', "3");
        dictionary.put('f', "|=");
        dictionary.put('g', "&");
        dictionary.put('h', "#");
        dictionary.put('i', "1");
        dictionary.put('j', "_|");
        dictionary.put('k', ">|");
        dictionary.put('l', "1");
        dictionary.put('m', "/\\/\\");
        dictionary.put('n', "^/");
        dictionary.put('o', "0");
        dictionary.put('p', "|*");
        dictionary.put('q', "(_,)");
        dictionary.put('r', "I2");
        dictionary.put('s', "5");
        dictionary.put('t', "7");
        dictionary.put('u', "(_)");
        dictionary.put('v', "\\/");
        dictionary.put('w', "\\/\\/");
        dictionary.put('x', "><");
        dictionary.put('y', "J");
        dictionary.put('z', "2");
        dictionary.put(' ', " ");

    }

    public static void main(String[] args) {
        insertLetters(dictionary);
        System.out.println(toLeet("a"));
        System.out.println(toLeet("leet"));
    }

    static StringBuilder toLeet(String text) {
        StringBuilder leetText = new StringBuilder();

        for (char letter : text.toCharArray())
            for (Map.Entry<Character, String> dictValue : dictionary.entrySet())
                if (dictValue.getKey() == letter)
                    leetText.append(dictValue.getValue());
        return leetText;
    }
}