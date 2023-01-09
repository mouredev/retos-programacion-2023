import java.util.Scanner;
import java.util.HashMap;

/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
 */
 
public class el_lenguaje_hacker {

    //Declare method translate. It receives only one String from for loop
    public static void translate(String character) {
        //Declare a HashMap and set values for each alphabet character
        HashMap<String, String> leetAlphabet = new HashMap<>();
        //Set all values for each alphabet character
        leetAlphabet.put("a", "4");
        leetAlphabet.put("b", "l3");
        leetAlphabet.put("c", "[");
        leetAlphabet.put("d", ")");
        leetAlphabet.put("e", "3");
        leetAlphabet.put("f", "|=");
        leetAlphabet.put("g", "&");
        leetAlphabet.put("h", "#");
        leetAlphabet.put("i", "1");
        leetAlphabet.put("j", ",_|");
        leetAlphabet.put("k", ">|");
        leetAlphabet.put("l", "1");
        leetAlphabet.put("m", "/\\/\\");
        leetAlphabet.put("n", "^/");
        leetAlphabet.put("o", "0");
        leetAlphabet.put("p", "|*");
        leetAlphabet.put("q", "(_,)");
        leetAlphabet.put("r", "l2");
        leetAlphabet.put("s", "5");
        leetAlphabet.put("t", "7");
        leetAlphabet.put("u", "(_)");
        leetAlphabet.put("v", "\\/");
        leetAlphabet.put("w", "\\/\\/");
        leetAlphabet.put("x", "><");
        leetAlphabet.put("y", "j");
        leetAlphabet.put("z", "2");
        leetAlphabet.put(" ", " ");
        leetAlphabet.put("1", "L");
        leetAlphabet.put("2", "R");
        leetAlphabet.put("3", "E");
        leetAlphabet.put("4", "A");
        leetAlphabet.put("5", "S");
        leetAlphabet.put("6", "b");
        leetAlphabet.put("7", "T");
        leetAlphabet.put("8", "B");
        leetAlphabet.put("9", "g");
        leetAlphabet.put("0", "o");
        //leetAlphabet.get is a method to find the assigned value depending on the provided key(character) 
        System.out.print(leetAlphabet.get(character));
    }

    public static void main(String[] args) {
        //Declare a new instance of the Scanner class using an InpuStream constructor
        Scanner userInput = new Scanner(System.in);
        //Pritn out a message to indicate the user to input a message
        System.out.println("Enter the message to convert");
        //Read the message from console and convert the message to lower case
        String userInputLowerCase = userInput.nextLine().toLowerCase();

        //Loop Through the user message
        for (int i = 0; i < userInputLowerCase.length(); i++) {
            //The loop sends each character to the translate method
            translate(userInputLowerCase.substring(i, i + 1));
        }
    }
}
