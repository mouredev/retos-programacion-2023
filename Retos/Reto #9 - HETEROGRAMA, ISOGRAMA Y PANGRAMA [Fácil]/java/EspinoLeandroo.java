import java.util.HashSet;
import java.util.Set;

public class EspinoLeandroo {

    public static boolean isHeterogram(String text) {
        Set<Character> characters = new HashSet<>();
        for (char c : text.toCharArray()) {
            if (Character.isLetter(c)) {
                if (characters.contains(Character.toLowerCase(c))) {
                    return false;
                }
                characters.add(Character.toLowerCase(c));
            }
        }
        return true;
    }

    public static boolean isIsogram(String text) {
        Set<Character> characters = new HashSet<>();
        for (char c : text.toCharArray()) {
            if (Character.isLetter(c)) {
                if (characters.contains(Character.toLowerCase(c))) {
                    return false;
                }
                characters.add(Character.toLowerCase(c));
            }
        }
        return true;
    }

    public static boolean isPangram(String text) {
        Set<Character> characters = new HashSet<>();
        for (char c : text.toCharArray()) {
            if (Character.isLetter(c)) {
                characters.add(Character.toLowerCase(c));
            }
        }
        return characters.size() == 26; 
    }

    public static void main(String[] args) {
        String heterogramText = "murciélago";
        String isogramText = "mariposa";
        String pangramText = "The quick brown fox jumps over the lazy dog";

        System.out.println("Es heterograma: " + isHeterogram(heterogramText));
        System.out.println("Es isograma: " + isIsogram(isogramText));
        System.out.println("Es pangrama: " + isPangram(pangramText));
    }

    
}
