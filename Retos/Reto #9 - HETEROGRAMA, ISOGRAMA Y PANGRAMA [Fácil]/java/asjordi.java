import java.util.*;

public class Words {

    public boolean isHeterogram(String str) {

        str = sanitizeString(str);
        HashSet<Character> letters = new HashSet<>();

        for (int i = 0; i < str.length(); i++) {
            if (letters.contains(str.charAt(i))) return false;
            letters.add(str.charAt(i));
        }

        return true;

    }

    public boolean isIsogram(String str) {

        str = sanitizeString(str);

        int ref = 0;
        boolean areEquals = true;
        HashMap<Character, Integer> words = new HashMap<>();

        for (int i = 0; i < str.length(); i++) {

            if (words.containsKey(str.charAt(i))) {
                int value = words.get(str.charAt(i));
                words.replace(str.charAt(i), value + 1);
                continue;
            }

            words.put(str.charAt(i), 1);
        }

        for (int value : words.values()) {
            if (ref == 0) {
                ref = value;
            } else if (ref != value) {
                areEquals = false;
            }
        }

        return areEquals;

    }

    public boolean isPangram(String str) {

        str = sanitizeString(str);

        HashSet<String> letters = new HashSet();

        for(int i = 0; i< str.length(); i++) {
            char l = str.charAt(i);
            if (Character.toString(l).matches("[a-z]"))
                letters.add(String.valueOf(l));
        }

        return letters.size() == 26;

    }

    public String sanitizeString(String str) {

        str = str.replace(" ", "")
                .replace("//d", "")
                .replace(".", "")
                .replace(",", "")
                .toLowerCase();

        return str;

    }

}
