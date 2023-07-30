import java.util.Scanner;
import java.util.stream.IntStream;


/**
    Transformar un texto o una frase al lenguaje hacker "leet"(1337)
 */
public class vandresca {

    private  static String[] normalAlphabet = {"A", "B", "C", "D", "E", "F", "G", "H", "I",
            "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
            "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "};

    private static String[] leetAlphabet = {"4", "|3", "[", "|)", "3", "|=", "6", "/-/","|", "_/",
            "|<", "1", "|v|", "|\\|", "0", "/>", "0,", "|2", "5", "7", "|_|", "\\/", "\\/\\/", "><","j", "2",
            "O", "L" ,"R", "E", "A", "S", "b", "T", "B", "g", " "};

    public static void main(String[] args) {

        System.out.println("Introduce un texto;");
        Scanner input = new Scanner(System.in);
        String text = input.nextLine().toUpperCase();
        input.close();
        String output = "";
        for(int i=0; i<text.length(); i++){
            output += translateCharacter(text.charAt(i));
        }

        System.out.println("La cadena resultante es: "+ output);
    }

    private static String translateCharacter(Character character){
        int index = IntStream.range(0, normalAlphabet.length)
                .filter(i ->normalAlphabet[i].equals(character.toString()))
                .findFirst()
                .orElse(-1);
        return leetAlphabet[index];
    }
}
