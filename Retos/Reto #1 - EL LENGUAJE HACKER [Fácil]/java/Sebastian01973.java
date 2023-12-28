import java.util.HashMap;
import java.util.Scanner;

/**
 * The type Sebastian 01973.
 */
public class Sebastian01973 {

    /**
     * The constant charArrayAlphanumeric.
     */
    public static final char[] charArrayAlphanumeric = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' '};

    /**
     * The constant strLenguajeLeet o lenguaje hacker
     */
    public static final String[] strLenguajeLeet = {"4", "|3", "[", ")", "3", "|=", "&", "#", "1", ",_|", ">|", "1", "/\\/\\", "^/",
            "0", "|*", "(_,)", "I2", "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2", "o", "L", "R", "E", "A", "S", "b", "T", "B", "g", " "};

    private HashMap<Character, String> dictionary; //Diccionario que contiene las transformaciones

    /**
     * Instantiates a new Sebastian 01973.
     */
    public Sebastian01973() {
        this.dictionary = new HashMap<>();
        for (int i = 0; i < charArrayAlphanumeric.length; i++) {
            dictionary.put(charArrayAlphanumeric[i],strLenguajeLeet[i]);
        }
    }

    /**
     * Text transformation string.
     * Metodo que convierte el texto en un codigo hacker
     * @param text the text
     * @return the string
     */
    public String textTransformation(String text){
        StringBuilder hackerText = new StringBuilder();
        char[] letters = text.toLowerCase().toCharArray();
        for (char letter : letters) {
            hackerText.append(dictionary.get(letter));
        }
        return hackerText.toString();
    }


    /**
     * The entry point of application.
     *
     * @param args the input arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese un texto");
        String text = scanner.nextLine(); //Obtener el texto
        Sebastian01973 sebastian01973 = new Sebastian01973();
        String newText = sebastian01973.textTransformation(text);
        System.out.println(newText);
    }
}
