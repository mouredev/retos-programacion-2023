/*
 * Escribe un programa que reciba un texto y transforme lenguaje natural a
 * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
 *  se caracteriza por sustituir caracteres alfanuméricos.
 * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
 *   con el alfabeto y los números en "leet".
 *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
*/

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class estuardodev {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Ingresa el texto que deseas traducir a lenguaje hacker: ");
        String entrada = scanner.nextLine();

        if (entrada == null || entrada.isEmpty()) {
            System.out.println("El texto es nulo o incorrecto.");
        } else {
            lenguajeHacker(entrada);
        }
    }

    public static void lenguajeHacker(String texto) {
        Map<String, String> valoresHacker = new HashMap<>();
        valoresHacker.put("A", "4");
        valoresHacker.put("B", "I3");
        valoresHacker.put("C", "[");
        valoresHacker.put("D", ")");
        valoresHacker.put("E", "3");
        valoresHacker.put("F", "|=");
        valoresHacker.put("G", "&");
        valoresHacker.put("H", "#");
        valoresHacker.put("I", "1");
        valoresHacker.put("J", ",_|");
        valoresHacker.put("K", ">|");
        valoresHacker.put("L", "£");
        valoresHacker.put("M", "/\\/");
        valoresHacker.put("N", "^/");
        valoresHacker.put("O", "0");
        valoresHacker.put("P", "|*");
        valoresHacker.put("Q", "(_,)");
        valoresHacker.put("R", "I2");
        valoresHacker.put("S", "5");
        valoresHacker.put("T", "7");
        valoresHacker.put("U", "(_)");
        valoresHacker.put("V", "\\/");
        valoresHacker.put("W", "\\_:_/");
        valoresHacker.put("X", "><");
        valoresHacker.put("Y", "j");
        valoresHacker.put("Z", "2");
        valoresHacker.put("a", "@");
        valoresHacker.put("b", "!3");
        valoresHacker.put("c", "©");
        valoresHacker.put("d", "|}");
        valoresHacker.put("e", "ë");
        valoresHacker.put("f", "ph");
        valoresHacker.put("g", "gee");
        valoresHacker.put("h", ":-:");
        valoresHacker.put("i", "3y3");
        valoresHacker.put("j", "._]");
        valoresHacker.put("k", "|c");
        valoresHacker.put("l", "|");
        valoresHacker.put("m", "<\\/>");
        valoresHacker.put("n", "{\\}");
        valoresHacker.put("o", "oh");
        valoresHacker.put("p", "|°");
        valoresHacker.put("q", "0_");
        valoresHacker.put("r", "|-");
        valoresHacker.put("s", "ehs");
        valoresHacker.put("t", "']['");
        valoresHacker.put("u", "L|");
        valoresHacker.put("v", "\\|");
        valoresHacker.put("w", "(n)");
        valoresHacker.put("x", "?");
        valoresHacker.put("y", "`/");
        valoresHacker.put("z", "7_");
        valoresHacker.put("1", "L");
        valoresHacker.put("2", "R");
        valoresHacker.put("3", "E");
        valoresHacker.put("4", "A");
        valoresHacker.put("5", "S");
        valoresHacker.put("6", "G");
        valoresHacker.put("7", "T");
        valoresHacker.put("8", "B");
        valoresHacker.put("9", "q");
        valoresHacker.put("0", "o");

        for (String key : valoresHacker.keySet()) {
            texto = texto.replace(key, valoresHacker.get(key));
        }

        System.out.println(texto);
    }
}
