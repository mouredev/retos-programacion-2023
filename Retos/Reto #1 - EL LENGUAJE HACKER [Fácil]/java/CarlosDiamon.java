package github.carlosdiamon.controller;

import java.util.Scanner;

public class CarlosDiamon {
    /*
     * Escribe un programa que reciba un texto y transforme lenguaje natural a
     * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
     *  se caracteriza por sustituir caracteres alfanuméricos.
     * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/)
     *   con el alfabeto y los números en "leet".
     *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
     */

    private static final String ALPHABET = "abcdefghijklmnñopqrstuvwxy1234567890";
    private static final String[] ALPHABET_LEET =
            {"4", "I3", "[", "|)", "3", "|=", "&", "#", "1", ",_|", "<|", "1", "/\\/\\", "^/",
                    "~/", "0", "|*", "(_,)", "I2", "5", "7", "(_)", "\\/", "\\/\\/", "><", "j", "2",
                    "L", "R", "E", "A", "S", "B", "T", "B", "G", "O"};
    public static void main(String[] args) {



        Scanner scn = new Scanner(System.in);

        boolean session = true;

        do {

            System.out.println("/-/-/-MENU H4CK3R-/-/-/" +
                    "\n\t 1. transformar texto a leet" +
                    "\n\t 2. [ Salir ]");
            switch (scn.nextInt()) {
                case 1 -> {
                    System.out.print("\n*) Digita el texto a convertir (leet): ");
                    scn.nextLine(); // Vaciar Buffer
                    String text = scn.nextLine().toLowerCase();
                    System.out.println(returnLeet(text));
                }
                case 2 -> {
                    session = false;
                    System.out.println("Saliendo ...");
                }
                case default -> System.out.println("*) No existe esa opción, vuelva a intentarlo");
            }

        }while (session);


    }

    private static String returnLeet(String text) { // Leet Modo intermedio
        if (text.isEmpty()) return "";

        StringBuilder newText = new StringBuilder();

        for (int i = 0; i < text.length(); i++) {
            boolean matches = true;
            for (int j = 0; j < ALPHABET.length(); j++) {
                if (text.charAt(i) == ALPHABET.charAt(j)) {
                    newText.append(ALPHABET_LEET[j]);
                    matches = true; // Encontro el parecido
                    break;
                } else {
                    matches = false; // no parecido entre los caracteres de la lista
                }
            }
            if (!matches) newText.append(text.charAt(i)); // Concatenar el caracter no encontrado
        }

        return newText.toString();
    }

}
