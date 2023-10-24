import java.util.Scanner;

public class rearalf {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        int passwordLength = 0;
        boolean capitalLetters = false;
        boolean numbers = false;
        boolean symbols = false;
        boolean isValidInput = false;

        do {
            System.out.print("Password must be between 8 and 16 in length: ");
            passwordLength = scanner.nextInt();
            if (passwordLength >= 8 && passwordLength <= 16) {
                isValidInput = true;
            } else
                System.out.println("Invalid password length. Please enter a value between 8 and 16.");
        } while (!isValidInput);
        System.out.println("");

        isValidInput = false;
        do {
            try {
                System.out.print("Include uppercase characters (true/false): ");
                capitalLetters = scanner.nextBoolean();
                isValidInput = true;
            } catch (Exception e) {
                System.out.println("Invalid input. Please enter 'true' or 'false'.");
                System.out.println("");
                scanner.nextLine();
            }
        } while (!isValidInput);
        System.out.println("");

        isValidInput = false;
        do {
            try {
                System.out.print("Include numbers (true/false): ");
                numbers = scanner.nextBoolean();
                isValidInput = true;
            } catch (Exception e) {
                System.out.println("Invalid input.Please enter 'true' or 'false'.");
                System.out.println("");
                scanner.nextLine();
            }
        } while (!isValidInput);
        System.out.println("");

        isValidInput = false;
        do {
            try {
                System.out.print("Include symbols (true/false): ");
                symbols = scanner.nextBoolean();
                isValidInput = true;
            } catch (Exception e) {
                System.out.println("Invalid input.Please enter 'true' or 'false'.");
                System.out.println("");
                scanner.nextLine();
            }
        } while (!isValidInput);
        System.out.println("");

        System.out.println("");
        System.out.println("The password is: " +
                GeneratePassword(passwordLength,
                        capitalLetters,
                        numbers,
                        symbols));
        System.out.println("");

        scanner.close();
    }

    public static String GeneratePassword(int passwordLength, boolean withUpperCase, boolean withNumbers,
            boolean withSymbols) {
        String lowerCaseChars = "abcdefghijklmnopqrstuvwxyz";
        String upperCaseChas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String numberChars = "0123456789";
        String symbolChars = "!@#$%^&*()-_+=";

        StringBuilder password = new StringBuilder();

        String availableChars = lowerCaseChars;

        if (withUpperCase)
            availableChars += upperCaseChas;

        if (withNumbers)
            availableChars += numberChars;

        if (withSymbols)
            availableChars += symbolChars;

        for (int i = 0; i < passwordLength; i++) {
            int randomIndex = (int) (Math.random() * availableChars.length());
            char randomChar = availableChars.charAt(randomIndex);
            password.append(randomChar);
        }

        return password.toString();
    }

}
