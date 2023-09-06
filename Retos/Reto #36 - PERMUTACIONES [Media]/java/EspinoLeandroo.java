import java.util.ArrayList;
import java.util.List;

public class EspinoLeandroo {

    public static void main(String[] args) {
        String word = "Leandro";
        List<String> permutations = generatePermutations(word);
        for (String permutation : permutations) {
            System.out.println(permutation);
        }
    }

    public static List<String> generatePermutations(String word) {
        List<String> permutations = new ArrayList<>();
        generatePermutationsHelper(word.toCharArray(), 0, permutations);
        return permutations;
    }

    private static void generatePermutationsHelper(char[] word, int index, List<String> permutations) {
        if (index == word.length - 1) {
            permutations.add(new String(word));
        } else {
            for (int i = index; i < word.length; i++) {
                swap(word, index, i);
                generatePermutationsHelper(word, index + 1, permutations);
                swap(word, index, i); // Deshacer el intercambio para volver al estado original
            }
        }
    }

    private static void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
