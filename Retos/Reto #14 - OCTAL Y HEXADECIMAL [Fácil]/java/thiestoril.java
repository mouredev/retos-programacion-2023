import java.util.Scanner;
import java.util.HashMap;


public class thiestoril {

    // Converts an integer to an octal number
    private static String intToOct(int number) {
        String octal = "";

        while (number != 0) {
            octal = (number % 8) + octal;
            number /= 8;
        }

        return octal;
    }

    // Converts an integer to a hexadecimal
    private static String intToHex(int number, HashMap <Integer, String> dic) {
        String hex = "";
        int aux;
        
        while (number != 0) {
            aux = number % 16;
            hex = (aux < 10) ? aux + hex : dic.get(aux) + hex;
            number /= 16;
        }

        return hex;
    }

    public static void main(String args[]) {

        // Get the input
        System.out.println("Insert a number:");

        Scanner scan = new Scanner(System.in);
        String input = scan.next();

        int number = Integer.parseInt(input);

        // Setup dictionary
        HashMap <Integer, String> dict = new HashMap <Integer, String>();
        dict.put(10, "A");
        dict.put(11, "B");
        dict.put(12, "C");
        dict.put(13, "D");
        dict.put(14, "E");
        dict.put(15, "F");

        // Convert to octal
        String octal = intToOct(number);

        // Convert to hex
        String hex = intToHex(number, dict);

        // Print the results
        System.out.println("Octal is: " + octal);
        System.out.println("Hexadecimal is: " + hex);
    }
}