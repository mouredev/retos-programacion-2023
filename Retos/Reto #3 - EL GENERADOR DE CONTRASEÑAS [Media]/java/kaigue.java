/*
 * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
 * Podrás configurar generar contraseñas con los siguientes parámetros:
 * - Longitud: Entre 8 y 16.
 * - Con o sin letras mayúsculas.
 * - Con o sin números.
 * - Con o sin símbolos.
 * (Pudiendo combinar todos estos parámetros entre ellos)
 */

import java.util.Random;
import java.util.Scanner;

public class kaigue {
    public static void main(String[] args) {
        System.out.println("Password: " + GeneratePassword(true, true, true));
    }
    
    public static String GeneratePassword(boolean upper_cases, boolean numbers, boolean symbols) {
        String Password = "";
        try (Scanner input = new Scanner(System.in)) {
            Random random = new Random();
            int digits;
            System.out.print("Introduzca la cantidad de digitos deseada: ");
            do {
                digits = input.nextInt();
                if (digits < 8 || digits > 16) {
                    System.out.println("Debe tener entre 8 y 16 digitos");
                }
            } while (digits < 8 || digits > 16);
            
            String characters = "qwertyuiopasdfghjklñzxcvbnm";
            if (upper_cases) {
                characters += characters.toUpperCase();
            }
            if (numbers) {
                characters += "0123456789";
            }
            if (symbols) {
                characters += ",.-@/-_{+'#&?!|:;[*¿}]¡";
            }
            
            for (int i = 0; i < digits; i++) {
                //int random = (int) (4 * Math.random());
                int rand = random.nextInt(characters.length());
                Password += String.valueOf(characters.charAt(rand));  
            }
        }
        return Password;
    }
}
