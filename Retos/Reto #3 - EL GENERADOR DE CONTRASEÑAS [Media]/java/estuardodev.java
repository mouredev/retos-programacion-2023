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

public class estuardodev {
    static Random random = new Random();

    public static void main(String[] args) {
        System.out.println("------------------------------------------------------");
        System.out.println("--             Generador de Contraseñas             --");
        System.out.println("--              Hecho por @estuardodev              --");
        System.out.println("--                   -------------                  --");
        System.out.println("--        Antes debemos configurar unas cosas       --");
        System.out.println("------------------------------------------------------");

        Scanner scanner = new Scanner(System.in);

        System.out.print("\nIngresa la longitud de tu contraseña (Entre 8 y 16): ");
        int longitud = scanner.nextInt();
        if (longitud < 8 || longitud > 16) {
            System.out.println("Ingresa valores válidos por favor.");
            System.exit(0);
        }

        int conSinMayusculas = pregunta("mayúsculas");

        int conSinNumeros = pregunta("números");

        int conSinSimbolos = pregunta("símbolos");

        System.out.println("\nTu contraseña nueva es: " + generadorPassword(longitud, conSinMayusculas, conSinNumeros, conSinSimbolos)
                + "\n\nNUNCA COMPARTAS TU CONTRASEÑA CON NADIE.");

        scanner.close();
    }

    public static String generadorPassword(int longitud, int mayusculas, int numeros, int simbolos) {
        StringBuilder password = new StringBuilder();
        String pilar;

        while (password.length() < longitud) {
            if (mayusculas == 1) {
                pilar = String.valueOf(abecedario(true));
                password.append(pilar);
            } else {
                pilar = String.valueOf(abecedario(false));
                password.append(pilar);
            }
            if (numeros == 1) {
                pilar = String.valueOf(numeros());
                password.append(pilar);
            }
            if (simbolos == 1) {
                pilar = String.valueOf(caracteres());
                password.append(pilar);
            }
        }
        return password.toString();
    }

    public static int pregunta(String palabra) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("\n¿Deseas " + palabra + "?\n[1] - SI\n[0] - NO\nRespuesta: ");
        int dato = scanner.nextInt();
        if (dato < 0 || dato > 1) {
            System.out.println("Ingresa valores válidos por favor.");
            System.exit(0);
        }
        return dato;
    }

    public static char abecedario(boolean mayuscula) {
        String ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ";
        String abc = "abcdefghijklmnñopqrstuvwxyz";

        if (mayuscula) {
            String ABCabc = ABC + abc;
            return ABCabc.charAt(random.nextInt(ABCabc.length()));
        } else {
            return abc.charAt(random.nextInt(abc.length()));
        }
    }

    public static char numeros() {
        String nums = "0123456789";
        return nums.charAt(random.nextInt(nums.length()));
    }

    public static char caracteres() {
        String caracteres = "!{}+¿°!#%$%/&(&()/?¡_.,.-{+}¿/*-+.@";
        return caracteres.charAt(random.nextInt(caracteres.length()));
    }
}
