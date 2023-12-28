import java.util.ArrayList;
import java.util.List;

public class Qv1ko {

    public static void main(String[] args) {

        permutations("sol");

    }

    private static void permutations(String word) {

        List<String> words = new ArrayList<String>();
        generatePermutation("", word, words);
        System.out.println(words.toString());

    }

    private static void generatePermutation(String prefix, String word, List<String> words) {

        if (word.length() == 0) {

            words.add(prefix);

        } else {

            for (int i = 0; i < word.length(); i++) {
                generatePermutation(prefix + word.charAt(i), word.substring(0, i) + word.substring(i + 1, word.length()), words);
            }

        }

    }

}
