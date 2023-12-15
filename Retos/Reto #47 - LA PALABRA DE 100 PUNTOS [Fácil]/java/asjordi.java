import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Words {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Words w = new Words();
        int wordValue = 0;
        String word = "";
        System.out.println("Enter a word, the program ends if the word equals 100 points.");

        while (wordValue != 100) {
            word = sc.nextLine();
            wordValue = w.calculate(word);
            System.out.println("Value = " + wordValue);
        }

        System.out.println("Congratulations! The word " + word + " is equal to 100");
    }

    private final Map<Character, Integer> map;

    public Words() {
        this.map = new HashMap<>();
        loadCharacters();
    }

    public int calculate(String word){
        int sum = 0;

        for (char c : word.toLowerCase().toCharArray()) {
            if (this.map.containsKey(c)) sum += this.map.get(c);
        }

        return sum;
    }

    private void loadCharacters(){
        char[] alphabet = "abcdefghijklmnñopqrstuvwxyz".toCharArray();

        for (int i = 0; i < alphabet.length; i++) {
            this.map.put(alphabet[i], i + 1);
        }
    }

}
