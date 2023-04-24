import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Variables
        String longitud;
        boolean upperCase;
        boolean numbers;
        boolean symbols;
        String password = "";
        Scanner sc = new Scanner(System.in);

        // Pedimos los datos
        try {
            System.out.println("Introduce la longitud de la contraseña (entre 8 y 16): ");
            longitud = sc.nextLine();
            int longitudNum = Integer.parseInt(longitud);
            if (longitudNum >= 8 && longitudNum <= 16) {
                System.out.println("¿Quieres mayúsculas? (true/false)");
                upperCase = sc.nextBoolean();
                System.out.println("¿Quieres números? (true/false)");
                numbers = sc.nextBoolean();
                System.out.println("¿Quieres símbolos? (true/false)");
                symbols = sc.nextBoolean();

                // Generamos la contraseña
                password = generatePassword(longitudNum, upperCase, numbers, symbols);

            } else {
                System.out.println("La longitud debe estar entre 8 y 16");
            }

            System.out.println("La contraseña es: " + password);
        } catch (NumberFormatException ex) {
            System.out.println("Tienes que introducir un número");
        }catch (InputMismatchException ex) {
            System.out.println("Tienes que escribir true o false");
        }


    }

    private static String generatePassword(int longitudNum, boolean upperCase, boolean numbers, boolean symbols) {
        String password = "";
        String upperCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String lowerCaseLetters = "abcdefghijklmnopqrstuvwxyz";
        String numbersLetters = "0123456789";
        String symbolsLetters = "!#$%&/()=?¡¿";
        String allLetters = lowerCaseLetters;
        if (upperCase) {
            allLetters += upperCaseLetters;
        }
        if (numbers) {
            allLetters += numbersLetters;
        }
        if (symbols) {
            allLetters += symbolsLetters;
        }
        for (int i = 0; i < longitudNum; i++) {
            int random = (int) (Math.random() * allLetters.length());
            password += allLetters.charAt(random);
        }
        return password;
    }
}
