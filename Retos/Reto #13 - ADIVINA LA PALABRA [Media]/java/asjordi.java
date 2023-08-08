import java.util.List;
import java.util.Random;
import java.util.Scanner;

public class GuessWord {

    public static void main(String[] args) {
        GuessWord g = new GuessWord(1);
        g.play();
    }

    private final Random r = new Random();
    private final List<String> listOfWords = List.of("java", "javascript", "python", "csharp", "nodejs", "mysql", "git", "github");
    private final String word;
    private int attempts = 3;

    public GuessWord(int attempts){
        if (attempts > 3) this.attempts = attempts;
        this.word = listOfWords.get(r.nextInt(listOfWords.size()));
    }

    public void play(){

        String hideWord = hideCharacters(this.word);
        boolean wordIsComplete = false;
        Scanner sc = new Scanner(System.in);

        System.out.println("Welcome to the word guessing game");

        while (!wordIsComplete) {
            if (this.attempts == 0) break;
            System.out.println("Remaining attempts: " + this.attempts);
            System.out.println("Guess the word --> " + hideWord);
            System.out.println("Enter a character or a full word!");
            String userInput = sc.nextLine();

            if (userInput.length() > 0){
                if (userInput.equals(this.word)){
                    System.out.println("You win!!\nThe word is: " + this.word);
                    wordIsComplete = true;
                } else if (this.word.contains(userInput)){
                    hideWord = searchMatches(this.word, hideWord, userInput);
                    if (hideWord.equals(this.word)){
                        System.out.println("You win!!\nThe word is: " + this.word);
                        wordIsComplete = true;
                        break;
                    }
                }
            }

            this.attempts--;
        }

        if (!wordIsComplete) System.out.println("You lost!!\nThe word is: " + this.word);

    }

    private String hideCharacters(String str){

        List<String> alphabet = List.of(
                "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
        );

        int limitHide = (str.length() * 60) / 100;
        int actualLength = 0;

        while (actualLength < limitHide){
            String letter = alphabet.get(r.nextInt(alphabet.size()));
            if (str.contains(letter)) {
                str = str.replace(letter, "_");
            }
            actualLength = str.length() - str.replace("_", "").length();
        }

        return str;

    }

    public String searchMatches(String originalWord, String hideWord, String letter){

        String[] originalWordArr = originalWord.split("");
        String[] hideWordArr = hideWord.split("");

        for (int i = 0; i < originalWordArr.length; i++) {
            if (originalWordArr[i].equals(letter)){
                hideWordArr[i] = letter;
            }
        }

        return String.join("", hideWordArr);

    }

}
