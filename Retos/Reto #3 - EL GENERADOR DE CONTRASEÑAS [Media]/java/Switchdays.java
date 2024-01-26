package com.retos;

/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

import java.security.SecureRandom;
        import java.util.ArrayList;
        import java.util.Collections;
        import java.util.List;
        import java.util.Scanner;

public class Reto3GeneradorPasswords {
    private static final String LOWERCASE_CHARACTERS = "abcdefghijklmnopqrstuvwxyz";
    private static final String UPPERCASE_CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static final String DIGITS = "0123456789";
    private static final String SYMBOLS = "!@#$%^&*()-_+=<>?/{}[]|";

    public static String generatePassword(int length, boolean useUppercase, boolean useDigits, boolean useSymbols) {
        StringBuilder validCharacters = new StringBuilder(LOWERCASE_CHARACTERS);

        if (useUppercase) {
            validCharacters.append(UPPERCASE_CHARACTERS);
        }

        if (useDigits) {
            validCharacters.append(DIGITS);
        }

        if (useSymbols) {
            validCharacters.append(SYMBOLS);
        }

        SecureRandom random = new SecureRandom();
        List<Character> passwordCharacters = new ArrayList<>();

        for (int i = 0; i < length; i++) {
            char randomChar = validCharacters.charAt(random.nextInt(validCharacters.length()));
            passwordCharacters.add(randomChar);
        }

        Collections.shuffle(passwordCharacters);

        StringBuilder password = new StringBuilder();
        for (char character : passwordCharacters) {
            password.append(character);
        }

        return password.toString();
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Longitud de la contraseña (entre 8 y 16): ");
        int length = scanner.nextInt();

        System.out.print("¿Incluir letras mayúsculas? (true/false): ");
        boolean useUppercase = scanner.nextBoolean();

        System.out.print("¿Incluir números? (true/false): ");
        boolean useDigits = scanner.nextBoolean();

        System.out.print("¿Incluir símbolos? (true/false): ");
        boolean useSymbols = scanner.nextBoolean();

        if (length >= 8 && length <= 16) {
            String password = generatePassword(length, useUppercase, useDigits, useSymbols);
            System.out.println("Contraseña generada: " + password);
        } else {
            System.out.println("La longitud de la contraseña debe estar entre 8 y 16 caracteres.");
        }
    }
}
