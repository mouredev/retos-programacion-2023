import java.util.Random;
import java.util.Scanner;


/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */
public class Amartellram {


    private static String ALPHABET = "abcdefghijklmnñopqrstuvwxyz";
    private static String NUMBERS = "0123456789";
    private static String SYMBOLS = "<>?;'{}[]\\|!@#$%^&*()_+/-";


    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int length = 0;
        boolean withNumbers = false;
        boolean withSymbols = false;

        do {
            System.out.print("Ingresar longitud de la contraseña: ");
            length = scanner.nextInt();
        } while (length < 8 || length > 16);

        System.out.println("""
                Contraseña con números?
                1. Si
                2. No (defecto)
                """);
        System.out.print("Elección: ");
        withNumbers = scanner.nextInt() == 1;

        System.out.println("""
                Contraseña con símbolos?
                1. Si
                2. No (defecto)
                """);

        System.out.print("Elección: ");
        withSymbols = scanner.nextInt() == 1;

        System.out.println("Contraseña generada: " + generatePassword(length, withNumbers, withSymbols));


    }

    public static String generatePassword(int length, boolean withNumbers, boolean withSymbols) {

        StringBuilder electionsBuilder = new StringBuilder(ALPHABET);
        if(withNumbers)
            electionsBuilder.append(NUMBERS);
        if (withSymbols)
            electionsBuilder.append(SYMBOLS);

        String elections = electionsBuilder.toString();
        StringBuilder passwordBuilder = new StringBuilder();

        Random random = new Random();

        for(int i = 0 ; i < length; i++) {
            passwordBuilder.append(elections.charAt(random.nextInt(elections.length())));
        }

        return passwordBuilder.toString();
    }
}
