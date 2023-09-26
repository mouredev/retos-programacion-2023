import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.List;

public class Reto1 {

    public static void main(String[] args) {
        List<String> letters = List.of("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ");
        List<String> secrets = Arrays.asList("4", "I3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", "/\\/\\", "^/", "0", "|*", "(_,)", "I2", "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2", " ");

        InputStreamReader inputStreamReader = new InputStreamReader(System.in);
        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);

        System.out.println(": ");

        try {
            String input = bufferedReader.readLine();
            List<String> splitWord = Arrays.asList(input.toLowerCase().split(""));

            StringBuilder secretWord = new StringBuilder();

            splitWord.forEach(l -> {
                int position = letters.indexOf(l);
                String secretLetter = secrets.get(position);
                secretWord.append(secretLetter);
            });

            System.out.println(secretWord);

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}